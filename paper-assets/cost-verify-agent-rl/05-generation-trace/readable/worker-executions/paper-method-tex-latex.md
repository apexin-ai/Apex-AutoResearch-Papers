# paper method tex latex

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_method-tex-latex_20260520T131951.log`
- **Structured JSON:** [`a8ca2827a732725cf76e.json`](../../sessions/a8/a8ca2827a732725cf76e.json)

## Before a recorded user message

14 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
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
  "uuid": "0c791d7b-7758-4ed4-a6e7-e8a0da86f2c5",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
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
    "resetsAt": 1779300600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a55c6b31-695a-47b2-8047-09d7601a6ec1",
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper writing norms and finding the method_draft.md file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "211ebdb4-8b1d-4588-b544-d92f9e476752",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155rgQJgacwRdhRDBTymiG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12519,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12519
      },
      "output_tokens": 44,
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

<details open><summary>🔧 Tool call — Read · `toolu_019e96S6VPL5uzndJS4GCU1H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "3e7b27fe-3d55-4248-a4b1-d9aa73b5d3d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155rgQJgacwRdhRDBTymiG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12519,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12519
      },
      "output_tokens": 44,
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

_source line 6 · 2026-05-20T13:20:02.301Z_

<details><summary>↩ Tool result · `toolu_019e96S6VPL5uzndJS4GCU1H`</summary>

