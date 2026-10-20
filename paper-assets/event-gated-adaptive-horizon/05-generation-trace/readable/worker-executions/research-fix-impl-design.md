# research fix impl design

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_research_fix-impl-design_20260513T011604.log`
- **Structured JSON:** [`54bf2d94e1d1b9122f91.json`](../../sessions/54/54bf2d94e1d1b9122f91.json)

## Before a recorded user message

52 recorded events

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
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
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
  "uuid": "f830d7ca-8d61-46d8-9fef-626ecaaa93e0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1778652000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f467c699-124f-43ea-961a-207a5c9f659f",
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the implementation design document to understand its current content and structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "19e737e0-23f0-447b-95f7-7b38ef404c3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HmpPd2dhALg6D6yy3HXeA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12210,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12210
      },
      "output_tokens": 20,
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

_source line 5_

先读取设计文档。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "24f4fd0f-74aa-4cf2-bf40-3246dfe942aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HmpPd2dhALg6D6yy3HXeA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12210,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12210
      },
      "output_tokens": 20,
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_0165CazV6VvYrEfA1ttR6vX5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "634a79be-c514-4d75-8c67-114bcbc48aec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HmpPd2dhALg6D6yy3HXeA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12210,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12210
      },
      "output_tokens": 20,
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

_source line 7 · 2026-05-13T01:16:19.166Z_

<details><summary>↩ Tool result · `toolu_0165CazV6VvYrEfA1ttR6vX5`</summary>

````text
1	# Event-Gated Adaptive-Horizon RSSM: Implementation Design
2	
3	**Codebase**: NM512/dreamerv3-torch (PyTorch)
4	**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.
5	
6	---
7	
8	## Architecture Overview (ASCII)
9	
10	```
11	                          IMAGINATION LOOP
12	 ┌──────────────────────────────────────────────────────────────────────┐
13	 │                                                                      │
14	 │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │
15	 │  │ prev    │    │           │    │          │    │               │  │
16	 │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │
17	 │  │         │    │           │    │ layers   │    │               │  │
18	 │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │
19	 │                 │  + Dt_emb │                            │          │
20	 │                 └───────────┘                       deter_t         │
21	 │                       ▲                                 │          │
22	 │                       │                                 ▼          │
23	 │              ┌────────┴───────┐              ┌──────────────────┐  │
24	 │              │  Dt Embedding  │              │  img_out_layers  │  │
25	 │              │  (learned,     │              └────────┬─────────┘  │
26	 │              │   dim=32)      │                       │            │
27	 │              └────────┬───────┘                       ▼            │
28	 │                       │                      ┌──────────────────┐  │
29	 │                       │                      │  stats layer     │  │
30	 │                       │                      │  -> stoch_t      │  │
31	 │              ┌────────┴───────┐              └────────┬─────────┘  │
32	 │              │  EVENT GATE    │                       │            │
33	 │              │  MLP(h_t, z_t) │◀──────────────────────┤            │
34	 │              │                │                       │            │
35	 │              │  Gumbel-       │              ┌────────┴─────────┐  │
36	 │              │  Softmax       │              │  feat_t =        │  │
37	 │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │
38	 │              └────────────────┘              │   deter_t]       │  │
39	 │                                              └────────┬─────────┘  │
40	 │                                                       │            │
41	 │                                                       ▼            │
42	 │                                              ┌──────────────────┐  │
43	 │                                              │  Actor / Critic  │  │
44	 │                                              │  Reward / Cont   │  │
45	 │                                              └──────────────────┘  │
46	 │                                                                      │
47	 └──────────────────────────────────────────────────────────────────────┘
48	
49	Gate supervision (training only):
50	  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)
51	  target: large delta -> small Dt, small delta -> large Dt
52	```
53	
54	---
55	
56	## Module A: Variable-Rate RSSM Modifications
57	
58	### A.1 Core Change: Dt Embedding in GRU Input
59	
60	The RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.
61	
62	**File**: `networks.py`
63	
64	**Constructor changes** (`RSSM.__init__`, lines 14-98):
65	
66	```python
67	# New parameters in __init__ signature:
68	#   max_dt: int = 8          # K, maximum temporal stride
69	#   dt_embed_dim: int = 32   # dimensionality of Dt embedding
70	
71	# After line 46 (self._device = device):
72	self._max_dt = max_dt
73	self._dt_embed_dim = dt_embed_dim
74	self._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)
75	nn.init.normal_(self._dt_embedding.weight, std=0.01)
76	
77	# Modify inp_dim calculation (lines 49-52):
78	# Original:
79	#   if self._discrete:
80	#       inp_dim = self._stoch * self._discrete + num_actions
81	#   else:
82	#       inp_dim = self._stoch + num_actions
83	# New:
84	if self._discrete:
85	    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim
86	else:
87	    inp_dim = self._stoch + num_actions + dt_embed_dim
88	```
89	
90	**`img_step` changes** (lines 208-233):
91	
92	```python
93	def img_step(self, prev_state, prev_action, dt=None, sample=True):
94	    prev_stoch = prev_state["stoch"]
95	    if self._discrete:
96	        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]
97	        prev_stoch = prev_stoch.reshape(shape)
98	
99	    # Dt embedding: default to dt=1 if not provided (backward compat)
100	    if dt is None:
101	        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,
102	                        device=prev_stoch.device)
103	    # dt is 1-indexed {1,...,K}, embedding is 0-indexed
104	    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)
105	
106	    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)
107	    x = self._img_in_layers(x)
108	    for _ in range(self._rec_depth):
109	        deter = prev_state["deter"]
110	        x, deter = self._cell(x, [deter])
111	        deter = deter[0]
112	    x = self._img_out_layers(x)
113	    stats = self._suff_stats_layer("ims", x)
114	    if sample:
115	        stoch = self.get_dist(stats).sample()
116	    else:
117	        stoch = self.get_dist(stats).mode()
118	    prior = {"stoch": stoch, "deter": deter, **stats}
119	    return prior
120	```
121	
122	**`obs_step` changes** (lines 174-206): Pass `dt=None` (defaults to 1) to `img_step` call at line 195. During world model training from replay, Dt is always 1 (we observe every real timestep); variable Dt only applies during imagination.
123	
124	```python
125	# Line 195: prior = self.img_step(prev_state, prev_action)
126	# No change needed if dt defaults to None->1 inside img_step
127	```
128	
129	**`observe` changes** (lines 127-143): No change. Training always uses Dt=1 on real data.
130	
131	**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:
132	
133	```python
134	def imagine_with_action(self, action, state, dt_sequence=None):
135	    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))
136	    action = swap(action)
137	    if dt_sequence is not None:
138	        dt_sequence = swap(dt_sequence)
139	        prior = tools.static_scan(
140	            lambda s, a, dt: self.img_step(s, a, dt=dt),
141	            [action, dt_sequence], state
142	        )
143	    else:
144	        prior = tools.static_scan(self.img_step, [action], state)
145	    prior = prior[0]
146	    prior = {k: swap(v) for k, v in prior.items()}
147	    return prior
148	```
149	
150	### A.2 Config Additions
151	
152	**File**: `configs.yaml`, under `defaults`:
153	
154	```yaml
155	# Event-Gated Adaptive Horizon
156	gate_max_dt: 8              # K: max temporal stride
157	gate_dt_embed_dim: 32       # Dt embedding dimension
158	gate_hidden_units: 256      # gate MLP hidden size
159	gate_hidden_layers: 2       # gate MLP depth
160	gate_tau_init: 1.0          # Gumbel-Softmax initial temperature
161	gate_tau_final: 0.5         # Gumbel-Softmax final temperature
162	gate_tau_anneal_steps: 200000  # linear anneal duration
163	gate_loss_weight: 1.0       # gate supervision loss coefficient
164	gate_entropy_bonus: 0.01    # entropy regularization weight
165	gate_curriculum_phase1: 50000   # forced Dt=1 phase
166	gate_curriculum_phase2: 150000  # linear ramp phase end
167	gate_enabled: false         # master switch
168	```
169	
170	**Hyperparameter search ranges**:
171	
172	| Parameter | Default | Search Range | Notes |
173	|---|---|---|---|
174	| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |
175	| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |
176	| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |
177	| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |
178	| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |
179	| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |
180	| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |
181	
182	### A.3 WorldModel Constructor Wiring
183	
184	**File**: `models.py`, `WorldModel.__init__` (lines 30-101)
185	
186	```python
187	# After line 54 (self.dynamics = networks.RSSM(...)):
188	# Add max_dt and dt_embed_dim to RSSM constructor call:
189	self.dynamics = networks.RSSM(
190	    config.dyn_stoch,
191	    config.dyn_deter,
192	    config.dyn_hidden,
193	    config.dyn_rec_depth,
194	    config.dyn_discrete,
195	    config.act,
196	    config.norm,
197	    config.dyn_mean_act,
198	    config.dyn_std_act,
199	    config.dyn_min_std,
200	    config.unimix_ratio,
201	    config.initial,
202	    config.num_actions,
203	    self.embed_size,
204	    config.device,
205	    max_dt=config.gate_max_dt if config.gate_enabled else 1,
206	    dt_embed_dim=config.gate_dt_embed_dim,
207	)
208	```
209	
210	---
211	
212	## Module B: Event Gate Architecture
213	
214	### B.1 Gate Network
215	
216	**File**: `networks.py` (new class, insert after RSSM class ~line 291)
217	
218	```python
219	class EventGate(nn.Module):
220	    def __init__(
221	        self,
222	        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)
223	        max_dt=8,
224	        hidden_units=256,
225	        hidden_layers=2,
226	        act="SiLU",
227	        norm=True,
228	        tau_init=1.0,
229	        tau_final=0.5,
230	        tau_anneal_steps=200000,
231	    ):
232	        super(EventGate, self).__init__()
233	        self._max_dt = max_dt
234	        self._tau_init = tau_init
235	        self._tau_final = tau_final
236	        self._tau_anneal_steps = tau_anneal_steps
237	
238	        act_fn = getattr(torch.nn, act)
239	        layers = []
240	        inp_dim = feat_size
241	        for i in range(hidden_layers):
242	            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))
243	            if norm:
244	                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))
245	            layers.append(act_fn())
246	            inp_dim = hidden_units
247	        self.mlp = nn.Sequential(*layers)
248	        self.mlp.apply(tools.weight_init)
249	
250	        self.logit_layer = nn.Linear(hidden_units, max_dt)
251	        self.logit_layer.apply(tools.uniform_weight_init(0.01))
252	
253	    def get_tau(self, step):
254	        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)
255	        return self._tau_init + frac * (self._tau_final - self._tau_init)
256	
257	    def forward(self, feat, step, hard=False):
258	        """
259	        Args:
260	            feat: (batch, feat_size) - concatenated [stoch, deter]
261	            step: int - current training step for temperature annealing
262	            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)
263	        Returns:
264	            dt_onehot: (batch, max_dt) - one-hot or soft assignment
265	            dt_index:  (batch,) - integer Dt in {1,...,K}
266	            logits:    (batch, max_dt) - raw logits for entropy computation
267	        """
268	        x = self.mlp(feat)
269	        logits = self.logit_layer(x)  # (batch, max_dt)
270	
271	        tau = self.get_tau(step)
272	        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)
273	
274	        # Dt index: 1-indexed
275	        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)
276	
277	        return dt_onehot, dt_index, logits
278	
279	    def entropy(self, logits):
280	        """Categorical entropy of the gate distribution."""
281	        probs = F.softmax(logits, dim=-1)
282	        log_probs = F.log_softmax(logits, dim=-1)
283	        return -(probs * log_probs).sum(dim=-1)  # (batch,)
284	```
285	
286	### B.2 Gate in Imagination Loop
287	
288	**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)
289	
290	The gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of "wall-clock" steps consumed varies, but the loop always runs `horizon` imagined transitions.
291	
292	```python
293	def _imagine(self, start, policy, horizon):
294	    dynamics = self._world_model.dynamics
295	    gate = self._world_model.event_gate  # added to WorldModel
296	    config = self._config
297	    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))
298	    start = {k: flatten(v) for k, v in start.items()}
299	    step = self._world_model._step
300	
301	    # Determine if gate is active based on curriculum
302	    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)
303	
304	    def step_fn(prev, _):
305	        state, _, _, prev_dt = prev
306	        feat = dynamics.get_feat(state)
307	        inp = feat.detach()
308	        action = policy(inp).sample()
309	
310	        # Use previous gate decision as Dt for this transition
311	        succ = dynamics.img_step(state, action, dt=prev_dt)
312	        succ_feat = dynamics.get_feat(succ)
313	
314	        # Gate decides Dt for the NEXT step
315	        if gate_active:
316	            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)
317	        else:
318	            batch_size = succ_feat.shape[0]
319	            next_dt = torch.ones(batch_size, dtype=torch.long,
320	                                 device=succ_feat.device)
321	            gate_logits = None
322	
323	        return succ, feat, action, next_dt
324	
325	    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],
326	                         dtype=torch.long, device=config.device)
327	
328	    succ, feats, actions, dts = tools.static_scan(
329	        step_fn, [torch.arange(horizon)],
330	        (start, None, None, init_dt)
331	    )
332	    states = {k: torch.cat([start[k][None], v[:-1]], 0)
333	              for k, v in succ.items()}
334	
335	    return feats, states, actions, dts  # dts: (horizon, batch)
336	```
337	
338	### B.3 Registering Gate in WorldModel
339	
340	**File**: `models.py`, `WorldModel.__init__` (after line 86):
341	
342	```python
343	if config.gate_enabled:
344	    self.event_gate = networks.EventGate(
345	        feat_size=feat_size,
346	        max_dt=config.gate_max_dt,
347	        hidden_units=config.gate_hidden_units,
348	        hidden_layers=config.gate_hidden_layers,
349	        act=config.act,
350	        norm=config.norm,
351	        tau_init=config.gate_tau_init,
352	        tau_final=config.gate_tau_final,
353	        tau_anneal_steps=config.gate_tau_anneal_steps,
354	    )
355	else:
356	    self.event_gate = None
357	```
358	
359	---
360	
361	## Module C: Gate Supervision
362	
363	### C.1 Supervision Signal
364	
365	The gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).
366	
367	**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.
368	
369	```python
370	def compute_gate_targets(feats, max_dt):
371	    """
372	    Args:
373	        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features
374	    Returns:
375	        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt
376	    """
377	    feats = feats.detach()  # stop gradient
378	
379	    # L2 delta between consecutive states
380	    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)
381	
382	    # Normalize deltas to [0, 1] within each batch
383	    delta_min = deltas.min(dim=0, keepdim=True).values
384	    delta_max = deltas.max(dim=0, keepdim=True).values
385	    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)
386	
387	    # Large delta -> small Dt (index 0 = Dt=1)
388	    # Small delta -> large Dt (index K-1 = Dt=K)
389	    # Map normalized delta to a "preferred Dt" float in [1, K]
390	    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)
391	
392	    # Create soft target via Gaussian kernel around preferred_dt
393	    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,
394	                              device=feats.device)  # (max_dt,)
395	    # (time-1, batch, 1) vs (max_dt,)
396	    sigma = 1.0
397	    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2
398	    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)
399	
400	    return target_dist
401	```
402	
403	### C.2 Gate Loss
404	
405	```python
406	def gate_loss(gate_logits, target_dist):
407	    """
408	    Cross-entropy between gate's predicted distribution and supervision target.
409	
410	    Args:
411	        gate_logits: (time-1, batch, max_dt) - raw gate logits
412	        target_dist: (time-1, batch, max_dt) - soft target from state deltas
413	    Returns:
414	        loss: (time-1, batch) - per-step per-batch loss
415	    """
416	    log_probs = F.log_softmax(gate_logits, dim=-1)
417	    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy
418	    return loss
419	```
420	
421	### C.3 Integration in WorldModel._train
422	
423	**File**: `models.py`, `WorldModel._train` (lines 108-174)
424	
425	The gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).
426	
427	```python
428	# After line 147 (model_loss = sum(scaled.values()) + kl_loss):
429	
430	if self._config.gate_enabled and self.event_gate is not None:
431	    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM
432	    # Run gate on each timestep's features
433	    # feat shape: (batch, time, feat_dim)
434	    B, T, D = feat.shape
435	    feat_flat = feat.reshape(B * T, D)
436	    _, _, gate_logits_flat = self.event_gate(
437	        feat_flat, self._step, hard=False
438	    )
439	    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)
440	
441	    # Supervision target from state deltas (time dim = axis 1)
442	    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)
443	    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)
444	    # target_dist: (time-1, batch, max_dt)
445	
446	    # Gate logits for steps 1..T-1 (we need t and t-1)
447	    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)
448	
449	    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)
450	
451	    # Entropy bonus
452	    g_entropy = self.event_gate.entropy(
453	        g_logits.reshape(-1, self._config.gate_max_dt)
454	    ).reshape(g_loss.shape)
455	
456	    # Curriculum: scale gate loss
457	    step = self._step
458	    if step < self._config.gate_curriculum_phase1:
459	        gate_scale = 0.0  # Phase 1: no gate training
460	    elif step < self._config.gate_curriculum_phase2:
461	        # Phase 2: linear ramp
462	        progress = (step - self._config.gate_curriculum_phase1) / (
463	            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1
464	        )
465	        gate_scale = progress
466	    else:
467	        gate_scale = 1.0  # Phase 3: full gate
468	
469	    total_gate_loss = gate_scale * (
470	        self._config.gate_loss_weight * g_loss.mean()
471	        - self._config.gate_entropy_bonus * g_entropy.mean()
472	    )
473	    model_loss = model_loss + total_gate_loss
474	```
475	
476	### C.4 Stop-Gradient Design
477	
478	Critical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.
479	
480	- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input
481	- `target_dist` uses `feats.detach()` internally
482	- Only `self.event_gate` parameters receive gradients from gate loss
483	- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads
484	
485	---
486	
487	## Module D: Adapted Lambda-Returns
488	
489	### D.1 Standard vs. Adapted Lambda-Return
490	
491	**Standard** (from `tools.py:691-717`):
492	
493	$$V_t^\lambda = r_{t+1} + \gamma \left[(1-\lambda) V(s_{t+1}) + \lambda V_{t+1}^\lambda\right]$$
494	
495	**Adapted for variable Dt**:
496	
497	$$V_t^\lambda = r_{t:t+\Delta t}^{\text{cum}} + \gamma^{\Delta t} \left[(1-\lambda) V(s_{t+\Delta t}) + \lambda V_{t+\Delta t}^\lambda\right]$$
498	
499	where:
500	- $r_{t:t+\Delta t}^{\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)
501	- $\gamma^{\Delta t}$: discount raised to the power of the stride
502	
503	### D.2 Modified lambda_return
504	
505	**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):
506	
507	```python
508	def lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):
509	    """
510	    Lambda-return with variable temporal strides.
511	
512	    Args:
513	        reward: (time, batch, 1) - per-step imagined reward
514	        value:  (time, batch, 1) - value estimates
515	        pcont:  (time, batch, 1) - continuation probability * base discount
516	        dt:     (time, batch) or (time, batch, 1) - temporal stride per step
517	        bootstrap: (batch, 1) - terminal value
518	        lambda_: float
519	        axis: int
520	    Returns:
521	        returns: list of (batch, 1) tensors
522	    """
523	    assert len(reward.shape) == len(value.shape)
524	    if isinstance(pcont, (int, float)):
525	        pcont = pcont * torch.ones_like(reward)
526	    if dt.dim() == 2:
527	        dt = dt.unsqueeze(-1)  # (time, batch, 1)
528	    dt = dt.float()
529	
530	    dims = list(range(len(reward.shape)))
531	    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]
532	    if axis != 0:
533	        reward = reward.permute(dims)
534	        value = value.permute(dims)
535	        pcont = pcont.permute(dims)
536	        dt = dt.permute(dims)
537	
538	    if bootstrap is None:
539	        bootstrap = torch.zeros_like(value[-1])
540	
541	    # Adjust reward and discount for variable Dt:
542	    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)
543	    reward_adj = reward * dt
544	    # gamma^Dt
545	    pcont_adj = pcont ** dt
546	
547	    next_values = torch.cat([value[1:], bootstrap[None]], 0)
548	    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)
549	
550	    returns = static_scan_for_lambda_return(
551	        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
552	        (inputs, pcont_adj), bootstrap
553	    )
554	    if axis != 0:
555	        returns = returns.permute(dims)
556	    return returns
557	```
558	
559	### D.3 Integration in ImagBehavior._compute_target
560	
561	**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):
562	
563	```python
564	def _compute_target(self, imag_feat, imag_state, reward, dts=None):
565	    if "cont" in self._world_model.heads:
566	        inp = self._world_model.dynamics.get_feat(imag_state)
567	        discount = self._config.discount * self._world_model.heads["cont"](inp).mean
568	    else:
569	        discount = self._config.discount * torch.ones_like(reward)
570	    value = self.value(imag_feat).mode()
571	
572	    if dts is not None and self._config.gate_enabled:
573	        target = tools.lambda_return_variable_dt(
574	            reward[1:],
575	            value[:-1],
576	            discount[1:],
577	            dts[1:],  # Dt for each imagined step
578	            bootstrap=value[-1],
579	            lambda_=self._config.discount_lambda,
580	            axis=0,
581	        )
582	    else:
583	        target = tools.lambda_return(
584	            reward[1:],
585	            value[:-1],
586	            discount[1:],
587	            bootstrap=value[-1],
588	            lambda_=self._config.discount_lambda,
589	            axis=0,
590	        )
591	
592	    # Adjusted weights: cumulative discount accounts for variable Dt
593	    if dts is not None and self._config.gate_enabled:
594	        pcont_adj = discount ** dts.unsqueeze(-1).float()
595	        weights = torch.cumprod(
596	            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0
597	        ).detach()
598	    else:
599	        weights = torch.cumprod(
600	            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0
601	        ).detach()
602	
603	    return target, weights, value[:-1]
604	```
605	
606	### D.4 Reward Accumulation Approximation
607	
608	In imagination, we don't have access to intermediate rewards between skipped steps. Two options:
609	
610	1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.
611	
612	2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.
613	
614	We use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).
615	
616	---
617	
618	## Module E: Gate Collapse Prevention
619	
620	### E.1 Failure Modes
621	
622	Gate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.
623	
624	### E.2 Entropy Regularization
625	
626	Already included in Module C's loss:
627	
628	```python
629	total_gate_loss = gate_scale * (
630	    config.gate_loss_weight * g_loss.mean()
631	    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy
632	)
633	```
634	
635	The entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.
636	
637	### E.3 Gating Curriculum (Three Phases)
638	
639	| Phase | Steps | Behavior | Rationale |
640	|---|---|---|---|
641	| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |
642	| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |
643	| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |
644	
645	Implementation (already shown in Module C.3):
646	
647	```python
648	if step < config.gate_curriculum_phase1:
649	    gate_scale = 0.0
650	elif step < config.gate_curriculum_phase2:
651	    progress = (step - config.gate_curriculum_phase1) / (
652	        config.gate_curriculum_phase2 - config.gate_curriculum_phase1
653	    )
654	    gate_scale = progress
655	else:
656	    gate_scale = 1.0
657	```
658	
659	In `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.
660	
661	### E.4 Collapse Detection Metrics
662	
663	**File**: `models.py`, add to metrics in `ImagBehavior._train`:
664	
665	```python
666	if self._config.gate_enabled and dts is not None:
667	    dts_float = dts.float()
668	    metrics["gate_dt_mean"] = to_np(torch.mean(dts_float))
669	    metrics["gate_dt_std"] = to_np(torch.std(dts_float))
670	    metrics["gate_dt_min"] = to_np(torch.min(dts_float))
671	    metrics["gate_dt_max"] = to_np(torch.max(dts_float))
672	
673	    # Distribution over K bins
674	    dt_counts = torch.bincount(
675	        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1
676	    )[1:]  # skip bin 0
677	    dt_dist = dt_counts.float() / dt_counts.sum()
678	    for k in range(self._config.gate_max_dt):
679	        metrics[f"gate_dt_{k+1}_frac"] = to_np(dt_dist[k])
680	
681	    # Entropy of empirical Dt distribution (collapse indicator)
682	    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()
683	    metrics["gate_empirical_entropy"] = to_np(emp_entropy)
684	    max_entropy = np.log(self._config.gate_max_dt)
685	    metrics["gate_entropy_ratio"] = to_np(emp_entropy) / max_entropy
686	```
687	
688	**Collapse alert thresholds**:
689	- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values
690	- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed
691	- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating
692	- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates
693	
694	### E.5 Automatic Recovery (Optional)
695	
696	If collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:
697	
698	```python
699	if gate_entropy_ratio < 0.2:
700	    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost
701	else:
702	    effective_entropy_bonus = config.gate_entropy_bonus
703	```
704	
705	This is optional and aggressive. Prefer tuning the base entropy bonus instead.
706	
707	---
708	
709	## Module F: Replay Buffer Subsampling Strategy
710	
711	### F.1 Problem Statement
712	
713	The world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.
714	
715	However, to train the RSSM to understand what "Dt=3" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.
716	
717	### F.2 Strategy 1: Post-Sampling Temporal Skip
718	
719	After sampling a standard `(batch_size, batch_length)` sequence from replay:
720	1. For a fraction of batch elements, randomly select skip patterns
721	2. Index into the sequence to create variable-rate subsequences
722	3. Train RSSM with corresponding Dt labels
723	
724	```python
725	def apply_temporal_skip(data, max_dt, skip_prob=0.3):
726	    """
727	    Args:
728	        data: dict of (batch, time, ...) tensors from replay
729	        max_dt: int
730	        skip_prob: probability of applying skip to each batch element
731	    Returns:
732	        data_skipped: dict with same batch dim but potentially shorter time dim
733	        dt_labels: (batch, time') tensor of Dt values used
734	    """
735	    B, T = data["action"].shape[:2]
736	    dt_labels = torch.ones(B, T, dtype=torch.long)
737	
738	    for b in range(B):
739	        if random.random() < skip_prob:
740	            t = 0
741	            indices = [0]
742	            while t < T - 1:
743	                dt = random.randint(1, min(max_dt, T - 1 - t))
744	                t += dt
745	                indices.append(t)
746	                dt_labels[b, len(indices) - 1] = dt
747	            # Subsample this batch element
748	            for key in data:
749	                data[key][b] = data[key][b, indices]
750	    return data, dt_labels
751	```
752	
753	**Pros**: Simple, no replay buffer changes.
754	**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.
755	
756	### F.3 Strategy 2: Precomputed Variable-Rate Subsequences
757	
758	At episode storage time, precompute and store multiple temporal resolutions:
759	- For each episode, generate several subsampled versions with different skip patterns
760	- Store cumulated rewards for skipped intervals
761	- Sample from this augmented dataset
762	
763	**Pros**: Efficient at training time; exact reward cumulation.
764	**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.
765	
766	### F.4 Recommended Approach: Strategy 1 with Modifications
767	
768	Strategy 1, but only applied to a separate "gate training" phase within each world model update:
769	
770	```python
771	# In WorldModel._train, after standard RSSM training:
772	if self._config.gate_enabled:
773	    # Sample a separate batch for gate-aware RSSM fine-tuning
774	    # Standard RSSM loss on full-rate data (as before)
775	    # Gate supervision on the same full-rate data (state deltas)
776	    # No need to actually skip in replay -- the gate learns from
777	    # observing which states are "skippable" in the full-rate stream
778	```
779	
780	**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means "predict what happens if I advance 3 steps." The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.
781	
782	The RSSM can generalize to larger Dt because:
783	1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)
784	2. The GRU learns to scale its update magnitude based on Dt_emb
785	3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable
786	
787	**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.
788	
789	---
790	
791	## File Modification Summary
792	
793	| File | Function/Class | Lines | Change Type |
794	|---|---|---|---|
795	| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |
796	| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |
797	| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |
798	| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |
799	| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |
800	| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |
801	| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |
802	| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |
803	| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |
804	| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |
805	| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |
806	| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |
807	
808	---
809	
810	## Risks and Mitigations
811	
812	### R1: Training Instability
813	
814	**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.
815	
816	**Mitigation**:
817	- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible
818	- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate
819	- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences
820	
821	### R2: Gate Collapse
822	
823	**Risk**: Gate degenerates to constant Dt, losing adaptivity.
824	
825	**Mitigation**:
826	- Entropy regularization in gate loss
827	- Curriculum prevents premature commitment
828	- Monitoring metrics with alert thresholds (Section E.4)
829	- Gumbel-Softmax temperature annealing ensures exploration early on
830	
831	### R3: Reward Approximation Error
832	
833	**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.
834	
835	**Mitigation**:
836	- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance
837	- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small
838	- Monitor `imag_reward` statistics for anomalies
839	
840	### R4: Compatibility with Original DreamerV3
841	
842	**Risk**: Modified code breaks when `gate_enabled=false`.
843	
844	**Mitigation**:
845	- All gate logic is guarded by `config.gate_enabled`
846	- `img_step` defaults `dt=None` which maps to Dt=1
847	- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)
848	- `_compute_target` falls back to standard `lambda_return`
849	- Net-zero change to behavior when `gate_enabled=false`
850	
851	### R5: Computational Overhead
852	
853	**Risk**: Gate MLP adds forward-pass cost in imagination.
854	
855	**Mitigation**:
856	- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)
857	- Gate is only called during imagination (not observation/training unroll)
858	- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute
859	
860	### R6: Replay Buffer Efficiency
861	
862	**Risk**: Strategy 1 subsampling wastes loaded data.
863	
864	**Mitigation**:
865	- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.
866	- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the "wasted" frames still contributed to the standard RSSM loss before subsampling.
867	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "b3723576-9074-4fba-bc24-965de77f3c71",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
      "content": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): Pass `dt=None` (defaults to 1) to `img_step` call at line 195. During world model training from replay, Dt is always 1 (we observe every real timestep); variable Dt only applies during imagination.\n\n```python\n# Line 195: prior = self.img_step(prev_state, prev_action)\n# No change needed if dt defaults to None->1 inside img_step\n```\n\n**`observe` changes** (lines 127-143): No change. Training always uses Dt=1 on real data.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 1.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=1.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Adjust reward and discount for variable Dt:\n    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)\n    reward_adj = reward * dt\n    # gamma^Dt\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n### D.4 Reward Accumulation Approximation\n\nIn imagination, we don't have access to intermediate rewards between skipped steps. Two options:\n\n1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.\n\n2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.\n\nWe use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
      "numLines": 867,
      "startLine": 1,
      "totalLines": 867
    }
  }
}
````

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the document. Let me plan all the edits needed:

1. **偏差 1: Module F (Replay Buffer)** - Complete rewrite of section F
2. **偏差 2: Module D (Reward)** - Fix reward accumulation, modify D.1, D.2, D.4
3. **偏差 3: Gumbel-Softmax temperature** - τ_init=1.0 → 5.0 in multiple places
4. **额外修正 1**: Module A obs_step needs to accept dt parameter


5. **额外修正 3**: File Modification Summary table update

Starting with the simplest changes first: I need to update the Gumbel-Softmax temperature parameter from 1.0 to 5.0 at lines 160 and 228, while line 352 already references the config correctly. Then I'll tackle the complete rewrite of Module F from lines 709-787, followed by the reward accumulation fixes in Module D across sections D.1, D.2, and D.4.

For Module A, I need to update the obs_step function to accept a dt parameter at lines 122-127. I'm grouping these edits by independence—the tau_init changes and Module F rewrite can happen in parallel since they don't affect each other, then I'll move through the Module D updates and the obs_step modification.

Let me map out each change precisely: updating gate_tau_init from 1.0 to 5.0 in the configs, changing tau_init in the EventGate class initialization, modifying the obs_step signature, and handling the Module D sections including the formula description fix, the reward_adj line correction, and deleting D.4 entirely. I'm working through the edits systematically, starting with the string replacements. For Edit 3, I need to update the `obs_step` explanation to clarify that it accepts an optional `dt` parameter and passes it to `img_step`, since during variable-Δt training the RSSM processes sub-sampled trajectories where Δt can be greater than 1.

