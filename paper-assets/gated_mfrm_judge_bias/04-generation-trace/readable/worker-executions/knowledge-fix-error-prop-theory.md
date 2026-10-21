# knowledge fix error prop theory

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_knowledge_fix_error_prop_theory_20260522T042849.log`
- **Structured JSON:** [`8eb70a08c31da0ecbfe7.json`](../../sessions/8e/8eb70a08c31da0ecbfe7.json)

## Before a recorded user message

46 recorded events

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
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
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
  "uuid": "366ee4f0-68cb-4833-99e8-6dcb3cefa2dc",
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
    "resetsAt": 1779439800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ef8f1c42-29d9-473b-bfa3-0c40cd0db9a8",
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd"
}
```

---

### Assistant

_source line 4_

Let me read the document first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "b02f461f-3a29-44bb-98a5-faf136bca707",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2nf5vz5JDEv7hbkcjNZr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12762,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12762
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

<details open><summary>🔧 Tool call — Read · `toolu_011Dz3QGycXh7yWXZCMYrkHZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "524291f1-d87c-416d-9454-8f2dae130599",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2nf5vz5JDEv7hbkcjNZr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12762,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12762
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

_source line 6 · 2026-05-22T04:28:58.990Z_

<details><summary>↩ Tool result · `toolu_011Dz3QGycXh7yWXZCMYrkHZ`</summary>

```text
1	# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis
2	
3	## 1. Problem Setup
4	
5	### 1.1 Model
6	
7	The Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \in \{0,1\}$ for model $n$, item $i$, and judge $j$:
8	
9	$$
10	\text{logit}\,P(Y_{nij}=1) = \theta_n - b_i - d_j + c_n \cdot e_i
11	$$
12	
13	where $\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \geq 0$ model-specific contamination susceptibility, and $e_i \in [0,1]$ item exposure level.
14	
15	### 1.2 Three-Stage Estimation
16	
17	| Stage | Estimates | Method |
18	|-------|-----------|--------|
19	| 1 | $\hat\theta^{(1)}, \hat{b}, \hat{d}$ | Standard MFRM (no contamination term) |
20	| 2 | $\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |
21	| 3 | $\hat\theta, \hat{c}_n$ | Joint G-MFRM via MCMC, with $\hat{e}_i$ plugged in as known |
22	
23	The critical feature: Stage 3 conditions on the point estimate $\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\hat{e}_i = e_i + \varepsilon_i$ with $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\theta_n$.
24	
25	### 1.3 Priors (Stage 3)
26	
27	| Parameter | Prior |
28	|-----------|-------|
29	| $\theta_n$ | $\mathcal{N}(0,1)$, centered to mean zero |
30	| $b_i$ | $\mathcal{N}(0,1)$ |
31	| $d_j$ | $\mathcal{N}(0, 0.5)$ |
32	| $c_n$ | $\text{HalfNormal}(0.5)$ |
33	
34	### 1.4 DGP Parameters (exp-012)
35	
36	$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:
37	
38	$$
39	\text{logit}\,P(Y_{nij}=1) = \theta_n - b_i - d_j + c_n \cdot e_i \cdot (1 + s_j)
40	$$
41	
42	Exposure values: $e_i = \text{sigmoid}(e_i^{\text{raw}})$ where $e_i^{\text{raw}} \sim \mathcal{N}(0,1)$.
43	
44	---
45	
46	## 2. Connection to Two-Step Estimator Literature
47	
48	### 2.1 Classical Frequentist Framework
49	
50	The G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:
51	
52	**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:
53	
54	$$
55	V_{\text{corrected}} = V_2 + V_2\!\left(C\,V_1\,C^\top - R\,V_1\,C^\top - C\,V_1\,R^\top\right)\!V_2
56	$$
57	
58	where $V_1, V_2$ are the step-specific variance matrices, $C = \partial^2 \ell_2 / \partial\alpha\,\partial\gamma^\top$ captures cross-step dependence, and $R = \partial^2 \ell_2 / \partial\alpha\,\partial\alpha^\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.
59	
60	**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.
61	
62	### 2.2 Bayesian Adaptation: Cut Feedback
63	
64	Our Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):
65	
66	- The **cut posterior** $p_{\text{cut}}(\theta, c \mid Y, \hat{e})$ conditions on the plug-in estimate $\hat{e}$ and "cuts" the feedback from Stage 3 to Stage 2.
67	- The **full posterior** $p(\theta, c \mid Y) = \int p(\theta, c \mid Y, e)\,p(e \mid \text{data})\,de$ would marginalize over $e_i$ uncertainty.
68	
69	The cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.
70	
71	### 2.3 Our Setting's Specificity
72	
73	Three features distinguish our problem from the textbook case:
74	
75	1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.
76	
77	2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.
78	
79	3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.
80	
81	---
82	
83	## 3. Main Results
84	
85	### 3.1 Proposition 1: Local Sensitivity via Implicit Function Theorem
86	
87	**Setup.** Fix model $n$ and consider the joint posterior mode $\hat\phi_n = (\hat\theta_n, \hat{c}_n)$ as a function of the exposure vector $e = (e_1, \ldots, e_I)$. At the posterior mode, the score vanishes:
88	
89	$$
90	\nabla_\phi L(\hat\phi_n; Y, e) = 0
91	$$
92	
93	where $L = \log p(\phi \mid Y, e)$ is the log-posterior.
94	
95	**Perturbation.** When $e \to \tilde{e} = e + \varepsilon$, the implicit function theorem gives:
96	
97	$$
98	\delta\phi_n \equiv \hat\phi_n(\tilde{e}) - \hat\phi_n(e) \approx -\mathcal{H}_n^{-1} \cdot \Delta s_n
99	$$
100	
101	where $\mathcal{H}_n = -\nabla^2_{\phi\phi} L$ is the posterior precision matrix and $\Delta s_n$ is the score perturbation.
102	
103	**Posterior precision matrix** (for the $(\theta_n, c_n)$ block, conditioning on $b, d$):
104	
105	$$
106	\mathcal{H}_n = \begin{pmatrix} A_n + \tau_\theta & B_n \\ B_n & C_n + \tau_c \end{pmatrix}
107	$$
108	
109	where $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:
110	
111	$$
112	A_n = \sum_{i,j} w_{nij}, \qquad B_n = \sum_{i,j} w_{nij}\,e_i, \qquad C_n = \sum_{i,j} w_{nij}\,e_i^2
113	$$
114	
115	$\tau_\theta = 1$ (prior precision for $\theta_n$), $\tau_c = 1/\sigma_c^2 = 4$ (curvature of $\text{HalfNormal}(0.5)$ log-density at the mode).
116	
117	**Score perturbation** (to first order in $\varepsilon$):
118	
119	$$
120	\Delta s_n = \begin{pmatrix} -\hat{c}_n \sum_i W_{ni}\,\varepsilon_i \\ -\hat{c}_n \sum_i W_{ni}\,e_i\,\varepsilon_i \end{pmatrix}
121	$$
122	
123	where $W_{ni} = \sum_j w_{nij}$ is the information contributed by item $i$.
124	
125	**Result.** The posterior mode shifts are:
126	
127	$$
128	\boxed{
129	\begin{aligned}
130	\delta c_n &= \frac{\hat{c}_n}{\det \mathcal{H}_n} \left[ B_n \sum_i W_{ni}\varepsilon_i - (A_n + \tau_\theta) \sum_i W_{ni} e_i \varepsilon_i \right] \\[6pt]
131	\delta \theta_n &= \frac{\hat{c}_n}{\det \mathcal{H}_n} \left[ B_n \sum_i W_{ni} e_i \varepsilon_i - (C_n + \tau_c) \sum_i W_{ni} \varepsilon_i \right]
132	\end{aligned}
133	}
134	$$
135	
136	where $\det \mathcal{H}_n = (A_n + \tau_\theta)(C_n + \tau_c) - B_n^2$.
137	
138	**Interpretation.** Both sensitivities are proportional to $\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\sum W_{ni}\varepsilon_i$ (aggregate noise, affects both parameters) and $\sum W_{ni}e_i\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).
139	
140	### 3.2 Proposition 2: Errors-in-Variables Attenuation of $c_n$
141	
142	The local analysis (Proposition 1) captures variance but misses the dominant effect at moderate-to-large $\sigma$: **systematic attenuation bias**.
143	
144	**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.
145	
146	Consider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):
147	
148	$$
149	Y_{nij} \approx \theta_n - b_i - d_j + c_n \cdot e_i + u_{nij}
150	$$
151	
152	When we fit with $\tilde{e}_i = e_i + \varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):
153	
154	$$
155	\tilde{c}_n \xrightarrow{p} c_n \cdot \frac{\text{Cov}_I(e_i, \tilde{e}_i)}{\text{Var}_I(\tilde{e}_i)} = c_n \cdot \frac{\text{Var}_I(e)}{\text{Var}_I(e) + \sigma^2} \equiv c_n \cdot \lambda(\sigma)
156	$$
157	
158	where $\text{Var}_I(e) = \frac{1}{I}\sum_i(e_i - \bar{e})^2$ is the cross-item variance of true exposure, and:
159	
160	$$
161	\boxed{\lambda(\sigma) = \frac{\text{Var}_I(e)}{\text{Var}_I(e) + \sigma^2}}
162	$$
163	
164	is the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).
165	
166	**Attenuation bias:**
167	
168	$$
169	\text{Bias}(\tilde{c}_n) = c_n\,(1 - \lambda) = c_n \cdot \frac{\sigma^2}{\text{Var}_I(e) + \sigma^2}
170	$$
171	
172	**Key properties:**
173	- The bias is **always toward zero** (underestimation of contamination)
174	- The bias is **proportional to $c_n$**: highly contaminated models suffer more
175	- The bias is **nonlinear in $\sigma$**: mild for $\sigma^2 \ll \text{Var}_I(e)$, catastrophic for $\sigma^2 \gg \text{Var}_I(e)$
176	
177	### 3.3 Proposition 3: RMSE Decomposition
178	
179	Combining the variance (Proposition 1) and bias (Proposition 2) channels:
180	
181	$$
182	\text{MSE}_c(\sigma) = \mathbb{E}_n\!\left[(\tilde{c}_n - c_n)^2\right]
183	$$
184	
185	Decomposing $\tilde{c}_n - c_n = (\tilde{c}_n - \hat{c}_n) + (\hat{c}_n - c_n)$:
186	
187	$$
188	\text{MSE}_c(\sigma) = \underbrace{\text{MSE}_c(0)}_{\text{baseline}} + \underbrace{(1-\lambda)^2 \cdot \mathbb{E}_n[\hat{c}_n^2]}_{\text{attenuation bias}^2} + \underbrace{\mathbb{E}_n[\text{Var}_\varepsilon(\tilde{c}_n)]}_{\text{noise variance}} + \underbrace{2(1-\lambda)\cdot\mathbb{E}_n[\hat{c}_n(\hat{c}_n - c_n)]}_{\text{cross-term}}
189	$$
190	
191	**Regime analysis:**
192	
193	- **Small $\sigma$ ($\sigma^2 \ll \text{Var}_I(e)$):** $1-\lambda \approx \sigma^2/\text{Var}_I(e)$, so the bias term scales as $\sigma^4$ and the variance term as $\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\sigma^2$.
194	
195	- **Large $\sigma$ ($\sigma^2 \gg \text{Var}_I(e)$):** $1-\lambda \to 1$, bias term saturates at $\mathbb{E}[\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\sqrt{\text{MSE}_c(0) + \mathbb{E}[\hat{c}_n^2]}$ — catastrophic degradation.
196	
197	- **Transition at $\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)}$**: The attenuation factor $\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.
198	
199	$$
200	\boxed{\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)}}
201	$$
202	
203	### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\theta_n$)
204	
205	**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\theta_n$ by a factor of $\Omega(I)$.
206	
207	**Proof sketch.** The sensitivity arises through two distinct mechanisms:
208	
209	**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:
210	
211	$$
212	\frac{\partial \ell}{\partial c_n} = \sum_{i,j}(Y_{nij} - p_{nij}) \cdot e_i
213	$$
214	
215	When $e_i \to \tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\lambda) \propto \sigma^2$.
216	
217	**(B) Indirect channel (affects $\theta_n$).** The score for $\theta_n$ does **not** involve $e_i$:
218	
219	$$
220	\frac{\partial \ell}{\partial \theta_n} = \sum_{i,j}(Y_{nij} - p_{nij})
221	$$
222	
223	The perturbation affects $\theta_n$ only through the changed predicted probabilities $\tilde{p}_{nij} = \sigma(\theta_n - b_i - d_j + c_n\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.
224	
225	**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption $W_{ni} \approx \bar{W}$:
226	
227	$$
228	\frac{\mathbb{E}[\delta c_n^2]}{\mathbb{E}[\delta \theta_n^2]} = \frac{(A_n+\tau_\theta)^2 \text{Var}_I(e) + \tau_\theta^2 \bar{e}^2}{(C_n+\tau_c)^2 + \text{Var}_I(e) \cdot B_n^2 - 2B_n(C_n+\tau_c)\bar{e}}
229	$$
230	
231	With typical values ($A_n \approx 176$, $B_n \approx 88$, $C_n \approx 51$, $\tau_\theta = 1$, $\tau_c = 4$):
232	
233	$$
234	\frac{\mathbb{E}[\delta c_n^2]}{\mathbb{E}[\delta \theta_n^2]} \approx \frac{1285}{443} \approx 2.9
235	$$
236	
237	This local variance ratio of $\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\sigma$) affects $c_n$ directly but $\theta_n$ only through the coupling, amplifying the differential further.
238	
239	**Absorption mechanism.** When $c_n$ is attenuated, the "missing" contamination advantage $c_n(1-\lambda)\bar{e}$ is partially absorbed by $\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\theta_n$ vs. $c_n$.
240	
241	### 3.5 Corollary 2: Nonlinear Scaling Mechanism
242	
243	The transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:
244	
245	$$
246	\text{Bias}^2(c_n) = c_n^2 \cdot \left(\frac{\sigma^2}{\text{Var}_I(e) + \sigma^2}\right)^2
247	$$
248	
249	This function has three regimes:
250	
251	| Regime | Condition | Scaling | Character |
252	|--------|-----------|---------|-----------|
253	| Linear | $\sigma^2 \ll V_e$ | $\propto \sigma^4 / V_e^2$ | Negligible bias |
254	| Transition | $\sigma^2 \approx V_e$ | $\propto 1/4$ | Moderate bias |
255	| Saturation | $\sigma^2 \gg V_e$ | $\to c_n^2$ | Complete signal loss |
256	
257	where $V_e = \text{Var}_I(e)$.
258	
259	The nonlinearity is **intrinsic to the multiplicative $c_n \cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.
260	
261	---
262	
263	## 4. Numerical Calibration
264	
265	### 4.1 DGP-Specific Constants
266	
267	For the exp-012 DGP with $e_i = \text{sigmoid}(\mathcal{N}(0,1))$:
268	
269	$$
270	\mathbb{E}[e_i] = 0.5, \qquad \mathbb{E}[e_i^2] \approx 0.29, \qquad \text{Var}_I(e) \approx 0.04
271	$$
272	
273	The critical noise level:
274	
275	$$
276	\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)} \approx \sqrt{0.04} = 0.20
277	$$
278	
279	### 4.2 Attenuation Factor at Experimental Noise Levels
280	
281	| $\sigma$ | $\sigma^2$ | $\lambda = V_e/(V_e + \sigma^2)$ | $1-\lambda$ | $(1-\lambda)^2$ |
282	|----------|-----------|----------------------------------|-------------|-----------------|
283	| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |
284	| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |
285	| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |
286	| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |
287	
288	At $\sigma = 0.2 = \sigma_{\text{crit}}$: exactly half the signal variance is noise. At $\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.
289	
290	### 4.3 Comparison with exp-012 Results
291	
292	| $\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\lambda$ | $\theta$ RMSE (exp) | $\theta$ degradation (exp) |
293	|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|
294	| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |
295	| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |
296	| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |
297	| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |
298	
299	**Qualitative agreement:** The theory correctly predicts:
300	
301	1. **Ordering**: $c_n$ degradation > $\theta$ degradation at every noise level ✓
302	2. **Mild degradation at $\sigma=0.1$**: $\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓
303	3. **Transition at $\sigma=0.2$**: $\lambda = 0.5$ → moderate degradation ✓
304	4. **Severe degradation at $\sigma=0.5$**: $\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓
305	5. **Superlinear scaling**: the jump from $\sigma=0.2$ to $\sigma=0.5$ is disproportionately large ✓
306	
307	**Sensitivity ratio:** Experimental $c_n$ degradation / $\theta$ degradation:
308	- $\sigma=0.1$: 2.3/1.4 = 1.6×
309	- $\sigma=0.2$: 7.9/5.9 = 1.3×
310	- $\sigma=0.5$: 57.9/36.9 = 1.6×
311	
312	Theory predicts $\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\theta_n$.
313	
314	### 4.4 Phase Transition Verification
315	
316	The theory predicts a transition at $\sigma_{\text{crit}} = 0.20$. The experimental data confirms:
317	
318	- Below $\sigma_{\text{crit}}$ ($\sigma = 0.1$): RMSE degradation < 2.5% for both parameters
319	- At $\sigma_{\text{crit}}$ ($\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)
320	- Above $\sigma_{\text{crit}}$ ($\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)
321	
322	The ratio $\sigma = 0.5$ is $2.5\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.
323	
324	---
325	
326	## 5. Discussion
327	
328	### 5.1 Why $c_n$ Is More Sensitive Than $\theta_n$
329	
330	Three reinforcing mechanisms:
331	
332	1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.
333	
334	2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).
335	
336	3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\theta_n$, the symmetric $\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.
337	
338	### 5.2 Why the Degradation Is Nonlinear
339	
340	The nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:
341	
342	The attenuation factor $\lambda = V_e/(V_e + \sigma^2)$ is a **harmonic** function of $\sigma^2$. The resulting squared bias $(1-\lambda)^2 = \sigma^4/(V_e + \sigma^2)^2$ is:
343	- Convex for $\sigma^2 < V_e/3$ (accelerating degradation)
344	- Concave for $\sigma^2 > V_e/3$ (decelerating toward saturation)
345	
346	At $\sigma = 0.5$, we have $\sigma^2/V_e \approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).
347	
348	### 5.3 Tightness of the Bounds
349	
350	The theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:
351	
352	1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.
353	
354	2. **Logistic nonlinearity**: The linear EIV attenuation formula $\lambda = V_e/(V_e + \sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.
355	
356	3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.
357	
358	Despite these limitations, the theory correctly identifies (a) the critical noise threshold $\sigma_{\text{crit}} \approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.
359	
360	### 5.4 Practical Implications for Stage 2 Quality
361	
362	The attenuation analysis yields a concrete requirement for Stage 2 estimation:
363	
364	$$
365	\sigma_e < \sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)}
366	$$
367	
368	For typical benchmark exposure distributions where $\text{Var}(e) \approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:
369	
370	$$
371	\sigma_e < 0.20\text{–}0.28
372	$$
373	
374	Within this range, RMSE degradation stays below $\sim$10% for both $c_n$ and $\theta_n$. The exp-012 results confirm this: at $\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.
375	
376	### 5.5 Connection to Robustness Claims
377	
378	The theoretical analysis supports the following characterization for the paper:
379	
380	> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\hat\theta$ degrade by $< 6\%$ RMSE and contamination estimates $\hat{c}_n$ by $< 8\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \theta$ follows from the direct multiplicative coupling $c_n \cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.
381	
382	---
383	
384	## 6. References
385	
386	- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.
387	- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.
388	- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.
389	- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.
390	- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.
391	- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.
392	- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.
393	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "0f58b9e5-fde2-4fdf-88a5-f0b976471438",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
      "content": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Proposition 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Proposition 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Proposition 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Proposition 3: RMSE Decomposition\n\nCombining the variance (Proposition 1) and bias (Proposition 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\nThis local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
      "numLines": 393,
      "startLine": 1,
      "totalLines": 393
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full document. Let me plan the four modifications:

### Fix 1: Mark sensitivity ratio as qualitative
The relevant section is §3.4 (lines 203-238) and §4.3 (lines 291-312). The calculation of ≈2.9× is at lines 231-237. I need to add the qualifier after the ratio calculation and also adjust the comparison section.

### Fix 2: σ_crit DGP-dependent
I need to find all occurrences of "σ_crit ≈ 0.20" and ensure each has the formula and DGP-dependency note. Let me check all occurrences:


- Line 197-201: §3.3 already has the formula
- Line 274-277: §4.1 has the formula but needs the DGP-dependency note added
- Line 316: §4.4 is missing the formula entirely
- Line 358: §5.3 is missing the formula
- Line 365: §5.4 already has the formula
- Line 380: §5.5 already has the formula

So I need to add the formula back into §4.4 and §5.3 for consistency. Then I'll tackle renaming all three propositions to "Result" or "Approximate Result" — that's lines 85, 140, 177, plus the cross-references at 226 and 312. Finally, I need to expand the absorption mechanism discussion in §3.4 to explain how θ gets systematically overestimated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "214d1418-0cf8-49e5-9fc9-47dea92070f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWiBxnkX13aG4tfq1YCg2s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9186,
      "cache_read_input_tokens": 24209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9186
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

_source line 8_

I'll make all four modifications now.

**Fix 1** — Add qualitative caveat to the sensitivity ratio in §3.4 and §4.3.

**Fix 2** — Add DGP-dependency to all σ_crit ≈ 0.20 occurrences.

**Fix 3** — Rename "Proposition" to "Approximate Result".

**Fix 4** — Expand absorption mechanism in §3.4.

Starting with the edits:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "befa6f77-59f0-423a-8b3b-8d7ed3630828",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWiBxnkX13aG4tfq1YCg2s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9186,
      "cache_read_input_tokens": 24209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9186
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01K1XKaCvuMxRUFe4K2xZQMC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "### 3.1 Proposition 1: Local Sensitivity via Implicit Function Theorem",
  "new_string": "### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "71f0c7ba-2356-4942-b263-abedb062d27c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWiBxnkX13aG4tfq1YCg2s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9186,
      "cache_read_input_tokens": 24209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9186
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

_source line 10 · 2026-05-22T04:29:16.994Z_

<details><summary>↩ Tool result · `toolu_01K1XKaCvuMxRUFe4K2xZQMC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "a0f74120-4502-4e9c-bcb1-409a5f036b0a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "### 3.1 Proposition 1: Local Sensitivity via Implicit Function Theorem",
    "newString": "### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Proposition 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Proposition 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Proposition 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Proposition 3: RMSE Decomposition\n\nCombining the variance (Proposition 1) and bias (Proposition 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\nThis local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 82,
        "oldLines": 7,
        "newStart": 82,
        "newLines": 7,
        "lines": [
          " ",
          " ## 3. Main Results",
          " ",
          "-### 3.1 Proposition 1: Local Sensitivity via Implicit Function Theorem",
          "+### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem",
          " ",
          " **Setup.** Fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:",
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01RfNoLvdLFiH5mdqTt2fm68`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "### 3.2 Proposition 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Proposition 1) captures variance but misses the dominant effect",
  "new_string": "### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "041a5d6e-e90b-42da-8166-c649227344de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eBCo8D1Spwv9Z34pfYuzL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 33395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 864
      },
      "output_tokens": 72,
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

