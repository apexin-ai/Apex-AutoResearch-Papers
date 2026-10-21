# paper method rewrite framingB

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_method-rewrite-framingB_20260516T045212.log`
- **Structured JSON:** [`07328316fbf5741b1e3f.json`](../../sessions/07/07328316fbf5741b1e3f.json)

## Before a recorded user message

35 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
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
  "uuid": "7a91bcd5-7f04-418a-831e-c1416d4b1a28",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

I'll start by reading the three reference files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "9796ba00-85dd-4692-a64d-a6d2425d30d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179Q4QSq44AddHiugKnEtiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12321,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12321
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

_source line 4_

<details open><summary>🔧 Tool call — Read · `toolu_01XrXvSNgeJjJKUuxK5Fteti`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "87fde84e-4199-4534-a954-c00d69776b0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179Q4QSq44AddHiugKnEtiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12321,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12321
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

### Runtime record

_source line 5_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778924400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "37d0aea8-91d1-4c62-98e3-2bd805c65e32",
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7"
}
```

---

### Tool result

_source line 6 · 2026-05-16T04:52:20.997Z_

<details><summary>↩ Tool result · `toolu_01XrXvSNgeJjJKUuxK5Fteti`</summary>

```text
1	% Method — Draft v2
2	% Target: CoRL 2026
3	% Status: Updated 2026-05-16 — DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC/7-of-8). DIFF-M2, DIFF-M3 already applied.
4	% Note: Complements experimental_setup.md (Section 4). Some overlap in
5	%   diagnostic framework and factorial design is intentional—final paper
6	%   may merge or redistribute content between Sections 3 and 4.
7	
8	# 3. Methodology
9	
10	We present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.
11	
12	
13	## 3.1 Background: DreamerV3 and Variable-Rate Imagination
14	
15	### World-Model Actor-Critic
16	
17	DreamerV3 \citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:
18	
19	$$h_{t+1} = f_\theta(h_t, z_t, a_t), \quad \hat{z}_{t+1} \sim p_\theta(\cdot \mid h_{t+1})$$
20	
21	An actor $\pi_\psi$ selects actions and a critic $V_\xi$ estimates $\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\Delta t = 1$) and $H = 15$.
22	
23	### Temporal Abstraction via Variable-Rate Imagination
24	
25	Temporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.
26	
27	We introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:
28	
29	**Temporal step-size embedding.** An embedding $e_{\Delta t} \in \mathbb{R}^d$ conditions the RSSM transition on the step size:
30	
31	$$h_{t+\Delta t} = f_\theta(h_t, z_t, a_t, e_{\Delta t})$$
32	
33	We study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\Delta t$ values; the untrained and removed configurations serve as controls.
34	
35	**Temporal subsampling.** When enabled, the replay buffer stores both $\Delta t{=}1$ and $\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\Delta t{=}1$ transitions are used for world-model training.
36	
37	**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\Delta t{=}1$ (standard) or $\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.
38	
39	### Conditioning-Induced Value Overestimation (CIVO)
40	
41	When the RSSM predicts $\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\xi$ receives precise $\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.
42	
43	We term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \& Schuurmans' \citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\Delta t}$ and the RSSM's degraded fidelity at $\Delta t > 1$, not the policy's representational capacity.
44	
45	
46	## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio
47	
48	### Motivation
49	
50	Distinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\_001\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.
51	
52	### Definition
53	
54	**Value-evaluation ratio.** At training step $k$:
55	
56	$$r_k = \frac{\bar{v}_k}{\bar{R}_k}$$
57	
58	where $\bar{v}_k$ is the mean predicted value across imagined states and $\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.
59	
60	**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:
61	
62	$$\hat{r}_k = \frac{r_k^{\,\text{exp}}}{r_k^{\,\text{baseline}}}$$
63	
64	This removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.
65	
66	### Diagnostic Thresholds
67	
68	We calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:
69	
70	- **$\hat{r}_k > 1.5$ (at $k \geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\_embedding conditions exceed 1.5$\times$ at 35K+ steps (exp\_008d seed 1: 1.71$\times$@35K $\to$ 2.09$\times$@45K; exp\_009b seed 2: 1.62$\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\_008f seed 1 peak: 1.02$\times$@25K; exp\_009c seed 2 peak: 1.26$\times$@25K).
71	
72	- **$0.8 \leq \hat{r}_k \leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.
73	
74	- **$\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.
75	
76	**Temporal validity constraint.** The NVE threshold applies only at $k \geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\_009b at 25K shows NVE = 2.05$\times$ and exp\_008e\_v3 at 25K shows NVE = 1.93$\times$, both artifacts of the baseline's $r_{25\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.
77	
78	**Aggregate diagnostic power.** Evaluating the 1.5$\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\ref{tab:nve_sensitivity}). The single false positive is exp\_008e\_v3\_s2, which exhibits late-onset NVE = 3.78$\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \S3.3. At a stricter threshold of 1.7$\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).
79	
80	### Properties of the NVE Metric
81	
82	Two properties make NVE informative for detecting the CIVO:
83	
84	**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\_008d shows NVE = 1.71$\times$@35K $\to$ 2.09$\times$@45K $\to$ 4.12$\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\_008a, exp\_008f) show stable or declining NVE trajectories.
85	
86	**Collapse association.** Sustained NVE $>$ 1.5$\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\_008d seed 1: three consecutive checkpoints above 1.5$\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\_009b seed 2: 1.62$\times$@45K $\to$ 1.41$\times$@55K $\to$ 0.94$\times$@65K, declining) does not lead to collapse. This pattern is consistent with a "point of no return" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.
87	
88	
89	## 3.3 Causal Analysis Protocol
90	
91	### Design Rationale
92	
93	This is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.
94	
95	### Factorial Structure
96	
97	We vary three factors (temporal embedding type $\times$ subsampling $\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \S4 for the complete configuration matrix). Rather than filling all cells of the $3 \times 2 \times 2$ grid, we prioritize the comparisons most informative for causal isolation.
98	
99	### Causal Chain and Its Tests
100	
101	The causal chain under investigation is:
102	
103	$$\text{trained } e_{\Delta t} \;\xrightarrow{\text{Link 1}}\; \text{pathological NVE} \;\xrightarrow{\text{Link 2}}\; \text{actor exploitation} \;\xrightarrow{\text{Link 3}}\; \text{performance collapse}$$
104	
105	Each link is tested by a specific controlled comparison:
106	
107	**Link 1: Trained dt\_embedding $\to$ pathological overestimation.** The comparison between exp\_008d (trained dt\_embedding, $d{=}32$) and exp\_008f (removed dt\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\Delta t{=}2$ imagination). Exp\_008d exhibits accelerating NVE (1.71$\times$@35K $\to$ 2.09$\times$@45K), while exp\_008f remains in the normal range (0.73$\times$@35K $\to$ 0.83$\times$@45K). This is the primary causal evidence.
108	
109	**Link 2: Sustained overestimation $\to$ collapse (stochastic).** Multi-seed replication of exp\_008d reveals that the NVE $>$ 1.5$\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\_008d) shows sustained NVE $>$ 1.5$\times$ across three checkpoints and collapses; seed 2 (exp\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.
110	
111	**Link 3: Imagination $\Delta t$ as the critical variable.** Exp\_008e\_v3 uses a trained dt\_embedding (identical to exp\_008d and exp\_006) but restricts imagination rollouts to $\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\_008e\_v3, seed 1) with NVE = 0.80$\times$ (healthy). The contrast with exp\_006 (same trained dt\_embedding, subsample ON, $H{=}15$, but $\Delta t{=}2$ imagination $\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\Delta t > 1$ predictions during imagination.
112	
113	### 2$\times$2 Ablation Matrix
114	
115	To close the causal loop, we cross dt\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:
116	
117	| dt\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |
118	|:---:|:---:|:---:|:---:|:---:|
119	| Trained ($d{=}32$) | ON | 008d | 4.12$\times$@55K (sustained $\uparrow$) | CIVO $\to$ collapse |
120	| Trained ($d{=}32$) | OFF | 008a | 0.93$\times$@55K | Stable, 85\% baseline@105K |
121	| Frozen ($d{=}32$) | ON | 015b | 1.45$\times$@55K $\to$ 0.65$\times$@65K | Sub-threshold transient; gradient starvation collapse |
122	| Removed ($d{=}0$) | ON | 008f | $\leq$1.02$\times$ | No CIVO |
123	
124	Trained dt\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\_015b: peak 1.45$\times$@55K) that self-corrects to 0.65$\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\times$. The subsample-OFF condition (exp\_008a) confirms that a trained embedding without exposure to $\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.
125	
126	### Supporting Analyses
127	
128	**Horizon effect (C5).** Exp\_008c ($H{=}8$) vs. exp\_008a ($H{=}15$), both with untrained dt\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\_008a: 778@105K; exp\_008c: 241@65K plateau).
129	
130	**Temporal distance amplification (C4).** Exp\_006 ($\Delta t{=}2$, peak 485@35K $\to$ collapse) vs. exp\_007 ($\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\Delta t$, consistent with compounding RSSM prediction errors. Only two $\Delta t$ values are tested; we report the monotonic trend (dt=1 $\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.
131	
132	### RSSM Fidelity Analysis
133	
134	To ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\Delta t{=}1$ vs. $\Delta t{=}2$ across three conditions (exp\_rssm\_fidelity\_analysis):
135	
136	| Condition | $\Delta t{=}1$ obs MSE | $\Delta t{=}2$ obs MSE | Obs gap | $\Delta t{=}1$ rew MAE | $\Delta t{=}2$ rew MAE | Rew gap |
137	|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
138	| Baseline (exp\_001) | 13.49 | 27.50 | 2.04$\times$ | 0.0102 | 0.0159 | 1.56$\times$ |
139	| 008d (trained emb) | 41.31 | 53.67 | 1.30$\times$ | 0.0568 | 0.1579 | 2.78$\times$ |
140	| 008f (no emb) | 8.01 | 22.04 | 2.75$\times$ | 0.7469 | 0.7526 | 1.01$\times$ |
141	
142	Two patterns are diagnostically relevant:
143	
144	1. **Trained embedding enables differentiated but biased reward predictions.** In exp\_008d, the reward head produces sharply different predictions for $\Delta t{=}1$ vs. $\Delta t{=}2$ (reward gap 2.78$\times$), but these differentiated predictions rest on poor absolute state quality ($\Delta t{=}1$ obs MSE = 41.31, 3.1$\times$ baseline). The critic receives confident but systematically biased reward signals at $\Delta t{=}2$, fueling value overestimation.
145	
146	2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\_008f, the reward head cannot distinguish $\Delta t$ values (gap 1.01$\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\times$ baseline). Exp\_008f is therefore a *causal control* that confirms the dt\_embedding's role in overestimation, not a recommended configuration.
147	
148	**Caveat on obs gap ratios.** Exp\_008d's low obs gap ratio (1.30$\times$) is misleading---its $\Delta t{=}1$ absolute error is already 3.1$\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.
149	
150	### Gradient Decomposition of the Temporal Embedding
151	
152	To identify which loss component drives $e_{\Delta t}$'s learned representation, we decompose $\nabla_\theta e_{\Delta t}$ by loss term using \texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061).
153	
154	| Loss component | Gradient norm | Share (\%) |
155	|----------------|:---:|:---:|
156	| Observation decoders (orientations, velocity, height) | 1.505 | 93 |
157	| KL dynamics | 0.119 | 7 |
158	| Continuation head | $<$0.001 | $<$1 |
159	| Reward head | 0.000 | 0 |
160	
161	The temporal embedding receives 93\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). Three implications follow:
162	
163	1. **Exp\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.
164	
165	2. **$e_{\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.
166	
167	3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\% contribution from observation decoders. This motivates the full SGS design (exp\_018), which detaches $e_{\Delta t}$ from all non-KL gradient pathways.
168	
169	### Stop-Gradient Surgery: An Informative Negative (exp\_016e)
170	\label{sec:sgs_negative}
171	
172	The gradient decomposition above was motivated by a null result: exp\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\Delta t}$.
173	
174	**Configuration.** Exp\_016e replicates exp\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\Delta t}$, subsampling ON, $H{=}8$, $\Delta t{=}2$ imagination) with one modification: \texttt{reward\_dt\_emb\_detach=True}, which applies $\text{sg}(\cdot)$ to $e_{\Delta t}$ before the reward head during the backward pass.
175	
176	**Results.** Exp\_016e collapses in the same qualitative pattern as exp\_008d. Peak eval return reaches 326.7 at 75K (exp\_016e), then drops to 31.7 by 95K---a 90.3\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\times$ at 95K (exp\_016e). The timing difference relative to exp\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.
177	
178	**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\ 1 scalar reward) dominates the gradient signal to $e_{\Delta t}$ by two orders of magnitude.
179	
180	**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\% of the gradient flow to $e_{\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\_018) or by restructuring how $e_{\Delta t}$ interacts with the RSSM transition function.
181	
182	### Imagination Step Size as Causal Variable
183	
184	The factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:
185	
186	**$\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\_008e\_v3 uses the same trained dt\_embedding and multi-rate training data as exp\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\_008e\_v3, seed 1), 95\% of baseline (exp\_001\_baseline: 915.67@105K), with NVE = 0.80$\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\Delta t > 1$ predictions during imagination.
187	
188	**$\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\_008e\_v3\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\_008e\_v3\_s2), with NVE = 3.78$\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\_008e\_v3\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\_008d.
189	
190	**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:
191	
192	- *Pathway A (CIVO):* Trained dt\_embedding + $\Delta t{>}1$ imagination $\to$ value overestimation (NVE $\uparrow$) $\to$ actor over-exploitation (entropy $\downarrow$) $\to$ performance collapse. Observed in exp\_008d (seed 1) and exp\_009b (seed 2, transient).
193	
194	- *Pathway B (non-CIVO):* $\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\_008e\_v3\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.
195	
196	To rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\_009a), comparable to seed 1's 915.67 (exp\_001\_baseline). The collapse in exp\_008e\_v3\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.
197	
198	**Implication.** Restricting imagination to $\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "3c9e53b2-cfd0-4dce-8053-499e8cfea940",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md",
      "content": "% Method — Draft v2\n% Target: CoRL 2026\n% Status: Updated 2026-05-16 — DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC/7-of-8). DIFF-M2, DIFF-M3 already applied.\n% Note: Complements experimental_setup.md (Section 4). Some overlap in\n%   diagnostic framework and factorial design is intentional—final paper\n%   may merge or redistribute content between Sections 3 and 4.\n\n# 3. Methodology\n\nWe present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \\citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \\citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.\n\n\n## 3.1 Background: DreamerV3 and Variable-Rate Imagination\n\n### World-Model Actor-Critic\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:\n\n$$h_{t+1} = f_\\theta(h_t, z_t, a_t), \\quad \\hat{z}_{t+1} \\sim p_\\theta(\\cdot \\mid h_{t+1})$$\n\nAn actor $\\pi_\\psi$ selects actions and a critic $V_\\xi$ estimates $\\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\\Delta t = 1$) and $H = 15$.\n\n### Temporal Abstraction via Variable-Rate Imagination\n\nTemporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \\citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.\n\nWe introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:\n\n**Temporal step-size embedding.** An embedding $e_{\\Delta t} \\in \\mathbb{R}^d$ conditions the RSSM transition on the step size:\n\n$$h_{t+\\Delta t} = f_\\theta(h_t, z_t, a_t, e_{\\Delta t})$$\n\nWe study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\\Delta t$ values; the untrained and removed configurations serve as controls.\n\n**Temporal subsampling.** When enabled, the replay buffer stores both $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\\Delta t{=}1$ transitions are used for world-model training.\n\n**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\\Delta t{=}1$ (standard) or $\\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.\n\n### Conditioning-Induced Value Overestimation (CIVO)\n\nWhen the RSSM predicts $\\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\\xi$ receives precise $\\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.\n\nWe term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \\& Schuurmans' \\citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\\Delta t}$ and the RSSM's degraded fidelity at $\\Delta t > 1$, not the policy's representational capacity.\n\n\n## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio\n\n### Motivation\n\nDistinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\\_001\\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.\n\n### Definition\n\n**Value-evaluation ratio.** At training step $k$:\n\n$$r_k = \\frac{\\bar{v}_k}{\\bar{R}_k}$$\n\nwhere $\\bar{v}_k$ is the mean predicted value across imagined states and $\\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.\n\n**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:\n\n$$\\hat{r}_k = \\frac{r_k^{\\,\\text{exp}}}{r_k^{\\,\\text{baseline}}}$$\n\nThis removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.\n\n### Diagnostic Thresholds\n\nWe calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:\n\n- **$\\hat{r}_k > 1.5$ (at $k \\geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\\_embedding conditions exceed 1.5$\\times$ at 35K+ steps (exp\\_008d seed 1: 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K; exp\\_009b seed 2: 1.62$\\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\\_008f seed 1 peak: 1.02$\\times$@25K; exp\\_009c seed 2 peak: 1.26$\\times$@25K).\n\n- **$0.8 \\leq \\hat{r}_k \\leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.\n\n- **$\\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.\n\n**Temporal validity constraint.** The NVE threshold applies only at $k \\geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\\_009b at 25K shows NVE = 2.05$\\times$ and exp\\_008e\\_v3 at 25K shows NVE = 1.93$\\times$, both artifacts of the baseline's $r_{25\\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.\n\n**Aggregate diagnostic power.** Evaluating the 1.5$\\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\\ref{tab:nve_sensitivity}). The single false positive is exp\\_008e\\_v3\\_s2, which exhibits late-onset NVE = 3.78$\\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \\S3.3. At a stricter threshold of 1.7$\\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).\n\n### Properties of the NVE Metric\n\nTwo properties make NVE informative for detecting the CIVO:\n\n**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\\_008d shows NVE = 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K $\\to$ 4.12$\\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\\_008a, exp\\_008f) show stable or declining NVE trajectories.\n\n**Collapse association.** Sustained NVE $>$ 1.5$\\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\\_008d seed 1: three consecutive checkpoints above 1.5$\\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\\_009b seed 2: 1.62$\\times$@45K $\\to$ 1.41$\\times$@55K $\\to$ 0.94$\\times$@65K, declining) does not lead to collapse. This pattern is consistent with a \"point of no return\" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.\n\n\n## 3.3 Causal Analysis Protocol\n\n### Design Rationale\n\nThis is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.\n\n### Factorial Structure\n\nWe vary three factors (temporal embedding type $\\times$ subsampling $\\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \\S4 for the complete configuration matrix). Rather than filling all cells of the $3 \\times 2 \\times 2$ grid, we prioritize the comparisons most informative for causal isolation.\n\n### Causal Chain and Its Tests\n\nThe causal chain under investigation is:\n\n$$\\text{trained } e_{\\Delta t} \\;\\xrightarrow{\\text{Link 1}}\\; \\text{pathological NVE} \\;\\xrightarrow{\\text{Link 2}}\\; \\text{actor exploitation} \\;\\xrightarrow{\\text{Link 3}}\\; \\text{performance collapse}$$\n\nEach link is tested by a specific controlled comparison:\n\n**Link 1: Trained dt\\_embedding $\\to$ pathological overestimation.** The comparison between exp\\_008d (trained dt\\_embedding, $d{=}32$) and exp\\_008f (removed dt\\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\\Delta t{=}2$ imagination). Exp\\_008d exhibits accelerating NVE (1.71$\\times$@35K $\\to$ 2.09$\\times$@45K), while exp\\_008f remains in the normal range (0.73$\\times$@35K $\\to$ 0.83$\\times$@45K). This is the primary causal evidence.\n\n**Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.\n\n**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n### 2$\\times$2 Ablation Matrix\n\nTo close the causal loop, we cross dt\\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:\n\n| dt\\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |\n|:---:|:---:|:---:|:---:|:---:|\n| Trained ($d{=}32$) | ON | 008d | 4.12$\\times$@55K (sustained $\\uparrow$) | CIVO $\\to$ collapse |\n| Trained ($d{=}32$) | OFF | 008a | 0.93$\\times$@55K | Stable, 85\\% baseline@105K |\n| Frozen ($d{=}32$) | ON | 015b | 1.45$\\times$@55K $\\to$ 0.65$\\times$@65K | Sub-threshold transient; gradient starvation collapse |\n| Removed ($d{=}0$) | ON | 008f | $\\leq$1.02$\\times$ | No CIVO |\n\nTrained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.\n\n### Supporting Analyses\n\n**Horizon effect (C5).** Exp\\_008c ($H{=}8$) vs. exp\\_008a ($H{=}15$), both with untrained dt\\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\\_008a: 778@105K; exp\\_008c: 241@65K plateau).\n\n**Temporal distance amplification (C4).** Exp\\_006 ($\\Delta t{=}2$, peak 485@35K $\\to$ collapse) vs. exp\\_007 ($\\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\\Delta t$, consistent with compounding RSSM prediction errors. Only two $\\Delta t$ values are tested; we report the monotonic trend (dt=1 $\\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.\n\n### RSSM Fidelity Analysis\n\nTo ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\\Delta t{=}1$ vs. $\\Delta t{=}2$ across three conditions (exp\\_rssm\\_fidelity\\_analysis):\n\n| Condition | $\\Delta t{=}1$ obs MSE | $\\Delta t{=}2$ obs MSE | Obs gap | $\\Delta t{=}1$ rew MAE | $\\Delta t{=}2$ rew MAE | Rew gap |\n|-----------|:---:|:---:|:---:|:---:|:---:|:---:|\n| Baseline (exp\\_001) | 13.49 | 27.50 | 2.04$\\times$ | 0.0102 | 0.0159 | 1.56$\\times$ |\n| 008d (trained emb) | 41.31 | 53.67 | 1.30$\\times$ | 0.0568 | 0.1579 | 2.78$\\times$ |\n| 008f (no emb) | 8.01 | 22.04 | 2.75$\\times$ | 0.7469 | 0.7526 | 1.01$\\times$ |\n\nTwo patterns are diagnostically relevant:\n\n1. **Trained embedding enables differentiated but biased reward predictions.** In exp\\_008d, the reward head produces sharply different predictions for $\\Delta t{=}1$ vs. $\\Delta t{=}2$ (reward gap 2.78$\\times$), but these differentiated predictions rest on poor absolute state quality ($\\Delta t{=}1$ obs MSE = 41.31, 3.1$\\times$ baseline). The critic receives confident but systematically biased reward signals at $\\Delta t{=}2$, fueling value overestimation.\n\n2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\\_008f, the reward head cannot distinguish $\\Delta t$ values (gap 1.01$\\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\\times$ baseline). Exp\\_008f is therefore a *causal control* that confirms the dt\\_embedding's role in overestimation, not a recommended configuration.\n\n**Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.\n\n### Gradient Decomposition of the Temporal Embedding\n\nTo identify which loss component drives $e_{\\Delta t}$'s learned representation, we decompose $\\nabla_\\theta e_{\\Delta t}$ by loss term using \\texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061).\n\n| Loss component | Gradient norm | Share (\\%) |\n|----------------|:---:|:---:|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93 |\n| KL dynamics | 0.119 | 7 |\n| Continuation head | $<$0.001 | $<$1 |\n| Reward head | 0.000 | 0 |\n\nThe temporal embedding receives 93\\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). Three implications follow:\n\n1. **Exp\\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.\n\n2. **$e_{\\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.\n\n3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\\% contribution from observation decoders. This motivates the full SGS design (exp\\_018), which detaches $e_{\\Delta t}$ from all non-KL gradient pathways.\n\n### Stop-Gradient Surgery: An Informative Negative (exp\\_016e)\n\\label{sec:sgs_negative}\n\nThe gradient decomposition above was motivated by a null result: exp\\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\\Delta t}$.\n\n**Configuration.** Exp\\_016e replicates exp\\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\\Delta t}$, subsampling ON, $H{=}8$, $\\Delta t{=}2$ imagination) with one modification: \\texttt{reward\\_dt\\_emb\\_detach=True}, which applies $\\text{sg}(\\cdot)$ to $e_{\\Delta t}$ before the reward head during the backward pass.\n\n**Results.** Exp\\_016e collapses in the same qualitative pattern as exp\\_008d. Peak eval return reaches 326.7 at 75K (exp\\_016e), then drops to 31.7 by 95K---a 90.3\\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\\times$ at 95K (exp\\_016e). The timing difference relative to exp\\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.\n\n**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\\ 1 scalar reward) dominates the gradient signal to $e_{\\Delta t}$ by two orders of magnitude.\n\n**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\n### Imagination Step Size as Causal Variable\n\nThe factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:\n\n**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**$\\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\\_008e\\_v3\\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\\_008e\\_v3\\_s2), with NVE = 3.78$\\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\\_008e\\_v3\\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\\_008d.\n\n**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:\n\n- *Pathway A (CIVO):* Trained dt\\_embedding + $\\Delta t{>}1$ imagination $\\to$ value overestimation (NVE $\\uparrow$) $\\to$ actor over-exploitation (entropy $\\downarrow$) $\\to$ performance collapse. Observed in exp\\_008d (seed 1) and exp\\_009b (seed 2, transient).\n\n- *Pathway B (non-CIVO):* $\\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\\_008e\\_v3\\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.\n\nTo rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\\_009a), comparable to seed 1's 915.67 (exp\\_001\\_baseline). The collapse in exp\\_008e\\_v3\\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.\n\n**Implication.** Restricting imagination to $\\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.\n",
      "numLines": 199,
      "startLine": 1,
      "totalLines": 199
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019cf3yVBpGfgeb8wosDYg1Z`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "ae558152-825a-4bb2-a28d-ef0cc6d300ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179Q4QSq44AddHiugKnEtiZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12321,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12321
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