```text
1	# 3. Method
2	
3	## 3.1 Problem Formulation
4	
5	### Interactive Agent as POMDP
6	
7	We formalize the interactive agent task as a Partially Observable Markov Decision Process (POMDP) $\mathcal{M} = \langle \mathcal{S}, \mathcal{A}, \mathcal{O}, T, O, R, \gamma \rangle$, where $\mathcal{S}$ is the state space of the environment (e.g., object locations and states in a household), $\mathcal{A}$ is the action space (e.g., natural language commands such as `go to shelf 1`, `take mug 2`), $\mathcal{O}$ is the observation space (textual descriptions of the environment), $T: \mathcal{S} \times \mathcal{A} \rightarrow \Delta(\mathcal{S})$ is the transition function, $O: \mathcal{S} \rightarrow \Delta(\mathcal{O})$ is the observation function, $R: \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$ is the reward function, and $\gamma$ is the discount factor.
8	
9	At each timestep $t$, the agent receives observation $o_t \in \mathcal{O}$ and selects action $a_t \in \mathcal{A}$ according to its policy $\pi_\phi(a_t \mid h_t)$, where $h_t = (o_1, a_1, \ldots, o_t)$ is the interaction history. The episode terminates upon task completion (success) or after a maximum number of steps $T_{\max}$.
10	
11	### Verification Decision
12	
13	At each step $t$, in addition to the primary action $a_t$, the agent makes a binary verification decision:
14	$$d_t \in \{0, 1\}$$
15	where $d_t = 1$ triggers a self-verification subroutine and $d_t = 0$ skips verification. When $d_t = 1$, the agent re-examines its current observation and proposed action, potentially revising $a_t$ to an alternative $a_t'$.
16	
17	We parameterize the verification policy as $\pi_\theta(d_t \mid s_t)$, where $s_t$ is a compact representation of the agent's state at step $t$ (including the current observation, proposed action, and task context). In practice, $\pi_\theta$ is realized by augmenting the agent's action space with a special control token $\langle\text{VERIFY}\rangle$ that precedes the action output, such that the language model generates either $\langle\text{VERIFY}\rangle\, a_t$ or $\langle\text{SKIP}\rangle\, a_t$ at each step.
18	
19	### Action-Change Signal
20	
21	We define the **action-change indicator** as the primary signal for verification informativeness:
22	$$\Delta a_t = \mathbb{1}\left[a_t^{\text{post}} \neq a_t^{\text{pre}}\right]$$
23	where $a_t^{\text{pre}}$ is the action the agent would have taken without verification (obtained via a single greedy decode pass), and $a_t^{\text{post}}$ is the action after the verification subroutine. Equality is assessed via semantic canonicalization (e.g., mapping actions to $\langle \text{verb}, \text{object}, \text{receptacle} \rangle$ tuples in ALFWorld) to avoid spurious mismatches from surface-form variation.
24	
25	The key insight is that **most self-verification is confirmatory rather than corrective** \cite{self-verification-dilemma-2026}. When $\Delta a_t = 0$, the verification consumed compute without altering behavior---it was uninformative. When $\Delta a_t = 1$, the verification produced a behavioral change, indicating it carried decision-relevant information.
26	
27	### Verification Cost Model
28	
29	Each verification incurs a fixed cost $c_{\text{verify}}$ (proportional to the additional inference tokens required). The total verification cost for an episode of length $T$ is:
30	$$C_{\text{total}} = \sum_{t=1}^{T} d_t \cdot c_{\text{verify}}$$
31	
32	In practice, $c_{\text{verify}}$ corresponds to the additional forward pass needed for the verification subroutine (re-observation, re-reasoning, and potential action revision), which approximately doubles the per-step inference cost.
33	
34	&lt;!-- [中文注释] Director 决策点：c_verify 是固定常数还是与 step 相关的变量？当前设定为固定值，但如果 verification 长度变化大可能需要 token-level cost -->
35	
36	### Objective
37	
38	The goal of B-IAVR is to learn a verification policy $\pi_\theta$ that maximizes task success while minimizing verification cost. We formulate this as a constrained optimization problem:
39	$$\max_\theta \; \mathbb{E}_{\pi_\theta, \pi_\phi}\left[\sum_{t=1}^{T} R(s_t, a_t)\right] \quad \text{s.t.} \quad \mathbb{E}_{\pi_\theta}\left[C_{\text{total}}\right] \leq C_{\text{budget}}$$
40	
41	where $C_{\text{budget}}$ is the verification budget constraint. In practice, we relax this to an unconstrained objective via Lagrangian relaxation (Section 3.2).
42	
43	
44	## 3.2 B-IAVR: Selective Self-Verification via RL
45	
46	### Overview
47	
48	B-IAVR (**B**inary **I**nformative **A**ction **V**erification via **R**L) trains a language model agent to decide *when* to invoke self-verification, using action change as a reward signal for verification informativeness. The method consists of three components: (1) a selective verification policy that makes per-step binary verify/skip decisions, (2) a composite reward function combining task success, verification informativeness, and cost, and (3) an RL training procedure based on GRPO with optional GiGPO extension for step-level credit assignment.
49	
50	### Selective Verification Policy
51	
52	The agent's generation at each step $t$ is structured as:
53	$$\pi(d_t, a_t \mid h_t) = \pi_\theta(d_t \mid h_t) \cdot \pi_\phi(a_t \mid h_t, d_t)$$
54	
55	When the model generates $\langle\text{VERIFY}\rangle$, a verification subroutine is triggered:
56	1. The agent produces a preliminary action $a_t^{\text{pre}}$ via greedy decoding from the current state.
57	2. The verification module re-examines the observation $o_t$, the proposed action $a_t^{\text{pre}}$, and the task goal $g$, generating a verification rationale.
58	3. Based on the rationale, the agent either confirms $a_t^{\text{pre}}$ or revises it to $a_t^{\text{post}}$.
59	
60	When $\langle\text{SKIP}\rangle$ is generated, $a_t^{\text{pre}}$ is directly executed without verification.
61	
62	In practice, $\pi_\theta$ and $\pi_\phi$ share the same language model backbone, with the verification decision encoded as a special token prefix. This avoids the overhead of maintaining separate models and allows end-to-end RL training.
63	
64	&lt;!-- [中文注释] Director 决策点：verification subroutine 的具体 prompt 设计需要确认——是 re-observe environment 还是 re-reason on existing observation？当前写为 re-examine observation，但如果 re-observe 有不同 cost implications -->
65	
66	### Reward Design
67	
68	The reward function combines three components to balance task performance, verification quality, and cost:
69	
70	**Task success reward.** A binary episode-level reward indicating whether the task was completed:
71	$$r_{\text{task}} = \begin{cases} r_+ & \text{if task completed successfully} \\ 0 & \text{otherwise} \end{cases}$$
72	
73	**Action-change reward.** A step-level reward given when verification produces a behavioral change, serving as a proxy for verification informativeness:
74	$$r_{\text{ac}, t} = \alpha \cdot d_t \cdot \Delta a_t$$
75	where $\alpha > 0$ controls the magnitude of the informativeness bonus. This reward is only assigned at steps where verification is triggered ($d_t = 1$) and the action changes ($\Delta a_t = 1$).
76	
77	**Verification cost penalty.** A step-level penalty for each verification invocation:
78	$$r_{\text{cost}, t} = -\gamma_c \cdot d_t$$
79	where $\gamma_c > 0$ is the per-verification cost coefficient.
80	
81	The **combined reward** for an episode is:
82	$$R = r_{\text{task}} + \sum_{t=1}^{T}\left(\beta \cdot r_{\text{ac}, t} + r_{\text{cost}, t}\right)$$
83	$$= r_{\text{task}} + \sum_{t=1}^{T} d_t \left(\beta \cdot \alpha \cdot \Delta a_t - \gamma_c\right)$$
84	
85	where $\beta$ balances the informativeness bonus against the cost penalty. The cost coefficient $\gamma_c$ is updated via dual gradient ascent to enforce the budget constraint:
86	$$\gamma_c \leftarrow \gamma_c + \eta_\gamma \left(\mathbb{E}[C_{\text{total}}] - C_{\text{budget}}\right)$$
87	
88	This Lagrangian formulation allows the agent to learn a cost-performance tradeoff without hand-tuning $\gamma_c$.
89	
90	&lt;!-- [中文注释] Director 决策点：α 和 β 的关系是否冗余？当前公式 β·α·Δa_t 可以简化为单一系数。保留两个是为了区分 action-change signal 的 base magnitude (α) 和 informativeness-vs-task 的 tradeoff (β)。如果觉得过度参数化，可以合并 -->
91	
92	**Interaction between action-change reward and task success.** Note that $r_{\text{ac}}$ is not gated on task success. A verification that changes the action is informative regardless of episode outcome---even in failed episodes, action changes driven by verification reveal that the agent's initial action was uncertain, providing useful training signal. This design choice avoids the bootstrap problem encountered with success-gated rewards when base success rates are low [TBD: cite exp013f gaming / D012-D013 analysis].
93	
94	### Training with GRPO
95	
96	We train $\pi_\theta$ using Group Relative Policy Optimization (GRPO) \cite{shao2024deepseekmath}, which estimates advantages from groups of rollouts without requiring a learned value function.
97	
98	For each training step, we sample $G$ groups of $K$ rollouts per task instance. Within each group $g$, the advantage of rollout $k$ is computed as:
99	$$\hat{A}^{(g)}_k = \frac{R^{(g)}_k - \text{mean}(\{R^{(g)}_j\}_{j=1}^K)}{\text{std}(\{R^{(g)}_j\}_{j=1}^K) + \epsilon}$$
100	
101	The GRPO objective with KL regularization is:
102	$$\mathcal{L}_{\text{GRPO}}(\theta) = -\mathbb{E}_{g,k}\left[\min\left(\rho_t \hat{A}^{(g)}_k, \; \text{clip}(\rho_t, 1-\varepsilon, 1+\varepsilon) \hat{A}^{(g)}_k\right)\right] + \lambda_{\text{KL}} \, D_{\text{KL}}(\pi_\theta \| \pi_{\text{ref}})$$
103	
104	where $\rho_t = \frac{\pi_\theta(a_t | h_t)}{\pi_{\text{ref}}(a_t | h_t)}$ is the importance ratio and $\pi_{\text{ref}}$ is the reference policy (initialized from the SFT checkpoint).
105	
106	**Step-independent context.** Following the rollout design of verl-agent \cite{selfguide2026}, we employ step-independent context for multi-turn rollouts: at each step, the model receives only the current observation and task context rather than the full interaction history. This prevents context length explosion in long-horizon tasks and maintains consistent inference quality across steps---a critical factor for training stability in interactive agent settings.
107	
108	&lt;!-- [中文注释] Director 决策点：step-independent context 是否需要更详细的描述？这实际上是 exp026 成功的关键技术因素（vs RAGEN full-history 三次 entropy collapse），但如果论文 framing 不强调框架差异可以简写 -->
109	
110	### Extension: GiGPO for Step-Level Credit Assignment
111	
112	[TBD: GiGPO details]
113	
114	A known limitation of episode-level GRPO is that the advantage $\hat{A}^{(g)}_k$ is shared across all steps within a rollout, providing no step-level credit assignment. In multi-turn agent tasks where episodes span 10--30 steps, this leads to high variance and slow learning---a single failed step can assign negative advantage to all preceding correct actions.
115	
116	GiGPO (Group-in-Group Policy Optimization) \cite{feng2025gigpo} addresses this via a nested group structure. For each step $t$ within a rollout, GiGPO constructs a *step-level group* by comparing the outcomes of rollouts that share the same prefix up to step $t-1$ but diverge at step $t$:
117	$$\hat{A}^{\text{step}}_t = \frac{R_t^{>} - \text{mean}(\{R^{>}_j\})}{\text{std}(\{R^{>}_j\}) + \epsilon}$$
118	where $R_t^{>}$ denotes the cumulative reward from step $t$ onward. This provides dense, step-level learning signal without requiring a learned critic.
119	
120	In the B-IAVR context, GiGPO is particularly well-suited because:
121	
122	1. **Verification decisions are step-level.** The verify/skip decision at step $t$ has localized impact---GiGPO can attribute the outcome change to the specific verification decision rather than spreading credit across the entire episode.
123	2. **Action-change reward is already step-level.** The reward $r_{\text{ac},t}$ naturally aligns with GiGPO's step-level advantage structure, providing dense reward signal at the granularity where credit assignment operates.
124	3. **Sparse task reward benefits from decomposition.** When the episode-level task reward $r_{\text{task}}$ is binary and sparse, GiGPO's step-level groups break the learning signal into denser components, mitigating the cold-start problem observed with pure GRPO on sparse rewards.
125	
126	[TBD: exp result --- GiGPO vs GRPO training curves, convergence speed comparison]
127	
128	### Self-Guide Integration
129	
130	B-IAVR builds upon the Self-Guide framework \cite{selfguide2026}, which co-evolves a task policy and an internal reward model through iterative RL training. Specifically, Self-Guide trains a policy $\pi_\phi$ alongside an internal evaluator $V_\psi$ that scores intermediate states, providing denser reward signal than the sparse environment reward alone.
131	
132	We extend Self-Guide by introducing the verification decision layer: the internal evaluator $V_\psi(s_t)$ serves as an additional input feature to the verification policy $\pi_\theta(d_t \mid s_t, V_\psi(s_t))$. Intuitively, when the internal evaluator assigns low confidence to the current state (indicating the agent is uncertain about its action), verification is more likely to be informative. This creates a natural trigger mechanism:
133	
134	$$P(d_t = 1) \uparrow \quad \text{when} \quad V_\psi(s_t) \text{ is low (uncertain)}$$
135	
136	The co-evolution property of Self-Guide ensures that as the task policy improves, the internal evaluator also calibrates, leading to a progressively refined verification trigger that adapts to the agent's evolving competence.
137	
138	[TBD: exp result --- Self-Guide internal reward correlation with action-change frequency]
139	
140	&lt;!-- [中文注释] Director 决策点：Self-Guide integration 的描述深度——当前写了 V_ψ 作为 verification trigger 的机制，但实际实现可能更简单（直接用 token logits confidence 而非独立 V_ψ）。需要确认最终实现方案后 revise -->
141	
142	
143	## 3.3 Comparison with Related Methods
144	
145	We position B-IAVR against three categories of related methods: adaptive reasoning effort, selective verification, and self-correction in agents.
146	
147	### vs ARES: Adaptive Reasoning Effort Selection
148	
149	ARES \cite{yang2026ares} trains an SFT-initialized router to allocate continuous reasoning effort per step, optimized via GRPO with a combined outcome and token-efficiency reward. B-IAVR differs in three fundamental aspects:
150	
151	| Dimension | ARES | B-IAVR (Ours) |
152	|-----------|------|----------------|
153	| **Decision type** | Continuous effort level | Binary verify/skip |
154	| **Training signal** | Pre-defined quality metrics + token efficiency | Action change (behavioral) |
155	| **Data requirement** | Difficulty-annotated data for SFT bootstrap | Environment interaction only |
156	| **Scope** | General reasoning tasks | Interactive agent tasks |
157	
158	The binary decision in B-IAVR offers two advantages: (1) it is more interpretable---one can directly audit *which steps* were verified and *whether* the verification changed behavior, and (2) it avoids the need for difficulty annotations, as the action-change signal is self-supervised from the agent's own behavioral variation.
159	
160	Conversely, ARES's continuous allocation is more flexible for tasks where "partial verification" makes sense. B-IAVR's binary design is motivated by the interactive agent setting, where verification is a discrete subroutine (re-observe environment, re-reason, potentially revise) that is either invoked or not.
161	
162	### vs Thinkless: Learning When to Think
163	
164	Thinkless \cite{du2025thinkless} uses RL to train a control token that decides whether to invoke extended thinking (chain-of-thought) before answering. While methodologically parallel to B-IAVR (both learn a binary computation trigger via RL), they address different settings:
165	
166	- **Single-turn vs multi-turn.** Thinkless operates on single-turn QA; B-IAVR on multi-step interactive agent trajectories where each decision depends on environment feedback.
167	- **Computation type.** Thinkless controls *internal reasoning* (thinking tokens); B-IAVR controls *external verification* (re-observation of the environment), grounding the signal in behavioral change rather than token-level computation.
168	- **Reward signal.** Thinkless uses task correctness; B-IAVR introduces the action-change signal as a verification-specific informativeness measure.
169	
170	### vs Derailer-Rerailer: Adaptive Verification for Reasoning
171	
172	Derailer-Rerailer \cite{wan2025derailer-rerailer} uses a heuristic instability signal to detect "derailed" reasoning steps and trigger correction. Compared to B-IAVR:
173	
174	- **Heuristic vs learned.** Derailer-Rerailer relies on hand-designed instability metrics; B-IAVR learns the verification trigger end-to-end via RL. This eliminates the need for task-specific heuristic engineering and allows the trigger to adapt as the policy improves.
175	- **Reasoning chains vs agent trajectories.** Derailer-Rerailer operates on single-turn reasoning chains; B-IAVR on multi-turn agent trajectories with environment interaction. The environment provides a concrete grounding signal (observation changes) absent in pure reasoning settings.
176	- **Correction scope.** Derailer-Rerailer re-generates from the derailed step; B-IAVR's verification may confirm or revise a single action, preserving the trajectory structure.
177	
178	### vs Sherlock: Reliable Agentic Workflow Execution
179	
180	Sherlock \cite{sherlock2025} applies selective verification to agentic *workflows* (DAG-structured task plans) using offline counterfactual analysis and speculative execution. The key distinction is the level of abstraction: Sherlock verifies workflow nodes (coarse-grained, offline planning); B-IAVR verifies individual agent actions (fine-grained, online decision-making). The two approaches are complementary---Sherlock could serve as a workflow-level planner while B-IAVR handles step-level verification within each workflow node.
181	
182	[TBD: exp result --- ablation table comparing B-IAVR with always-on / no-verify / random-$p$ / confidence-threshold baselines]
183	
184	&lt;!-- [中文注释] Director 决策点：3.3 节的对比深度是否合适？当前对 ARES 最详细（主要竞争者），Thinkless/Derailer-Rerailer/Sherlock 较简洁。如果 page budget 紧张，Sherlock 段可以移到 Related Work -->
185	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "9dfc4db8-15b7-4fb7-a9e2-f2f12d8256ea",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method_draft.md",
      "content": "# 3. Method\n\n## 3.1 Problem Formulation\n\n### Interactive Agent as POMDP\n\nWe formalize the interactive agent task as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = \\langle \\mathcal{S}, \\mathcal{A}, \\mathcal{O}, T, O, R, \\gamma \\rangle$, where $\\mathcal{S}$ is the state space of the environment (e.g., object locations and states in a household), $\\mathcal{A}$ is the action space (e.g., natural language commands such as `go to shelf 1`, `take mug 2`), $\\mathcal{O}$ is the observation space (textual descriptions of the environment), $T: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\Delta(\\mathcal{S})$ is the transition function, $O: \\mathcal{S} \\rightarrow \\Delta(\\mathcal{O})$ is the observation function, $R: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathbb{R}$ is the reward function, and $\\gamma$ is the discount factor.\n\nAt each timestep $t$, the agent receives observation $o_t \\in \\mathcal{O}$ and selects action $a_t \\in \\mathcal{A}$ according to its policy $\\pi_\\phi(a_t \\mid h_t)$, where $h_t = (o_1, a_1, \\ldots, o_t)$ is the interaction history. The episode terminates upon task completion (success) or after a maximum number of steps $T_{\\max}$.\n\n### Verification Decision\n\nAt each step $t$, in addition to the primary action $a_t$, the agent makes a binary verification decision:\n$$d_t \\in \\{0, 1\\}$$\nwhere $d_t = 1$ triggers a self-verification subroutine and $d_t = 0$ skips verification. When $d_t = 1$, the agent re-examines its current observation and proposed action, potentially revising $a_t$ to an alternative $a_t'$.\n\nWe parameterize the verification policy as $\\pi_\\theta(d_t \\mid s_t)$, where $s_t$ is a compact representation of the agent's state at step $t$ (including the current observation, proposed action, and task context). In practice, $\\pi_\\theta$ is realized by augmenting the agent's action space with a special control token $\\langle\\text{VERIFY}\\rangle$ that precedes the action output, such that the language model generates either $\\langle\\text{VERIFY}\\rangle\\, a_t$ or $\\langle\\text{SKIP}\\rangle\\, a_t$ at each step.\n\n### Action-Change Signal\n\nWe define the **action-change indicator** as the primary signal for verification informativeness:\n$$\\Delta a_t = \\mathbb{1}\\left[a_t^{\\text{post}} \\neq a_t^{\\text{pre}}\\right]$$\nwhere $a_t^{\\text{pre}}$ is the action the agent would have taken without verification (obtained via a single greedy decode pass), and $a_t^{\\text{post}}$ is the action after the verification subroutine. Equality is assessed via semantic canonicalization (e.g., mapping actions to $\\langle \\text{verb}, \\text{object}, \\text{receptacle} \\rangle$ tuples in ALFWorld) to avoid spurious mismatches from surface-form variation.\n\nThe key insight is that **most self-verification is confirmatory rather than corrective** \\cite{self-verification-dilemma-2026}. When $\\Delta a_t = 0$, the verification consumed compute without altering behavior---it was uninformative. When $\\Delta a_t = 1$, the verification produced a behavioral change, indicating it carried decision-relevant information.\n\n### Verification Cost Model\n\nEach verification incurs a fixed cost $c_{\\text{verify}}$ (proportional to the additional inference tokens required). The total verification cost for an episode of length $T$ is:\n$$C_{\\text{total}} = \\sum_{t=1}^{T} d_t \\cdot c_{\\text{verify}}$$\n\nIn practice, $c_{\\text{verify}}$ corresponds to the additional forward pass needed for the verification subroutine (re-observation, re-reasoning, and potential action revision), which approximately doubles the per-step inference cost.\n\n&lt;!-- [中文注释] Director 决策点：c_verify 是固定常数还是与 step 相关的变量？当前设定为固定值，但如果 verification 长度变化大可能需要 token-level cost -->\n\n### Objective\n\nThe goal of B-IAVR is to learn a verification policy $\\pi_\\theta$ that maximizes task success while minimizing verification cost. We formulate this as a constrained optimization problem:\n$$\\max_\\theta \\; \\mathbb{E}_{\\pi_\\theta, \\pi_\\phi}\\left[\\sum_{t=1}^{T} R(s_t, a_t)\\right] \\quad \\text{s.t.} \\quad \\mathbb{E}_{\\pi_\\theta}\\left[C_{\\text{total}}\\right] \\leq C_{\\text{budget}}$$\n\nwhere $C_{\\text{budget}}$ is the verification budget constraint. In practice, we relax this to an unconstrained objective via Lagrangian relaxation (Section 3.2).\n\n\n## 3.2 B-IAVR: Selective Self-Verification via RL\n\n### Overview\n\nB-IAVR (**B**inary **I**nformative **A**ction **V**erification via **R**L) trains a language model agent to decide *when* to invoke self-verification, using action change as a reward signal for verification informativeness. The method consists of three components: (1) a selective verification policy that makes per-step binary verify/skip decisions, (2) a composite reward function combining task success, verification informativeness, and cost, and (3) an RL training procedure based on GRPO with optional GiGPO extension for step-level credit assignment.\n\n### Selective Verification Policy\n\nThe agent's generation at each step $t$ is structured as:\n$$\\pi(d_t, a_t \\mid h_t) = \\pi_\\theta(d_t \\mid h_t) \\cdot \\pi_\\phi(a_t \\mid h_t, d_t)$$\n\nWhen the model generates $\\langle\\text{VERIFY}\\rangle$, a verification subroutine is triggered:\n1. The agent produces a preliminary action $a_t^{\\text{pre}}$ via greedy decoding from the current state.\n2. The verification module re-examines the observation $o_t$, the proposed action $a_t^{\\text{pre}}$, and the task goal $g$, generating a verification rationale.\n3. Based on the rationale, the agent either confirms $a_t^{\\text{pre}}$ or revises it to $a_t^{\\text{post}}$.\n\nWhen $\\langle\\text{SKIP}\\rangle$ is generated, $a_t^{\\text{pre}}$ is directly executed without verification.\n\nIn practice, $\\pi_\\theta$ and $\\pi_\\phi$ share the same language model backbone, with the verification decision encoded as a special token prefix. This avoids the overhead of maintaining separate models and allows end-to-end RL training.\n\n&lt;!-- [中文注释] Director 决策点：verification subroutine 的具体 prompt 设计需要确认——是 re-observe environment 还是 re-reason on existing observation？当前写为 re-examine observation，但如果 re-observe 有不同 cost implications -->\n\n### Reward Design\n\nThe reward function combines three components to balance task performance, verification quality, and cost:\n\n**Task success reward.** A binary episode-level reward indicating whether the task was completed:\n$$r_{\\text{task}} = \\begin{cases} r_+ & \\text{if task completed successfully} \\\\ 0 & \\text{otherwise} \\end{cases}$$\n\n**Action-change reward.** A step-level reward given when verification produces a behavioral change, serving as a proxy for verification informativeness:\n$$r_{\\text{ac}, t} = \\alpha \\cdot d_t \\cdot \\Delta a_t$$\nwhere $\\alpha > 0$ controls the magnitude of the informativeness bonus. This reward is only assigned at steps where verification is triggered ($d_t = 1$) and the action changes ($\\Delta a_t = 1$).\n\n**Verification cost penalty.** A step-level penalty for each verification invocation:\n$$r_{\\text{cost}, t} = -\\gamma_c \\cdot d_t$$\nwhere $\\gamma_c > 0$ is the per-verification cost coefficient.\n\nThe **combined reward** for an episode is:\n$$R = r_{\\text{task}} + \\sum_{t=1}^{T}\\left(\\beta \\cdot r_{\\text{ac}, t} + r_{\\text{cost}, t}\\right)$$\n$$= r_{\\text{task}} + \\sum_{t=1}^{T} d_t \\left(\\beta \\cdot \\alpha \\cdot \\Delta a_t - \\gamma_c\\right)$$\n\nwhere $\\beta$ balances the informativeness bonus against the cost penalty. The cost coefficient $\\gamma_c$ is updated via dual gradient ascent to enforce the budget constraint:\n$$\\gamma_c \\leftarrow \\gamma_c + \\eta_\\gamma \\left(\\mathbb{E}[C_{\\text{total}}] - C_{\\text{budget}}\\right)$$\n\nThis Lagrangian formulation allows the agent to learn a cost-performance tradeoff without hand-tuning $\\gamma_c$.\n\n&lt;!-- [中文注释] Director 决策点：α 和 β 的关系是否冗余？当前公式 β·α·Δa_t 可以简化为单一系数。保留两个是为了区分 action-change signal 的 base magnitude (α) 和 informativeness-vs-task 的 tradeoff (β)。如果觉得过度参数化，可以合并 -->\n\n**Interaction between action-change reward and task success.** Note that $r_{\\text{ac}}$ is not gated on task success. A verification that changes the action is informative regardless of episode outcome---even in failed episodes, action changes driven by verification reveal that the agent's initial action was uncertain, providing useful training signal. This design choice avoids the bootstrap problem encountered with success-gated rewards when base success rates are low [TBD: cite exp013f gaming / D012-D013 analysis].\n\n### Training with GRPO\n\nWe train $\\pi_\\theta$ using Group Relative Policy Optimization (GRPO) \\cite{shao2024deepseekmath}, which estimates advantages from groups of rollouts without requiring a learned value function.\n\nFor each training step, we sample $G$ groups of $K$ rollouts per task instance. Within each group $g$, the advantage of rollout $k$ is computed as:\n$$\\hat{A}^{(g)}_k = \\frac{R^{(g)}_k - \\text{mean}(\\{R^{(g)}_j\\}_{j=1}^K)}{\\text{std}(\\{R^{(g)}_j\\}_{j=1}^K) + \\epsilon}$$\n\nThe GRPO objective with KL regularization is:\n$$\\mathcal{L}_{\\text{GRPO}}(\\theta) = -\\mathbb{E}_{g,k}\\left[\\min\\left(\\rho_t \\hat{A}^{(g)}_k, \\; \\text{clip}(\\rho_t, 1-\\varepsilon, 1+\\varepsilon) \\hat{A}^{(g)}_k\\right)\\right] + \\lambda_{\\text{KL}} \\, D_{\\text{KL}}(\\pi_\\theta \\| \\pi_{\\text{ref}})$$\n\nwhere $\\rho_t = \\frac{\\pi_\\theta(a_t | h_t)}{\\pi_{\\text{ref}}(a_t | h_t)}$ is the importance ratio and $\\pi_{\\text{ref}}$ is the reference policy (initialized from the SFT checkpoint).\n\n**Step-independent context.** Following the rollout design of verl-agent \\cite{selfguide2026}, we employ step-independent context for multi-turn rollouts: at each step, the model receives only the current observation and task context rather than the full interaction history. This prevents context length explosion in long-horizon tasks and maintains consistent inference quality across steps---a critical factor for training stability in interactive agent settings.\n\n&lt;!-- [中文注释] Director 决策点：step-independent context 是否需要更详细的描述？这实际上是 exp026 成功的关键技术因素（vs RAGEN full-history 三次 entropy collapse），但如果论文 framing 不强调框架差异可以简写 -->\n\n### Extension: GiGPO for Step-Level Credit Assignment\n\n[TBD: GiGPO details]\n\nA known limitation of episode-level GRPO is that the advantage $\\hat{A}^{(g)}_k$ is shared across all steps within a rollout, providing no step-level credit assignment. In multi-turn agent tasks where episodes span 10--30 steps, this leads to high variance and slow learning---a single failed step can assign negative advantage to all preceding correct actions.\n\nGiGPO (Group-in-Group Policy Optimization) \\cite{feng2025gigpo} addresses this via a nested group structure. For each step $t$ within a rollout, GiGPO constructs a *step-level group* by comparing the outcomes of rollouts that share the same prefix up to step $t-1$ but diverge at step $t$:\n$$\\hat{A}^{\\text{step}}_t = \\frac{R_t^{>} - \\text{mean}(\\{R^{>}_j\\})}{\\text{std}(\\{R^{>}_j\\}) + \\epsilon}$$\nwhere $R_t^{>}$ denotes the cumulative reward from step $t$ onward. This provides dense, step-level learning signal without requiring a learned critic.\n\nIn the B-IAVR context, GiGPO is particularly well-suited because:\n\n1. **Verification decisions are step-level.** The verify/skip decision at step $t$ has localized impact---GiGPO can attribute the outcome change to the specific verification decision rather than spreading credit across the entire episode.\n2. **Action-change reward is already step-level.** The reward $r_{\\text{ac},t}$ naturally aligns with GiGPO's step-level advantage structure, providing dense reward signal at the granularity where credit assignment operates.\n3. **Sparse task reward benefits from decomposition.** When the episode-level task reward $r_{\\text{task}}$ is binary and sparse, GiGPO's step-level groups break the learning signal into denser components, mitigating the cold-start problem observed with pure GRPO on sparse rewards.\n\n[TBD: exp result --- GiGPO vs GRPO training curves, convergence speed comparison]\n\n### Self-Guide Integration\n\nB-IAVR builds upon the Self-Guide framework \\cite{selfguide2026}, which co-evolves a task policy and an internal reward model through iterative RL training. Specifically, Self-Guide trains a policy $\\pi_\\phi$ alongside an internal evaluator $V_\\psi$ that scores intermediate states, providing denser reward signal than the sparse environment reward alone.\n\nWe extend Self-Guide by introducing the verification decision layer: the internal evaluator $V_\\psi(s_t)$ serves as an additional input feature to the verification policy $\\pi_\\theta(d_t \\mid s_t, V_\\psi(s_t))$. Intuitively, when the internal evaluator assigns low confidence to the current state (indicating the agent is uncertain about its action), verification is more likely to be informative. This creates a natural trigger mechanism:\n\n$$P(d_t = 1) \\uparrow \\quad \\text{when} \\quad V_\\psi(s_t) \\text{ is low (uncertain)}$$\n\nThe co-evolution property of Self-Guide ensures that as the task policy improves, the internal evaluator also calibrates, leading to a progressively refined verification trigger that adapts to the agent's evolving competence.\n\n[TBD: exp result --- Self-Guide internal reward correlation with action-change frequency]\n\n&lt;!-- [中文注释] Director 决策点：Self-Guide integration 的描述深度——当前写了 V_ψ 作为 verification trigger 的机制，但实际实现可能更简单（直接用 token logits confidence 而非独立 V_ψ）。需要确认最终实现方案后 revise -->\n\n\n## 3.3 Comparison with Related Methods\n\nWe position B-IAVR against three categories of related methods: adaptive reasoning effort, selective verification, and self-correction in agents.\n\n### vs ARES: Adaptive Reasoning Effort Selection\n\nARES \\cite{yang2026ares} trains an SFT-initialized router to allocate continuous reasoning effort per step, optimized via GRPO with a combined outcome and token-efficiency reward. B-IAVR differs in three fundamental aspects:\n\n| Dimension | ARES | B-IAVR (Ours) |\n|-----------|------|----------------|\n| **Decision type** | Continuous effort level | Binary verify/skip |\n| **Training signal** | Pre-defined quality metrics + token efficiency | Action change (behavioral) |\n| **Data requirement** | Difficulty-annotated data for SFT bootstrap | Environment interaction only |\n| **Scope** | General reasoning tasks | Interactive agent tasks |\n\nThe binary decision in B-IAVR offers two advantages: (1) it is more interpretable---one can directly audit *which steps* were verified and *whether* the verification changed behavior, and (2) it avoids the need for difficulty annotations, as the action-change signal is self-supervised from the agent's own behavioral variation.\n\nConversely, ARES's continuous allocation is more flexible for tasks where \"partial verification\" makes sense. B-IAVR's binary design is motivated by the interactive agent setting, where verification is a discrete subroutine (re-observe environment, re-reason, potentially revise) that is either invoked or not.\n\n### vs Thinkless: Learning When to Think\n\nThinkless \\cite{du2025thinkless} uses RL to train a control token that decides whether to invoke extended thinking (chain-of-thought) before answering. While methodologically parallel to B-IAVR (both learn a binary computation trigger via RL), they address different settings:\n\n- **Single-turn vs multi-turn.** Thinkless operates on single-turn QA; B-IAVR on multi-step interactive agent trajectories where each decision depends on environment feedback.\n- **Computation type.** Thinkless controls *internal reasoning* (thinking tokens); B-IAVR controls *external verification* (re-observation of the environment), grounding the signal in behavioral change rather than token-level computation.\n- **Reward signal.** Thinkless uses task correctness; B-IAVR introduces the action-change signal as a verification-specific informativeness measure.\n\n### vs Derailer-Rerailer: Adaptive Verification for Reasoning\n\nDerailer-Rerailer \\cite{wan2025derailer-rerailer} uses a heuristic instability signal to detect \"derailed\" reasoning steps and trigger correction. Compared to B-IAVR:\n\n- **Heuristic vs learned.** Derailer-Rerailer relies on hand-designed instability metrics; B-IAVR learns the verification trigger end-to-end via RL. This eliminates the need for task-specific heuristic engineering and allows the trigger to adapt as the policy improves.\n- **Reasoning chains vs agent trajectories.** Derailer-Rerailer operates on single-turn reasoning chains; B-IAVR on multi-turn agent trajectories with environment interaction. The environment provides a concrete grounding signal (observation changes) absent in pure reasoning settings.\n- **Correction scope.** Derailer-Rerailer re-generates from the derailed step; B-IAVR's verification may confirm or revise a single action, preserving the trajectory structure.\n\n### vs Sherlock: Reliable Agentic Workflow Execution\n\nSherlock \\cite{sherlock2025} applies selective verification to agentic *workflows* (DAG-structured task plans) using offline counterfactual analysis and speculative execution. The key distinction is the level of abstraction: Sherlock verifies workflow nodes (coarse-grained, offline planning); B-IAVR verifies individual agent actions (fine-grained, online decision-making). The two approaches are complementary---Sherlock could serve as a workflow-level planner while B-IAVR handles step-level verification within each workflow node.\n\n[TBD: exp result --- ablation table comparing B-IAVR with always-on / no-verify / random-$p$ / confidence-threshold baselines]\n\n&lt;!-- [中文注释] Director 决策点：3.3 节的对比深度是否合适？当前对 ARES 最详细（主要竞争者），Thinkless/Derailer-Rerailer/Sherlock 较简洁。如果 page budget 紧张，Sherlock 段可以移到 Related Work -->\n",
      "numLines": 185,
      "startLine": 1,
      "totalLines": 185
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01RXRxzRTQMaHQdfLCikavFt`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "3b148f66-8fed-433a-ab1c-f8cb5b6450a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155rgQJgacwRdhRDBTymiG2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12519,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12519
      },
      "output_tokens": 44,
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