Now I'm moving to Edit 4, which involves adapting the value function computation for variable time steps. Now I need to fix the reward handling in Module D.2 — since the reward head is already trained to predict cumulative rewards during sub-sampling, I can remove the approximation scaling and use the reward value directly, along with adjusting the discount factor for the variable stride.

For Edit 6, I'm removing the entire D.4 section about reward accumulation approximation since it's no longer needed with this approach.

For Edit 7, I need to rewrite Module F completely to explain the new sub-sampling and cumulative reward computation method.

For Edit 8, I'll update the file modification summary table to reflect all these changes.

For Edits 9, I need to revisit risks R3 and R6 to account for how the new approach handles them differently.

Let me work through these edits in order since they're all in the same document and depend on each other.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "2f450c98-51dc-4f7b-bddc-0171b9154986",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTFXe6PbFCUmJeW5gX7SVi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12987,
      "cache_read_input_tokens": 24051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12987
      },
      "output_tokens": 12,
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

_source line 9_

文档已读取完毕，共 867 行。现在开始逐个修正。

先做几个独立的简单修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "7d87b7c1-663b-48c3-b009-4e3b00a8eac2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTFXe6PbFCUmJeW5gX7SVi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12987,
      "cache_read_input_tokens": 24051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12987
      },
      "output_tokens": 12,
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

_source line 10_