_source line 8 · 2026-05-16T04:52:21.378Z_

<details><summary>↩ Tool result · `toolu_019cf3yVBpGfgeb8wosDYg1Z`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "d40ca9b3-86ee-4c71-a9ae-b9fee97f30ec",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me read the other two reference files now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "eefbcd94-b169-44f9-b08c-b771863df11d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mzery3bFhg8U9AsVvaAsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7940,
      "cache_read_input_tokens": 24162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7940
      },
      "output_tokens": 18,
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

_source line 10_

Now let me read the other two reference files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "eb565f7e-1106-4d07-a3f6-8b9ac92f5c49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mzery3bFhg8U9AsVvaAsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7940,
      "cache_read_input_tokens": 24162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7940
      },
      "output_tokens": 18,
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Jkz2T3Y5vATtf5KuA9jjtp`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "c92b0a5d-48d2-4e19-8a4f-dd87178f1312",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mzery3bFhg8U9AsVvaAsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7940,
      "cache_read_input_tokens": 24162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7940
      },
      "output_tokens": 18,
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

_source line 12 · 2026-05-16T04:52:26.026Z_

<details><summary>↩ Tool result · `toolu_01Jkz2T3Y5vATtf5KuA9jjtp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\n\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\n\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\n\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\n\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\n\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\n\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\n\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\n\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\n\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\"point of no return\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\n\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\n\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\"eliminates\\\" 改为 \\\"significantly delays and reduces\\\"。推荐方案仍是 008e_v3（C6）**。\\n\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\n\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\n|-------|------------|------------|---------|---------------|---------------|------------|\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\n\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\n\\n**dt_emb Gradient Decomposition (D061)**\\n\\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\\n\\n| Source | Grad Norm | Fraction |\\n|--------|-----------|----------|\\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\\n| KL dynamics | 0.119 | 7% |\\n| Cont head | ~0 (included in decoder total) | <1% |\\n| **Reward head** | **0.000** | **0%** |\\n| **Total** | **1.624** | **100%** |\\n\\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。\\n\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\n\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\n\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\n\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\\n\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\n\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\n\\n### C4: Longer dt amplifies the problem\\n\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\n\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\n\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\n\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\n\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\n\\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\\n\\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\\n\\n原假设\\\"dt=1 imagination = practical mitigation\\\"被**否证**。跨 seed 数据：\\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\\n- **独立 seed 崩溃率: 1/2 (50%)**\\n\\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\\n\\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\\n\\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\\n\\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\\n|------|---------------------|---------------------|\\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\\n\\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\\n\\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \\\"seed 2 本身不稳定\\\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\\n\\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\\n|------|-------------------|------------|------|\\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\\n\\n**C6 最终状态: PARTIALLY FALSIFIED**\\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\\n- 崩溃是配置导致的，不是 seed 特异性\\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\\n\\n**论文表述建议**: \\\"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\\\"\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\\n\\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\\n\\n---\\n\\n## Story Arc\\n\\n### 1. Introduction\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\\n\\n### 2. Background & Related Work\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\n- World-model RL (Dreamer family, IRIS, TWM)\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\\n\\n### 3. Methodology\\n- DreamerV3 as base architecture\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\n\\n### 4. Results\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\"smoking gun\\\" comparison (008c vs 008d)\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\n- **Finding 4**: Longer dt amplifies (C4)\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\\n\\n### 5. Discussion\\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\\n\\n### 6. Implications for Future Work\\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\\n- Need for diagnostic methodology in temporal abstraction research\\n\\n---\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Limited to one environment / one base algorithm\\\"\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\n\\n### R2: \\\"No proposed solution — what's the actionable takeaway?\\\"\\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\\n\\n### R3: \\\"Value/eval ratio is a crude proxy for overestimation\\\"\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\n\\n### R4: \\\"The factorial design is incomplete — missing cells in the grid\\\"\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\n\\n### R5: \\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\"\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\\n\\n### R6: \\\"All results from a single seed — how robust are the conclusions?\\\"\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\n\\n### R7: \\\"The factorial design confounds dt_embedding training with training data composition\\\"\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\\n\\n### R8: \\\"008f reward prediction degradation undermines the causal control\\\"\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\"去掉 dt_embedding → 不崩塌\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\n\\n---\\n\\n## Experiment Coverage Assessment\\n\\n| Claim | Evidence Status | Gaps |\\n|-------|----------------|------|\\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\\n\\n### Priority Actions Before Submission\\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \\\"multiple vulnerability pathways\\\" (CIVO Pathway A + non-CIVO Pathway B)\\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。\\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\\n\\n---\\n\\n## Key Figures (Planned)\\n\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\\n\", \"total_chars\": 33549, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "1ba9646a-9baf-44a7-aaac-072ddb65b035",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\\\n\\\\n## Title Candidates\\\\n\\\\n1. **\\\\\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\\\\\"**\\\\n2. ~~**\\\\\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\\\\\"**~~ (deprecated — \\\\\\\"delusional critic\\\\\\\" conflicts with Lu et al. 2018)\\\\n3. **\\\\\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\\\\\"** ← preferred after D037 terminology decision\\\\n4. **\\\\\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\\\\\"**\\\\n\\\\n**⚠️ D037 术语决定**: \\\\\\\"delusional critic\\\\\\\" → **\\\\\\\"conditioning-induced value overestimation\\\\\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\\\\\"delusional critic\\\\\\\" → \\\\\\\"conditioning-induced value overestimation\\\\\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\\\n\\\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\\\\\"known failure class 的 specific instance\\\\\\\" 升级为 \\\\\\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\\\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\\\n\\\\n## Venue\\\\n\\\\n**CoRL 2026** — Deadline: 2026-05-29\\\\n\\\\n## Narrative Positioning\\\\n\\\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\\\n\\\\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\\\n\\\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\\\n\\\\n---\\\\n\\\\n## Core Claims\\\\n\\\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\\\n\\\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\\\n\\\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\\\n\\\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\\\n\\\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\\\n\\\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\\\n\\\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\\\n\\\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\\\n\\\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\\\\\"point of no return\\\\\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\\\n\\\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\\\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\\\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\\\n\\\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\\\\\"eliminates\\\\\\\" 改为 \\\\\\\"significantly delays and reduces\\\\\\\"。推荐方案仍是 008e_v3（C6）**。\\\\n\\\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\\\n\\\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\\\n|-------|------------|------------|---------|---------------|---------------|------------|\\\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\\\n\\\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\\\n\\\\n**dt_emb Gradient Decomposition (D061)**\\\\n\\\\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\\\\n\\\\n| Source | Grad Norm | Fraction |\\\\n|--------|-----------|----------|\\\\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\\\\n| KL dynamics | 0.119 | 7% |\\\\n| Cont head | ~0 (included in decoder total) | <1% |\\\\n| **Reward head** | **0.000** | **0%** |\\\\n| **Total** | **1.624** | **100%** |\\\\n\\\\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。\\\\n\\\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\\\n\\\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\\\n\\\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\\\n\\\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\\\\n\\\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\\\n\\\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\\\n\\\\n### C4: Longer dt amplifies the problem\\\\n\\\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\\\n\\\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\\\n\\\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\\\n\\\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\\\n\\\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\\\n\\\\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\\\\n\\\\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\\\\n\\\\n原假设\\\\\\\"dt=1 imagination = practical mitigation\\\\\\\"被**否证**。跨 seed 数据：\\\\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\\\\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\\\\n- **独立 seed 崩溃率: 1/2 (50%)**\\\\n\\\\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\\\\n\\\\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\\\\n\\\\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\\\\n\\\\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\\\\n|------|---------------------|---------------------|\\\\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\\\\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\\\\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\\\\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\\\\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\\\\n\\\\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\\\\n\\\\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \\\\\\\"seed 2 本身不稳定\\\\\\\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\\\\n\\\\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\\\\n|------|-------------------|------------|------|\\\\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\\\\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\\\\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\\\\n\\\\n**C6 最终状态: PARTIALLY FALSIFIED**\\\\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\\\\n- 崩溃是配置导致的，不是 seed 特异性\\\\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\\\\n\\\\n**论文表述建议**: \\\\\\\"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\\\\\\\"\\\\n\\\\n| Evidence | Experiment | Key Metric |\\\\n|----------|-----------|------------|\\\\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\\\\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\\\\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\\\\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\\\\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\\\\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\\\\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\\\\n\\\\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\\\\n\\\\n---\\\\n\\\\n## Story Arc\\\\n\\\\n### 1. Introduction\\\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\\\\n\\\\n### 2. Background & Related Work\\\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\\\n- World-model RL (Dreamer family, IRIS, TWM)\\\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\\\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\\\\n\\\\n### 3. Methodology\\\\n- DreamerV3 as base architecture\\\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\\\n\\\\n### 4. Results\\\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\\\\\"smoking gun\\\\\\\" comparison (008c vs 008d)\\\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\\\n- **Finding 4**: Longer dt amplifies (C4)\\\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\\\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\\\\n\\\\n### 5. Discussion\\\\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\\\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\\\\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\\\\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\\\\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\\\\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\\\\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\\\\n\\\\n### 6. Implications for Future Work\\\\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\\\\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\\\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\\\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\\\\n- Need for diagnostic methodology in temporal abstraction research\\\\n\\\\n---\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### R1: \\\\\\\"Limited to one environment / one base algorithm\\\\\\\"\\\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\\\n\\\\n### R2: \\\\\\\"No proposed solution — what's the actionable takeaway?\\\\\\\"\\\\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\\\\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\\\\n\\\\n### R3: \\\\\\\"Value/eval ratio is a crude proxy for overestimation\\\\\\\"\\\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\\\n\\\\n### R4: \\\\\\\"The factorial design is incomplete — missing cells in the grid\\\\\\\"\\\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\\\n\\\\n### R5: \\\\\\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\\\\\"\\\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\\\\n\\\\n### R6: \\\\\\\"All results from a single seed — how robust are the conclusions?\\\\\\\"\\\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\\\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\\\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\\\n\\\\n### R7: \\\\\\\"The factorial design confounds dt_embedding training with training data composition\\\\\\\"\\\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\\\\n\\\\n### R8: \\\\\\\"008f reward prediction degradation undermines the causal control\\\\\\\"\\\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\\\\\"去掉 dt_embedding → 不崩塌\\\\\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\\\n\\\\n---\\\\n\\\\n## Experiment Coverage Assessment\\\\n\\\\n| Claim | Evidence Status | Gaps |\\\\n|-------|----------------|------|\\\\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\\\\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\\\\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\\\\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\\\\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\\\\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\\\\n\\\\n### Priority Actions Before Submission\\\\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\\\\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\\\\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\\\\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\\\\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\\\\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \\\\\\\"multiple vulnerability pathways\\\\\\\" (CIVO Pathway A + non-CIVO Pathway B)\\\\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。\\\\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\\\\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\\\\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\\\\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\\\\n\\\\n---\\\\n\\\\n## Key Figures (Planned)\\\\n\\\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\\\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\\\\n\\\", \\\"total_chars\\\": 33549, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**CoRL 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.\\n\\nWe scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.\\n\\n---\\n\\n## Core Claims\\n\\n### C1: Variable-rate imagination in DreamerV3 consistently degrades performance\\n\\nTemporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |\\n| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |\\n| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |\\n\\n**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.\\n\\n### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk\\n\\n**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**\\n\\nThe trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:\\n\\n- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)\\n- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)\\n- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb\\n\\n**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。\\n\\n**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a \\\"point of no return\\\" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).\\n\\nThe trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |\\n| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |\\n| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |\\n| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |\\n| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |\\n| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |\\n| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |\\n| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**dt_emb 的 93% 梯度来自 observation decoders（orientations/velocity/height），7% 来自 KL dynamics，reward=0。** |\\n| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |\\n\\n**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 \\\"eliminates\\\" 改为 \\\"significantly delays and reduces\\\"。推荐方案仍是 008e_v3（C6）**。\\n\\n**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**\\n\\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\\n|-------|------------|------------|---------|---------------|---------------|------------|\\n| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |\\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |\\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |\\n\\n**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。\\n\\n**dt_emb Gradient Decomposition (D061)**\\n\\n梯度验证（torch.autograd.grad analysis, commit 5fc8e49）揭示 dt_emb.weight 的梯度来源分布：\\n\\n| Source | Grad Norm | Fraction |\\n|--------|-----------|----------|\\n| Observation decoders (orientations, velocity, height) | 1.505 | 93% |\\n| KL dynamics | 0.119 | 7% |\\n| Cont head | ~0 (included in decoder total) | <1% |\\n| **Reward head** | **0.000** | **0%** |\\n| **Total** | **1.624** | **100%** |\\n\\n这意味着：(1) 016e 的 reward_dt_emb_detach 是 no-op——detach 了一个不存在的梯度通路；(2) dt_emb 的训练几乎完全由 observation reconstruction loss 驱动；(3) Full-SGS（exp_018）移除 observation decoder 梯度后仅保留 7% KL 梯度，是真正的 gradient-level intervention。\\n\\n**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.\\n\\n### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance\\n\\nWhen dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |\\n| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |\\n| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |\\n| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |\\n| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |\\n\\n**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.\\n\\n**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).\\n\\n**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.\\n\\n### C4: Longer dt amplifies the problem\\n\\nIncreasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |\\n| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |\\n| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |\\n\\n**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.\\n\\n### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause\\n\\nSubsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |\\n| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |\\n| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |\\n| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |\\n| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |\\n\\n**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.\\n\\n### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself\\n\\n**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。\\n\\n原假设\\\"dt=1 imagination = practical mitigation\\\"被**否证**。跨 seed 数据：\\n- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）\\n- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）\\n- **独立 seed 崩溃率: 1/2 (50%)**\\n\\n对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。\\n\\n**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**\\n\\nReviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：\\n\\n| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |\\n|------|---------------------|---------------------|\\n| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |\\n| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |\\n| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |\\n| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |\\n| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |\\n\\n**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。\\n\\n**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 \\\"seed 2 本身不稳定\\\" 假说。**008e_v3_s2 的崩溃是配置导致的**。\\n\\n| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |\\n|------|-------------------|------------|------|\\n| 85K | 618.7 | 715.2 | 008e_v3 略高 |\\n| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |\\n| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |\\n\\n**C6 最终状态: PARTIALLY FALSIFIED**\\n- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）\\n- 崩溃是配置导致的，不是 seed 特异性\\n- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性\\n\\n**论文表述建议**: \\\"Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop.\\\"\\n\\n| Evidence | Experiment | Key Metric |\\n|----------|-----------|------------|\\n| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |\\n| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |\\n| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |\\n| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |\\n| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |\\n| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |\\n| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |\\n\\n**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。\\n\\n---\\n\\n## Story Arc\\n\\n### 1. Introduction\\n- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)\\n- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction\\n- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?\\n- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop\\n\\n### 2. Background & Related Work\\n- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)\\n- World-model RL (Dreamer family, IRIS, TWM)\\n- Variable-rate planning in world models (few prior works, mostly positive framing)\\n- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)\\n\\n### 3. Methodology\\n- DreamerV3 as base architecture\\n- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating\\n- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines\\n- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves\\n\\n### 4. Results\\n- **Finding 1**: All dt>1 configurations degrade (C1)\\n- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the \\\"smoking gun\\\" comparison (008c vs 008d)\\n- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)\\n- **Finding 4**: Longer dt amplifies (C4)\\n- **Finding 5**: Horizon/subsample effects are secondary (C5)\\n- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)\\n\\n### 5. Discussion\\n- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)\\n- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x) — trained dt_emb 让 reward head 在 dt=2 时产生系统性偏差，这是 critic 被误导的直接来源\\n- 008f 的 reward 退化 trade-off：去掉 dt_embedding 避免崩塌但牺牲 reward 预测质量\\n- **D040: Multiple vulnerability pathways**: 008e_v3_s2 在 dt=1 imagination 下崩溃 (nve=3.78x@105K)，但机制与 008d 的 CIVO 不同：008d = value explosion → eval decline → entropy ↓；008e_v3_s2 = eval crash → value stable → entropy ↑。009a baseline s2 稳定排除 seed 脆弱。Trained dt_embedding creates vulnerability through multiple pathways: Pathway A (CIVO, value-driven) requires dt>1 imagination; Pathway B (non-CIVO policy instability, eval-driven) operates independently of imagination dt\\n- Connection to existing theory: non-delusional Q-learning (Lu et al., 2018), model exploitation in MBRL\\n- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)\\n- **D032: Value self-correction mechanism (009b)**: 009b (008d seed 2) demonstrates that pathological overestimation (nve>1.5x) is not always irreversible. Value peaked at 110.9@65K then monotonically self-corrected to 67.3@105K, while eval simultaneously improved (172→268). Hypothesized mechanism: when the critic's overestimation does not yet dominate the actor's gradient signal (transient vs sustained nve>1.5x), the actor can still learn from real environment returns, creating a corrective force. In 008d seed 1, the sustained overestimation (3 consecutive checkpoints >1.5x at 35K+) overwhelmed this correction. The bifurcation likely depends on early training stochasticity — initialization and data sampling order determine whether the overestimation feedback loop locks in before correction can take hold (consistent with primacy bias in MBRL, Qiao et al. 2023; early outlier runs, Bjorck et al. 2022). This makes nve>1.5x a **necessary condition** for collapse but not sufficient — the temporal persistence of overestimation is the second gate.\\n\\n### 6. Implications for Future Work\\n- **D038 update**: dt=1 imagination is NOT sufficient — trained dt_embedding in critic is the fundamental vulnerability, regardless of imagination strategy\\n- Don't use trained dt_embedding for temporal conditioning in imagination-based actor-critic training without safeguards (TAWM shows this works in MPC — the vulnerability is specific to imagination-based training)\\n- RSSM prediction quality must improve before variable-rate imagination is viable\\n- Potential safeguards: (a) ~~detach dt_embedding gradients from reward head~~ **架构层面无效（reward gradient = 0 by design）。梯度分解揭示 dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward 贡献为 0。真正的干预目标是 observation decoder→dt_emb 梯度通路（Full-SGS, exp_018 planned）。**, (b) stop-gradient on dt>1 critic targets, (c) pessimistic value ensemble for dt>1 transitions, (d) uncertainty-gated truncation\\n- Need for diagnostic methodology in temporal abstraction research\\n\\n---\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Limited to one environment / one base algorithm\\\"\\n**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.\\n**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.\\n\\n### R2: \\\"No proposed solution — what's the actionable takeaway?\\\"\\n**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.\\n**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).\\n\\n### R3: \\\"Value/eval ratio is a crude proxy for overestimation\\\"\\n**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.\\n**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.\\n\\n### R4: \\\"The factorial design is incomplete — missing cells in the grid\\\"\\n**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.\\n**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.\\n\\n### R5: \\\"Novelty concern — model exploitation / value overestimation in MBRL is well-known\\\"\\n**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.\\n\\n### R6: \\\"All results from a single seed — how robust are the conclusions?\\\"\\n**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.\\n**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.\\n**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.\\n\\n### R7: \\\"The factorial design confounds dt_embedding training with training data composition\\\"\\n**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).\\n**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.\\n\\n### R8: \\\"008f reward prediction degradation undermines the causal control\\\"\\n**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是\\\"去掉 dt_embedding → 不崩塌\\\"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。\\n**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。\\n\\n---\\n\\n## Experiment Coverage Assessment\\n\\n| Claim | Evidence Status | Gaps |\\n|-------|----------------|------|\\n| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |\\n| C2 (reliable pathological overestimation) | ⚠️ Moderate-strong (D032) — nve>1.5x threshold: 4/4 perfect separation (trained 2/2 exceed, untrained 0/2 exceed). Collapse stochastic: 1/2 trained seeds. Causal direction unambiguous. | 009e (008d seed 1) to narrow collapse probability; 009f (008f seed 1) for third untrained seed; 009c→200K |\\n| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |\\n| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |\\n| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |\\n| C6 (dt=1 imag as mitigation) | ⚠️ **D040: PARTIALLY FALSIFIED** — s2 collapsed (nve=3.78x) but via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable → config-caused. **Repositioned**: trained dt_embedding creates multiple vulnerability pathways; dt=1 imagination eliminates CIVO pathway but not policy instability pathway. Onset delay ~70K steps is a positive finding. | Need s3-s4 to narrow collapse rate. Characterize Pathway B mechanism. Consider: trained dt_emb + subsample OFF + dt=1 imag (no dt>1 in training data) |\\n\\n### Priority Actions Before Submission\\n1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed\\n2. ~~**008e_v3 B+ confound**~~ — ✅ Done: 869.9@105K (95% baseline), B+ confirmed\\n3. ~~**008f C2 causal control**~~ — ✅ Done: V-recovery to 503@105K, normalized v/e=0.30x\\n4. ~~**008e_v3_s2 (seed=2)**~~ — ❌ D040: **COLLAPSED via non-CIVO pathway** (eval-driven, entropy ↑). C6 partially falsified — multiple vulnerability pathways.\\n5. ~~**Multi-seed replication**~~ — ✅ D040: 009a baseline s2 DONE (stable). All Walker Walk seeds complete.\\n6. ~~**Narrative pivot**~~ — ✅ D040: C6 reframed as \\\"multiple vulnerability pathways\\\" (CIVO Pathway A + non-CIVO Pathway B)\\n6.5. ~~**SGS (reward_dt_emb_detach) 验证**~~ — ❌ exp_016e: reward_dt_emb_detach 是 no-op（梯度验证揭示 reward gradient = 0 by architecture）。016e 与 008d 的差异（onset timing, peak height）归因于随机变异，非 SGS 效果。dt_emb 的 93% 梯度来自 observation decoders，7% 来自 KL dynamics，reward=0。\\n7. **考虑新实验**: trained dt_emb + subsample OFF + dt=1 imag — 如果 stable → 确认 training data dt>1 transitions 是 trigger\\n8. **Cheetah Run cross-environment** — P0 priority, addresses R1\\n9. **Figures** — learning curves, normalized v/e (含 008e_v3_s2 崩溃轨迹), RSSM fidelity table\\n10. **Threshold sensitivity analysis** — plan_034, 0 GPU cost\\n\\n---\\n\\n## Key Figures (Planned)\\n\\n1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)\\n2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes\\n3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis\\n4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse\\n5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)\\n6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）\\n7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.\\n\", \"total_chars\": 33549, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01USgs8P9TzdyZZCWehURweg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/framing_b_reaudit.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "55e59dba-352e-49b4-8eab-546c7c267ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mzery3bFhg8U9AsVvaAsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7940,
      "cache_read_input_tokens": 24162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7940
      },
      "output_tokens": 18,
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