_source line 8 · 2026-05-20T13:20:02.557Z_

<details><summary>↩ Tool result · `toolu_01RXRxzRTQMaHQdfLCikavFt`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "a171f6a8-378b-4cb4-9a57-32f4a3f9c80f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
````

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have the method_draft.md content and the writing norms. Let me convert the markdown to LaTeX. Key things to note from the norms:

1. No em-dashes (—) or en-dashes (–) for explanation - replace with commas, parentheses, or split sentences
2. No -ing phrase endings
3. Use booktabs for tables
4. Proper LaTeX formatting

Let me also note:
- The draft has HTML comments (&lt;!-- -->) which are Chinese director notes - these should be stripped
- [TBD] markers should be kept as comments or placeholders


- Citations like \cite{...} are already in LaTeX format
- Math is already LaTeX compatible
- Need to convert the markdown table to LaTeX tabular
- Need to handle bold/italic markers
- Need to handle lists

Now I'll carefully convert the structure. The section headers map to LaTeX commands: top-level becomes \section, subsections become \subsection, and subsubsections become \subsubsection. Display math with $$ converts to equation environments. I need to strip the HTML comments, preserve the [TBD] markers, and convert the markdown table to a proper booktabs table.

For inline formatting, I'm converting **bold** to \textbf, *italic* to \textit, and backticks to \texttt. I also notice some em-dashes that could be tightened up, and there's a line about episodes that appears to be cut off mid-sentence. I'm scanning through the text systematically to identify all dash usage—em-dashes need to be replaced with semicolons or periods, while hyphens in compound adjectives like "step-level" and "episode-level" are fine to keep. I'm also checking for italicized words like "when" that need proper LaTeX formatting, and making sure the table uses booktabs styling with appropriate cross-reference labels. I'm realizing the core task here is format conversion from Markdown to LaTeX, not content editing. The writing norms are just reference material—I need to preserve the actual content while changing only the formatting. Let me focus on the conversion itself rather than getting caught up in style revisions. Writing LaTeX structure... the `\langle\text{VERIFY}\rangle` tokens that appear outside math mode in the markdown, I need to wrap them in math mode or use a text command.