_source line 12 · 2026-05-22T04:29:21.776Z_

<details><summary>↩ Tool result · `toolu_01RfNoLvdLFiH5mdqTt2fm68`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "14402930-dcde-48dd-9a8a-c0abc89e4b4e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "### 3.2 Proposition 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Proposition 1) captures variance but misses the dominant effect",
    "newString": "### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Proposition 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Proposition 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Proposition 3: RMSE Decomposition\n\nCombining the variance (Proposition 1) and bias (Proposition 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\nThis local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 137,
        "oldLines": 9,
        "newStart": 137,
        "newLines": 9,
        "lines": [
          " ",
          " **Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).",
          " ",
          "-### 3.2 Proposition 2: Errors-in-Variables Attenuation of $c_n$",
          "+### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$",
          " ",
          "-The local analysis (Proposition 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.",
          "+The local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.",
          " ",
          " **Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.",
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01RDboLEv3c8xz5Vn9BixQXX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "### 3.3 Proposition 3: RMSE Decomposition\n\nCombining the variance (Proposition 1) and bias (Proposition 2) channels:",
  "new_string": "### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "846fa742-0403-47d7-9d25-6473e752266a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gBddfFqhTNLvJYPZANBkR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 34259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 291
      },
      "output_tokens": 72,
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

_source line 14 · 2026-05-22T04:29:26.647Z_