_source line 14 · 2026-05-16T04:52:27.741Z_

<details><summary>↩ Tool result · `toolu_01USgs8P9TzdyZZCWehURweg`</summary>

```text
1	# Framing B Re-Audit: Per-Section Diff Checklist
2	
3	> Date: 2026-05-16 | Framing: **B — Diagnostic paper + SGS as informative negative result**
4	> Governing decisions: D059 (Framing B approved), D061 (gradient decomposition: reward=0, obs=93%)
5	> NVE diagnostic: 7/8 accuracy, AUROC=0.933, 1 FP (008e_v3_s2 non-CIVO)
6	
7	---
8	
9	## 1. Abstract
10	
11	**Current status:** NOT WRITTEN
12	
13	**Framing B requirements:**
14	- Diagnostic analysis paper positioning (not method paper)
15	- Core question: "Why does temporal abstraction fail in world-model RL?"
16	- Key findings: trained dt_embedding → CIVO → stochastic collapse
17	- NVE diagnostic framework: 7/8, AUROC=0.933
18	- Gradient decomposition: 93% obs decoders, 0% reward → reward-only SGS is architectural no-op
19	- TAWM contrast: dt-conditioning succeeds in MPC (TAWM, ICML 2025) but fails in imagination-based AC
20	- Scope: DreamerV3 + Walker Walk (+ Cheetah pending)
21	
22	**Outline (≤150 words):**
23	1. Temporal abstraction via variable-rate imagination is a natural extension of world-model RL, but consistently degrades performance [1 sentence]
24	2. We present a systematic diagnostic analysis identifying trained dt-embedding as the necessary condition for conditioning-induced value overestimation (CIVO) [1 sentence]
25	3. Gradient decomposition reveals 93% of dt_emb gradients come from observation decoders (0% reward), making reward-only stop-gradient an architectural no-op [1 sentence]
26	4. NVE diagnostic threshold achieves AUROC=0.933 for CIVO detection [1 sentence]
27	5. Contrast with TAWM: dt-conditioning succeeds in MPC but fails in imagination-based AC — architecture-specific vulnerability [1 sentence]
28	6. Scoped to DreamerV3/RSSM; actionable guidelines for future temporal abstraction work [1 sentence]
29	
30	**Legacy framing risks:** N/A (not yet written)
31	
32	**Missing content:** Entire section
33	
34	---
35	
36	## 2. Introduction
37	
38	**Current status:** NOT WRITTEN
39	
40	**Framing B requirements:**
41	- Open with temporal abstraction as longstanding RL goal (options, macro-actions)
42	- World-model RL as natural testbed (modify imagination dt without changing env interaction)
43	- Puzzle framing: all attempts at variable-rate imagination degrade performance — why?
44	- TAWM contrast as novelty anchor: dt-conditioning works in MPC (TD-MPC2) but fails in imagination-based AC → architecture-specific vulnerability, not a generic negative
45	- Contribution list:
46	  1. Causal chain: trained dt_emb → CIVO (NVE>1.5x) → stochastic collapse
47	  2. NVE diagnostic framework (7/8 accuracy, AUROC=0.933)
48	  3. Gradient decomposition revealing reward=0 pathway (SGS = no-op)
49	  4. 2×2 ablation matrix closing the causal loop (D049)
50	- NOT a method paper — no new algorithm proposed
51	- Scope disclaimer: DreamerV3 + RSSM
52	
53	**Legacy framing risks:** N/A (not yet written)
54	
55	**Missing content:** Entire section. Must be written from scratch per story arc in paper_framing.md.
56	
57	---
58	
59	## 3. Related Work
60	
61	**Current status:** NOT WRITTEN
62	
63	**Framing B requirements:**
64	- Temporal abstraction in model-free RL: options framework (Sutton 1999), FiGAR, action repeat
65	- World-model RL: Dreamer family, IRIS, TWM
66	- **TAWM (Nhu et al., ICML 2025)** — CRITICAL: dt-conditioning succeeds in TD-MPC2 (MPC setting). Must position as: "dt-conditioning is not inherently broken; the vulnerability is specific to imagination-based actor-critic." This is the key novelty upgrade (D037)
67	- Variable-rate planning in world models (limited prior work)
68	- Value overestimation in MBRL: Lu et al. 2018 (delusional bias), Janner et al. 2019 (model exploitation). **Must explicitly differentiate** CIVO from Lu et al.'s delusional bias (different mechanism: model imprecision + learned conditioning amplification vs policy-class constraints)
69	- Diagnostic/analysis papers as a genre (precedent for non-method contributions)
70	
71	**Legacy framing risks:** N/A (not yet written)
72	
73	**Missing content:** Entire section. TAWM positioning is the single most important item for novelty defense.
74	
75	---
76	
77	## 4. Method (paper/method.md)
78	
79	**Current status:** DRAFT v1, 144 lines. Covers §3.1 (Background), §3.2 (NVE diagnostic), §3.3 (Causal analysis + RSSM fidelity + mitigation).
80	
81	### 4.1 Diff items
82	
83	**DIFF-M1: §3 title — consider repositioning as "Methodology" or "Diagnostic Framework"**
84	- Current: "3. Methodology" — acceptable for diagnostic paper
85	- No change needed
86	
87	**DIFF-M2: "The Delusional Critic Hypothesis" heading (line 39) → rename**
88	- Current: `### The Delusional Critic Hypothesis`
89	- Required: `### Conditioning-Induced Value Overestimation (CIVO)`
90	- The subsection body (lines 41-43) already uses "CIVO" and differentiates from Lu et al. Good.
91	- But line 43 still says: `We term this the *CIVO*, drawing on Lu & Schuurmans' concept of delusional policies, where function approximation introduces inconsistencies in Q-learning backups.`
92	- **Action:** Rename heading. Revise body to lead with CIVO definition, then note Lu et al. analogy as secondary (not "drawing on" — that implies derivation). Emphasize: CIVO is model-induced (temporal extrapolation error), Lu et al.'s delusion is policy-class-induced. Keep distinction explicit per D037.
93	
94	**DIFF-M3: §3.3 "Mitigation: dt=1 Imagination" (lines 135-143) — MAJOR UPDATE NEEDED**
95	- Current: Presents 008e_v3 seed 1 as 95% baseline recovery, single-seed success. Lines 142-143 say "seed 2 is in progress."
96	- Framing B reality: **008e_v3_s2 COLLAPSED** (eval 715→137, nve=3.78x). C6 partially falsified (D038/D040).
97	- **Actions:**
98	  1. Remove "Mitigation" framing entirely — dt=1 imagination is NOT a robust mitigation
99	  2. Rewrite as "Imagination Step Size as Causal Variable" — the diagnostic point (trained dt_emb + dt=1 still collapses at 1/2 rate) is the finding
100	  3. Add s2 collapse data with mechanism contrast table (value-driven CIVO in 008d vs eval-driven instability in 008e_v3_s2)
101	  4. Add 009a baseline s2 stability data ruling out seed fragility
102	  5. Reframe: trained dt_embedding creates vulnerability through multiple pathways (Pathway A: CIVO via dt>1 imagination; Pathway B: non-CIVO policy instability independent of imagination dt)
103	  6. Remove lines 142-143 ("ongoing" language for s2)
104	
105	**DIFF-M4: Add §3.X — Gradient Decomposition of dt_embedding (NEW SUBSECTION)**
106	- Not in current draft at all. This is a D061 finding.
107	- **Content:**
108	  - torch.autograd.grad analysis on dt_emb.weight
109	  - Gradient source breakdown: obs decoders 93% (1.505), KL 7% (0.119), reward 0% (0.000)
110	  - Implication 1: reward_dt_emb_detach (016e) is architectural no-op
111	  - Implication 2: dt_emb training is driven by observation reconstruction, not reward
112	  - Implication 3: Full-SGS (018) removing obs decoder gradients is the real gradient-level intervention
113	- **Placement:** After RSSM fidelity analysis (before or after the mitigation/causal-variable section)
114	
115	**DIFF-M5: Add SGS as informative negative result (NEW SUBSECTION or folded into gradient decomposition)**
116	- 016e experiment: reward_dt_emb_detach=True
117	- Result: collapse at 95K (nve=10.42x), indistinguishable from 008d stochastic variation
118	- Interpretation: reward-only SGS is no-op because reward gradient to dt_emb = 0 by architecture
119	- Previously interpreted as "SGS delays collapse ~50K" — **this interpretation is WITHDRAWN** (D061)
120	- Frame as: "The null result is informative: it eliminates reward head as CIVO gradient pathway and redirects attention to observation decoders"
121	
122	**DIFF-M6: 2×2 ablation matrix (D049) — not yet in method.md**
123	- The 2×2 matrix (trained/frozen/removed × subsample ON/OFF) is referenced in ROADMAP but not in method section
124	- Should add 015b (frozen dt_emb, subsample ON) result: peak nve 1.45x@55K → self-corrected → gradient starvation collapse
125	- This fills the ablation picture: trained=CIVO, frozen=sub-threshold transient, removed=blocked
126	
127	**DIFF-M7: NVE diagnostic power update**
128	- Current draft (lines 70-71): "4/4 classification accuracy" — still accurate for threshold separation
129	- Framing B adds: AUROC=0.933, 7/8 overall accuracy, 1 FP (008e_v3_s2 non-CIVO late collapse)
130	- **Action:** Add AUROC=0.933 and 7/8 framing after the 4/4 threshold statement. Reference nve_sensitivity_table.tex. Clarify: 4/4 is for trained-vs-removed at threshold; 7/8 includes all conditions with 008e_v3_s2 as FP due to non-CIVO mechanism.
131	
132	### 4.2 Legacy framing risks in method.md
133	
134	| Line(s) | Issue | Action |
135	|---------|-------|--------|
136	| 39 | "The Delusional Critic Hypothesis" heading | Rename to "Conditioning-Induced Value Overestimation (CIVO)" |
137	| 43 | "drawing on Lu & Schuurmans' concept of delusional policies" | Weaken to "analogous to" and add explicit differentiation |
138	| 135 | "Mitigation: dt=1 Imagination with Multi-Rate Training" | Remove "Mitigation" framing; rewrite as diagnostic finding |
139	| 137-139 | "zero-cost mitigation" / "achieves eval return 869.9" (single seed only) | Remove mitigation language; add s2 collapse data |
140	| 142-143 | "seed 2 is in progress" | Replace with s2 collapse results + mechanism analysis |
141	
142	### 4.3 Missing content in method.md
143	
144	| Item | Priority | Notes |
145	|------|----------|-------|
146	| Gradient decomposition subsection (D061) | P0 | Core Framing B contribution |
147	| SGS informative negative (016e + D061) | P0 | Required by Framing B |
148	| 015b frozen dt_emb results | P1 | Completes 2×2 matrix |
149	| 008e_v3_s2 collapse + dual pathway analysis | P0 | C6 partially falsified |
150	| AUROC=0.933 / 7/8 framing | P1 | NVE strength update |
151	
152	---
153	
154	## 5. Experimental Setup (paper/sections/experimental_setup.md)
155	
156	**Current status:** DRAFT v1, 130 lines. Covers §4.1 (Base architecture), §4.2 (Environment), §4.3 (Factorial design + Table 1), §4.4 (NVE diagnostic), §4.5 (Training details).
157	
158	### 5.1 Diff items
159	
160	**DIFF-E1: Table 1 (factorial table, lines 55-78) — needs new rows**
161	- Missing experiments: 015b (frozen dt_emb), 016e (SGS/reward detach), 009a/009b/009c (seeds)
162	- **Action:** Add rows for:
163	  - 015b: frozen dt_emb, subsample ON, H=15, dt=2 imag → "Frozen embedding control"
164	  - 016e: trained dt_emb + reward_dt_emb_detach, subsample ON, H=8, dt=2 imag → "Stop-gradient (reward)" or "SGS control"
165	  - Possibly 018 (planned) as a footnote row
166	- Seed replication rows (009a/b/c) can be listed as notes under existing rows rather than separate rows
167	
168	**DIFF-E2: §4.2 Environment — update cross-env status**
169	- Lines 35-41: mentions Cheetah Run and Cartpole Swingup with footnote "in progress"
170	- 010a Cheetah baseline is now RUNNING (ROADMAP)
171	- **Action:** Keep footnote but update wording if 010a completes before submission. Remove Cartpole Swingup if it won't be run (focus resources on Cheetah).
172	
173	**DIFF-E3: §4.4 NVE diagnostic — add AUROC and 7/8 framing**
174	- Current: 4/4 classification (lines 111-113)
175	- **Action:** Add paragraph after threshold definition:
176	  - AUROC=0.933 across all 8 experimental conditions (task B2)
177	  - 7/8 accuracy with 1 FP (008e_v3_s2, identified as non-CIVO late collapse via trajectory analysis)
178	  - Reference nve_sensitivity_table.tex
179	  - Supplementary task B1 (@1.7x): AUROC=1.0, 8/8
180	
181	**DIFF-E4: §4.5 Training details — update seed info**
182	- Line 129: "key conditions (baseline, 008d, 008f, 008e_v3) add seed 2"
183	- **Action:** Update to reflect completed seed 2 runs: 009a (baseline s2, complete, stable), 009b (008d s2, complete, self-corrected), 009c (008f s2, complete), 008e_v3_s2 (complete, collapsed via non-CIVO pathway). Remove "in progress" language.
184	
185	**DIFF-E5: "event-gated variable-rate imagination" naming (line 15)**
186	- Current: "We introduce an *event-gated variable-rate imagination* mechanism"
187	- Framing B is a diagnostic paper — the mechanism being studied failed. The naming suggests we're proposing it.
188	- **Action:** Reword: "We study a *variable-rate imagination* mechanism..." or "We investigate the following modifications to the DreamerV3 imagination pipeline..."
189	
190	### 5.2 Legacy framing risks in experimental_setup.md
191	
192	| Line(s) | Issue | Action |
193	|---------|-------|--------|
194	| 15 | "We introduce an event-gated variable-rate imagination mechanism" | Reword — we study/investigate, not introduce |
195	| 57 | Table caption: "unless noted" for dt=2 default | Fine, but add 016e row |
196	| 87 | "mitigation condition (008e_v3)" | Remove "mitigation" label — partially falsified |
197	| 109 | "we will update to the mean of seeds 1 and 2 once..." | Update: 009a baseline s2 is now complete; update normalization |
198	
199	### 5.3 Missing content in experimental_setup.md
200	
201	| Item | Priority | Notes |
202	|------|----------|-------|
203	| 016e (SGS) in factorial table | P0 | Core Framing B experiment |
204	| 015b (frozen) in factorial table | P1 | Completes 2×2 matrix |
205	| AUROC/7/8 in diagnostic section | P1 | Matched with method.md update |
206	| Updated seed status | P1 | Remove "in progress" language |
207	
208	---
209	
210	## 6. Results
211	
212	**Current status:** NOT WRITTEN
213	
214	**Framing B requirements:**
215	Structure as diagnostic findings, not performance claims:
216	
217	**Finding 1 (C1):** All dt>1 configurations degrade performance
218	- 3 configs: 005 (learned gate), 006 (fixed dt=2), 007 (fixed dt=4)
219	- Learning curves overlay (hero figure)
220	
221	**Finding 2 (C2):** Trained dt_embedding is the necessary condition for CIVO
222	- 008d vs 008f (primary causal comparison): trained → nve 2.09x → collapse; removed → nve ≤1.02x → stable
223	- 4/4 threshold separation across seeds
224	- 2×2 matrix: trained/frozen/removed × subsample
225	
226	**Finding 3 (C3):** Untrained dt_embedding suppresses value drift
227	- 008a: 85% baseline at 105K, nve 0.59-0.93x
228	- 008c vs 008a: horizon effect
229	
230	**Finding 4 (C4):** Longer dt amplifies degradation
231	- dt=1 (~950) > dt=2 (485) > dt=4 (177) monotonic
232	
233	**Finding 5 (C5):** Subsampling/horizon are secondary factors
234	- 008e_v3 s1: subsample ON + dt=1 imag → 95% baseline
235	
236	**Finding 6 (C6, partially falsified):** dt=1 imagination does not prevent collapse
237	- 008e_v3_s2 collapsed (eval 715→137, nve=3.78x)
238	- Dual pathway analysis: CIVO (Pathway A, 008d) vs non-CIVO policy instability (Pathway B, 008e_v3_s2)
239	- 009a baseline s2 stable → config-caused
240	
241	**Finding 7 (NEW — Framing B core):** Gradient decomposition reveals reward=0 pathway
242	- dt_emb gradient: obs decoders 93%, KL 7%, reward 0%
243	- 016e SGS = no-op (informative negative)
244	- Reframes understanding of which pathways drive dt_emb training
245	
246	**Finding 8: NVE diagnostic framework performance**
247	- task B2: 7/8, AUROC=0.933, 1 FP
248	- task B1 (supplementary): 8/8, AUROC=1.0
249	- Threshold sensitivity analysis (nve_sensitivity_table.tex)
250	
251	**Legacy framing risks:** N/A (not yet written, but must NOT include):
252	- "SGS delays collapse" — WITHDRAWN (D061)
253	- "dt=1 imagination as practical mitigation" — PARTIALLY FALSIFIED (D038/D040)
254	- "delusional critic" terminology
255	
256	**Missing content:** Entire section
257	
258	---
259	
260	## 7. Discussion
261	
262	**Current status:** NOT WRITTEN
263	
264	**Framing B requirements:**
265	
266	1. **CIVO mechanism explanation**: Why trained dt_embedding causes overestimation
267	   - RSSM fidelity gap at dt>1 (Table: absolute errors + ratios)
268	   - 008d reward gap (2.78x) = critic receives confident but biased reward signals
269	   - 008f reward gap (1.01x) = no differentiation → no bias → no CIVO
270	
271	2. **Gradient decomposition implications** (D061)
272	   - dt_emb is trained by observation reconstruction, not reward
273	   - Reward-only SGS is no-op → future interventions must target obs decoder pathway
274	   - Full-SGS (018) as the correct gradient-level test
275	
276	3. **Dual vulnerability pathways** (D040)
277	   - Pathway A (CIVO): value-driven, entropy ↓, requires dt>1 imagination (008d)
278	   - Pathway B (non-CIVO policy instability): eval-driven, entropy ↑, independent of imagination dt (008e_v3_s2)
279	   - Trained dt_embedding as common root, but mechanisms diverge
280	
281	4. **Value self-correction** (009b)
282	   - Transient nve>1.5x → self-correction (009b s2) vs sustained → collapse (008d s1)
283	   - Hypothesis: "point of no return" where feedback loop locks
284	   - Connection to primacy bias (Qiao et al. 2023), early outlier runs (Bjorck et al. 2022)
285	
286	5. **TAWM contrast** (D037 — CRITICAL for novelty)
287	   - TAWM: dt-conditioning succeeds in TD-MPC2 (MPC)
288	   - Our finding: fails in imagination-based AC
289	   - Key difference: MPC re-plans from real states; imagination-based AC compounds errors across full rollout
290	   - Novelty upgrade: "architecture-specific vulnerability, not generic failure"
291	
292	6. **Connection to MBRL overestimation literature**
293	   - Lu et al. 2018: delusional bias (policy-class) — differentiate from CIVO (model-induced)
294	   - Janner et al. 2019: model exploitation — CIVO is a specific instance mediated by temporal conditioning
295	   - Why model-free temporal abstraction doesn't suffer the same failure
296	
297	**Legacy framing risks:** Must ensure:
298	- No "SGS delays collapse" claim
299	- No "delusional critic" usage
300	- No "dt=1 imagination solves the problem" framing
301	- 008f positioned as causal control, not recommended approach
302	
303	**Missing content:** Entire section
304	
305	---
306	
307	## 8. Limitations
308	
309	**Current status:** NOT WRITTEN
310	
311	**Framing B requirements:**
312	1. Single primary environment (Walker Walk) — Cheetah pending (010a)
313	2. Limited seed count (2 seeds per key condition; stochastic collapse hard to characterize)
314	3. NVE threshold calibrated and evaluated on same data (not independent validation)
315	4. NVE confidence intervals wide: 95% CI = [47.3%, 99.7%] for 7/8
316	5. Only one base algorithm (DreamerV3); generalizability to other world-model architectures discussed but not tested
317	6. No formal causal inference framework (interventional, not observational, but not a formal DAG-based analysis)
318	7. Full-SGS (018) and Cheetah cross-env results pending at submission
319	8. 008e_v3_s2 collapse mechanism (Pathway B) not fully characterized — entropy increase noted but root cause unclear
320	
321	**Legacy framing risks:** N/A (not yet written)
322	
323	**Missing content:** Entire section
324	
325	---
326	
327	## 9. Conclusion
328	
329	**Current status:** NOT WRITTEN
330	
331	**Framing B requirements:**
332	- Restate core finding: trained dt_embedding is the necessary condition for CIVO in imagination-based AC
333	- Gradient decomposition: 93% obs decoders, 0% reward → reward pathway is architectural null
334	- NVE as practical diagnostic tool (AUROC=0.933)
335	- TAWM contrast: dt-conditioning is not inherently broken — the vulnerability is specific to imagination + learned dynamics
336	- Actionable guidance: don't use trained dt_embedding in imagination-based AC without safeguards; target obs decoder pathway for interventions
337	- Open questions: Full-SGS effectiveness (018), cross-environment generality, Pathway B characterization
338	
339	**Legacy framing risks:** N/A (not yet written)
340	
341	**Missing content:** Entire section
342	
343	---
344	
345	## Global Diff Items (cross-cutting)
346	
347	### G1: "delusional critic" → CIVO full-text replacement (D037)
348	
349	**Affected files:**
350	- `paper/method.md` line 39: heading "The Delusional Critic Hypothesis"
351	- `paper/method.md` line 43: "We term this the *CIVO*, drawing on Lu & Schuurmans'"
352	
353	**Action:** Rename heading; rewrite body to define CIVO first, Lu et al. as analogy (not derivation). Search entire paper directory for any other occurrences before declaring clean.
354	
355	### G2: 016e narrative — MUST be "no-op", not "delays collapse" (D061)
356	
357	**Old claim (D057/D058, WITHDRAWN):** "SGS delays collapse ~50K steps"
358	**Correct claim (D061):** "016e reward_dt_emb_detach is a no-op; reward gradient to dt_emb = 0 by architecture. Observed timing differences from 008d are stochastic variation."
359	
360	**Affected files:** Not yet in any written section (016e hasn't been written up yet), but MUST be checked in any future draft. The paper_framing.md exp_016e entry is already updated.
361	
362	### G3: 008e_v3 — NOT a mitigation, partially falsified (D038/D040)
363	
364	**Old claim:** "dt=1 imagination = practical mitigation (95% baseline recovery)"
365	**Correct claim:** "dt=1 imagination does not prevent collapse (1/2 seeds collapse via non-CIVO pathway). Trained dt_embedding creates vulnerability through multiple pathways."
366	
367	**Affected files:**
368	- `paper/method.md` lines 135-143: entire "Mitigation" subsection must be rewritten
369	- `paper/sections/experimental_setup.md` line 87: "mitigation condition (008e_v3)"
370	
371	### G4: TAWM positioning (D037 novelty upgrade)
372	
373	**Status:** Not in any existing section.
374	**Required in:** Related Work (primary), Introduction (contribution claim), Discussion (mechanism contrast)
375	**Key sentence:** "TAWM (Nhu et al., ICML 2025) demonstrates that dt-conditioning succeeds in MPC settings (TD-MPC2), establishing that the vulnerability we identify is specific to imagination-based actor-critic training, not an inherent limitation of temporal conditioning."
376	
377	### G5: 2×2 ablation matrix (D049)
378	
379	**Status:** Referenced in ROADMAP but not yet in paper sections.
380	**Required in:** Results section, Discussion
381	**Content:** trained/frozen/removed × subsample ON/OFF matrix showing CIVO status per cell
382	
383	### G6: Figures needed
384	
385	| Figure | Status | Content |
386	|--------|--------|---------|
387	| Fig 1: Learning curves (hero) | Not created | All experiments overlaid |
388	| Fig 2: NVE trajectories | Not created | Healthy vs pathological separation |
389	| Fig 3: Factorial grid | Exists (updated per ROADMAP) | 2×2 matrix visualization |
390	| Fig 4: Causal diagram | Not created | dt_emb → CIVO → collapse chain |
391	| Fig 5: dt magnitude comparison | Not created | dt=1/2/4 monotonic decline |
392	| Fig 6: 008e_v3 dual seed | Exists (updated per ROADMAP) | s1 healthy + s2 collapse |
393	| Table: RSSM fidelity | In method.md | Needs absolute + ratio side-by-side |
394	| Table: NVE sensitivity | nve_sensitivity_table.tex | AUROC=0.933, exists |
395	| Table: Gradient decomposition | Not created | obs 93%, KL 7%, reward 0% |
396	
397	---
398	
399	## Priority-Ordered Execution Plan
400	
401	### P0 — Blocking for submission
402	
403	1. Rewrite `paper/method.md` §3.3 "Mitigation" → dual pathway finding (DIFF-M3)
404	2. Add gradient decomposition subsection to method.md (DIFF-M4)
405	3. Add SGS informative negative subsection (DIFF-M5)
406	4. Rename "Delusional Critic Hypothesis" → CIVO (DIFF-M2)
407	5. Write Results section (Section 5)
408	6. Write Introduction
409	7. Write Abstract
410	8. Write Discussion (especially TAWM contrast, dual pathways, gradient implications)
411	9. Add 016e to factorial table (DIFF-E1)
412	10. Update NVE diagnostic with AUROC=0.933 (DIFF-M7, DIFF-E3)
413	
414	### P1 — Important but not blocking
415	
416	11. Write Related Work (especially TAWM)
417	12. Write Limitations
418	13. Write Conclusion
419	14. Add 015b to factorial table and results
420	15. Update seed status / remove "in progress" language (DIFF-E4)
421	16. Reword "event-gated" as diagnostic study language (DIFF-E5)
422	17. Create gradient decomposition table
423	18. Update baseline normalization with 009a (DIFF-E4, experimental_setup.md line 109)
424	
425	### P2 — Polish
426	
427	19. Create missing figures (Fig 1, 2, 4, 5)
428	20. Cross-reference consistency check (method ↔ experimental_setup)
429	21. Final "delusional critic" grep across all files
430	22. Ensure RSSM fidelity table shows absolute + ratio everywhere
431	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "11047b1e-872c-413e-a2bd-6bc8b79b9f14",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/framing_b_reaudit.md",
      "content": "# Framing B Re-Audit: Per-Section Diff Checklist\n\n> Date: 2026-05-16 | Framing: **B — Diagnostic paper + SGS as informative negative result**\n> Governing decisions: D059 (Framing B approved), D061 (gradient decomposition: reward=0, obs=93%)\n> NVE diagnostic: 7/8 accuracy, AUROC=0.933, 1 FP (008e_v3_s2 non-CIVO)\n\n---\n\n## 1. Abstract\n\n**Current status:** NOT WRITTEN\n\n**Framing B requirements:**\n- Diagnostic analysis paper positioning (not method paper)\n- Core question: \"Why does temporal abstraction fail in world-model RL?\"\n- Key findings: trained dt_embedding → CIVO → stochastic collapse\n- NVE diagnostic framework: 7/8, AUROC=0.933\n- Gradient decomposition: 93% obs decoders, 0% reward → reward-only SGS is architectural no-op\n- TAWM contrast: dt-conditioning succeeds in MPC (TAWM, ICML 2025) but fails in imagination-based AC\n- Scope: DreamerV3 + Walker Walk (+ Cheetah pending)\n\n**Outline (≤150 words):**\n1. Temporal abstraction via variable-rate imagination is a natural extension of world-model RL, but consistently degrades performance [1 sentence]\n2. We present a systematic diagnostic analysis identifying trained dt-embedding as the necessary condition for conditioning-induced value overestimation (CIVO) [1 sentence]\n3. Gradient decomposition reveals 93% of dt_emb gradients come from observation decoders (0% reward), making reward-only stop-gradient an architectural no-op [1 sentence]\n4. NVE diagnostic threshold achieves AUROC=0.933 for CIVO detection [1 sentence]\n5. Contrast with TAWM: dt-conditioning succeeds in MPC but fails in imagination-based AC — architecture-specific vulnerability [1 sentence]\n6. Scoped to DreamerV3/RSSM; actionable guidelines for future temporal abstraction work [1 sentence]\n\n**Legacy framing risks:** N/A (not yet written)\n\n**Missing content:** Entire section\n\n---\n\n## 2. Introduction\n\n**Current status:** NOT WRITTEN\n\n**Framing B requirements:**\n- Open with temporal abstraction as longstanding RL goal (options, macro-actions)\n- World-model RL as natural testbed (modify imagination dt without changing env interaction)\n- Puzzle framing: all attempts at variable-rate imagination degrade performance — why?\n- TAWM contrast as novelty anchor: dt-conditioning works in MPC (TD-MPC2) but fails in imagination-based AC → architecture-specific vulnerability, not a generic negative\n- Contribution list:\n  1. Causal chain: trained dt_emb → CIVO (NVE>1.5x) → stochastic collapse\n  2. NVE diagnostic framework (7/8 accuracy, AUROC=0.933)\n  3. Gradient decomposition revealing reward=0 pathway (SGS = no-op)\n  4. 2×2 ablation matrix closing the causal loop (D049)\n- NOT a method paper — no new algorithm proposed\n- Scope disclaimer: DreamerV3 + RSSM\n\n**Legacy framing risks:** N/A (not yet written)\n\n**Missing content:** Entire section. Must be written from scratch per story arc in paper_framing.md.\n\n---\n\n## 3. Related Work\n\n**Current status:** NOT WRITTEN\n\n**Framing B requirements:**\n- Temporal abstraction in model-free RL: options framework (Sutton 1999), FiGAR, action repeat\n- World-model RL: Dreamer family, IRIS, TWM\n- **TAWM (Nhu et al., ICML 2025)** — CRITICAL: dt-conditioning succeeds in TD-MPC2 (MPC setting). Must position as: \"dt-conditioning is not inherently broken; the vulnerability is specific to imagination-based actor-critic.\" This is the key novelty upgrade (D037)\n- Variable-rate planning in world models (limited prior work)\n- Value overestimation in MBRL: Lu et al. 2018 (delusional bias), Janner et al. 2019 (model exploitation). **Must explicitly differentiate** CIVO from Lu et al.'s delusional bias (different mechanism: model imprecision + learned conditioning amplification vs policy-class constraints)\n- Diagnostic/analysis papers as a genre (precedent for non-method contributions)\n\n**Legacy framing risks:** N/A (not yet written)\n\n**Missing content:** Entire section. TAWM positioning is the single most important item for novelty defense.\n\n---\n\n## 4. Method (paper/method.md)\n\n**Current status:** DRAFT v1, 144 lines. Covers §3.1 (Background), §3.2 (NVE diagnostic), §3.3 (Causal analysis + RSSM fidelity + mitigation).\n\n### 4.1 Diff items\n\n**DIFF-M1: §3 title — consider repositioning as \"Methodology\" or \"Diagnostic Framework\"**\n- Current: \"3. Methodology\" — acceptable for diagnostic paper\n- No change needed\n\n**DIFF-M2: \"The Delusional Critic Hypothesis\" heading (line 39) → rename**\n- Current: `### The Delusional Critic Hypothesis`\n- Required: `### Conditioning-Induced Value Overestimation (CIVO)`\n- The subsection body (lines 41-43) already uses \"CIVO\" and differentiates from Lu et al. Good.\n- But line 43 still says: `We term this the *CIVO*, drawing on Lu & Schuurmans' concept of delusional policies, where function approximation introduces inconsistencies in Q-learning backups.`\n- **Action:** Rename heading. Revise body to lead with CIVO definition, then note Lu et al. analogy as secondary (not \"drawing on\" — that implies derivation). Emphasize: CIVO is model-induced (temporal extrapolation error), Lu et al.'s delusion is policy-class-induced. Keep distinction explicit per D037.\n\n**DIFF-M3: §3.3 \"Mitigation: dt=1 Imagination\" (lines 135-143) — MAJOR UPDATE NEEDED**\n- Current: Presents 008e_v3 seed 1 as 95% baseline recovery, single-seed success. Lines 142-143 say \"seed 2 is in progress.\"\n- Framing B reality: **008e_v3_s2 COLLAPSED** (eval 715→137, nve=3.78x). C6 partially falsified (D038/D040).\n- **Actions:**\n  1. Remove \"Mitigation\" framing entirely — dt=1 imagination is NOT a robust mitigation\n  2. Rewrite as \"Imagination Step Size as Causal Variable\" — the diagnostic point (trained dt_emb + dt=1 still collapses at 1/2 rate) is the finding\n  3. Add s2 collapse data with mechanism contrast table (value-driven CIVO in 008d vs eval-driven instability in 008e_v3_s2)\n  4. Add 009a baseline s2 stability data ruling out seed fragility\n  5. Reframe: trained dt_embedding creates vulnerability through multiple pathways (Pathway A: CIVO via dt>1 imagination; Pathway B: non-CIVO policy instability independent of imagination dt)\n  6. Remove lines 142-143 (\"ongoing\" language for s2)\n\n**DIFF-M4: Add §3.X — Gradient Decomposition of dt_embedding (NEW SUBSECTION)**\n- Not in current draft at all. This is a D061 finding.\n- **Content:**\n  - torch.autograd.grad analysis on dt_emb.weight\n  - Gradient source breakdown: obs decoders 93% (1.505), KL 7% (0.119), reward 0% (0.000)\n  - Implication 1: reward_dt_emb_detach (016e) is architectural no-op\n  - Implication 2: dt_emb training is driven by observation reconstruction, not reward\n  - Implication 3: Full-SGS (018) removing obs decoder gradients is the real gradient-level intervention\n- **Placement:** After RSSM fidelity analysis (before or after the mitigation/causal-variable section)\n\n**DIFF-M5: Add SGS as informative negative result (NEW SUBSECTION or folded into gradient decomposition)**\n- 016e experiment: reward_dt_emb_detach=True\n- Result: collapse at 95K (nve=10.42x), indistinguishable from 008d stochastic variation\n- Interpretation: reward-only SGS is no-op because reward gradient to dt_emb = 0 by architecture\n- Previously interpreted as \"SGS delays collapse ~50K\" — **this interpretation is WITHDRAWN** (D061)\n- Frame as: \"The null result is informative: it eliminates reward head as CIVO gradient pathway and redirects attention to observation decoders\"\n\n**DIFF-M6: 2×2 ablation matrix (D049) — not yet in method.md**\n- The 2×2 matrix (trained/frozen/removed × subsample ON/OFF) is referenced in ROADMAP but not in method section\n- Should add 015b (frozen dt_emb, subsample ON) result: peak nve 1.45x@55K → self-corrected → gradient starvation collapse\n- This fills the ablation picture: trained=CIVO, frozen=sub-threshold transient, removed=blocked\n\n**DIFF-M7: NVE diagnostic power update**\n- Current draft (lines 70-71): \"4/4 classification accuracy\" — still accurate for threshold separation\n- Framing B adds: AUROC=0.933, 7/8 overall accuracy, 1 FP (008e_v3_s2 non-CIVO late collapse)\n- **Action:** Add AUROC=0.933 and 7/8 framing after the 4/4 threshold statement. Reference nve_sensitivity_table.tex. Clarify: 4/4 is for trained-vs-removed at threshold; 7/8 includes all conditions with 008e_v3_s2 as FP due to non-CIVO mechanism.\n\n### 4.2 Legacy framing risks in method.md\n\n| Line(s) | Issue | Action |\n|---------|-------|--------|\n| 39 | \"The Delusional Critic Hypothesis\" heading | Rename to \"Conditioning-Induced Value Overestimation (CIVO)\" |\n| 43 | \"drawing on Lu & Schuurmans' concept of delusional policies\" | Weaken to \"analogous to\" and add explicit differentiation |\n| 135 | \"Mitigation: dt=1 Imagination with Multi-Rate Training\" | Remove \"Mitigation\" framing; rewrite as diagnostic finding |\n| 137-139 | \"zero-cost mitigation\" / \"achieves eval return 869.9\" (single seed only) | Remove mitigation language; add s2 collapse data |\n| 142-143 | \"seed 2 is in progress\" | Replace with s2 collapse results + mechanism analysis |\n\n### 4.3 Missing content in method.md\n\n| Item | Priority | Notes |\n|------|----------|-------|\n| Gradient decomposition subsection (D061) | P0 | Core Framing B contribution |\n| SGS informative negative (016e + D061) | P0 | Required by Framing B |\n| 015b frozen dt_emb results | P1 | Completes 2×2 matrix |\n| 008e_v3_s2 collapse + dual pathway analysis | P0 | C6 partially falsified |\n| AUROC=0.933 / 7/8 framing | P1 | NVE strength update |\n\n---\n\n## 5. Experimental Setup (paper/sections/experimental_setup.md)\n\n**Current status:** DRAFT v1, 130 lines. Covers §4.1 (Base architecture), §4.2 (Environment), §4.3 (Factorial design + Table 1), §4.4 (NVE diagnostic), §4.5 (Training details).\n\n### 5.1 Diff items\n\n**DIFF-E1: Table 1 (factorial table, lines 55-78) — needs new rows**\n- Missing experiments: 015b (frozen dt_emb), 016e (SGS/reward detach), 009a/009b/009c (seeds)\n- **Action:** Add rows for:\n  - 015b: frozen dt_emb, subsample ON, H=15, dt=2 imag → \"Frozen embedding control\"\n  - 016e: trained dt_emb + reward_dt_emb_detach, subsample ON, H=8, dt=2 imag → \"Stop-gradient (reward)\" or \"SGS control\"\n  - Possibly 018 (planned) as a footnote row\n- Seed replication rows (009a/b/c) can be listed as notes under existing rows rather than separate rows\n\n**DIFF-E2: §4.2 Environment — update cross-env status**\n- Lines 35-41: mentions Cheetah Run and Cartpole Swingup with footnote \"in progress\"\n- 010a Cheetah baseline is now RUNNING (ROADMAP)\n- **Action:** Keep footnote but update wording if 010a completes before submission. Remove Cartpole Swingup if it won't be run (focus resources on Cheetah).\n\n**DIFF-E3: §4.4 NVE diagnostic — add AUROC and 7/8 framing**\n- Current: 4/4 classification (lines 111-113)\n- **Action:** Add paragraph after threshold definition:\n  - AUROC=0.933 across all 8 experimental conditions (task B2)\n  - 7/8 accuracy with 1 FP (008e_v3_s2, identified as non-CIVO late collapse via trajectory analysis)\n  - Reference nve_sensitivity_table.tex\n  - Supplementary task B1 (@1.7x): AUROC=1.0, 8/8\n\n**DIFF-E4: §4.5 Training details — update seed info**\n- Line 129: \"key conditions (baseline, 008d, 008f, 008e_v3) add seed 2\"\n- **Action:** Update to reflect completed seed 2 runs: 009a (baseline s2, complete, stable), 009b (008d s2, complete, self-corrected), 009c (008f s2, complete), 008e_v3_s2 (complete, collapsed via non-CIVO pathway). Remove \"in progress\" language.\n\n**DIFF-E5: \"event-gated variable-rate imagination\" naming (line 15)**\n- Current: \"We introduce an *event-gated variable-rate imagination* mechanism\"\n- Framing B is a diagnostic paper — the mechanism being studied failed. The naming suggests we're proposing it.\n- **Action:** Reword: \"We study a *variable-rate imagination* mechanism...\" or \"We investigate the following modifications to the DreamerV3 imagination pipeline...\"\n\n### 5.2 Legacy framing risks in experimental_setup.md\n\n| Line(s) | Issue | Action |\n|---------|-------|--------|\n| 15 | \"We introduce an event-gated variable-rate imagination mechanism\" | Reword — we study/investigate, not introduce |\n| 57 | Table caption: \"unless noted\" for dt=2 default | Fine, but add 016e row |\n| 87 | \"mitigation condition (008e_v3)\" | Remove \"mitigation\" label — partially falsified |\n| 109 | \"we will update to the mean of seeds 1 and 2 once...\" | Update: 009a baseline s2 is now complete; update normalization |\n\n### 5.3 Missing content in experimental_setup.md\n\n| Item | Priority | Notes |\n|------|----------|-------|\n| 016e (SGS) in factorial table | P0 | Core Framing B experiment |\n| 015b (frozen) in factorial table | P1 | Completes 2×2 matrix |\n| AUROC/7/8 in diagnostic section | P1 | Matched with method.md update |\n| Updated seed status | P1 | Remove \"in progress\" language |\n\n---\n\n## 6. Results\n\n**Current status:** NOT WRITTEN\n\n**Framing B requirements:**\nStructure as diagnostic findings, not performance claims:\n\n**Finding 1 (C1):** All dt>1 configurations degrade performance\n- 3 configs: 005 (learned gate), 006 (fixed dt=2), 007 (fixed dt=4)\n- Learning curves overlay (hero figure)\n\n**Finding 2 (C2):** Trained dt_embedding is the necessary condition for CIVO\n- 008d vs 008f (primary causal comparison): trained → nve 2.09x → collapse; removed → nve ≤1.02x → stable\n- 4/4 threshold separation across seeds\n- 2×2 matrix: trained/frozen/removed × subsample\n\n**Finding 3 (C3):** Untrained dt_embedding suppresses value drift\n- 008a: 85% baseline at 105K, nve 0.59-0.93x\n- 008c vs 008a: horizon effect\n\n**Finding 4 (C4):** Longer dt amplifies degradation\n- dt=1 (~950) > dt=2 (485) > dt=4 (177) monotonic\n\n**Finding 5 (C5):** Subsampling/horizon are secondary factors\n- 008e_v3 s1: subsample ON + dt=1 imag → 95% baseline\n\n**Finding 6 (C6, partially falsified):** dt=1 imagination does not prevent collapse\n- 008e_v3_s2 collapsed (eval 715→137, nve=3.78x)\n- Dual pathway analysis: CIVO (Pathway A, 008d) vs non-CIVO policy instability (Pathway B, 008e_v3_s2)\n- 009a baseline s2 stable → config-caused\n\n**Finding 7 (NEW — Framing B core):** Gradient decomposition reveals reward=0 pathway\n- dt_emb gradient: obs decoders 93%, KL 7%, reward 0%\n- 016e SGS = no-op (informative negative)\n- Reframes understanding of which pathways drive dt_emb training\n\n**Finding 8: NVE diagnostic framework performance**\n- task B2: 7/8, AUROC=0.933, 1 FP\n- task B1 (supplementary): 8/8, AUROC=1.0\n- Threshold sensitivity analysis (nve_sensitivity_table.tex)\n\n**Legacy framing risks:** N/A (not yet written, but must NOT include):\n- \"SGS delays collapse\" — WITHDRAWN (D061)\n- \"dt=1 imagination as practical mitigation\" — PARTIALLY FALSIFIED (D038/D040)\n- \"delusional critic\" terminology\n\n**Missing content:** Entire section\n\n---\n\n## 7. Discussion\n\n**Current status:** NOT WRITTEN\n\n**Framing B requirements:**\n\n1. **CIVO mechanism explanation**: Why trained dt_embedding causes overestimation\n   - RSSM fidelity gap at dt>1 (Table: absolute errors + ratios)\n   - 008d reward gap (2.78x) = critic receives confident but biased reward signals\n   - 008f reward gap (1.01x) = no differentiation → no bias → no CIVO\n\n2. **Gradient decomposition implications** (D061)\n   - dt_emb is trained by observation reconstruction, not reward\n   - Reward-only SGS is no-op → future interventions must target obs decoder pathway\n   - Full-SGS (018) as the correct gradient-level test\n\n3. **Dual vulnerability pathways** (D040)\n   - Pathway A (CIVO): value-driven, entropy ↓, requires dt>1 imagination (008d)\n   - Pathway B (non-CIVO policy instability): eval-driven, entropy ↑, independent of imagination dt (008e_v3_s2)\n   - Trained dt_embedding as common root, but mechanisms diverge\n\n4. **Value self-correction** (009b)\n   - Transient nve>1.5x → self-correction (009b s2) vs sustained → collapse (008d s1)\n   - Hypothesis: \"point of no return\" where feedback loop locks\n   - Connection to primacy bias (Qiao et al. 2023), early outlier runs (Bjorck et al. 2022)\n\n5. **TAWM contrast** (D037 — CRITICAL for novelty)\n   - TAWM: dt-conditioning succeeds in TD-MPC2 (MPC)\n   - Our finding: fails in imagination-based AC\n   - Key difference: MPC re-plans from real states; imagination-based AC compounds errors across full rollout\n   - Novelty upgrade: \"architecture-specific vulnerability, not generic failure\"\n\n6. **Connection to MBRL overestimation literature**\n   - Lu et al. 2018: delusional bias (policy-class) — differentiate from CIVO (model-induced)\n   - Janner et al. 2019: model exploitation — CIVO is a specific instance mediated by temporal conditioning\n   - Why model-free temporal abstraction doesn't suffer the same failure\n\n**Legacy framing risks:** Must ensure:\n- No \"SGS delays collapse\" claim\n- No \"delusional critic\" usage\n- No \"dt=1 imagination solves the problem\" framing\n- 008f positioned as causal control, not recommended approach\n\n**Missing content:** Entire section\n\n---\n\n## 8. Limitations\n\n**Current status:** NOT WRITTEN\n\n**Framing B requirements:**\n1. Single primary environment (Walker Walk) — Cheetah pending (010a)\n2. Limited seed count (2 seeds per key condition; stochastic collapse hard to characterize)\n3. NVE threshold calibrated and evaluated on same data (not independent validation)\n4. NVE confidence intervals wide: 95% CI = [47.3%, 99.7%] for 7/8\n5. Only one base algorithm (DreamerV3); generalizability to other world-model architectures discussed but not tested\n6. No formal causal inference framework (interventional, not observational, but not a formal DAG-based analysis)\n7. Full-SGS (018) and Cheetah cross-env results pending at submission\n8. 008e_v3_s2 collapse mechanism (Pathway B) not fully characterized — entropy increase noted but root cause unclear\n\n**Legacy framing risks:** N/A (not yet written)\n\n**Missing content:** Entire section\n\n---\n\n## 9. Conclusion\n\n**Current status:** NOT WRITTEN\n\n**Framing B requirements:**\n- Restate core finding: trained dt_embedding is the necessary condition for CIVO in imagination-based AC\n- Gradient decomposition: 93% obs decoders, 0% reward → reward pathway is architectural null\n- NVE as practical diagnostic tool (AUROC=0.933)\n- TAWM contrast: dt-conditioning is not inherently broken — the vulnerability is specific to imagination + learned dynamics\n- Actionable guidance: don't use trained dt_embedding in imagination-based AC without safeguards; target obs decoder pathway for interventions\n- Open questions: Full-SGS effectiveness (018), cross-environment generality, Pathway B characterization\n\n**Legacy framing risks:** N/A (not yet written)\n\n**Missing content:** Entire section\n\n---\n\n## Global Diff Items (cross-cutting)\n\n### G1: \"delusional critic\" → CIVO full-text replacement (D037)\n\n**Affected files:**\n- `paper/method.md` line 39: heading \"The Delusional Critic Hypothesis\"\n- `paper/method.md` line 43: \"We term this the *CIVO*, drawing on Lu & Schuurmans'\"\n\n**Action:** Rename heading; rewrite body to define CIVO first, Lu et al. as analogy (not derivation). Search entire paper directory for any other occurrences before declaring clean.\n\n### G2: 016e narrative — MUST be \"no-op\", not \"delays collapse\" (D061)\n\n**Old claim (D057/D058, WITHDRAWN):** \"SGS delays collapse ~50K steps\"\n**Correct claim (D061):** \"016e reward_dt_emb_detach is a no-op; reward gradient to dt_emb = 0 by architecture. Observed timing differences from 008d are stochastic variation.\"\n\n**Affected files:** Not yet in any written section (016e hasn't been written up yet), but MUST be checked in any future draft. The paper_framing.md exp_016e entry is already updated.\n\n### G3: 008e_v3 — NOT a mitigation, partially falsified (D038/D040)\n\n**Old claim:** \"dt=1 imagination = practical mitigation (95% baseline recovery)\"\n**Correct claim:** \"dt=1 imagination does not prevent collapse (1/2 seeds collapse via non-CIVO pathway). Trained dt_embedding creates vulnerability through multiple pathways.\"\n\n**Affected files:**\n- `paper/method.md` lines 135-143: entire \"Mitigation\" subsection must be rewritten\n- `paper/sections/experimental_setup.md` line 87: \"mitigation condition (008e_v3)\"\n\n### G4: TAWM positioning (D037 novelty upgrade)\n\n**Status:** Not in any existing section.\n**Required in:** Related Work (primary), Introduction (contribution claim), Discussion (mechanism contrast)\n**Key sentence:** \"TAWM (Nhu et al., ICML 2025) demonstrates that dt-conditioning succeeds in MPC settings (TD-MPC2), establishing that the vulnerability we identify is specific to imagination-based actor-critic training, not an inherent limitation of temporal conditioning.\"\n\n### G5: 2×2 ablation matrix (D049)\n\n**Status:** Referenced in ROADMAP but not yet in paper sections.\n**Required in:** Results section, Discussion\n**Content:** trained/frozen/removed × subsample ON/OFF matrix showing CIVO status per cell\n\n### G6: Figures needed\n\n| Figure | Status | Content |\n|--------|--------|---------|\n| Fig 1: Learning curves (hero) | Not created | All experiments overlaid |\n| Fig 2: NVE trajectories | Not created | Healthy vs pathological separation |\n| Fig 3: Factorial grid | Exists (updated per ROADMAP) | 2×2 matrix visualization |\n| Fig 4: Causal diagram | Not created | dt_emb → CIVO → collapse chain |\n| Fig 5: dt magnitude comparison | Not created | dt=1/2/4 monotonic decline |\n| Fig 6: 008e_v3 dual seed | Exists (updated per ROADMAP) | s1 healthy + s2 collapse |\n| Table: RSSM fidelity | In method.md | Needs absolute + ratio side-by-side |\n| Table: NVE sensitivity | nve_sensitivity_table.tex | AUROC=0.933, exists |\n| Table: Gradient decomposition | Not created | obs 93%, KL 7%, reward 0% |\n\n---\n\n## Priority-Ordered Execution Plan\n\n### P0 — Blocking for submission\n\n1. Rewrite `paper/method.md` §3.3 \"Mitigation\" → dual pathway finding (DIFF-M3)\n2. Add gradient decomposition subsection to method.md (DIFF-M4)\n3. Add SGS informative negative subsection (DIFF-M5)\n4. Rename \"Delusional Critic Hypothesis\" → CIVO (DIFF-M2)\n5. Write Results section (Section 5)\n6. Write Introduction\n7. Write Abstract\n8. Write Discussion (especially TAWM contrast, dual pathways, gradient implications)\n9. Add 016e to factorial table (DIFF-E1)\n10. Update NVE diagnostic with AUROC=0.933 (DIFF-M7, DIFF-E3)\n\n### P1 — Important but not blocking\n\n11. Write Related Work (especially TAWM)\n12. Write Limitations\n13. Write Conclusion\n14. Add 015b to factorial table and results\n15. Update seed status / remove \"in progress\" language (DIFF-E4)\n16. Reword \"event-gated\" as diagnostic study language (DIFF-E5)\n17. Create gradient decomposition table\n18. Update baseline normalization with 009a (DIFF-E4, experimental_setup.md line 109)\n\n### P2 — Polish\n\n19. Create missing figures (Fig 1, 2, 4, 5)\n20. Cross-reference consistency check (method ↔ experimental_setup)\n21. Final \"delusional critic\" grep across all files\n22. Ensure RSSM fidelity table shows absolute + ratio everywhere\n",
      "numLines": 431,
      "startLine": 1,
      "totalLines": 431
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
Now I have a clear picture of the current state and what needs to be done. Let me review the current method.md carefully and map each DIFF item to specific edits needed.

Current method.md analysis:
- Lines 1-3: Header comments
- Lines 8-10: §3 Methodology intro
- Lines 13-38: §3.1 Background
- Lines 39-43: "Conditioning-Induced Value Overestimation (CIVO)" — Already renamed from "Delusional Critic Hypothesis"! Wait, line 39 says `### Conditioning-Induced Value Overestimation (CIVO)`. 

So DIFF-M2 may have already been partially applied. Looking at the status comment on line 3, it says DIFF-M2, M3, M6, and M7 are already applied. Let me verify each one against what's actually in the file:

**DIFF-M2 (heading rename + body rewrite)**: The heading is indeed renamed to CIVO, so that part checks out.

- Lines 46-86: §3.2 Diagnostic Framework (NVE)
- Lines 89-198: §3.3 Causal Analysis Protocol

Looking at the body text around the CIVO section, it's using "analogous to" rather than "drawing on," and it explicitly differentiates between Lu et al.'s policy-class-induced delusions versus CIVO being model-induced. So DIFF-M2 does appear to be already applied.

**DIFF-M3 (§3.3 mitigation rewrite)**: Now checking lines 182-198 where the Imagination section is... Step Size as Causal Variable` — ✅ renamed from "Mitigation"
- Has seed 2 collapse data, dual-pathway analysis, 009a baseline s2 stability — ✅
- No "seed 2 is in progress" language — ✅
- Seems DIFF-M3 is already applied.

**DIFF-M4 (Gradient Decomposition subsection)**: 
- Lines 150-167: `### Gradient Decomposition of the Temporal Embedding` — ✅ exists
- Has the gradient table, three implications — ✅
- Seems DIFF-M4 is already applied.

**DIFF-M5 (SGS informative negative)**: 
- Lines 169-180: `### Stop-Gradient Surgery: An Informative Negative (exp\_016e)` — ✅ exists
- Has the \label, configuration, results, and architectural no-op explanation — ✅
- No "SGS delays collapse" language — ✅
- Seems DIFF-M5 is already applied.

**DIFF-M6 (2×2 ablation matrix)**: 
- Lines 113-124: Has the 2×2 matrix table — ✅
- Status says "DIFF-M6 (2×2 ablation matrix)" already applied.

**DIFF-M7 (NVE AUROC/7-of-8)**: 
- Lines 77-78: The NVE diagnostic achieves 0.933 AUROC with 7 out of 8 classification accuracy across all eight experimental conditions, with the single false positive occurring in exp\_008e\_v3\_s2 — ✅
- Status says "DIFF-M7 (NVE AUROC/7-of-8)" already applied.

Hold on — all six DIFFs appear to be already applied? Let me reread the task more carefully. The task says I'm responsible for rewriting paper/method.md to conform to Framing B, and lists six diff items: DIFF-M2 through DIFF-M7. But the status comment on line 3 says "DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC/7-of-8). DIFF-M2, DIFF-M3 already applied." And I can see M4 and M5 content in the file as well. Let me reread the instructions.

The framing_b_reaudit.md was written on 2026-05-16 and describes what needs to change, but method.md was also updated on 2026-05-16 and already claims all these diffs are applied. Looking more carefully at the reaudit: DIFF-M2 says the current heading is "The Delusional Critic Hypothesis" with body text about "Lu & Schuurmans' concept", but in method.md the heading is already "Conditioning-Induced Value Overestimation (CIVO)" with "analogous to" language. DIFF-M3 says current is "Mitigation: dt=1 Imagination" but method.md already has "Imagination Step Size as Causal Variable". It looks like the reaudit was describing the old state, and then the changes were already made.

Now I'm checking the header comment in method.md which confirms M2, M3, M6, M7 are applied, and M4, M5 content is present too. Let me verify each requirement against what's actually in the file to see if everything is truly complete or if something's still missing. Going through each diff: M2 has the right heading and defines CIVO first with Lu et al. as analogy, M3 has the correct title with s2 collapse data and dual-pathway analysis including the 009a baseline stability, and no "seed 2 in progress" language. I'm checking the status line more carefully—it mentions M2, M3, M6, and M7 as applied, but M4 and M5 are also present in the file content, which is confusing. Let me trace through what's actually been updated versus what the metadata claims. I've verified that all 6 diffs are already present in the file, so it's in the target state. But let me systematically check the hard constraints to make sure there aren't any violations I missed. I'm searching through the content for prohibited phrases and concepts — the "delusional critic" term appears only in a citation context describing Lu & Schuurmans' work rather than our own mechanism, which should be acceptable, and I don't see "SGS delays collapse" anywhere. Now I need to verify the constraint about dt=1 imagination around line 198. I'm verifying all the numerical claims against the source data — the NVE ratios, baseline percentages, gradient distributions, and evaluation metrics all align with what was provided. The file already incorporates all six diffs and satisfies every constraint, so now I need to examine DIFF-M6 more closely to understand what it requires.

Looking at the ablation matrix structure, the task specifies a 3×2 layout comparing dt_embedding states (trained/frozen/removed) against subsample conditions, but the actual file uses a different table format with columns for embedding type, subsample setting, experiment ID, peak NVE, and outcome. I'm checking whether this alternative representation captures the same experimental comparisons or if the structure needs adjustment. The table format is clearer for publication anyway, so this layout difference is fine. All six diffs appear to be applied already, and the file content matches what was described in the reaudit document. Let me double-check the task header to confirm whether M4 and M5 were explicitly marked as applied or if they came from an earlier version.

Looking at the status line, it only calls out M2, M3, M6, and M7, but M4 and M5 content is definitely present in the file. The status line might have just omitted them. Let me verify the quality of the gradient decomposition section and the NVE analysis to make sure they're solid.

Checking the gradient breakdown table around lines 154-159, I see the observation decoders dominating at 93% (1.505), KL dynamics at 7% (0.119), and the continuation and reward heads contributing negligibly. The three key implications all check out: 016e is an architectural no-op, dt_emb is driven by observation reconstruction, and Full-SGS (018) is the correct intervention. But I notice the table seems to be missing the total row that should show 1.624 — let me verify that's actually there in the current file. The math checks out — the continuation head is negligible and the component values sum to the stated total of 1.624. Now I'm verifying the DIFF-M5 results, which show the model peaking at 326.7 before collapsing to 31.7 with an NVE spike of 10.42x at step 95K, and the write-up correctly frames this as an informative null result rather than evidence of delayed collapse.

I'm also doing a final sweep to confirm that the old "SGS delays collapse" interpretation has been completely removed from the file, since that framing was explicitly retracted. I'm comparing the before and after states of the file — the reaudit shows what method.md looked like originally, and the current version confirms all the changes have been applied. The section title changed from "Delusional Critic Hypothesis" to "Conditioning-Induced Value Overestimation," the wording around line 43 shifted to use "analogous to," and the mitigation section now includes the full collapse data for seed 2. I should update the status comment on line 3 to explicitly list all six diffs since they're all present in the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "7a974d9a-1eb5-451c-a573-8bddc24d59ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWqA1Qh6mLxCML8jBhhbnS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21246,
      "cache_read_input_tokens": 32102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21246
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

_source line 16_

All three files read. Now analyzing the current state of `method.md` against each of the 6 DIFFs.

The status line (line 3) says "DIFF-M6, DIFF-M7. DIFF-M2, DIFF-M3 already applied." — and examining the content, M4 (gradient decomposition, lines 150-167) and M5 (SGS negative, lines 169-180) are also present. Let me verify each DIFF systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "30b26512-179f-4f45-8d3b-371729a379bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWqA1Qh6mLxCML8jBhhbnS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21246,
      "cache_read_input_tokens": 32102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21246
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

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01JCMnDhAidgzChjcMBbBWKT`</summary>

```json
{
  "pattern": "delusional critic",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "3634fcc2-3bed-4953-a0e3-72c02a8e1b1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWqA1Qh6mLxCML8jBhhbnS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21246,
      "cache_read_input_tokens": 32102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21246
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

_source line 18 · 2026-05-16T04:54:09.841Z_

<details><summary>↩ Tool result · `toolu_01JCMnDhAidgzChjcMBbBWKT`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "42d05ee4-e0e5-4db5-a4a1-509b16f6a1fb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_011rQCNKoVio5DhYXRGcUNNN`</summary>

```json
{
  "pattern": "SGS delays|delays collapse",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "588e0c0c-fc35-44f6-9c61-7549f89618a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWqA1Qh6mLxCML8jBhhbnS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21246,
      "cache_read_input_tokens": 32102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21246
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

_source line 20 · 2026-05-16T04:54:10.733Z_

<details><summary>↩ Tool result · `toolu_011rQCNKoVio5DhYXRGcUNNN`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "e88bb2a2-8740-4144-a23a-84ce6f11f9dc",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ek1EJ9AnMPcZLEwzvzzExz`</summary>

```json
{
  "pattern": "mitigation|practical mitigation|zero-cost",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "fd17c208-6dbe-4a5b-ad49-accbb505c742",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWqA1Qh6mLxCML8jBhhbnS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21246,
      "cache_read_input_tokens": 32102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21246
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

_source line 22 · 2026-05-16T04:54:11.538Z_

<details><summary>↩ Tool result · `toolu_01Ek1EJ9AnMPcZLEwzvzzExz`</summary>

```text
198:**Implication.** Restricting imagination to $\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "1d6fba41-5ddf-4174-8370-a8138980a034",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "198:**Implication.** Restricting imagination to $\\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the hard constraints:

1. "delusional critic" — No matches ✅
2. "SGS delays collapse" — No matches ✅
3. "practical mitigation" / "zero-cost" — No matches. The one "mitigation" match is in "not a robust mitigation strategy" which is the correct anti-framing ✅

All 6 DIFFs are confirmed applied. The status line on line 3 just needs updating to reflect all 6 are done. Let me update it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "7c8e205e-7242-463e-b690-e879ed058395",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHsmQNYnPok6kxYSjpwqYb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5829,
      "cache_read_input_tokens": 53348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5829
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

_source line 24_

All hard constraints verified:
- "delusional critic": 0 occurrences ✅
- "SGS delays collapse": 0 occurrences ✅
- "mitigation" only appears in "not a robust mitigation strategy" (correct anti-framing) ✅

All 6 DIFFs (M2–M7) are already applied in the current file. The only issue is the status comment on line 3 doesn't list M4 and M5. Updating it for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "9fe1870d-2546-4bda-81bc-db00748cc350",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHsmQNYnPok6kxYSjpwqYb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5829,
      "cache_read_input_tokens": 53348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5829
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01NJddVxR11YrzEqh3HfeHau`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md",
  "old_string": "% Status: Updated 2026-05-16 — DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC/7-of-8). DIFF-M2, DIFF-M3 already applied.",
  "new_string": "% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "a29a6a57-bd0d-41ef-8094-1321edbbde61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHsmQNYnPok6kxYSjpwqYb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5829,
      "cache_read_input_tokens": 53348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5829
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

_source line 26 · 2026-05-16T04:54:20.578Z_

<details><summary>↩ Tool result · `toolu_01NJddVxR11YrzEqh3HfeHau`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "b9a13e07-6af8-439f-b6f1-dc3eb7228525",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md",
    "oldString": "% Status: Updated 2026-05-16 — DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC/7-of-8). DIFF-M2, DIFF-M3 already applied.",
    "newString": "% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).",
    "originalFile": "% Method — Draft v2\n% Target: CoRL 2026\n% Status: Updated 2026-05-16 — DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC/7-of-8). DIFF-M2, DIFF-M3 already applied.\n% Note: Complements experimental_setup.md (Section 4). Some overlap in\n%   diagnostic framework and factorial design is intentional—final paper\n%   may merge or redistribute content between Sections 3 and 4.\n\n# 3. Methodology\n\nWe present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \\citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \\citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.\n\n\n## 3.1 Background: DreamerV3 and Variable-Rate Imagination\n\n### World-Model Actor-Critic\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:\n\n$$h_{t+1} = f_\\theta(h_t, z_t, a_t), \\quad \\hat{z}_{t+1} \\sim p_\\theta(\\cdot \\mid h_{t+1})$$\n\nAn actor $\\pi_\\psi$ selects actions and a critic $V_\\xi$ estimates $\\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\\Delta t = 1$) and $H = 15$.\n\n### Temporal Abstraction via Variable-Rate Imagination\n\nTemporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \\citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.\n\nWe introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:\n\n**Temporal step-size embedding.** An embedding $e_{\\Delta t} \\in \\mathbb{R}^d$ conditions the RSSM transition on the step size:\n\n$$h_{t+\\Delta t} = f_\\theta(h_t, z_t, a_t, e_{\\Delta t})$$\n\nWe study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\\Delta t$ values; the untrained and removed configurations serve as controls.\n\n**Temporal subsampling.** When enabled, the replay buffer stores both $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\\Delta t{=}1$ transitions are used for world-model training.\n\n**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\\Delta t{=}1$ (standard) or $\\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.\n\n### Conditioning-Induced Value Overestimation (CIVO)\n\nWhen the RSSM predicts $\\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\\xi$ receives precise $\\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.\n\nWe term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \\& Schuurmans' \\citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\\Delta t}$ and the RSSM's degraded fidelity at $\\Delta t > 1$, not the policy's representational capacity.\n\n\n## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio\n\n### Motivation\n\nDistinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\\_001\\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.\n\n### Definition\n\n**Value-evaluation ratio.** At training step $k$:\n\n$$r_k = \\frac{\\bar{v}_k}{\\bar{R}_k}$$\n\nwhere $\\bar{v}_k$ is the mean predicted value across imagined states and $\\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.\n\n**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:\n\n$$\\hat{r}_k = \\frac{r_k^{\\,\\text{exp}}}{r_k^{\\,\\text{baseline}}}$$\n\nThis removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.\n\n### Diagnostic Thresholds\n\nWe calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:\n\n- **$\\hat{r}_k > 1.5$ (at $k \\geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\\_embedding conditions exceed 1.5$\\times$ at 35K+ steps (exp\\_008d seed 1: 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K; exp\\_009b seed 2: 1.62$\\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\\_008f seed 1 peak: 1.02$\\times$@25K; exp\\_009c seed 2 peak: 1.26$\\times$@25K).\n\n- **$0.8 \\leq \\hat{r}_k \\leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.\n\n- **$\\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.\n\n**Temporal validity constraint.** The NVE threshold applies only at $k \\geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\\_009b at 25K shows NVE = 2.05$\\times$ and exp\\_008e\\_v3 at 25K shows NVE = 1.93$\\times$, both artifacts of the baseline's $r_{25\\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.\n\n**Aggregate diagnostic power.** Evaluating the 1.5$\\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\\ref{tab:nve_sensitivity}). The single false positive is exp\\_008e\\_v3\\_s2, which exhibits late-onset NVE = 3.78$\\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \\S3.3. At a stricter threshold of 1.7$\\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).\n\n### Properties of the NVE Metric\n\nTwo properties make NVE informative for detecting the CIVO:\n\n**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\\_008d shows NVE = 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K $\\to$ 4.12$\\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\\_008a, exp\\_008f) show stable or declining NVE trajectories.\n\n**Collapse association.** Sustained NVE $>$ 1.5$\\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\\_008d seed 1: three consecutive checkpoints above 1.5$\\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\\_009b seed 2: 1.62$\\times$@45K $\\to$ 1.41$\\times$@55K $\\to$ 0.94$\\times$@65K, declining) does not lead to collapse. This pattern is consistent with a \"point of no return\" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.\n\n\n## 3.3 Causal Analysis Protocol\n\n### Design Rationale\n\nThis is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.\n\n### Factorial Structure\n\nWe vary three factors (temporal embedding type $\\times$ subsampling $\\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \\S4 for the complete configuration matrix). Rather than filling all cells of the $3 \\times 2 \\times 2$ grid, we prioritize the comparisons most informative for causal isolation.\n\n### Causal Chain and Its Tests\n\nThe causal chain under investigation is:\n\n$$\\text{trained } e_{\\Delta t} \\;\\xrightarrow{\\text{Link 1}}\\; \\text{pathological NVE} \\;\\xrightarrow{\\text{Link 2}}\\; \\text{actor exploitation} \\;\\xrightarrow{\\text{Link 3}}\\; \\text{performance collapse}$$\n\nEach link is tested by a specific controlled comparison:\n\n**Link 1: Trained dt\\_embedding $\\to$ pathological overestimation.** The comparison between exp\\_008d (trained dt\\_embedding, $d{=}32$) and exp\\_008f (removed dt\\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\\Delta t{=}2$ imagination). Exp\\_008d exhibits accelerating NVE (1.71$\\times$@35K $\\to$ 2.09$\\times$@45K), while exp\\_008f remains in the normal range (0.73$\\times$@35K $\\to$ 0.83$\\times$@45K). This is the primary causal evidence.\n\n**Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.\n\n**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n### 2$\\times$2 Ablation Matrix\n\nTo close the causal loop, we cross dt\\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:\n\n| dt\\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |\n|:---:|:---:|:---:|:---:|:---:|\n| Trained ($d{=}32$) | ON | 008d | 4.12$\\times$@55K (sustained $\\uparrow$) | CIVO $\\to$ collapse |\n| Trained ($d{=}32$) | OFF | 008a | 0.93$\\times$@55K | Stable, 85\\% baseline@105K |\n| Frozen ($d{=}32$) | ON | 015b | 1.45$\\times$@55K $\\to$ 0.65$\\times$@65K | Sub-threshold transient; gradient starvation collapse |\n| Removed ($d{=}0$) | ON | 008f | $\\leq$1.02$\\times$ | No CIVO |\n\nTrained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.\n\n### Supporting Analyses\n\n**Horizon effect (C5).** Exp\\_008c ($H{=}8$) vs. exp\\_008a ($H{=}15$), both with untrained dt\\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\\_008a: 778@105K; exp\\_008c: 241@65K plateau).\n\n**Temporal distance amplification (C4).** Exp\\_006 ($\\Delta t{=}2$, peak 485@35K $\\to$ collapse) vs. exp\\_007 ($\\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\\Delta t$, consistent with compounding RSSM prediction errors. Only two $\\Delta t$ values are tested; we report the monotonic trend (dt=1 $\\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.\n\n### RSSM Fidelity Analysis\n\nTo ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\\Delta t{=}1$ vs. $\\Delta t{=}2$ across three conditions (exp\\_rssm\\_fidelity\\_analysis):\n\n| Condition | $\\Delta t{=}1$ obs MSE | $\\Delta t{=}2$ obs MSE | Obs gap | $\\Delta t{=}1$ rew MAE | $\\Delta t{=}2$ rew MAE | Rew gap |\n|-----------|:---:|:---:|:---:|:---:|:---:|:---:|\n| Baseline (exp\\_001) | 13.49 | 27.50 | 2.04$\\times$ | 0.0102 | 0.0159 | 1.56$\\times$ |\n| 008d (trained emb) | 41.31 | 53.67 | 1.30$\\times$ | 0.0568 | 0.1579 | 2.78$\\times$ |\n| 008f (no emb) | 8.01 | 22.04 | 2.75$\\times$ | 0.7469 | 0.7526 | 1.01$\\times$ |\n\nTwo patterns are diagnostically relevant:\n\n1. **Trained embedding enables differentiated but biased reward predictions.** In exp\\_008d, the reward head produces sharply different predictions for $\\Delta t{=}1$ vs. $\\Delta t{=}2$ (reward gap 2.78$\\times$), but these differentiated predictions rest on poor absolute state quality ($\\Delta t{=}1$ obs MSE = 41.31, 3.1$\\times$ baseline). The critic receives confident but systematically biased reward signals at $\\Delta t{=}2$, fueling value overestimation.\n\n2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\\_008f, the reward head cannot distinguish $\\Delta t$ values (gap 1.01$\\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\\times$ baseline). Exp\\_008f is therefore a *causal control* that confirms the dt\\_embedding's role in overestimation, not a recommended configuration.\n\n**Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.\n\n### Gradient Decomposition of the Temporal Embedding\n\nTo identify which loss component drives $e_{\\Delta t}$'s learned representation, we decompose $\\nabla_\\theta e_{\\Delta t}$ by loss term using \\texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061).\n\n| Loss component | Gradient norm | Share (\\%) |\n|----------------|:---:|:---:|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93 |\n| KL dynamics | 0.119 | 7 |\n| Continuation head | $<$0.001 | $<$1 |\n| Reward head | 0.000 | 0 |\n\nThe temporal embedding receives 93\\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). Three implications follow:\n\n1. **Exp\\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.\n\n2. **$e_{\\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.\n\n3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\\% contribution from observation decoders. This motivates the full SGS design (exp\\_018), which detaches $e_{\\Delta t}$ from all non-KL gradient pathways.\n\n### Stop-Gradient Surgery: An Informative Negative (exp\\_016e)\n\\label{sec:sgs_negative}\n\nThe gradient decomposition above was motivated by a null result: exp\\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\\Delta t}$.\n\n**Configuration.** Exp\\_016e replicates exp\\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\\Delta t}$, subsampling ON, $H{=}8$, $\\Delta t{=}2$ imagination) with one modification: \\texttt{reward\\_dt\\_emb\\_detach=True}, which applies $\\text{sg}(\\cdot)$ to $e_{\\Delta t}$ before the reward head during the backward pass.\n\n**Results.** Exp\\_016e collapses in the same qualitative pattern as exp\\_008d. Peak eval return reaches 326.7 at 75K (exp\\_016e), then drops to 31.7 by 95K---a 90.3\\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\\times$ at 95K (exp\\_016e). The timing difference relative to exp\\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.\n\n**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\\ 1 scalar reward) dominates the gradient signal to $e_{\\Delta t}$ by two orders of magnitude.\n\n**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\n### Imagination Step Size as Causal Variable\n\nThe factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:\n\n**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**$\\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\\_008e\\_v3\\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\\_008e\\_v3\\_s2), with NVE = 3.78$\\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\\_008e\\_v3\\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\\_008d.\n\n**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:\n\n- *Pathway A (CIVO):* Trained dt\\_embedding + $\\Delta t{>}1$ imagination $\\to$ value overestimation (NVE $\\uparrow$) $\\to$ actor over-exploitation (entropy $\\downarrow$) $\\to$ performance collapse. Observed in exp\\_008d (seed 1) and exp\\_009b (seed 2, transient).\n\n- *Pathway B (non-CIVO):* $\\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\\_008e\\_v3\\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.\n\nTo rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\\_009a), comparable to seed 1's 915.67 (exp\\_001\\_baseline). The collapse in exp\\_008e\\_v3\\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.\n\n**Implication.** Restricting imagination to $\\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " % Method — Draft v2",
          " % Target: CoRL 2026",
          "-% Status: Updated 2026-05-16 — DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC/7-of-8). DIFF-M2, DIFF-M3 already applied.",
          "+% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).",
          " % Note: Complements experimental_setup.md (Section 4). Some overlap in",
          " %   diagnostic framework and factorial design is intentional—final paper",
          " %   may merge or redistribute content between Sections 3 and 4."
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

_source line 27_

Now let me do a final read to confirm full consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "fccb6e6e-fc2e-4b21-850a-c7bc16c48f1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fx5P8nwSsewAPcJD3gaY3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 59177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01RhWy8bnQGUZfM8Ng3dhSJL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "d7c2f723-ad68-4b10-9a4a-485329cbc353",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fx5P8nwSsewAPcJD3gaY3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 59177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 29 · 2026-05-16T04:54:23.466Z_

<details><summary>↩ Tool result · `toolu_01RhWy8bnQGUZfM8Ng3dhSJL`</summary>

```text
1	% Method — Draft v2
2	% Target: CoRL 2026
3	% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).
4	% Note: Complements experimental_setup.md (Section 4). Some overlap in
5	%   diagnostic framework and factorial design is intentional—final paper
6	%   may merge or redistribute content between Sections 3 and 4.
7	
8	# 3. Methodology
9	
10	We present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.
11	
12	
13	## 3.1 Background: DreamerV3 and Variable-Rate Imagination
14	
15	### World-Model Actor-Critic
16	
17	DreamerV3 \citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:
18	
19	$$h_{t+1} = f_\theta(h_t, z_t, a_t), \quad \hat{z}_{t+1} \sim p_\theta(\cdot \mid h_{t+1})$$
20	
21	An actor $\pi_\psi$ selects actions and a critic $V_\xi$ estimates $\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\Delta t = 1$) and $H = 15$.
22	
23	### Temporal Abstraction via Variable-Rate Imagination
24	
25	Temporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.
26	
27	We introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:
28	
29	**Temporal step-size embedding.** An embedding $e_{\Delta t} \in \mathbb{R}^d$ conditions the RSSM transition on the step size:
30	
31	$$h_{t+\Delta t} = f_\theta(h_t, z_t, a_t, e_{\Delta t})$$
32	
33	We study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\Delta t$ values; the untrained and removed configurations serve as controls.
34	
35	**Temporal subsampling.** When enabled, the replay buffer stores both $\Delta t{=}1$ and $\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\Delta t{=}1$ transitions are used for world-model training.
36	
37	**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\Delta t{=}1$ (standard) or $\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.
38	
39	### Conditioning-Induced Value Overestimation (CIVO)
40	
41	When the RSSM predicts $\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\xi$ receives precise $\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.
42	
43	We term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \& Schuurmans' \citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\Delta t}$ and the RSSM's degraded fidelity at $\Delta t > 1$, not the policy's representational capacity.
44	
45	
46	## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio
47	
48	### Motivation
49	
50	Distinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\_001\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.
51	
52	### Definition
53	
54	**Value-evaluation ratio.** At training step $k$:
55	
56	$$r_k = \frac{\bar{v}_k}{\bar{R}_k}$$
57	
58	where $\bar{v}_k$ is the mean predicted value across imagined states and $\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.
59	
60	**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:
61	
62	$$\hat{r}_k = \frac{r_k^{\,\text{exp}}}{r_k^{\,\text{baseline}}}$$
63	
64	This removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.
65	
66	### Diagnostic Thresholds
67	
68	We calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:
69	
70	- **$\hat{r}_k > 1.5$ (at $k \geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\_embedding conditions exceed 1.5$\times$ at 35K+ steps (exp\_008d seed 1: 1.71$\times$@35K $\to$ 2.09$\times$@45K; exp\_009b seed 2: 1.62$\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\_008f seed 1 peak: 1.02$\times$@25K; exp\_009c seed 2 peak: 1.26$\times$@25K).
71	
72	- **$0.8 \leq \hat{r}_k \leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.
73	
74	- **$\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.
75	
76	**Temporal validity constraint.** The NVE threshold applies only at $k \geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\_009b at 25K shows NVE = 2.05$\times$ and exp\_008e\_v3 at 25K shows NVE = 1.93$\times$, both artifacts of the baseline's $r_{25\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.
77	
78	**Aggregate diagnostic power.** Evaluating the 1.5$\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\ref{tab:nve_sensitivity}). The single false positive is exp\_008e\_v3\_s2, which exhibits late-onset NVE = 3.78$\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \S3.3. At a stricter threshold of 1.7$\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).
79	
80	### Properties of the NVE Metric
81	
82	Two properties make NVE informative for detecting the CIVO:
83	
84	**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\_008d shows NVE = 1.71$\times$@35K $\to$ 2.09$\times$@45K $\to$ 4.12$\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\_008a, exp\_008f) show stable or declining NVE trajectories.
85	
86	**Collapse association.** Sustained NVE $>$ 1.5$\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\_008d seed 1: three consecutive checkpoints above 1.5$\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\_009b seed 2: 1.62$\times$@45K $\to$ 1.41$\times$@55K $\to$ 0.94$\times$@65K, declining) does not lead to collapse. This pattern is consistent with a "point of no return" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.
87	
88	
89	## 3.3 Causal Analysis Protocol
90	
91	### Design Rationale
92	
93	This is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.
94	
95	### Factorial Structure
96	
97	We vary three factors (temporal embedding type $\times$ subsampling $\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \S4 for the complete configuration matrix). Rather than filling all cells of the $3 \times 2 \times 2$ grid, we prioritize the comparisons most informative for causal isolation.
98	
99	### Causal Chain and Its Tests
100	
101	The causal chain under investigation is:
102	
103	$$\text{trained } e_{\Delta t} \;\xrightarrow{\text{Link 1}}\; \text{pathological NVE} \;\xrightarrow{\text{Link 2}}\; \text{actor exploitation} \;\xrightarrow{\text{Link 3}}\; \text{performance collapse}$$
104	
105	Each link is tested by a specific controlled comparison:
106	
107	**Link 1: Trained dt\_embedding $\to$ pathological overestimation.** The comparison between exp\_008d (trained dt\_embedding, $d{=}32$) and exp\_008f (removed dt\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\Delta t{=}2$ imagination). Exp\_008d exhibits accelerating NVE (1.71$\times$@35K $\to$ 2.09$\times$@45K), while exp\_008f remains in the normal range (0.73$\times$@35K $\to$ 0.83$\times$@45K). This is the primary causal evidence.
108	
109	**Link 2: Sustained overestimation $\to$ collapse (stochastic).** Multi-seed replication of exp\_008d reveals that the NVE $>$ 1.5$\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\_008d) shows sustained NVE $>$ 1.5$\times$ across three checkpoints and collapses; seed 2 (exp\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.
110	
111	**Link 3: Imagination $\Delta t$ as the critical variable.** Exp\_008e\_v3 uses a trained dt\_embedding (identical to exp\_008d and exp\_006) but restricts imagination rollouts to $\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\_008e\_v3, seed 1) with NVE = 0.80$\times$ (healthy). The contrast with exp\_006 (same trained dt\_embedding, subsample ON, $H{=}15$, but $\Delta t{=}2$ imagination $\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\Delta t > 1$ predictions during imagination.
112	
113	### 2$\times$2 Ablation Matrix
114	
115	To close the causal loop, we cross dt\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:
116	
117	| dt\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |
118	|:---:|:---:|:---:|:---:|:---:|
119	| Trained ($d{=}32$) | ON | 008d | 4.12$\times$@55K (sustained $\uparrow$) | CIVO $\to$ collapse |
120	| Trained ($d{=}32$) | OFF | 008a | 0.93$\times$@55K | Stable, 85\% baseline@105K |
121	| Frozen ($d{=}32$) | ON | 015b | 1.45$\times$@55K $\to$ 0.65$\times$@65K | Sub-threshold transient; gradient starvation collapse |
122	| Removed ($d{=}0$) | ON | 008f | $\leq$1.02$\times$ | No CIVO |
123	
124	Trained dt\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\_015b: peak 1.45$\times$@55K) that self-corrects to 0.65$\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\times$. The subsample-OFF condition (exp\_008a) confirms that a trained embedding without exposure to $\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.
125	
126	### Supporting Analyses
127	
128	**Horizon effect (C5).** Exp\_008c ($H{=}8$) vs. exp\_008a ($H{=}15$), both with untrained dt\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\_008a: 778@105K; exp\_008c: 241@65K plateau).
129	
130	**Temporal distance amplification (C4).** Exp\_006 ($\Delta t{=}2$, peak 485@35K $\to$ collapse) vs. exp\_007 ($\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\Delta t$, consistent with compounding RSSM prediction errors. Only two $\Delta t$ values are tested; we report the monotonic trend (dt=1 $\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.
131	
132	### RSSM Fidelity Analysis
133	
134	To ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\Delta t{=}1$ vs. $\Delta t{=}2$ across three conditions (exp\_rssm\_fidelity\_analysis):
135	
136	| Condition | $\Delta t{=}1$ obs MSE | $\Delta t{=}2$ obs MSE | Obs gap | $\Delta t{=}1$ rew MAE | $\Delta t{=}2$ rew MAE | Rew gap |
137	|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
138	| Baseline (exp\_001) | 13.49 | 27.50 | 2.04$\times$ | 0.0102 | 0.0159 | 1.56$\times$ |
139	| 008d (trained emb) | 41.31 | 53.67 | 1.30$\times$ | 0.0568 | 0.1579 | 2.78$\times$ |
140	| 008f (no emb) | 8.01 | 22.04 | 2.75$\times$ | 0.7469 | 0.7526 | 1.01$\times$ |
141	
142	Two patterns are diagnostically relevant:
143	
144	1. **Trained embedding enables differentiated but biased reward predictions.** In exp\_008d, the reward head produces sharply different predictions for $\Delta t{=}1$ vs. $\Delta t{=}2$ (reward gap 2.78$\times$), but these differentiated predictions rest on poor absolute state quality ($\Delta t{=}1$ obs MSE = 41.31, 3.1$\times$ baseline). The critic receives confident but systematically biased reward signals at $\Delta t{=}2$, fueling value overestimation.
145	
146	2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\_008f, the reward head cannot distinguish $\Delta t$ values (gap 1.01$\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\times$ baseline). Exp\_008f is therefore a *causal control* that confirms the dt\_embedding's role in overestimation, not a recommended configuration.
147	
148	**Caveat on obs gap ratios.** Exp\_008d's low obs gap ratio (1.30$\times$) is misleading---its $\Delta t{=}1$ absolute error is already 3.1$\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.
149	
150	### Gradient Decomposition of the Temporal Embedding
151	
152	To identify which loss component drives $e_{\Delta t}$'s learned representation, we decompose $\nabla_\theta e_{\Delta t}$ by loss term using \texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061).
153	
154	| Loss component | Gradient norm | Share (\%) |
155	|----------------|:---:|:---:|
156	| Observation decoders (orientations, velocity, height) | 1.505 | 93 |
157	| KL dynamics | 0.119 | 7 |
158	| Continuation head | $<$0.001 | $<$1 |
159	| Reward head | 0.000 | 0 |
160	
161	The temporal embedding receives 93\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). Three implications follow:
162	
163	1. **Exp\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.
164	
165	2. **$e_{\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.
166	
167	3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\% contribution from observation decoders. This motivates the full SGS design (exp\_018), which detaches $e_{\Delta t}$ from all non-KL gradient pathways.
168	
169	### Stop-Gradient Surgery: An Informative Negative (exp\_016e)
170	\label{sec:sgs_negative}
171	
172	The gradient decomposition above was motivated by a null result: exp\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\Delta t}$.
173	
174	**Configuration.** Exp\_016e replicates exp\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\Delta t}$, subsampling ON, $H{=}8$, $\Delta t{=}2$ imagination) with one modification: \texttt{reward\_dt\_emb\_detach=True}, which applies $\text{sg}(\cdot)$ to $e_{\Delta t}$ before the reward head during the backward pass.
175	
176	**Results.** Exp\_016e collapses in the same qualitative pattern as exp\_008d. Peak eval return reaches 326.7 at 75K (exp\_016e), then drops to 31.7 by 95K---a 90.3\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\times$ at 95K (exp\_016e). The timing difference relative to exp\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.
177	
178	**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\ 1 scalar reward) dominates the gradient signal to $e_{\Delta t}$ by two orders of magnitude.
179	
180	**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\% of the gradient flow to $e_{\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\_018) or by restructuring how $e_{\Delta t}$ interacts with the RSSM transition function.
181	
182	### Imagination Step Size as Causal Variable
183	
184	The factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:
185	
186	**$\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\_008e\_v3 uses the same trained dt\_embedding and multi-rate training data as exp\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\_008e\_v3, seed 1), 95\% of baseline (exp\_001\_baseline: 915.67@105K), with NVE = 0.80$\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\Delta t > 1$ predictions during imagination.
187	
188	**$\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\_008e\_v3\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\_008e\_v3\_s2), with NVE = 3.78$\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\_008e\_v3\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\_008d.
189	
190	**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:
191	
192	- *Pathway A (CIVO):* Trained dt\_embedding + $\Delta t{>}1$ imagination $\to$ value overestimation (NVE $\uparrow$) $\to$ actor over-exploitation (entropy $\downarrow$) $\to$ performance collapse. Observed in exp\_008d (seed 1) and exp\_009b (seed 2, transient).
193	
194	- *Pathway B (non-CIVO):* $\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\_008e\_v3\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.
195	
196	To rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\_009a), comparable to seed 1's 915.67 (exp\_001\_baseline). The collapse in exp\_008e\_v3\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.
197	
198	**Implication.** Restricting imagination to $\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "40f4e9af-6e1f-42ee-8156-3605d390aa07",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md",
      "content": "% Method — Draft v2\n% Target: CoRL 2026\n% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).\n% Note: Complements experimental_setup.md (Section 4). Some overlap in\n%   diagnostic framework and factorial design is intentional—final paper\n%   may merge or redistribute content between Sections 3 and 4.\n\n# 3. Methodology\n\nWe present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \\citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \\citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.\n\n\n## 3.1 Background: DreamerV3 and Variable-Rate Imagination\n\n### World-Model Actor-Critic\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:\n\n$$h_{t+1} = f_\\theta(h_t, z_t, a_t), \\quad \\hat{z}_{t+1} \\sim p_\\theta(\\cdot \\mid h_{t+1})$$\n\nAn actor $\\pi_\\psi$ selects actions and a critic $V_\\xi$ estimates $\\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\\Delta t = 1$) and $H = 15$.\n\n### Temporal Abstraction via Variable-Rate Imagination\n\nTemporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \\citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.\n\nWe introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:\n\n**Temporal step-size embedding.** An embedding $e_{\\Delta t} \\in \\mathbb{R}^d$ conditions the RSSM transition on the step size:\n\n$$h_{t+\\Delta t} = f_\\theta(h_t, z_t, a_t, e_{\\Delta t})$$\n\nWe study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\\Delta t$ values; the untrained and removed configurations serve as controls.\n\n**Temporal subsampling.** When enabled, the replay buffer stores both $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\\Delta t{=}1$ transitions are used for world-model training.\n\n**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\\Delta t{=}1$ (standard) or $\\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.\n\n### Conditioning-Induced Value Overestimation (CIVO)\n\nWhen the RSSM predicts $\\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\\xi$ receives precise $\\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.\n\nWe term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \\& Schuurmans' \\citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\\Delta t}$ and the RSSM's degraded fidelity at $\\Delta t > 1$, not the policy's representational capacity.\n\n\n## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio\n\n### Motivation\n\nDistinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\\_001\\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.\n\n### Definition\n\n**Value-evaluation ratio.** At training step $k$:\n\n$$r_k = \\frac{\\bar{v}_k}{\\bar{R}_k}$$\n\nwhere $\\bar{v}_k$ is the mean predicted value across imagined states and $\\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.\n\n**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:\n\n$$\\hat{r}_k = \\frac{r_k^{\\,\\text{exp}}}{r_k^{\\,\\text{baseline}}}$$\n\nThis removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.\n\n### Diagnostic Thresholds\n\nWe calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:\n\n- **$\\hat{r}_k > 1.5$ (at $k \\geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\\_embedding conditions exceed 1.5$\\times$ at 35K+ steps (exp\\_008d seed 1: 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K; exp\\_009b seed 2: 1.62$\\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\\_008f seed 1 peak: 1.02$\\times$@25K; exp\\_009c seed 2 peak: 1.26$\\times$@25K).\n\n- **$0.8 \\leq \\hat{r}_k \\leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.\n\n- **$\\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.\n\n**Temporal validity constraint.** The NVE threshold applies only at $k \\geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\\_009b at 25K shows NVE = 2.05$\\times$ and exp\\_008e\\_v3 at 25K shows NVE = 1.93$\\times$, both artifacts of the baseline's $r_{25\\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.\n\n**Aggregate diagnostic power.** Evaluating the 1.5$\\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\\ref{tab:nve_sensitivity}). The single false positive is exp\\_008e\\_v3\\_s2, which exhibits late-onset NVE = 3.78$\\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \\S3.3. At a stricter threshold of 1.7$\\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).\n\n### Properties of the NVE Metric\n\nTwo properties make NVE informative for detecting the CIVO:\n\n**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\\_008d shows NVE = 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K $\\to$ 4.12$\\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\\_008a, exp\\_008f) show stable or declining NVE trajectories.\n\n**Collapse association.** Sustained NVE $>$ 1.5$\\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\\_008d seed 1: three consecutive checkpoints above 1.5$\\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\\_009b seed 2: 1.62$\\times$@45K $\\to$ 1.41$\\times$@55K $\\to$ 0.94$\\times$@65K, declining) does not lead to collapse. This pattern is consistent with a \"point of no return\" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.\n\n\n## 3.3 Causal Analysis Protocol\n\n### Design Rationale\n\nThis is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.\n\n### Factorial Structure\n\nWe vary three factors (temporal embedding type $\\times$ subsampling $\\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \\S4 for the complete configuration matrix). Rather than filling all cells of the $3 \\times 2 \\times 2$ grid, we prioritize the comparisons most informative for causal isolation.\n\n### Causal Chain and Its Tests\n\nThe causal chain under investigation is:\n\n$$\\text{trained } e_{\\Delta t} \\;\\xrightarrow{\\text{Link 1}}\\; \\text{pathological NVE} \\;\\xrightarrow{\\text{Link 2}}\\; \\text{actor exploitation} \\;\\xrightarrow{\\text{Link 3}}\\; \\text{performance collapse}$$\n\nEach link is tested by a specific controlled comparison:\n\n**Link 1: Trained dt\\_embedding $\\to$ pathological overestimation.** The comparison between exp\\_008d (trained dt\\_embedding, $d{=}32$) and exp\\_008f (removed dt\\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\\Delta t{=}2$ imagination). Exp\\_008d exhibits accelerating NVE (1.71$\\times$@35K $\\to$ 2.09$\\times$@45K), while exp\\_008f remains in the normal range (0.73$\\times$@35K $\\to$ 0.83$\\times$@45K). This is the primary causal evidence.\n\n**Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.\n\n**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n### 2$\\times$2 Ablation Matrix\n\nTo close the causal loop, we cross dt\\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:\n\n| dt\\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |\n|:---:|:---:|:---:|:---:|:---:|\n| Trained ($d{=}32$) | ON | 008d | 4.12$\\times$@55K (sustained $\\uparrow$) | CIVO $\\to$ collapse |\n| Trained ($d{=}32$) | OFF | 008a | 0.93$\\times$@55K | Stable, 85\\% baseline@105K |\n| Frozen ($d{=}32$) | ON | 015b | 1.45$\\times$@55K $\\to$ 0.65$\\times$@65K | Sub-threshold transient; gradient starvation collapse |\n| Removed ($d{=}0$) | ON | 008f | $\\leq$1.02$\\times$ | No CIVO |\n\nTrained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.\n\n### Supporting Analyses\n\n**Horizon effect (C5).** Exp\\_008c ($H{=}8$) vs. exp\\_008a ($H{=}15$), both with untrained dt\\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\\_008a: 778@105K; exp\\_008c: 241@65K plateau).\n\n**Temporal distance amplification (C4).** Exp\\_006 ($\\Delta t{=}2$, peak 485@35K $\\to$ collapse) vs. exp\\_007 ($\\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\\Delta t$, consistent with compounding RSSM prediction errors. Only two $\\Delta t$ values are tested; we report the monotonic trend (dt=1 $\\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.\n\n### RSSM Fidelity Analysis\n\nTo ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\\Delta t{=}1$ vs. $\\Delta t{=}2$ across three conditions (exp\\_rssm\\_fidelity\\_analysis):\n\n| Condition | $\\Delta t{=}1$ obs MSE | $\\Delta t{=}2$ obs MSE | Obs gap | $\\Delta t{=}1$ rew MAE | $\\Delta t{=}2$ rew MAE | Rew gap |\n|-----------|:---:|:---:|:---:|:---:|:---:|:---:|\n| Baseline (exp\\_001) | 13.49 | 27.50 | 2.04$\\times$ | 0.0102 | 0.0159 | 1.56$\\times$ |\n| 008d (trained emb) | 41.31 | 53.67 | 1.30$\\times$ | 0.0568 | 0.1579 | 2.78$\\times$ |\n| 008f (no emb) | 8.01 | 22.04 | 2.75$\\times$ | 0.7469 | 0.7526 | 1.01$\\times$ |\n\nTwo patterns are diagnostically relevant:\n\n1. **Trained embedding enables differentiated but biased reward predictions.** In exp\\_008d, the reward head produces sharply different predictions for $\\Delta t{=}1$ vs. $\\Delta t{=}2$ (reward gap 2.78$\\times$), but these differentiated predictions rest on poor absolute state quality ($\\Delta t{=}1$ obs MSE = 41.31, 3.1$\\times$ baseline). The critic receives confident but systematically biased reward signals at $\\Delta t{=}2$, fueling value overestimation.\n\n2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\\_008f, the reward head cannot distinguish $\\Delta t$ values (gap 1.01$\\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\\times$ baseline). Exp\\_008f is therefore a *causal control* that confirms the dt\\_embedding's role in overestimation, not a recommended configuration.\n\n**Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.\n\n### Gradient Decomposition of the Temporal Embedding\n\nTo identify which loss component drives $e_{\\Delta t}$'s learned representation, we decompose $\\nabla_\\theta e_{\\Delta t}$ by loss term using \\texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061).\n\n| Loss component | Gradient norm | Share (\\%) |\n|----------------|:---:|:---:|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93 |\n| KL dynamics | 0.119 | 7 |\n| Continuation head | $<$0.001 | $<$1 |\n| Reward head | 0.000 | 0 |\n\nThe temporal embedding receives 93\\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). Three implications follow:\n\n1. **Exp\\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.\n\n2. **$e_{\\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.\n\n3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\\% contribution from observation decoders. This motivates the full SGS design (exp\\_018), which detaches $e_{\\Delta t}$ from all non-KL gradient pathways.\n\n### Stop-Gradient Surgery: An Informative Negative (exp\\_016e)\n\\label{sec:sgs_negative}\n\nThe gradient decomposition above was motivated by a null result: exp\\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\\Delta t}$.\n\n**Configuration.** Exp\\_016e replicates exp\\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\\Delta t}$, subsampling ON, $H{=}8$, $\\Delta t{=}2$ imagination) with one modification: \\texttt{reward\\_dt\\_emb\\_detach=True}, which applies $\\text{sg}(\\cdot)$ to $e_{\\Delta t}$ before the reward head during the backward pass.\n\n**Results.** Exp\\_016e collapses in the same qualitative pattern as exp\\_008d. Peak eval return reaches 326.7 at 75K (exp\\_016e), then drops to 31.7 by 95K---a 90.3\\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\\times$ at 95K (exp\\_016e). The timing difference relative to exp\\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.\n\n**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\\ 1 scalar reward) dominates the gradient signal to $e_{\\Delta t}$ by two orders of magnitude.\n\n**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\n### Imagination Step Size as Causal Variable\n\nThe factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:\n\n**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**$\\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\\_008e\\_v3\\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\\_008e\\_v3\\_s2), with NVE = 3.78$\\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\\_008e\\_v3\\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\\_008d.\n\n**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:\n\n- *Pathway A (CIVO):* Trained dt\\_embedding + $\\Delta t{>}1$ imagination $\\to$ value overestimation (NVE $\\uparrow$) $\\to$ actor over-exploitation (entropy $\\downarrow$) $\\to$ performance collapse. Observed in exp\\_008d (seed 1) and exp\\_009b (seed 2, transient).\n\n- *Pathway B (non-CIVO):* $\\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\\_008e\\_v3\\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.\n\nTo rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\\_009a), comparable to seed 1's 915.67 (exp\\_001\\_baseline). The collapse in exp\\_008e\\_v3\\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.\n\n**Implication.** Restricting imagination to $\\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.\n",
      "numLines": 199,
      "startLine": 1,
      "totalLines": 199
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
All 6 DIFFs are confirmed applied and consistent. Let me verify one more thing - the cross-reference in line 176 says "Section~\ref{sec:gradient_decomposition}" but I don't see a corresponding \label for the gradient decomposition section. The label for SGS negative is on line 170: `\label{sec:sgs_negative}`. But line 163 references `Section~\ref{sec:sgs_negative}` and line 176 references `Section~\ref{sec:gradient_decomposition}`. 