Looking at line 17: `$\langle\text{VERIFY}\rangle$` — already in inline math
And `$\langle\text{SKIP}\rangle$` — also in inline math

Line 52-53: The aligned equation uses `\pi(d_t, a_t \mid h_t)` — needs equation environment.

Lines 56-58: Numbered list with descriptions.

Line 70-71: Cases environment for r_task.

Lines 82-83: Two consecutive equations that form the combined reward. Could use align environment.

Line 86: Update rule for γ_c.

Line 98-99: GRPO advantage formula.

Line 101-103: GRPO objective with multi-line structure that could benefit from split or align.

Line 116-118: GiGPO advantage formula.

For the comparison table around lines 150-157, I need to convert the markdown table into a booktabs-formatted LaTeX table with proper styling.

I should also add labels to sections and key equations to enable cross-referencing throughout the document. Finally, I'll handle the [TBD: ...] markers by converting them to proper notation.

Writing the LaTeX now...

Formatting the Method section with proper equation environments and labels... The verification policy is implemented by adding special control tokens to the language model's output—either $\langle\text{VERIFY}\rangle$ or $\langle\text{SKIP}\rangle$ preceding each action. To measure whether verification is actually useful, I'm defining an action-change indicator that checks whether the agent's action differs before and after the verification step.

The crucial observation is that most self-verification doesn't actually change behavior—it's confirmatory rather than corrective. When the action remains unchanged, the verification was just wasted computation. But when it does produce a different action, that signals the verification contained meaningful decision-relevant information. I'm using semantic canonicalization to compare actions fairly, mapping them to structured tuples so surface-level variations don't create false positives.

Now I'm working through the formatting question around em-dashes. The instruction emphasizes preserving content while only changing format, so I should keep the substance intact but adjust the typographic choices to align with paper-writing conventions. The em-dashes can become semicolons or other punctuation that serves the same logical function without the stylistic baggage.

Let me write out the complete LaTeX file with this approach in mind. I'm working through the structure of the comparison section, deciding whether to use subsubsections or paragraphs for the individual method comparisons—the markdown headers suggest subsubsections are appropriate here, and I'll keep that consistent with the rest of the document structure. I'm identifying the paragraph-level headers within the Reward Design section — these bold text items like "Task success reward" and "Action-change reward" should use LaTeX's `\paragraph{}` command rather than markdown-style headers. I also notice the acronym breakdown for B-IAVR needs special formatting to highlight each letter, and I'll need to handle the numbered and bulleted lists in the extension and comparison sections appropriately. Now I'm ready to write out the complete LaTeX file with proper equation numbering and structure.

I should check which equations are actually referenced elsewhere in the document before deciding on numbering — looking through the draft, I see section references but no explicit equation citations like "Eq. (X)", so I'll number all equations since they're substantive and could be referenced from other parts of the paper. I also notice there are several [TBD] markers scattered throughout that I'll need to preserve as placeholders for the author to fill in later.

For the inline code snippets like `go to shelf 1`, I'll wrap them in `\texttt{}` to maintain the monospace formatting in LaTeX. The HTML comments in Chinese appear to be editorial notes, so I'll remove those entirely. Now I need to be careful with LaTeX special characters when writing out the complete file. Hyphens in cite keys work fine in LaTeX. Now I'm writing out the complete file structure, being careful with the formatting — I'll set up the section headers, subsections, and the math notation for the tuple representation, then fill in the content carefully.

Writing LaTeX file... Writing LaTeX table and equations... Writing LaTeX equations... Finishing the LaTeX equation with the clipping function and KL divergence term, then moving on to write out the full document. I need to convert the bold section headings to LaTeX paragraph formatting and make sure the reward descriptions are properly formatted. the original formatting. I'll go with `\paragraph{Task success reward.}` to preserve the period from the markdown source.

Now I'm thinking through how to handle the informal mathematical notation—like the arrow notation showing how probability changes with uncertainty. I'll use an unnumbered equation environment to keep it consistent with the rest of the document, then move on to writing out the full LaTeX file.

For the equation numbering strategy, I should focus on the core equations that define the method: the action-change indicator, combined reward formulation, Lagrangian updates, and the GRPO objective. The supporting equations like the individual reward components and cost calculations can remain unnumbered to keep the document cleaner. Actually, since this is a methods section, numbering everything might be the safer approach to match typical paper conventions.

Now I'm writing out the full LaTeX file with all the equations properly formatted and the citation keys already in place. I need to make sure the formatting is consistent throughout and all the technical details are captured correctly.

For the GiGPO section, I'm converting the numbered list items into LaTeX enumerate format with bold headings, and then handling the verification subroutine steps the same way.

In the comparison section, I'll switch the bullet points to itemize environment while preserving the bold labels.

I also need to replace the em-dashes throughout the document—converting them to semicolons, periods, or commas depending on context to match standard LaTeX conventions.

Now I'm ready to write out the full file. I'm deciding whether to replace the em-dashes since the style guide explicitly marks it as a hard rule, but I want to keep the scope focused on format conversion rather than deep content editing. I'll go ahead and convert `---` to proper LaTeX em-dashes, and I notice there's an en-dash in a number range at line 114 which the norms allow as an exception, so I'll leave that intact. Now I'm writing out the LaTeX file starting with the Method section and formalizing the interactive agent task as a POMDP.

Continuing with the mathematical definitions...

At each timestep, the agent observes the environment state and selects actions based on its policy, which conditions on the interaction history up to that point. Episodes end when the task succeeds or we hit the maximum step limit. Beyond the primary action selection, the agent also makes a binary verification decision at each step—either triggering a self-verification routine to reconsider its proposed action, or skipping verification entirely. I'm parameterizing this verification policy as another learned component.

In practice, the agent generates either a special VERIFY token or a SKIP token before outputting its action, allowing the language model to control whether it wants to double-check itself. The key signal for measuring whether verification is actually useful is whether the agent changes its action after verification—I'm tracking this as an action-change indicator that compares the action before and after the verification step.

The crucial observation is that most self-verification doesn't actually change anything; it's confirmatory rather than corrective. When the action stays the same, verification just wasted compute. When it changes, that's when verification actually provided decision-relevant information, so I'm using that signal to measure informativeness.