<details open><summary>🔧 Tool call — Edit · `toolu_01ThQw4BtTRCiWk6AWhc5ey6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "gate_tau_init: 1.0          # Gumbel-Softmax initial temperature",
  "new_string": "gate_tau_init: 5.0          # Gumbel-Softmax initial temperature"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "e21031e1-9783-49bc-b973-3fa46943f96c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTFXe6PbFCUmJeW5gX7SVi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12987,
      "cache_read_input_tokens": 24051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12987
      },
      "output_tokens": 12,
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

_source line 11 · 2026-05-13T01:17:17.231Z_

<details><summary>↩ Tool result · `toolu_01ThQw4BtTRCiWk6AWhc5ey6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "d9747a88-a32c-4f88-902a-d96a2a400c0a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "gate_tau_init: 1.0          # Gumbel-Softmax initial temperature",
    "newString": "gate_tau_init: 5.0          # Gumbel-Softmax initial temperature",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): Pass `dt=None` (defaults to 1) to `img_step` call at line 195. During world model training from replay, Dt is always 1 (we observe every real timestep); variable Dt only applies during imagination.\n\n```python\n# Line 195: prior = self.img_step(prev_state, prev_action)\n# No change needed if dt defaults to None->1 inside img_step\n```\n\n**`observe` changes** (lines 127-143): No change. Training always uses Dt=1 on real data.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 1.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=1.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Adjust reward and discount for variable Dt:\n    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)\n    reward_adj = reward * dt\n    # gamma^Dt\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n### D.4 Reward Accumulation Approximation\n\nIn imagination, we don't have access to intermediate rewards between skipped steps. Two options:\n\n1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.\n\n2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.\n\nWe use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
    "structuredPatch": [
      {
        "oldStart": 157,
        "oldLines": 7,
        "newStart": 157,
        "newLines": 7,
        "lines": [
          " gate_dt_embed_dim: 32       # Dt embedding dimension",
          " gate_hidden_units: 256      # gate MLP hidden size",
          " gate_hidden_layers: 2       # gate MLP depth",
          "-gate_tau_init: 1.0          # Gumbel-Softmax initial temperature",
          "+gate_tau_init: 5.0          # Gumbel-Softmax initial temperature",
          " gate_tau_final: 0.5         # Gumbel-Softmax final temperature",
          " gate_tau_anneal_steps: 200000  # linear anneal duration",
          " gate_loss_weight: 1.0       # gate supervision loss coefficient"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Edit · `toolu_012BzsZfZAF3ASmnELQTjokL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "        tau_init=1.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()",
  "new_string": "        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "9497f9fc-6fec-478a-8e39-598519220f26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPJtuZ38EfbxcRAFRcvzWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 37038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2517
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

_source line 13 · 2026-05-13T01:17:25.537Z_

<details><summary>↩ Tool result · `toolu_012BzsZfZAF3ASmnELQTjokL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "a9649491-1f48-4790-84c5-424fcddae35c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "        tau_init=1.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()",
    "newString": "        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): Pass `dt=None` (defaults to 1) to `img_step` call at line 195. During world model training from replay, Dt is always 1 (we observe every real timestep); variable Dt only applies during imagination.\n\n```python\n# Line 195: prior = self.img_step(prev_state, prev_action)\n# No change needed if dt defaults to None->1 inside img_step\n```\n\n**`observe` changes** (lines 127-143): No change. Training always uses Dt=1 on real data.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=1.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Adjust reward and discount for variable Dt:\n    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)\n    reward_adj = reward * dt\n    # gamma^Dt\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n### D.4 Reward Accumulation Approximation\n\nIn imagination, we don't have access to intermediate rewards between skipped steps. Two options:\n\n1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.\n\n2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.\n\nWe use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
    "structuredPatch": [
      {
        "oldStart": 225,
        "oldLines": 7,
        "newStart": 225,
        "newLines": 7,
        "lines": [
          "         hidden_layers=2,",
          "         act=\"SiLU\",",
          "         norm=True,",
          "-        tau_init=1.0,",
          "+        tau_init=5.0,",
          "         tau_final=0.5,",
          "         tau_anneal_steps=200000,",
          "     ):"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 14_

偏差 3 已修正。现在修正 Module A 的 obs_step（额外修正 1）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "11c989c4-5a04-4ffe-a54e-adc77b58d931",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqpAuePZr9isimSaYLjBM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 39555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 293
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01DZZnGr45G8J4F86w3Fhoqb`</summary>

````json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "**`obs_step` changes** (lines 174-206): Pass `dt=None` (defaults to 1) to `img_step` call at line 195. During world model training from replay, Dt is always 1 (we observe every real timestep); variable Dt only applies during imagination.\n\n```python\n# Line 195: prior = self.img_step(prev_state, prev_action)\n# No change needed if dt defaults to None->1 inside img_step\n```\n\n**`observe` changes** (lines 127-143): No change. Training always uses Dt=1 on real data.",
  "new_string": "**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`."
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "996939d8-793f-4c99-b3ed-3d845ecf4543",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqpAuePZr9isimSaYLjBM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 39555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 293
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

_source line 16 · 2026-05-13T01:17:37.840Z_

<details><summary>↩ Tool result · `toolu_01DZZnGr45G8J4F86w3Fhoqb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "f4e4f572-b146-4280-b40e-41f5c82f5aac",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "**`obs_step` changes** (lines 174-206): Pass `dt=None` (defaults to 1) to `img_step` call at line 195. During world model training from replay, Dt is always 1 (we observe every real timestep); variable Dt only applies during imagination.\n\n```python\n# Line 195: prior = self.img_step(prev_state, prev_action)\n# No change needed if dt defaults to None->1 inside img_step\n```\n\n**`observe` changes** (lines 127-143): No change. Training always uses Dt=1 on real data.",
    "newString": "**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): Pass `dt=None` (defaults to 1) to `img_step` call at line 195. During world model training from replay, Dt is always 1 (we observe every real timestep); variable Dt only applies during imagination.\n\n```python\n# Line 195: prior = self.img_step(prev_state, prev_action)\n# No change needed if dt defaults to None->1 inside img_step\n```\n\n**`observe` changes** (lines 127-143): No change. Training always uses Dt=1 on real data.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Adjust reward and discount for variable Dt:\n    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)\n    reward_adj = reward * dt\n    # gamma^Dt\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n### D.4 Reward Accumulation Approximation\n\nIn imagination, we don't have access to intermediate rewards between skipped steps. Two options:\n\n1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.\n\n2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.\n\nWe use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
    "structuredPatch": [
      {
        "oldStart": 119,
        "oldLines": 14,
        "newStart": 119,
        "newLines": 17,
        "lines": [
          "     return prior",
          " ```",
          " ",
          "-**`obs_step` changes** (lines 174-206): Pass `dt=None` (defaults to 1) to `img_step` call at line 195. During world model training from replay, Dt is always 1 (we observe every real timestep); variable Dt only applies during imagination.",
          "+**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.",
          " ",
          " ```python",
          "-# Line 195: prior = self.img_step(prev_state, prev_action)",
          "-# No change needed if dt defaults to None->1 inside img_step",
          "+def obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):",
          "+    # ... (existing reset / mask logic unchanged) ...",
          "+    prior = self.img_step(prev_state, prev_action, dt=dt)",
          "+    # ... (existing posterior computation unchanged) ...",
          "+    return post, prior",
          " ```",
          " ",
          "-**`observe` changes** (lines 127-143): No change. Training always uses Dt=1 on real data.",
          "+**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.",
          " ",
          " **`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 17_

修正 Module D.1 的公式说明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "e078eefa-e74a-49c2-9fbb-44fe5dd38e44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GA7bRqXm2XHRjohA21WfkP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 581,
      "cache_read_input_tokens": 39848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 581
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01X5PSuk7tFN75HMWZ9MDmQ2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "where:\n- $r_{t:t+\\Delta t}^{\\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride",
  "new_string": "where:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "27f7d03f-ba8b-420a-9c7b-93e97bfb373d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GA7bRqXm2XHRjohA21WfkP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 581,
      "cache_read_input_tokens": 39848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 581
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

_source line 19 · 2026-05-13T01:17:45.478Z_

<details><summary>↩ Tool result · `toolu_01X5PSuk7tFN75HMWZ9MDmQ2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "6ce0b9ad-7934-4efd-bce8-2ba9ed73cf77",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "where:\n- $r_{t:t+\\Delta t}^{\\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride",
    "newString": "where:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Adjust reward and discount for variable Dt:\n    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)\n    reward_adj = reward * dt\n    # gamma^Dt\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n### D.4 Reward Accumulation Approximation\n\nIn imagination, we don't have access to intermediate rewards between skipped steps. Two options:\n\n1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.\n\n2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.\n\nWe use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
    "structuredPatch": [
      {
        "oldStart": 500,
        "oldLines": 7,
        "newStart": 500,
        "newLines": 7,
        "lines": [
          " $$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$",
          " ",
          " where:",
          "-- $r_{t:t+\\Delta t}^{\\text{cum}}$: cumulated reward over Dt skipped steps (in imagination, the reward head predicts a single reward for the jumped state; we scale it by Dt as an approximation)",
          "+- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.",
          " - $\\gamma^{\\Delta t}$: discount raised to the power of the stride",
          " ",
          " ### D.2 Modified lambda_return"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 20_

修正 Module D.2 的 lambda_return 函数——去掉 `reward * dt` 近似。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "71e16b3b-77de-42ef-9ad3-6fe341936bc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtZMo7ogwbNWQjAudhn6dj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 403,
      "cache_read_input_tokens": 40429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 403
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01MoXgocVUwta2wnH6qDuX1m`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "    # Adjust reward and discount for variable Dt:\n    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)\n    reward_adj = reward * dt\n    # gamma^Dt\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)",
  "new_string": "    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),\n    # so use it directly. gamma^Dt for the discount:\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "855328f3-06bb-4f0f-a3a3-b6798c37c2c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtZMo7ogwbNWQjAudhn6dj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 403,
      "cache_read_input_tokens": 40429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 403
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

_source line 22 · 2026-05-13T01:17:53.585Z_

<details><summary>↩ Tool result · `toolu_01MoXgocVUwta2wnH6qDuX1m`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "af5e0aa8-c557-45d5-b98b-7db255259e48",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "    # Adjust reward and discount for variable Dt:\n    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)\n    reward_adj = reward * dt\n    # gamma^Dt\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)",
    "newString": "    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),\n    # so use it directly. gamma^Dt for the discount:\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Adjust reward and discount for variable Dt:\n    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)\n    reward_adj = reward * dt\n    # gamma^Dt\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n### D.4 Reward Accumulation Approximation\n\nIn imagination, we don't have access to intermediate rewards between skipped steps. Two options:\n\n1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.\n\n2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.\n\nWe use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
    "structuredPatch": [
      {
        "oldStart": 541,
        "oldLines": 14,
        "newStart": 541,
        "newLines": 12,
        "lines": [
          "     if bootstrap is None:",
          "         bootstrap = torch.zeros_like(value[-1])",
          " ",
          "-    # Adjust reward and discount for variable Dt:",
          "-    # r_cum ~= r * Dt  (approximation: reward head predicts per-step reward)",
          "-    reward_adj = reward * dt",
          "-    # gamma^Dt",
          "+    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),",
          "+    # so use it directly. gamma^Dt for the discount:",
          "     pcont_adj = pcont ** dt",
          " ",
          "     next_values = torch.cat([value[1:], bootstrap[None]], 0)",
          "-    inputs = reward_adj + pcont_adj * next_values * (1 - lambda_)",
          "+    inputs = reward + pcont_adj * next_values * (1 - lambda_)",
          " ",
          "     returns = static_scan_for_lambda_return(",
          "         lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 23_

删除 D.4 整节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "5072f389-c055-47d3-9986-d9ec3cf2b0aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAQj4TciEzRYsbjYATUJBB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 40832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 538
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

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01V31VWigLAJtMBK2WZNoot9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "### D.4 Reward Accumulation Approximation\n\nIn imagination, we don't have access to intermediate rewards between skipped steps. Two options:\n\n1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.\n\n2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.\n\nWe use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).\n\n---",
  "new_string": "---"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "88450f82-d837-429b-a7c3-d4f8fb3bbea2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAQj4TciEzRYsbjYATUJBB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 40832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 538
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

_source line 25 · 2026-05-13T01:18:02.801Z_

<details><summary>↩ Tool result · `toolu_01V31VWigLAJtMBK2WZNoot9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "95a0425f-553a-411f-9a30-600bdef3df87",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "### D.4 Reward Accumulation Approximation\n\nIn imagination, we don't have access to intermediate rewards between skipped steps. Two options:\n\n1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.\n\n2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.\n\nWe use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).\n\n---",
    "newString": "---",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),\n    # so use it directly. gamma^Dt for the discount:\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n### D.4 Reward Accumulation Approximation\n\nIn imagination, we don't have access to intermediate rewards between skipped steps. Two options:\n\n1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.\n\n2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.\n\nWe use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
    "structuredPatch": [
      {
        "oldStart": 604,
        "oldLines": 16,
        "newStart": 604,
        "newLines": 6,
        "lines": [
          "     return target, weights, value[:-1]",
          " ```",
          " ",
          "-### D.4 Reward Accumulation Approximation",
          "-",
          "-In imagination, we don't have access to intermediate rewards between skipped steps. Two options:",
          "-",
          "-1. **Scale approximation** (recommended, simpler): `r_cum = r_predicted * Dt`. The reward head predicts reward at the landed state; multiplying by Dt approximates cumulation assuming roughly constant reward rate.",
          "-",
          "-2. **Multi-step unroll** (expensive): Actually unroll Dt sub-steps with Dt=1 to sum rewards, then only keep the final state. This is accurate but defeats the purpose of skipping.",
          "-",
          "-We use option 1. The approximation error is bounded when reward is smooth, which is the regime where large Dt is appropriate (gate should learn large Dt only for low-variance reward regions).",
          "-",
          " ---",
          " ",
          " ## Module E: Gate Collapse Prevention"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 26_

重写 Module F。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "f7d09059-b92a-4bee-b739-683825530e88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYSzdBLa6RjDcUN4Wxw8p8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 41370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 392
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_0199saHyYAzmMT1Wfhx2URp2`</summary>

````json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.",
  "new_string": "## Module F: Variable-Δt Replay Sub-Sampling\n\n### F.1 Motivation\n\nTo teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.\n\n### F.2 Sub-Sampling Procedure\n\nFor each training batch:\n\n1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.\n2. For each batch element, independently draw a stride from a **log-uniform distribution**:\n   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).\n3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.\n4. For each gap of Δt frames, compute:\n   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`\n   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`\n5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).\n\nWithin a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.\n\n### F.3 Implementation\n\n**File**: `tools.py` (new function)\n\n```python\ndef subsample_variable_dt(data, max_dt, discount):\n    \"\"\"\n    Variable-Δt sub-sampling of replay trajectories.\n\n    Args:\n        data: dict of (batch, time, ...) tensors — must include\n              'action', 'reward', 'cont' (and observation keys).\n        max_dt: int — K, maximum temporal stride.\n        discount: float — γ, environment discount factor.\n    Returns:\n        data_sub: dict of (batch, time', ...) sub-sampled tensors.\n        dt_labels: (batch, time') int tensor, stride used per step.\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    # Sample per-element Δt from log-uniform over [1, K]\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)\n\n    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))\n    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    # Build index and aggregate tensors\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        # Sub-sample observation / action tensors\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        # Cumulative discounted reward and min continuation\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            gamma_powers = discount ** torch.arange(\n                t_end - t_start, dtype=torch.float, device=device\n            )\n            reward_cum[b, i] = (\n                gamma_powers.unsqueeze(-1) * data[\"reward\"][b, t_start:t_end]\n            ).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n```\n\n### F.4 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train`\n\n```python\n# Before calling self.dynamics.observe():\nif self._config.gate_enabled:\n    data, dt_labels = tools.subsample_variable_dt(\n        data, self._config.gate_max_dt, self._config.discount,\n    )\n    # dt_labels: (batch, time') — passed to observe → obs_step → img_step\nelse:\n    dt_labels = None\n```\n\nThe `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).\n\n### F.5 Design Notes\n\n- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.\n- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.\n- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.\n- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal."
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "13a2f35f-6540-4637-a705-18dc51c5f396",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYSzdBLa6RjDcUN4Wxw8p8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 41370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 392
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

_source line 28 · 2026-05-13T01:19:04.795Z_

<details><summary>↩ Tool result · `toolu_0199saHyYAzmMT1Wfhx2URp2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "5bed1e5b-0a86-4738-babd-00e6035619fb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.",
    "newString": "## Module F: Variable-Δt Replay Sub-Sampling\n\n### F.1 Motivation\n\nTo teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.\n\n### F.2 Sub-Sampling Procedure\n\nFor each training batch:\n\n1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.\n2. For each batch element, independently draw a stride from a **log-uniform distribution**:\n   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).\n3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.\n4. For each gap of Δt frames, compute:\n   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`\n   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`\n5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).\n\nWithin a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.\n\n### F.3 Implementation\n\n**File**: `tools.py` (new function)\n\n```python\ndef subsample_variable_dt(data, max_dt, discount):\n    \"\"\"\n    Variable-Δt sub-sampling of replay trajectories.\n\n    Args:\n        data: dict of (batch, time, ...) tensors — must include\n              'action', 'reward', 'cont' (and observation keys).\n        max_dt: int — K, maximum temporal stride.\n        discount: float — γ, environment discount factor.\n    Returns:\n        data_sub: dict of (batch, time', ...) sub-sampled tensors.\n        dt_labels: (batch, time') int tensor, stride used per step.\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    # Sample per-element Δt from log-uniform over [1, K]\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)\n\n    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))\n    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    # Build index and aggregate tensors\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        # Sub-sample observation / action tensors\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        # Cumulative discounted reward and min continuation\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            gamma_powers = discount ** torch.arange(\n                t_end - t_start, dtype=torch.float, device=device\n            )\n            reward_cum[b, i] = (\n                gamma_powers.unsqueeze(-1) * data[\"reward\"][b, t_start:t_end]\n            ).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n```\n\n### F.4 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train`\n\n```python\n# Before calling self.dynamics.observe():\nif self._config.gate_enabled:\n    data, dt_labels = tools.subsample_variable_dt(\n        data, self._config.gate_max_dt, self._config.discount,\n    )\n    # dt_labels: (batch, time') — passed to observe → obs_step → img_step\nelse:\n    dt_labels = None\n```\n\nThe `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).\n\n### F.5 Design Notes\n\n- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.\n- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.\n- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.\n- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal.",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),\n    # so use it directly. gamma^Dt for the discount:\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Replay Buffer Subsampling Strategy\n\n### F.1 Problem Statement\n\nThe world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.\n\nHowever, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.\n\n### F.2 Strategy 1: Post-Sampling Temporal Skip\n\nAfter sampling a standard `(batch_size, batch_length)` sequence from replay:\n1. For a fraction of batch elements, randomly select skip patterns\n2. Index into the sequence to create variable-rate subsequences\n3. Train RSSM with corresponding Dt labels\n\n```python\ndef apply_temporal_skip(data, max_dt, skip_prob=0.3):\n    \"\"\"\n    Args:\n        data: dict of (batch, time, ...) tensors from replay\n        max_dt: int\n        skip_prob: probability of applying skip to each batch element\n    Returns:\n        data_skipped: dict with same batch dim but potentially shorter time dim\n        dt_labels: (batch, time') tensor of Dt values used\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    dt_labels = torch.ones(B, T, dtype=torch.long)\n\n    for b in range(B):\n        if random.random() < skip_prob:\n            t = 0\n            indices = [0]\n            while t < T - 1:\n                dt = random.randint(1, min(max_dt, T - 1 - t))\n                t += dt\n                indices.append(t)\n                dt_labels[b, len(indices) - 1] = dt\n            # Subsample this batch element\n            for key in data:\n                data[key][b] = data[key][b, indices]\n    return data, dt_labels\n```\n\n**Pros**: Simple, no replay buffer changes.\n**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.\n\n### F.3 Strategy 2: Precomputed Variable-Rate Subsequences\n\nAt episode storage time, precompute and store multiple temporal resolutions:\n- For each episode, generate several subsampled versions with different skip patterns\n- Store cumulated rewards for skipped intervals\n- Sample from this augmented dataset\n\n**Pros**: Efficient at training time; exact reward cumulation.\n**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.\n\n### F.4 Recommended Approach: Strategy 1 with Modifications\n\nStrategy 1, but only applied to a separate \"gate training\" phase within each world model update:\n\n```python\n# In WorldModel._train, after standard RSSM training:\nif self._config.gate_enabled:\n    # Sample a separate batch for gate-aware RSSM fine-tuning\n    # Standard RSSM loss on full-rate data (as before)\n    # Gate supervision on the same full-rate data (state deltas)\n    # No need to actually skip in replay -- the gate learns from\n    # observing which states are \"skippable\" in the full-rate stream\n```\n\n**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.\n\nThe RSSM can generalize to larger Dt because:\n1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)\n2. The GRU learns to scale its update magnitude based on Dt_emb\n3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable\n\n**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
    "structuredPatch": [
      {
        "oldStart": 697,
        "oldLines": 85,
        "newStart": 697,
        "newLines": 118,
        "lines": [
          " ",
          " ---",
          " ",
          "-## Module F: Replay Buffer Subsampling Strategy",
          "+## Module F: Variable-Δt Replay Sub-Sampling",
          " ",
          "-### F.1 Problem Statement",
          "+### F.1 Motivation",
          " ",
          "-The world model is trained on fixed-rate trajectories from the replay buffer (every real environment step). Variable Dt is an imagination-only concept. The replay buffer itself does not need fundamental changes.",
          "+To teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.",
          " ",
          "-However, to train the RSSM to understand what \"Dt=3\" means (i.e., predicting state 3 steps ahead), we need exposure to multi-step transitions during world model training.",
          "+### F.2 Sub-Sampling Procedure",
          " ",
          "-### F.2 Strategy 1: Post-Sampling Temporal Skip",
          "+For each training batch:",
          " ",
          "-After sampling a standard `(batch_size, batch_length)` sequence from replay:",
          "-1. For a fraction of batch elements, randomly select skip patterns",
          "-2. Index into the sequence to create variable-rate subsequences",
          "-3. Train RSSM with corresponding Dt labels",
          "+1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.",
          "+2. For each batch element, independently draw a stride from a **log-uniform distribution**:",
          "+   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).",
          "+3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.",
          "+4. For each gap of Δt frames, compute:",
          "+   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`",
          "+   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`",
          "+5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).",
          " ",
          "+Within a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.",
          "+",
          "+### F.3 Implementation",
          "+",
          "+**File**: `tools.py` (new function)",
          "+",
          " ```python",
          "-def apply_temporal_skip(data, max_dt, skip_prob=0.3):",
          "+def subsample_variable_dt(data, max_dt, discount):",
          "     \"\"\"",
          "+    Variable-Δt sub-sampling of replay trajectories.",
          "+",
          "     Args:",
          "-        data: dict of (batch, time, ...) tensors from replay",
          "-        max_dt: int",
          "-        skip_prob: probability of applying skip to each batch element",
          "+        data: dict of (batch, time, ...) tensors — must include",
          "+              'action', 'reward', 'cont' (and observation keys).",
          "+        max_dt: int — K, maximum temporal stride.",
          "+        discount: float — γ, environment discount factor.",
          "     Returns:",
          "-        data_skipped: dict with same batch dim but potentially shorter time dim",
          "-        dt_labels: (batch, time') tensor of Dt values used",
          "+        data_sub: dict of (batch, time', ...) sub-sampled tensors.",
          "+        dt_labels: (batch, time') int tensor, stride used per step.",
          "     \"\"\"",
          "     B, T = data[\"action\"].shape[:2]",
          "-    dt_labels = torch.ones(B, T, dtype=torch.long)",
          "+    device = data[\"action\"].device",
          " ",
          "+    # Sample per-element Δt from log-uniform over [1, K]",
          "+    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))",
          "+    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)",
          "+",
          "+    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))",
          "+    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused",
          "+    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()",
          "+    T_sub = sub_len.max().item()",
          "+",
          "+    # Build index and aggregate tensors",
          "+    data_sub = {}",
          "+    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)",
          "+    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)",
          "+    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)",
          "+",
          "     for b in range(B):",
          "-        if random.random() < skip_prob:",
          "-            t = 0",
          "-            indices = [0]",
          "-            while t < T - 1:",
          "-                dt = random.randint(1, min(max_dt, T - 1 - t))",
          "-                t += dt",
          "-                indices.append(t)",
          "-                dt_labels[b, len(indices) - 1] = dt",
          "-            # Subsample this batch element",
          "-            for key in data:",
          "-                data[key][b] = data[key][b, indices]",
          "-    return data, dt_labels",
          "-```",
          "+        dt_b = dt_per_elem[b].item()",
          "+        indices = list(range(0, T, dt_b))",
          "+        L = len(indices)",
          " ",
          "-**Pros**: Simple, no replay buffer changes.",
          "-**Cons**: Wastes computation on unused timesteps; variable-length sequences within a batch require padding; only a fraction of batches see variable Dt.",
          "+        # Sub-sample observation / action tensors",
          "+        for key in data:",
          "+            if key not in data_sub:",
          "+                data_sub[key] = torch.zeros(",
          "+                    B, T_sub, *data[key].shape[2:],",
          "+                    dtype=data[key].dtype, device=device,",
          "+                )",
          "+            data_sub[key][b, :L] = data[key][b, indices]",
          " ",
          "-### F.3 Strategy 2: Precomputed Variable-Rate Subsequences",
          "+        # Cumulative discounted reward and min continuation",
          "+        for i, t_start in enumerate(indices[:-1]):",
          "+            t_end = min(t_start + dt_b, T)",
          "+            gamma_powers = discount ** torch.arange(",
          "+                t_end - t_start, dtype=torch.float, device=device",
          "+            )",
          "+            reward_cum[b, i] = (",
          "+                gamma_powers.unsqueeze(-1) * data[\"reward\"][b, t_start:t_end]",
          "+            ).sum(dim=0)",
          "+            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values",
          " ",
          "-At episode storage time, precompute and store multiple temporal resolutions:",
          "-- For each episode, generate several subsampled versions with different skip patterns",
          "-- Store cumulated rewards for skipped intervals",
          "-- Sample from this augmented dataset",
          "+        dt_labels[b, :L] = dt_b",
          " ",
          "-**Pros**: Efficient at training time; exact reward cumulation.",
          "-**Cons**: 2-3x storage; complex episode management; skip patterns are fixed at write time.",
          "+    data_sub[\"reward\"] = reward_cum",
          "+    data_sub[\"cont\"] = cont_min",
          "+    return data_sub, dt_labels",
          "+```",
          " ",
          "-### F.4 Recommended Approach: Strategy 1 with Modifications",
          "+### F.4 Integration in WorldModel._train",
          " ",
          "-Strategy 1, but only applied to a separate \"gate training\" phase within each world model update:",
          "+**File**: `models.py`, `WorldModel._train`",
          " ",
          " ```python",
          "-# In WorldModel._train, after standard RSSM training:",
          "+# Before calling self.dynamics.observe():",
          " if self._config.gate_enabled:",
          "-    # Sample a separate batch for gate-aware RSSM fine-tuning",
          "-    # Standard RSSM loss on full-rate data (as before)",
          "-    # Gate supervision on the same full-rate data (state deltas)",
          "-    # No need to actually skip in replay -- the gate learns from",
          "-    # observing which states are \"skippable\" in the full-rate stream",
          "+    data, dt_labels = tools.subsample_variable_dt(",
          "+        data, self._config.gate_max_dt, self._config.discount,",
          "+    )",
          "+    # dt_labels: (batch, time') — passed to observe → obs_step → img_step",
          "+else:",
          "+    dt_labels = None",
          " ```",
          " ",
          "-**Key insight**: The RSSM does not need to train on skipped data. It only needs to understand Dt via the embedding. During imagination, Dt=3 means \"predict what happens if I advance 3 steps.\" The Dt embedding is trained to modulate the GRU's integration speed. The supervision signal (state deltas) is available from full-rate data.",
          "+The `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).",
          " ",
          "-The RSSM can generalize to larger Dt because:",
          "-1. The Dt embedding is a smooth function (learned embedding table, interpolated by Gumbel-Softmax soft assignment during training)",
          "-2. The GRU learns to scale its update magnitude based on Dt_emb",
          "-3. The gate supervision ensures Dt is only large when state changes are small, where prediction error from larger Dt is tolerable",
          "+### F.5 Design Notes",
          " ",
          "-**If empirical results show poor generalization to large Dt**: add Strategy 1 as a fine-tuning stage after Phase 1, using skip_prob=0.2 and limiting max Dt to the curriculum's current allowed range.",
          "+- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.",
          "+- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.",
          "+- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.",
          "+- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal.",
          " ",
          " ---",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 29_

修正 Risks 部分的 R3（reward 近似误差）和 R6（replay buffer）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "7ab9fa1d-86a4-4030-8788-a0d7080edc86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjsjgcyD7n7fbuqYMvyWHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2788,
      "cache_read_input_tokens": 41762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2788
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01BTj7y4G1s3W2ueKmdgJMri`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies",
  "new_string": "### R3: Reward Prediction Under Variable Δt\n\n**Risk**: The reward head must generalize across different Δt values, predicting cumulative discounted rewards for strides it may not have seen frequently.\n\n**Mitigation**:\n- Log-uniform Δt sampling (Module F) provides balanced training coverage across all stride values\n- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)\n- The gate supervision ensures large Δt is chosen only when state changes are small, correlating with low reward variance — the easier prediction regime\n- Monitor `imag_reward` statistics for anomalies across different Δt values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "5a4b5163-eb05-4ed1-b56e-35a8f4c3a89e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjsjgcyD7n7fbuqYMvyWHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2788,
      "cache_read_input_tokens": 41762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2788
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

_source line 31 · 2026-05-13T01:19:17.467Z_

<details><summary>↩ Tool result · `toolu_01BTj7y4G1s3W2ueKmdgJMri`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "e8de72a4-3b9e-441b-bebf-7c4a00d36bba",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies",
    "newString": "### R3: Reward Prediction Under Variable Δt\n\n**Risk**: The reward head must generalize across different Δt values, predicting cumulative discounted rewards for strides it may not have seen frequently.\n\n**Mitigation**:\n- Log-uniform Δt sampling (Module F) provides balanced training coverage across all stride values\n- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)\n- The gate supervision ensures large Δt is chosen only when state changes are small, correlating with low reward variance — the easier prediction regime\n- Monitor `imag_reward` statistics for anomalies across different Δt values",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),\n    # so use it directly. gamma^Dt for the discount:\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Variable-Δt Replay Sub-Sampling\n\n### F.1 Motivation\n\nTo teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.\n\n### F.2 Sub-Sampling Procedure\n\nFor each training batch:\n\n1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.\n2. For each batch element, independently draw a stride from a **log-uniform distribution**:\n   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).\n3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.\n4. For each gap of Δt frames, compute:\n   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`\n   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`\n5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).\n\nWithin a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.\n\n### F.3 Implementation\n\n**File**: `tools.py` (new function)\n\n```python\ndef subsample_variable_dt(data, max_dt, discount):\n    \"\"\"\n    Variable-Δt sub-sampling of replay trajectories.\n\n    Args:\n        data: dict of (batch, time, ...) tensors — must include\n              'action', 'reward', 'cont' (and observation keys).\n        max_dt: int — K, maximum temporal stride.\n        discount: float — γ, environment discount factor.\n    Returns:\n        data_sub: dict of (batch, time', ...) sub-sampled tensors.\n        dt_labels: (batch, time') int tensor, stride used per step.\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    # Sample per-element Δt from log-uniform over [1, K]\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)\n\n    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))\n    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    # Build index and aggregate tensors\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        # Sub-sample observation / action tensors\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        # Cumulative discounted reward and min continuation\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            gamma_powers = discount ** torch.arange(\n                t_end - t_start, dtype=torch.float, device=device\n            )\n            reward_cum[b, i] = (\n                gamma_powers.unsqueeze(-1) * data[\"reward\"][b, t_start:t_end]\n            ).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n```\n\n### F.4 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train`\n\n```python\n# Before calling self.dynamics.observe():\nif self._config.gate_enabled:\n    data, dt_labels = tools.subsample_variable_dt(\n        data, self._config.gate_max_dt, self._config.discount,\n    )\n    # dt_labels: (batch, time') — passed to observe → obs_step → img_step\nelse:\n    dt_labels = None\n```\n\nThe `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).\n\n### F.5 Design Notes\n\n- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.\n- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.\n- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.\n- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Approximation Error\n\n**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.\n\n**Mitigation**:\n- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance\n- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small\n- Monitor `imag_reward` statistics for anomalies\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
    "structuredPatch": [
      {
        "oldStart": 852,
        "oldLines": 14,
        "newStart": 852,
        "newLines": 15,
        "lines": [
          " - Monitoring metrics with alert thresholds (Section E.4)",
          " - Gumbel-Softmax temperature annealing ensures exploration early on",
          " ",
          "-### R3: Reward Approximation Error",
          "+### R3: Reward Prediction Under Variable Δt",
          " ",
          "-**Risk**: `r_cum = r * Dt` is inaccurate when reward varies within the skipped interval.",
          "+**Risk**: The reward head must generalize across different Δt values, predicting cumulative discounted rewards for strides it may not have seen frequently.",
          " ",
          " **Mitigation**:",
          "-- The gate is supervised to choose large Dt only when state delta is small, which correlates with low reward variance",
          "-- For environments with sparse rewards (Atari, Crafter), most steps have r=0, so the approximation is exact for large Dt steps and only active near reward events where Dt should be small",
          "-- Monitor `imag_reward` statistics for anomalies",
          "+- Log-uniform Δt sampling (Module F) provides balanced training coverage across all stride values",
          "+- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)",
          "+- The gate supervision ensures large Δt is chosen only when state changes are small, correlating with low reward variance — the easier prediction regime",
          "+- Monitor `imag_reward` statistics for anomalies across different Δt values",
          " ",
          " ### R4: Compatibility with Original DreamerV3",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01YWr2HecYPuQ6ULWa46oq5B`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.",
  "new_string": "### R6: Replay Buffer Sub-Sampling Overhead\n\n**Risk**: Variable-Δt sub-sampling (Module F) reduces effective sequence length, discarding some frames per batch.\n\n**Mitigation**:\n- Log-uniform distribution means ~50% of batch elements get Δt ≤ 2, preserving fine-grained temporal resolution for most of the batch\n- Sub-sampled frames still contribute via cumulative reward and min-continuation aggregation — no information is fully discarded\n- The standard (Δt=1) training path remains active for half the batch, maintaining RSSM's single-step prediction quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "c5654cf8-ffea-4d84-b409-d4be132eb6e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cJuq7w98for2KPNVm3wfj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 44550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 509
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

_source line 33 · 2026-05-13T01:19:29.201Z_

<details><summary>↩ Tool result · `toolu_01YWr2HecYPuQ6ULWa46oq5B`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "c82f050f-5996-4abb-95db-512b678cd9a9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.",
    "newString": "### R6: Replay Buffer Sub-Sampling Overhead\n\n**Risk**: Variable-Δt sub-sampling (Module F) reduces effective sequence length, discarding some frames per batch.\n\n**Mitigation**:\n- Log-uniform distribution means ~50% of batch elements get Δt ≤ 2, preserving fine-grained temporal resolution for most of the batch\n- Sub-sampled frames still contribute via cumulative reward and min-continuation aggregation — no information is fully discarded\n- The standard (Δt=1) training path remains active for half the batch, maintaining RSSM's single-step prediction quality",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),\n    # so use it directly. gamma^Dt for the discount:\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Variable-Δt Replay Sub-Sampling\n\n### F.1 Motivation\n\nTo teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.\n\n### F.2 Sub-Sampling Procedure\n\nFor each training batch:\n\n1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.\n2. For each batch element, independently draw a stride from a **log-uniform distribution**:\n   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).\n3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.\n4. For each gap of Δt frames, compute:\n   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`\n   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`\n5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).\n\nWithin a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.\n\n### F.3 Implementation\n\n**File**: `tools.py` (new function)\n\n```python\ndef subsample_variable_dt(data, max_dt, discount):\n    \"\"\"\n    Variable-Δt sub-sampling of replay trajectories.\n\n    Args:\n        data: dict of (batch, time, ...) tensors — must include\n              'action', 'reward', 'cont' (and observation keys).\n        max_dt: int — K, maximum temporal stride.\n        discount: float — γ, environment discount factor.\n    Returns:\n        data_sub: dict of (batch, time', ...) sub-sampled tensors.\n        dt_labels: (batch, time') int tensor, stride used per step.\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    # Sample per-element Δt from log-uniform over [1, K]\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)\n\n    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))\n    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    # Build index and aggregate tensors\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        # Sub-sample observation / action tensors\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        # Cumulative discounted reward and min continuation\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            gamma_powers = discount ** torch.arange(\n                t_end - t_start, dtype=torch.float, device=device\n            )\n            reward_cum[b, i] = (\n                gamma_powers.unsqueeze(-1) * data[\"reward\"][b, t_start:t_end]\n            ).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n```\n\n### F.4 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train`\n\n```python\n# Before calling self.dynamics.observe():\nif self._config.gate_enabled:\n    data, dt_labels = tools.subsample_variable_dt(\n        data, self._config.gate_max_dt, self._config.discount,\n    )\n    # dt_labels: (batch, time') — passed to observe → obs_step → img_step\nelse:\n    dt_labels = None\n```\n\nThe `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).\n\n### F.5 Design Notes\n\n- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.\n- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.\n- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.\n- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Prediction Under Variable Δt\n\n**Risk**: The reward head must generalize across different Δt values, predicting cumulative discounted rewards for strides it may not have seen frequently.\n\n**Mitigation**:\n- Log-uniform Δt sampling (Module F) provides balanced training coverage across all stride values\n- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)\n- The gate supervision ensures large Δt is chosen only when state changes are small, correlating with low reward variance — the easier prediction regime\n- Monitor `imag_reward` statistics for anomalies across different Δt values\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Efficiency\n\n**Risk**: Strategy 1 subsampling wastes loaded data.\n\n**Mitigation**:\n- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.\n- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.\n",
    "structuredPatch": [
      {
        "oldStart": 882,
        "oldLines": 10,
        "newStart": 882,
        "newLines": 11,
        "lines": [
          " - Gate is only called during imagination (not observation/training unroll)",
          " - With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute",
          " ",
          "-### R6: Replay Buffer Efficiency",
          "+### R6: Replay Buffer Sub-Sampling Overhead",
          " ",
          "-**Risk**: Strategy 1 subsampling wastes loaded data.",
          "+**Risk**: Variable-Δt sub-sampling (Module F) reduces effective sequence length, discarding some frames per batch.",
          " ",
          " **Mitigation**:",
          "-- Primary recommendation is to NOT subsample replay. The RSSM learns Dt semantics through the embedding; the gate learns from full-rate state deltas.",
          "-- If subsampling is needed, it applies to a small fraction (skip_prob=0.2-0.3) and the \"wasted\" frames still contributed to the standard RSSM loss before subsampling.",
          "+- Log-uniform distribution means ~50% of batch elements get Δt ≤ 2, preserving fine-grained temporal resolution for most of the batch",
          "+- Sub-sampled frames still contribute via cumulative reward and min-continuation aggregation — no information is fully discarded",
          "+- The standard (Δt=1) training path remains active for half the batch, maintaining RSSM's single-step prediction quality"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 34_

最后更新 File Modification Summary 表格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "2d37d54b-793c-4f46-bb0d-ffa052622ae4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHKyB4tT9UoeuAoMyknCUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 45059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 460
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

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_01W3CtJrGvzVH15BR8n4V6mN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "old_string": "| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |",
  "new_string": "| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.obs_step` | 174-206 | Modify: add `dt` param, forward to `img_step` |\n| `networks.py` | `RSSM.observe` | 127-143 | Modify: accept and forward per-step `dt` labels |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax (τ_init=5.0) |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add variable-Δt sub-sampling + gate loss |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` (reward already cumulative) |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return (uses cumulative reward directly) |\n| `tools.py` | (new) `subsample_variable_dt` | new | Add: log-uniform Δt sub-sampling with cumulative reward / min-cont |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters (τ_init=5.0) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "a65f60b3-428d-4988-9c33-afdafe0af361",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHKyB4tT9UoeuAoMyknCUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 45059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 460
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

_source line 36 · 2026-05-13T01:19:48.349Z_

<details><summary>↩ Tool result · `toolu_01W3CtJrGvzVH15BR8n4V6mN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "3fdbf231-51fc-47ca-9f31-19cd49d68c9a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
    "oldString": "| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |",
    "newString": "| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.obs_step` | 174-206 | Modify: add `dt` param, forward to `img_step` |\n| `networks.py` | `RSSM.observe` | 127-143 | Modify: accept and forward per-step `dt` labels |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax (τ_init=5.0) |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add variable-Δt sub-sampling + gate loss |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` (reward already cumulative) |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return (uses cumulative reward directly) |\n| `tools.py` | (new) `subsample_variable_dt` | new | Add: log-uniform Δt sub-sampling with cumulative reward / min-cont |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters (τ_init=5.0) |",
    "originalFile": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus` | 0.01 | {0.001, 0.01, 0.1} | Prevents collapse |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - self._config.gate_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),\n    # so use it directly. gamma^Dt for the discount:\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Variable-Δt Replay Sub-Sampling\n\n### F.1 Motivation\n\nTo teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.\n\n### F.2 Sub-Sampling Procedure\n\nFor each training batch:\n\n1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.\n2. For each batch element, independently draw a stride from a **log-uniform distribution**:\n   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).\n3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.\n4. For each gap of Δt frames, compute:\n   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`\n   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`\n5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).\n\nWithin a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.\n\n### F.3 Implementation\n\n**File**: `tools.py` (new function)\n\n```python\ndef subsample_variable_dt(data, max_dt, discount):\n    \"\"\"\n    Variable-Δt sub-sampling of replay trajectories.\n\n    Args:\n        data: dict of (batch, time, ...) tensors — must include\n              'action', 'reward', 'cont' (and observation keys).\n        max_dt: int — K, maximum temporal stride.\n        discount: float — γ, environment discount factor.\n    Returns:\n        data_sub: dict of (batch, time', ...) sub-sampled tensors.\n        dt_labels: (batch, time') int tensor, stride used per step.\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    # Sample per-element Δt from log-uniform over [1, K]\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)\n\n    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))\n    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    # Build index and aggregate tensors\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        # Sub-sample observation / action tensors\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        # Cumulative discounted reward and min continuation\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            gamma_powers = discount ** torch.arange(\n                t_end - t_start, dtype=torch.float, device=device\n            )\n            reward_cum[b, i] = (\n                gamma_powers.unsqueeze(-1) * data[\"reward\"][b, t_start:t_end]\n            ).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n```\n\n### F.4 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train`\n\n```python\n# Before calling self.dynamics.observe():\nif self._config.gate_enabled:\n    data, dt_labels = tools.subsample_variable_dt(\n        data, self._config.gate_max_dt, self._config.discount,\n    )\n    # dt_labels: (batch, time') — passed to observe → obs_step → img_step\nelse:\n    dt_labels = None\n```\n\nThe `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).\n\n### F.5 Design Notes\n\n- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.\n- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.\n- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.\n- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Prediction Under Variable Δt\n\n**Risk**: The reward head must generalize across different Δt values, predicting cumulative discounted rewards for strides it may not have seen frequently.\n\n**Mitigation**:\n- Log-uniform Δt sampling (Module F) provides balanced training coverage across all stride values\n- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)\n- The gate supervision ensures large Δt is chosen only when state changes are small, correlating with low reward variance — the easier prediction regime\n- Monitor `imag_reward` statistics for anomalies across different Δt values\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Sub-Sampling Overhead\n\n**Risk**: Variable-Δt sub-sampling (Module F) reduces effective sequence length, discarding some frames per batch.\n\n**Mitigation**:\n- Log-uniform distribution means ~50% of batch elements get Δt ≤ 2, preserving fine-grained temporal resolution for most of the batch\n- Sub-sampled frames still contribute via cumulative reward and min-continuation aggregation — no information is fully discarded\n- The standard (Δt=1) training path remains active for half the batch, maintaining RSSM's single-step prediction quality\n",
    "structuredPatch": [
      {
        "oldStart": 819,
        "oldLines": 15,
        "newStart": 819,
        "newLines": 18,
        "lines": [
          " | `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |",
          " | `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |",
          " | `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |",
          "+| `networks.py` | `RSSM.obs_step` | 174-206 | Modify: add `dt` param, forward to `img_step` |",
          "+| `networks.py` | `RSSM.observe` | 127-143 | Modify: accept and forward per-step `dt` labels |",
          " | `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |",
          "-| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax |",
          "+| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax (τ_init=5.0) |",
          " | `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |",
          "-| `models.py` | `WorldModel._train` | 108-174 | Modify: add gate loss computation |",
          "+| `models.py` | `WorldModel._train` | 108-174 | Modify: add variable-Δt sub-sampling + gate loss |",
          " | `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |",
          "-| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` |",
          "+| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` (reward already cumulative) |",
          " | `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |",
          "-| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return |",
          "-| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters |",
          "+| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return (uses cumulative reward directly) |",
          "+| `tools.py` | (new) `subsample_variable_dt` | new | Add: log-uniform Δt sub-sampling with cumulative reward / min-cont |",
          "+| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters (τ_init=5.0) |",
          " ",
          " ---",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 37_

验证修改后的文件完整性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "157349ae-c112-4734-9da9-bb468b9857e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aLk3XzGfHip3fvjRsmU7v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1303,
      "cache_read_input_tokens": 45519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1303
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

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01TvJ45QZy4d5MYNJVMGgw62`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "offset": 120,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "3dd06382-9135-486c-b8e2-7141740ff3c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aLk3XzGfHip3fvjRsmU7v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1303,
      "cache_read_input_tokens": 45519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1303
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

_source line 39 · 2026-05-13T01:19:51.752Z_

<details><summary>↩ Tool result · `toolu_01TvJ45QZy4d5MYNJVMGgw62`</summary>

````text
120	```
121	
122	**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.
123	
124	```python
125	def obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):
126	    # ... (existing reset / mask logic unchanged) ...
127	    prior = self.img_step(prev_state, prev_action, dt=dt)
128	    # ... (existing posterior computation unchanged) ...
129	    return post, prior
130	```
131	
132	**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.
133	
134	**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:
135	
136	```python
137	def imagine_with_action(self, action, state, dt_sequence=None):
138	    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))
139	    action = swap(action)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "b76796fc-e295-4621-8c56-3a498b354baf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
      "content": "```\n\n**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)",
      "numLines": 20,
      "startLine": 120,
      "totalLines": 896
    }
  }
}
````

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01Po2qcubcGMVsYUmpW1vrzK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "offset": 155,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "a3305953-6bc8-4b44-ac67-314d68c411c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159ULA38z287ywEDCSzovju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 46822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 593
      },
      "output_tokens": 65,
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

_source line 41 · 2026-05-13T01:19:54.257Z_

<details><summary>↩ Tool result · `toolu_01Po2qcubcGMVsYUmpW1vrzK`</summary>

````text
155	**File**: `configs.yaml`, under `defaults`:
156	
157	```yaml
158	# Event-Gated Adaptive Horizon
159	gate_max_dt: 8              # K: max temporal stride
160	gate_dt_embed_dim: 32       # Dt embedding dimension
161	gate_hidden_units: 256      # gate MLP hidden size
162	gate_hidden_layers: 2       # gate MLP depth
163	gate_tau_init: 5.0          # Gumbel-Softmax initial temperature
164	gate_tau_final: 0.5         # Gumbel-Softmax final temperature
165	gate_tau_anneal_steps: 200000  # linear anneal duration
166	gate_loss_weight: 1.0       # gate supervision loss coefficient
167	gate_entropy_bonus: 0.01    # entropy regularization weight
168	gate_curriculum_phase1: 50000   # forced Dt=1 phase
169	gate_curriculum_phase2: 150000  # linear ramp phase end
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "c09239a5-97ac-4691-850d-58ec64eea5d3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
      "content": "**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus: 0.01    # entropy regularization weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end",
      "numLines": 15,
      "startLine": 155,
      "totalLines": 896
    }
  }
}
````

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_011c45tnnY9oTxo6XCaGAiYZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "offset": 488,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "f6cc9215-1231-4078-82cf-321d5bd87857",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV6Kg9hVrN9gkC2KCummWP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 47415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 394
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

_source line 43 · 2026-05-13T01:19:58.366Z_

<details><summary>↩ Tool result · `toolu_011c45tnnY9oTxo6XCaGAiYZ`</summary>

````text
488	---
489	
490	## Module D: Adapted Lambda-Returns
491	
492	### D.1 Standard vs. Adapted Lambda-Return
493	
494	**Standard** (from `tools.py:691-717`):
495	
496	$$V_t^\lambda = r_{t+1} + \gamma \left[(1-\lambda) V(s_{t+1}) + \lambda V_{t+1}^\lambda\right]$$
497	
498	**Adapted for variable Dt**:
499	
500	$$V_t^\lambda = r_{t:t+\Delta t}^{\text{cum}} + \gamma^{\Delta t} \left[(1-\lambda) V(s_{t+\Delta t}) + \lambda V_{t+\Delta t}^\lambda\right]$$
501	
502	where:
503	- $r_{t:t+\Delta t}^{\text{cum}} = \sum_{k=0}^{\Delta t - 1} \gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.
504	- $\gamma^{\Delta t}$: discount raised to the power of the stride
505	
506	### D.2 Modified lambda_return
507	
508	**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):
509	
510	```python
511	def lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):
512	    """
513	    Lambda-return with variable temporal strides.
514	
515	    Args:
516	        reward: (time, batch, 1) - per-step imagined reward
517	        value:  (time, batch, 1) - value estimates
518	        pcont:  (time, batch, 1) - continuation probability * base discount
519	        dt:     (time, batch) or (time, batch, 1) - temporal stride per step
520	        bootstrap: (batch, 1) - terminal value
521	        lambda_: float
522	        axis: int
523	    Returns:
524	        returns: list of (batch, 1) tensors
525	    """
526	    assert len(reward.shape) == len(value.shape)
527	    if isinstance(pcont, (int, float)):
528	        pcont = pcont * torch.ones_like(reward)
529	    if dt.dim() == 2:
530	        dt = dt.unsqueeze(-1)  # (time, batch, 1)
531	    dt = dt.float()
532	
533	    dims = list(range(len(reward.shape)))
534	    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]
535	    if axis != 0:
536	        reward = reward.permute(dims)
537	        value = value.permute(dims)
538	        pcont = pcont.permute(dims)
539	        dt = dt.permute(dims)
540	
541	    if bootstrap is None:
542	        bootstrap = torch.zeros_like(value[-1])
543	
544	    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),
545	    # so use it directly. gamma^Dt for the discount:
546	    pcont_adj = pcont ** dt
547	
548	    next_values = torch.cat([value[1:], bootstrap[None]], 0)
549	    inputs = reward + pcont_adj * next_values * (1 - lambda_)
550	
551	    returns = static_scan_for_lambda_return(
552	        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
553	        (inputs, pcont_adj), bootstrap
554	    )
555	    if axis != 0:
556	        returns = returns.permute(dims)
557	    return returns
558	```
559	
560	### D.3 Integration in ImagBehavior._compute_target
561	
562	**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):
563	
564	```python
565	def _compute_target(self, imag_feat, imag_state, reward, dts=None):
566	    if "cont" in self._world_model.heads:
567	        inp = self._world_model.dynamics.get_feat(imag_state)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "30973a98-f46a-43fc-ab6d-5a329e17bb42",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
      "content": "---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),\n    # so use it directly. gamma^Dt for the discount:\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)",
      "numLines": 80,
      "startLine": 488,
      "totalLines": 896
    }
  }
}
````

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01GgqXZwrBcFSAeABwFJUqFd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "offset": 596,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "baa57560-1f90-401b-9cc9-ff49d06802d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuKAiVzzjqNhruBzCfbeo2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 47809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1274
      },
      "output_tokens": 35,
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

_source line 45 · 2026-05-13T01:20:04.618Z_

<details><summary>↩ Tool result · `toolu_01GgqXZwrBcFSAeABwFJUqFd`</summary>

````text
596	        weights = torch.cumprod(
597	            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0
598	        ).detach()
599	    else:
600	        weights = torch.cumprod(
601	            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0
602	        ).detach()
603	
604	    return target, weights, value[:-1]
605	```
606	
607	---
608	
609	## Module E: Gate Collapse Prevention
610	
611	### E.1 Failure Modes
612	
613	Gate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.
614	
615	### E.2 Entropy Regularization
616	
617	Already included in Module C's loss:
618	
619	```python
620	total_gate_loss = gate_scale * (
621	    config.gate_loss_weight * g_loss.mean()
622	    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy
623	)
624	```
625	
626	The entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.
627	
628	### E.3 Gating Curriculum (Three Phases)
629	
630	| Phase | Steps | Behavior | Rationale |
631	|---|---|---|---|
632	| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |
633	| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |
634	| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |
635	
636	Implementation (already shown in Module C.3):
637	
638	```python
639	if step < config.gate_curriculum_phase1:
640	    gate_scale = 0.0
641	elif step < config.gate_curriculum_phase2:
642	    progress = (step - config.gate_curriculum_phase1) / (
643	        config.gate_curriculum_phase2 - config.gate_curriculum_phase1
644	    )
645	    gate_scale = progress
646	else:
647	    gate_scale = 1.0
648	```
649	
650	In `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.
651	
652	### E.4 Collapse Detection Metrics
653	
654	**File**: `models.py`, add to metrics in `ImagBehavior._train`:
655	
656	```python
657	if self._config.gate_enabled and dts is not None:
658	    dts_float = dts.float()
659	    metrics["gate_dt_mean"] = to_np(torch.mean(dts_float))
660	    metrics["gate_dt_std"] = to_np(torch.std(dts_float))
661	    metrics["gate_dt_min"] = to_np(torch.min(dts_float))
662	    metrics["gate_dt_max"] = to_np(torch.max(dts_float))
663	
664	    # Distribution over K bins
665	    dt_counts = torch.bincount(
666	        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1
667	    )[1:]  # skip bin 0
668	    dt_dist = dt_counts.float() / dt_counts.sum()
669	    for k in range(self._config.gate_max_dt):
670	        metrics[f"gate_dt_{k+1}_frac"] = to_np(dt_dist[k])
671	
672	    # Entropy of empirical Dt distribution (collapse indicator)
673	    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()
674	    metrics["gate_empirical_entropy"] = to_np(emp_entropy)
675	    max_entropy = np.log(self._config.gate_max_dt)
676	    metrics["gate_entropy_ratio"] = to_np(emp_entropy) / max_entropy
677	```
678	
679	**Collapse alert thresholds**:
680	- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values
681	- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed
682	- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating
683	- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates
684	
685	### E.5 Automatic Recovery (Optional)
686	
687	If collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:
688	
689	```python
690	if gate_entropy_ratio < 0.2:
691	    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost
692	else:
693	    effective_entropy_bonus = config.gate_entropy_bonus
694	```
695	
696	This is optional and aggressive. Prefer tuning the base entropy bonus instead.
697	
698	---
699	
700	## Module F: Variable-Δt Replay Sub-Sampling
701	
702	### F.1 Motivation
703	
704	To teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.
705	
706	### F.2 Sub-Sampling Procedure
707	
708	For each training batch:
709	
710	1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.
711	2. For each batch element, independently draw a stride from a **log-uniform distribution**:
712	   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).
713	3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.
714	4. For each gap of Δt frames, compute:
715	   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "efea396f-d7a0-4a86-9077-f37f4bf8b46d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
      "content": "        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - config.gate_entropy_bonus * g_entropy.mean()  # maximize entropy\n)\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient `gate_entropy_bonus=0.01` is small enough to not override the supervision signal but large enough to prevent premature commitment.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus * 10  # 10x boost\nelse:\n    effective_entropy_bonus = config.gate_entropy_bonus\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Variable-Δt Replay Sub-Sampling\n\n### F.1 Motivation\n\nTo teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.\n\n### F.2 Sub-Sampling Procedure\n\nFor each training batch:\n\n1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.\n2. For each batch element, independently draw a stride from a **log-uniform distribution**:\n   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).\n3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.\n4. For each gap of Δt frames, compute:\n   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`",
      "numLines": 120,
      "startLine": 596,
      "totalLines": 896
    }
  }
}
````

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01D8PJ9A8XCbwMvfJGJcoz8c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "offset": 715,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "cc053aee-e608-466c-9b49-3a2477e56171",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThP156W4TqrCcsE57ib4uT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1885,
      "cache_read_input_tokens": 49083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1885
      },
      "output_tokens": 36,
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

_source line 47 · 2026-05-13T01:20:08.853Z_

<details><summary>↩ Tool result · `toolu_01D8PJ9A8XCbwMvfJGJcoz8c`</summary>

````text
715	   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`
716	   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`
717	5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).
718	
719	Within a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.
720	
721	### F.3 Implementation
722	
723	**File**: `tools.py` (new function)
724	
725	```python
726	def subsample_variable_dt(data, max_dt, discount):
727	    """
728	    Variable-Δt sub-sampling of replay trajectories.
729	
730	    Args:
731	        data: dict of (batch, time, ...) tensors — must include
732	              'action', 'reward', 'cont' (and observation keys).
733	        max_dt: int — K, maximum temporal stride.
734	        discount: float — γ, environment discount factor.
735	    Returns:
736	        data_sub: dict of (batch, time', ...) sub-sampled tensors.
737	        dt_labels: (batch, time') int tensor, stride used per step.
738	    """
739	    B, T = data["action"].shape[:2]
740	    device = data["action"].device
741	
742	    # Sample per-element Δt from log-uniform over [1, K]
743	    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))
744	    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)
745	
746	    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))
747	    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused
748	    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()
749	    T_sub = sub_len.max().item()
750	
751	    # Build index and aggregate tensors
752	    data_sub = {}
753	    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)
754	    reward_cum = torch.zeros(B, T_sub, *data["reward"].shape[2:], device=device)
755	    cont_min = torch.ones(B, T_sub, *data["cont"].shape[2:], device=device)
756	
757	    for b in range(B):
758	        dt_b = dt_per_elem[b].item()
759	        indices = list(range(0, T, dt_b))
760	        L = len(indices)
761	
762	        # Sub-sample observation / action tensors
763	        for key in data:
764	            if key not in data_sub:
765	                data_sub[key] = torch.zeros(
766	                    B, T_sub, *data[key].shape[2:],
767	                    dtype=data[key].dtype, device=device,
768	                )
769	            data_sub[key][b, :L] = data[key][b, indices]
770	
771	        # Cumulative discounted reward and min continuation
772	        for i, t_start in enumerate(indices[:-1]):
773	            t_end = min(t_start + dt_b, T)
774	            gamma_powers = discount ** torch.arange(
775	                t_end - t_start, dtype=torch.float, device=device
776	            )
777	            reward_cum[b, i] = (
778	                gamma_powers.unsqueeze(-1) * data["reward"][b, t_start:t_end]
779	            ).sum(dim=0)
780	            cont_min[b, i] = data["cont"][b, t_start:t_end].min(dim=0).values
781	
782	        dt_labels[b, :L] = dt_b
783	
784	    data_sub["reward"] = reward_cum
785	    data_sub["cont"] = cont_min
786	    return data_sub, dt_labels
787	```
788	
789	### F.4 Integration in WorldModel._train
790	
791	**File**: `models.py`, `WorldModel._train`
792	
793	```python
794	# Before calling self.dynamics.observe():
795	if self._config.gate_enabled:
796	    data, dt_labels = tools.subsample_variable_dt(
797	        data, self._config.gate_max_dt, self._config.discount,
798	    )
799	    # dt_labels: (batch, time') — passed to observe → obs_step → img_step
800	else:
801	    dt_labels = None
802	```
803	
804	The `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).
805	
806	### F.5 Design Notes
807	
808	- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.
809	- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.
810	- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.
811	- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal.
812	
813	---
814	
815	## File Modification Summary
816	
817	| File | Function/Class | Lines | Change Type |
818	|---|---|---|---|
819	| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |
820	| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |
821	| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |
822	| `networks.py` | `RSSM.obs_step` | 174-206 | Modify: add `dt` param, forward to `img_step` |
823	| `networks.py` | `RSSM.observe` | 127-143 | Modify: accept and forward per-step `dt` labels |
824	| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |
825	| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax (τ_init=5.0) |
826	| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |
827	| `models.py` | `WorldModel._train` | 108-174 | Modify: add variable-Δt sub-sampling + gate loss |
828	| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |
829	| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` (reward already cumulative) |
830	| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |
831	| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return (uses cumulative reward directly) |
832	| `tools.py` | (new) `subsample_variable_dt` | new | Add: log-uniform Δt sub-sampling with cumulative reward / min-cont |
833	| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters (τ_init=5.0) |
834	
835	---
836	
837	## Risks and Mitigations
838	
839	### R1: Training Instability
840	
841	**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.
842	
843	**Mitigation**:
844	- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible
845	- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate
846	- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences
847	
848	### R2: Gate Collapse
849	
850	**Risk**: Gate degenerates to constant Dt, losing adaptivity.
851	
852	**Mitigation**:
853	- Entropy regularization in gate loss
854	- Curriculum prevents premature commitment
855	- Monitoring metrics with alert thresholds (Section E.4)
856	- Gumbel-Softmax temperature annealing ensures exploration early on
857	
858	### R3: Reward Prediction Under Variable Δt
859	
860	**Risk**: The reward head must generalize across different Δt values, predicting cumulative discounted rewards for strides it may not have seen frequently.
861	
862	**Mitigation**:
863	- Log-uniform Δt sampling (Module F) provides balanced training coverage across all stride values
864	- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "a450e47a-8660-4413-bf34-7557e1c9f22f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
      "content": "   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`\n   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`\n5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).\n\nWithin a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.\n\n### F.3 Implementation\n\n**File**: `tools.py` (new function)\n\n```python\ndef subsample_variable_dt(data, max_dt, discount):\n    \"\"\"\n    Variable-Δt sub-sampling of replay trajectories.\n\n    Args:\n        data: dict of (batch, time, ...) tensors — must include\n              'action', 'reward', 'cont' (and observation keys).\n        max_dt: int — K, maximum temporal stride.\n        discount: float — γ, environment discount factor.\n    Returns:\n        data_sub: dict of (batch, time', ...) sub-sampled tensors.\n        dt_labels: (batch, time') int tensor, stride used per step.\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    # Sample per-element Δt from log-uniform over [1, K]\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)\n\n    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))\n    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    # Build index and aggregate tensors\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        # Sub-sample observation / action tensors\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        # Cumulative discounted reward and min continuation\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            gamma_powers = discount ** torch.arange(\n                t_end - t_start, dtype=torch.float, device=device\n            )\n            reward_cum[b, i] = (\n                gamma_powers.unsqueeze(-1) * data[\"reward\"][b, t_start:t_end]\n            ).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n```\n\n### F.4 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train`\n\n```python\n# Before calling self.dynamics.observe():\nif self._config.gate_enabled:\n    data, dt_labels = tools.subsample_variable_dt(\n        data, self._config.gate_max_dt, self._config.discount,\n    )\n    # dt_labels: (batch, time') — passed to observe → obs_step → img_step\nelse:\n    dt_labels = None\n```\n\nThe `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).\n\n### F.5 Design Notes\n\n- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.\n- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.\n- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.\n- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.obs_step` | 174-206 | Modify: add `dt` param, forward to `img_step` |\n| `networks.py` | `RSSM.observe` | 127-143 | Modify: accept and forward per-step `dt` labels |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax (τ_init=5.0) |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add variable-Δt sub-sampling + gate loss |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` (reward already cumulative) |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return (uses cumulative reward directly) |\n| `tools.py` | (new) `subsample_variable_dt` | new | Add: log-uniform Δt sub-sampling with cumulative reward / min-cont |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters (τ_init=5.0) |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Prediction Under Variable Δt\n\n**Risk**: The reward head must generalize across different Δt values, predicting cumulative discounted rewards for strides it may not have seen frequently.\n\n**Mitigation**:\n- Log-uniform Δt sampling (Module F) provides balanced training coverage across all stride values\n- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)",
      "numLines": 150,
      "startLine": 715,
      "totalLines": 896
    }
  }
}
````

</details>

---

### Assistant

_source line 48_

全部修改完成且一致。验证最后几行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "cc8fee6b-8b1c-44e8-9830-5f88221bea7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011X988YhRwhR2HkZWHrvr7f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2739,
      "cache_read_input_tokens": 50968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2739
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01T9MhotkRpZmFz9KK9br7kP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
  "offset": 864,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "fe5ff9aa-9044-48eb-b13e-b98c1f82a8c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011X988YhRwhR2HkZWHrvr7f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2739,
      "cache_read_input_tokens": 50968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2739
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

_source line 50 · 2026-05-13T01:20:13.741Z_

<details><summary>↩ Tool result · `toolu_01T9MhotkRpZmFz9KK9br7kP`</summary>

```text
864	- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)
865	- The gate supervision ensures large Δt is chosen only when state changes are small, correlating with low reward variance — the easier prediction regime
866	- Monitor `imag_reward` statistics for anomalies across different Δt values
867	
868	### R4: Compatibility with Original DreamerV3
869	
870	**Risk**: Modified code breaks when `gate_enabled=false`.
871	
872	**Mitigation**:
873	- All gate logic is guarded by `config.gate_enabled`
874	- `img_step` defaults `dt=None` which maps to Dt=1
875	- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)
876	- `_compute_target` falls back to standard `lambda_return`
877	- Net-zero change to behavior when `gate_enabled=false`
878	
879	### R5: Computational Overhead
880	
881	**Risk**: Gate MLP adds forward-pass cost in imagination.
882	
883	**Mitigation**:
884	- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)
885	- Gate is only called during imagination (not observation/training unroll)
886	- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute
887	
888	### R6: Replay Buffer Sub-Sampling Overhead
889	
890	**Risk**: Variable-Δt sub-sampling (Module F) reduces effective sequence length, discarding some frames per batch.
891	
892	**Mitigation**:
893	- Log-uniform distribution means ~50% of batch elements get Δt ≤ 2, preserving fine-grained temporal resolution for most of the batch
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "b6000ae0-15e1-4796-a9a3-f32b0921369b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
      "content": "- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)\n- The gate supervision ensures large Δt is chosen only when state changes are small, correlating with low reward variance — the easier prediction regime\n- Monitor `imag_reward` statistics for anomalies across different Δt values\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Sub-Sampling Overhead\n\n**Risk**: Variable-Δt sub-sampling (Module F) reduces effective sequence length, discarding some frames per batch.\n\n**Mitigation**:\n- Log-uniform distribution means ~50% of batch elements get Δt ≤ 2, preserving fine-grained temporal resolution for most of the batch",
      "numLines": 30,
      "startLine": 864,
      "totalLines": 896
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

所有修改已完成，文档内部一致。修正总结：

1. **偏差 1 (Module F)**：整节重写。删除"不修改 buffer"的错误建议和 Strategy 1/2/3 对比，替换为 variable-Δt 子采样方案——log-uniform 采样 Δt、累积折扣 reward `r_cum`、最小存续概率 `c_min`，含完整 `subsample_variable_dt` 伪代码。

2. **偏差 2 (Module D)**：D.1 公式说明改为引用 Module F 预计算的累积折扣 reward；D.2 中 `reward_adj = reward * dt` 删除，直接使用已是累积值的 reward；D.4 (Scale Approximation) 整节删除。

3. **偏差 3 (温度)**：`tau_init` 从 1.0 改为 5.0，涉及 A.2 configs.yaml、B.1 EventGate 默认参数两处。

4. **额外修正**：A.1 `obs_step` 增加 `dt=None` 参数并传递给 `img_step`；`observe` 说明更新为接收 per-step dt labels；File Modification Summary 表格新增 `obs_step`/`observe`/`subsample_variable_dt` 行并标注 τ_init=5.0；R3/R6 风险描述更新为匹配新方案。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "uuid": "ad023070-2eec-48be-84e2-8d868c86c19f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGNkg7xoMsfENMSos9TEYJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 621,
      "cache_read_input_tokens": 53707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 621
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

_source line 52_

所有修改已完成，文档内部一致。修正总结：

1. **偏差 1 (Module F)**：整节重写。删除"不修改 buffer"的错误建议和 Strategy 1/2/3 对比，替换为 variable-Δt 子采样方案——log-uniform 采样 Δt、累积折扣 reward `r_cum`、最小存续概率 `c_min`，含完整 `subsample_variable_dt` 伪代码。

2. **偏差 2 (Module D)**：D.1 公式说明改为引用 Module F 预计算的累积折扣 reward；D.2 中 `reward_adj = reward * dt` 删除，直接使用已是累积值的 reward；D.4 (Scale Approximation) 整节删除。

3. **偏差 3 (温度)**：`tau_init` 从 1.0 改为 5.0，涉及 A.2 configs.yaml、B.1 EventGate 默认参数两处。

4. **额外修正**：A.1 `obs_step` 增加 `dt=None` 参数并传递给 `img_step`；`observe` 说明更新为接收 per-step dt labels；File Modification Summary 表格新增 `obs_step`/`observe`/`subsample_variable_dt` 行并标注 τ_init=5.0；R3/R6 风险描述更新为匹配新方案。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 253485,
  "duration_api_ms": 253992,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "872e13f8-cfca-41b1-bdb6-ef99bd37d4f5",
  "total_cost_usd": 0.9015317500000001,
  "usage": {
    "input_tokens": 19,
    "cache_creation_input_tokens": 42487,
    "cache_read_input_tokens": 747658,
    "output_tokens": 10396,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42487,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 416,
        "cache_read_input_tokens": 53707,
        "cache_creation_input_tokens": 621,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 621
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2064,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021639999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 19,
      "outputTokens": 10396,
      "cacheReadInputTokens": 747658,
      "cacheCreationInputTokens": 42487,
      "webSearchRequests": 0,
      "costUSD": 0.8993677500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fbc45969-76ff-46d7-b8ba-ad9fb4dee2f1"
}
```

</details>

---