Wait, there's no `\label{sec:gradient_decomposition}` in the file! Line 176 references it but it doesn't exist. This is a broken cross-reference.


I need to add the missing label to the gradient decomposition section at line 150, right after the heading, to match the pattern used for the SGS negative section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "60e3e69d-cab9-4b6a-95fc-aa5d1dc140a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRyJDfKjRpykKk7e6zEfbe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7538,
      "cache_read_input_tokens": 59801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7538
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

One issue: line 176 references `Section~\ref{sec:gradient_decomposition}` but there's no corresponding `\label`. Adding it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "faf70efe-a87b-48c3-a003-a2cc6953885f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRyJDfKjRpykKk7e6zEfbe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7538,
      "cache_read_input_tokens": 59801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7538
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Pq7hLj21ZWiWZFCV1ub2Dr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md",
  "old_string": "### Gradient Decomposition of the Temporal Embedding\n\nTo identify which loss component",
  "new_string": "### Gradient Decomposition of the Temporal Embedding\n\\label{sec:gradient_decomposition}\n\nTo identify which loss component"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "5263f1ca-57ed-4aef-b52e-777190a40e40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRyJDfKjRpykKk7e6zEfbe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7538,
      "cache_read_input_tokens": 59801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7538
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

_source line 33 · 2026-05-16T04:54:35.462Z_