Now I'm modeling the cost of verification—each check requires a fixed computational overhead for the additional inference pass, and across an episode, this accumulates based on how many times verification is triggered. The core objective is to learn a policy that balances task success against this verification cost, deciding when verification is worth the computational expense. I'm introducing B-IAVR, which trains the model to selectively decide when to verify its outputs using action changes as a signal for how informative verification is, combining a binary verification policy at each step with a composite reward function that balances task success, verification value, and computational cost, all optimized through reinforcement learning with GRPO and optional step-level credit assignment.

The verification policy factors into two components: the model first decides whether to verify or skip, then generates an action. When verification is triggered, the agent produces a preliminary action through greedy decoding, passes it through a verification module that examines the current state and goal to generate reasoning about whether to confirm or revise the action, and executes the final decision. If skipping is chosen, the preliminary action runs directly without this extra scrutiny.

In the actual implementation, both the verification decision and action generation share the same language model backbone, with the verification choice encoded as a special token prefix—this keeps things efficient by avoiding separate models and enables end-to-end reinforcement learning training.

The reward structure combines task completion, action changes from verification, and cost considerations. Task success gives a binary episode-level reward when the goal is achieved. Action-change rewards are applied at each step when verification actually modifies the action, serving as a signal for how useful the verification was.

Writing reward equations... cost-performance tradeoff without hand-tuning $\gamma_c$. The action-change reward isn't conditioned on task success—even failed episodes provide useful signal when the agent changes its action, since that reveals uncertainty in the initial decision and avoids the bootstrap problem that arises when base success rates are low. For training, I'm using Group Relative Policy Optimization to estimate advantages from rollout groups without needing a separate value function.

Within each group, I compute normalized advantages by centering each rollout's reward against the group mean and dividing by the group standard deviation. The GRPO objective then applies a clipped importance ratio to these advantages while adding KL regularization against the reference policy to prevent divergence. For multi-turn rollouts, I'm using step-independent context where the model receives fresh context at each step rather than accumulating history.

To address the limitation that episode-level advantages don't provide step-specific credit assignment—which causes high variance when a single failed action taints an entire trajectory—GiGPO introduces a nested grouping structure that assigns advantages at the step level. iGPO constructs a step-level group by comparing outcomes of rollouts that share the same prefix up to step $t-1$ but diverge at step $t$, using normalized reward differences to provide dense learning signals without a learned critic.

GiGPO fits well with B-IAVR because verification decisions operate at the step level with localized impact, the action-change reward naturally aligns with step-level advantage computation, and decomposing sparse task rewards into denser step-level components helps overcome cold-start problems.

Now I'm looking at how B-IAVR extends the Self-Guide framework by incorporating the internal evaluator's confidence scores as features for the verification policy, so the model can learn when to request verification based on state uncertainty. Now I'm comparing B-IAVR with ARES across several key dimensions—while ARES uses a continuous reasoning effort allocation trained with outcome and efficiency rewards, B-IAVR takes a simpler binary approach to verification decisions, using action-level feedback as the training signal instead of pre-defined quality metrics. The key distinction from Thinkless is that while both use RL to learn binary triggers, they operate in fundamentally different contexts—Thinkless decides whether to invoke internal reasoning on single-turn questions, whereas B-IAVR determines when to re-observe and re-reason within multi-step agent interactions where each decision depends on environment feedback. B-IAVR's verification is about external environment interaction, not just internal chain-of-thought computation.

For Derailer-Rerailer, the main difference is that it uses hand-crafted instability metrics to detect reasoning failures, while B-IAVR learns the verification trigger end-to-end through RL, allowing it to discover what signals actually matter for deciding when to re-verify.

B-IAVR also operates on multi-turn agent trajectories with environment interaction rather than single reasoning chains, which gives it concrete grounding through observation changes. When verification triggers, B-IAVR can confirm or revise individual actions while keeping the trajectory intact, whereas Derailer-Rerailer regenerates from the derailed step entirely.

Sherlock takes a different angle by verifying coarse-grained workflow nodes using offline counterfactual analysis, while B-IAVR focuses on fine-grained online verification of individual actions—these approaches complement each other, with Sherlock handling workflow-level planning and B-IAVR managing step-level verification within each node.

Now I'm reviewing the LaTeX conversion details: making sure formatting like em-dashes, bold, italics, code blocks, and math notation are all properly handled. The KL divergence notation with `\|` should render correctly as the parallel bars symbol, and I'm being careful with hyphenation to prevent unwanted spacing in expressions like `1{-}\varepsilon`.

For the clip function notation, I'm simplifying to use standard binary minus spacing since `1-\varepsilon` and `1+\varepsilon` are straightforward arithmetic expressions. I'm also considering table formatting for the ARES comparison—using fixed column widths like `p{3.2cm}` to ensure text wraps properly in a two-column paper layout where space is constrained. Writing LaTeX formatting...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "fdfefd5a-9d9f-4568-a425-6d6761065b72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL4MMKJBznVJZ3UX8Dx73F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11447,
      "cache_read_input_tokens": 24220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11447
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

_source line 10_

读取 method_draft.md 和写作规范完成，开始转换。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "9c57a743-fed8-4922-a108-f339dcdd8640",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL4MMKJBznVJZ3UX8Dx73F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11447,
      "cache_read_input_tokens": 24220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11447
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

_source line 11_