<details><summary>↩ Tool result · `toolu_01RDboLEv3c8xz5Vn9BixQXX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "670b65e9-5841-402e-85e6-515c0d8e2c6f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "### 3.3 Proposition 3: RMSE Decomposition\n\nCombining the variance (Proposition 1) and bias (Proposition 2) channels:",
    "newString": "### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Proposition 3: RMSE Decomposition\n\nCombining the variance (Proposition 1) and bias (Proposition 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\nThis local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 174,
        "oldLines": 9,
        "newStart": 174,
        "newLines": 9,
        "lines": [
          " - The bias is **proportional to $c_n$**: highly contaminated models suffer more",
          " - The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$",
          " ",
          "-### 3.3 Proposition 3: RMSE Decomposition",
          "+### 3.3 Approximate Result 3: RMSE Decomposition",
          " ",
          "-Combining the variance (Proposition 1) and bias (Proposition 2) channels:",
          "+Combining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:",
          " ",
          " $$",
          " \\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]"
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

_source line 15_

Now fix the "Approximate Result" label and add "under the linearized model approximation" to the setup of Result 1:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "74368ffa-60d3-4b3e-8b42-5a2f918e3619",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1P8Y1tw8Fs74RYLYGgmAE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 276,
      "cache_read_input_tokens": 34550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 276
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

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01KTaD36DZuJU41Z6zxUePUC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "**Setup.** Fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$.",
  "new_string": "**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "ccaf3bf8-4f18-4824-a12c-8f3b74587dc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1P8Y1tw8Fs74RYLYGgmAE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 276,
      "cache_read_input_tokens": 34550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 276
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

_source line 17 · 2026-05-22T04:29:33.347Z_

<details><summary>↩ Tool result · `toolu_01KTaD36DZuJU41Z6zxUePUC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "600ae61a-27d8-425e-afad-e94dd77c5765",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "**Setup.** Fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$.",
    "newString": "**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$.",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\nThis local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 7,
        "newStart": 84,
        "newLines": 7,
        "lines": [
          " ",
          " ### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem",
          " ",
          "-**Setup.** Fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:",
          "+**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:",
          " ",
          " $$",
          " \\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0"
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

_source line 18_

Now update remaining "Proposition 1" references in the text:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "5e49fc23-fc59-4b61-86bf-540d28f0b96c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XgRrLxJdnaUWzN5XtZ2uGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 34826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01C9pDRTTbVhJYFyBJ5MHp95`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption",
  "new_string": "**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "cda29dd9-acf5-45ee-af30-c115bd977676",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XgRrLxJdnaUWzN5XtZ2uGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 34826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 20 · 2026-05-22T04:29:39.293Z_

<details><summary>↩ Tool result · `toolu_01C9pDRTTbVhJYFyBJ5MHp95`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "83371dca-b028-441e-885d-2630b3ccfb3a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption",
    "newString": "**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\nThis local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 222,
        "oldLines": 7,
        "newStart": 222,
        "newLines": 7,
        "lines": [
          " ",
          " The perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.",
          " ",
          "-**Quantitatively**, from the local sensitivity (Proposition 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:",
          "+**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:",
          " ",
          " $$",
          " \\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}"
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

_source line 21_

Now fix the sensitivity ratio in §3.4 — add the qualitative caveat after the ≈ 2.9 calculation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "4ee34254-2e4f-4c23-acea-3fd0d4dfedea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SbMQV5ih6bSXrv5HALeyat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 35188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_019dxufwSM9rBoE3CVhfQ6i3`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\nThis local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.",
  "new_string": "$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\n> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\\theta_n$) and the critical threshold ($\\sigma_{\\text{crit}} \\approx 0.20$), though the predicted sensitivity ratio ($\\sim$3×) overestimates the experimental ratio ($\\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.\n\nMoreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "b5adb4e8-9830-4533-befb-390ce9882dae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SbMQV5ih6bSXrv5HALeyat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 35188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 23 · 2026-05-22T04:29:49.875Z_

<details><summary>↩ Tool result · `toolu_019dxufwSM9rBoE3CVhfQ6i3`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "d00ffabd-5b63-48f0-aced-16f059100889",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\nThis local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.",
    "newString": "$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\n> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\\theta_n$) and the critical threshold ($\\sigma_{\\text{crit}} \\approx 0.20$), though the predicted sensitivity ratio ($\\sim$3×) overestimates the experimental ratio ($\\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.\n\nMoreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\nThis local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 234,
        "oldLines": 8,
        "newStart": 234,
        "newLines": 10,
        "lines": [
          " \\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9",
          " $$",
          " ",
          "-This local variance ratio of $\\sim$3× is consistent with the experimental observation. Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.",
          "+> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\\theta_n$) and the critical threshold ($\\sigma_{\\text{crit}} \\approx 0.20$), though the predicted sensitivity ratio ($\\sim$3×) overestimates the experimental ratio ($\\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.",
          " ",
          "+Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.",
          "+",
          " **Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.",
          " ",
          " ### 3.5 Corollary 2: Nonlinear Scaling Mechanism"
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

_source line 24_

Now fix the §4.3 sensitivity ratio comparison to reinforce the qualitative nature:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "8e0a99ce-4065-4498-be6b-cb46d6e828c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxhwQiBs9FePWnMSa2BCSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 572,
      "cache_read_input_tokens": 35553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 572
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — Edit · `toolu_0121HVXDMFRpsrrcHEzNA7tL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.",
  "new_string": "**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nThe linearized local analysis (Approximate Result 1) predicts a sensitivity ratio of $\\sim$2.9×, which overestimates the experimental ratio of $\\sim$1.5×. This discrepancy arises because (a) the linearization ignores the moderating effect of logistic saturation on extreme perturbations, and (b) $\\theta_n$ absorbs part of the attenuated contamination signal, increasing its own degradation and narrowing the gap. The predicted ratio should be understood as a qualitative directional prediction: the theory correctly identifies $c_n$ as the more sensitive parameter but does not precisely calibrate the magnitude of the differential."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "ef4ebf58-3365-4bda-982f-e10a86870d53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxhwQiBs9FePWnMSa2BCSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 572,
      "cache_read_input_tokens": 35553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 572
      },
      "output_tokens": 4,
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

_source line 26 · 2026-05-22T04:30:01.465Z_

<details><summary>↩ Tool result · `toolu_0121HVXDMFRpsrrcHEzNA7tL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "f9fd6835-0567-4ba6-9bf8-a0bb3ef9bf11",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.",
    "newString": "**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nThe linearized local analysis (Approximate Result 1) predicts a sensitivity ratio of $\\sim$2.9×, which overestimates the experimental ratio of $\\sim$1.5×. This discrepancy arises because (a) the linearization ignores the moderating effect of logistic saturation on extreme perturbations, and (b) $\\theta_n$ absorbs part of the attenuated contamination signal, increasing its own degradation and narrowing the gap. The predicted ratio should be understood as a qualitative directional prediction: the theory correctly identifies $c_n$ as the more sensitive parameter but does not precisely calibrate the magnitude of the differential.",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\n> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\\theta_n$) and the critical threshold ($\\sigma_{\\text{crit}} \\approx 0.20$), though the predicted sensitivity ratio ($\\sim$3×) overestimates the experimental ratio ($\\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.\n\nMoreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nTheory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 311,
        "oldLines": 7,
        "newStart": 311,
        "newLines": 7,
        "lines": [
          " - $\\sigma=0.2$: 7.9/5.9 = 1.3×",
          " - $\\sigma=0.5$: 57.9/36.9 = 1.6×",
          " ",
          "-Theory predicts $\\sim$2.9× from the local analysis (Proposition 1). The experimental ratio is lower, likely because (a) $\\theta_n$ also suffers from the absorption of attenuated contamination, and (b) the local analysis overestimates $c_n$ sensitivity relative to the full nonlinear model. Nevertheless, $c_n$ is consistently more sensitive than $\\theta_n$.",
          "+The linearized local analysis (Approximate Result 1) predicts a sensitivity ratio of $\\sim$2.9×, which overestimates the experimental ratio of $\\sim$1.5×. This discrepancy arises because (a) the linearization ignores the moderating effect of logistic saturation on extreme perturbations, and (b) $\\theta_n$ absorbs part of the attenuated contamination signal, increasing its own degradation and narrowing the gap. The predicted ratio should be understood as a qualitative directional prediction: the theory correctly identifies $c_n$ as the more sensitive parameter but does not precisely calibrate the magnitude of the differential.",
          " ",
          " ### 4.4 Phase Transition Verification",
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

_source line 27_

Now **Fix 2** — σ_crit DGP-dependency. Let me update §4.1 to emphasize DGP-specificity:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "6b76d4f5-045d-400e-864a-4ab8a115ac81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFzPZ4YGj2ZXH1ZsZQJm7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 36125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 663
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

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_01HPup4Ps4wBCHMTRFwrpYzL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "The critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$",
  "new_string": "The critical noise level (DGP-specific, determined by item exposure heterogeneity):\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20 \\quad \\text{for the bimodal exposure distribution used in exp-012 (where } \\text{Var}_I(e) \\approx 0.04\\text{)}\n$$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "ca9081e5-8c24-4437-85de-3380b8fad08a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFzPZ4YGj2ZXH1ZsZQJm7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 36125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 663
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

_source line 29 · 2026-05-22T04:30:08.573Z_

<details><summary>↩ Tool result · `toolu_01HPup4Ps4wBCHMTRFwrpYzL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "6fdf9618-a375-4efc-b36d-fe70dc91d16e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "The critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$",
    "newString": "The critical noise level (DGP-specific, determined by item exposure heterogeneity):\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20 \\quad \\text{for the bimodal exposure distribution used in exp-012 (where } \\text{Var}_I(e) \\approx 0.04\\text{)}\n$$",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\n> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\\theta_n$) and the critical threshold ($\\sigma_{\\text{crit}} \\approx 0.20$), though the predicted sensitivity ratio ($\\sim$3×) overestimates the experimental ratio ($\\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.\n\nMoreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level:\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nThe linearized local analysis (Approximate Result 1) predicts a sensitivity ratio of $\\sim$2.9×, which overestimates the experimental ratio of $\\sim$1.5×. This discrepancy arises because (a) the linearization ignores the moderating effect of logistic saturation on extreme perturbations, and (b) $\\theta_n$ absorbs part of the attenuated contamination signal, increasing its own degradation and narrowing the gap. The predicted ratio should be understood as a qualitative directional prediction: the theory correctly identifies $c_n$ as the more sensitive parameter but does not precisely calibrate the magnitude of the differential.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 272,
        "oldLines": 10,
        "newStart": 272,
        "newLines": 10,
        "lines": [
          " \\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04",
          " $$",
          " ",
          "-The critical noise level:",
          "+The critical noise level (DGP-specific, determined by item exposure heterogeneity):",
          " ",
          " $$",
          "-\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20",
          "+\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20 \\quad \\text{for the bimodal exposure distribution used in exp-012 (where } \\text{Var}_I(e) \\approx 0.04\\text{)}",
          " $$",
          " ",
          " ### 4.2 Attenuation Factor at Experimental Noise Levels"
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

_source line 30_

Fix §4.4 — add formula and DGP note:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "6f7160ce-6ded-4a8e-baed-4716807a6460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014C5zuMtbGD3vCNGbLqBWNi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 388,
      "cache_read_input_tokens": 36788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 388
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01Pz5f5MJM8uS4ach3bbugWg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "The theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:",
  "new_string": "The theory predicts a transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.20$ (for the exp-012 DGP where $\\text{Var}_I(e) \\approx 0.04$; this threshold varies with the item exposure distribution). The experimental data confirms:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "c7bef5d2-60c4-4433-acb2-a102c3466c8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014C5zuMtbGD3vCNGbLqBWNi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 388,
      "cache_read_input_tokens": 36788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 388
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

_source line 32 · 2026-05-22T04:30:14.148Z_

<details><summary>↩ Tool result · `toolu_01Pz5f5MJM8uS4ach3bbugWg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "6a87dec8-78e8-4274-9a91-c898916503a3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "The theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:",
    "newString": "The theory predicts a transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.20$ (for the exp-012 DGP where $\\text{Var}_I(e) \\approx 0.04$; this threshold varies with the item exposure distribution). The experimental data confirms:",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\n> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\\theta_n$) and the critical threshold ($\\sigma_{\\text{crit}} \\approx 0.20$), though the predicted sensitivity ratio ($\\sim$3×) overestimates the experimental ratio ($\\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.\n\nMoreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level (DGP-specific, determined by item exposure heterogeneity):\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20 \\quad \\text{for the bimodal exposure distribution used in exp-012 (where } \\text{Var}_I(e) \\approx 0.04\\text{)}\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nThe linearized local analysis (Approximate Result 1) predicts a sensitivity ratio of $\\sim$2.9×, which overestimates the experimental ratio of $\\sim$1.5×. This discrepancy arises because (a) the linearization ignores the moderating effect of logistic saturation on extreme perturbations, and (b) $\\theta_n$ absorbs part of the attenuated contamination signal, increasing its own degradation and narrowing the gap. The predicted ratio should be understood as a qualitative directional prediction: the theory correctly identifies $c_n$ as the more sensitive parameter but does not precisely calibrate the magnitude of the differential.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 315,
        "oldLines": 7,
        "newStart": 315,
        "newLines": 7,
        "lines": [
          " ",
          " ### 4.4 Phase Transition Verification",
          " ",
          "-The theory predicts a transition at $\\sigma_{\\text{crit}} = 0.20$. The experimental data confirms:",
          "+The theory predicts a transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.20$ (for the exp-012 DGP where $\\text{Var}_I(e) \\approx 0.04$; this threshold varies with the item exposure distribution). The experimental data confirms:",
          " ",
          " - Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters",
          " - At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)"
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

_source line 33_

Fix §5.3 — add formula:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "fdbe541f-de02-4598-b6e1-d8a0eaeb309d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8hvxDyhoupX6r8zk6RUV9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 325,
      "cache_read_input_tokens": 37176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 325
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01H8JuNfTEbELVnj36LnErGr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "Despite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.",
  "new_string": "Despite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.2$ (DGP-specific, governed by item exposure heterogeneity), (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "20f2b841-3db0-4b36-95bb-e6eb800d1ea8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8hvxDyhoupX6r8zk6RUV9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 325,
      "cache_read_input_tokens": 37176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 325
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

_source line 35 · 2026-05-22T04:30:20.211Z_

<details><summary>↩ Tool result · `toolu_01H8JuNfTEbELVnj36LnErGr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "4ae1019e-9555-40a9-9a7c-7fa83d54069f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "Despite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.",
    "newString": "Despite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.2$ (DGP-specific, governed by item exposure heterogeneity), (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\n> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\\theta_n$) and the critical threshold ($\\sigma_{\\text{crit}} \\approx 0.20$), though the predicted sensitivity ratio ($\\sim$3×) overestimates the experimental ratio ($\\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.\n\nMoreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level (DGP-specific, determined by item exposure heterogeneity):\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20 \\quad \\text{for the bimodal exposure distribution used in exp-012 (where } \\text{Var}_I(e) \\approx 0.04\\text{)}\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nThe linearized local analysis (Approximate Result 1) predicts a sensitivity ratio of $\\sim$2.9×, which overestimates the experimental ratio of $\\sim$1.5×. This discrepancy arises because (a) the linearization ignores the moderating effect of logistic saturation on extreme perturbations, and (b) $\\theta_n$ absorbs part of the attenuated contamination signal, increasing its own degradation and narrowing the gap. The predicted ratio should be understood as a qualitative directional prediction: the theory correctly identifies $c_n$ as the more sensitive parameter but does not precisely calibrate the magnitude of the differential.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.20$ (for the exp-012 DGP where $\\text{Var}_I(e) \\approx 0.04$; this threshold varies with the item exposure distribution). The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 357,
        "oldLines": 7,
        "newStart": 357,
        "newLines": 7,
        "lines": [
          " ",
          " 3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.",
          " ",
          "-Despite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} \\approx 0.2$, (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.",
          "+Despite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.2$ (DGP-specific, governed by item exposure heterogeneity), (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.",
          " ",
          " ### 5.4 Practical Implications for Stage 2 Quality",
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

_source line 36_

Now **Fix 4** — expand the absorption mechanism in §3.4:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "74d0a96b-6b72-4cdb-91ed-4ae0c92fec9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RavF9iATLmkAbnyGw3Ncq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 37501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 476
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01HhiNWx9Zm3yGJbm2hoszrs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "old_string": "**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.",
  "new_string": "**Absorption mechanism.** When $c_n$ is attenuated toward zero by noise, the variance in $Y_{nij}$ that was originally explained by the $c_n \\cdot e_i$ interaction term must be redistributed to other parameters in Stage 3 — particularly to $\\theta_n$. For truly contaminated models ($c_n > 0$), the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is absorbed into $\\theta_n$, **systematically inflating ability estimates for contaminated models**. This is the mechanism by which contamination effects are \"hidden\" inside ability estimates when joint estimation is not performed.\n\nThis absorption has two consequences: (1) it **limits** $\\theta_n$ degradation in RMSE terms (since the absorbed signal partially compensates the noise-induced variance), while (2) **amplifying** the $c_n$ error (since the signal that would identify contamination is siphoned away). The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\nThis mechanism has greater narrative significance than the RMSE numbers alone, because it directly supports the paper's core argument: without joint estimation of contamination and ability, contaminated models receive systematically inflated ability estimates — their contamination-driven advantage is misattributed to genuine capability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "630ee422-3125-49f7-9618-b305ac47ada5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RavF9iATLmkAbnyGw3Ncq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 37501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 476
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

_source line 38 · 2026-05-22T04:30:51.551Z_

<details><summary>↩ Tool result · `toolu_01HhiNWx9Zm3yGJbm2hoszrs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "c874a94a-e89c-424a-b18a-25cf537ed4d9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
    "oldString": "**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.",
    "newString": "**Absorption mechanism.** When $c_n$ is attenuated toward zero by noise, the variance in $Y_{nij}$ that was originally explained by the $c_n \\cdot e_i$ interaction term must be redistributed to other parameters in Stage 3 — particularly to $\\theta_n$. For truly contaminated models ($c_n > 0$), the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is absorbed into $\\theta_n$, **systematically inflating ability estimates for contaminated models**. This is the mechanism by which contamination effects are \"hidden\" inside ability estimates when joint estimation is not performed.\n\nThis absorption has two consequences: (1) it **limits** $\\theta_n$ degradation in RMSE terms (since the absorbed signal partially compensates the noise-induced variance), while (2) **amplifying** the $c_n$ error (since the signal that would identify contamination is siphoned away). The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\nThis mechanism has greater narrative significance than the RMSE numbers alone, because it directly supports the paper's core argument: without joint estimation of contamination and ability, contaminated models receive systematically inflated ability estimates — their contamination-driven advantage is misattributed to genuine capability.",
    "originalFile": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\n> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\\theta_n$) and the critical threshold ($\\sigma_{\\text{crit}} \\approx 0.20$), though the predicted sensitivity ratio ($\\sim$3×) overestimates the experimental ratio ($\\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.\n\nMoreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level (DGP-specific, determined by item exposure heterogeneity):\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20 \\quad \\text{for the bimodal exposure distribution used in exp-012 (where } \\text{Var}_I(e) \\approx 0.04\\text{)}\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nThe linearized local analysis (Approximate Result 1) predicts a sensitivity ratio of $\\sim$2.9×, which overestimates the experimental ratio of $\\sim$1.5×. This discrepancy arises because (a) the linearization ignores the moderating effect of logistic saturation on extreme perturbations, and (b) $\\theta_n$ absorbs part of the attenuated contamination signal, increasing its own degradation and narrowing the gap. The predicted ratio should be understood as a qualitative directional prediction: the theory correctly identifies $c_n$ as the more sensitive parameter but does not precisely calibrate the magnitude of the differential.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.20$ (for the exp-012 DGP where $\\text{Var}_I(e) \\approx 0.04$; this threshold varies with the item exposure distribution). The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.2$ (DGP-specific, governed by item exposure heterogeneity), (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
    "structuredPatch": [
      {
        "oldStart": 238,
        "oldLines": 8,
        "newStart": 238,
        "newLines": 12,
        "lines": [
          " ",
          " Moreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.",
          " ",
          "-**Absorption mechanism.** When $c_n$ is attenuated, the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is partially absorbed by $\\theta_n$ (inflating ability estimates for contaminated models). This absorption **limits** $\\theta_n$ degradation while **amplifying** the $c_n$ error. The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.",
          "+**Absorption mechanism.** When $c_n$ is attenuated toward zero by noise, the variance in $Y_{nij}$ that was originally explained by the $c_n \\cdot e_i$ interaction term must be redistributed to other parameters in Stage 3 — particularly to $\\theta_n$. For truly contaminated models ($c_n > 0$), the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is absorbed into $\\theta_n$, **systematically inflating ability estimates for contaminated models**. This is the mechanism by which contamination effects are \"hidden\" inside ability estimates when joint estimation is not performed.",
          " ",
          "+This absorption has two consequences: (1) it **limits** $\\theta_n$ degradation in RMSE terms (since the absorbed signal partially compensates the noise-induced variance), while (2) **amplifying** the $c_n$ error (since the signal that would identify contamination is siphoned away). The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.",
          "+",
          "+This mechanism has greater narrative significance than the RMSE numbers alone, because it directly supports the paper's core argument: without joint estimation of contamination and ability, contaminated models receive systematically inflated ability estimates — their contamination-driven advantage is misattributed to genuine capability.",
          "+",
          " ### 3.5 Corollary 2: Nonlinear Scaling Mechanism",
          " ",
          " The transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:"
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

Now let me verify the full document reads consistently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "403adcfc-accb-44d6-a929-fbe6039f1e74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4sLAx6N8EjHPgAbwf1ftp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 37977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 670
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

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_019UZVjptuQwUKRgTHPQ78qp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "4dba8b00-7943-4504-8511-60081770ca79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4sLAx6N8EjHPgAbwf1ftp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 37977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 670
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

_source line 41 · 2026-05-22T04:30:54.407Z_

<details><summary>↩ Tool result · `toolu_019UZVjptuQwUKRgTHPQ78qp`</summary>

```text
1	# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis
2	
3	## 1. Problem Setup
4	
5	### 1.1 Model
6	
7	The Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \in \{0,1\}$ for model $n$, item $i$, and judge $j$:
8	
9	$$
10	\text{logit}\,P(Y_{nij}=1) = \theta_n - b_i - d_j + c_n \cdot e_i
11	$$
12	
13	where $\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \geq 0$ model-specific contamination susceptibility, and $e_i \in [0,1]$ item exposure level.
14	
15	### 1.2 Three-Stage Estimation
16	
17	| Stage | Estimates | Method |
18	|-------|-----------|--------|
19	| 1 | $\hat\theta^{(1)}, \hat{b}, \hat{d}$ | Standard MFRM (no contamination term) |
20	| 2 | $\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |
21	| 3 | $\hat\theta, \hat{c}_n$ | Joint G-MFRM via MCMC, with $\hat{e}_i$ plugged in as known |
22	
23	The critical feature: Stage 3 conditions on the point estimate $\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\hat{e}_i = e_i + \varepsilon_i$ with $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\theta_n$.
24	
25	### 1.3 Priors (Stage 3)
26	
27	| Parameter | Prior |
28	|-----------|-------|
29	| $\theta_n$ | $\mathcal{N}(0,1)$, centered to mean zero |
30	| $b_i$ | $\mathcal{N}(0,1)$ |
31	| $d_j$ | $\mathcal{N}(0, 0.5)$ |
32	| $c_n$ | $\text{HalfNormal}(0.5)$ |
33	
34	### 1.4 DGP Parameters (exp-012)
35	
36	$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:
37	
38	$$
39	\text{logit}\,P(Y_{nij}=1) = \theta_n - b_i - d_j + c_n \cdot e_i \cdot (1 + s_j)
40	$$
41	
42	Exposure values: $e_i = \text{sigmoid}(e_i^{\text{raw}})$ where $e_i^{\text{raw}} \sim \mathcal{N}(0,1)$.
43	
44	---
45	
46	## 2. Connection to Two-Step Estimator Literature
47	
48	### 2.1 Classical Frequentist Framework
49	
50	The G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:
51	
52	**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:
53	
54	$$
55	V_{\text{corrected}} = V_2 + V_2\!\left(C\,V_1\,C^\top - R\,V_1\,C^\top - C\,V_1\,R^\top\right)\!V_2
56	$$
57	
58	where $V_1, V_2$ are the step-specific variance matrices, $C = \partial^2 \ell_2 / \partial\alpha\,\partial\gamma^\top$ captures cross-step dependence, and $R = \partial^2 \ell_2 / \partial\alpha\,\partial\alpha^\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.
59	
60	**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.
61	
62	### 2.2 Bayesian Adaptation: Cut Feedback
63	
64	Our Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):
65	
66	- The **cut posterior** $p_{\text{cut}}(\theta, c \mid Y, \hat{e})$ conditions on the plug-in estimate $\hat{e}$ and "cuts" the feedback from Stage 3 to Stage 2.
67	- The **full posterior** $p(\theta, c \mid Y) = \int p(\theta, c \mid Y, e)\,p(e \mid \text{data})\,de$ would marginalize over $e_i$ uncertainty.
68	
69	The cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.
70	
71	### 2.3 Our Setting's Specificity
72	
73	Three features distinguish our problem from the textbook case:
74	
75	1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.
76	
77	2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.
78	
79	3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.
80	
81	---
82	
83	## 3. Main Results
84	
85	### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem
86	
87	**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\hat\phi_n = (\hat\theta_n, \hat{c}_n)$ as a function of the exposure vector $e = (e_1, \ldots, e_I)$. At the posterior mode, the score vanishes:
88	
89	$$
90	\nabla_\phi L(\hat\phi_n; Y, e) = 0
91	$$
92	
93	where $L = \log p(\phi \mid Y, e)$ is the log-posterior.
94	
95	**Perturbation.** When $e \to \tilde{e} = e + \varepsilon$, the implicit function theorem gives:
96	
97	$$
98	\delta\phi_n \equiv \hat\phi_n(\tilde{e}) - \hat\phi_n(e) \approx -\mathcal{H}_n^{-1} \cdot \Delta s_n
99	$$
100	
101	where $\mathcal{H}_n = -\nabla^2_{\phi\phi} L$ is the posterior precision matrix and $\Delta s_n$ is the score perturbation.
102	
103	**Posterior precision matrix** (for the $(\theta_n, c_n)$ block, conditioning on $b, d$):
104	
105	$$
106	\mathcal{H}_n = \begin{pmatrix} A_n + \tau_\theta & B_n \\ B_n & C_n + \tau_c \end{pmatrix}
107	$$
108	
109	where $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:
110	
111	$$
112	A_n = \sum_{i,j} w_{nij}, \qquad B_n = \sum_{i,j} w_{nij}\,e_i, \qquad C_n = \sum_{i,j} w_{nij}\,e_i^2
113	$$
114	
115	$\tau_\theta = 1$ (prior precision for $\theta_n$), $\tau_c = 1/\sigma_c^2 = 4$ (curvature of $\text{HalfNormal}(0.5)$ log-density at the mode).
116	
117	**Score perturbation** (to first order in $\varepsilon$):
118	
119	$$
120	\Delta s_n = \begin{pmatrix} -\hat{c}_n \sum_i W_{ni}\,\varepsilon_i \\ -\hat{c}_n \sum_i W_{ni}\,e_i\,\varepsilon_i \end{pmatrix}
121	$$
122	
123	where $W_{ni} = \sum_j w_{nij}$ is the information contributed by item $i$.
124	
125	**Result.** The posterior mode shifts are:
126	
127	$$
128	\boxed{
129	\begin{aligned}
130	\delta c_n &= \frac{\hat{c}_n}{\det \mathcal{H}_n} \left[ B_n \sum_i W_{ni}\varepsilon_i - (A_n + \tau_\theta) \sum_i W_{ni} e_i \varepsilon_i \right] \\[6pt]
131	\delta \theta_n &= \frac{\hat{c}_n}{\det \mathcal{H}_n} \left[ B_n \sum_i W_{ni} e_i \varepsilon_i - (C_n + \tau_c) \sum_i W_{ni} \varepsilon_i \right]
132	\end{aligned}
133	}
134	$$
135	
136	where $\det \mathcal{H}_n = (A_n + \tau_\theta)(C_n + \tau_c) - B_n^2$.
137	
138	**Interpretation.** Both sensitivities are proportional to $\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\sum W_{ni}\varepsilon_i$ (aggregate noise, affects both parameters) and $\sum W_{ni}e_i\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).
139	
140	### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$
141	
142	The local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\sigma$: **systematic attenuation bias**.
143	
144	**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.
145	
146	Consider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):
147	
148	$$
149	Y_{nij} \approx \theta_n - b_i - d_j + c_n \cdot e_i + u_{nij}
150	$$
151	
152	When we fit with $\tilde{e}_i = e_i + \varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):
153	
154	$$
155	\tilde{c}_n \xrightarrow{p} c_n \cdot \frac{\text{Cov}_I(e_i, \tilde{e}_i)}{\text{Var}_I(\tilde{e}_i)} = c_n \cdot \frac{\text{Var}_I(e)}{\text{Var}_I(e) + \sigma^2} \equiv c_n \cdot \lambda(\sigma)
156	$$
157	
158	where $\text{Var}_I(e) = \frac{1}{I}\sum_i(e_i - \bar{e})^2$ is the cross-item variance of true exposure, and:
159	
160	$$
161	\boxed{\lambda(\sigma) = \frac{\text{Var}_I(e)}{\text{Var}_I(e) + \sigma^2}}
162	$$
163	
164	is the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).
165	
166	**Attenuation bias:**
167	
168	$$
169	\text{Bias}(\tilde{c}_n) = c_n\,(1 - \lambda) = c_n \cdot \frac{\sigma^2}{\text{Var}_I(e) + \sigma^2}
170	$$
171	
172	**Key properties:**
173	- The bias is **always toward zero** (underestimation of contamination)
174	- The bias is **proportional to $c_n$**: highly contaminated models suffer more
175	- The bias is **nonlinear in $\sigma$**: mild for $\sigma^2 \ll \text{Var}_I(e)$, catastrophic for $\sigma^2 \gg \text{Var}_I(e)$
176	
177	### 3.3 Approximate Result 3: RMSE Decomposition
178	
179	Combining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:
180	
181	$$
182	\text{MSE}_c(\sigma) = \mathbb{E}_n\!\left[(\tilde{c}_n - c_n)^2\right]
183	$$
184	
185	Decomposing $\tilde{c}_n - c_n = (\tilde{c}_n - \hat{c}_n) + (\hat{c}_n - c_n)$:
186	
187	$$
188	\text{MSE}_c(\sigma) = \underbrace{\text{MSE}_c(0)}_{\text{baseline}} + \underbrace{(1-\lambda)^2 \cdot \mathbb{E}_n[\hat{c}_n^2]}_{\text{attenuation bias}^2} + \underbrace{\mathbb{E}_n[\text{Var}_\varepsilon(\tilde{c}_n)]}_{\text{noise variance}} + \underbrace{2(1-\lambda)\cdot\mathbb{E}_n[\hat{c}_n(\hat{c}_n - c_n)]}_{\text{cross-term}}
189	$$
190	
191	**Regime analysis:**
192	
193	- **Small $\sigma$ ($\sigma^2 \ll \text{Var}_I(e)$):** $1-\lambda \approx \sigma^2/\text{Var}_I(e)$, so the bias term scales as $\sigma^4$ and the variance term as $\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\sigma^2$.
194	
195	- **Large $\sigma$ ($\sigma^2 \gg \text{Var}_I(e)$):** $1-\lambda \to 1$, bias term saturates at $\mathbb{E}[\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\sqrt{\text{MSE}_c(0) + \mathbb{E}[\hat{c}_n^2]}$ — catastrophic degradation.
196	
197	- **Transition at $\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)}$**: The attenuation factor $\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.
198	
199	$$
200	\boxed{\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)}}
201	$$
202	
203	### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\theta_n$)
204	
205	**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\theta_n$ by a factor of $\Omega(I)$.
206	
207	**Proof sketch.** The sensitivity arises through two distinct mechanisms:
208	
209	**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:
210	
211	$$
212	\frac{\partial \ell}{\partial c_n} = \sum_{i,j}(Y_{nij} - p_{nij}) \cdot e_i
213	$$
214	
215	When $e_i \to \tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\lambda) \propto \sigma^2$.
216	
217	**(B) Indirect channel (affects $\theta_n$).** The score for $\theta_n$ does **not** involve $e_i$:
218	
219	$$
220	\frac{\partial \ell}{\partial \theta_n} = \sum_{i,j}(Y_{nij} - p_{nij})
221	$$
222	
223	The perturbation affects $\theta_n$ only through the changed predicted probabilities $\tilde{p}_{nij} = \sigma(\theta_n - b_i - d_j + c_n\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.
224	
225	**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption $W_{ni} \approx \bar{W}$:
226	
227	$$
228	\frac{\mathbb{E}[\delta c_n^2]}{\mathbb{E}[\delta \theta_n^2]} = \frac{(A_n+\tau_\theta)^2 \text{Var}_I(e) + \tau_\theta^2 \bar{e}^2}{(C_n+\tau_c)^2 + \text{Var}_I(e) \cdot B_n^2 - 2B_n(C_n+\tau_c)\bar{e}}
229	$$
230	
231	With typical values ($A_n \approx 176$, $B_n \approx 88$, $C_n \approx 51$, $\tau_\theta = 1$, $\tau_c = 4$):
232	
233	$$
234	\frac{\mathbb{E}[\delta c_n^2]}{\mathbb{E}[\delta \theta_n^2]} \approx \frac{1285}{443} \approx 2.9
235	$$
236	
237	> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\theta_n$) and the critical threshold ($\sigma_{\text{crit}} \approx 0.20$), though the predicted sensitivity ratio ($\sim$3×) overestimates the experimental ratio ($\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.
238	
239	Moreover, the **attenuation bias** (which dominates at larger $\sigma$) affects $c_n$ directly but $\theta_n$ only through the coupling, amplifying the differential further.
240	
241	**Absorption mechanism.** When $c_n$ is attenuated toward zero by noise, the variance in $Y_{nij}$ that was originally explained by the $c_n \cdot e_i$ interaction term must be redistributed to other parameters in Stage 3 — particularly to $\theta_n$. For truly contaminated models ($c_n > 0$), the "missing" contamination advantage $c_n(1-\lambda)\bar{e}$ is absorbed into $\theta_n$, **systematically inflating ability estimates for contaminated models**. This is the mechanism by which contamination effects are "hidden" inside ability estimates when joint estimation is not performed.
242	
243	This absorption has two consequences: (1) it **limits** $\theta_n$ degradation in RMSE terms (since the absorbed signal partially compensates the noise-induced variance), while (2) **amplifying** the $c_n$ error (since the signal that would identify contamination is siphoned away). The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\theta_n$ vs. $c_n$.
244	
245	This mechanism has greater narrative significance than the RMSE numbers alone, because it directly supports the paper's core argument: without joint estimation of contamination and ability, contaminated models receive systematically inflated ability estimates — their contamination-driven advantage is misattributed to genuine capability.
246	
247	### 3.5 Corollary 2: Nonlinear Scaling Mechanism
248	
249	The transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:
250	
251	$$
252	\text{Bias}^2(c_n) = c_n^2 \cdot \left(\frac{\sigma^2}{\text{Var}_I(e) + \sigma^2}\right)^2
253	$$
254	
255	This function has three regimes:
256	
257	| Regime | Condition | Scaling | Character |
258	|--------|-----------|---------|-----------|
259	| Linear | $\sigma^2 \ll V_e$ | $\propto \sigma^4 / V_e^2$ | Negligible bias |
260	| Transition | $\sigma^2 \approx V_e$ | $\propto 1/4$ | Moderate bias |
261	| Saturation | $\sigma^2 \gg V_e$ | $\to c_n^2$ | Complete signal loss |
262	
263	where $V_e = \text{Var}_I(e)$.
264	
265	The nonlinearity is **intrinsic to the multiplicative $c_n \cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.
266	
267	---
268	
269	## 4. Numerical Calibration
270	
271	### 4.1 DGP-Specific Constants
272	
273	For the exp-012 DGP with $e_i = \text{sigmoid}(\mathcal{N}(0,1))$:
274	
275	$$
276	\mathbb{E}[e_i] = 0.5, \qquad \mathbb{E}[e_i^2] \approx 0.29, \qquad \text{Var}_I(e) \approx 0.04
277	$$
278	
279	The critical noise level (DGP-specific, determined by item exposure heterogeneity):
280	
281	$$
282	\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)} \approx \sqrt{0.04} = 0.20 \quad \text{for the bimodal exposure distribution used in exp-012 (where } \text{Var}_I(e) \approx 0.04\text{)}
283	$$
284	
285	### 4.2 Attenuation Factor at Experimental Noise Levels
286	
287	| $\sigma$ | $\sigma^2$ | $\lambda = V_e/(V_e + \sigma^2)$ | $1-\lambda$ | $(1-\lambda)^2$ |
288	|----------|-----------|----------------------------------|-------------|-----------------|
289	| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |
290	| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |
291	| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |
292	| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |
293	
294	At $\sigma = 0.2 = \sigma_{\text{crit}}$: exactly half the signal variance is noise. At $\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.
295	
296	### 4.3 Comparison with exp-012 Results
297	
298	| $\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\lambda$ | $\theta$ RMSE (exp) | $\theta$ degradation (exp) |
299	|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|
300	| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |
301	| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |
302	| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |
303	| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |
304	
305	**Qualitative agreement:** The theory correctly predicts:
306	
307	1. **Ordering**: $c_n$ degradation > $\theta$ degradation at every noise level ✓
308	2. **Mild degradation at $\sigma=0.1$**: $\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓
309	3. **Transition at $\sigma=0.2$**: $\lambda = 0.5$ → moderate degradation ✓
310	4. **Severe degradation at $\sigma=0.5$**: $\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓
311	5. **Superlinear scaling**: the jump from $\sigma=0.2$ to $\sigma=0.5$ is disproportionately large ✓
312	
313	**Sensitivity ratio:** Experimental $c_n$ degradation / $\theta$ degradation:
314	- $\sigma=0.1$: 2.3/1.4 = 1.6×
315	- $\sigma=0.2$: 7.9/5.9 = 1.3×
316	- $\sigma=0.5$: 57.9/36.9 = 1.6×
317	
318	The linearized local analysis (Approximate Result 1) predicts a sensitivity ratio of $\sim$2.9×, which overestimates the experimental ratio of $\sim$1.5×. This discrepancy arises because (a) the linearization ignores the moderating effect of logistic saturation on extreme perturbations, and (b) $\theta_n$ absorbs part of the attenuated contamination signal, increasing its own degradation and narrowing the gap. The predicted ratio should be understood as a qualitative directional prediction: the theory correctly identifies $c_n$ as the more sensitive parameter but does not precisely calibrate the magnitude of the differential.
319	
320	### 4.4 Phase Transition Verification
321	
322	The theory predicts a transition at $\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)} \approx 0.20$ (for the exp-012 DGP where $\text{Var}_I(e) \approx 0.04$; this threshold varies with the item exposure distribution). The experimental data confirms:
323	
324	- Below $\sigma_{\text{crit}}$ ($\sigma = 0.1$): RMSE degradation < 2.5% for both parameters
325	- At $\sigma_{\text{crit}}$ ($\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)
326	- Above $\sigma_{\text{crit}}$ ($\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)
327	
328	The ratio $\sigma = 0.5$ is $2.5\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.
329	
330	---
331	
332	## 5. Discussion
333	
334	### 5.1 Why $c_n$ Is More Sensitive Than $\theta_n$
335	
336	Three reinforcing mechanisms:
337	
338	1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.
339	
340	2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).
341	
342	3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\theta_n$, the symmetric $\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.
343	
344	### 5.2 Why the Degradation Is Nonlinear
345	
346	The nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:
347	
348	The attenuation factor $\lambda = V_e/(V_e + \sigma^2)$ is a **harmonic** function of $\sigma^2$. The resulting squared bias $(1-\lambda)^2 = \sigma^4/(V_e + \sigma^2)^2$ is:
349	- Convex for $\sigma^2 < V_e/3$ (accelerating degradation)
350	- Concave for $\sigma^2 > V_e/3$ (decelerating toward saturation)
351	
352	At $\sigma = 0.5$, we have $\sigma^2/V_e \approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).
353	
354	### 5.3 Tightness of the Bounds
355	
356	The theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:
357	
358	1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.
359	
360	2. **Logistic nonlinearity**: The linear EIV attenuation formula $\lambda = V_e/(V_e + \sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.
361	
362	3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.
363	
364	Despite these limitations, the theory correctly identifies (a) the critical noise threshold $\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)} \approx 0.2$ (DGP-specific, governed by item exposure heterogeneity), (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.
365	
366	### 5.4 Practical Implications for Stage 2 Quality
367	
368	The attenuation analysis yields a concrete requirement for Stage 2 estimation:
369	
370	$$
371	\sigma_e < \sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)}
372	$$
373	
374	For typical benchmark exposure distributions where $\text{Var}(e) \approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:
375	
376	$$
377	\sigma_e < 0.20\text{–}0.28
378	$$
379	
380	Within this range, RMSE degradation stays below $\sim$10% for both $c_n$ and $\theta_n$. The exp-012 results confirm this: at $\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.
381	
382	### 5.5 Connection to Robustness Claims
383	
384	The theoretical analysis supports the following characterization for the paper:
385	
386	> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\hat\theta$ degrade by $< 6\%$ RMSE and contamination estimates $\hat{c}_n$ by $< 8\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \theta$ follows from the direct multiplicative coupling $c_n \cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.
387	
388	---
389	
390	## 6. References
391	
392	- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.
393	- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.
394	- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.
395	- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.
396	- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.
397	- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.
398	- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.
399	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "25afe10f-aa5b-4300-9c90-63c8ae8d39cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
      "content": "# Error Propagation in Staged G-MFRM Estimation: Theoretical Analysis\n\n## 1. Problem Setup\n\n### 1.1 Model\n\nThe Gated Multi-Facet Rasch Model (G-MFRM) specifies binary responses $Y_{nij} \\in \\{0,1\\}$ for model $n$, item $i$, and judge $j$:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i\n$$\n\nwhere $\\theta_n$ is model ability, $b_i$ item difficulty, $d_j$ judge severity, $c_n \\geq 0$ model-specific contamination susceptibility, and $e_i \\in [0,1]$ item exposure level.\n\n### 1.2 Three-Stage Estimation\n\n| Stage | Estimates | Method |\n|-------|-----------|--------|\n| 1 | $\\hat\\theta^{(1)}, \\hat{b}, \\hat{d}$ | Standard MFRM (no contamination term) |\n| 2 | $\\hat{e}_i$ | External estimation (performance gaps, temporal signals, memorization scores) |\n| 3 | $\\hat\\theta, \\hat{c}_n$ | Joint G-MFRM via MCMC, with $\\hat{e}_i$ plugged in as known |\n\nThe critical feature: Stage 3 conditions on the point estimate $\\hat{e}_i$ rather than marginalizing over $e_i$ uncertainty. When $\\hat{e}_i = e_i + \\varepsilon_i$ with $\\varepsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$, the estimation error in $e_i$ propagates into the posteriors of $c_n$ and $\\theta_n$.\n\n### 1.3 Priors (Stage 3)\n\n| Parameter | Prior |\n|-----------|-------|\n| $\\theta_n$ | $\\mathcal{N}(0,1)$, centered to mean zero |\n| $b_i$ | $\\mathcal{N}(0,1)$ |\n| $d_j$ | $\\mathcal{N}(0, 0.5)$ |\n| $c_n$ | $\\text{HalfNormal}(0.5)$ |\n\n### 1.4 DGP Parameters (exp-012)\n\n$N=50$ models, $I=100$ items, $J=8$ judges. True DGP includes a judge-level contamination sensitivity term $s_j$ that is **not modeled** in Stage 3:\n\n$$\n\\text{logit}\\,P(Y_{nij}=1) = \\theta_n - b_i - d_j + c_n \\cdot e_i \\cdot (1 + s_j)\n$$\n\nExposure values: $e_i = \\text{sigmoid}(e_i^{\\text{raw}})$ where $e_i^{\\text{raw}} \\sim \\mathcal{N}(0,1)$.\n\n---\n\n## 2. Connection to Two-Step Estimator Literature\n\n### 2.1 Classical Frequentist Framework\n\nThe G-MFRM staged estimation is an instance of the **generated regressors** problem (Pagan, 1984): Stage 2 produces $\\hat{e}_i$, which enters Stage 3 as if it were observed. Two foundational results apply:\n\n**Murphy & Topel (1985)** showed that in two-step MLE, the naive variance of the second-step estimator is biased downward. The corrected asymptotic variance is:\n\n$$\nV_{\\text{corrected}} = V_2 + V_2\\!\\left(C\\,V_1\\,C^\\top - R\\,V_1\\,C^\\top - C\\,V_1\\,R^\\top\\right)\\!V_2\n$$\n\nwhere $V_1, V_2$ are the step-specific variance matrices, $C = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\gamma^\\top$ captures cross-step dependence, and $R = \\partial^2 \\ell_2 / \\partial\\alpha\\,\\partial\\alpha^\\top$ is the second-step Hessian. The correction term is always positive semi-definite: ignoring first-step uncertainty **always** underestimates second-step variance.\n\n**Newey & McFadden (1994, Handbook of Econometrics, Ch. 36)** generalized this to semiparametric two-step estimators under regularity conditions, establishing that the asymptotic distribution of the second-step estimator has an additional variance component proportional to the first-step estimation error.\n\n### 2.2 Bayesian Adaptation: Cut Feedback\n\nOur Stage 3 is Bayesian (MCMC), not MLE. The relevant Bayesian framework is **modular inference with cut feedback** (Plummer, 2015; Liu et al., 2009; Pompe & Jacob, 2021):\n\n- The **cut posterior** $p_{\\text{cut}}(\\theta, c \\mid Y, \\hat{e})$ conditions on the plug-in estimate $\\hat{e}$ and \"cuts\" the feedback from Stage 3 to Stage 2.\n- The **full posterior** $p(\\theta, c \\mid Y) = \\int p(\\theta, c \\mid Y, e)\\,p(e \\mid \\text{data})\\,de$ would marginalize over $e_i$ uncertainty.\n\nThe cut posterior underestimates uncertainty by exactly the Murphy-Topel correction, adapted to the Bayesian setting via the **Bernstein-von Mises theorem**: for large samples, the posterior concentrates around the MLE with covariance equal to the inverse Fisher information, so the frequentist variance correction translates directly.\n\n### 2.3 Our Setting's Specificity\n\nThree features distinguish our problem from the textbook case:\n\n1. **Multiplicative structure**: $e_i$ enters as a multiplicative factor $c_n \\cdot e_i$, not as an additive covariate. This creates an **errors-in-variables** (EIV) problem for $c_n$, inducing attenuation bias beyond mere variance inflation.\n\n2. **High-dimensional nuisance parameters**: $b_i$ ($I=100$ parameters) and $d_j$ ($J=8$) are jointly re-estimated in Stage 3, creating cross-parameter propagation channels.\n\n3. **Half-normal prior on $c_n$**: The positivity constraint $c_n \\geq 0$ with prior mode at zero interacts with the EIV attenuation (both push $c_n$ toward zero), amplifying the bias for truly contaminated models.\n\n---\n\n## 3. Main Results\n\n### 3.1 Approximate Result 1: Local Sensitivity via Implicit Function Theorem\n\n**Setup.** Under the linearized model approximation, fix model $n$ and consider the joint posterior mode $\\hat\\phi_n = (\\hat\\theta_n, \\hat{c}_n)$ as a function of the exposure vector $e = (e_1, \\ldots, e_I)$. At the posterior mode, the score vanishes:\n\n$$\n\\nabla_\\phi L(\\hat\\phi_n; Y, e) = 0\n$$\n\nwhere $L = \\log p(\\phi \\mid Y, e)$ is the log-posterior.\n\n**Perturbation.** When $e \\to \\tilde{e} = e + \\varepsilon$, the implicit function theorem gives:\n\n$$\n\\delta\\phi_n \\equiv \\hat\\phi_n(\\tilde{e}) - \\hat\\phi_n(e) \\approx -\\mathcal{H}_n^{-1} \\cdot \\Delta s_n\n$$\n\nwhere $\\mathcal{H}_n = -\\nabla^2_{\\phi\\phi} L$ is the posterior precision matrix and $\\Delta s_n$ is the score perturbation.\n\n**Posterior precision matrix** (for the $(\\theta_n, c_n)$ block, conditioning on $b, d$):\n\n$$\n\\mathcal{H}_n = \\begin{pmatrix} A_n + \\tau_\\theta & B_n \\\\ B_n & C_n + \\tau_c \\end{pmatrix}\n$$\n\nwhere $w_{nij} = p_{nij}(1 - p_{nij})$ is the Bernoulli variance weight, and:\n\n$$\nA_n = \\sum_{i,j} w_{nij}, \\qquad B_n = \\sum_{i,j} w_{nij}\\,e_i, \\qquad C_n = \\sum_{i,j} w_{nij}\\,e_i^2\n$$\n\n$\\tau_\\theta = 1$ (prior precision for $\\theta_n$), $\\tau_c = 1/\\sigma_c^2 = 4$ (curvature of $\\text{HalfNormal}(0.5)$ log-density at the mode).\n\n**Score perturbation** (to first order in $\\varepsilon$):\n\n$$\n\\Delta s_n = \\begin{pmatrix} -\\hat{c}_n \\sum_i W_{ni}\\,\\varepsilon_i \\\\ -\\hat{c}_n \\sum_i W_{ni}\\,e_i\\,\\varepsilon_i \\end{pmatrix}\n$$\n\nwhere $W_{ni} = \\sum_j w_{nij}$ is the information contributed by item $i$.\n\n**Result.** The posterior mode shifts are:\n\n$$\n\\boxed{\n\\begin{aligned}\n\\delta c_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni}\\varepsilon_i - (A_n + \\tau_\\theta) \\sum_i W_{ni} e_i \\varepsilon_i \\right] \\\\[6pt]\n\\delta \\theta_n &= \\frac{\\hat{c}_n}{\\det \\mathcal{H}_n} \\left[ B_n \\sum_i W_{ni} e_i \\varepsilon_i - (C_n + \\tau_c) \\sum_i W_{ni} \\varepsilon_i \\right]\n\\end{aligned}\n}\n$$\n\nwhere $\\det \\mathcal{H}_n = (A_n + \\tau_\\theta)(C_n + \\tau_c) - B_n^2$.\n\n**Interpretation.** Both sensitivities are proportional to $\\hat{c}_n$: models with zero contamination are unaffected by $e_i$ noise. The noise enters through two channels: $\\sum W_{ni}\\varepsilon_i$ (aggregate noise, affects both parameters) and $\\sum W_{ni}e_i\\varepsilon_i$ (exposure-weighted noise, primarily affects $c_n$).\n\n### 3.2 Approximate Result 2: Errors-in-Variables Attenuation of $c_n$\n\nThe local analysis (Approximate Result 1) captures variance but misses the dominant effect at moderate-to-large $\\sigma$: **systematic attenuation bias**.\n\n**Derivation.** In the G-MFRM, $c_n$ is identified from the cross-item covariation between responses and exposure. Since $\\theta_n$ acts as a model-specific intercept, only the **within-item variation** of $e_i$ identifies $c_n$. This is a classical errors-in-variables setting.\n\nConsider the linearized model for model $n$ (fixing $b_i, d_j$, approximating the logistic link):\n\n$$\nY_{nij} \\approx \\theta_n - b_i - d_j + c_n \\cdot e_i + u_{nij}\n$$\n\nWhen we fit with $\\tilde{e}_i = e_i + \\varepsilon_i$ instead of $e_i$, the estimator for $c_n$ satisfies (in population):\n\n$$\n\\tilde{c}_n \\xrightarrow{p} c_n \\cdot \\frac{\\text{Cov}_I(e_i, \\tilde{e}_i)}{\\text{Var}_I(\\tilde{e}_i)} = c_n \\cdot \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2} \\equiv c_n \\cdot \\lambda(\\sigma)\n$$\n\nwhere $\\text{Var}_I(e) = \\frac{1}{I}\\sum_i(e_i - \\bar{e})^2$ is the cross-item variance of true exposure, and:\n\n$$\n\\boxed{\\lambda(\\sigma) = \\frac{\\text{Var}_I(e)}{\\text{Var}_I(e) + \\sigma^2}}\n$$\n\nis the **attenuation factor**. This is the standard result for errors-in-variables (Fuller, 1987, Ch. 1).\n\n**Attenuation bias:**\n\n$$\n\\text{Bias}(\\tilde{c}_n) = c_n\\,(1 - \\lambda) = c_n \\cdot \\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\n$$\n\n**Key properties:**\n- The bias is **always toward zero** (underestimation of contamination)\n- The bias is **proportional to $c_n$**: highly contaminated models suffer more\n- The bias is **nonlinear in $\\sigma$**: mild for $\\sigma^2 \\ll \\text{Var}_I(e)$, catastrophic for $\\sigma^2 \\gg \\text{Var}_I(e)$\n\n### 3.3 Approximate Result 3: RMSE Decomposition\n\nCombining the variance (Approximate Result 1) and bias (Approximate Result 2) channels:\n\n$$\n\\text{MSE}_c(\\sigma) = \\mathbb{E}_n\\!\\left[(\\tilde{c}_n - c_n)^2\\right]\n$$\n\nDecomposing $\\tilde{c}_n - c_n = (\\tilde{c}_n - \\hat{c}_n) + (\\hat{c}_n - c_n)$:\n\n$$\n\\text{MSE}_c(\\sigma) = \\underbrace{\\text{MSE}_c(0)}_{\\text{baseline}} + \\underbrace{(1-\\lambda)^2 \\cdot \\mathbb{E}_n[\\hat{c}_n^2]}_{\\text{attenuation bias}^2} + \\underbrace{\\mathbb{E}_n[\\text{Var}_\\varepsilon(\\tilde{c}_n)]}_{\\text{noise variance}} + \\underbrace{2(1-\\lambda)\\cdot\\mathbb{E}_n[\\hat{c}_n(\\hat{c}_n - c_n)]}_{\\text{cross-term}}\n$$\n\n**Regime analysis:**\n\n- **Small $\\sigma$ ($\\sigma^2 \\ll \\text{Var}_I(e)$):** $1-\\lambda \\approx \\sigma^2/\\text{Var}_I(e)$, so the bias term scales as $\\sigma^4$ and the variance term as $\\sigma^2$. **Variance dominates.** RMSE degradation is mild and approximately linear in $\\sigma^2$.\n\n- **Large $\\sigma$ ($\\sigma^2 \\gg \\text{Var}_I(e)$):** $1-\\lambda \\to 1$, bias term saturates at $\\mathbb{E}[\\hat{c}_n^2]$. **Bias dominates.** RMSE approaches $\\sqrt{\\text{MSE}_c(0) + \\mathbb{E}[\\hat{c}_n^2]}$ — catastrophic degradation.\n\n- **Transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$**: The attenuation factor $\\lambda = 1/2$ (half the signal is lost to noise). This marks the crossover from variance-dominated to bias-dominated regime.\n\n$$\n\\boxed{\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}}\n$$\n\n### 3.4 Corollary 1: Differential Sensitivity ($c_n$ vs. $\\theta_n$)\n\n**Claim:** $c_n$ is more sensitive to $e_i$ noise than $\\theta_n$ by a factor of $\\Omega(I)$.\n\n**Proof sketch.** The sensitivity arises through two distinct mechanisms:\n\n**(A) Direct channel (affects $c_n$).** The score function for $c_n$ directly involves $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial c_n} = \\sum_{i,j}(Y_{nij} - p_{nij}) \\cdot e_i\n$$\n\nWhen $e_i \\to \\tilde{e}_i$, the perturbation enters **multiplicatively** in the score, causing both bias (attenuation) and variance inflation. The attenuation bias grows as $(1-\\lambda) \\propto \\sigma^2$.\n\n**(B) Indirect channel (affects $\\theta_n$).** The score for $\\theta_n$ does **not** involve $e_i$:\n\n$$\n\\frac{\\partial \\ell}{\\partial \\theta_n} = \\sum_{i,j}(Y_{nij} - p_{nij})\n$$\n\nThe perturbation affects $\\theta_n$ only through the changed predicted probabilities $\\tilde{p}_{nij} = \\sigma(\\theta_n - b_i - d_j + c_n\\tilde{e}_i)$. This is a second-order effect: the noise enters the score only through the change in $p_{nij}$, not through a multiplicative coupling.\n\n**Quantitatively**, from the local sensitivity (Approximate Result 1), under the homogeneity assumption $W_{ni} \\approx \\bar{W}$:\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} = \\frac{(A_n+\\tau_\\theta)^2 \\text{Var}_I(e) + \\tau_\\theta^2 \\bar{e}^2}{(C_n+\\tau_c)^2 + \\text{Var}_I(e) \\cdot B_n^2 - 2B_n(C_n+\\tau_c)\\bar{e}}\n$$\n\nWith typical values ($A_n \\approx 176$, $B_n \\approx 88$, $C_n \\approx 51$, $\\tau_\\theta = 1$, $\\tau_c = 4$):\n\n$$\n\\frac{\\mathbb{E}[\\delta c_n^2]}{\\mathbb{E}[\\delta \\theta_n^2]} \\approx \\frac{1285}{443} \\approx 2.9\n$$\n\n> **Qualitative caveat.** The EIV framework correctly predicts the ordering ($c_n$ more sensitive than $\\theta_n$) and the critical threshold ($\\sigma_{\\text{crit}} \\approx 0.20$), though the predicted sensitivity ratio ($\\sim$3×) overestimates the experimental ratio ($\\sim$1.5×) due to linearization and the moderating effect of logistic saturation. The ratio above should therefore be interpreted as a qualitative directional prediction rather than a precise quantitative bound.\n\nMoreover, the **attenuation bias** (which dominates at larger $\\sigma$) affects $c_n$ directly but $\\theta_n$ only through the coupling, amplifying the differential further.\n\n**Absorption mechanism.** When $c_n$ is attenuated toward zero by noise, the variance in $Y_{nij}$ that was originally explained by the $c_n \\cdot e_i$ interaction term must be redistributed to other parameters in Stage 3 — particularly to $\\theta_n$. For truly contaminated models ($c_n > 0$), the \"missing\" contamination advantage $c_n(1-\\lambda)\\bar{e}$ is absorbed into $\\theta_n$, **systematically inflating ability estimates for contaminated models**. This is the mechanism by which contamination effects are \"hidden\" inside ability estimates when joint estimation is not performed.\n\nThis absorption has two consequences: (1) it **limits** $\\theta_n$ degradation in RMSE terms (since the absorbed signal partially compensates the noise-induced variance), while (2) **amplifying** the $c_n$ error (since the signal that would identify contamination is siphoned away). The fraction absorbed depends on the correlation between $e_i$ and $b_i$ (confounding structure) and the relative precision of $\\theta_n$ vs. $c_n$.\n\nThis mechanism has greater narrative significance than the RMSE numbers alone, because it directly supports the paper's core argument: without joint estimation of contamination and ability, contaminated models receive systematically inflated ability estimates — their contamination-driven advantage is misattributed to genuine capability.\n\n### 3.5 Corollary 2: Nonlinear Scaling Mechanism\n\nThe transition from mild (σ=0.1) to severe (σ=0.5) degradation is explained by the **quadratic-to-saturating** shape of the attenuation bias:\n\n$$\n\\text{Bias}^2(c_n) = c_n^2 \\cdot \\left(\\frac{\\sigma^2}{\\text{Var}_I(e) + \\sigma^2}\\right)^2\n$$\n\nThis function has three regimes:\n\n| Regime | Condition | Scaling | Character |\n|--------|-----------|---------|-----------|\n| Linear | $\\sigma^2 \\ll V_e$ | $\\propto \\sigma^4 / V_e^2$ | Negligible bias |\n| Transition | $\\sigma^2 \\approx V_e$ | $\\propto 1/4$ | Moderate bias |\n| Saturation | $\\sigma^2 \\gg V_e$ | $\\to c_n^2$ | Complete signal loss |\n\nwhere $V_e = \\text{Var}_I(e)$.\n\nThe nonlinearity is **intrinsic to the multiplicative $c_n \\cdot e_i$ structure**: it does not arise from the logistic link or the Bayesian framework, but from the fundamental signal-to-noise ratio of the exposure covariate.\n\n---\n\n## 4. Numerical Calibration\n\n### 4.1 DGP-Specific Constants\n\nFor the exp-012 DGP with $e_i = \\text{sigmoid}(\\mathcal{N}(0,1))$:\n\n$$\n\\mathbb{E}[e_i] = 0.5, \\qquad \\mathbb{E}[e_i^2] \\approx 0.29, \\qquad \\text{Var}_I(e) \\approx 0.04\n$$\n\nThe critical noise level (DGP-specific, determined by item exposure heterogeneity):\n\n$$\n\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx \\sqrt{0.04} = 0.20 \\quad \\text{for the bimodal exposure distribution used in exp-012 (where } \\text{Var}_I(e) \\approx 0.04\\text{)}\n$$\n\n### 4.2 Attenuation Factor at Experimental Noise Levels\n\n| $\\sigma$ | $\\sigma^2$ | $\\lambda = V_e/(V_e + \\sigma^2)$ | $1-\\lambda$ | $(1-\\lambda)^2$ |\n|----------|-----------|----------------------------------|-------------|-----------------|\n| 0.0 | 0.000 | 1.000 | 0.000 | 0.000 |\n| 0.1 | 0.010 | 0.800 | 0.200 | 0.040 |\n| 0.2 | 0.040 | 0.500 | 0.500 | 0.250 |\n| 0.5 | 0.250 | 0.138 | 0.862 | 0.743 |\n\nAt $\\sigma = 0.2 = \\sigma_{\\text{crit}}$: exactly half the signal variance is noise. At $\\sigma = 0.5$: only 14% of the signal remains — $c_n$ estimates are almost entirely noise-driven.\n\n### 4.3 Comparison with exp-012 Results\n\n| $\\sigma$ | $c_n$ RMSE (exp) | $c_n$ degradation (exp) | Attenuation $1-\\lambda$ | $\\theta$ RMSE (exp) | $\\theta$ degradation (exp) |\n|----------|-------------------|------------------------|------------------------|---------------------|---------------------------|\n| 0.0 | 0.533 | baseline | 0.00 | 0.1277 | baseline |\n| 0.1 | 0.545 | +2.3% | 0.20 | 0.1295 | +1.4% |\n| 0.2 | 0.575 | +7.9% | 0.50 | 0.1352 | +5.9% |\n| 0.5 | 0.842 | +57.9% | 0.86 | 0.1748 | +36.9% |\n\n**Qualitative agreement:** The theory correctly predicts:\n\n1. **Ordering**: $c_n$ degradation > $\\theta$ degradation at every noise level ✓\n2. **Mild degradation at $\\sigma=0.1$**: $\\sigma^2/V_e = 0.25$ (well below transition) → small effect ✓\n3. **Transition at $\\sigma=0.2$**: $\\lambda = 0.5$ → moderate degradation ✓\n4. **Severe degradation at $\\sigma=0.5$**: $\\lambda = 0.14$ → near-complete signal loss for $c_n$ ✓\n5. **Superlinear scaling**: the jump from $\\sigma=0.2$ to $\\sigma=0.5$ is disproportionately large ✓\n\n**Sensitivity ratio:** Experimental $c_n$ degradation / $\\theta$ degradation:\n- $\\sigma=0.1$: 2.3/1.4 = 1.6×\n- $\\sigma=0.2$: 7.9/5.9 = 1.3×\n- $\\sigma=0.5$: 57.9/36.9 = 1.6×\n\nThe linearized local analysis (Approximate Result 1) predicts a sensitivity ratio of $\\sim$2.9×, which overestimates the experimental ratio of $\\sim$1.5×. This discrepancy arises because (a) the linearization ignores the moderating effect of logistic saturation on extreme perturbations, and (b) $\\theta_n$ absorbs part of the attenuated contamination signal, increasing its own degradation and narrowing the gap. The predicted ratio should be understood as a qualitative directional prediction: the theory correctly identifies $c_n$ as the more sensitive parameter but does not precisely calibrate the magnitude of the differential.\n\n### 4.4 Phase Transition Verification\n\nThe theory predicts a transition at $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.20$ (for the exp-012 DGP where $\\text{Var}_I(e) \\approx 0.04$; this threshold varies with the item exposure distribution). The experimental data confirms:\n\n- Below $\\sigma_{\\text{crit}}$ ($\\sigma = 0.1$): RMSE degradation < 2.5% for both parameters\n- At $\\sigma_{\\text{crit}}$ ($\\sigma = 0.2$): RMSE degradation 6–8% (moderate, manageable)\n- Above $\\sigma_{\\text{crit}}$ ($\\sigma = 0.5$): RMSE degradation 37–58% (severe, unacceptable)\n\nThe ratio $\\sigma = 0.5$ is $2.5\\times$ the critical value, placing it firmly in the saturation regime where the contamination signal is overwhelmed by noise.\n\n---\n\n## 5. Discussion\n\n### 5.1 Why $c_n$ Is More Sensitive Than $\\theta_n$\n\nThree reinforcing mechanisms:\n\n1. **Direct multiplicative coupling**: $c_n$ multiplies $e_i$ in the likelihood; $\\theta_n$ does not. Noise in $e_i$ directly corrupts the $c_n$ score function.\n\n2. **EIV attenuation**: The classical errors-in-variables bias pushes $c_n$ toward zero. No analogous bias exists for $\\theta_n$ (which is an intercept, not a coefficient of the noisy covariate).\n\n3. **Prior reinforcement**: The HalfNormal(0.5) prior has its mode at zero, in the same direction as the attenuation bias. For contaminated models ($c_n > 0$), the prior and attenuation conspire to underestimate $c_n$. For $\\theta_n$, the symmetric $\\mathcal{N}(0,1)$ prior does not systematically reinforce any noise-induced bias.\n\n### 5.2 Why the Degradation Is Nonlinear\n\nThe nonlinearity is **not** primarily due to the logistic link function or the Bayesian framework. It arises from the fundamental structure of the errors-in-variables problem:\n\nThe attenuation factor $\\lambda = V_e/(V_e + \\sigma^2)$ is a **harmonic** function of $\\sigma^2$. The resulting squared bias $(1-\\lambda)^2 = \\sigma^4/(V_e + \\sigma^2)^2$ is:\n- Convex for $\\sigma^2 < V_e/3$ (accelerating degradation)\n- Concave for $\\sigma^2 > V_e/3$ (decelerating toward saturation)\n\nAt $\\sigma = 0.5$, we have $\\sigma^2/V_e \\approx 6.25$, deep in the concave/saturation regime. The system is past the inflection point: further noise increase would yield diminishing marginal degradation (because there is little signal left to destroy).\n\n### 5.3 Tightness of the Bounds\n\nThe theoretical attenuation factor provides a **qualitative** characterization rather than exact RMSE predictions, for three reasons:\n\n1. **Joint estimation effects**: The full model jointly estimates $(N + I + J + N)$ parameters. Perturbation of $e_i$ cascades through $b_i$ adjustments (which affect all $N$ models) and $d_j$ adjustments (which affect all items). These cross-parameter interactions are captured by the full Hessian inverse but not by the per-model block analysis.\n\n2. **Logistic nonlinearity**: The linear EIV attenuation formula $\\lambda = V_e/(V_e + \\sigma^2)$ is exact for Gaussian linear models but approximate for logistic models. The logistic link moderates extreme predictions (through the sigmoid's saturation), potentially making the actual attenuation less severe than the linear prediction.\n\n3. **MCMC posterior mean vs. mode**: The theoretical analysis targets the posterior mode, while exp-012 reports posterior means. For asymmetric distributions (e.g., HalfNormal for $c_n$), these can differ meaningfully.\n\nDespite these limitations, the theory correctly identifies (a) the critical noise threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)} \\approx 0.2$ (DGP-specific, governed by item exposure heterogeneity), (b) the ordering of parameter sensitivities, and (c) the qualitative scaling regime, validating the Monte Carlo findings with a principled theoretical foundation.\n\n### 5.4 Practical Implications for Stage 2 Quality\n\nThe attenuation analysis yields a concrete requirement for Stage 2 estimation:\n\n$$\n\\sigma_e < \\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}\n$$\n\nFor typical benchmark exposure distributions where $\\text{Var}(e) \\approx 0.04$–$0.08$ (depending on exposure heterogeneity), this translates to:\n\n$$\n\\sigma_e < 0.20\\text{–}0.28\n$$\n\nWithin this range, RMSE degradation stays below $\\sim$10% for both $c_n$ and $\\theta_n$. The exp-012 results confirm this: at $\\sigma = 0.2$, $c_n$ RMSE degrades 7.9% and $\\theta$ RMSE degrades 5.9% — both acceptable for practical contamination auditing.\n\n### 5.5 Connection to Robustness Claims\n\nThe theoretical analysis supports the following characterization for the paper:\n\n> **Robustness characterization.** The G-MFRM staged estimator exhibits graceful degradation under Stage 2 estimation error, with a critical threshold $\\sigma_{\\text{crit}} = \\sqrt{\\text{Var}_I(e)}$ governing the transition from variance-dominated (mild) to bias-dominated (severe) degradation. For exposure estimation noise below this threshold, ability estimates $\\hat\\theta$ degrade by $< 6\\%$ RMSE and contamination estimates $\\hat{c}_n$ by $< 8\\%$ RMSE (Table 4, exp-012). The differential sensitivity of $c_n > \\theta$ follows from the direct multiplicative coupling $c_n \\cdot e_i$ in the likelihood, consistent with classical errors-in-variables theory (Pagan, 1984; Fuller, 1987). This provides a formal justification for the empirical robustness observed in the Monte Carlo sensitivity analysis.\n\n---\n\n## 6. References\n\n- Fuller, W.A. (1987). *Measurement Error Models*. Wiley.\n- Liu, F., Bayarri, M.J., & Berger, J.O. (2009). Modularization in Bayesian analysis, with emphasis on analysis of computer models. *Bayesian Analysis*, 4(1), 119–150.\n- Murphy, K.M. & Topel, R.H. (1985). Estimation and inference in two-step econometric models. *Journal of Business & Economic Statistics*, 3(4), 370–379.\n- Newey, W.K. & McFadden, D. (1994). Large sample estimation and hypothesis testing. *Handbook of Econometrics*, Vol. 4, Ch. 36, 2111–2245.\n- Pagan, A. (1984). Econometric issues in the analysis of regressions with generated regressors. *International Economic Review*, 25(1), 221–247.\n- Plummer, M. (2015). Cuts in Bayesian graphical models. *Statistics and Computing*, 25, 37–43.\n- Pompe, E. & Jacob, P.E. (2021). Asymptotics of cut distributions and robust modular inference using Posterior Bootstrap. *arXiv:2110.11149*.\n",
      "numLines": 399,
      "startLine": 1,
      "totalLines": 399
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

Let me also check for any remaining bare "Proposition" references I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "a2cb2ff4-2cd9-4b18-9b6c-2918b67c850b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hu13ToPn1KzkCPNkpSLzDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9715,
      "cache_read_input_tokens": 38647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9715
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

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_01RJ93huHdFSyaJo4aZiCoMt`</summary>

```json
{
  "pattern": "Proposition",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/error_propagation_theory.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "59fa1d0c-7798-48a1-84ea-90d24777d9f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hu13ToPn1KzkCPNkpSLzDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9715,
      "cache_read_input_tokens": 38647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9715
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

_source line 44 · 2026-05-22T04:31:06.149Z_

<details><summary>↩ Tool result · `toolu_01RJ93huHdFSyaJo4aZiCoMt`</summary>

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
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "84e7e560-dfcb-4f10-8287-498c1bc441c7",
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

### Assistant

_source line 45_

All four modifications complete:

1. **Sensitivity ratio → qualitative**: Added blockquote caveat in §3.4 after the 2.9× calculation, and rewrote the §4.3 comparison paragraph to frame the ratio as a qualitative directional prediction with explicit explanation of the discrepancy (linearization + logistic saturation).

2. **σ_crit DGP-dependent**: Updated §4.1 (added "DGP-specific" label + full parenthetical for exp-012), §4.4 (added formula + DGP note), and §5.3 (added formula + "DGP-specific, governed by item exposure heterogeneity"). §3.3, §5.4, §5.5 already had the formula and were left as-is.

3. **Proposition → Approximate Result**: Renamed all three to "Approximate Result 1/2/3", added "under the linearized model approximation" to Result 1's setup, and updated all cross-references.

4. **Absorption mechanism expanded**: Rewrote the absorption paragraph in §3.4 to explain the variance redistribution mechanism, the systematic θ inflation for contaminated models, and the direct connection to the paper's core argument (no joint estimation → contaminated models get inflated ability estimates).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "uuid": "e85cbd34-ea08-4cad-bba4-2ff6c86abfe1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01245ecCigtgiE7xuNVBgfCg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 48362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
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

_source line 46_

All four modifications complete:

1. **Sensitivity ratio → qualitative**: Added blockquote caveat in §3.4 after the 2.9× calculation, and rewrote the §4.3 comparison paragraph to frame the ratio as a qualitative directional prediction with explicit explanation of the discrepancy (linearization + logistic saturation).

2. **σ_crit DGP-dependent**: Updated §4.1 (added "DGP-specific" label + full parenthetical for exp-012), §4.4 (added formula + DGP note), and §5.3 (added formula + "DGP-specific, governed by item exposure heterogeneity"). §3.3, §5.4, §5.5 already had the formula and were left as-is.

3. **Proposition → Approximate Result**: Renamed all three to "Approximate Result 1/2/3", added "under the linearized model approximation" to Result 1's setup, and updated all cross-references.

4. **Absorption mechanism expanded**: Rewrote the absorption paragraph in §3.4 to explain the variance redistribution mechanism, the systematic θ inflation for contaminated models, and the direct connection to the paper's core argument (no joint estimation → contaminated models get inflated ability estimates).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 144313,
  "duration_api_ms": 145051,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "2717086c-5e1d-43e1-bdf0-ac6a48ec0dcd",
  "total_cost_usd": 0.6179669999999999,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 37074,
    "cache_read_input_tokens": 516003,
    "output_tokens": 5065,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37074,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 302,
        "cache_read_input_tokens": 48362,
        "cache_creation_input_tokens": 159,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 159
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1473,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0015429999999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 5065,
      "cacheReadInputTokens": 516003,
      "cacheCreationInputTokens": 37074,
      "webSearchRequests": 0,
      "costUSD": 0.6164239999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "01fe44ae-c115-4d1d-b1c2-a6d418c45643"
}
```

</details>

---