<details><summary>↩ Tool result · `toolu_01Pq7hLj21ZWiWZFCV1ub2Dr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "5dfcfe05-8822-4203-a906-c8fa2b9ae246",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/method.md",
    "oldString": "### Gradient Decomposition of the Temporal Embedding\n\nTo identify which loss component",
    "newString": "### Gradient Decomposition of the Temporal Embedding\n\\label{sec:gradient_decomposition}\n\nTo identify which loss component",
    "originalFile": "% Method — Draft v2\n% Target: CoRL 2026\n% Status: Updated 2026-05-16 — All 6 Framing B diffs applied: DIFF-M2 (CIVO heading), DIFF-M3 (imagination causal variable), DIFF-M4 (gradient decomposition), DIFF-M5 (SGS informative negative), DIFF-M6 (2×2 ablation matrix), DIFF-M7 (NVE AUROC=0.933, 7/8).\n% Note: Complements experimental_setup.md (Section 4). Some overlap in\n%   diagnostic framework and factorial design is intentional—final paper\n%   may merge or redistribute content between Sections 3 and 4.\n\n# 3. Methodology\n\nWe present a systematic diagnostic methodology for identifying why variable-rate imagination fails in world-model reinforcement learning. Our approach combines (i) controlled factorial experiments that isolate individual causal factors, (ii) a normalized diagnostic metric that separates pathological value overestimation from benign overshoot, and (iii) a world-model fidelity analysis that grounds the failure mechanism in prediction error. All experiments use DreamerV3 \\citep{hafner2023dreamerv3} on Walker Walk from the DeepMind Control Suite \\citep{tassa2018deepmind}; we scope claims to this architecture and report single-environment results throughout.\n\n\n## 3.1 Background: DreamerV3 and Variable-Rate Imagination\n\n### World-Model Actor-Critic\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a latent dynamics model---the Recurrent State-Space Model (RSSM)---from environment interactions and trains an actor-critic entirely within imagined trajectories. The RSSM maintains a latent state $s_t = (h_t, z_t)$ consisting of a deterministic recurrent component $h_t$ and a stochastic discrete representation $z_t$. At each imagination step, the model predicts:\n\n$$h_{t+1} = f_\\theta(h_t, z_t, a_t), \\quad \\hat{z}_{t+1} \\sim p_\\theta(\\cdot \\mid h_{t+1})$$\n\nAn actor $\\pi_\\psi$ selects actions and a critic $V_\\xi$ estimates $\\lambda$-returns, both trained on imagined trajectories of horizon $H$ steps. In the standard configuration, each imagination step corresponds to one environment transition ($\\Delta t = 1$) and $H = 15$.\n\n### Temporal Abstraction via Variable-Rate Imagination\n\nTemporal abstraction---reasoning at multiple timescales---is a longstanding goal in RL \\citep{sutton1999options, precup2000temporal}. World-model RL provides a natural setting: by setting the imagination step size $\\Delta t > 1$, the agent can plan over longer temporal horizons without increasing the number of imagination steps. An $H$-step rollout at $\\Delta t = 2$ covers $2H$ environment steps of lookahead at the same computational cost as the standard $H$-step rollout.\n\nWe introduce three modifications to the DreamerV3 imagination pipeline, each independently controllable:\n\n**Temporal step-size embedding.** An embedding $e_{\\Delta t} \\in \\mathbb{R}^d$ conditions the RSSM transition on the step size:\n\n$$h_{t+\\Delta t} = f_\\theta(h_t, z_t, a_t, e_{\\Delta t})$$\n\nWe study three configurations: *trained* ($d{=}32$, jointly optimized with the world model), *untrained* ($d{=}32$, randomly initialized and frozen), and *removed* ($d{=}0$, no temporal conditioning). The trained embedding enables the RSSM to specialize predictions for different $\\Delta t$ values; the untrained and removed configurations serve as controls.\n\n**Temporal subsampling.** When enabled, the replay buffer stores both $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (constructed by skipping alternate frames), exposing the RSSM to multi-rate dynamics during training. When disabled, only $\\Delta t{=}1$ transitions are used for world-model training.\n\n**Imagination step size.** During actor-critic optimization, imagination rollouts use a fixed step size: $\\Delta t{=}1$ (standard) or $\\Delta t{>}1$ (variable-rate). This factor is independently controllable from the world model's training data composition.\n\n### Conditioning-Induced Value Overestimation (CIVO)\n\nWhen the RSSM predicts $\\Delta t > 1$ transitions, it must extrapolate over a larger temporal gap, and state prediction fidelity degrades. With a trained temporal embedding, the critic $V_\\xi$ receives precise $\\Delta t$ information and can exploit the model's confident but inaccurate multi-step predictions to form systematically optimistic value estimates. If these overestimates persistently exceed achievable returns, the actor pursues policies that are optimal under the model but suboptimal in reality.\n\nWe term this *conditioning-induced value overestimation (CIVO)*. The mechanism is analogous to Lu \\& Schuurmans' \\citep{lu2018nondelusional} delusional policies, where function approximation introduces inconsistencies in Q-learning backups, but the source differs: Lu et al.'s delusions are *policy-class-induced* (the policy's functional form cannot represent consistent backups), whereas CIVO is *model-induced* (the world model's temporal extrapolation error produces systematically biased latent states that the critic treats as accurate). The delusion source is the conditioning signal $e_{\\Delta t}$ and the RSSM's degraded fidelity at $\\Delta t > 1$, not the policy's representational capacity.\n\n\n## 3.2 Diagnostic Framework: Normalized Value-Evaluation Ratio\n\n### Motivation\n\nDistinguishing pathological from benign value overestimation is the central diagnostic challenge. Even the standard DreamerV3 baseline exhibits value overshoot during training: at step 25K, the baseline's value-evaluation ratio is 0.087 (exp\\_001\\_baseline), rising to 0.656 by 105K as the critic converges. Any diagnostic metric must remove this baseline trend to isolate the *excess* overestimation attributable to variable-rate imagination.\n\n### Definition\n\n**Value-evaluation ratio.** At training step $k$:\n\n$$r_k = \\frac{\\bar{v}_k}{\\bar{R}_k}$$\n\nwhere $\\bar{v}_k$ is the mean predicted value across imagined states and $\\bar{R}_k$ is the mean evaluation return over 10 episodes. This measures how closely the critic's estimates track achievable performance.\n\n**Normalized value-evaluation ratio (NVE).** We normalize by the baseline's ratio at the same step:\n\n$$\\hat{r}_k = \\frac{r_k^{\\,\\text{exp}}}{r_k^{\\,\\text{baseline}}}$$\n\nThis removes the baseline's own overshoot trend, isolating excess overestimation. We normalize all v/e ratios against exp\\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X.\n\n### Diagnostic Thresholds\n\nWe calibrate thresholds from the observed separation between experimental conditions. We emphasize that these serve as empirical *markers*, not formal hypothesis tests---they are calibrated and evaluated on the same experiments:\n\n- **$\\hat{r}_k > 1.5$ (at $k \\geq$ 35K)**: **Pathological overestimation.** The critic overestimates far beyond baseline levels. This threshold achieves 4/4 classification accuracy across available seeds: both trained dt\\_embedding conditions exceed 1.5$\\times$ at 35K+ steps (exp\\_008d seed 1: 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K; exp\\_009b seed 2: 1.62$\\times$@45K), while neither removed-embedding condition exceeds the threshold (exp\\_008f seed 1 peak: 1.02$\\times$@25K; exp\\_009c seed 2 peak: 1.26$\\times$@25K).\n\n- **$0.8 \\leq \\hat{r}_k \\leq 1.2$**: **Normal range.** Value estimates track the baseline's overshoot pattern.\n\n- **$\\hat{r}_k < 0.7$**: **Value suppression.** The critic underestimates returns relative to baseline, indicating conservative value learning.\n\n**Temporal validity constraint.** The NVE threshold applies only at $k \\geq$ 35K steps, where the baseline $r_k > 0.24$ and ratios are stable. At earlier steps, the small baseline denominator amplifies noise: for example, exp\\_009b at 25K shows NVE = 2.05$\\times$ and exp\\_008e\\_v3 at 25K shows NVE = 1.93$\\times$, both artifacts of the baseline's $r_{25\\text{K}} = 0.087$ rather than genuine pathological overestimation. We report these early-step values for completeness but exclude them from diagnostic classification.\n\n**Aggregate diagnostic power.** Evaluating the 1.5$\\times$ threshold across all eight experimental conditions (task B2), the NVE diagnostic achieves AUROC = 0.933 with 7/8 classification accuracy (Table~\\ref{tab:nve_sensitivity}). The single false positive is exp\\_008e\\_v3\\_s2, which exhibits late-onset NVE = 3.78$\\times$ driven by eval collapse rather than value overestimation---a non-CIVO failure pathway analyzed in \\S3.3. At a stricter threshold of 1.7$\\times$ (task B1), the metric achieves 8/8 accuracy and AUROC = 1.0 (supplementary material).\n\n### Properties of the NVE Metric\n\nTwo properties make NVE informative for detecting the CIVO:\n\n**Acceleration signature.** In pathological conditions, NVE does not merely exceed 1.5$\\times$---it *accelerates*, reflecting a positive feedback loop between overestimated values and actor exploitation. Exp\\_008d shows NVE = 1.71$\\times$@35K $\\to$ 2.09$\\times$@45K $\\to$ 4.12$\\times$@55K, with each checkpoint further from baseline. Healthy conditions (exp\\_008a, exp\\_008f) show stable or declining NVE trajectories.\n\n**Collapse association.** Sustained NVE $>$ 1.5$\\times$ across multiple consecutive checkpoints at 35K+ steps is associated with catastrophic performance collapse (exp\\_008d seed 1: three consecutive checkpoints above 1.5$\\times$, followed by eval return declining from 167 to 83). Transient exceedance followed by self-correction (exp\\_009b seed 2: 1.62$\\times$@45K $\\to$ 1.41$\\times$@55K $\\to$ 0.94$\\times$@65K, declining) does not lead to collapse. This pattern is consistent with a \"point of no return\" where the overestimation feedback loop becomes self-reinforcing, though with only two seeds under the trained-embedding condition, we report this association descriptively rather than as a statistical claim.\n\n\n## 3.3 Causal Analysis Protocol\n\n### Design Rationale\n\nThis is a diagnostic analysis. Our goal is to identify *which components* of variable-rate imagination cause degradation and trigger pathological overestimation, not to propose a new algorithm. We achieve this through controlled comparisons that vary one factor at a time, holding all others constant.\n\n### Factorial Structure\n\nWe vary three factors (temporal embedding type $\\times$ subsampling $\\times$ horizon) across eight treatment conditions plus a baseline (see Table 1 in \\S4 for the complete configuration matrix). Rather than filling all cells of the $3 \\times 2 \\times 2$ grid, we prioritize the comparisons most informative for causal isolation.\n\n### Causal Chain and Its Tests\n\nThe causal chain under investigation is:\n\n$$\\text{trained } e_{\\Delta t} \\;\\xrightarrow{\\text{Link 1}}\\; \\text{pathological NVE} \\;\\xrightarrow{\\text{Link 2}}\\; \\text{actor exploitation} \\;\\xrightarrow{\\text{Link 3}}\\; \\text{performance collapse}$$\n\nEach link is tested by a specific controlled comparison:\n\n**Link 1: Trained dt\\_embedding $\\to$ pathological overestimation.** The comparison between exp\\_008d (trained dt\\_embedding, $d{=}32$) and exp\\_008f (removed dt\\_embedding, $d{=}0$) isolates the effect of temporal embedding conditioning with all other factors held constant (subsample ON, $H{=}8$, $\\Delta t{=}2$ imagination). Exp\\_008d exhibits accelerating NVE (1.71$\\times$@35K $\\to$ 2.09$\\times$@45K), while exp\\_008f remains in the normal range (0.73$\\times$@35K $\\to$ 0.83$\\times$@45K). This is the primary causal evidence.\n\n**Link 2: Sustained overestimation $\\to$ collapse (stochastic).** Multi-seed replication of exp\\_008d reveals that the NVE $>$ 1.5$\\times$ marker is reliable across seeds (2/2 trained-embedding seeds exceed the threshold at 35K+), but collapse is stochastic: seed 1 (exp\\_008d) shows sustained NVE $>$ 1.5$\\times$ across three checkpoints and collapses; seed 2 (exp\\_009b) shows transient exceedance and self-corrects, with eval return rising from 141@25K to peak 278.5@95K. We report this stochasticity transparently---the diagnostic marker is reliable; collapse is a probabilistic downstream outcome.\n\n**Link 3: Imagination $\\Delta t$ as the critical variable.** Exp\\_008e\\_v3 uses a trained dt\\_embedding (identical to exp\\_008d and exp\\_006) but restricts imagination rollouts to $\\Delta t{=}1$, with subsample ON and $H{=}15$. This condition achieves eval return 869.9 at 105K steps (95% of baseline 915.67; exp\\_008e\\_v3, seed 1) with NVE = 0.80$\\times$ (healthy). The contrast with exp\\_006 (same trained dt\\_embedding, subsample ON, $H{=}15$, but $\\Delta t{=}2$ imagination $\\to$ collapse at 55K) isolates the imagination step size as the critical variable. The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\\Delta t > 1$ predictions during imagination.\n\n### 2$\\times$2 Ablation Matrix\n\nTo close the causal loop, we cross dt\\_embedding configuration (trained / frozen / removed) with temporal subsampling (ON / OFF), isolating the necessary condition for sustained CIVO:\n\n| dt\\_embedding | Subsample | Exp | Peak NVE (35K+) | Outcome |\n|:---:|:---:|:---:|:---:|:---:|\n| Trained ($d{=}32$) | ON | 008d | 4.12$\\times$@55K (sustained $\\uparrow$) | CIVO $\\to$ collapse |\n| Trained ($d{=}32$) | OFF | 008a | 0.93$\\times$@55K | Stable, 85\\% baseline@105K |\n| Frozen ($d{=}32$) | ON | 015b | 1.45$\\times$@55K $\\to$ 0.65$\\times$@65K | Sub-threshold transient; gradient starvation collapse |\n| Removed ($d{=}0$) | ON | 008f | $\\leq$1.02$\\times$ | No CIVO |\n\nTrained dt\\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\\times$ across consecutive checkpoints). Frozen embedding produces sub-threshold transient overestimation (exp\\_015b: peak 1.45$\\times$@55K) that self-corrects to 0.65$\\times$@65K before collapsing through a distinct gradient starvation mechanism (actor loss $\\to$ 0 as the frozen embedding drifts from the RSSM's evolving representations). Removing the embedding entirely (exp\\_008f, $d{=}0$) blocks CIVO: NVE never exceeds 1.02$\\times$. The subsample-OFF condition (exp\\_008a) confirms that a trained embedding without exposure to $\\Delta t{>}1$ training data also avoids CIVO, establishing that both embedding capacity *and* multi-rate training data are jointly required to trigger the overestimation feedback loop.\n\n### Supporting Analyses\n\n**Horizon effect (C5).** Exp\\_008c ($H{=}8$) vs. exp\\_008a ($H{=}15$), both with untrained dt\\_embedding and subsample OFF, shows that longer imagination horizons improve learning quality independently of the CIVO mechanism (exp\\_008a: 778@105K; exp\\_008c: 241@65K plateau).\n\n**Temporal distance amplification (C4).** Exp\\_006 ($\\Delta t{=}2$, peak 485@35K $\\to$ collapse) vs. exp\\_007 ($\\Delta t{=}4$, peak 177@25K, severe degradation) shows monotonic performance decline with increasing $\\Delta t$, consistent with compounding RSSM prediction errors. Only two $\\Delta t$ values are tested; we report the monotonic trend (dt=1 $\\approx$950 $>$ dt=2 peak 485 $>$ dt=4 peak 177) without stronger generalization claims.\n\n### RSSM Fidelity Analysis\n\nTo ground the CIVO mechanism in world-model prediction quality, we analyze RSSM fidelity by measuring observation prediction error (MSE) and reward prediction error (MAE) at $\\Delta t{=}1$ vs. $\\Delta t{=}2$ across three conditions (exp\\_rssm\\_fidelity\\_analysis):\n\n| Condition | $\\Delta t{=}1$ obs MSE | $\\Delta t{=}2$ obs MSE | Obs gap | $\\Delta t{=}1$ rew MAE | $\\Delta t{=}2$ rew MAE | Rew gap |\n|-----------|:---:|:---:|:---:|:---:|:---:|:---:|\n| Baseline (exp\\_001) | 13.49 | 27.50 | 2.04$\\times$ | 0.0102 | 0.0159 | 1.56$\\times$ |\n| 008d (trained emb) | 41.31 | 53.67 | 1.30$\\times$ | 0.0568 | 0.1579 | 2.78$\\times$ |\n| 008f (no emb) | 8.01 | 22.04 | 2.75$\\times$ | 0.7469 | 0.7526 | 1.01$\\times$ |\n\nTwo patterns are diagnostically relevant:\n\n1. **Trained embedding enables differentiated but biased reward predictions.** In exp\\_008d, the reward head produces sharply different predictions for $\\Delta t{=}1$ vs. $\\Delta t{=}2$ (reward gap 2.78$\\times$), but these differentiated predictions rest on poor absolute state quality ($\\Delta t{=}1$ obs MSE = 41.31, 3.1$\\times$ baseline). The critic receives confident but systematically biased reward signals at $\\Delta t{=}2$, fueling value overestimation.\n\n2. **Removing the embedding prevents differentiation but degrades reward quality.** In exp\\_008f, the reward head cannot distinguish $\\Delta t$ values (gap 1.01$\\times$), blocking the systematic bias that drives the CIVO. However, this comes at the cost of severely degraded reward prediction (MAE = 0.747, 73$\\times$ baseline). Exp\\_008f is therefore a *causal control* that confirms the dt\\_embedding's role in overestimation, not a recommended configuration.\n\n**Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.\n\n### Gradient Decomposition of the Temporal Embedding\n\nTo identify which loss component drives $e_{\\Delta t}$'s learned representation, we decompose $\\nabla_\\theta e_{\\Delta t}$ by loss term using \\texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061).\n\n| Loss component | Gradient norm | Share (\\%) |\n|----------------|:---:|:---:|\n| Observation decoders (orientations, velocity, height) | 1.505 | 93 |\n| KL dynamics | 0.119 | 7 |\n| Continuation head | $<$0.001 | $<$1 |\n| Reward head | 0.000 | 0 |\n\nThe temporal embedding receives 93\\% of its gradient from observation reconstruction and numerically negligible---zero to within floating-point precision---from the reward head (D061). Three implications follow:\n\n1. **Exp\\_016e is an architectural no-op.** The reward-only stop-gradient surgery (Section~\\ref{sec:sgs_negative}) detaches a gradient that does not exist. Its null effect is structurally determined, not an empirical surprise.\n\n2. **$e_{\\Delta t}$ is shaped by observation reconstruction, not reward prediction.** The embedding learns temporal information that helps observation decoders minimize reconstruction error. If this induces systematic biases in latent states at $\\Delta t{>}1$---states that are easy to decode but dynamically inaccurate---these biases propagate to all downstream heads, including the critic's value estimates. CIVO thus originates in the observation reconstruction objective, not the reward pathway.\n\n3. **Full SGS is the correct gradient-level intervention.** A meaningful intervention must address the dominant 93\\% contribution from observation decoders. This motivates the full SGS design (exp\\_018), which detaches $e_{\\Delta t}$ from all non-KL gradient pathways.\n\n### Stop-Gradient Surgery: An Informative Negative (exp\\_016e)\n\\label{sec:sgs_negative}\n\nThe gradient decomposition above was motivated by a null result: exp\\_016e, a reward-only stop-gradient surgery (SGS) that failed to attenuate CIVO. This negative result is informative because it constrains the space of viable interventions and reveals the architectural structure of gradient flow through $e_{\\Delta t}$.\n\n**Configuration.** Exp\\_016e replicates exp\\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\\Delta t}$, subsampling ON, $H{=}8$, $\\Delta t{=}2$ imagination) with one modification: \\texttt{reward\\_dt\\_emb\\_detach=True}, which applies $\\text{sg}(\\cdot)$ to $e_{\\Delta t}$ before the reward head during the backward pass.\n\n**Results.** Exp\\_016e collapses in the same qualitative pattern as exp\\_008d. Peak eval return reaches 326.7 at 75K (exp\\_016e), then drops to 31.7 by 95K---a 90.3\\% decline. NVE remains in the normal range through 85K, then spikes to 10.42$\\times$ at 95K (exp\\_016e). The timing difference relative to exp\\_008d (which crosses the pathological NVE threshold at 35K) cannot be attributed to the intervention, since the intervention is an architectural no-op (Section~\\ref{sec:gradient_decomposition}); seed-level stochasticity is the parsimonious explanation.\n\n**Why this is an architectural no-op.** The gradient decomposition (Table above) shows the reward head contributes zero gradient to $e_{\\Delta t}$. Detaching a zero-gradient pathway changes nothing. The reward head's negligible contribution arises from DreamerV3's architecture: the observation decoders' high-dimensional output space (24 dimensions vs.\\ 1 scalar reward) dominates the gradient signal to $e_{\\Delta t}$ by two orders of magnitude.\n\n**Implication for intervention design.** Any strategy targeting the reward head alone---reward prediction regularization, reward-conditioned value clipping, or reward-pathway stop-gradient---addresses $<$1\\% of the gradient flow to $e_{\\Delta t}$ and is unlikely to mitigate CIVO. Effective interventions must operate on the observation reconstruction pathway, either by modifying gradient flow (full SGS, exp\\_018) or by restructuring how $e_{\\Delta t}$ interacts with the RSSM transition function.\n\n### Imagination Step Size as Causal Variable\n\nThe factorial analysis isolates the imagination step size as the causal variable that triggers CIVO. Two lines of evidence support this:\n\n**$\\Delta t{=}1$ imagination removes CIVO (seed 1).** Exp\\_008e\\_v3 uses the same trained dt\\_embedding and multi-rate training data as exp\\_008d (the primary CIVO-exhibiting condition), but restricts imagination rollouts to $\\Delta t{=}1$ with $H{=}15$. At 105K steps, it achieves eval return 869.9 (exp\\_008e\\_v3, seed 1), 95\\% of baseline (exp\\_001\\_baseline: 915.67@105K), with NVE = 0.80$\\times$ (healthy range). The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\\Delta t > 1$ predictions during imagination.\n\n**$\\Delta t{=}1$ imagination does not prevent all failure modes (seed 2).** Exp\\_008e\\_v3\\_s2 replicates the same configuration with seed 2 and exhibits catastrophic collapse: eval return peaks at 715 early in training, then declines to 137 by 105K steps (exp\\_008e\\_v3\\_s2), with NVE = 3.78$\\times$ at the final checkpoint. This collapse co-occurs with rising entropy (exp\\_008e\\_v3\\_s2), contrasting with the entropy-decreasing, value-driven collapse signature of CIVO in exp\\_008d.\n\n**Dual-pathway analysis.** The seed-1 vs. seed-2 divergence reveals two distinct failure pathways:\n\n- *Pathway A (CIVO):* Trained dt\\_embedding + $\\Delta t{>}1$ imagination $\\to$ value overestimation (NVE $\\uparrow$) $\\to$ actor over-exploitation (entropy $\\downarrow$) $\\to$ performance collapse. Observed in exp\\_008d (seed 1) and exp\\_009b (seed 2, transient).\n\n- *Pathway B (non-CIVO):* $\\Delta t{=}1$ imagination, no value overestimation trigger, but eval-driven collapse with entropy increase. Observed in exp\\_008e\\_v3\\_s2 (seed 2). The rising entropy signature suggests exploration failure or policy instability unrelated to the CIVO mechanism.\n\nTo rule out seed fragility as the explanation for Pathway B, we verify that the baseline is stable at seed 2: exp\\_009a (DreamerV3 baseline, seed 2) achieves eval return 911.2 at 105K steps (exp\\_009a), comparable to seed 1's 915.67 (exp\\_001\\_baseline). The collapse in exp\\_008e\\_v3\\_s2 is therefore attributable to the interaction between multi-rate training and seed-specific dynamics, not to inherent instability at seed 2.\n\n**Implication.** Restricting imagination to $\\Delta t{=}1$ eliminates Pathway A (CIVO) but does not guarantee stable training. The $\\Delta t{=}1$ configuration is a *diagnostic control* confirming the causal role of imagination step size, not a robust mitigation strategy.\n",
    "structuredPatch": [
      {
        "oldStart": 148,
        "oldLines": 6,
        "newStart": 148,
        "newLines": 7,
        "lines": [
          " **Caveat on obs gap ratios.** Exp\\_008d's low obs gap ratio (1.30$\\times$) is misleading---its $\\Delta t{=}1$ absolute error is already 3.1$\\times$ baseline, indicating the model has degraded overall. We report both absolute errors and ratios to avoid ratio-only comparisons that could obscure this.",
          " ",
          " ### Gradient Decomposition of the Temporal Embedding",
          "+\\label{sec:gradient_decomposition}",
          " ",
          " To identify which loss component drives $e_{\\Delta t}$'s learned representation, we decompose $\\nabla_\\theta e_{\\Delta t}$ by loss term using \\texttt{torch.autograd.grad}, measuring each component's gradient norm at step 95K (D061).",
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

### Assistant

_source line 34_

All 6 Framing B diffs (M2–M7) were already applied. I made two housekeeping fixes:
1. Updated the status comment to list all 6 diffs explicitly
2. Added the missing `\label{sec:gradient_decomposition}` that line 176's `\ref` depends on

Verified hard constraints: zero occurrences of "delusional critic", "SGS delays collapse", or "practical mitigation". All numbers match the provided data sources. 008f is positioned as causal control, not recommendation. The file is consistent with Framing B.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "uuid": "7350b685-d09b-4f8d-9541-407ed387996b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qd6C8mQ7aSfT1WdE8x8xhu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 67339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 613
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

_source line 35_

All 6 Framing B diffs (M2–M7) were already applied. I made two housekeeping fixes:
1. Updated the status comment to list all 6 diffs explicitly
2. Added the missing `\label{sec:gradient_decomposition}` that line 176's `\ref` depends on

Verified hard constraints: zero occurrences of "delusional critic", "SGS delays collapse", or "practical mitigation". All numbers match the provided data sources. 008f is positioned as causal control, not recommendation. The file is consistent with Framing B.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 144813,
  "duration_api_ms": 148220,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "3ea334ef-5a13-4f38-bdf5-c243e9b238f7",
  "total_cost_usd": 0.68948975,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 56111,
    "cache_read_input_tokens": 307770,
    "output_tokens": 7302,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 56111,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 137,
        "cache_read_input_tokens": 67339,
        "cache_creation_input_tokens": 613,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 613
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2176,
      "outputTokens": 26,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002306,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 7302,
      "cacheReadInputTokens": 307770,
      "cacheCreationInputTokens": 56111,
      "webSearchRequests": 0,
      "costUSD": 0.68718375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "49990fba-dca4-4b18-98f7-baeb33d4478e"
}
```

</details>

---