<details open><summary>🔧 Tool call — Write · `toolu_01SYufYPzSku8U7jJXsuZ21w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method.tex",
  "content": "% method.tex — Method section for B-IAVR paper\n% Converted from method_draft.md\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{subsec:problem-formulation}\n\n\\subsubsection{Interactive Agent as POMDP}\n\nWe formalize the interactive agent task as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = \\langle \\mathcal{S}, \\mathcal{A}, \\mathcal{O}, T, O, R, \\gamma \\rangle$, where $\\mathcal{S}$ is the state space of the environment (e.g., object locations and states in a household), $\\mathcal{A}$ is the action space (e.g., natural language commands such as \\texttt{go to shelf 1}, \\texttt{take mug 2}), $\\mathcal{O}$ is the observation space (textual descriptions of the environment), $T: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\Delta(\\mathcal{S})$ is the transition function, $O: \\mathcal{S} \\rightarrow \\Delta(\\mathcal{O})$ is the observation function, $R: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathbb{R}$ is the reward function, and $\\gamma$ is the discount factor.\n\nAt each timestep $t$, the agent receives observation $o_t \\in \\mathcal{O}$ and selects action $a_t \\in \\mathcal{A}$ according to its policy $\\pi_\\phi(a_t \\mid h_t)$, where $h_t = (o_1, a_1, \\ldots, o_t)$ is the interaction history. The episode terminates upon task completion (success) or after a maximum number of steps $T_{\\max}$.\n\n\\subsubsection{Verification Decision}\n\nAt each step $t$, in addition to the primary action $a_t$, the agent makes a binary verification decision:\n\\begin{equation}\nd_t \\in \\{0, 1\\}\n\\label{eq:verify-decision}\n\\end{equation}\nwhere $d_t = 1$ triggers a self-verification subroutine and $d_t = 0$ skips verification. When $d_t = 1$, the agent re-examines its current observation and proposed action, potentially revising $a_t$ to an alternative $a_t'$.\n\nWe parameterize the verification policy as $\\pi_\\theta(d_t \\mid s_t)$, where $s_t$ is a compact representation of the agent's state at step $t$ (including the current observation, proposed action, and task context). In practice, $\\pi_\\theta$ is realized by augmenting the agent's action space with a special control token $\\langle\\text{VERIFY}\\rangle$ that precedes the action output, such that the language model generates either $\\langle\\text{VERIFY}\\rangle\\, a_t$ or $\\langle\\text{SKIP}\\rangle\\, a_t$ at each step.\n\n\\subsubsection{Action-Change Signal}\n\nWe define the \\textbf{action-change indicator} as the primary signal for verification informativeness:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}\\left[a_t^{\\text{post}} \\neq a_t^{\\text{pre}}\\right]\n\\label{eq:action-change}\n\\end{equation}\nwhere $a_t^{\\text{pre}}$ is the action the agent would have taken without verification (obtained via a single greedy decode pass), and $a_t^{\\text{post}}$ is the action after the verification subroutine. Equality is assessed via semantic canonicalization (e.g., mapping actions to $\\langle \\text{verb}, \\text{object}, \\text{receptacle} \\rangle$ tuples in ALFWorld) to avoid spurious mismatches from surface-form variation.\n\nThe key insight is that \\textbf{most self-verification is confirmatory rather than corrective}~\\cite{self-verification-dilemma-2026}. When $\\Delta a_t = 0$, the verification consumed compute without altering behavior; it was uninformative. When $\\Delta a_t = 1$, the verification produced a behavioral change, which indicates it carried decision-relevant information.\n\n\\subsubsection{Verification Cost Model}\n\nEach verification incurs a fixed cost $c_{\\text{verify}}$ (proportional to the additional inference tokens required). The total verification cost for an episode of length $T$ is:\n\\begin{equation}\nC_{\\text{total}} = \\sum_{t=1}^{T} d_t \\cdot c_{\\text{verify}}\n\\label{eq:total-cost}\n\\end{equation}\n\nIn practice, $c_{\\text{verify}}$ corresponds to the additional forward pass needed for the verification subroutine (re-observation, re-reasoning, and potential action revision), which approximately doubles the per-step inference cost.\n\n\\subsubsection{Objective}\n\nThe goal of B-IAVR is to learn a verification policy $\\pi_\\theta$ that maximizes task success while minimizing verification cost. We formulate this as a constrained optimization problem:\n\\begin{equation}\n\\max_\\theta \\; \\mathbb{E}_{\\pi_\\theta, \\pi_\\phi}\\left[\\sum_{t=1}^{T} R(s_t, a_t)\\right] \\quad \\text{s.t.} \\quad \\mathbb{E}_{\\pi_\\theta}\\left[C_{\\text{total}}\\right] \\leq C_{\\text{budget}}\n\\label{eq:objective}\n\\end{equation}\nwhere $C_{\\text{budget}}$ is the verification budget constraint. In practice, we relax this to an unconstrained objective via Lagrangian relaxation (Section~\\ref{subsec:biavr}).\n\n\n\\subsection{B-IAVR: Selective Self-Verification via RL}\n\\label{subsec:biavr}\n\n\\subsubsection{Overview}\n\nB-IAVR (\\textbf{B}inary \\textbf{I}nformative \\textbf{A}ction \\textbf{V}erification via \\textbf{R}L) trains a language model agent to decide \\textit{when} to invoke self-verification, using action change as a reward signal for verification informativeness. The method consists of three components: (1) a selective verification policy that makes per-step binary verify/skip decisions, (2) a composite reward function combining task success, verification informativeness, and cost, and (3) an RL training procedure based on GRPO with optional GiGPO extension for step-level credit assignment.\n\n\\subsubsection{Selective Verification Policy}\n\nThe agent's generation at each step $t$ is structured as:\n\\begin{equation}\n\\pi(d_t, a_t \\mid h_t) = \\pi_\\theta(d_t \\mid h_t) \\cdot \\pi_\\phi(a_t \\mid h_t, d_t)\n\\label{eq:policy-factorization}\n\\end{equation}\n\nWhen the model generates $\\langle\\text{VERIFY}\\rangle$, a verification subroutine is triggered:\n\\begin{enumerate}\n    \\item The agent produces a preliminary action $a_t^{\\text{pre}}$ via greedy decoding from the current state.\n    \\item The verification module re-examines the observation $o_t$, the proposed action $a_t^{\\text{pre}}$, and the task goal $g$, then generates a verification rationale.\n    \\item Based on the rationale, the agent either confirms $a_t^{\\text{pre}}$ or revises it to $a_t^{\\text{post}}$.\n\\end{enumerate}\n\nWhen $\\langle\\text{SKIP}\\rangle$ is generated, $a_t^{\\text{pre}}$ is directly executed without verification.\n\nIn practice, $\\pi_\\theta$ and $\\pi_\\phi$ share the same language model backbone, with the verification decision encoded as a special token prefix. This avoids the overhead of maintaining separate models and allows end-to-end RL training.\n\n\\subsubsection{Reward Design}\n\nThe reward function combines three components to balance task performance, verification quality, and cost:\n\n\\paragraph{Task success reward.} A binary episode-level reward indicating whether the task was completed:\n\\begin{equation}\nr_{\\text{task}} = \\begin{cases} r_+ & \\text{if task completed successfully} \\\\ 0 & \\text{otherwise} \\end{cases}\n\\label{eq:task-reward}\n\\end{equation}\n\n\\paragraph{Action-change reward.} A step-level reward given when verification produces a behavioral change, serving as a proxy for verification informativeness:\n\\begin{equation}\nr_{\\text{ac}, t} = \\alpha \\cdot d_t \\cdot \\Delta a_t\n\\label{eq:ac-reward}\n\\end{equation}\nwhere $\\alpha > 0$ controls the magnitude of the informativeness bonus. This reward is only assigned at steps where verification is triggered ($d_t = 1$) and the action changes ($\\Delta a_t = 1$).\n\n\\paragraph{Verification cost penalty.} A step-level penalty for each verification invocation:\n\\begin{equation}\nr_{\\text{cost}, t} = -\\gamma_c \\cdot d_t\n\\label{eq:cost-penalty}\n\\end{equation}\nwhere $\\gamma_c > 0$ is the per-verification cost coefficient.\n\nThe \\textbf{combined reward} for an episode is:\n\\begin{align}\nR &= r_{\\text{task}} + \\sum_{t=1}^{T}\\left(\\beta \\cdot r_{\\text{ac}, t} + r_{\\text{cost}, t}\\right) \\nonumber \\\\\n  &= r_{\\text{task}} + \\sum_{t=1}^{T} d_t \\left(\\beta \\cdot \\alpha \\cdot \\Delta a_t - \\gamma_c\\right)\n\\label{eq:combined-reward}\n\\end{align}\nwhere $\\beta$ balances the informativeness bonus against the cost penalty. The cost coefficient $\\gamma_c$ is updated via dual gradient ascent to enforce the budget constraint:\n\\begin{equation}\n\\gamma_c \\leftarrow \\gamma_c + \\eta_\\gamma \\left(\\mathbb{E}[C_{\\text{total}}] - C_{\\text{budget}}\\right)\n\\label{eq:lagrangian-update}\n\\end{equation}\n\nThis Lagrangian formulation allows the agent to learn a cost-performance tradeoff without hand-tuning $\\gamma_c$.\n\n\\paragraph{Interaction between action-change reward and task success.} Note that $r_{\\text{ac}}$ is not gated on task success. A verification that changes the action is informative regardless of episode outcome; even in failed episodes, action changes driven by verification reveal that the agent's initial action was uncertain and provide useful training signal. This design choice avoids the bootstrap problem encountered with success-gated rewards when base success rates are low.\n% TODO: cite exp013f gaming / D012-D013 analysis\n\n\\subsubsection{Training with GRPO}\n\nWe train $\\pi_\\theta$ using Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, which estimates advantages from groups of rollouts without requiring a learned value function.\n\nFor each training step, we sample $G$ groups of $K$ rollouts per task instance. Within each group $g$, the advantage of rollout $k$ is computed as:\n\\begin{equation}\n\\hat{A}^{(g)}_k = \\frac{R^{(g)}_k - \\text{mean}(\\{R^{(g)}_j\\}_{j=1}^K)}{\\text{std}(\\{R^{(g)}_j\\}_{j=1}^K) + \\epsilon}\n\\label{eq:grpo-advantage}\n\\end{equation}\n\nThe GRPO objective with KL regularization is:\n\\begin{multline}\n\\mathcal{L}_{\\text{GRPO}}(\\theta) = -\\mathbb{E}_{g,k}\\left[\\min\\left(\\rho_t \\hat{A}^{(g)}_k, \\; \\text{clip}(\\rho_t, 1-\\varepsilon, 1+\\varepsilon) \\hat{A}^{(g)}_k\\right)\\right] \\\\\n+ \\lambda_{\\text{KL}} \\, D_{\\text{KL}}(\\pi_\\theta \\| \\pi_{\\text{ref}})\n\\label{eq:grpo-objective}\n\\end{multline}\nwhere $\\rho_t = \\frac{\\pi_\\theta(a_t | h_t)}{\\pi_{\\text{ref}}(a_t | h_t)}$ is the importance ratio and $\\pi_{\\text{ref}}$ is the reference policy (initialized from the SFT checkpoint).\n\n\\paragraph{Step-independent context.} Following the rollout design of verl-agent~\\cite{selfguide2026}, we employ step-independent context for multi-turn rollouts: at each step, the model receives only the current observation and task context rather than the full interaction history. This prevents context length explosion in long-horizon tasks and maintains consistent inference quality across steps, a critical factor for training stability in interactive agent settings.\n\n\\subsubsection{Extension: GiGPO for Step-Level Credit Assignment}\n\n% TODO: GiGPO details\n\nA known limitation of episode-level GRPO is that the advantage $\\hat{A}^{(g)}_k$ is shared across all steps within a rollout and provides no step-level credit assignment. In multi-turn agent tasks where episodes span 10--30 steps, this leads to high variance and slow learning. A single failed step can assign negative advantage to all preceding correct actions.\n\nGiGPO (Group-in-Group Policy Optimization)~\\cite{feng2025gigpo} addresses this via a nested group structure. For each step $t$ within a rollout, GiGPO constructs a \\textit{step-level group} by comparing the outcomes of rollouts that share the same prefix up to step $t-1$ but diverge at step $t$:\n\\begin{equation}\n\\hat{A}^{\\text{step}}_t = \\frac{R_t^{>} - \\text{mean}(\\{R^{>}_j\\})}{\\text{std}(\\{R^{>}_j\\}) + \\epsilon}\n\\label{eq:gigpo-advantage}\n\\end{equation}\nwhere $R_t^{>}$ denotes the cumulative reward from step $t$ onward. This provides dense, step-level learning signal without requiring a learned critic.\n\nIn the B-IAVR context, GiGPO is particularly well-suited because:\n\\begin{enumerate}\n    \\item \\textbf{Verification decisions are step-level.} The verify/skip decision at step $t$ has localized impact. GiGPO can attribute the outcome change to the specific verification decision rather than spreading credit across the entire episode.\n    \\item \\textbf{Action-change reward is already step-level.} The reward $r_{\\text{ac},t}$ naturally aligns with GiGPO's step-level advantage structure and provides dense reward signal at the granularity where credit assignment operates.\n    \\item \\textbf{Sparse task reward benefits from decomposition.} When the episode-level task reward $r_{\\text{task}}$ is binary and sparse, GiGPO's step-level groups break the learning signal into denser components and mitigate the cold-start problem observed with pure GRPO on sparse rewards.\n\\end{enumerate}\n\n% TODO: exp result — GiGPO vs GRPO training curves, convergence speed comparison\n\n\\subsubsection{Self-Guide Integration}\n\nB-IAVR builds upon the Self-Guide framework~\\cite{selfguide2026}, which co-evolves a task policy and an internal reward model through iterative RL training. Specifically, Self-Guide trains a policy $\\pi_\\phi$ alongside an internal evaluator $V_\\psi$ that scores intermediate states and provides denser reward signal than the sparse environment reward alone.\n\nWe extend Self-Guide by introducing the verification decision layer: the internal evaluator $V_\\psi(s_t)$ serves as an additional input feature to the verification policy $\\pi_\\theta(d_t \\mid s_t, V_\\psi(s_t))$. Intuitively, when the internal evaluator assigns low confidence to the current state (indicating the agent is uncertain about its action), verification is more likely to be informative. This creates a natural trigger mechanism:\n\\begin{equation}\nP(d_t = 1) \\uparrow \\quad \\text{when} \\quad V_\\psi(s_t) \\text{ is low (uncertain)}\n\\label{eq:selfguide-trigger}\n\\end{equation}\n\nThe co-evolution property of Self-Guide ensures that as the task policy improves, the internal evaluator also calibrates. This leads to a progressively refined verification trigger that adapts to the agent's evolving competence.\n\n% TODO: exp result — Self-Guide internal reward correlation with action-change frequency\n\n\n\\subsection{Comparison with Related Methods}\n\\label{subsec:comparison}\n\nWe position B-IAVR against three categories of related methods: adaptive reasoning effort, selective verification, and self-correction in agents.\n\n\\subsubsection{vs ARES: Adaptive Reasoning Effort Selection}\n\nARES~\\cite{yang2026ares} trains an SFT-initialized router to allocate continuous reasoning effort per step, optimized via GRPO with a combined outcome and token-efficiency reward. B-IAVR differs in three fundamental aspects:\n\n\\begin{table}[t]\n\\centering\n\\caption{Comparison of B-IAVR with ARES across key design dimensions.}\n\\label{tab:ares-comparison}\n\\begin{tabular}{lp{3.2cm}p{3.2cm}}\n\\toprule\n\\textbf{Dimension} & \\textbf{ARES} & \\textbf{B-IAVR (Ours)} \\\\\n\\midrule\n\\textbf{Decision type} & Continuous effort level & Binary verify/skip \\\\\n\\textbf{Training signal} & Pre-defined quality metrics + token efficiency & Action change (behavioral) \\\\\n\\textbf{Data requirement} & Difficulty-annotated data for SFT bootstrap & Environment interaction only \\\\\n\\textbf{Scope} & General reasoning tasks & Interactive agent tasks \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe binary decision in B-IAVR offers two advantages: (1) it is more interpretable, as one can directly audit \\textit{which steps} were verified and \\textit{whether} the verification changed behavior, and (2) it avoids the need for difficulty annotations, as the action-change signal is self-supervised from the agent's own behavioral variation.\n\nConversely, ARES's continuous allocation is more flexible for tasks where ``partial verification'' makes sense. B-IAVR's binary design is motivated by the interactive agent setting, where verification is a discrete subroutine (re-observe environment, re-reason, potentially revise) that is either invoked or not.\n\n\\subsubsection{vs Thinkless: Learning When to Think}\n\nThinkless~\\cite{du2025thinkless} uses RL to train a control token that decides whether to invoke extended thinking (chain-of-thought) before answering. While methodologically parallel to B-IAVR (both learn a binary computation trigger via RL), they address different settings:\n\\begin{itemize}\n    \\item \\textbf{Single-turn vs multi-turn.} Thinkless operates on single-turn QA; B-IAVR on multi-step interactive agent trajectories where each decision depends on environment feedback.\n    \\item \\textbf{Computation type.} Thinkless controls \\textit{internal reasoning} (thinking tokens); B-IAVR controls \\textit{external verification} (re-observation of the environment), grounding the signal in behavioral change rather than token-level computation.\n    \\item \\textbf{Reward signal.} Thinkless uses task correctness; B-IAVR introduces the action-change signal as a verification-specific informativeness measure.\n\\end{itemize}\n\n\\subsubsection{vs Derailer-Rerailer: Adaptive Verification for Reasoning}\n\nDerailer-Rerailer~\\cite{wan2025derailer-rerailer} uses a heuristic instability signal to detect ``derailed'' reasoning steps and trigger correction. Compared to B-IAVR:\n\\begin{itemize}\n    \\item \\textbf{Heuristic vs learned.} Derailer-Rerailer relies on hand-designed instability metrics; B-IAVR learns the verification trigger end-to-end via RL. This eliminates the need for task-specific heuristic engineering and allows the trigger to adapt as the policy improves.\n    \\item \\textbf{Reasoning chains vs agent trajectories.} Derailer-Rerailer operates on single-turn reasoning chains; B-IAVR on multi-turn agent trajectories with environment interaction. The environment provides a concrete grounding signal (observation changes) absent in pure reasoning settings.\n    \\item \\textbf{Correction scope.} Derailer-Rerailer re-generates from the derailed step; B-IAVR's verification may confirm or revise a single action and preserves the trajectory structure.\n\\end{itemize}\n\n\\subsubsection{vs Sherlock: Reliable Agentic Workflow Execution}\n\nSherlock~\\cite{sherlock2025} applies selective verification to agentic \\textit{workflows} (DAG-structured task plans) using offline counterfactual analysis and speculative execution. The key distinction is the level of abstraction: Sherlock verifies workflow nodes (coarse-grained, offline planning); B-IAVR verifies individual agent actions (fine-grained, online decision-making). The two approaches are complementary: Sherlock could serve as a workflow-level planner while B-IAVR handles step-level verification within each workflow node.\n\n% TODO: exp result — ablation table comparing B-IAVR with always-on / no-verify / random-p / confidence-threshold baselines\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "6947ead8-d891-42c0-be1c-9deb2aea0283",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL4MMKJBznVJZ3UX8Dx73F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11447,
      "cache_read_input_tokens": 24220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11447
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

_source line 12 · 2026-05-20T13:25:46.648Z_

<details><summary>↩ Tool result · `toolu_01SYufYPzSku8U7jJXsuZ21w`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "86c1e540-0973-4780-b9fb-2ffbd52ff253",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method.tex",
    "content": "% method.tex — Method section for B-IAVR paper\n% Converted from method_draft.md\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{subsec:problem-formulation}\n\n\\subsubsection{Interactive Agent as POMDP}\n\nWe formalize the interactive agent task as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = \\langle \\mathcal{S}, \\mathcal{A}, \\mathcal{O}, T, O, R, \\gamma \\rangle$, where $\\mathcal{S}$ is the state space of the environment (e.g., object locations and states in a household), $\\mathcal{A}$ is the action space (e.g., natural language commands such as \\texttt{go to shelf 1}, \\texttt{take mug 2}), $\\mathcal{O}$ is the observation space (textual descriptions of the environment), $T: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\Delta(\\mathcal{S})$ is the transition function, $O: \\mathcal{S} \\rightarrow \\Delta(\\mathcal{O})$ is the observation function, $R: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathbb{R}$ is the reward function, and $\\gamma$ is the discount factor.\n\nAt each timestep $t$, the agent receives observation $o_t \\in \\mathcal{O}$ and selects action $a_t \\in \\mathcal{A}$ according to its policy $\\pi_\\phi(a_t \\mid h_t)$, where $h_t = (o_1, a_1, \\ldots, o_t)$ is the interaction history. The episode terminates upon task completion (success) or after a maximum number of steps $T_{\\max}$.\n\n\\subsubsection{Verification Decision}\n\nAt each step $t$, in addition to the primary action $a_t$, the agent makes a binary verification decision:\n\\begin{equation}\nd_t \\in \\{0, 1\\}\n\\label{eq:verify-decision}\n\\end{equation}\nwhere $d_t = 1$ triggers a self-verification subroutine and $d_t = 0$ skips verification. When $d_t = 1$, the agent re-examines its current observation and proposed action, potentially revising $a_t$ to an alternative $a_t'$.\n\nWe parameterize the verification policy as $\\pi_\\theta(d_t \\mid s_t)$, where $s_t$ is a compact representation of the agent's state at step $t$ (including the current observation, proposed action, and task context). In practice, $\\pi_\\theta$ is realized by augmenting the agent's action space with a special control token $\\langle\\text{VERIFY}\\rangle$ that precedes the action output, such that the language model generates either $\\langle\\text{VERIFY}\\rangle\\, a_t$ or $\\langle\\text{SKIP}\\rangle\\, a_t$ at each step.\n\n\\subsubsection{Action-Change Signal}\n\nWe define the \\textbf{action-change indicator} as the primary signal for verification informativeness:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}\\left[a_t^{\\text{post}} \\neq a_t^{\\text{pre}}\\right]\n\\label{eq:action-change}\n\\end{equation}\nwhere $a_t^{\\text{pre}}$ is the action the agent would have taken without verification (obtained via a single greedy decode pass), and $a_t^{\\text{post}}$ is the action after the verification subroutine. Equality is assessed via semantic canonicalization (e.g., mapping actions to $\\langle \\text{verb}, \\text{object}, \\text{receptacle} \\rangle$ tuples in ALFWorld) to avoid spurious mismatches from surface-form variation.\n\nThe key insight is that \\textbf{most self-verification is confirmatory rather than corrective}~\\cite{self-verification-dilemma-2026}. When $\\Delta a_t = 0$, the verification consumed compute without altering behavior; it was uninformative. When $\\Delta a_t = 1$, the verification produced a behavioral change, which indicates it carried decision-relevant information.\n\n\\subsubsection{Verification Cost Model}\n\nEach verification incurs a fixed cost $c_{\\text{verify}}$ (proportional to the additional inference tokens required). The total verification cost for an episode of length $T$ is:\n\\begin{equation}\nC_{\\text{total}} = \\sum_{t=1}^{T} d_t \\cdot c_{\\text{verify}}\n\\label{eq:total-cost}\n\\end{equation}\n\nIn practice, $c_{\\text{verify}}$ corresponds to the additional forward pass needed for the verification subroutine (re-observation, re-reasoning, and potential action revision), which approximately doubles the per-step inference cost.\n\n\\subsubsection{Objective}\n\nThe goal of B-IAVR is to learn a verification policy $\\pi_\\theta$ that maximizes task success while minimizing verification cost. We formulate this as a constrained optimization problem:\n\\begin{equation}\n\\max_\\theta \\; \\mathbb{E}_{\\pi_\\theta, \\pi_\\phi}\\left[\\sum_{t=1}^{T} R(s_t, a_t)\\right] \\quad \\text{s.t.} \\quad \\mathbb{E}_{\\pi_\\theta}\\left[C_{\\text{total}}\\right] \\leq C_{\\text{budget}}\n\\label{eq:objective}\n\\end{equation}\nwhere $C_{\\text{budget}}$ is the verification budget constraint. In practice, we relax this to an unconstrained objective via Lagrangian relaxation (Section~\\ref{subsec:biavr}).\n\n\n\\subsection{B-IAVR: Selective Self-Verification via RL}\n\\label{subsec:biavr}\n\n\\subsubsection{Overview}\n\nB-IAVR (\\textbf{B}inary \\textbf{I}nformative \\textbf{A}ction \\textbf{V}erification via \\textbf{R}L) trains a language model agent to decide \\textit{when} to invoke self-verification, using action change as a reward signal for verification informativeness. The method consists of three components: (1) a selective verification policy that makes per-step binary verify/skip decisions, (2) a composite reward function combining task success, verification informativeness, and cost, and (3) an RL training procedure based on GRPO with optional GiGPO extension for step-level credit assignment.\n\n\\subsubsection{Selective Verification Policy}\n\nThe agent's generation at each step $t$ is structured as:\n\\begin{equation}\n\\pi(d_t, a_t \\mid h_t) = \\pi_\\theta(d_t \\mid h_t) \\cdot \\pi_\\phi(a_t \\mid h_t, d_t)\n\\label{eq:policy-factorization}\n\\end{equation}\n\nWhen the model generates $\\langle\\text{VERIFY}\\rangle$, a verification subroutine is triggered:\n\\begin{enumerate}\n    \\item The agent produces a preliminary action $a_t^{\\text{pre}}$ via greedy decoding from the current state.\n    \\item The verification module re-examines the observation $o_t$, the proposed action $a_t^{\\text{pre}}$, and the task goal $g$, then generates a verification rationale.\n    \\item Based on the rationale, the agent either confirms $a_t^{\\text{pre}}$ or revises it to $a_t^{\\text{post}}$.\n\\end{enumerate}\n\nWhen $\\langle\\text{SKIP}\\rangle$ is generated, $a_t^{\\text{pre}}$ is directly executed without verification.\n\nIn practice, $\\pi_\\theta$ and $\\pi_\\phi$ share the same language model backbone, with the verification decision encoded as a special token prefix. This avoids the overhead of maintaining separate models and allows end-to-end RL training.\n\n\\subsubsection{Reward Design}\n\nThe reward function combines three components to balance task performance, verification quality, and cost:\n\n\\paragraph{Task success reward.} A binary episode-level reward indicating whether the task was completed:\n\\begin{equation}\nr_{\\text{task}} = \\begin{cases} r_+ & \\text{if task completed successfully} \\\\ 0 & \\text{otherwise} \\end{cases}\n\\label{eq:task-reward}\n\\end{equation}\n\n\\paragraph{Action-change reward.} A step-level reward given when verification produces a behavioral change, serving as a proxy for verification informativeness:\n\\begin{equation}\nr_{\\text{ac}, t} = \\alpha \\cdot d_t \\cdot \\Delta a_t\n\\label{eq:ac-reward}\n\\end{equation}\nwhere $\\alpha > 0$ controls the magnitude of the informativeness bonus. This reward is only assigned at steps where verification is triggered ($d_t = 1$) and the action changes ($\\Delta a_t = 1$).\n\n\\paragraph{Verification cost penalty.} A step-level penalty for each verification invocation:\n\\begin{equation}\nr_{\\text{cost}, t} = -\\gamma_c \\cdot d_t\n\\label{eq:cost-penalty}\n\\end{equation}\nwhere $\\gamma_c > 0$ is the per-verification cost coefficient.\n\nThe \\textbf{combined reward} for an episode is:\n\\begin{align}\nR &= r_{\\text{task}} + \\sum_{t=1}^{T}\\left(\\beta \\cdot r_{\\text{ac}, t} + r_{\\text{cost}, t}\\right) \\nonumber \\\\\n  &= r_{\\text{task}} + \\sum_{t=1}^{T} d_t \\left(\\beta \\cdot \\alpha \\cdot \\Delta a_t - \\gamma_c\\right)\n\\label{eq:combined-reward}\n\\end{align}\nwhere $\\beta$ balances the informativeness bonus against the cost penalty. The cost coefficient $\\gamma_c$ is updated via dual gradient ascent to enforce the budget constraint:\n\\begin{equation}\n\\gamma_c \\leftarrow \\gamma_c + \\eta_\\gamma \\left(\\mathbb{E}[C_{\\text{total}}] - C_{\\text{budget}}\\right)\n\\label{eq:lagrangian-update}\n\\end{equation}\n\nThis Lagrangian formulation allows the agent to learn a cost-performance tradeoff without hand-tuning $\\gamma_c$.\n\n\\paragraph{Interaction between action-change reward and task success.} Note that $r_{\\text{ac}}$ is not gated on task success. A verification that changes the action is informative regardless of episode outcome; even in failed episodes, action changes driven by verification reveal that the agent's initial action was uncertain and provide useful training signal. This design choice avoids the bootstrap problem encountered with success-gated rewards when base success rates are low.\n% TODO: cite exp013f gaming / D012-D013 analysis\n\n\\subsubsection{Training with GRPO}\n\nWe train $\\pi_\\theta$ using Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, which estimates advantages from groups of rollouts without requiring a learned value function.\n\nFor each training step, we sample $G$ groups of $K$ rollouts per task instance. Within each group $g$, the advantage of rollout $k$ is computed as:\n\\begin{equation}\n\\hat{A}^{(g)}_k = \\frac{R^{(g)}_k - \\text{mean}(\\{R^{(g)}_j\\}_{j=1}^K)}{\\text{std}(\\{R^{(g)}_j\\}_{j=1}^K) + \\epsilon}\n\\label{eq:grpo-advantage}\n\\end{equation}\n\nThe GRPO objective with KL regularization is:\n\\begin{multline}\n\\mathcal{L}_{\\text{GRPO}}(\\theta) = -\\mathbb{E}_{g,k}\\left[\\min\\left(\\rho_t \\hat{A}^{(g)}_k, \\; \\text{clip}(\\rho_t, 1-\\varepsilon, 1+\\varepsilon) \\hat{A}^{(g)}_k\\right)\\right] \\\\\n+ \\lambda_{\\text{KL}} \\, D_{\\text{KL}}(\\pi_\\theta \\| \\pi_{\\text{ref}})\n\\label{eq:grpo-objective}\n\\end{multline}\nwhere $\\rho_t = \\frac{\\pi_\\theta(a_t | h_t)}{\\pi_{\\text{ref}}(a_t | h_t)}$ is the importance ratio and $\\pi_{\\text{ref}}$ is the reference policy (initialized from the SFT checkpoint).\n\n\\paragraph{Step-independent context.} Following the rollout design of verl-agent~\\cite{selfguide2026}, we employ step-independent context for multi-turn rollouts: at each step, the model receives only the current observation and task context rather than the full interaction history. This prevents context length explosion in long-horizon tasks and maintains consistent inference quality across steps, a critical factor for training stability in interactive agent settings.\n\n\\subsubsection{Extension: GiGPO for Step-Level Credit Assignment}\n\n% TODO: GiGPO details\n\nA known limitation of episode-level GRPO is that the advantage $\\hat{A}^{(g)}_k$ is shared across all steps within a rollout and provides no step-level credit assignment. In multi-turn agent tasks where episodes span 10--30 steps, this leads to high variance and slow learning. A single failed step can assign negative advantage to all preceding correct actions.\n\nGiGPO (Group-in-Group Policy Optimization)~\\cite{feng2025gigpo} addresses this via a nested group structure. For each step $t$ within a rollout, GiGPO constructs a \\textit{step-level group} by comparing the outcomes of rollouts that share the same prefix up to step $t-1$ but diverge at step $t$:\n\\begin{equation}\n\\hat{A}^{\\text{step}}_t = \\frac{R_t^{>} - \\text{mean}(\\{R^{>}_j\\})}{\\text{std}(\\{R^{>}_j\\}) + \\epsilon}\n\\label{eq:gigpo-advantage}\n\\end{equation}\nwhere $R_t^{>}$ denotes the cumulative reward from step $t$ onward. This provides dense, step-level learning signal without requiring a learned critic.\n\nIn the B-IAVR context, GiGPO is particularly well-suited because:\n\\begin{enumerate}\n    \\item \\textbf{Verification decisions are step-level.} The verify/skip decision at step $t$ has localized impact. GiGPO can attribute the outcome change to the specific verification decision rather than spreading credit across the entire episode.\n    \\item \\textbf{Action-change reward is already step-level.} The reward $r_{\\text{ac},t}$ naturally aligns with GiGPO's step-level advantage structure and provides dense reward signal at the granularity where credit assignment operates.\n    \\item \\textbf{Sparse task reward benefits from decomposition.} When the episode-level task reward $r_{\\text{task}}$ is binary and sparse, GiGPO's step-level groups break the learning signal into denser components and mitigate the cold-start problem observed with pure GRPO on sparse rewards.\n\\end{enumerate}\n\n% TODO: exp result — GiGPO vs GRPO training curves, convergence speed comparison\n\n\\subsubsection{Self-Guide Integration}\n\nB-IAVR builds upon the Self-Guide framework~\\cite{selfguide2026}, which co-evolves a task policy and an internal reward model through iterative RL training. Specifically, Self-Guide trains a policy $\\pi_\\phi$ alongside an internal evaluator $V_\\psi$ that scores intermediate states and provides denser reward signal than the sparse environment reward alone.\n\nWe extend Self-Guide by introducing the verification decision layer: the internal evaluator $V_\\psi(s_t)$ serves as an additional input feature to the verification policy $\\pi_\\theta(d_t \\mid s_t, V_\\psi(s_t))$. Intuitively, when the internal evaluator assigns low confidence to the current state (indicating the agent is uncertain about its action), verification is more likely to be informative. This creates a natural trigger mechanism:\n\\begin{equation}\nP(d_t = 1) \\uparrow \\quad \\text{when} \\quad V_\\psi(s_t) \\text{ is low (uncertain)}\n\\label{eq:selfguide-trigger}\n\\end{equation}\n\nThe co-evolution property of Self-Guide ensures that as the task policy improves, the internal evaluator also calibrates. This leads to a progressively refined verification trigger that adapts to the agent's evolving competence.\n\n% TODO: exp result — Self-Guide internal reward correlation with action-change frequency\n\n\n\\subsection{Comparison with Related Methods}\n\\label{subsec:comparison}\n\nWe position B-IAVR against three categories of related methods: adaptive reasoning effort, selective verification, and self-correction in agents.\n\n\\subsubsection{vs ARES: Adaptive Reasoning Effort Selection}\n\nARES~\\cite{yang2026ares} trains an SFT-initialized router to allocate continuous reasoning effort per step, optimized via GRPO with a combined outcome and token-efficiency reward. B-IAVR differs in three fundamental aspects:\n\n\\begin{table}[t]\n\\centering\n\\caption{Comparison of B-IAVR with ARES across key design dimensions.}\n\\label{tab:ares-comparison}\n\\begin{tabular}{lp{3.2cm}p{3.2cm}}\n\\toprule\n\\textbf{Dimension} & \\textbf{ARES} & \\textbf{B-IAVR (Ours)} \\\\\n\\midrule\n\\textbf{Decision type} & Continuous effort level & Binary verify/skip \\\\\n\\textbf{Training signal} & Pre-defined quality metrics + token efficiency & Action change (behavioral) \\\\\n\\textbf{Data requirement} & Difficulty-annotated data for SFT bootstrap & Environment interaction only \\\\\n\\textbf{Scope} & General reasoning tasks & Interactive agent tasks \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe binary decision in B-IAVR offers two advantages: (1) it is more interpretable, as one can directly audit \\textit{which steps} were verified and \\textit{whether} the verification changed behavior, and (2) it avoids the need for difficulty annotations, as the action-change signal is self-supervised from the agent's own behavioral variation.\n\nConversely, ARES's continuous allocation is more flexible for tasks where ``partial verification'' makes sense. B-IAVR's binary design is motivated by the interactive agent setting, where verification is a discrete subroutine (re-observe environment, re-reason, potentially revise) that is either invoked or not.\n\n\\subsubsection{vs Thinkless: Learning When to Think}\n\nThinkless~\\cite{du2025thinkless} uses RL to train a control token that decides whether to invoke extended thinking (chain-of-thought) before answering. While methodologically parallel to B-IAVR (both learn a binary computation trigger via RL), they address different settings:\n\\begin{itemize}\n    \\item \\textbf{Single-turn vs multi-turn.} Thinkless operates on single-turn QA; B-IAVR on multi-step interactive agent trajectories where each decision depends on environment feedback.\n    \\item \\textbf{Computation type.} Thinkless controls \\textit{internal reasoning} (thinking tokens); B-IAVR controls \\textit{external verification} (re-observation of the environment), grounding the signal in behavioral change rather than token-level computation.\n    \\item \\textbf{Reward signal.} Thinkless uses task correctness; B-IAVR introduces the action-change signal as a verification-specific informativeness measure.\n\\end{itemize}\n\n\\subsubsection{vs Derailer-Rerailer: Adaptive Verification for Reasoning}\n\nDerailer-Rerailer~\\cite{wan2025derailer-rerailer} uses a heuristic instability signal to detect ``derailed'' reasoning steps and trigger correction. Compared to B-IAVR:\n\\begin{itemize}\n    \\item \\textbf{Heuristic vs learned.} Derailer-Rerailer relies on hand-designed instability metrics; B-IAVR learns the verification trigger end-to-end via RL. This eliminates the need for task-specific heuristic engineering and allows the trigger to adapt as the policy improves.\n    \\item \\textbf{Reasoning chains vs agent trajectories.} Derailer-Rerailer operates on single-turn reasoning chains; B-IAVR on multi-turn agent trajectories with environment interaction. The environment provides a concrete grounding signal (observation changes) absent in pure reasoning settings.\n    \\item \\textbf{Correction scope.} Derailer-Rerailer re-generates from the derailed step; B-IAVR's verification may confirm or revise a single action and preserves the trajectory structure.\n\\end{itemize}\n\n\\subsubsection{vs Sherlock: Reliable Agentic Workflow Execution}\n\nSherlock~\\cite{sherlock2025} applies selective verification to agentic \\textit{workflows} (DAG-structured task plans) using offline counterfactual analysis and speculative execution. The key distinction is the level of abstraction: Sherlock verifies workflow nodes (coarse-grained, offline planning); B-IAVR verifies individual agent actions (fine-grained, online decision-making). The two approaches are complementary: Sherlock could serve as a workflow-level planner while B-IAVR handles step-level verification within each workflow node.\n\n% TODO: exp result — ablation table comparing B-IAVR with always-on / no-verify / random-p / confidence-threshold baselines\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 13_

已写入 `method.tex`。转换要点：

- Markdown 标题 → `\section` / `\subsection` / `\subsubsection`，均加 `\label`
- 所有 display math → `equation` / `align` / `multline` 环境，带编号和 label（共 15 个公式）
- 加粗段落标题（Task success reward 等） → `\paragraph{}`
- 表格 → booktabs 格式（`\toprule` / `\midrule` / `\bottomrule`），`p{3.2cm}` 列宽自动换行
- 有序/无序列表 → `enumerate` / `itemize`
- 行内代码 → `\texttt{}`，强调 → `\textit{}`，加粗 → `\textbf{}`
- 引用 `\cite{}` 前加 `~` 防断行
- em-dash（`---`）已替换为分号/句号（遵守写作规范 §5.1）
- `-ing` 短语结尾处做了最小化改写（如 "indicating..." → "which indicates..."）
- HTML 注释（Director 决策点）已删除
- `[TBD]` 标记转为 `% TODO:` LaTeX 注释
- 引号 → LaTeX 格式（` `` '' `）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "uuid": "60c0c46e-cf7d-42b0-9042-17e63b451a8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fMsUUVDZNhJSssU8Ljduo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20637,
      "cache_read_input_tokens": 35667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20637
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

_source line 14_

已写入 `method.tex`。转换要点：

- Markdown 标题 → `\section` / `\subsection` / `\subsubsection`，均加 `\label`
- 所有 display math → `equation` / `align` / `multline` 环境，带编号和 label（共 15 个公式）
- 加粗段落标题（Task success reward 等） → `\paragraph{}`
- 表格 → booktabs 格式（`\toprule` / `\midrule` / `\bottomrule`），`p{3.2cm}` 列宽自动换行
- 有序/无序列表 → `enumerate` / `itemize`
- 行内代码 → `\texttt{}`，强调 → `\textit{}`，加粗 → `\textbf{}`
- 引用 `\cite{}` 前加 `~` 防断行
- em-dash（`---`）已替换为分号/句号（遵守写作规范 §5.1）
- `-ing` 短语结尾处做了最小化改写（如 "indicating..." → "which indicates..."）
- HTML 注释（Director 决策点）已删除
- `[TBD]` 标记转为 `% TODO:` LaTeX 注释
- 引号 → LaTeX 格式（` `` '' `）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 361082,
  "duration_api_ms": 362321,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "e95a019c-6e23-4fef-91f7-085152bd1af1",
  "total_cost_usd": 0.8461207499999999,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 44603,
    "cache_read_input_tokens": 71588,
    "output_tokens": 21182,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44603,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 373,
        "cache_read_input_tokens": 35667,
        "cache_creation_input_tokens": 20637,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 20637
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1908,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001983,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 21182,
      "cacheReadInputTokens": 71588,
      "cacheCreationInputTokens": 44603,
      "webSearchRequests": 0,
      "costUSD": 0.8441377499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5f24eda7-036a-4fd2-a66b-fb155728717a"
}
```

</details>

---
