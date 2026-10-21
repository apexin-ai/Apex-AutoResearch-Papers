# write method section

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_write_method-section_20260513T063657.log`
- **Structured JSON:** [`c0969f0cb8bb0301cd58.json`](../../sessions/c0/c0969f0cb8bb0301cd58.json)

## Before a recorded user message

22 recorded events

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
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
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
  "uuid": "f8f56836-ce1d-4a05-a9de-48945ca596e2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1778659200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6ee851ef-7783-4498-8367-6c0573a38096",
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3"
}
```

---

### Assistant

_source line 4_

I'll read all the reference materials first, then write the method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "0592bfea-fe02-444c-a1b4-f67653c87e65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGvuUf2bFiCqJ6dSCykPiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12473,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12473
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01ArzHJp9gH6Yc5qdFN6Y5SY`</summary>

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
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "025ad86b-8f4f-4b1b-b33a-f2a0b8cc1a9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGvuUf2bFiCqJ6dSCykPiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12473,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12473
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

_source line 6 · 2026-05-13T06:37:09.470Z_

<details><summary>↩ Tool result · `toolu_01ArzHJp9gH6Yc5qdFN6Y5SY`</summary>

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
140	    if dt_sequence is not None:
141	        dt_sequence = swap(dt_sequence)
142	        prior = tools.static_scan(
143	            lambda s, a, dt: self.img_step(s, a, dt=dt),
144	            [action, dt_sequence], state
145	        )
146	    else:
147	        prior = tools.static_scan(self.img_step, [action], state)
148	    prior = prior[0]
149	    prior = {k: swap(v) for k, v in prior.items()}
150	    return prior
151	```
152	
153	### A.2 Config Additions
154	
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
167	gate_entropy_bonus_init: 0.1    # entropy regularization initial weight
168	gate_entropy_bonus_final: 0.01  # entropy regularization final weight
169	gate_curriculum_phase1: 50000   # forced Dt=1 phase
170	gate_curriculum_phase2: 150000  # linear ramp phase end
171	gate_enabled: false         # master switch
172	```
173	
174	**Hyperparameter search ranges**:
175	
176	| Parameter | Default | Search Range | Notes |
177	|---|---|---|---|
178	| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |
179	| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |
180	| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |
181	| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |
182	| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |
183	| `gate_entropy_bonus_init` | 0.1 | {0.05, 0.1, 0.2} | Early exploration pressure |
184	| `gate_entropy_bonus_final` | 0.01 | {0.001, 0.01, 0.05} | Prevents collapse at convergence |
185	| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |
186	
187	### A.3 WorldModel Constructor Wiring
188	
189	**File**: `models.py`, `WorldModel.__init__` (lines 30-101)
190	
191	```python
192	# After line 54 (self.dynamics = networks.RSSM(...)):
193	# Add max_dt and dt_embed_dim to RSSM constructor call:
194	self.dynamics = networks.RSSM(
195	    config.dyn_stoch,
196	    config.dyn_deter,
197	    config.dyn_hidden,
198	    config.dyn_rec_depth,
199	    config.dyn_discrete,
200	    config.act,
201	    config.norm,
202	    config.dyn_mean_act,
203	    config.dyn_std_act,
204	    config.dyn_min_std,
205	    config.unimix_ratio,
206	    config.initial,
207	    config.num_actions,
208	    self.embed_size,
209	    config.device,
210	    max_dt=config.gate_max_dt if config.gate_enabled else 1,
211	    dt_embed_dim=config.gate_dt_embed_dim,
212	)
213	```
214	
215	---
216	
217	## Module B: Event Gate Architecture
218	
219	### B.1 Gate Network
220	
221	**File**: `networks.py` (new class, insert after RSSM class ~line 291)
222	
223	```python
224	class EventGate(nn.Module):
225	    def __init__(
226	        self,
227	        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)
228	        max_dt=8,
229	        hidden_units=256,
230	        hidden_layers=2,
231	        act="SiLU",
232	        norm=True,
233	        tau_init=5.0,
234	        tau_final=0.5,
235	        tau_anneal_steps=200000,
236	    ):
237	        super(EventGate, self).__init__()
238	        self._max_dt = max_dt
239	        self._tau_init = tau_init
240	        self._tau_final = tau_final
241	        self._tau_anneal_steps = tau_anneal_steps
242	
243	        act_fn = getattr(torch.nn, act)
244	        layers = []
245	        inp_dim = feat_size
246	        for i in range(hidden_layers):
247	            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))
248	            if norm:
249	                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))
250	            layers.append(act_fn())
251	            inp_dim = hidden_units
252	        self.mlp = nn.Sequential(*layers)
253	        self.mlp.apply(tools.weight_init)
254	
255	        self.logit_layer = nn.Linear(hidden_units, max_dt)
256	        self.logit_layer.apply(tools.uniform_weight_init(0.01))
257	
258	    def get_tau(self, step):
259	        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)
260	        return self._tau_init + frac * (self._tau_final - self._tau_init)
261	
262	    def forward(self, feat, step, hard=False):
263	        """
264	        Args:
265	            feat: (batch, feat_size) - concatenated [stoch, deter]
266	            step: int - current training step for temperature annealing
267	            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)
268	        Returns:
269	            dt_onehot: (batch, max_dt) - one-hot or soft assignment
270	            dt_index:  (batch,) - integer Dt in {1,...,K}
271	            logits:    (batch, max_dt) - raw logits for entropy computation
272	        """
273	        x = self.mlp(feat)
274	        logits = self.logit_layer(x)  # (batch, max_dt)
275	
276	        tau = self.get_tau(step)
277	        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)
278	
279	        # Dt index: 1-indexed
280	        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)
281	
282	        return dt_onehot, dt_index, logits
283	
284	    def entropy(self, logits):
285	        """Categorical entropy of the gate distribution."""
286	        probs = F.softmax(logits, dim=-1)
287	        log_probs = F.log_softmax(logits, dim=-1)
288	        return -(probs * log_probs).sum(dim=-1)  # (batch,)
289	```
290	
291	### B.2 Gate in Imagination Loop
292	
293	**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)
294	
295	The gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of "wall-clock" steps consumed varies, but the loop always runs `horizon` imagined transitions.
296	
297	```python
298	def _imagine(self, start, policy, horizon):
299	    dynamics = self._world_model.dynamics
300	    gate = self._world_model.event_gate  # added to WorldModel
301	    config = self._config
302	    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))
303	    start = {k: flatten(v) for k, v in start.items()}
304	    step = self._world_model._step
305	
306	    # Determine if gate is active based on curriculum
307	    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)
308	
309	    def step_fn(prev, _):
310	        state, _, _, prev_dt = prev
311	        feat = dynamics.get_feat(state)
312	        inp = feat.detach()
313	        action = policy(inp).sample()
314	
315	        # Use previous gate decision as Dt for this transition
316	        succ = dynamics.img_step(state, action, dt=prev_dt)
317	        succ_feat = dynamics.get_feat(succ)
318	
319	        # Gate decides Dt for the NEXT step
320	        if gate_active:
321	            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)
322	        else:
323	            batch_size = succ_feat.shape[0]
324	            next_dt = torch.ones(batch_size, dtype=torch.long,
325	                                 device=succ_feat.device)
326	            gate_logits = None
327	
328	        return succ, feat, action, next_dt
329	
330	    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],
331	                         dtype=torch.long, device=config.device)
332	
333	    succ, feats, actions, dts = tools.static_scan(
334	        step_fn, [torch.arange(horizon)],
335	        (start, None, None, init_dt)
336	    )
337	    states = {k: torch.cat([start[k][None], v[:-1]], 0)
338	              for k, v in succ.items()}
339	
340	    return feats, states, actions, dts  # dts: (horizon, batch)
341	```
342	
343	### B.3 Registering Gate in WorldModel
344	
345	**File**: `models.py`, `WorldModel.__init__` (after line 86):
346	
347	```python
348	if config.gate_enabled:
349	    self.event_gate = networks.EventGate(
350	        feat_size=feat_size,
351	        max_dt=config.gate_max_dt,
352	        hidden_units=config.gate_hidden_units,
353	        hidden_layers=config.gate_hidden_layers,
354	        act=config.act,
355	        norm=config.norm,
356	        tau_init=config.gate_tau_init,
357	        tau_final=config.gate_tau_final,
358	        tau_anneal_steps=config.gate_tau_anneal_steps,
359	    )
360	else:
361	    self.event_gate = None
362	```
363	
364	---
365	
366	## Module C: Gate Supervision
367	
368	### C.1 Supervision Signal
369	
370	The gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).
371	
372	**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.
373	
374	```python
375	def compute_gate_targets(feats, max_dt):
376	    """
377	    Args:
378	        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features
379	    Returns:
380	        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt
381	    """
382	    feats = feats.detach()  # stop gradient
383	
384	    # L2 delta between consecutive states
385	    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)
386	
387	    # Normalize deltas to [0, 1] within each batch
388	    delta_min = deltas.min(dim=0, keepdim=True).values
389	    delta_max = deltas.max(dim=0, keepdim=True).values
390	    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)
391	
392	    # Large delta -> small Dt (index 0 = Dt=1)
393	    # Small delta -> large Dt (index K-1 = Dt=K)
394	    # Map normalized delta to a "preferred Dt" float in [1, K]
395	    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)
396	
397	    # Create soft target via Gaussian kernel around preferred_dt
398	    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,
399	                              device=feats.device)  # (max_dt,)
400	    # (time-1, batch, 1) vs (max_dt,)
401	    sigma = 1.0
402	    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2
403	    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)
404	
405	    return target_dist
406	```
407	
408	### C.2 Gate Loss
409	
410	```python
411	def gate_loss(gate_logits, target_dist):
412	    """
413	    Cross-entropy between gate's predicted distribution and supervision target.
414	
415	    Args:
416	        gate_logits: (time-1, batch, max_dt) - raw gate logits
417	        target_dist: (time-1, batch, max_dt) - soft target from state deltas
418	    Returns:
419	        loss: (time-1, batch) - per-step per-batch loss
420	    """
421	    log_probs = F.log_softmax(gate_logits, dim=-1)
422	    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy
423	    return loss
424	```
425	
426	### C.3 Integration in WorldModel._train
427	
428	**File**: `models.py`, `WorldModel._train` (lines 108-174)
429	
430	The gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).
431	
432	```python
433	# After line 147 (model_loss = sum(scaled.values()) + kl_loss):
434	
435	if self._config.gate_enabled and self.event_gate is not None:
436	    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM
437	    # Run gate on each timestep's features
438	    # feat shape: (batch, time, feat_dim)
439	    B, T, D = feat.shape
440	    feat_flat = feat.reshape(B * T, D)
441	    _, _, gate_logits_flat = self.event_gate(
442	        feat_flat, self._step, hard=False
443	    )
444	    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)
445	
446	    # Supervision target from state deltas (time dim = axis 1)
447	    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)
448	    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)
449	    # target_dist: (time-1, batch, max_dt)
450	
451	    # Gate logits for steps 1..T-1 (we need t and t-1)
452	    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)
453	
454	    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)
455	
456	    # Entropy bonus
457	    g_entropy = self.event_gate.entropy(
458	        g_logits.reshape(-1, self._config.gate_max_dt)
459	    ).reshape(g_loss.shape)
460	
461	    # Curriculum: scale gate loss
462	    step = self._step
463	    if step < self._config.gate_curriculum_phase1:
464	        gate_scale = 0.0  # Phase 1: no gate training
465	    elif step < self._config.gate_curriculum_phase2:
466	        # Phase 2: linear ramp
467	        progress = (step - self._config.gate_curriculum_phase1) / (
468	            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1
469	        )
470	        gate_scale = progress
471	    else:
472	        gate_scale = 1.0  # Phase 3: full gate
473	
474	    # Entropy bonus annealing: λ_H from 0.1 → 0.01
475	    entropy_frac = min(step / max(self._config.gate_tau_anneal_steps, 1), 1.0)
476	    effective_entropy_bonus = (
477	        self._config.gate_entropy_bonus_init
478	        + entropy_frac * (self._config.gate_entropy_bonus_final - self._config.gate_entropy_bonus_init)
479	    )
480	
481	    total_gate_loss = gate_scale * (
482	        self._config.gate_loss_weight * g_loss.mean()
483	        - effective_entropy_bonus * g_entropy.mean()
484	    )
485	    model_loss = model_loss + total_gate_loss
486	```
487	
488	### C.4 Stop-Gradient Design
489	
490	Critical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.
491	
492	- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input
493	- `target_dist` uses `feats.detach()` internally
494	- Only `self.event_gate` parameters receive gradients from gate loss
495	- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads
496	
497	---
498	
499	## Module D: Adapted Lambda-Returns
500	
501	### D.1 Standard vs. Adapted Lambda-Return
502	
503	**Standard** (from `tools.py:691-717`):
504	
505	$$V_t^\lambda = r_{t+1} + \gamma \left[(1-\lambda) V(s_{t+1}) + \lambda V_{t+1}^\lambda\right]$$
506	
507	**Adapted for variable Dt**:
508	
509	$$V_t^\lambda = r_{t:t+\Delta t}^{\text{cum}} + \gamma^{\Delta t} \left[(1-\lambda) V(s_{t+\Delta t}) + \lambda V_{t+\Delta t}^\lambda\right]$$
510	
511	where:
512	- $r_{t:t+\Delta t}^{\text{cum}} = \sum_{k=0}^{\Delta t - 1} \gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.
513	- $\gamma^{\Delta t}$: discount raised to the power of the stride
514	
515	### D.2 Modified lambda_return
516	
517	**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):
518	
519	```python
520	def lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):
521	    """
522	    Lambda-return with variable temporal strides.
523	
524	    Args:
525	        reward: (time, batch, 1) - per-step imagined reward
526	        value:  (time, batch, 1) - value estimates
527	        pcont:  (time, batch, 1) - continuation probability * base discount
528	        dt:     (time, batch) or (time, batch, 1) - temporal stride per step
529	        bootstrap: (batch, 1) - terminal value
530	        lambda_: float
531	        axis: int
532	    Returns:
533	        returns: list of (batch, 1) tensors
534	    """
535	    assert len(reward.shape) == len(value.shape)
536	    if isinstance(pcont, (int, float)):
537	        pcont = pcont * torch.ones_like(reward)
538	    if dt.dim() == 2:
539	        dt = dt.unsqueeze(-1)  # (time, batch, 1)
540	    dt = dt.float()
541	
542	    dims = list(range(len(reward.shape)))
543	    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]
544	    if axis != 0:
545	        reward = reward.permute(dims)
546	        value = value.permute(dims)
547	        pcont = pcont.permute(dims)
548	        dt = dt.permute(dims)
549	
550	    if bootstrap is None:
551	        bootstrap = torch.zeros_like(value[-1])
552	
553	    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),
554	    # so use it directly. gamma^Dt for the discount:
555	    pcont_adj = pcont ** dt
556	
557	    next_values = torch.cat([value[1:], bootstrap[None]], 0)
558	    inputs = reward + pcont_adj * next_values * (1 - lambda_)
559	
560	    returns = static_scan_for_lambda_return(
561	        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
562	        (inputs, pcont_adj), bootstrap
563	    )
564	    if axis != 0:
565	        returns = returns.permute(dims)
566	    return returns
567	```
568	
569	### D.3 Integration in ImagBehavior._compute_target
570	
571	**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):
572	
573	```python
574	def _compute_target(self, imag_feat, imag_state, reward, dts=None):
575	    if "cont" in self._world_model.heads:
576	        inp = self._world_model.dynamics.get_feat(imag_state)
577	        discount = self._config.discount * self._world_model.heads["cont"](inp).mean
578	    else:
579	        discount = self._config.discount * torch.ones_like(reward)
580	    value = self.value(imag_feat).mode()
581	
582	    if dts is not None and self._config.gate_enabled:
583	        target = tools.lambda_return_variable_dt(
584	            reward[1:],
585	            value[:-1],
586	            discount[1:],
587	            dts[1:],  # Dt for each imagined step
588	            bootstrap=value[-1],
589	            lambda_=self._config.discount_lambda,
590	            axis=0,
591	        )
592	    else:
593	        target = tools.lambda_return(
594	            reward[1:],
595	            value[:-1],
596	            discount[1:],
597	            bootstrap=value[-1],
598	            lambda_=self._config.discount_lambda,
599	            axis=0,
600	        )
601	
602	    # Adjusted weights: cumulative discount accounts for variable Dt
603	    if dts is not None and self._config.gate_enabled:
604	        pcont_adj = discount ** dts.unsqueeze(-1).float()
605	        weights = torch.cumprod(
606	            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0
607	        ).detach()
608	    else:
609	        weights = torch.cumprod(
610	            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0
611	        ).detach()
612	
613	    return target, weights, value[:-1]
614	```
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
629	# effective_entropy_bonus anneals from gate_entropy_bonus_init (0.1)
630	# to gate_entropy_bonus_final (0.01) over gate_tau_anneal_steps
631	total_gate_loss = gate_scale * (
632	    config.gate_loss_weight * g_loss.mean()
633	    - effective_entropy_bonus * g_entropy.mean()  # maximize entropy
634	```
635	
636	The entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient anneals from `λ_H=0.1` (strong early exploration) to `λ_H=0.01` (convergence), following the same schedule as Gumbel-Softmax temperature. High initial λ_H prevents the gate from committing to a narrow Δt range before the RSSM has learned good dynamics.
637	
638	### E.3 Gating Curriculum (Three Phases)
639	
640	| Phase | Steps | Behavior | Rationale |
641	|---|---|---|---|
642	| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |
643	| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |
644	| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |
645	
646	Implementation (already shown in Module C.3):
647	
648	```python
649	if step < config.gate_curriculum_phase1:
650	    gate_scale = 0.0
651	elif step < config.gate_curriculum_phase2:
652	    progress = (step - config.gate_curriculum_phase1) / (
653	        config.gate_curriculum_phase2 - config.gate_curriculum_phase1
654	    )
655	    gate_scale = progress
656	else:
657	    gate_scale = 1.0
658	```
659	
660	In `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.
661	
662	### E.4 Collapse Detection Metrics
663	
664	**File**: `models.py`, add to metrics in `ImagBehavior._train`:
665	
666	```python
667	if self._config.gate_enabled and dts is not None:
668	    dts_float = dts.float()
669	    metrics["gate_dt_mean"] = to_np(torch.mean(dts_float))
670	    metrics["gate_dt_std"] = to_np(torch.std(dts_float))
671	    metrics["gate_dt_min"] = to_np(torch.min(dts_float))
672	    metrics["gate_dt_max"] = to_np(torch.max(dts_float))
673	
674	    # Distribution over K bins
675	    dt_counts = torch.bincount(
676	        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1
677	    )[1:]  # skip bin 0
678	    dt_dist = dt_counts.float() / dt_counts.sum()
679	    for k in range(self._config.gate_max_dt):
680	        metrics[f"gate_dt_{k+1}_frac"] = to_np(dt_dist[k])
681	
682	    # Entropy of empirical Dt distribution (collapse indicator)
683	    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()
684	    metrics["gate_empirical_entropy"] = to_np(emp_entropy)
685	    max_entropy = np.log(self._config.gate_max_dt)
686	    metrics["gate_entropy_ratio"] = to_np(emp_entropy) / max_entropy
687	```
688	
689	**Collapse alert thresholds**:
690	- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values
691	- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed
692	- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating
693	- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates
694	
695	### E.5 Automatic Recovery (Optional)
696	
697	If collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:
698	
699	```python
700	if gate_entropy_ratio < 0.2:
701	    effective_entropy_bonus = config.gate_entropy_bonus_init  # reset to initial high value
702	else:
703	    # normal annealing (see Module C.3)
704	    pass
705	```
706	
707	This is optional and aggressive. Prefer tuning the base entropy bonus instead.
708	
709	---
710	
711	## Module F: Variable-Δt Replay Sub-Sampling
712	
713	### F.1 Motivation
714	
715	To teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.
716	
717	### F.2 Sub-Sampling Procedure
718	
719	For each training batch:
720	
721	1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.
722	2. For each batch element, independently draw a stride from a **log-uniform distribution**:
723	   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).
724	3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.
725	4. For each gap of Δt frames, compute:
726	   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`
727	   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`
728	5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).
729	
730	Within a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.
731	
732	### F.3 Implementation
733	
734	**File**: `tools.py` (new function)
735	
736	```python
737	def subsample_variable_dt(data, max_dt, discount):
738	    """
739	    Variable-Δt sub-sampling of replay trajectories.
740	
741	    Args:
742	        data: dict of (batch, time, ...) tensors — must include
743	              'action', 'reward', 'cont' (and observation keys).
744	        max_dt: int — K, maximum temporal stride.
745	        discount: float — γ, environment discount factor.
746	    Returns:
747	        data_sub: dict of (batch, time', ...) sub-sampled tensors.
748	        dt_labels: (batch, time') int tensor, stride used per step.
749	    """
750	    B, T = data["action"].shape[:2]
751	    device = data["action"].device
752	
753	    # Sample per-element Δt from log-uniform over [1, K]
754	    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))
755	    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)
756	
757	    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))
758	    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused
759	    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()
760	    T_sub = sub_len.max().item()
761	
762	    # Build index and aggregate tensors
763	    data_sub = {}
764	    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)
765	    reward_cum = torch.zeros(B, T_sub, *data["reward"].shape[2:], device=device)
766	    cont_min = torch.ones(B, T_sub, *data["cont"].shape[2:], device=device)
767	
768	    for b in range(B):
769	        dt_b = dt_per_elem[b].item()
770	        indices = list(range(0, T, dt_b))
771	        L = len(indices)
772	
773	        # Sub-sample observation / action tensors
774	        for key in data:
775	            if key not in data_sub:
776	                data_sub[key] = torch.zeros(
777	                    B, T_sub, *data[key].shape[2:],
778	                    dtype=data[key].dtype, device=device,
779	                )
780	            data_sub[key][b, :L] = data[key][b, indices]
781	
782	        # Cumulative discounted reward and min continuation
783	        for i, t_start in enumerate(indices[:-1]):
784	            t_end = min(t_start + dt_b, T)
785	            gamma_powers = discount ** torch.arange(
786	                t_end - t_start, dtype=torch.float, device=device
787	            )
788	            reward_cum[b, i] = (
789	                gamma_powers.unsqueeze(-1) * data["reward"][b, t_start:t_end]
790	            ).sum(dim=0)
791	            cont_min[b, i] = data["cont"][b, t_start:t_end].min(dim=0).values
792	
793	        dt_labels[b, :L] = dt_b
794	
795	    data_sub["reward"] = reward_cum
796	    data_sub["cont"] = cont_min
797	    return data_sub, dt_labels
798	```
799	
800	### F.4 Integration in WorldModel._train
801	
802	**File**: `models.py`, `WorldModel._train`
803	
804	```python
805	# Before calling self.dynamics.observe():
806	if self._config.gate_enabled:
807	    data, dt_labels = tools.subsample_variable_dt(
808	        data, self._config.gate_max_dt, self._config.discount,
809	    )
810	    # dt_labels: (batch, time') — passed to observe → obs_step → img_step
811	else:
812	    dt_labels = None
813	```
814	
815	The `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).
816	
817	### F.5 Design Notes
818	
819	- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.
820	- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.
821	- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.
822	- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal.
823	
824	---
825	
826	## File Modification Summary
827	
828	| File | Function/Class | Lines | Change Type |
829	|---|---|---|---|
830	| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |
831	| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |
832	| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |
833	| `networks.py` | `RSSM.obs_step` | 174-206 | Modify: add `dt` param, forward to `img_step` |
834	| `networks.py` | `RSSM.observe` | 127-143 | Modify: accept and forward per-step `dt` labels |
835	| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |
836	| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax (τ_init=5.0) |
837	| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |
838	| `models.py` | `WorldModel._train` | 108-174 | Modify: add variable-Δt sub-sampling + gate loss |
839	| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |
840	| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` (reward already cumulative) |
841	| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |
842	| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return (uses cumulative reward directly) |
843	| `tools.py` | (new) `subsample_variable_dt` | new | Add: log-uniform Δt sub-sampling with cumulative reward / min-cont |
844	| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters (τ_init=5.0) |
845	
846	---
847	
848	## Risks and Mitigations
849	
850	### R1: Training Instability
851	
852	**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.
853	
854	**Mitigation**:
855	- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible
856	- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate
857	- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences
858	
859	### R2: Gate Collapse
860	
861	**Risk**: Gate degenerates to constant Dt, losing adaptivity.
862	
863	**Mitigation**:
864	- Entropy regularization in gate loss
865	- Curriculum prevents premature commitment
866	- Monitoring metrics with alert thresholds (Section E.4)
867	- Gumbel-Softmax temperature annealing ensures exploration early on
868	
869	### R3: Reward Prediction Under Variable Δt
870	
871	**Risk**: The reward head must generalize across different Δt values, predicting cumulative discounted rewards for strides it may not have seen frequently.
872	
873	**Mitigation**:
874	- Log-uniform Δt sampling (Module F) provides balanced training coverage across all stride values
875	- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)
876	- The gate supervision ensures large Δt is chosen only when state changes are small, correlating with low reward variance — the easier prediction regime
877	- Monitor `imag_reward` statistics for anomalies across different Δt values
878	
879	### R4: Compatibility with Original DreamerV3
880	
881	**Risk**: Modified code breaks when `gate_enabled=false`.
882	
883	**Mitigation**:
884	- All gate logic is guarded by `config.gate_enabled`
885	- `img_step` defaults `dt=None` which maps to Dt=1
886	- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)
887	- `_compute_target` falls back to standard `lambda_return`
888	- Net-zero change to behavior when `gate_enabled=false`
889	
890	### R5: Computational Overhead
891	
892	**Risk**: Gate MLP adds forward-pass cost in imagination.
893	
894	**Mitigation**:
895	- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)
896	- Gate is only called during imagination (not observation/training unroll)
897	- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute
898	
899	### R6: Replay Buffer Sub-Sampling Overhead
900	
901	**Risk**: Variable-Δt sub-sampling (Module F) reduces effective sequence length, discarding some frames per batch.
902	
903	**Mitigation**:
904	- Log-uniform distribution means ~50% of batch elements get Δt ≤ 2, preserving fine-grained temporal resolution for most of the batch
905	- Sub-sampled frames still contribute via cumulative reward and min-continuation aggregation — no information is fully discarded
906	- The standard (Δt=1) training path remains active for half the batch, maintaining RSSM's single-step prediction quality
907	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "62bd9d3c-f684-435c-a677-f8c824696df8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/implementation_design.md",
      "content": "# Event-Gated Adaptive-Horizon RSSM: Implementation Design\n\n**Codebase**: NM512/dreamerv3-torch (PyTorch)\n**Core idea**: A learned event gate on top of the RSSM decides per-step temporal stride Dt in {1,...,K}, enabling variable-rate imagination that extends the effective planning horizon without proportionally increasing compute.\n\n---\n\n## Architecture Overview (ASCII)\n\n```\n                          IMAGINATION LOOP\n ┌──────────────────────────────────────────────────────────────────────┐\n │                                                                      │\n │  ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌───────────────┐  │\n │  │ prev    │    │           │    │          │    │               │  │\n │  │ stoch_t │───▶│  concat   │───▶│ img_in   │───▶│   GRU Cell    │  │\n │  │         │    │           │    │ layers   │    │               │  │\n │  └─────────┘    │  + action │    └──────────┘    └───────┬───────┘  │\n │                 │  + Dt_emb │                            │          │\n │                 └───────────┘                       deter_t         │\n │                       ▲                                 │          │\n │                       │                                 ▼          │\n │              ┌────────┴───────┐              ┌──────────────────┐  │\n │              │  Dt Embedding  │              │  img_out_layers  │  │\n │              │  (learned,     │              └────────┬─────────┘  │\n │              │   dim=32)      │                       │            │\n │              └────────┬───────┘                       ▼            │\n │                       │                      ┌──────────────────┐  │\n │                       │                      │  stats layer     │  │\n │                       │                      │  -> stoch_t      │  │\n │              ┌────────┴───────┐              └────────┬─────────┘  │\n │              │  EVENT GATE    │                       │            │\n │              │  MLP(h_t, z_t) │◀──────────────────────┤            │\n │              │                │                       │            │\n │              │  Gumbel-       │              ┌────────┴─────────┐  │\n │              │  Softmax       │              │  feat_t =        │  │\n │              │  -> Dt_{t+1}   │              │  [stoch_t;       │  │\n │              └────────────────┘              │   deter_t]       │  │\n │                                              └────────┬─────────┘  │\n │                                                       │            │\n │                                                       ▼            │\n │                                              ┌──────────────────┐  │\n │                                              │  Actor / Critic  │  │\n │                                              │  Reward / Cont   │  │\n │                                              └──────────────────┘  │\n │                                                                      │\n └──────────────────────────────────────────────────────────────────────┘\n\nGate supervision (training only):\n  delta = || feat_t - feat_{t-1} ||_2   (stop-gradient on both)\n  target: large delta -> small Dt, small delta -> large Dt\n```\n\n---\n\n## Module A: Variable-Rate RSSM Modifications\n\n### A.1 Core Change: Dt Embedding in GRU Input\n\nThe RSSM's `img_step` currently concatenates `prev_stoch` and `prev_action` as GRU input. We add a learned embedding of the temporal stride Dt.\n\n**File**: `networks.py`\n\n**Constructor changes** (`RSSM.__init__`, lines 14-98):\n\n```python\n# New parameters in __init__ signature:\n#   max_dt: int = 8          # K, maximum temporal stride\n#   dt_embed_dim: int = 32   # dimensionality of Dt embedding\n\n# After line 46 (self._device = device):\nself._max_dt = max_dt\nself._dt_embed_dim = dt_embed_dim\nself._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\nnn.init.normal_(self._dt_embedding.weight, std=0.01)\n\n# Modify inp_dim calculation (lines 49-52):\n# Original:\n#   if self._discrete:\n#       inp_dim = self._stoch * self._discrete + num_actions\n#   else:\n#       inp_dim = self._stoch + num_actions\n# New:\nif self._discrete:\n    inp_dim = self._stoch * self._discrete + num_actions + dt_embed_dim\nelse:\n    inp_dim = self._stoch + num_actions + dt_embed_dim\n```\n\n**`img_step` changes** (lines 208-233):\n\n```python\ndef img_step(self, prev_state, prev_action, dt=None, sample=True):\n    prev_stoch = prev_state[\"stoch\"]\n    if self._discrete:\n        shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n        prev_stoch = prev_stoch.reshape(shape)\n\n    # Dt embedding: default to dt=1 if not provided (backward compat)\n    if dt is None:\n        dt = torch.ones(prev_stoch.shape[0], dtype=torch.long,\n                        device=prev_stoch.device)\n    # dt is 1-indexed {1,...,K}, embedding is 0-indexed\n    dt_emb = self._dt_embedding(dt - 1)  # (batch, dt_embed_dim)\n\n    x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n    x = self._img_in_layers(x)\n    for _ in range(self._rec_depth):\n        deter = prev_state[\"deter\"]\n        x, deter = self._cell(x, [deter])\n        deter = deter[0]\n    x = self._img_out_layers(x)\n    stats = self._suff_stats_layer(\"ims\", x)\n    if sample:\n        stoch = self.get_dist(stats).sample()\n    else:\n        stoch = self.get_dist(stats).mode()\n    prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n    return prior\n```\n\n**`obs_step` changes** (lines 174-206): `obs_step` must accept an optional `dt` parameter and forward it to `img_step`. During variable-Δt training (Module F), the RSSM sees sub-sampled trajectories where Δt > 1.\n\n```python\ndef obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n    # ... (existing reset / mask logic unchanged) ...\n    prior = self.img_step(prev_state, prev_action, dt=dt)\n    # ... (existing posterior computation unchanged) ...\n    return post, prior\n```\n\n**`observe` changes** (lines 127-143): When training with variable-Δt sub-sampling (Module F), the `observe` loop receives per-step `dt` labels and passes them to `obs_step`.\n\n**`imagine_with_action` changes** (lines 145-152): Add optional `dt_sequence` parameter:\n\n```python\ndef imagine_with_action(self, action, state, dt_sequence=None):\n    swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n    action = swap(action)\n    if dt_sequence is not None:\n        dt_sequence = swap(dt_sequence)\n        prior = tools.static_scan(\n            lambda s, a, dt: self.img_step(s, a, dt=dt),\n            [action, dt_sequence], state\n        )\n    else:\n        prior = tools.static_scan(self.img_step, [action], state)\n    prior = prior[0]\n    prior = {k: swap(v) for k, v in prior.items()}\n    return prior\n```\n\n### A.2 Config Additions\n\n**File**: `configs.yaml`, under `defaults`:\n\n```yaml\n# Event-Gated Adaptive Horizon\ngate_max_dt: 8              # K: max temporal stride\ngate_dt_embed_dim: 32       # Dt embedding dimension\ngate_hidden_units: 256      # gate MLP hidden size\ngate_hidden_layers: 2       # gate MLP depth\ngate_tau_init: 5.0          # Gumbel-Softmax initial temperature\ngate_tau_final: 0.5         # Gumbel-Softmax final temperature\ngate_tau_anneal_steps: 200000  # linear anneal duration\ngate_loss_weight: 1.0       # gate supervision loss coefficient\ngate_entropy_bonus_init: 0.1    # entropy regularization initial weight\ngate_entropy_bonus_final: 0.01  # entropy regularization final weight\ngate_curriculum_phase1: 50000   # forced Dt=1 phase\ngate_curriculum_phase2: 150000  # linear ramp phase end\ngate_enabled: false         # master switch\n```\n\n**Hyperparameter search ranges**:\n\n| Parameter | Default | Search Range | Notes |\n|---|---|---|---|\n| `gate_max_dt` | 8 | {4, 8, 16} | K=4 conservative, K=16 aggressive |\n| `gate_dt_embed_dim` | 32 | {16, 32, 64} | Larger if K is large |\n| `gate_hidden_units` | 256 | {128, 256, 512} | Scale with dyn_deter |\n| `gate_tau_final` | 0.5 | {0.1, 0.3, 0.5, 1.0} | Lower = harder decisions |\n| `gate_loss_weight` | 1.0 | {0.1, 0.5, 1.0, 5.0} | Critical for stability |\n| `gate_entropy_bonus_init` | 0.1 | {0.05, 0.1, 0.2} | Early exploration pressure |\n| `gate_entropy_bonus_final` | 0.01 | {0.001, 0.01, 0.05} | Prevents collapse at convergence |\n| `gate_curriculum_phase1` | 50000 | {25K, 50K, 100K} | Depends on env convergence |\n\n### A.3 WorldModel Constructor Wiring\n\n**File**: `models.py`, `WorldModel.__init__` (lines 30-101)\n\n```python\n# After line 54 (self.dynamics = networks.RSSM(...)):\n# Add max_dt and dt_embed_dim to RSSM constructor call:\nself.dynamics = networks.RSSM(\n    config.dyn_stoch,\n    config.dyn_deter,\n    config.dyn_hidden,\n    config.dyn_rec_depth,\n    config.dyn_discrete,\n    config.act,\n    config.norm,\n    config.dyn_mean_act,\n    config.dyn_std_act,\n    config.dyn_min_std,\n    config.unimix_ratio,\n    config.initial,\n    config.num_actions,\n    self.embed_size,\n    config.device,\n    max_dt=config.gate_max_dt if config.gate_enabled else 1,\n    dt_embed_dim=config.gate_dt_embed_dim,\n)\n```\n\n---\n\n## Module B: Event Gate Architecture\n\n### B.1 Gate Network\n\n**File**: `networks.py` (new class, insert after RSSM class ~line 291)\n\n```python\nclass EventGate(nn.Module):\n    def __init__(\n        self,\n        feat_size,      # dyn_stoch * dyn_discrete + dyn_deter (e.g. 32*32+512=1536)\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) - concatenated [stoch, deter]\n            step: int - current training step for temperature annealing\n            hard: bool - if True, use hard Gumbel-Softmax (argmax in forward)\n        Returns:\n            dt_onehot: (batch, max_dt) - one-hot or soft assignment\n            dt_index:  (batch,) - integer Dt in {1,...,K}\n            logits:    (batch, max_dt) - raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)  # (batch, max_dt)\n\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n\n        # Dt index: 1-indexed\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1  # (batch,)\n\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)  # (batch,)\n```\n\n### B.2 Gate in Imagination Loop\n\n**File**: `models.py`, `ImagBehavior._imagine` (lines 351-369)\n\nThe gate is called **after** each `img_step` to decide Dt for the **next** step. During imagination, the actual number of \"wall-clock\" steps consumed varies, but the loop always runs `horizon` imagined transitions.\n\n```python\ndef _imagine(self, start, policy, horizon):\n    dynamics = self._world_model.dynamics\n    gate = self._world_model.event_gate  # added to WorldModel\n    config = self._config\n    flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n    start = {k: flatten(v) for k, v in start.items()}\n    step = self._world_model._step\n\n    # Determine if gate is active based on curriculum\n    gate_active = (config.gate_enabled and step > config.gate_curriculum_phase1)\n\n    def step_fn(prev, _):\n        state, _, _, prev_dt = prev\n        feat = dynamics.get_feat(state)\n        inp = feat.detach()\n        action = policy(inp).sample()\n\n        # Use previous gate decision as Dt for this transition\n        succ = dynamics.img_step(state, action, dt=prev_dt)\n        succ_feat = dynamics.get_feat(succ)\n\n        # Gate decides Dt for the NEXT step\n        if gate_active:\n            _, next_dt, gate_logits = gate(succ_feat.detach(), step, hard=True)\n        else:\n            batch_size = succ_feat.shape[0]\n            next_dt = torch.ones(batch_size, dtype=torch.long,\n                                 device=succ_feat.device)\n            gate_logits = None\n\n        return succ, feat, action, next_dt\n\n    init_dt = torch.ones(start[list(start.keys())[0]].shape[0],\n                         dtype=torch.long, device=config.device)\n\n    succ, feats, actions, dts = tools.static_scan(\n        step_fn, [torch.arange(horizon)],\n        (start, None, None, init_dt)\n    )\n    states = {k: torch.cat([start[k][None], v[:-1]], 0)\n              for k, v in succ.items()}\n\n    return feats, states, actions, dts  # dts: (horizon, batch)\n```\n\n### B.3 Registering Gate in WorldModel\n\n**File**: `models.py`, `WorldModel.__init__` (after line 86):\n\n```python\nif config.gate_enabled:\n    self.event_gate = networks.EventGate(\n        feat_size=feat_size,\n        max_dt=config.gate_max_dt,\n        hidden_units=config.gate_hidden_units,\n        hidden_layers=config.gate_hidden_layers,\n        act=config.act,\n        norm=config.norm,\n        tau_init=config.gate_tau_init,\n        tau_final=config.gate_tau_final,\n        tau_anneal_steps=config.gate_tau_anneal_steps,\n    )\nelse:\n    self.event_gate = None\n```\n\n---\n\n## Module C: Gate Supervision\n\n### C.1 Supervision Signal\n\nThe gate should predict small Dt when latent state changes rapidly (needs fine temporal resolution) and large Dt when state is static (can skip ahead).\n\n**Supervision target**: soft label derived from `||feat_t - feat_{t-1}||_2`.\n\n```python\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"\n    Args:\n        feats: (time, batch, feat_dim) - STOP-GRADIENT latent features\n    Returns:\n        target_dist: (time-1, batch, max_dt) - soft target distribution over Dt\n    \"\"\"\n    feats = feats.detach()  # stop gradient\n\n    # L2 delta between consecutive states\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n\n    # Normalize deltas to [0, 1] within each batch\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n\n    # Large delta -> small Dt (index 0 = Dt=1)\n    # Small delta -> large Dt (index K-1 = Dt=K)\n    # Map normalized delta to a \"preferred Dt\" float in [1, K]\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)  # (time-1, batch)\n\n    # Create soft target via Gaussian kernel around preferred_dt\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32,\n                              device=feats.device)  # (max_dt,)\n    # (time-1, batch, 1) vs (max_dt,)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)  # (time-1, batch, max_dt)\n\n    return target_dist\n```\n\n### C.2 Gate Loss\n\n```python\ndef gate_loss(gate_logits, target_dist):\n    \"\"\"\n    Cross-entropy between gate's predicted distribution and supervision target.\n\n    Args:\n        gate_logits: (time-1, batch, max_dt) - raw gate logits\n        target_dist: (time-1, batch, max_dt) - soft target from state deltas\n    Returns:\n        loss: (time-1, batch) - per-step per-batch loss\n    \"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    loss = -(target_dist * log_probs).sum(dim=-1)  # cross-entropy\n    return loss\n```\n\n### C.3 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train` (lines 108-174)\n\nThe gate is trained jointly with the world model. Gate supervision uses features from the posterior (already computed).\n\n```python\n# After line 147 (model_loss = sum(scaled.values()) + kl_loss):\n\nif self._config.gate_enabled and self.event_gate is not None:\n    feat = self.dynamics.get_feat(post).detach()  # stop gradient to RSSM\n    # Run gate on each timestep's features\n    # feat shape: (batch, time, feat_dim)\n    B, T, D = feat.shape\n    feat_flat = feat.reshape(B * T, D)\n    _, _, gate_logits_flat = self.event_gate(\n        feat_flat, self._step, hard=False\n    )\n    gate_logits = gate_logits_flat.reshape(B, T, self._config.gate_max_dt)\n\n    # Supervision target from state deltas (time dim = axis 1)\n    feat_time = feat.permute(1, 0, 2)  # (time, batch, feat_dim)\n    target_dist = compute_gate_targets(feat_time, self._config.gate_max_dt)\n    # target_dist: (time-1, batch, max_dt)\n\n    # Gate logits for steps 1..T-1 (we need t and t-1)\n    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)  # (time-1, batch, max_dt)\n\n    g_loss = gate_loss(g_logits, target_dist)  # (time-1, batch)\n\n    # Entropy bonus\n    g_entropy = self.event_gate.entropy(\n        g_logits.reshape(-1, self._config.gate_max_dt)\n    ).reshape(g_loss.shape)\n\n    # Curriculum: scale gate loss\n    step = self._step\n    if step < self._config.gate_curriculum_phase1:\n        gate_scale = 0.0  # Phase 1: no gate training\n    elif step < self._config.gate_curriculum_phase2:\n        # Phase 2: linear ramp\n        progress = (step - self._config.gate_curriculum_phase1) / (\n            self._config.gate_curriculum_phase2 - self._config.gate_curriculum_phase1\n        )\n        gate_scale = progress\n    else:\n        gate_scale = 1.0  # Phase 3: full gate\n\n    # Entropy bonus annealing: λ_H from 0.1 → 0.01\n    entropy_frac = min(step / max(self._config.gate_tau_anneal_steps, 1), 1.0)\n    effective_entropy_bonus = (\n        self._config.gate_entropy_bonus_init\n        + entropy_frac * (self._config.gate_entropy_bonus_final - self._config.gate_entropy_bonus_init)\n    )\n\n    total_gate_loss = gate_scale * (\n        self._config.gate_loss_weight * g_loss.mean()\n        - effective_entropy_bonus * g_entropy.mean()\n    )\n    model_loss = model_loss + total_gate_loss\n```\n\n### C.4 Stop-Gradient Design\n\nCritical: the gate loss must **not** backpropagate into the RSSM. The gate learns to *read* the latent dynamics, not to *shape* them.\n\n- `feat = self.dynamics.get_feat(post).detach()` -- stop gradient before gate input\n- `target_dist` uses `feats.detach()` internally\n- Only `self.event_gate` parameters receive gradients from gate loss\n- The gate is included in `self.parameters()` via `nn.Module` registration, so the existing `self._model_opt` optimizer will update it alongside the world model heads\n\n---\n\n## Module D: Adapted Lambda-Returns\n\n### D.1 Standard vs. Adapted Lambda-Return\n\n**Standard** (from `tools.py:691-717`):\n\n$$V_t^\\lambda = r_{t+1} + \\gamma \\left[(1-\\lambda) V(s_{t+1}) + \\lambda V_{t+1}^\\lambda\\right]$$\n\n**Adapted for variable Dt**:\n\n$$V_t^\\lambda = r_{t:t+\\Delta t}^{\\text{cum}} + \\gamma^{\\Delta t} \\left[(1-\\lambda) V(s_{t+\\Delta t}) + \\lambda V_{t+\\Delta t}^\\lambda\\right]$$\n\nwhere:\n- $r_{t:t+\\Delta t}^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k r_{t+k}$: cumulative discounted reward, pre-computed during sub-sampling (Module F). The reward head is trained to directly predict this quantity, so no approximation is needed at imagination time.\n- $\\gamma^{\\Delta t}$: discount raised to the power of the stride\n\n### D.2 Modified lambda_return\n\n**File**: `tools.py`, new function alongside existing `lambda_return` (line 691):\n\n```python\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"\n    Lambda-return with variable temporal strides.\n\n    Args:\n        reward: (time, batch, 1) - per-step imagined reward\n        value:  (time, batch, 1) - value estimates\n        pcont:  (time, batch, 1) - continuation probability * base discount\n        dt:     (time, batch) or (time, batch, 1) - temporal stride per step\n        bootstrap: (batch, 1) - terminal value\n        lambda_: float\n        axis: int\n    Returns:\n        returns: list of (batch, 1) tensors\n    \"\"\"\n    assert len(reward.shape) == len(value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)  # (time, batch, 1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    # Reward is already cumulative-discounted (pre-computed in Module F sub-sampling),\n    # so use it directly. gamma^Dt for the discount:\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n```\n\n### D.3 Integration in ImagBehavior._compute_target\n\n**File**: `models.py`, `ImagBehavior._compute_target` (lines 371-389):\n\n```python\ndef _compute_target(self, imag_feat, imag_state, reward, dts=None):\n    if \"cont\" in self._world_model.heads:\n        inp = self._world_model.dynamics.get_feat(imag_state)\n        discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n    else:\n        discount = self._config.discount * torch.ones_like(reward)\n    value = self.value(imag_feat).mode()\n\n    if dts is not None and self._config.gate_enabled:\n        target = tools.lambda_return_variable_dt(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            dts[1:],  # Dt for each imagined step\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n    else:\n        target = tools.lambda_return(\n            reward[1:],\n            value[:-1],\n            discount[1:],\n            bootstrap=value[-1],\n            lambda_=self._config.discount_lambda,\n            axis=0,\n        )\n\n    # Adjusted weights: cumulative discount accounts for variable Dt\n    if dts is not None and self._config.gate_enabled:\n        pcont_adj = discount ** dts.unsqueeze(-1).float()\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n        ).detach()\n    else:\n        weights = torch.cumprod(\n            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n        ).detach()\n\n    return target, weights, value[:-1]\n```\n\n---\n\n## Module E: Gate Collapse Prevention\n\n### E.1 Failure Modes\n\nGate collapse = the gate converges to always outputting the same Dt (typically Dt=1 or Dt=K). This removes the adaptive benefit entirely.\n\n### E.2 Entropy Regularization\n\nAlready included in Module C's loss:\n\n```python\n# effective_entropy_bonus anneals from gate_entropy_bonus_init (0.1)\n# to gate_entropy_bonus_final (0.01) over gate_tau_anneal_steps\ntotal_gate_loss = gate_scale * (\n    config.gate_loss_weight * g_loss.mean()\n    - effective_entropy_bonus * g_entropy.mean()  # maximize entropy\n```\n\nThe entropy bonus encourages the gate to maintain uncertainty across Dt choices. The coefficient anneals from `λ_H=0.1` (strong early exploration) to `λ_H=0.01` (convergence), following the same schedule as Gumbel-Softmax temperature. High initial λ_H prevents the gate from committing to a narrow Δt range before the RSSM has learned good dynamics.\n\n### E.3 Gating Curriculum (Three Phases)\n\n| Phase | Steps | Behavior | Rationale |\n|---|---|---|---|\n| 1 | 0 ~ 50K | Dt forced to 1, gate loss weight = 0 | RSSM must first learn good dynamics with standard DreamerV3 |\n| 2 | 50K ~ 150K | Gate loss linearly ramped from 0 to 1, Dt in imagination uses gate | Gradual introduction; RSSM adapts to variable Dt |\n| 3 | 150K+ | Full gating, gate_scale = 1.0 | Free optimization |\n\nImplementation (already shown in Module C.3):\n\n```python\nif step < config.gate_curriculum_phase1:\n    gate_scale = 0.0\nelif step < config.gate_curriculum_phase2:\n    progress = (step - config.gate_curriculum_phase1) / (\n        config.gate_curriculum_phase2 - config.gate_curriculum_phase1\n    )\n    gate_scale = progress\nelse:\n    gate_scale = 1.0\n```\n\nIn `_imagine`, the gate is only activated when `step > gate_curriculum_phase1`.\n\n### E.4 Collapse Detection Metrics\n\n**File**: `models.py`, add to metrics in `ImagBehavior._train`:\n\n```python\nif self._config.gate_enabled and dts is not None:\n    dts_float = dts.float()\n    metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n    metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n    metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n    metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n\n    # Distribution over K bins\n    dt_counts = torch.bincount(\n        dts.reshape(-1).long(), minlength=self._config.gate_max_dt + 1\n    )[1:]  # skip bin 0\n    dt_dist = dt_counts.float() / dt_counts.sum()\n    for k in range(self._config.gate_max_dt):\n        metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n\n    # Entropy of empirical Dt distribution (collapse indicator)\n    emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n    metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n    max_entropy = np.log(self._config.gate_max_dt)\n    metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n```\n\n**Collapse alert thresholds**:\n- `gate_entropy_ratio < 0.3`: **Warning** -- gate is concentrating on few Dt values\n- `gate_entropy_ratio < 0.1`: **Critical** -- gate has likely collapsed\n- `gate_dt_std < 0.5`: **Warning** -- nearly deterministic gating\n- Any single `gate_dt_k_frac > 0.8`: **Warning** -- one Dt dominates\n\n### E.5 Automatic Recovery (Optional)\n\nIf collapse is detected during Phase 3, one mitigation is to temporarily boost the entropy bonus:\n\n```python\nif gate_entropy_ratio < 0.2:\n    effective_entropy_bonus = config.gate_entropy_bonus_init  # reset to initial high value\nelse:\n    # normal annealing (see Module C.3)\n    pass\n```\n\nThis is optional and aggressive. Prefer tuning the base entropy bonus instead.\n\n---\n\n## Module F: Variable-Δt Replay Sub-Sampling\n\n### F.1 Motivation\n\nTo teach the RSSM to predict across different temporal strides, training must include variable-Δt transitions. We achieve this by **sub-sampling trajectories from the replay buffer** at randomly chosen Δt during each training batch, with pre-computed cumulative rewards and minimum continuation flags for skipped frames.\n\n### F.2 Sub-Sampling Procedure\n\nFor each training batch:\n\n1. Sample a standard `(batch, seq_len=64)` trajectory from the replay buffer.\n2. For each batch element, independently draw a stride from a **log-uniform distribution**:\n   `dt = clamp(round(exp(uniform(0, log(K)))), 1, K)` where `K = gate_max_dt` (default 8).\n3. Sub-sample the trajectory by retaining frames at indices `t = 0, Δt, 2Δt, ...`.\n4. For each gap of Δt frames, compute:\n   - **Cumulative discounted reward**: `r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k}`\n   - **Minimum continuation probability**: `c_min = min_{k=0}^{Δt-1} c_{t+k}`\n5. Attach Δt as a per-step label for the RSSM (`obs_step` receives `dt`).\n\nWithin a single batch element, Δt is fixed (all gaps use the same stride). Different batch elements may have different Δt values.\n\n### F.3 Implementation\n\n**File**: `tools.py` (new function)\n\n```python\ndef subsample_variable_dt(data, max_dt, discount):\n    \"\"\"\n    Variable-Δt sub-sampling of replay trajectories.\n\n    Args:\n        data: dict of (batch, time, ...) tensors — must include\n              'action', 'reward', 'cont' (and observation keys).\n        max_dt: int — K, maximum temporal stride.\n        discount: float — γ, environment discount factor.\n    Returns:\n        data_sub: dict of (batch, time', ...) sub-sampled tensors.\n        dt_labels: (batch, time') int tensor, stride used per step.\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    # Sample per-element Δt from log-uniform over [1, K]\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)\n\n    # Determine sub-sampled length (worst case: dt=K → ceil(T/K))\n    max_sublen = (T + max_dt - 1) // 1  # allocate full length, mask unused\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    # Build index and aggregate tensors\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        # Sub-sample observation / action tensors\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        # Cumulative discounted reward and min continuation\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            gamma_powers = discount ** torch.arange(\n                t_end - t_start, dtype=torch.float, device=device\n            )\n            reward_cum[b, i] = (\n                gamma_powers.unsqueeze(-1) * data[\"reward\"][b, t_start:t_end]\n            ).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n```\n\n### F.4 Integration in WorldModel._train\n\n**File**: `models.py`, `WorldModel._train`\n\n```python\n# Before calling self.dynamics.observe():\nif self._config.gate_enabled:\n    data, dt_labels = tools.subsample_variable_dt(\n        data, self._config.gate_max_dt, self._config.discount,\n    )\n    # dt_labels: (batch, time') — passed to observe → obs_step → img_step\nelse:\n    dt_labels = None\n```\n\nThe `observe` loop forwards `dt_labels` to `obs_step`, which in turn passes `dt` to `img_step` (see Module A.1).\n\n### F.5 Design Notes\n\n- **Log-uniform distribution** ensures balanced coverage: `P(Δt=1) ≈ P(Δt=2) ≈ P(Δt=4) ≈ P(Δt=8)` on a log scale. This avoids over-representing small strides.\n- **Per-element fixed Δt** simplifies batching (no ragged sequences). A future extension can use per-step variable Δt within each element.\n- The reward head learns to predict `r_cum` directly — no scale approximation needed at imagination time.\n- The continue predictor learns to estimate `c_min` — conservative: if any frame within the gap is terminal, the interval is marked terminal.\n\n---\n\n## File Modification Summary\n\n| File | Function/Class | Lines | Change Type |\n|---|---|---|---|\n| `networks.py` | `RSSM.__init__` | 14-98 | Modify: add `max_dt`, `dt_embed_dim` params, `_dt_embedding` |\n| `networks.py` | `RSSM.__init__` | 49-52 | Modify: expand `inp_dim` by `dt_embed_dim` |\n| `networks.py` | `RSSM.img_step` | 208-233 | Modify: add `dt` param, embed and concat Dt |\n| `networks.py` | `RSSM.obs_step` | 174-206 | Modify: add `dt` param, forward to `img_step` |\n| `networks.py` | `RSSM.observe` | 127-143 | Modify: accept and forward per-step `dt` labels |\n| `networks.py` | `RSSM.imagine_with_action` | 145-152 | Modify: add optional `dt_sequence` param |\n| `networks.py` | (new) `EventGate` | after 291 | Add: gate MLP + Gumbel-Softmax (τ_init=5.0) |\n| `models.py` | `WorldModel.__init__` | 30-101 | Modify: instantiate `EventGate`, wire config |\n| `models.py` | `WorldModel._train` | 108-174 | Modify: add variable-Δt sub-sampling + gate loss |\n| `models.py` | `ImagBehavior._imagine` | 351-369 | Modify: gate-driven variable Dt in loop |\n| `models.py` | `ImagBehavior._compute_target` | 371-389 | Modify: `lambda_return_variable_dt` (reward already cumulative) |\n| `models.py` | `ImagBehavior._train` | 290-349 | Modify: pass `dts`, add gate metrics |\n| `tools.py` | (new) `lambda_return_variable_dt` | after 717 | Add: Dt-adjusted lambda return (uses cumulative reward directly) |\n| `tools.py` | (new) `subsample_variable_dt` | new | Add: log-uniform Δt sub-sampling with cumulative reward / min-cont |\n| `configs.yaml` | `defaults` | end of section | Add: `gate_*` hyperparameters (τ_init=5.0) |\n\n---\n\n## Risks and Mitigations\n\n### R1: Training Instability\n\n**Risk**: The Dt embedding changes the GRU input distribution. Early in training, randomly initialized Dt embeddings inject noise.\n\n**Mitigation**:\n- Initialize Dt embedding weights near zero (`std=0.01`), so initial impact is negligible\n- Phase 1 curriculum (0-50K steps) forces Dt=1 and doesn't train the gate\n- The `_img_in_layers` (Linear + LayerNorm + SiLU) normalizes the concatenated input, absorbing scale differences\n\n### R2: Gate Collapse\n\n**Risk**: Gate degenerates to constant Dt, losing adaptivity.\n\n**Mitigation**:\n- Entropy regularization in gate loss\n- Curriculum prevents premature commitment\n- Monitoring metrics with alert thresholds (Section E.4)\n- Gumbel-Softmax temperature annealing ensures exploration early on\n\n### R3: Reward Prediction Under Variable Δt\n\n**Risk**: The reward head must generalize across different Δt values, predicting cumulative discounted rewards for strides it may not have seen frequently.\n\n**Mitigation**:\n- Log-uniform Δt sampling (Module F) provides balanced training coverage across all stride values\n- Cumulative discounted reward targets are exact (pre-computed from replay data, not approximated)\n- The gate supervision ensures large Δt is chosen only when state changes are small, correlating with low reward variance — the easier prediction regime\n- Monitor `imag_reward` statistics for anomalies across different Δt values\n\n### R4: Compatibility with Original DreamerV3\n\n**Risk**: Modified code breaks when `gate_enabled=false`.\n\n**Mitigation**:\n- All gate logic is guarded by `config.gate_enabled`\n- `img_step` defaults `dt=None` which maps to Dt=1\n- When gate is disabled, `inp_dim` does not include `dt_embed_dim` (guard in constructor)\n- `_compute_target` falls back to standard `lambda_return`\n- Net-zero change to behavior when `gate_enabled=false`\n\n### R5: Computational Overhead\n\n**Risk**: Gate MLP adds forward-pass cost in imagination.\n\n**Mitigation**:\n- Gate MLP is small (2 layers x 256 units = ~400K params vs. RSSM's ~5M)\n- Gate is only called during imagination (not observation/training unroll)\n- With effective gating, the imagined horizon can be reduced (fewer steps to cover the same planning depth), potentially net-reducing compute\n\n### R6: Replay Buffer Sub-Sampling Overhead\n\n**Risk**: Variable-Δt sub-sampling (Module F) reduces effective sequence length, discarding some frames per batch.\n\n**Mitigation**:\n- Log-uniform distribution means ~50% of batch elements get Δt ≤ 2, preserving fine-grained temporal resolution for most of the batch\n- Sub-sampled frames still contribute via cumulative reward and min-continuation aggregation — no information is fully discarded\n- The standard (Δt=1) training path remains active for half the batch, maintaining RSSM's single-step prediction quality\n",
      "numLines": 907,
      "startLine": 1,
      "totalLines": 907
    }
  }
}
````

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_015hkb6iFEfqr2CMuAAYbCG4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/networks.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "44d096ec-8616-406d-a356-fb81d5bf4e5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGvuUf2bFiCqJ6dSCykPiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12473,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12473
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

_source line 8 · 2026-05-13T06:37:10.020Z_

<details><summary>↩ Tool result · `toolu_015hkb6iFEfqr2CMuAAYbCG4`</summary>

```text
1	# Event-Gated Adaptive-Horizon DreamerV3 — Network Definitions
2	# Modified from NM512/dreamerv3-torch.
3	# Changes: RSSM accepts variable dt via learned embedding; new EventGate class.
4	
5	import math
6	import numpy as np
7	import re
8	
9	import torch
10	from torch import nn
11	import torch.nn.functional as F
12	from torch import distributions as torchd
13	
14	import tools
15	
16	
17	class RSSM(nn.Module):
18	    def __init__(
19	        self,
20	        stoch=30,
21	        deter=200,
22	        hidden=200,
23	        rec_depth=1,
24	        discrete=False,
25	        act="SiLU",
26	        norm=True,
27	        mean_act="none",
28	        std_act="softplus",
29	        min_std=0.1,
30	        unimix_ratio=0.01,
31	        initial="learned",
32	        num_actions=None,
33	        embed=None,
34	        device=None,
35	        max_dt=1,
36	        dt_embed_dim=32,
37	    ):
38	        super(RSSM, self).__init__()
39	        self._stoch = stoch
40	        self._deter = deter
41	        self._hidden = hidden
42	        self._min_std = min_std
43	        self._rec_depth = rec_depth
44	        self._discrete = discrete
45	        act = getattr(torch.nn, act)
46	        self._mean_act = mean_act
47	        self._std_act = std_act
48	        self._unimix_ratio = unimix_ratio
49	        self._initial = initial
50	        self._num_actions = num_actions
51	        self._embed = embed
52	        self._device = device
53	
54	        self._max_dt = max_dt
55	        self._dt_embed_dim = dt_embed_dim
56	        if self._max_dt > 1:
57	            self._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)
58	            nn.init.normal_(self._dt_embedding.weight, std=0.01)
59	        else:
60	            self._dt_embedding = None
61	
62	        inp_layers = []
63	        if self._discrete:
64	            inp_dim = self._stoch * self._discrete + num_actions
65	        else:
66	            inp_dim = self._stoch + num_actions
67	        if self._dt_embedding is not None:
68	            inp_dim += dt_embed_dim
69	        inp_layers.append(nn.Linear(inp_dim, self._hidden, bias=False))
70	        if norm:
71	            inp_layers.append(nn.LayerNorm(self._hidden, eps=1e-03))
72	        inp_layers.append(act())
73	        self._img_in_layers = nn.Sequential(*inp_layers)
74	        self._img_in_layers.apply(tools.weight_init)
75	        self._cell = GRUCell(self._hidden, self._deter, norm=norm)
76	        self._cell.apply(tools.weight_init)
77	
78	        img_out_layers = []
79	        inp_dim = self._deter
80	        img_out_layers.append(nn.Linear(inp_dim, self._hidden, bias=False))
81	        if norm:
82	            img_out_layers.append(nn.LayerNorm(self._hidden, eps=1e-03))
83	        img_out_layers.append(act())
84	        self._img_out_layers = nn.Sequential(*img_out_layers)
85	        self._img_out_layers.apply(tools.weight_init)
86	
87	        obs_out_layers = []
88	        inp_dim = self._deter + self._embed
89	        obs_out_layers.append(nn.Linear(inp_dim, self._hidden, bias=False))
90	        if norm:
91	            obs_out_layers.append(nn.LayerNorm(self._hidden, eps=1e-03))
92	        obs_out_layers.append(act())
93	        self._obs_out_layers = nn.Sequential(*obs_out_layers)
94	        self._obs_out_layers.apply(tools.weight_init)
95	
96	        if self._discrete:
97	            self._imgs_stat_layer = nn.Linear(
98	                self._hidden, self._stoch * self._discrete
99	            )
100	            self._imgs_stat_layer.apply(tools.uniform_weight_init(1.0))
101	            self._obs_stat_layer = nn.Linear(self._hidden, self._stoch * self._discrete)
102	            self._obs_stat_layer.apply(tools.uniform_weight_init(1.0))
103	        else:
104	            self._imgs_stat_layer = nn.Linear(self._hidden, 2 * self._stoch)
105	            self._imgs_stat_layer.apply(tools.uniform_weight_init(1.0))
106	            self._obs_stat_layer = nn.Linear(self._hidden, 2 * self._stoch)
107	            self._obs_stat_layer.apply(tools.uniform_weight_init(1.0))
108	
109	        if self._initial == "learned":
110	            self.W = torch.nn.Parameter(
111	                torch.zeros((1, self._deter), device=torch.device(self._device)),
112	                requires_grad=True,
113	            )
114	
115	    def initial(self, batch_size):
116	        deter = torch.zeros(batch_size, self._deter, device=self._device)
117	        if self._discrete:
118	            state = dict(
119	                logit=torch.zeros(
120	                    [batch_size, self._stoch, self._discrete], device=self._device
121	                ),
122	                stoch=torch.zeros(
123	                    [batch_size, self._stoch, self._discrete], device=self._device
124	                ),
125	                deter=deter,
126	            )
127	        else:
128	            state = dict(
129	                mean=torch.zeros([batch_size, self._stoch], device=self._device),
130	                std=torch.zeros([batch_size, self._stoch], device=self._device),
131	                stoch=torch.zeros([batch_size, self._stoch], device=self._device),
132	                deter=deter,
133	            )
134	        if self._initial == "zeros":
135	            return state
136	        elif self._initial == "learned":
137	            state["deter"] = torch.tanh(self.W).repeat(batch_size, 1)
138	            state["stoch"] = self.get_stoch(state["deter"])
139	            return state
140	        else:
141	            raise NotImplementedError(self._initial)
142	
143	    def observe(self, embed, action, is_first, state=None, dt_labels=None):
144	        swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))
145	        # (batch, time, ch) -> (time, batch, ch)
146	        embed, action, is_first = swap(embed), swap(action), swap(is_first)
147	        # prev_state[0] means selecting posterior of return(posterior, prior) from obs_step
148	        if dt_labels is not None:
149	            dt_labels_t = swap(dt_labels)
150	            post, prior = tools.static_scan(
151	                lambda prev_state, prev_act, embed, is_first, dt: self.obs_step(
152	                    prev_state[0], prev_act, embed, is_first, dt=dt
153	                ),
154	                (action, embed, is_first, dt_labels_t),
155	                (state, state),
156	            )
157	        else:
158	            post, prior = tools.static_scan(
159	                lambda prev_state, prev_act, embed, is_first: self.obs_step(
160	                    prev_state[0], prev_act, embed, is_first
161	                ),
162	                (action, embed, is_first),
163	                (state, state),
164	            )
165	
166	        # (batch, time, stoch, discrete_num) -> (batch, time, stoch, discrete_num)
167	        post = {k: swap(v) for k, v in post.items()}
168	        prior = {k: swap(v) for k, v in prior.items()}
169	        return post, prior
170	
171	    def imagine_with_action(self, action, state, dt_sequence=None):
172	        swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))
173	        assert isinstance(state, dict), state
174	        action = swap(action)
175	        if dt_sequence is not None:
176	            dt_sequence = swap(dt_sequence)
177	            prior = tools.static_scan(
178	                lambda s, a, dt: self.img_step(s, a, dt=dt),
179	                [action, dt_sequence], state
180	            )
181	        else:
182	            prior = tools.static_scan(self.img_step, [action], state)
183	        prior = prior[0]
184	        prior = {k: swap(v) for k, v in prior.items()}
185	        return prior
186	
187	    def get_feat(self, state):
188	        stoch = state["stoch"]
189	        if self._discrete:
190	            shape = list(stoch.shape[:-2]) + [self._stoch * self._discrete]
191	            stoch = stoch.reshape(shape)
192	        return torch.cat([stoch, state["deter"]], -1)
193	
194	    def get_dist(self, state, dtype=None):
195	        if self._discrete:
196	            logit = state["logit"]
197	            dist = torchd.independent.Independent(
198	                tools.OneHotDist(logit, unimix_ratio=self._unimix_ratio), 1
199	            )
200	        else:
201	            mean, std = state["mean"], state["std"]
202	            dist = tools.ContDist(
203	                torchd.independent.Independent(torchd.normal.Normal(mean, std), 1)
204	            )
205	        return dist
206	
207	    def obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):
208	        # initialize all prev_state
209	        if prev_state == None or torch.sum(is_first) == len(is_first):
210	            prev_state = self.initial(len(is_first))
211	            prev_action = torch.zeros(
212	                (len(is_first), self._num_actions), device=self._device
213	            )
214	        # overwrite the prev_state only where is_first=True
215	        elif torch.sum(is_first) > 0:
216	            is_first = is_first[:, None]
217	            prev_action *= 1.0 - is_first
218	            init_state = self.initial(len(is_first))
219	            for key, val in prev_state.items():
220	                is_first_r = torch.reshape(
221	                    is_first,
222	                    is_first.shape + (1,) * (len(val.shape) - len(is_first.shape)),
223	                )
224	                prev_state[key] = (
225	                    val * (1.0 - is_first_r) + init_state[key] * is_first_r
226	                )
227	
228	        prior = self.img_step(prev_state, prev_action, dt=dt)
229	        x = torch.cat([prior["deter"], embed], -1)
230	        # (batch_size, prior_deter + embed) -> (batch_size, hidden)
231	        x = self._obs_out_layers(x)
232	        # (batch_size, hidden) -> (batch_size, stoch, discrete_num)
233	        stats = self._suff_stats_layer("obs", x)
234	        if sample:
235	            stoch = self.get_dist(stats).sample()
236	        else:
237	            stoch = self.get_dist(stats).mode()
238	        post = {"stoch": stoch, "deter": prior["deter"], **stats}
239	        return post, prior
240	
241	    def img_step(self, prev_state, prev_action, dt=None, sample=True):
242	        # (batch, stoch, discrete_num)
243	        prev_stoch = prev_state["stoch"]
244	        if self._discrete:
245	            shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]
246	            # (batch, stoch, discrete_num) -> (batch, stoch * discrete_num)
247	            prev_stoch = prev_stoch.reshape(shape)
248	
249	        if self._dt_embedding is not None:
250	            if dt is None:
251	                dt = torch.ones(
252	                    prev_stoch.shape[0], dtype=torch.long,
253	                    device=prev_stoch.device
254	                )
255	            dt_emb = self._dt_embedding(dt - 1)
256	            x = torch.cat([prev_stoch, prev_action, dt_emb], -1)
257	        else:
258	            x = torch.cat([prev_stoch, prev_action], -1)
259	
260	        # (batch, stoch * discrete_num + action [+ dt_emb]) -> (batch, hidden)
261	        x = self._img_in_layers(x)
262	        for _ in range(self._rec_depth):  # rec depth is not correctly implemented
263	            deter = prev_state["deter"]
264	            # (batch, hidden), (batch, deter) -> (batch, deter), (batch, deter)
265	            x, deter = self._cell(x, [deter])
266	            deter = deter[0]  # Keras wraps the state in a list.
267	        # (batch, deter) -> (batch, hidden)
268	        x = self._img_out_layers(x)
269	        # (batch, hidden) -> (batch_size, stoch, discrete_num)
270	        stats = self._suff_stats_layer("ims", x)
271	        if sample:
272	            stoch = self.get_dist(stats).sample()
273	        else:
274	            stoch = self.get_dist(stats).mode()
275	        prior = {"stoch": stoch, "deter": deter, **stats}
276	        return prior
277	
278	    def get_stoch(self, deter):
279	        x = self._img_out_layers(deter)
280	        stats = self._suff_stats_layer("ims", x)
281	        dist = self.get_dist(stats)
282	        return dist.mode()
283	
284	    def _suff_stats_layer(self, name, x):
285	        if self._discrete:
286	            if name == "ims":
287	                x = self._imgs_stat_layer(x)
288	            elif name == "obs":
289	                x = self._obs_stat_layer(x)
290	            else:
291	                raise NotImplementedError
292	            logit = x.reshape(list(x.shape[:-1]) + [self._stoch, self._discrete])
293	            return {"logit": logit}
294	        else:
295	            if name == "ims":
296	                x = self._imgs_stat_layer(x)
297	            elif name == "obs":
298	                x = self._obs_stat_layer(x)
299	            else:
300	                raise NotImplementedError
301	            mean, std = torch.split(x, [self._stoch] * 2, -1)
302	            mean = {
303	                "none": lambda: mean,
304	                "tanh5": lambda: 5.0 * torch.tanh(mean / 5.0),
305	            }[self._mean_act]()
306	            std = {
307	                "softplus": lambda: torch.softplus(std),
308	                "abs": lambda: torch.abs(std + 1),
309	                "sigmoid": lambda: torch.sigmoid(std),
310	                "sigmoid2": lambda: 2 * torch.sigmoid(std / 2),
311	            }[self._std_act]()
312	            std = std + self._min_std
313	            return {"mean": mean, "std": std}
314	
315	    def kl_loss(self, post, prior, free, dyn_scale, rep_scale):
316	        kld = torchd.kl.kl_divergence
317	        dist = lambda x: self.get_dist(x)
318	        sg = lambda x: {k: v.detach() for k, v in x.items()}
319	
320	        rep_loss = value = kld(
321	            dist(post) if self._discrete else dist(post)._dist,
322	            dist(sg(prior)) if self._discrete else dist(sg(prior))._dist,
323	        )
324	        dyn_loss = kld(
325	            dist(sg(post)) if self._discrete else dist(sg(post))._dist,
326	            dist(prior) if self._discrete else dist(prior)._dist,
327	        )
328	        # this is implemented using maximum at the original repo as the gradients are not backpropagated for the out of limits.
329	        rep_loss = torch.clip(rep_loss, min=free)
330	        dyn_loss = torch.clip(dyn_loss, min=free)
331	        loss = dyn_scale * dyn_loss + rep_scale * rep_loss
332	
333	        return loss, value, dyn_loss, rep_loss
334	
335	
336	class EventGate(nn.Module):
337	    """Learned event gate that decides per-step temporal stride dt in {1,...,K}."""
338	
339	    def __init__(
340	        self,
341	        feat_size,
342	        max_dt=8,
343	        hidden_units=256,
344	        hidden_layers=2,
345	        act="SiLU",
346	        norm=True,
347	        tau_init=5.0,
348	        tau_final=0.5,
349	        tau_anneal_steps=200000,
350	    ):
351	        super(EventGate, self).__init__()
352	        self._max_dt = max_dt
353	        self._tau_init = tau_init
354	        self._tau_final = tau_final
355	        self._tau_anneal_steps = tau_anneal_steps
356	
357	        act_fn = getattr(torch.nn, act)
358	        layers = []
359	        inp_dim = feat_size
360	        for i in range(hidden_layers):
361	            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))
362	            if norm:
363	                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))
364	            layers.append(act_fn())
365	            inp_dim = hidden_units
366	        self.mlp = nn.Sequential(*layers)
367	        self.mlp.apply(tools.weight_init)
368	
369	        self.logit_layer = nn.Linear(hidden_units, max_dt)
370	        self.logit_layer.apply(tools.uniform_weight_init(0.01))
371	
372	    def get_tau(self, step):
373	        """Linear temperature annealing from tau_init to tau_final."""
374	        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)
375	        return self._tau_init + frac * (self._tau_final - self._tau_init)
376	
377	    def forward(self, feat, step, hard=False):
378	        """
379	        Args:
380	            feat: (batch, feat_size) — concatenated [stoch, deter]
381	            step: int — current training step for temperature annealing
382	            hard: bool — if True, use hard Gumbel-Softmax
383	        Returns:
384	            dt_onehot: (batch, max_dt) — one-hot or soft assignment
385	            dt_index:  (batch,) — integer dt in {1,...,K}
386	            logits:    (batch, max_dt) — raw logits for entropy computation
387	        """
388	        x = self.mlp(feat)
389	        logits = self.logit_layer(x)
390	        tau = self.get_tau(step)
391	        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)
392	        dt_index = torch.argmax(dt_onehot, dim=-1) + 1
393	        return dt_onehot, dt_index, logits
394	
395	    def entropy(self, logits):
396	        """Categorical entropy of the gate distribution."""
397	        probs = F.softmax(logits, dim=-1)
398	        log_probs = F.log_softmax(logits, dim=-1)
399	        return -(probs * log_probs).sum(dim=-1)
400	
401	
402	class MultiEncoder(nn.Module):
403	    def __init__(
404	        self,
405	        shapes,
406	        mlp_keys,
407	        cnn_keys,
408	        act,
409	        norm,
410	        cnn_depth,
411	        kernel_size,
412	        minres,
413	        mlp_layers,
414	        mlp_units,
415	        symlog_inputs,
416	    ):
417	        super(MultiEncoder, self).__init__()
418	        excluded = ("is_first", "is_last", "is_terminal", "reward")
419	        shapes = {
420	            k: v
421	            for k, v in shapes.items()
422	            if k not in excluded and not k.startswith("log_")
423	        }
424	        self.cnn_shapes = {
425	            k: v for k, v in shapes.items() if len(v) == 3 and re.match(cnn_keys, k)
426	        }
427	        self.mlp_shapes = {
428	            k: v
429	            for k, v in shapes.items()
430	            if len(v) in (1, 2) and re.match(mlp_keys, k)
431	        }
432	        print("Encoder CNN shapes:", self.cnn_shapes)
433	        print("Encoder MLP shapes:", self.mlp_shapes)
434	
435	        self.outdim = 0
436	        if self.cnn_shapes:
437	            input_ch = sum([v[-1] for v in self.cnn_shapes.values()])
438	            input_shape = tuple(self.cnn_shapes.values())[0][:2] + (input_ch,)
439	            self._cnn = ConvEncoder(
440	                input_shape, cnn_depth, act, norm, kernel_size, minres
441	            )
442	            self.outdim += self._cnn.outdim
443	        if self.mlp_shapes:
444	            input_size = sum([sum(v) for v in self.mlp_shapes.values()])
445	            self._mlp = MLP(
446	                input_size,
447	                None,
448	                mlp_layers,
449	                mlp_units,
450	                act,
451	                norm,
452	                symlog_inputs=symlog_inputs,
453	                name="Encoder",
454	            )
455	            self.outdim += mlp_units
456	
457	    def forward(self, obs):
458	        outputs = []
459	        if self.cnn_shapes:
460	            inputs = torch.cat([obs[k] for k in self.cnn_shapes], -1)
461	            outputs.append(self._cnn(inputs))
462	        if self.mlp_shapes:
463	            inputs = torch.cat([obs[k] for k in self.mlp_shapes], -1)
464	            outputs.append(self._mlp(inputs))
465	        outputs = torch.cat(outputs, -1)
466	        return outputs
467	
468	
469	class MultiDecoder(nn.Module):
470	    def __init__(
471	        self,
472	        feat_size,
473	        shapes,
474	        mlp_keys,
475	        cnn_keys,
476	        act,
477	        norm,
478	        cnn_depth,
479	        kernel_size,
480	        minres,
481	        mlp_layers,
482	        mlp_units,
483	        cnn_sigmoid,
484	        image_dist,
485	        vector_dist,
486	        outscale,
487	    ):
488	        super(MultiDecoder, self).__init__()
489	        excluded = ("is_first", "is_last", "is_terminal")
490	        shapes = {k: v for k, v in shapes.items() if k not in excluded}
491	        self.cnn_shapes = {
492	            k: v for k, v in shapes.items() if len(v) == 3 and re.match(cnn_keys, k)
493	        }
494	        self.mlp_shapes = {
495	            k: v
496	            for k, v in shapes.items()
497	            if len(v) in (1, 2) and re.match(mlp_keys, k)
498	        }
499	        print("Decoder CNN shapes:", self.cnn_shapes)
500	        print("Decoder MLP shapes:", self.mlp_shapes)
501	
502	        if self.cnn_shapes:
503	            some_shape = list(self.cnn_shapes.values())[0]
504	            shape = (sum(x[-1] for x in self.cnn_shapes.values()),) + some_shape[:-1]
505	            self._cnn = ConvDecoder(
506	                feat_size,
507	                shape,
508	                cnn_depth,
509	                act,
510	                norm,
511	                kernel_size,
512	                minres,
513	                outscale=outscale,
514	                cnn_sigmoid=cnn_sigmoid,
515	            )
516	        if self.mlp_shapes:
517	            self._mlp = MLP(
518	                feat_size,
519	                self.mlp_shapes,
520	                mlp_layers,
521	                mlp_units,
522	                act,
523	                norm,
524	                vector_dist,
525	                outscale=outscale,
526	                name="Decoder",
527	            )
528	        self._image_dist = image_dist
529	
530	    def forward(self, features):
531	        dists = {}
532	        if self.cnn_shapes:
533	            feat = features
534	            outputs = self._cnn(feat)
535	            split_sizes = [v[-1] for v in self.cnn_shapes.values()]
536	            outputs = torch.split(outputs, split_sizes, -1)
537	            dists.update(
538	                {
539	                    key: self._make_image_dist(output)
540	                    for key, output in zip(self.cnn_shapes.keys(), outputs)
541	                }
542	            )
543	        if self.mlp_shapes:
544	            dists.update(self._mlp(features))
545	        return dists
546	
547	    def _make_image_dist(self, mean):
548	        if self._image_dist == "normal":
549	            return tools.ContDist(
550	                torchd.independent.Independent(torchd.normal.Normal(mean, 1), 3)
551	            )
552	        if self._image_dist == "mse":
553	            return tools.MSEDist(mean)
554	        raise NotImplementedError(self._image_dist)
555	
556	
557	class ConvEncoder(nn.Module):
558	    def __init__(
559	        self,
560	        input_shape,
561	        depth=32,
562	        act="SiLU",
563	        norm=True,
564	        kernel_size=4,
565	        minres=4,
566	    ):
567	        super(ConvEncoder, self).__init__()
568	        act = getattr(torch.nn, act)
569	        h, w, input_ch = input_shape
570	        stages = int(np.log2(h) - np.log2(minres))
571	        in_dim = input_ch
572	        out_dim = depth
573	        layers = []
574	        for i in range(stages):
575	            layers.append(
576	                Conv2dSamePad(
577	                    in_channels=in_dim,
578	                    out_channels=out_dim,
579	                    kernel_size=kernel_size,
580	                    stride=2,
581	                    bias=False,
582	                )
583	            )
584	            if norm:
585	                layers.append(ImgChLayerNorm(out_dim))
586	            layers.append(act())
587	            in_dim = out_dim
588	            out_dim *= 2
589	            h, w = h // 2, w // 2
590	
591	        self.outdim = out_dim // 2 * h * w
592	        self.layers = nn.Sequential(*layers)
593	        self.layers.apply(tools.weight_init)
594	
595	    def forward(self, obs):
596	        obs -= 0.5
597	        # (batch, time, h, w, ch) -> (batch * time, h, w, ch)
598	        x = obs.reshape((-1,) + tuple(obs.shape[-3:]))
599	        # (batch * time, h, w, ch) -> (batch * time, ch, h, w)
600	        x = x.permute(0, 3, 1, 2)
601	        x = self.layers(x)
602	        # (batch * time, ...) -> (batch * time, -1)
603	        x = x.reshape([x.shape[0], np.prod(x.shape[1:])])
604	        # (batch * time, -1) -> (batch, time, -1)
605	        return x.reshape(list(obs.shape[:-3]) + [x.shape[-1]])
606	
607	
608	class ConvDecoder(nn.Module):
609	    def __init__(
610	        self,
611	        feat_size,
612	        shape=(3, 64, 64),
613	        depth=32,
614	        act=nn.ELU,
615	        norm=True,
616	        kernel_size=4,
617	        minres=4,
618	        outscale=1.0,
619	        cnn_sigmoid=False,
620	    ):
621	        super(ConvDecoder, self).__init__()
622	        act = getattr(torch.nn, act)
623	        self._shape = shape
624	        self._cnn_sigmoid = cnn_sigmoid
625	        layer_num = int(np.log2(shape[1]) - np.log2(minres))
626	        self._minres = minres
627	        out_ch = minres**2 * depth * 2 ** (layer_num - 1)
628	        self._embed_size = out_ch
629	
630	        self._linear_layer = nn.Linear(feat_size, out_ch)
631	        self._linear_layer.apply(tools.uniform_weight_init(outscale))
632	        in_dim = out_ch // (minres**2)
633	        out_dim = in_dim // 2
634	
635	        layers = []
636	        h, w = minres, minres
637	        for i in range(layer_num):
638	            bias = False
639	            if i == layer_num - 1:
640	                out_dim = self._shape[0]
641	                act = False
642	                bias = True
643	                norm = False
644	
645	            if i != 0:
646	                in_dim = 2 ** (layer_num - (i - 1) - 2) * depth
647	            pad_h, outpad_h = self.calc_same_pad(k=kernel_size, s=2, d=1)
648	            pad_w, outpad_w = self.calc_same_pad(k=kernel_size, s=2, d=1)
649	            layers.append(
650	                nn.ConvTranspose2d(
651	                    in_dim,
652	                    out_dim,
653	                    kernel_size,
654	                    2,
655	                    padding=(pad_h, pad_w),
656	                    output_padding=(outpad_h, outpad_w),
657	                    bias=bias,
658	                )
659	            )
660	            if norm:
661	                layers.append(ImgChLayerNorm(out_dim))
662	            if act:
663	                layers.append(act())
664	            in_dim = out_dim
665	            out_dim //= 2
666	            h, w = h * 2, w * 2
667	        [m.apply(tools.weight_init) for m in layers[:-1]]
668	        layers[-1].apply(tools.uniform_weight_init(outscale))
669	        self.layers = nn.Sequential(*layers)
670	
671	    def calc_same_pad(self, k, s, d):
672	        val = d * (k - 1) - s + 1
673	        pad = math.ceil(val / 2)
674	        outpad = pad * 2 - val
675	        return pad, outpad
676	
677	    def forward(self, features, dtype=None):
678	        x = self._linear_layer(features)
679	        # (batch, time, -1) -> (batch * time, h, w, ch)
680	        x = x.reshape(
681	            [-1, self._minres, self._minres, self._embed_size // self._minres**2]
682	        )
683	        # (batch, time, -1) -> (batch * time, ch, h, w)
684	        x = x.permute(0, 3, 1, 2)
685	        x = self.layers(x)
686	        # (batch, time, -1) -> (batch, time, ch, h, w)
687	        mean = x.reshape(features.shape[:-1] + self._shape)
688	        # (batch, time, ch, h, w) -> (batch, time, h, w, ch)
689	        mean = mean.permute(0, 1, 3, 4, 2)
690	        if self._cnn_sigmoid:
691	            mean = F.sigmoid(mean)
692	        else:
693	            mean += 0.5
694	        return mean
695	
696	
697	class MLP(nn.Module):
698	    def __init__(
699	        self,
700	        inp_dim,
701	        shape,
702	        layers,
703	        units,
704	        act="SiLU",
705	        norm=True,
706	        dist="normal",
707	        std=1.0,
708	        min_std=0.1,
709	        max_std=1.0,
710	        absmax=None,
711	        temp=0.1,
712	        unimix_ratio=0.01,
713	        outscale=1.0,
714	        symlog_inputs=False,
715	        device="cuda",
716	        name="NoName",
717	    ):
718	        super(MLP, self).__init__()
719	        self._shape = (shape,) if isinstance(shape, int) else shape
720	        if self._shape is not None and len(self._shape) == 0:
721	            self._shape = (1,)
722	        act = getattr(torch.nn, act)
723	        self._dist = dist
724	        self._std = std if isinstance(std, str) else torch.tensor((std,), device=device)
725	        self._min_std = min_std
726	        self._max_std = max_std
727	        self._absmax = absmax
728	        self._temp = temp
729	        self._unimix_ratio = unimix_ratio
730	        self._symlog_inputs = symlog_inputs
731	        self._device = device
732	
733	        self.layers = nn.Sequential()
734	        for i in range(layers):
735	            self.layers.add_module(
736	                f"{name}_linear{i}", nn.Linear(inp_dim, units, bias=False)
737	            )
738	            if norm:
739	                self.layers.add_module(
740	                    f"{name}_norm{i}", nn.LayerNorm(units, eps=1e-03)
741	                )
742	            self.layers.add_module(f"{name}_act{i}", act())
743	            if i == 0:
744	                inp_dim = units
745	        self.layers.apply(tools.weight_init)
746	
747	        if isinstance(self._shape, dict):
748	            self.mean_layer = nn.ModuleDict()
749	            for name, shape in self._shape.items():
750	                self.mean_layer[name] = nn.Linear(inp_dim, np.prod(shape))
751	            self.mean_layer.apply(tools.uniform_weight_init(outscale))
752	            if self._std == "learned":
753	                assert dist in ("tanh_normal", "normal", "trunc_normal", "huber"), dist
754	                self.std_layer = nn.ModuleDict()
755	                for name, shape in self._shape.items():
756	                    self.std_layer[name] = nn.Linear(inp_dim, np.prod(shape))
757	                self.std_layer.apply(tools.uniform_weight_init(outscale))
758	        elif self._shape is not None:
759	            self.mean_layer = nn.Linear(inp_dim, np.prod(self._shape))
760	            self.mean_layer.apply(tools.uniform_weight_init(outscale))
761	            if self._std == "learned":
762	                assert dist in ("tanh_normal", "normal", "trunc_normal", "huber"), dist
763	                self.std_layer = nn.Linear(units, np.prod(self._shape))
764	                self.std_layer.apply(tools.uniform_weight_init(outscale))
765	
766	    def forward(self, features, dtype=None):
767	        x = features
768	        if self._symlog_inputs:
769	            x = tools.symlog(x)
770	        out = self.layers(x)
771	        # Used for encoder output
772	        if self._shape is None:
773	            return out
774	        if isinstance(self._shape, dict):
775	            dists = {}
776	            for name, shape in self._shape.items():
777	                mean = self.mean_layer[name](out)
778	                if self._std == "learned":
779	                    std = self.std_layer[name](out)
780	                else:
781	                    std = self._std
782	                dists.update({name: self.dist(self._dist, mean, std, shape)})
783	            return dists
784	        else:
785	            mean = self.mean_layer(out)
786	            if self._std == "learned":
787	                std = self.std_layer(out)
788	            else:
789	                std = self._std
790	            return self.dist(self._dist, mean, std, self._shape)
791	
792	    def dist(self, dist, mean, std, shape):
793	        if dist == "tanh_normal":
794	            mean = torch.tanh(mean)
795	            std = F.softplus(std) + self._min_std
796	            dist = torchd.normal.Normal(mean, std)
797	            dist = torchd.transformed_distribution.TransformedDistribution(
798	                dist, tools.TanhBijector()
799	            )
800	            dist = torchd.independent.Independent(dist, 1)
801	            dist = tools.SampleDist(dist)
802	        elif dist == "normal":
803	            std = (self._max_std - self._min_std) * torch.sigmoid(
804	                std + 2.0
805	            ) + self._min_std
806	            dist = torchd.normal.Normal(torch.tanh(mean), std)
807	            dist = tools.ContDist(
808	                torchd.independent.Independent(dist, 1), absmax=self._absmax
809	            )
810	        elif dist == "normal_std_fixed":
811	            dist = torchd.normal.Normal(mean, self._std)
812	            dist = tools.ContDist(
813	                torchd.independent.Independent(dist, 1), absmax=self._absmax
814	            )
815	        elif dist == "trunc_normal":
816	            mean = torch.tanh(mean)
817	            std = 2 * torch.sigmoid(std / 2) + self._min_std
818	            dist = tools.SafeTruncatedNormal(mean, std, -1, 1)
819	            dist = tools.ContDist(
820	                torchd.independent.Independent(dist, 1), absmax=self._absmax
821	            )
822	        elif dist == "onehot":
823	            dist = tools.OneHotDist(mean, unimix_ratio=self._unimix_ratio)
824	        elif dist == "onehot_gumble":
825	            dist = tools.ContDist(
826	                torchd.gumbel.Gumbel(mean, 1 / self._temp), absmax=self._absmax
827	            )
828	        elif dist == "huber":
829	            dist = tools.ContDist(
830	                torchd.independent.Independent(
831	                    tools.UnnormalizedHuber(mean, std, 1.0),
832	                    len(shape),
833	                    absmax=self._absmax,
834	                )
835	            )
836	        elif dist == "binary":
837	            dist = tools.Bernoulli(
838	                torchd.independent.Independent(
839	                    torchd.bernoulli.Bernoulli(logits=mean), len(shape)
840	                )
841	            )
842	        elif dist == "symlog_disc":
843	            dist = tools.DiscDist(logits=mean, device=self._device)
844	        elif dist == "symlog_mse":
845	            dist = tools.SymlogDist(mean)
846	        else:
847	            raise NotImplementedError(dist)
848	        return dist
849	
850	
851	class GRUCell(nn.Module):
852	    def __init__(self, inp_size, size, norm=True, act=torch.tanh, update_bias=-1):
853	        super(GRUCell, self).__init__()
854	        self._inp_size = inp_size
855	        self._size = size
856	        self._act = act
857	        self._update_bias = update_bias
858	        self.layers = nn.Sequential()
859	        self.layers.add_module(
860	            "GRU_linear", nn.Linear(inp_size + size, 3 * size, bias=False)
861	        )
862	        if norm:
863	            self.layers.add_module("GRU_norm", nn.LayerNorm(3 * size, eps=1e-03))
864	
865	    @property
866	    def state_size(self):
867	        return self._size
868	
869	    def forward(self, inputs, state):
870	        state = state[0]  # Keras wraps the state in a list.
871	        parts = self.layers(torch.cat([inputs, state], -1))
872	        reset, cand, update = torch.split(parts, [self._size] * 3, -1)
873	        reset = torch.sigmoid(reset)
874	        cand = self._act(reset * cand)
875	        update = torch.sigmoid(update + self._update_bias)
876	        output = update * cand + (1 - update) * state
877	        return output, [output]
878	
879	
880	class Conv2dSamePad(torch.nn.Conv2d):
881	    def calc_same_pad(self, i, k, s, d):
882	        return max((math.ceil(i / s) - 1) * s + (k - 1) * d + 1 - i, 0)
883	
884	    def forward(self, x):
885	        ih, iw = x.size()[-2:]
886	        pad_h = self.calc_same_pad(
887	            i=ih, k=self.kernel_size[0], s=self.stride[0], d=self.dilation[0]
888	        )
889	        pad_w = self.calc_same_pad(
890	            i=iw, k=self.kernel_size[1], s=self.stride[1], d=self.dilation[1]
891	        )
892	
893	        if pad_h > 0 or pad_w > 0:
894	            x = F.pad(
895	                x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2]
896	            )
897	
898	        ret = F.conv2d(
899	            x,
900	            self.weight,
901	            self.bias,
902	            self.stride,
903	            self.padding,
904	            self.dilation,
905	            self.groups,
906	        )
907	        return ret
908	
909	
910	class ImgChLayerNorm(nn.Module):
911	    def __init__(self, ch, eps=1e-03):
912	        super(ImgChLayerNorm, self).__init__()
913	        self.norm = torch.nn.LayerNorm(ch, eps=eps)
914	
915	    def forward(self, x):
916	        x = x.permute(0, 2, 3, 1)
917	        x = self.norm(x)
918	        x = x.permute(0, 3, 1, 2)
919	        return x
920	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "f879a520-8162-417e-8ce0-f7de53f9ae8c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/networks.py",
      "content": "# Event-Gated Adaptive-Horizon DreamerV3 — Network Definitions\n# Modified from NM512/dreamerv3-torch.\n# Changes: RSSM accepts variable dt via learned embedding; new EventGate class.\n\nimport math\nimport numpy as np\nimport re\n\nimport torch\nfrom torch import nn\nimport torch.nn.functional as F\nfrom torch import distributions as torchd\n\nimport tools\n\n\nclass RSSM(nn.Module):\n    def __init__(\n        self,\n        stoch=30,\n        deter=200,\n        hidden=200,\n        rec_depth=1,\n        discrete=False,\n        act=\"SiLU\",\n        norm=True,\n        mean_act=\"none\",\n        std_act=\"softplus\",\n        min_std=0.1,\n        unimix_ratio=0.01,\n        initial=\"learned\",\n        num_actions=None,\n        embed=None,\n        device=None,\n        max_dt=1,\n        dt_embed_dim=32,\n    ):\n        super(RSSM, self).__init__()\n        self._stoch = stoch\n        self._deter = deter\n        self._hidden = hidden\n        self._min_std = min_std\n        self._rec_depth = rec_depth\n        self._discrete = discrete\n        act = getattr(torch.nn, act)\n        self._mean_act = mean_act\n        self._std_act = std_act\n        self._unimix_ratio = unimix_ratio\n        self._initial = initial\n        self._num_actions = num_actions\n        self._embed = embed\n        self._device = device\n\n        self._max_dt = max_dt\n        self._dt_embed_dim = dt_embed_dim\n        if self._max_dt > 1:\n            self._dt_embedding = nn.Embedding(max_dt, dt_embed_dim)\n            nn.init.normal_(self._dt_embedding.weight, std=0.01)\n        else:\n            self._dt_embedding = None\n\n        inp_layers = []\n        if self._discrete:\n            inp_dim = self._stoch * self._discrete + num_actions\n        else:\n            inp_dim = self._stoch + num_actions\n        if self._dt_embedding is not None:\n            inp_dim += dt_embed_dim\n        inp_layers.append(nn.Linear(inp_dim, self._hidden, bias=False))\n        if norm:\n            inp_layers.append(nn.LayerNorm(self._hidden, eps=1e-03))\n        inp_layers.append(act())\n        self._img_in_layers = nn.Sequential(*inp_layers)\n        self._img_in_layers.apply(tools.weight_init)\n        self._cell = GRUCell(self._hidden, self._deter, norm=norm)\n        self._cell.apply(tools.weight_init)\n\n        img_out_layers = []\n        inp_dim = self._deter\n        img_out_layers.append(nn.Linear(inp_dim, self._hidden, bias=False))\n        if norm:\n            img_out_layers.append(nn.LayerNorm(self._hidden, eps=1e-03))\n        img_out_layers.append(act())\n        self._img_out_layers = nn.Sequential(*img_out_layers)\n        self._img_out_layers.apply(tools.weight_init)\n\n        obs_out_layers = []\n        inp_dim = self._deter + self._embed\n        obs_out_layers.append(nn.Linear(inp_dim, self._hidden, bias=False))\n        if norm:\n            obs_out_layers.append(nn.LayerNorm(self._hidden, eps=1e-03))\n        obs_out_layers.append(act())\n        self._obs_out_layers = nn.Sequential(*obs_out_layers)\n        self._obs_out_layers.apply(tools.weight_init)\n\n        if self._discrete:\n            self._imgs_stat_layer = nn.Linear(\n                self._hidden, self._stoch * self._discrete\n            )\n            self._imgs_stat_layer.apply(tools.uniform_weight_init(1.0))\n            self._obs_stat_layer = nn.Linear(self._hidden, self._stoch * self._discrete)\n            self._obs_stat_layer.apply(tools.uniform_weight_init(1.0))\n        else:\n            self._imgs_stat_layer = nn.Linear(self._hidden, 2 * self._stoch)\n            self._imgs_stat_layer.apply(tools.uniform_weight_init(1.0))\n            self._obs_stat_layer = nn.Linear(self._hidden, 2 * self._stoch)\n            self._obs_stat_layer.apply(tools.uniform_weight_init(1.0))\n\n        if self._initial == \"learned\":\n            self.W = torch.nn.Parameter(\n                torch.zeros((1, self._deter), device=torch.device(self._device)),\n                requires_grad=True,\n            )\n\n    def initial(self, batch_size):\n        deter = torch.zeros(batch_size, self._deter, device=self._device)\n        if self._discrete:\n            state = dict(\n                logit=torch.zeros(\n                    [batch_size, self._stoch, self._discrete], device=self._device\n                ),\n                stoch=torch.zeros(\n                    [batch_size, self._stoch, self._discrete], device=self._device\n                ),\n                deter=deter,\n            )\n        else:\n            state = dict(\n                mean=torch.zeros([batch_size, self._stoch], device=self._device),\n                std=torch.zeros([batch_size, self._stoch], device=self._device),\n                stoch=torch.zeros([batch_size, self._stoch], device=self._device),\n                deter=deter,\n            )\n        if self._initial == \"zeros\":\n            return state\n        elif self._initial == \"learned\":\n            state[\"deter\"] = torch.tanh(self.W).repeat(batch_size, 1)\n            state[\"stoch\"] = self.get_stoch(state[\"deter\"])\n            return state\n        else:\n            raise NotImplementedError(self._initial)\n\n    def observe(self, embed, action, is_first, state=None, dt_labels=None):\n        swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n        # (batch, time, ch) -> (time, batch, ch)\n        embed, action, is_first = swap(embed), swap(action), swap(is_first)\n        # prev_state[0] means selecting posterior of return(posterior, prior) from obs_step\n        if dt_labels is not None:\n            dt_labels_t = swap(dt_labels)\n            post, prior = tools.static_scan(\n                lambda prev_state, prev_act, embed, is_first, dt: self.obs_step(\n                    prev_state[0], prev_act, embed, is_first, dt=dt\n                ),\n                (action, embed, is_first, dt_labels_t),\n                (state, state),\n            )\n        else:\n            post, prior = tools.static_scan(\n                lambda prev_state, prev_act, embed, is_first: self.obs_step(\n                    prev_state[0], prev_act, embed, is_first\n                ),\n                (action, embed, is_first),\n                (state, state),\n            )\n\n        # (batch, time, stoch, discrete_num) -> (batch, time, stoch, discrete_num)\n        post = {k: swap(v) for k, v in post.items()}\n        prior = {k: swap(v) for k, v in prior.items()}\n        return post, prior\n\n    def imagine_with_action(self, action, state, dt_sequence=None):\n        swap = lambda x: x.permute([1, 0] + list(range(2, len(x.shape))))\n        assert isinstance(state, dict), state\n        action = swap(action)\n        if dt_sequence is not None:\n            dt_sequence = swap(dt_sequence)\n            prior = tools.static_scan(\n                lambda s, a, dt: self.img_step(s, a, dt=dt),\n                [action, dt_sequence], state\n            )\n        else:\n            prior = tools.static_scan(self.img_step, [action], state)\n        prior = prior[0]\n        prior = {k: swap(v) for k, v in prior.items()}\n        return prior\n\n    def get_feat(self, state):\n        stoch = state[\"stoch\"]\n        if self._discrete:\n            shape = list(stoch.shape[:-2]) + [self._stoch * self._discrete]\n            stoch = stoch.reshape(shape)\n        return torch.cat([stoch, state[\"deter\"]], -1)\n\n    def get_dist(self, state, dtype=None):\n        if self._discrete:\n            logit = state[\"logit\"]\n            dist = torchd.independent.Independent(\n                tools.OneHotDist(logit, unimix_ratio=self._unimix_ratio), 1\n            )\n        else:\n            mean, std = state[\"mean\"], state[\"std\"]\n            dist = tools.ContDist(\n                torchd.independent.Independent(torchd.normal.Normal(mean, std), 1)\n            )\n        return dist\n\n    def obs_step(self, prev_state, prev_action, embed, is_first, dt=None, sample=True):\n        # initialize all prev_state\n        if prev_state == None or torch.sum(is_first) == len(is_first):\n            prev_state = self.initial(len(is_first))\n            prev_action = torch.zeros(\n                (len(is_first), self._num_actions), device=self._device\n            )\n        # overwrite the prev_state only where is_first=True\n        elif torch.sum(is_first) > 0:\n            is_first = is_first[:, None]\n            prev_action *= 1.0 - is_first\n            init_state = self.initial(len(is_first))\n            for key, val in prev_state.items():\n                is_first_r = torch.reshape(\n                    is_first,\n                    is_first.shape + (1,) * (len(val.shape) - len(is_first.shape)),\n                )\n                prev_state[key] = (\n                    val * (1.0 - is_first_r) + init_state[key] * is_first_r\n                )\n\n        prior = self.img_step(prev_state, prev_action, dt=dt)\n        x = torch.cat([prior[\"deter\"], embed], -1)\n        # (batch_size, prior_deter + embed) -> (batch_size, hidden)\n        x = self._obs_out_layers(x)\n        # (batch_size, hidden) -> (batch_size, stoch, discrete_num)\n        stats = self._suff_stats_layer(\"obs\", x)\n        if sample:\n            stoch = self.get_dist(stats).sample()\n        else:\n            stoch = self.get_dist(stats).mode()\n        post = {\"stoch\": stoch, \"deter\": prior[\"deter\"], **stats}\n        return post, prior\n\n    def img_step(self, prev_state, prev_action, dt=None, sample=True):\n        # (batch, stoch, discrete_num)\n        prev_stoch = prev_state[\"stoch\"]\n        if self._discrete:\n            shape = list(prev_stoch.shape[:-2]) + [self._stoch * self._discrete]\n            # (batch, stoch, discrete_num) -> (batch, stoch * discrete_num)\n            prev_stoch = prev_stoch.reshape(shape)\n\n        if self._dt_embedding is not None:\n            if dt is None:\n                dt = torch.ones(\n                    prev_stoch.shape[0], dtype=torch.long,\n                    device=prev_stoch.device\n                )\n            dt_emb = self._dt_embedding(dt - 1)\n            x = torch.cat([prev_stoch, prev_action, dt_emb], -1)\n        else:\n            x = torch.cat([prev_stoch, prev_action], -1)\n\n        # (batch, stoch * discrete_num + action [+ dt_emb]) -> (batch, hidden)\n        x = self._img_in_layers(x)\n        for _ in range(self._rec_depth):  # rec depth is not correctly implemented\n            deter = prev_state[\"deter\"]\n            # (batch, hidden), (batch, deter) -> (batch, deter), (batch, deter)\n            x, deter = self._cell(x, [deter])\n            deter = deter[0]  # Keras wraps the state in a list.\n        # (batch, deter) -> (batch, hidden)\n        x = self._img_out_layers(x)\n        # (batch, hidden) -> (batch_size, stoch, discrete_num)\n        stats = self._suff_stats_layer(\"ims\", x)\n        if sample:\n            stoch = self.get_dist(stats).sample()\n        else:\n            stoch = self.get_dist(stats).mode()\n        prior = {\"stoch\": stoch, \"deter\": deter, **stats}\n        return prior\n\n    def get_stoch(self, deter):\n        x = self._img_out_layers(deter)\n        stats = self._suff_stats_layer(\"ims\", x)\n        dist = self.get_dist(stats)\n        return dist.mode()\n\n    def _suff_stats_layer(self, name, x):\n        if self._discrete:\n            if name == \"ims\":\n                x = self._imgs_stat_layer(x)\n            elif name == \"obs\":\n                x = self._obs_stat_layer(x)\n            else:\n                raise NotImplementedError\n            logit = x.reshape(list(x.shape[:-1]) + [self._stoch, self._discrete])\n            return {\"logit\": logit}\n        else:\n            if name == \"ims\":\n                x = self._imgs_stat_layer(x)\n            elif name == \"obs\":\n                x = self._obs_stat_layer(x)\n            else:\n                raise NotImplementedError\n            mean, std = torch.split(x, [self._stoch] * 2, -1)\n            mean = {\n                \"none\": lambda: mean,\n                \"tanh5\": lambda: 5.0 * torch.tanh(mean / 5.0),\n            }[self._mean_act]()\n            std = {\n                \"softplus\": lambda: torch.softplus(std),\n                \"abs\": lambda: torch.abs(std + 1),\n                \"sigmoid\": lambda: torch.sigmoid(std),\n                \"sigmoid2\": lambda: 2 * torch.sigmoid(std / 2),\n            }[self._std_act]()\n            std = std + self._min_std\n            return {\"mean\": mean, \"std\": std}\n\n    def kl_loss(self, post, prior, free, dyn_scale, rep_scale):\n        kld = torchd.kl.kl_divergence\n        dist = lambda x: self.get_dist(x)\n        sg = lambda x: {k: v.detach() for k, v in x.items()}\n\n        rep_loss = value = kld(\n            dist(post) if self._discrete else dist(post)._dist,\n            dist(sg(prior)) if self._discrete else dist(sg(prior))._dist,\n        )\n        dyn_loss = kld(\n            dist(sg(post)) if self._discrete else dist(sg(post))._dist,\n            dist(prior) if self._discrete else dist(prior)._dist,\n        )\n        # this is implemented using maximum at the original repo as the gradients are not backpropagated for the out of limits.\n        rep_loss = torch.clip(rep_loss, min=free)\n        dyn_loss = torch.clip(dyn_loss, min=free)\n        loss = dyn_scale * dyn_loss + rep_scale * rep_loss\n\n        return loss, value, dyn_loss, rep_loss\n\n\nclass EventGate(nn.Module):\n    \"\"\"Learned event gate that decides per-step temporal stride dt in {1,...,K}.\"\"\"\n\n    def __init__(\n        self,\n        feat_size,\n        max_dt=8,\n        hidden_units=256,\n        hidden_layers=2,\n        act=\"SiLU\",\n        norm=True,\n        tau_init=5.0,\n        tau_final=0.5,\n        tau_anneal_steps=200000,\n    ):\n        super(EventGate, self).__init__()\n        self._max_dt = max_dt\n        self._tau_init = tau_init\n        self._tau_final = tau_final\n        self._tau_anneal_steps = tau_anneal_steps\n\n        act_fn = getattr(torch.nn, act)\n        layers = []\n        inp_dim = feat_size\n        for i in range(hidden_layers):\n            layers.append(nn.Linear(inp_dim, hidden_units, bias=False))\n            if norm:\n                layers.append(nn.LayerNorm(hidden_units, eps=1e-03))\n            layers.append(act_fn())\n            inp_dim = hidden_units\n        self.mlp = nn.Sequential(*layers)\n        self.mlp.apply(tools.weight_init)\n\n        self.logit_layer = nn.Linear(hidden_units, max_dt)\n        self.logit_layer.apply(tools.uniform_weight_init(0.01))\n\n    def get_tau(self, step):\n        \"\"\"Linear temperature annealing from tau_init to tau_final.\"\"\"\n        frac = min(step / max(self._tau_anneal_steps, 1), 1.0)\n        return self._tau_init + frac * (self._tau_final - self._tau_init)\n\n    def forward(self, feat, step, hard=False):\n        \"\"\"\n        Args:\n            feat: (batch, feat_size) — concatenated [stoch, deter]\n            step: int — current training step for temperature annealing\n            hard: bool — if True, use hard Gumbel-Softmax\n        Returns:\n            dt_onehot: (batch, max_dt) — one-hot or soft assignment\n            dt_index:  (batch,) — integer dt in {1,...,K}\n            logits:    (batch, max_dt) — raw logits for entropy computation\n        \"\"\"\n        x = self.mlp(feat)\n        logits = self.logit_layer(x)\n        tau = self.get_tau(step)\n        dt_onehot = F.gumbel_softmax(logits, tau=tau, hard=hard)\n        dt_index = torch.argmax(dt_onehot, dim=-1) + 1\n        return dt_onehot, dt_index, logits\n\n    def entropy(self, logits):\n        \"\"\"Categorical entropy of the gate distribution.\"\"\"\n        probs = F.softmax(logits, dim=-1)\n        log_probs = F.log_softmax(logits, dim=-1)\n        return -(probs * log_probs).sum(dim=-1)\n\n\nclass MultiEncoder(nn.Module):\n    def __init__(\n        self,\n        shapes,\n        mlp_keys,\n        cnn_keys,\n        act,\n        norm,\n        cnn_depth,\n        kernel_size,\n        minres,\n        mlp_layers,\n        mlp_units,\n        symlog_inputs,\n    ):\n        super(MultiEncoder, self).__init__()\n        excluded = (\"is_first\", \"is_last\", \"is_terminal\", \"reward\")\n        shapes = {\n            k: v\n            for k, v in shapes.items()\n            if k not in excluded and not k.startswith(\"log_\")\n        }\n        self.cnn_shapes = {\n            k: v for k, v in shapes.items() if len(v) == 3 and re.match(cnn_keys, k)\n        }\n        self.mlp_shapes = {\n            k: v\n            for k, v in shapes.items()\n            if len(v) in (1, 2) and re.match(mlp_keys, k)\n        }\n        print(\"Encoder CNN shapes:\", self.cnn_shapes)\n        print(\"Encoder MLP shapes:\", self.mlp_shapes)\n\n        self.outdim = 0\n        if self.cnn_shapes:\n            input_ch = sum([v[-1] for v in self.cnn_shapes.values()])\n            input_shape = tuple(self.cnn_shapes.values())[0][:2] + (input_ch,)\n            self._cnn = ConvEncoder(\n                input_shape, cnn_depth, act, norm, kernel_size, minres\n            )\n            self.outdim += self._cnn.outdim\n        if self.mlp_shapes:\n            input_size = sum([sum(v) for v in self.mlp_shapes.values()])\n            self._mlp = MLP(\n                input_size,\n                None,\n                mlp_layers,\n                mlp_units,\n                act,\n                norm,\n                symlog_inputs=symlog_inputs,\n                name=\"Encoder\",\n            )\n            self.outdim += mlp_units\n\n    def forward(self, obs):\n        outputs = []\n        if self.cnn_shapes:\n            inputs = torch.cat([obs[k] for k in self.cnn_shapes], -1)\n            outputs.append(self._cnn(inputs))\n        if self.mlp_shapes:\n            inputs = torch.cat([obs[k] for k in self.mlp_shapes], -1)\n            outputs.append(self._mlp(inputs))\n        outputs = torch.cat(outputs, -1)\n        return outputs\n\n\nclass MultiDecoder(nn.Module):\n    def __init__(\n        self,\n        feat_size,\n        shapes,\n        mlp_keys,\n        cnn_keys,\n        act,\n        norm,\n        cnn_depth,\n        kernel_size,\n        minres,\n        mlp_layers,\n        mlp_units,\n        cnn_sigmoid,\n        image_dist,\n        vector_dist,\n        outscale,\n    ):\n        super(MultiDecoder, self).__init__()\n        excluded = (\"is_first\", \"is_last\", \"is_terminal\")\n        shapes = {k: v for k, v in shapes.items() if k not in excluded}\n        self.cnn_shapes = {\n            k: v for k, v in shapes.items() if len(v) == 3 and re.match(cnn_keys, k)\n        }\n        self.mlp_shapes = {\n            k: v\n            for k, v in shapes.items()\n            if len(v) in (1, 2) and re.match(mlp_keys, k)\n        }\n        print(\"Decoder CNN shapes:\", self.cnn_shapes)\n        print(\"Decoder MLP shapes:\", self.mlp_shapes)\n\n        if self.cnn_shapes:\n            some_shape = list(self.cnn_shapes.values())[0]\n            shape = (sum(x[-1] for x in self.cnn_shapes.values()),) + some_shape[:-1]\n            self._cnn = ConvDecoder(\n                feat_size,\n                shape,\n                cnn_depth,\n                act,\n                norm,\n                kernel_size,\n                minres,\n                outscale=outscale,\n                cnn_sigmoid=cnn_sigmoid,\n            )\n        if self.mlp_shapes:\n            self._mlp = MLP(\n                feat_size,\n                self.mlp_shapes,\n                mlp_layers,\n                mlp_units,\n                act,\n                norm,\n                vector_dist,\n                outscale=outscale,\n                name=\"Decoder\",\n            )\n        self._image_dist = image_dist\n\n    def forward(self, features):\n        dists = {}\n        if self.cnn_shapes:\n            feat = features\n            outputs = self._cnn(feat)\n            split_sizes = [v[-1] for v in self.cnn_shapes.values()]\n            outputs = torch.split(outputs, split_sizes, -1)\n            dists.update(\n                {\n                    key: self._make_image_dist(output)\n                    for key, output in zip(self.cnn_shapes.keys(), outputs)\n                }\n            )\n        if self.mlp_shapes:\n            dists.update(self._mlp(features))\n        return dists\n\n    def _make_image_dist(self, mean):\n        if self._image_dist == \"normal\":\n            return tools.ContDist(\n                torchd.independent.Independent(torchd.normal.Normal(mean, 1), 3)\n            )\n        if self._image_dist == \"mse\":\n            return tools.MSEDist(mean)\n        raise NotImplementedError(self._image_dist)\n\n\nclass ConvEncoder(nn.Module):\n    def __init__(\n        self,\n        input_shape,\n        depth=32,\n        act=\"SiLU\",\n        norm=True,\n        kernel_size=4,\n        minres=4,\n    ):\n        super(ConvEncoder, self).__init__()\n        act = getattr(torch.nn, act)\n        h, w, input_ch = input_shape\n        stages = int(np.log2(h) - np.log2(minres))\n        in_dim = input_ch\n        out_dim = depth\n        layers = []\n        for i in range(stages):\n            layers.append(\n                Conv2dSamePad(\n                    in_channels=in_dim,\n                    out_channels=out_dim,\n                    kernel_size=kernel_size,\n                    stride=2,\n                    bias=False,\n                )\n            )\n            if norm:\n                layers.append(ImgChLayerNorm(out_dim))\n            layers.append(act())\n            in_dim = out_dim\n            out_dim *= 2\n            h, w = h // 2, w // 2\n\n        self.outdim = out_dim // 2 * h * w\n        self.layers = nn.Sequential(*layers)\n        self.layers.apply(tools.weight_init)\n\n    def forward(self, obs):\n        obs -= 0.5\n        # (batch, time, h, w, ch) -> (batch * time, h, w, ch)\n        x = obs.reshape((-1,) + tuple(obs.shape[-3:]))\n        # (batch * time, h, w, ch) -> (batch * time, ch, h, w)\n        x = x.permute(0, 3, 1, 2)\n        x = self.layers(x)\n        # (batch * time, ...) -> (batch * time, -1)\n        x = x.reshape([x.shape[0], np.prod(x.shape[1:])])\n        # (batch * time, -1) -> (batch, time, -1)\n        return x.reshape(list(obs.shape[:-3]) + [x.shape[-1]])\n\n\nclass ConvDecoder(nn.Module):\n    def __init__(\n        self,\n        feat_size,\n        shape=(3, 64, 64),\n        depth=32,\n        act=nn.ELU,\n        norm=True,\n        kernel_size=4,\n        minres=4,\n        outscale=1.0,\n        cnn_sigmoid=False,\n    ):\n        super(ConvDecoder, self).__init__()\n        act = getattr(torch.nn, act)\n        self._shape = shape\n        self._cnn_sigmoid = cnn_sigmoid\n        layer_num = int(np.log2(shape[1]) - np.log2(minres))\n        self._minres = minres\n        out_ch = minres**2 * depth * 2 ** (layer_num - 1)\n        self._embed_size = out_ch\n\n        self._linear_layer = nn.Linear(feat_size, out_ch)\n        self._linear_layer.apply(tools.uniform_weight_init(outscale))\n        in_dim = out_ch // (minres**2)\n        out_dim = in_dim // 2\n\n        layers = []\n        h, w = minres, minres\n        for i in range(layer_num):\n            bias = False\n            if i == layer_num - 1:\n                out_dim = self._shape[0]\n                act = False\n                bias = True\n                norm = False\n\n            if i != 0:\n                in_dim = 2 ** (layer_num - (i - 1) - 2) * depth\n            pad_h, outpad_h = self.calc_same_pad(k=kernel_size, s=2, d=1)\n            pad_w, outpad_w = self.calc_same_pad(k=kernel_size, s=2, d=1)\n            layers.append(\n                nn.ConvTranspose2d(\n                    in_dim,\n                    out_dim,\n                    kernel_size,\n                    2,\n                    padding=(pad_h, pad_w),\n                    output_padding=(outpad_h, outpad_w),\n                    bias=bias,\n                )\n            )\n            if norm:\n                layers.append(ImgChLayerNorm(out_dim))\n            if act:\n                layers.append(act())\n            in_dim = out_dim\n            out_dim //= 2\n            h, w = h * 2, w * 2\n        [m.apply(tools.weight_init) for m in layers[:-1]]\n        layers[-1].apply(tools.uniform_weight_init(outscale))\n        self.layers = nn.Sequential(*layers)\n\n    def calc_same_pad(self, k, s, d):\n        val = d * (k - 1) - s + 1\n        pad = math.ceil(val / 2)\n        outpad = pad * 2 - val\n        return pad, outpad\n\n    def forward(self, features, dtype=None):\n        x = self._linear_layer(features)\n        # (batch, time, -1) -> (batch * time, h, w, ch)\n        x = x.reshape(\n            [-1, self._minres, self._minres, self._embed_size // self._minres**2]\n        )\n        # (batch, time, -1) -> (batch * time, ch, h, w)\n        x = x.permute(0, 3, 1, 2)\n        x = self.layers(x)\n        # (batch, time, -1) -> (batch, time, ch, h, w)\n        mean = x.reshape(features.shape[:-1] + self._shape)\n        # (batch, time, ch, h, w) -> (batch, time, h, w, ch)\n        mean = mean.permute(0, 1, 3, 4, 2)\n        if self._cnn_sigmoid:\n            mean = F.sigmoid(mean)\n        else:\n            mean += 0.5\n        return mean\n\n\nclass MLP(nn.Module):\n    def __init__(\n        self,\n        inp_dim,\n        shape,\n        layers,\n        units,\n        act=\"SiLU\",\n        norm=True,\n        dist=\"normal\",\n        std=1.0,\n        min_std=0.1,\n        max_std=1.0,\n        absmax=None,\n        temp=0.1,\n        unimix_ratio=0.01,\n        outscale=1.0,\n        symlog_inputs=False,\n        device=\"cuda\",\n        name=\"NoName\",\n    ):\n        super(MLP, self).__init__()\n        self._shape = (shape,) if isinstance(shape, int) else shape\n        if self._shape is not None and len(self._shape) == 0:\n            self._shape = (1,)\n        act = getattr(torch.nn, act)\n        self._dist = dist\n        self._std = std if isinstance(std, str) else torch.tensor((std,), device=device)\n        self._min_std = min_std\n        self._max_std = max_std\n        self._absmax = absmax\n        self._temp = temp\n        self._unimix_ratio = unimix_ratio\n        self._symlog_inputs = symlog_inputs\n        self._device = device\n\n        self.layers = nn.Sequential()\n        for i in range(layers):\n            self.layers.add_module(\n                f\"{name}_linear{i}\", nn.Linear(inp_dim, units, bias=False)\n            )\n            if norm:\n                self.layers.add_module(\n                    f\"{name}_norm{i}\", nn.LayerNorm(units, eps=1e-03)\n                )\n            self.layers.add_module(f\"{name}_act{i}\", act())\n            if i == 0:\n                inp_dim = units\n        self.layers.apply(tools.weight_init)\n\n        if isinstance(self._shape, dict):\n            self.mean_layer = nn.ModuleDict()\n            for name, shape in self._shape.items():\n                self.mean_layer[name] = nn.Linear(inp_dim, np.prod(shape))\n            self.mean_layer.apply(tools.uniform_weight_init(outscale))\n            if self._std == \"learned\":\n                assert dist in (\"tanh_normal\", \"normal\", \"trunc_normal\", \"huber\"), dist\n                self.std_layer = nn.ModuleDict()\n                for name, shape in self._shape.items():\n                    self.std_layer[name] = nn.Linear(inp_dim, np.prod(shape))\n                self.std_layer.apply(tools.uniform_weight_init(outscale))\n        elif self._shape is not None:\n            self.mean_layer = nn.Linear(inp_dim, np.prod(self._shape))\n            self.mean_layer.apply(tools.uniform_weight_init(outscale))\n            if self._std == \"learned\":\n                assert dist in (\"tanh_normal\", \"normal\", \"trunc_normal\", \"huber\"), dist\n                self.std_layer = nn.Linear(units, np.prod(self._shape))\n                self.std_layer.apply(tools.uniform_weight_init(outscale))\n\n    def forward(self, features, dtype=None):\n        x = features\n        if self._symlog_inputs:\n            x = tools.symlog(x)\n        out = self.layers(x)\n        # Used for encoder output\n        if self._shape is None:\n            return out\n        if isinstance(self._shape, dict):\n            dists = {}\n            for name, shape in self._shape.items():\n                mean = self.mean_layer[name](out)\n                if self._std == \"learned\":\n                    std = self.std_layer[name](out)\n                else:\n                    std = self._std\n                dists.update({name: self.dist(self._dist, mean, std, shape)})\n            return dists\n        else:\n            mean = self.mean_layer(out)\n            if self._std == \"learned\":\n                std = self.std_layer(out)\n            else:\n                std = self._std\n            return self.dist(self._dist, mean, std, self._shape)\n\n    def dist(self, dist, mean, std, shape):\n        if dist == \"tanh_normal\":\n            mean = torch.tanh(mean)\n            std = F.softplus(std) + self._min_std\n            dist = torchd.normal.Normal(mean, std)\n            dist = torchd.transformed_distribution.TransformedDistribution(\n                dist, tools.TanhBijector()\n            )\n            dist = torchd.independent.Independent(dist, 1)\n            dist = tools.SampleDist(dist)\n        elif dist == \"normal\":\n            std = (self._max_std - self._min_std) * torch.sigmoid(\n                std + 2.0\n            ) + self._min_std\n            dist = torchd.normal.Normal(torch.tanh(mean), std)\n            dist = tools.ContDist(\n                torchd.independent.Independent(dist, 1), absmax=self._absmax\n            )\n        elif dist == \"normal_std_fixed\":\n            dist = torchd.normal.Normal(mean, self._std)\n            dist = tools.ContDist(\n                torchd.independent.Independent(dist, 1), absmax=self._absmax\n            )\n        elif dist == \"trunc_normal\":\n            mean = torch.tanh(mean)\n            std = 2 * torch.sigmoid(std / 2) + self._min_std\n            dist = tools.SafeTruncatedNormal(mean, std, -1, 1)\n            dist = tools.ContDist(\n                torchd.independent.Independent(dist, 1), absmax=self._absmax\n            )\n        elif dist == \"onehot\":\n            dist = tools.OneHotDist(mean, unimix_ratio=self._unimix_ratio)\n        elif dist == \"onehot_gumble\":\n            dist = tools.ContDist(\n                torchd.gumbel.Gumbel(mean, 1 / self._temp), absmax=self._absmax\n            )\n        elif dist == \"huber\":\n            dist = tools.ContDist(\n                torchd.independent.Independent(\n                    tools.UnnormalizedHuber(mean, std, 1.0),\n                    len(shape),\n                    absmax=self._absmax,\n                )\n            )\n        elif dist == \"binary\":\n            dist = tools.Bernoulli(\n                torchd.independent.Independent(\n                    torchd.bernoulli.Bernoulli(logits=mean), len(shape)\n                )\n            )\n        elif dist == \"symlog_disc\":\n            dist = tools.DiscDist(logits=mean, device=self._device)\n        elif dist == \"symlog_mse\":\n            dist = tools.SymlogDist(mean)\n        else:\n            raise NotImplementedError(dist)\n        return dist\n\n\nclass GRUCell(nn.Module):\n    def __init__(self, inp_size, size, norm=True, act=torch.tanh, update_bias=-1):\n        super(GRUCell, self).__init__()\n        self._inp_size = inp_size\n        self._size = size\n        self._act = act\n        self._update_bias = update_bias\n        self.layers = nn.Sequential()\n        self.layers.add_module(\n            \"GRU_linear\", nn.Linear(inp_size + size, 3 * size, bias=False)\n        )\n        if norm:\n            self.layers.add_module(\"GRU_norm\", nn.LayerNorm(3 * size, eps=1e-03))\n\n    @property\n    def state_size(self):\n        return self._size\n\n    def forward(self, inputs, state):\n        state = state[0]  # Keras wraps the state in a list.\n        parts = self.layers(torch.cat([inputs, state], -1))\n        reset, cand, update = torch.split(parts, [self._size] * 3, -1)\n        reset = torch.sigmoid(reset)\n        cand = self._act(reset * cand)\n        update = torch.sigmoid(update + self._update_bias)\n        output = update * cand + (1 - update) * state\n        return output, [output]\n\n\nclass Conv2dSamePad(torch.nn.Conv2d):\n    def calc_same_pad(self, i, k, s, d):\n        return max((math.ceil(i / s) - 1) * s + (k - 1) * d + 1 - i, 0)\n\n    def forward(self, x):\n        ih, iw = x.size()[-2:]\n        pad_h = self.calc_same_pad(\n            i=ih, k=self.kernel_size[0], s=self.stride[0], d=self.dilation[0]\n        )\n        pad_w = self.calc_same_pad(\n            i=iw, k=self.kernel_size[1], s=self.stride[1], d=self.dilation[1]\n        )\n\n        if pad_h > 0 or pad_w > 0:\n            x = F.pad(\n                x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2]\n            )\n\n        ret = F.conv2d(\n            x,\n            self.weight,\n            self.bias,\n            self.stride,\n            self.padding,\n            self.dilation,\n            self.groups,\n        )\n        return ret\n\n\nclass ImgChLayerNorm(nn.Module):\n    def __init__(self, ch, eps=1e-03):\n        super(ImgChLayerNorm, self).__init__()\n        self.norm = torch.nn.LayerNorm(ch, eps=eps)\n\n    def forward(self, x):\n        x = x.permute(0, 2, 3, 1)\n        x = self.norm(x)\n        x = x.permute(0, 3, 1, 2)\n        return x\n",
      "numLines": 920,
      "startLine": 1,
      "totalLines": 920
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01UVowmgZyhJXN1EpzRXwY1D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/models.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "2b017342-a60b-41aa-a99f-fd9364147bc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGvuUf2bFiCqJ6dSCykPiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12473,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12473
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

_source line 10 · 2026-05-13T06:37:10.401Z_

<details><summary>↩ Tool result · `toolu_01UVowmgZyhJXN1EpzRXwY1D`</summary>

```text
1	# Event-Gated Adaptive-Horizon DreamerV3 — World Model & Behavior
2	# Modified from NM512/dreamerv3-torch.
3	# Changes: WorldModel integrates EventGate + variable-dt sub-sampling;
4	#          ImagBehavior uses gate-driven dt in imagination + adapted lambda-returns.
5	
6	import copy
7	import math
8	
9	import torch
10	from torch import nn
11	from torch.nn import functional as F
12	
13	import networks
14	import tools
15	
16	to_np = lambda x: x.detach().cpu().numpy()
17	
18	
19	def compute_gate_targets(feats, max_dt):
20	    """Soft supervision target for the event gate derived from state deltas.
21	
22	    Large delta -> prefer small dt (index 0 = dt=1).
23	    Small delta -> prefer large dt (index K-1 = dt=K).
24	    """
25	    feats = feats.detach()
26	    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)
27	    delta_min = deltas.min(dim=0, keepdim=True).values
28	    delta_max = deltas.max(dim=0, keepdim=True).values
29	    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)
30	    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)
31	    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32, device=feats.device)
32	    sigma = 1.0
33	    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2
34	    target_dist = F.softmax(log_probs, dim=-1)
35	    return target_dist
36	
37	
38	def gate_loss_fn(gate_logits, target_dist):
39	    """Cross-entropy between gate predictions and supervision target."""
40	    log_probs = F.log_softmax(gate_logits, dim=-1)
41	    return -(target_dist * log_probs).sum(dim=-1)
42	
43	
44	class RewardEMA:
45	    """running mean and std"""
46	
47	    def __init__(self, device, alpha=1e-2):
48	        self.device = device
49	        self.alpha = alpha
50	        self.range = torch.tensor([0.05, 0.95], device=device)
51	
52	    def __call__(self, x, ema_vals):
53	        flat_x = torch.flatten(x.detach())
54	        x_quantile = torch.quantile(input=flat_x, q=self.range)
55	        # this should be in-place operation
56	        ema_vals[:] = self.alpha * x_quantile + (1 - self.alpha) * ema_vals
57	        scale = torch.clip(ema_vals[1] - ema_vals[0], min=1.0)
58	        offset = ema_vals[0]
59	        return offset.detach(), scale.detach()
60	
61	
62	class WorldModel(nn.Module):
63	    def __init__(self, obs_space, act_space, step, config):
64	        super(WorldModel, self).__init__()
65	        self._step = step
66	        self._use_amp = True if config.precision == 16 else False
67	        self._config = config
68	        shapes = {k: tuple(v.shape) for k, v in obs_space.spaces.items()}
69	        self.encoder = networks.MultiEncoder(shapes, **config.encoder)
70	        self.embed_size = self.encoder.outdim
71	        self.dynamics = networks.RSSM(
72	            config.dyn_stoch,
73	            config.dyn_deter,
74	            config.dyn_hidden,
75	            config.dyn_rec_depth,
76	            config.dyn_discrete,
77	            config.act,
78	            config.norm,
79	            config.dyn_mean_act,
80	            config.dyn_std_act,
81	            config.dyn_min_std,
82	            config.unimix_ratio,
83	            config.initial,
84	            config.num_actions,
85	            self.embed_size,
86	            config.device,
87	            max_dt=config.gate_max_dt if config.gate_enabled else 1,
88	            dt_embed_dim=config.gate_dt_embed_dim,
89	        )
90	        self.heads = nn.ModuleDict()
91	        if config.dyn_discrete:
92	            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter
93	        else:
94	            feat_size = config.dyn_stoch + config.dyn_deter
95	        self.heads["decoder"] = networks.MultiDecoder(
96	            feat_size, shapes, **config.decoder
97	        )
98	        self.heads["reward"] = networks.MLP(
99	            feat_size,
100	            (255,) if config.reward_head["dist"] == "symlog_disc" else (),
101	            config.reward_head["layers"],
102	            config.units,
103	            config.act,
104	            config.norm,
105	            dist=config.reward_head["dist"],
106	            outscale=config.reward_head["outscale"],
107	            device=config.device,
108	            name="Reward",
109	        )
110	        self.heads["cont"] = networks.MLP(
111	            feat_size,
112	            (),
113	            config.cont_head["layers"],
114	            config.units,
115	            config.act,
116	            config.norm,
117	            dist="binary",
118	            outscale=config.cont_head["outscale"],
119	            device=config.device,
120	            name="Cont",
121	        )
122	
123	        if config.gate_enabled:
124	            self.event_gate = networks.EventGate(
125	                feat_size=feat_size,
126	                max_dt=config.gate_max_dt,
127	                hidden_units=config.gate_hidden_units,
128	                hidden_layers=config.gate_hidden_layers,
129	                act=config.act,
130	                norm=config.norm,
131	                tau_init=config.gate_tau_init,
132	                tau_final=config.gate_tau_final,
133	                tau_anneal_steps=config.gate_tau_anneal_steps,
134	            )
135	            self.register_buffer(
136	                "gate_step", torch.tensor(0, dtype=torch.long)
137	            )
138	        else:
139	            self.event_gate = None
140	
141	        for name in config.grad_heads:
142	            assert name in self.heads, name
143	        self._model_opt = tools.Optimizer(
144	            "model",
145	            self.parameters(),
146	            config.model_lr,
147	            config.opt_eps,
148	            config.grad_clip,
149	            config.weight_decay,
150	            opt=config.opt,
151	            use_amp=self._use_amp,
152	        )
153	        print(
154	            f"Optimizer model_opt has {sum(param.numel() for param in self.parameters())} variables."
155	        )
156	        # other losses are scaled by 1.0.
157	        self._scales = dict(
158	            reward=config.reward_head["loss_scale"],
159	            cont=config.cont_head["loss_scale"],
160	        )
161	
162	    def _train(self, data):
163	        # action (batch_size, batch_length, act_dim)
164	        # image (batch_size, batch_length, h, w, ch)
165	        # reward (batch_size, batch_length)
166	        # discount (batch_size, batch_length)
167	        data = self.preprocess(data)
168	
169	        if self._config.gate_enabled:
170	            self.gate_step += 1
171	            data, dt_labels = tools.subsample_variable_dt(
172	                data, self._config.gate_max_dt, self._config.discount,
173	            )
174	        else:
175	            dt_labels = None
176	
177	        with tools.RequiresGrad(self):
178	            with torch.cuda.amp.autocast(self._use_amp):
179	                embed = self.encoder(data)
180	                if dt_labels is not None:
181	                    post, prior = self.dynamics.observe(
182	                        embed, data["action"], data["is_first"],
183	                        dt_labels=dt_labels,
184	                    )
185	                else:
186	                    post, prior = self.dynamics.observe(
187	                        embed, data["action"], data["is_first"]
188	                    )
189	                kl_free = self._config.kl_free
190	                dyn_scale = self._config.dyn_scale
191	                rep_scale = self._config.rep_scale
192	                kl_loss, kl_value, dyn_loss, rep_loss = self.dynamics.kl_loss(
193	                    post, prior, kl_free, dyn_scale, rep_scale
194	                )
195	                assert kl_loss.shape == embed.shape[:2], kl_loss.shape
196	                preds = {}
197	                for name, head in self.heads.items():
198	                    grad_head = name in self._config.grad_heads
199	                    feat = self.dynamics.get_feat(post)
200	                    feat = feat if grad_head else feat.detach()
201	                    pred = head(feat)
202	                    if type(pred) is dict:
203	                        preds.update(pred)
204	                    else:
205	                        preds[name] = pred
206	                losses = {}
207	                for name, pred in preds.items():
208	                    loss = -pred.log_prob(data[name])
209	                    assert loss.shape == embed.shape[:2], (name, loss.shape)
210	                    losses[name] = loss
211	                scaled = {
212	                    key: value * self._scales.get(key, 1.0)
213	                    for key, value in losses.items()
214	                }
215	                model_loss = sum(scaled.values()) + kl_loss
216	                mean_model_loss = torch.mean(model_loss)
217	
218	                if self._config.gate_enabled and self.event_gate is not None:
219	                    gate_feat = self.dynamics.get_feat(post).detach()
220	                    B_g, T_g, D_g = gate_feat.shape
221	                    gate_feat_flat = gate_feat.reshape(B_g * T_g, D_g)
222	                    step = self.gate_step.item()
223	                    _, _, gate_logits_flat = self.event_gate(
224	                        gate_feat_flat, step, hard=False
225	                    )
226	                    gate_logits = gate_logits_flat.reshape(
227	                        B_g, T_g, self._config.gate_max_dt
228	                    )
229	
230	                    feat_time = gate_feat.permute(1, 0, 2)
231	                    target_dist = compute_gate_targets(
232	                        feat_time, self._config.gate_max_dt
233	                    )
234	
235	                    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)
236	                    g_loss = gate_loss_fn(g_logits, target_dist)
237	
238	                    g_entropy = self.event_gate.entropy(
239	                        g_logits.reshape(-1, self._config.gate_max_dt)
240	                    ).reshape(g_loss.shape)
241	
242	                    if step < self._config.gate_curriculum_phase1:
243	                        gate_scale = 0.0
244	                    elif step < self._config.gate_curriculum_phase2:
245	                        progress = (step - self._config.gate_curriculum_phase1) / (
246	                            self._config.gate_curriculum_phase2
247	                            - self._config.gate_curriculum_phase1
248	                        )
249	                        gate_scale = progress
250	                    else:
251	                        gate_scale = 1.0
252	
253	                    entropy_frac = min(
254	                        step / max(self._config.gate_tau_anneal_steps, 1), 1.0
255	                    )
256	                    effective_entropy_bonus = (
257	                        self._config.gate_entropy_bonus_init
258	                        + entropy_frac
259	                        * (
260	                            self._config.gate_entropy_bonus_final
261	                            - self._config.gate_entropy_bonus_init
262	                        )
263	                    )
264	
265	                    total_gate_loss = gate_scale * (
266	                        self._config.gate_loss_weight * g_loss.mean()
267	                        - effective_entropy_bonus * g_entropy.mean()
268	                    )
269	                    mean_model_loss = mean_model_loss + total_gate_loss
270	
271	            metrics = self._model_opt(mean_model_loss, self.parameters())
272	
273	        # Store scalar metrics to avoid keeping (batch,time) arrays until the next log step.
274	        metrics.update(
275	            {f"{name}_loss": to_np(torch.mean(loss)) for name, loss in losses.items()}
276	        )
277	        metrics["kl_free"] = kl_free
278	        metrics["dyn_scale"] = dyn_scale
279	        metrics["rep_scale"] = rep_scale
280	        metrics["dyn_loss"] = to_np(torch.mean(dyn_loss))
281	        metrics["rep_loss"] = to_np(torch.mean(rep_loss))
282	        metrics["kl"] = to_np(torch.mean(kl_value))
283	        with torch.cuda.amp.autocast(self._use_amp):
284	            metrics["prior_ent"] = to_np(
285	                torch.mean(self.dynamics.get_dist(prior).entropy())
286	            )
287	            metrics["post_ent"] = to_np(
288	                torch.mean(self.dynamics.get_dist(post).entropy())
289	            )
290	            context = dict(
291	                embed=embed,
292	                feat=self.dynamics.get_feat(post),
293	                kl=kl_value,
294	                postent=self.dynamics.get_dist(post).entropy(),
295	            )
296	
297	        if self._config.gate_enabled and self.event_gate is not None:
298	            metrics["gate_loss"] = to_np(total_gate_loss)
299	            metrics["gate_scale"] = gate_scale
300	            metrics["gate_entropy_bonus"] = effective_entropy_bonus
301	
302	        post = {k: v.detach() for k, v in post.items()}
303	        return post, context, metrics
304	
305	    # this function is called during both rollout and training
306	    def preprocess(self, obs):
307	        obs = {
308	            k: torch.tensor(v, device=self._config.device, dtype=torch.float32)
309	            for k, v in obs.items()
310	        }
311	        obs["image"] = obs["image"] / 255.0
312	        if "discount" in obs:
313	            obs["discount"] *= self._config.discount
314	            # (batch_size, batch_length) -> (batch_size, batch_length, 1)
315	            obs["discount"] = obs["discount"].unsqueeze(-1)
316	        # 'is_first' is necesarry to initialize hidden state at training
317	        assert "is_first" in obs
318	        # 'is_terminal' is necesarry to train cont_head
319	        assert "is_terminal" in obs
320	        obs["cont"] = (1.0 - obs["is_terminal"]).unsqueeze(-1)
321	        return obs
322	
323	    def video_pred(self, data):
324	        data = self.preprocess(data)
325	        embed = self.encoder(data)
326	
327	        states, _ = self.dynamics.observe(
328	            embed[:6, :5], data["action"][:6, :5], data["is_first"][:6, :5]
329	        )
330	        recon = self.heads["decoder"](self.dynamics.get_feat(states))["image"].mode()[
331	            :6
332	        ]
333	        reward_post = self.heads["reward"](self.dynamics.get_feat(states)).mode()[:6]
334	        init = {k: v[:, -1] for k, v in states.items()}
335	        prior = self.dynamics.imagine_with_action(data["action"][:6, 5:], init)
336	        openl = self.heads["decoder"](self.dynamics.get_feat(prior))["image"].mode()
337	        reward_prior = self.heads["reward"](self.dynamics.get_feat(prior)).mode()
338	        # observed image is given until 5 steps
339	        model = torch.cat([recon[:, :5], openl], 1)
340	        truth = data["image"][:6]
341	        model = model
342	        error = (model - truth + 1.0) / 2.0
343	
344	        return torch.cat([truth, model, error], 2)
345	
346	
347	class ImagBehavior(nn.Module):
348	    def __init__(self, config, world_model):
349	        super(ImagBehavior, self).__init__()
350	        self._use_amp = True if config.precision == 16 else False
351	        self._config = config
352	        self._world_model = world_model
353	        if config.dyn_discrete:
354	            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter
355	        else:
356	            feat_size = config.dyn_stoch + config.dyn_deter
357	        self.actor = networks.MLP(
358	            feat_size,
359	            (config.num_actions,),
360	            config.actor["layers"],
361	            config.units,
362	            config.act,
363	            config.norm,
364	            config.actor["dist"],
365	            config.actor["std"],
366	            config.actor["min_std"],
367	            config.actor["max_std"],
368	            absmax=1.0,
369	            temp=config.actor["temp"],
370	            unimix_ratio=config.actor["unimix_ratio"],
371	            outscale=config.actor["outscale"],
372	            name="Actor",
373	        )
374	        self.value = networks.MLP(
375	            feat_size,
376	            (255,) if config.critic["dist"] == "symlog_disc" else (),
377	            config.critic["layers"],
378	            config.units,
379	            config.act,
380	            config.norm,
381	            config.critic["dist"],
382	            outscale=config.critic["outscale"],
383	            device=config.device,
384	            name="Value",
385	        )
386	        if config.critic["slow_target"]:
387	            self._slow_value = copy.deepcopy(self.value)
388	            self._updates = 0
389	        kw = dict(wd=config.weight_decay, opt=config.opt, use_amp=self._use_amp)
390	        self._actor_opt = tools.Optimizer(
391	            "actor",
392	            self.actor.parameters(),
393	            config.actor["lr"],
394	            config.actor["eps"],
395	            config.actor["grad_clip"],
396	            **kw,
397	        )
398	        print(
399	            f"Optimizer actor_opt has {sum(param.numel() for param in self.actor.parameters())} variables."
400	        )
401	        self._value_opt = tools.Optimizer(
402	            "value",
403	            self.value.parameters(),
404	            config.critic["lr"],
405	            config.critic["eps"],
406	            config.critic["grad_clip"],
407	            **kw,
408	        )
409	        print(
410	            f"Optimizer value_opt has {sum(param.numel() for param in self.value.parameters())} variables."
411	        )
412	        if self._config.reward_EMA:
413	            # register ema_vals to nn.Module for enabling torch.save and torch.load
414	            self.register_buffer(
415	                "ema_vals", torch.zeros((2,), device=self._config.device)
416	            )
417	            self.reward_ema = RewardEMA(device=self._config.device)
418	
419	    def _train(
420	        self,
421	        start,
422	        objective,
423	    ):
424	        self._update_slow_target()
425	        metrics = {}
426	
427	        with tools.RequiresGrad(self.actor):
428	            with torch.cuda.amp.autocast(self._use_amp):
429	                if self._config.gate_enabled:
430	                    imag_feat, imag_state, imag_action, dts = self._imagine(
431	                        start, self.actor, self._config.imag_horizon
432	                    )
433	                else:
434	                    imag_feat, imag_state, imag_action = self._imagine(
435	                        start, self.actor, self._config.imag_horizon
436	                    )
437	                    dts = None
438	                reward = objective(imag_feat, imag_state, imag_action)
439	                actor_ent = self.actor(imag_feat).entropy()
440	                state_ent = self._world_model.dynamics.get_dist(imag_state).entropy()
441	                # this target is not scaled by ema or sym_log.
442	                target, weights, base = self._compute_target(
443	                    imag_feat, imag_state, reward, dts=dts
444	                )
445	                actor_loss, mets = self._compute_actor_loss(
446	                    imag_feat,
447	                    imag_action,
448	                    target,
449	                    weights,
450	                    base,
451	                )
452	                actor_loss -= self._config.actor["entropy"] * actor_ent[:-1, ..., None]
453	                actor_loss = torch.mean(actor_loss)
454	                metrics.update(mets)
455	                value_input = imag_feat
456	
457	        with tools.RequiresGrad(self.value):
458	            with torch.cuda.amp.autocast(self._use_amp):
459	                value = self.value(value_input[:-1].detach())
460	                target = torch.stack(target, dim=1)
461	                # (time, batch, 1), (time, batch, 1) -> (time, batch)
462	                value_loss = -value.log_prob(target.detach())
463	                slow_target = self._slow_value(value_input[:-1].detach())
464	                if self._config.critic["slow_target"]:
465	                    value_loss -= value.log_prob(slow_target.mode().detach())
466	                # (time, batch, 1), (time, batch, 1) -> (1,)
467	                value_loss = torch.mean(weights[:-1] * value_loss[:, :, None])
468	
469	        metrics.update(tools.tensorstats(value.mode(), "value"))
470	        metrics.update(tools.tensorstats(target, "target"))
471	        metrics.update(tools.tensorstats(reward, "imag_reward"))
472	        if self._config.actor["dist"] in ["onehot"]:
473	            metrics.update(
474	                tools.tensorstats(
475	                    torch.argmax(imag_action, dim=-1).float(), "imag_action"
476	                )
477	            )
478	        else:
479	            metrics.update(tools.tensorstats(imag_action, "imag_action"))
480	        metrics["actor_entropy"] = to_np(torch.mean(actor_ent))
481	
482	        if self._config.gate_enabled and dts is not None:
483	            dts_float = dts.float()
484	            metrics["gate_dt_mean"] = to_np(torch.mean(dts_float))
485	            metrics["gate_dt_std"] = to_np(torch.std(dts_float))
486	            metrics["gate_dt_min"] = to_np(torch.min(dts_float))
487	            metrics["gate_dt_max"] = to_np(torch.max(dts_float))
488	            dt_counts = torch.bincount(
489	                dts.reshape(-1).long(),
490	                minlength=self._config.gate_max_dt + 1,
491	            )[1:]
492	            dt_dist = dt_counts.float() / dt_counts.sum()
493	            for k in range(self._config.gate_max_dt):
494	                metrics[f"gate_dt_{k+1}_frac"] = to_np(dt_dist[k])
495	            emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()
496	            metrics["gate_empirical_entropy"] = to_np(emp_entropy)
497	            max_entropy = math.log(self._config.gate_max_dt)
498	            metrics["gate_entropy_ratio"] = to_np(emp_entropy) / max_entropy
499	
500	        with tools.RequiresGrad(self):
501	            metrics.update(self._actor_opt(actor_loss, self.actor.parameters()))
502	            metrics.update(self._value_opt(value_loss, self.value.parameters()))
503	        return imag_feat, imag_state, imag_action, weights, metrics
504	
505	    def _imagine(self, start, policy, horizon):
506	        dynamics = self._world_model.dynamics
507	        flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))
508	        start = {k: flatten(v) for k, v in start.items()}
509	
510	        if self._config.gate_enabled:
511	            gate = self._world_model.event_gate
512	            config = self._config
513	            step = self._world_model.gate_step.item() if hasattr(
514	                self._world_model, "gate_step"
515	            ) else 0
516	            gate_active = (
517	                gate is not None and step > config.gate_curriculum_phase1
518	            )
519	
520	            def step_fn(prev, _):
521	                state, _, _, prev_dt = prev
522	                feat = dynamics.get_feat(state)
523	                inp = feat.detach()
524	                action = policy(inp).sample()
525	                succ = dynamics.img_step(state, action, dt=prev_dt)
526	                succ_feat = dynamics.get_feat(succ)
527	                if gate_active:
528	                    _, next_dt, _ = gate(succ_feat.detach(), step, hard=True)
529	                else:
530	                    batch_size = succ_feat.shape[0]
531	                    next_dt = torch.ones(
532	                        batch_size, dtype=torch.long, device=succ_feat.device
533	                    )
534	                return succ, feat, action, next_dt
535	
536	            init_dt = torch.ones(
537	                start[list(start.keys())[0]].shape[0],
538	                dtype=torch.long, device=config.device,
539	            )
540	            succ, feats, actions, dts = tools.static_scan(
541	                step_fn, [torch.arange(horizon)],
542	                (start, None, None, init_dt),
543	            )
544	            states = {
545	                k: torch.cat([start[k][None], v[:-1]], 0)
546	                for k, v in succ.items()
547	            }
548	            return feats, states, actions, dts
549	        else:
550	            def step(prev, _):
551	                state, _, _ = prev
552	                feat = dynamics.get_feat(state)
553	                inp = feat.detach()
554	                action = policy(inp).sample()
555	                succ = dynamics.img_step(state, action)
556	                return succ, feat, action
557	
558	            succ, feats, actions = tools.static_scan(
559	                step, [torch.arange(horizon)], (start, None, None)
560	            )
561	            states = {
562	                k: torch.cat([start[k][None], v[:-1]], 0)
563	                for k, v in succ.items()
564	            }
565	            return feats, states, actions
566	
567	    def _compute_target(self, imag_feat, imag_state, reward, dts=None):
568	        if "cont" in self._world_model.heads:
569	            inp = self._world_model.dynamics.get_feat(imag_state)
570	            discount = self._config.discount * self._world_model.heads["cont"](inp).mean
571	        else:
572	            discount = self._config.discount * torch.ones_like(reward)
573	        value = self.value(imag_feat).mode()
574	
575	        if dts is not None and self._config.gate_enabled:
576	            target = tools.lambda_return_variable_dt(
577	                reward[1:],
578	                value[:-1],
579	                discount[1:],
580	                dts[1:],
581	                bootstrap=value[-1],
582	                lambda_=self._config.discount_lambda,
583	                axis=0,
584	            )
585	            pcont_adj = discount ** dts.unsqueeze(-1).float()
586	            weights = torch.cumprod(
587	                torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0
588	            ).detach()
589	        else:
590	            target = tools.lambda_return(
591	                reward[1:],
592	                value[:-1],
593	                discount[1:],
594	                bootstrap=value[-1],
595	                lambda_=self._config.discount_lambda,
596	                axis=0,
597	            )
598	            weights = torch.cumprod(
599	                torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0
600	            ).detach()
601	        return target, weights, value[:-1]
602	
603	    def _compute_actor_loss(
604	        self,
605	        imag_feat,
606	        imag_action,
607	        target,
608	        weights,
609	        base,
610	    ):
611	        metrics = {}
612	        inp = imag_feat.detach()
613	        policy = self.actor(inp)
614	        # Q-val for actor is not transformed using symlog
615	        target = torch.stack(target, dim=1)
616	        if self._config.reward_EMA:
617	            offset, scale = self.reward_ema(target, self.ema_vals)
618	            normed_target = (target - offset) / scale
619	            normed_base = (base - offset) / scale
620	            adv = normed_target - normed_base
621	            metrics.update(tools.tensorstats(normed_target, "normed_target"))
622	            metrics["EMA_005"] = to_np(self.ema_vals[0])
623	            metrics["EMA_095"] = to_np(self.ema_vals[1])
624	        else:
625	            adv = target - base
626	
627	        if self._config.imag_gradient == "dynamics":
628	            actor_target = adv
629	        elif self._config.imag_gradient == "reinforce":
630	            actor_target = (
631	                policy.log_prob(imag_action)[:-1][:, :, None]
632	                * (target - self.value(imag_feat[:-1]).mode()).detach()
633	            )
634	        elif self._config.imag_gradient == "both":
635	            actor_target = (
636	                policy.log_prob(imag_action)[:-1][:, :, None]
637	                * (target - self.value(imag_feat[:-1]).mode()).detach()
638	            )
639	            mix = self._config.imag_gradient_mix
640	            actor_target = mix * target + (1 - mix) * actor_target
641	            metrics["imag_gradient_mix"] = mix
642	        else:
643	            raise NotImplementedError(self._config.imag_gradient)
644	        actor_loss = -weights[:-1] * actor_target
645	        return actor_loss, metrics
646	
647	    def _update_slow_target(self):
648	        if self._config.critic["slow_target"]:
649	            if self._updates % self._config.critic["slow_target_update"] == 0:
650	                mix = self._config.critic["slow_target_fraction"]
651	                for s, d in zip(self.value.parameters(), self._slow_value.parameters()):
652	                    d.data = mix * s.data + (1 - mix) * d.data
653	            self._updates += 1
654	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "c1c5590c-0124-4c0c-9a71-5a93f6e9b7d0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/models.py",
      "content": "# Event-Gated Adaptive-Horizon DreamerV3 — World Model & Behavior\n# Modified from NM512/dreamerv3-torch.\n# Changes: WorldModel integrates EventGate + variable-dt sub-sampling;\n#          ImagBehavior uses gate-driven dt in imagination + adapted lambda-returns.\n\nimport copy\nimport math\n\nimport torch\nfrom torch import nn\nfrom torch.nn import functional as F\n\nimport networks\nimport tools\n\nto_np = lambda x: x.detach().cpu().numpy()\n\n\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"Soft supervision target for the event gate derived from state deltas.\n\n    Large delta -> prefer small dt (index 0 = dt=1).\n    Small delta -> prefer large dt (index K-1 = dt=K).\n    \"\"\"\n    feats = feats.detach()\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32, device=feats.device)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)\n    return target_dist\n\n\ndef gate_loss_fn(gate_logits, target_dist):\n    \"\"\"Cross-entropy between gate predictions and supervision target.\"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    return -(target_dist * log_probs).sum(dim=-1)\n\n\nclass RewardEMA:\n    \"\"\"running mean and std\"\"\"\n\n    def __init__(self, device, alpha=1e-2):\n        self.device = device\n        self.alpha = alpha\n        self.range = torch.tensor([0.05, 0.95], device=device)\n\n    def __call__(self, x, ema_vals):\n        flat_x = torch.flatten(x.detach())\n        x_quantile = torch.quantile(input=flat_x, q=self.range)\n        # this should be in-place operation\n        ema_vals[:] = self.alpha * x_quantile + (1 - self.alpha) * ema_vals\n        scale = torch.clip(ema_vals[1] - ema_vals[0], min=1.0)\n        offset = ema_vals[0]\n        return offset.detach(), scale.detach()\n\n\nclass WorldModel(nn.Module):\n    def __init__(self, obs_space, act_space, step, config):\n        super(WorldModel, self).__init__()\n        self._step = step\n        self._use_amp = True if config.precision == 16 else False\n        self._config = config\n        shapes = {k: tuple(v.shape) for k, v in obs_space.spaces.items()}\n        self.encoder = networks.MultiEncoder(shapes, **config.encoder)\n        self.embed_size = self.encoder.outdim\n        self.dynamics = networks.RSSM(\n            config.dyn_stoch,\n            config.dyn_deter,\n            config.dyn_hidden,\n            config.dyn_rec_depth,\n            config.dyn_discrete,\n            config.act,\n            config.norm,\n            config.dyn_mean_act,\n            config.dyn_std_act,\n            config.dyn_min_std,\n            config.unimix_ratio,\n            config.initial,\n            config.num_actions,\n            self.embed_size,\n            config.device,\n            max_dt=config.gate_max_dt if config.gate_enabled else 1,\n            dt_embed_dim=config.gate_dt_embed_dim,\n        )\n        self.heads = nn.ModuleDict()\n        if config.dyn_discrete:\n            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter\n        else:\n            feat_size = config.dyn_stoch + config.dyn_deter\n        self.heads[\"decoder\"] = networks.MultiDecoder(\n            feat_size, shapes, **config.decoder\n        )\n        self.heads[\"reward\"] = networks.MLP(\n            feat_size,\n            (255,) if config.reward_head[\"dist\"] == \"symlog_disc\" else (),\n            config.reward_head[\"layers\"],\n            config.units,\n            config.act,\n            config.norm,\n            dist=config.reward_head[\"dist\"],\n            outscale=config.reward_head[\"outscale\"],\n            device=config.device,\n            name=\"Reward\",\n        )\n        self.heads[\"cont\"] = networks.MLP(\n            feat_size,\n            (),\n            config.cont_head[\"layers\"],\n            config.units,\n            config.act,\n            config.norm,\n            dist=\"binary\",\n            outscale=config.cont_head[\"outscale\"],\n            device=config.device,\n            name=\"Cont\",\n        )\n\n        if config.gate_enabled:\n            self.event_gate = networks.EventGate(\n                feat_size=feat_size,\n                max_dt=config.gate_max_dt,\n                hidden_units=config.gate_hidden_units,\n                hidden_layers=config.gate_hidden_layers,\n                act=config.act,\n                norm=config.norm,\n                tau_init=config.gate_tau_init,\n                tau_final=config.gate_tau_final,\n                tau_anneal_steps=config.gate_tau_anneal_steps,\n            )\n            self.register_buffer(\n                \"gate_step\", torch.tensor(0, dtype=torch.long)\n            )\n        else:\n            self.event_gate = None\n\n        for name in config.grad_heads:\n            assert name in self.heads, name\n        self._model_opt = tools.Optimizer(\n            \"model\",\n            self.parameters(),\n            config.model_lr,\n            config.opt_eps,\n            config.grad_clip,\n            config.weight_decay,\n            opt=config.opt,\n            use_amp=self._use_amp,\n        )\n        print(\n            f\"Optimizer model_opt has {sum(param.numel() for param in self.parameters())} variables.\"\n        )\n        # other losses are scaled by 1.0.\n        self._scales = dict(\n            reward=config.reward_head[\"loss_scale\"],\n            cont=config.cont_head[\"loss_scale\"],\n        )\n\n    def _train(self, data):\n        # action (batch_size, batch_length, act_dim)\n        # image (batch_size, batch_length, h, w, ch)\n        # reward (batch_size, batch_length)\n        # discount (batch_size, batch_length)\n        data = self.preprocess(data)\n\n        if self._config.gate_enabled:\n            self.gate_step += 1\n            data, dt_labels = tools.subsample_variable_dt(\n                data, self._config.gate_max_dt, self._config.discount,\n            )\n        else:\n            dt_labels = None\n\n        with tools.RequiresGrad(self):\n            with torch.cuda.amp.autocast(self._use_amp):\n                embed = self.encoder(data)\n                if dt_labels is not None:\n                    post, prior = self.dynamics.observe(\n                        embed, data[\"action\"], data[\"is_first\"],\n                        dt_labels=dt_labels,\n                    )\n                else:\n                    post, prior = self.dynamics.observe(\n                        embed, data[\"action\"], data[\"is_first\"]\n                    )\n                kl_free = self._config.kl_free\n                dyn_scale = self._config.dyn_scale\n                rep_scale = self._config.rep_scale\n                kl_loss, kl_value, dyn_loss, rep_loss = self.dynamics.kl_loss(\n                    post, prior, kl_free, dyn_scale, rep_scale\n                )\n                assert kl_loss.shape == embed.shape[:2], kl_loss.shape\n                preds = {}\n                for name, head in self.heads.items():\n                    grad_head = name in self._config.grad_heads\n                    feat = self.dynamics.get_feat(post)\n                    feat = feat if grad_head else feat.detach()\n                    pred = head(feat)\n                    if type(pred) is dict:\n                        preds.update(pred)\n                    else:\n                        preds[name] = pred\n                losses = {}\n                for name, pred in preds.items():\n                    loss = -pred.log_prob(data[name])\n                    assert loss.shape == embed.shape[:2], (name, loss.shape)\n                    losses[name] = loss\n                scaled = {\n                    key: value * self._scales.get(key, 1.0)\n                    for key, value in losses.items()\n                }\n                model_loss = sum(scaled.values()) + kl_loss\n                mean_model_loss = torch.mean(model_loss)\n\n                if self._config.gate_enabled and self.event_gate is not None:\n                    gate_feat = self.dynamics.get_feat(post).detach()\n                    B_g, T_g, D_g = gate_feat.shape\n                    gate_feat_flat = gate_feat.reshape(B_g * T_g, D_g)\n                    step = self.gate_step.item()\n                    _, _, gate_logits_flat = self.event_gate(\n                        gate_feat_flat, step, hard=False\n                    )\n                    gate_logits = gate_logits_flat.reshape(\n                        B_g, T_g, self._config.gate_max_dt\n                    )\n\n                    feat_time = gate_feat.permute(1, 0, 2)\n                    target_dist = compute_gate_targets(\n                        feat_time, self._config.gate_max_dt\n                    )\n\n                    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)\n                    g_loss = gate_loss_fn(g_logits, target_dist)\n\n                    g_entropy = self.event_gate.entropy(\n                        g_logits.reshape(-1, self._config.gate_max_dt)\n                    ).reshape(g_loss.shape)\n\n                    if step < self._config.gate_curriculum_phase1:\n                        gate_scale = 0.0\n                    elif step < self._config.gate_curriculum_phase2:\n                        progress = (step - self._config.gate_curriculum_phase1) / (\n                            self._config.gate_curriculum_phase2\n                            - self._config.gate_curriculum_phase1\n                        )\n                        gate_scale = progress\n                    else:\n                        gate_scale = 1.0\n\n                    entropy_frac = min(\n                        step / max(self._config.gate_tau_anneal_steps, 1), 1.0\n                    )\n                    effective_entropy_bonus = (\n                        self._config.gate_entropy_bonus_init\n                        + entropy_frac\n                        * (\n                            self._config.gate_entropy_bonus_final\n                            - self._config.gate_entropy_bonus_init\n                        )\n                    )\n\n                    total_gate_loss = gate_scale * (\n                        self._config.gate_loss_weight * g_loss.mean()\n                        - effective_entropy_bonus * g_entropy.mean()\n                    )\n                    mean_model_loss = mean_model_loss + total_gate_loss\n\n            metrics = self._model_opt(mean_model_loss, self.parameters())\n\n        # Store scalar metrics to avoid keeping (batch,time) arrays until the next log step.\n        metrics.update(\n            {f\"{name}_loss\": to_np(torch.mean(loss)) for name, loss in losses.items()}\n        )\n        metrics[\"kl_free\"] = kl_free\n        metrics[\"dyn_scale\"] = dyn_scale\n        metrics[\"rep_scale\"] = rep_scale\n        metrics[\"dyn_loss\"] = to_np(torch.mean(dyn_loss))\n        metrics[\"rep_loss\"] = to_np(torch.mean(rep_loss))\n        metrics[\"kl\"] = to_np(torch.mean(kl_value))\n        with torch.cuda.amp.autocast(self._use_amp):\n            metrics[\"prior_ent\"] = to_np(\n                torch.mean(self.dynamics.get_dist(prior).entropy())\n            )\n            metrics[\"post_ent\"] = to_np(\n                torch.mean(self.dynamics.get_dist(post).entropy())\n            )\n            context = dict(\n                embed=embed,\n                feat=self.dynamics.get_feat(post),\n                kl=kl_value,\n                postent=self.dynamics.get_dist(post).entropy(),\n            )\n\n        if self._config.gate_enabled and self.event_gate is not None:\n            metrics[\"gate_loss\"] = to_np(total_gate_loss)\n            metrics[\"gate_scale\"] = gate_scale\n            metrics[\"gate_entropy_bonus\"] = effective_entropy_bonus\n\n        post = {k: v.detach() for k, v in post.items()}\n        return post, context, metrics\n\n    # this function is called during both rollout and training\n    def preprocess(self, obs):\n        obs = {\n            k: torch.tensor(v, device=self._config.device, dtype=torch.float32)\n            for k, v in obs.items()\n        }\n        obs[\"image\"] = obs[\"image\"] / 255.0\n        if \"discount\" in obs:\n            obs[\"discount\"] *= self._config.discount\n            # (batch_size, batch_length) -> (batch_size, batch_length, 1)\n            obs[\"discount\"] = obs[\"discount\"].unsqueeze(-1)\n        # 'is_first' is necesarry to initialize hidden state at training\n        assert \"is_first\" in obs\n        # 'is_terminal' is necesarry to train cont_head\n        assert \"is_terminal\" in obs\n        obs[\"cont\"] = (1.0 - obs[\"is_terminal\"]).unsqueeze(-1)\n        return obs\n\n    def video_pred(self, data):\n        data = self.preprocess(data)\n        embed = self.encoder(data)\n\n        states, _ = self.dynamics.observe(\n            embed[:6, :5], data[\"action\"][:6, :5], data[\"is_first\"][:6, :5]\n        )\n        recon = self.heads[\"decoder\"](self.dynamics.get_feat(states))[\"image\"].mode()[\n            :6\n        ]\n        reward_post = self.heads[\"reward\"](self.dynamics.get_feat(states)).mode()[:6]\n        init = {k: v[:, -1] for k, v in states.items()}\n        prior = self.dynamics.imagine_with_action(data[\"action\"][:6, 5:], init)\n        openl = self.heads[\"decoder\"](self.dynamics.get_feat(prior))[\"image\"].mode()\n        reward_prior = self.heads[\"reward\"](self.dynamics.get_feat(prior)).mode()\n        # observed image is given until 5 steps\n        model = torch.cat([recon[:, :5], openl], 1)\n        truth = data[\"image\"][:6]\n        model = model\n        error = (model - truth + 1.0) / 2.0\n\n        return torch.cat([truth, model, error], 2)\n\n\nclass ImagBehavior(nn.Module):\n    def __init__(self, config, world_model):\n        super(ImagBehavior, self).__init__()\n        self._use_amp = True if config.precision == 16 else False\n        self._config = config\n        self._world_model = world_model\n        if config.dyn_discrete:\n            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter\n        else:\n            feat_size = config.dyn_stoch + config.dyn_deter\n        self.actor = networks.MLP(\n            feat_size,\n            (config.num_actions,),\n            config.actor[\"layers\"],\n            config.units,\n            config.act,\n            config.norm,\n            config.actor[\"dist\"],\n            config.actor[\"std\"],\n            config.actor[\"min_std\"],\n            config.actor[\"max_std\"],\n            absmax=1.0,\n            temp=config.actor[\"temp\"],\n            unimix_ratio=config.actor[\"unimix_ratio\"],\n            outscale=config.actor[\"outscale\"],\n            name=\"Actor\",\n        )\n        self.value = networks.MLP(\n            feat_size,\n            (255,) if config.critic[\"dist\"] == \"symlog_disc\" else (),\n            config.critic[\"layers\"],\n            config.units,\n            config.act,\n            config.norm,\n            config.critic[\"dist\"],\n            outscale=config.critic[\"outscale\"],\n            device=config.device,\n            name=\"Value\",\n        )\n        if config.critic[\"slow_target\"]:\n            self._slow_value = copy.deepcopy(self.value)\n            self._updates = 0\n        kw = dict(wd=config.weight_decay, opt=config.opt, use_amp=self._use_amp)\n        self._actor_opt = tools.Optimizer(\n            \"actor\",\n            self.actor.parameters(),\n            config.actor[\"lr\"],\n            config.actor[\"eps\"],\n            config.actor[\"grad_clip\"],\n            **kw,\n        )\n        print(\n            f\"Optimizer actor_opt has {sum(param.numel() for param in self.actor.parameters())} variables.\"\n        )\n        self._value_opt = tools.Optimizer(\n            \"value\",\n            self.value.parameters(),\n            config.critic[\"lr\"],\n            config.critic[\"eps\"],\n            config.critic[\"grad_clip\"],\n            **kw,\n        )\n        print(\n            f\"Optimizer value_opt has {sum(param.numel() for param in self.value.parameters())} variables.\"\n        )\n        if self._config.reward_EMA:\n            # register ema_vals to nn.Module for enabling torch.save and torch.load\n            self.register_buffer(\n                \"ema_vals\", torch.zeros((2,), device=self._config.device)\n            )\n            self.reward_ema = RewardEMA(device=self._config.device)\n\n    def _train(\n        self,\n        start,\n        objective,\n    ):\n        self._update_slow_target()\n        metrics = {}\n\n        with tools.RequiresGrad(self.actor):\n            with torch.cuda.amp.autocast(self._use_amp):\n                if self._config.gate_enabled:\n                    imag_feat, imag_state, imag_action, dts = self._imagine(\n                        start, self.actor, self._config.imag_horizon\n                    )\n                else:\n                    imag_feat, imag_state, imag_action = self._imagine(\n                        start, self.actor, self._config.imag_horizon\n                    )\n                    dts = None\n                reward = objective(imag_feat, imag_state, imag_action)\n                actor_ent = self.actor(imag_feat).entropy()\n                state_ent = self._world_model.dynamics.get_dist(imag_state).entropy()\n                # this target is not scaled by ema or sym_log.\n                target, weights, base = self._compute_target(\n                    imag_feat, imag_state, reward, dts=dts\n                )\n                actor_loss, mets = self._compute_actor_loss(\n                    imag_feat,\n                    imag_action,\n                    target,\n                    weights,\n                    base,\n                )\n                actor_loss -= self._config.actor[\"entropy\"] * actor_ent[:-1, ..., None]\n                actor_loss = torch.mean(actor_loss)\n                metrics.update(mets)\n                value_input = imag_feat\n\n        with tools.RequiresGrad(self.value):\n            with torch.cuda.amp.autocast(self._use_amp):\n                value = self.value(value_input[:-1].detach())\n                target = torch.stack(target, dim=1)\n                # (time, batch, 1), (time, batch, 1) -> (time, batch)\n                value_loss = -value.log_prob(target.detach())\n                slow_target = self._slow_value(value_input[:-1].detach())\n                if self._config.critic[\"slow_target\"]:\n                    value_loss -= value.log_prob(slow_target.mode().detach())\n                # (time, batch, 1), (time, batch, 1) -> (1,)\n                value_loss = torch.mean(weights[:-1] * value_loss[:, :, None])\n\n        metrics.update(tools.tensorstats(value.mode(), \"value\"))\n        metrics.update(tools.tensorstats(target, \"target\"))\n        metrics.update(tools.tensorstats(reward, \"imag_reward\"))\n        if self._config.actor[\"dist\"] in [\"onehot\"]:\n            metrics.update(\n                tools.tensorstats(\n                    torch.argmax(imag_action, dim=-1).float(), \"imag_action\"\n                )\n            )\n        else:\n            metrics.update(tools.tensorstats(imag_action, \"imag_action\"))\n        metrics[\"actor_entropy\"] = to_np(torch.mean(actor_ent))\n\n        if self._config.gate_enabled and dts is not None:\n            dts_float = dts.float()\n            metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n            metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n            metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n            metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n            dt_counts = torch.bincount(\n                dts.reshape(-1).long(),\n                minlength=self._config.gate_max_dt + 1,\n            )[1:]\n            dt_dist = dt_counts.float() / dt_counts.sum()\n            for k in range(self._config.gate_max_dt):\n                metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n            emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n            metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n            max_entropy = math.log(self._config.gate_max_dt)\n            metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n\n        with tools.RequiresGrad(self):\n            metrics.update(self._actor_opt(actor_loss, self.actor.parameters()))\n            metrics.update(self._value_opt(value_loss, self.value.parameters()))\n        return imag_feat, imag_state, imag_action, weights, metrics\n\n    def _imagine(self, start, policy, horizon):\n        dynamics = self._world_model.dynamics\n        flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n        start = {k: flatten(v) for k, v in start.items()}\n\n        if self._config.gate_enabled:\n            gate = self._world_model.event_gate\n            config = self._config\n            step = self._world_model.gate_step.item() if hasattr(\n                self._world_model, \"gate_step\"\n            ) else 0\n            gate_active = (\n                gate is not None and step > config.gate_curriculum_phase1\n            )\n\n            def step_fn(prev, _):\n                state, _, _, prev_dt = prev\n                feat = dynamics.get_feat(state)\n                inp = feat.detach()\n                action = policy(inp).sample()\n                succ = dynamics.img_step(state, action, dt=prev_dt)\n                succ_feat = dynamics.get_feat(succ)\n                if gate_active:\n                    _, next_dt, _ = gate(succ_feat.detach(), step, hard=True)\n                else:\n                    batch_size = succ_feat.shape[0]\n                    next_dt = torch.ones(\n                        batch_size, dtype=torch.long, device=succ_feat.device\n                    )\n                return succ, feat, action, next_dt\n\n            init_dt = torch.ones(\n                start[list(start.keys())[0]].shape[0],\n                dtype=torch.long, device=config.device,\n            )\n            succ, feats, actions, dts = tools.static_scan(\n                step_fn, [torch.arange(horizon)],\n                (start, None, None, init_dt),\n            )\n            states = {\n                k: torch.cat([start[k][None], v[:-1]], 0)\n                for k, v in succ.items()\n            }\n            return feats, states, actions, dts\n        else:\n            def step(prev, _):\n                state, _, _ = prev\n                feat = dynamics.get_feat(state)\n                inp = feat.detach()\n                action = policy(inp).sample()\n                succ = dynamics.img_step(state, action)\n                return succ, feat, action\n\n            succ, feats, actions = tools.static_scan(\n                step, [torch.arange(horizon)], (start, None, None)\n            )\n            states = {\n                k: torch.cat([start[k][None], v[:-1]], 0)\n                for k, v in succ.items()\n            }\n            return feats, states, actions\n\n    def _compute_target(self, imag_feat, imag_state, reward, dts=None):\n        if \"cont\" in self._world_model.heads:\n            inp = self._world_model.dynamics.get_feat(imag_state)\n            discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n        else:\n            discount = self._config.discount * torch.ones_like(reward)\n        value = self.value(imag_feat).mode()\n\n        if dts is not None and self._config.gate_enabled:\n            target = tools.lambda_return_variable_dt(\n                reward[1:],\n                value[:-1],\n                discount[1:],\n                dts[1:],\n                bootstrap=value[-1],\n                lambda_=self._config.discount_lambda,\n                axis=0,\n            )\n            pcont_adj = discount ** dts.unsqueeze(-1).float()\n            weights = torch.cumprod(\n                torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n            ).detach()\n        else:\n            target = tools.lambda_return(\n                reward[1:],\n                value[:-1],\n                discount[1:],\n                bootstrap=value[-1],\n                lambda_=self._config.discount_lambda,\n                axis=0,\n            )\n            weights = torch.cumprod(\n                torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n            ).detach()\n        return target, weights, value[:-1]\n\n    def _compute_actor_loss(\n        self,\n        imag_feat,\n        imag_action,\n        target,\n        weights,\n        base,\n    ):\n        metrics = {}\n        inp = imag_feat.detach()\n        policy = self.actor(inp)\n        # Q-val for actor is not transformed using symlog\n        target = torch.stack(target, dim=1)\n        if self._config.reward_EMA:\n            offset, scale = self.reward_ema(target, self.ema_vals)\n            normed_target = (target - offset) / scale\n            normed_base = (base - offset) / scale\n            adv = normed_target - normed_base\n            metrics.update(tools.tensorstats(normed_target, \"normed_target\"))\n            metrics[\"EMA_005\"] = to_np(self.ema_vals[0])\n            metrics[\"EMA_095\"] = to_np(self.ema_vals[1])\n        else:\n            adv = target - base\n\n        if self._config.imag_gradient == \"dynamics\":\n            actor_target = adv\n        elif self._config.imag_gradient == \"reinforce\":\n            actor_target = (\n                policy.log_prob(imag_action)[:-1][:, :, None]\n                * (target - self.value(imag_feat[:-1]).mode()).detach()\n            )\n        elif self._config.imag_gradient == \"both\":\n            actor_target = (\n                policy.log_prob(imag_action)[:-1][:, :, None]\n                * (target - self.value(imag_feat[:-1]).mode()).detach()\n            )\n            mix = self._config.imag_gradient_mix\n            actor_target = mix * target + (1 - mix) * actor_target\n            metrics[\"imag_gradient_mix\"] = mix\n        else:\n            raise NotImplementedError(self._config.imag_gradient)\n        actor_loss = -weights[:-1] * actor_target\n        return actor_loss, metrics\n\n    def _update_slow_target(self):\n        if self._config.critic[\"slow_target\"]:\n            if self._updates % self._config.critic[\"slow_target_update\"] == 0:\n                mix = self._config.critic[\"slow_target_fraction\"]\n                for s, d in zip(self.value.parameters(), self._slow_value.parameters()):\n                    d.data = mix * s.data + (1 - mix) * d.data\n            self._updates += 1\n",
      "numLines": 654,
      "startLine": 1,
      "totalLines": 654
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_012kfeZgewMoioG7XatBP3f8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/tools.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "faa0ec32-0054-4534-9d67-72a944028e1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGvuUf2bFiCqJ6dSCykPiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12473,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12473
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01Pxav7J3cXRL1H9jttTzRei`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/subsample_curriculum_patch.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "6b263e1a-a81b-432a-97e7-d193a2819e67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGvuUf2bFiCqJ6dSCykPiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12473,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12473
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

_source line 13 · 2026-05-13T06:37:10.989Z_

<details><summary>↩ Tool result · `toolu_01Pxav7J3cXRL1H9jttTzRei`</summary>

```text
1	# Subsample Curriculum Patch
2	# -------------------------
3	# Problem: subsample_variable_dt applies variable-dt subsampling in Phase 1
4	# (gate frozen, 0-50K steps), forcing RSSM to train on variable-dt data while
5	# imagination only uses dt=1. This train/imagine mismatch hurts return (~40% of baseline).
6	#
7	# Fix: tie subsampling range to gate_scale curriculum.
8	#   Phase 1 (gate_scale=0):    effective_max_dt=1 -> no subsampling (vanilla DreamerV3)
9	#   Phase 2 (0&lt;gate_scale<1):  effective_max_dt linearly ramps from 1 to K
10	#   Phase 3 (gate_scale=1):    effective_max_dt=K -> full log-uniform subsampling
11	#
12	# Deployment:
13	#   1. Replace subsample_variable_dt in tools.py (around line 763)
14	#   2. Replace the subsample call block in WorldModel._train in models.py (around line 169)
15	
16	import math
17	import torch
18	
19	
20	# =============================================================================
21	# Part 1: Replace tools.subsample_variable_dt (tools.py ~line 763-810)
22	# =============================================================================
23	
24	def subsample_variable_dt(data, max_dt, discount, effective_max_dt=None):
25	    """Variable-dt sub-sampling of replay trajectories.
26	
27	    Samples per-element dt from log-uniform over [1, effective_max_dt].
28	    Computes cumulative discounted reward and minimum continuation for each gap.
29	
30	    Args:
31	        data: dict of tensors, each (B, T, ...).
32	        max_dt: config maximum dt (used as upper bound clamp).
33	        discount: scalar discount factor for cumulative reward.
34	        effective_max_dt: curriculum-controlled max dt.
35	            None or <=1 means no subsampling (pure dt=1, vanilla DreamerV3).
36	    """
37	    B, T = data["action"].shape[:2]
38	    device = data["action"].device
39	
40	    if effective_max_dt is None:
41	        effective_max_dt = max_dt
42	
43	    effective_max_dt = max(1, min(int(round(effective_max_dt)), max_dt))
44	
45	    if effective_max_dt <= 1:
46	        dt_labels = torch.ones(B, T, dtype=torch.long, device=device)
47	        return data, dt_labels
48	
49	    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(effective_max_dt))
50	    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, effective_max_dt)
51	
52	    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()
53	    T_sub = sub_len.max().item()
54	
55	    data_sub = {}
56	    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)
57	    reward_cum = torch.zeros(B, T_sub, *data["reward"].shape[2:], device=device)
58	    cont_min = torch.ones(B, T_sub, *data["cont"].shape[2:], device=device)
59	
60	    for b in range(B):
61	        dt_b = dt_per_elem[b].item()
62	        indices = list(range(0, T, dt_b))
63	        L = len(indices)
64	
65	        for key in data:
66	            if key not in data_sub:
67	                data_sub[key] = torch.zeros(
68	                    B, T_sub, *data[key].shape[2:],
69	                    dtype=data[key].dtype, device=device,
70	                )
71	            data_sub[key][b, :L] = data[key][b, indices]
72	
73	        for i, t_start in enumerate(indices[:-1]):
74	            t_end = min(t_start + dt_b, T)
75	            span = t_end - t_start
76	            gamma_powers = discount ** torch.arange(
77	                span, dtype=torch.float, device=device
78	            )
79	            r_slice = data["reward"][b, t_start:t_end]
80	            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)
81	            cont_min[b, i] = data["cont"][b, t_start:t_end].min(dim=0).values
82	
83	        dt_labels[b, :L] = dt_b
84	
85	    data_sub["reward"] = reward_cum
86	    data_sub["cont"] = cont_min
87	    return data_sub, dt_labels
88	
89	
90	# =============================================================================
91	# Part 2: Replace subsample call in WorldModel._train (models.py ~line 169-173)
92	# =============================================================================
93	# Original code:
94	#
95	#     if self._config.gate_enabled:
96	#         self.gate_step += 1
97	#         data, dt_labels = tools.subsample_variable_dt(
98	#             data, self._config.gate_max_dt, self._config.discount,
99	#         )
100	#     else:
101	#         dt_labels = None
102	#
103	# Replace with:
104	#
105	#     if self._config.gate_enabled:
106	#         self.gate_step += 1
107	#         step = self.gate_step.item()
108	#         if step < self._config.gate_curriculum_phase1:
109	#             gate_scale = 0.0
110	#         elif step < self._config.gate_curriculum_phase2:
111	#             progress = (step - self._config.gate_curriculum_phase1) / (
112	#                 self._config.gate_curriculum_phase2
113	#                 - self._config.gate_curriculum_phase1
114	#             )
115	#             gate_scale = progress
116	#         else:
117	#             gate_scale = 1.0
118	#
119	#         effective_max_dt = 1 + gate_scale * (self._config.gate_max_dt - 1)
120	#         data, dt_labels = tools.subsample_variable_dt(
121	#             data, self._config.gate_max_dt, self._config.discount,
122	#             effective_max_dt=effective_max_dt,
123	#         )
124	#     else:
125	#         dt_labels = None
126	#
127	# NOTE: The gate_scale computation later in _train (around line 242) already
128	# duplicates the same curriculum logic for scaling the gate loss. After this
129	# patch, both blocks use the same gate_scale value. You can optionally refactor
130	# to compute gate_scale once and reuse it, but it is not required — the
131	# duplicated computation is trivially cheap and keeps the patch minimal.
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "dcf4db20-3164-4e4c-8b50-6a9a16c48019",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/subsample_curriculum_patch.py",
      "content": "# Subsample Curriculum Patch\n# -------------------------\n# Problem: subsample_variable_dt applies variable-dt subsampling in Phase 1\n# (gate frozen, 0-50K steps), forcing RSSM to train on variable-dt data while\n# imagination only uses dt=1. This train/imagine mismatch hurts return (~40% of baseline).\n#\n# Fix: tie subsampling range to gate_scale curriculum.\n#   Phase 1 (gate_scale=0):    effective_max_dt=1 -> no subsampling (vanilla DreamerV3)\n#   Phase 2 (0&lt;gate_scale<1):  effective_max_dt linearly ramps from 1 to K\n#   Phase 3 (gate_scale=1):    effective_max_dt=K -> full log-uniform subsampling\n#\n# Deployment:\n#   1. Replace subsample_variable_dt in tools.py (around line 763)\n#   2. Replace the subsample call block in WorldModel._train in models.py (around line 169)\n\nimport math\nimport torch\n\n\n# =============================================================================\n# Part 1: Replace tools.subsample_variable_dt (tools.py ~line 763-810)\n# =============================================================================\n\ndef subsample_variable_dt(data, max_dt, discount, effective_max_dt=None):\n    \"\"\"Variable-dt sub-sampling of replay trajectories.\n\n    Samples per-element dt from log-uniform over [1, effective_max_dt].\n    Computes cumulative discounted reward and minimum continuation for each gap.\n\n    Args:\n        data: dict of tensors, each (B, T, ...).\n        max_dt: config maximum dt (used as upper bound clamp).\n        discount: scalar discount factor for cumulative reward.\n        effective_max_dt: curriculum-controlled max dt.\n            None or <=1 means no subsampling (pure dt=1, vanilla DreamerV3).\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    if effective_max_dt is None:\n        effective_max_dt = max_dt\n\n    effective_max_dt = max(1, min(int(round(effective_max_dt)), max_dt))\n\n    if effective_max_dt <= 1:\n        dt_labels = torch.ones(B, T, dtype=torch.long, device=device)\n        return data, dt_labels\n\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(effective_max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, effective_max_dt)\n\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            span = t_end - t_start\n            gamma_powers = discount ** torch.arange(\n                span, dtype=torch.float, device=device\n            )\n            r_slice = data[\"reward\"][b, t_start:t_end]\n            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n\n\n# =============================================================================\n# Part 2: Replace subsample call in WorldModel._train (models.py ~line 169-173)\n# =============================================================================\n# Original code:\n#\n#     if self._config.gate_enabled:\n#         self.gate_step += 1\n#         data, dt_labels = tools.subsample_variable_dt(\n#             data, self._config.gate_max_dt, self._config.discount,\n#         )\n#     else:\n#         dt_labels = None\n#\n# Replace with:\n#\n#     if self._config.gate_enabled:\n#         self.gate_step += 1\n#         step = self.gate_step.item()\n#         if step < self._config.gate_curriculum_phase1:\n#             gate_scale = 0.0\n#         elif step < self._config.gate_curriculum_phase2:\n#             progress = (step - self._config.gate_curriculum_phase1) / (\n#                 self._config.gate_curriculum_phase2\n#                 - self._config.gate_curriculum_phase1\n#             )\n#             gate_scale = progress\n#         else:\n#             gate_scale = 1.0\n#\n#         effective_max_dt = 1 + gate_scale * (self._config.gate_max_dt - 1)\n#         data, dt_labels = tools.subsample_variable_dt(\n#             data, self._config.gate_max_dt, self._config.discount,\n#             effective_max_dt=effective_max_dt,\n#         )\n#     else:\n#         dt_labels = None\n#\n# NOTE: The gate_scale computation later in _train (around line 242) already\n# duplicates the same curriculum logic for scaling the gate loss. After this\n# patch, both blocks use the same gate_scale value. You can optionally refactor\n# to compute gate_scale once and reuse it, but it is not required — the\n# duplicated computation is trivially cheap and keeps the patch minimal.\n",
      "numLines": 132,
      "startLine": 1,
      "totalLines": 132
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T06:37:11.255Z_

<details><summary>↩ Tool result · `toolu_012kfeZgewMoioG7XatBP3f8`</summary>

```text
1	# Event-Gated Adaptive-Horizon DreamerV3 — Utility Functions
2	# Modified from NM512/dreamerv3-torch.
3	# Changes: added lambda_return_variable_dt and subsample_variable_dt.
4	
5	import datetime
6	import collections
7	import io
8	import os
9	import json
10	import math
11	import pathlib
12	import re
13	import time
14	import random
15	
16	import numpy as np
17	
18	import torch
19	from torch import nn
20	from torch.nn import functional as F
21	from torch import distributions as torchd
22	from torch.utils.tensorboard import SummaryWriter
23	
24	
25	to_np = lambda x: x.detach().cpu().numpy()
26	
27	
28	def symlog(x):
29	    return torch.sign(x) * torch.log(torch.abs(x) + 1.0)
30	
31	
32	def symexp(x):
33	    return torch.sign(x) * (torch.exp(torch.abs(x)) - 1.0)
34	
35	
36	class RequiresGrad:
37	    def __init__(self, model):
38	        self._model = model
39	
40	    def __enter__(self):
41	        self._model.requires_grad_(requires_grad=True)
42	
43	    def __exit__(self, *args):
44	        self._model.requires_grad_(requires_grad=False)
45	
46	
47	class TimeRecording:
48	    def __init__(self, comment):
49	        self._comment = comment
50	
51	    def __enter__(self):
52	        self._st = torch.cuda.Event(enable_timing=True)
53	        self._nd = torch.cuda.Event(enable_timing=True)
54	        self._st.record()
55	
56	    def __exit__(self, *args):
57	        self._nd.record()
58	        torch.cuda.synchronize()
59	        print(self._comment, self._st.elapsed_time(self._nd) / 1000)
60	
61	
62	class Logger:
63	    def __init__(self, logdir, step):
64	        self._logdir = logdir
65	        self._writer = SummaryWriter(log_dir=str(logdir), max_queue=1000)
66	        self._last_step = None
67	        self._last_time = None
68	        self._scalars = {}
69	        self._images = {}
70	        self._videos = {}
71	        self.step = step
72	
73	    def scalar(self, name, value):
74	        self._scalars[name] = float(value)
75	
76	    def image(self, name, value):
77	        self._images[name] = np.array(value)
78	
79	    def video(self, name, value):
80	        self._videos[name] = np.array(value)
81	
82	    def write(self, fps=False, step=False):
83	        if not step:
84	            step = self.step
85	        scalars = list(self._scalars.items())
86	        if fps:
87	            scalars.append(("fps", self._compute_fps(step)))
88	        print(f"[{step}]", " / ".join(f"{k} {v:.1f}" for k, v in scalars))
89	        with (self._logdir / "metrics.jsonl").open("a") as f:
90	            f.write(json.dumps({"step": step, **dict(scalars)}) + "\n")
91	        for name, value in scalars:
92	            if "/" not in name:
93	                self._writer.add_scalar("scalars/" + name, value, step)
94	            else:
95	                self._writer.add_scalar(name, value, step)
96	        for name, value in self._images.items():
97	            self._writer.add_image(name, value, step)
98	        for name, value in self._videos.items():
99	            name = name if isinstance(name, str) else name.decode("utf-8")
100	            if np.issubdtype(value.dtype, np.floating):
101	                value = np.clip(255 * value, 0, 255).astype(np.uint8)
102	            B, T, H, W, C = value.shape
103	            value = value.transpose(1, 4, 2, 0, 3).reshape((1, T, C, H, B * W))
104	            self._writer.add_video(name, value, step, 16)
105	
106	        self._writer.flush()
107	        self._scalars = {}
108	        self._images = {}
109	        self._videos = {}
110	
111	    def _compute_fps(self, step):
112	        if self._last_step is None:
113	            self._last_time = time.time()
114	            self._last_step = step
115	            return 0
116	        steps = step - self._last_step
117	        duration = time.time() - self._last_time
118	        self._last_time += duration
119	        self._last_step = step
120	        return steps / duration
121	
122	    def offline_scalar(self, name, value, step):
123	        self._writer.add_scalar("scalars/" + name, value, step)
124	
125	    def offline_video(self, name, value, step):
126	        if np.issubdtype(value.dtype, np.floating):
127	            value = np.clip(255 * value, 0, 255).astype(np.uint8)
128	        B, T, H, W, C = value.shape
129	        value = value.transpose(1, 4, 2, 0, 3).reshape((1, T, C, H, B * W))
130	        self._writer.add_video(name, value, step, 16)
131	
132	
133	def simulate(
134	    agent,
135	    envs,
136	    cache,
137	    directory,
138	    logger,
139	    is_eval=False,
140	    limit=None,
141	    steps=0,
142	    episodes=0,
143	    state=None,
144	):
145	    # initialize or unpack simulation state
146	    if state is None:
147	        step, episode = 0, 0
148	        done = np.ones(len(envs), bool)
149	        length = np.zeros(len(envs), np.int32)
150	        obs = [None] * len(envs)
151	        agent_state = None
152	        reward = [0] * len(envs)
153	    else:
154	        step, episode, done, length, obs, agent_state, reward = state
155	    while (steps and step < steps) or (episodes and episode < episodes):
156	        # reset envs if necessary
157	        if done.any():
158	            indices = [index for index, d in enumerate(done) if d]
159	            results = [envs[i].reset() for i in indices]
160	            results = [r() for r in results]
161	            for index, result in zip(indices, results):
162	                t = result.copy()
163	                t = {k: convert(v) for k, v in t.items()}
164	                # action will be added to transition in add_to_cache
165	                t["reward"] = 0.0
166	                t["discount"] = 1.0
167	                # initial state should be added to cache
168	                add_to_cache(cache, envs[index].id, t)
169	                # replace obs with done by initial state
170	                obs[index] = result
171	        # step agents
172	        obs = {k: np.stack([o[k] for o in obs]) for k in obs[0] if "log_" not in k}
173	        action, agent_state = agent(obs, done, agent_state)
174	        if isinstance(action, dict):
175	            action = [
176	                {k: np.array(action[k][i].detach().cpu()) for k in action}
177	                for i in range(len(envs))
178	            ]
179	        else:
180	            action = np.array(action)
181	        assert len(action) == len(envs)
182	        # step envs
183	        results = [e.step(a) for e, a in zip(envs, action)]
184	        results = [r() for r in results]
185	        obs, reward, done = zip(*[p[:3] for p in results])
186	        obs = list(obs)
187	        reward = list(reward)
188	        done = np.stack(done)
189	        episode += int(done.sum())
190	        length += 1
191	        step += len(envs)
192	        length *= 1 - done
193	        # add to cache
194	        for a, result, env in zip(action, results, envs):
195	            o, r, d, info = result
196	            o = {k: convert(v) for k, v in o.items()}
197	            transition = o.copy()
198	            if isinstance(a, dict):
199	                transition.update(a)
200	            else:
201	                transition["action"] = a
202	            transition["reward"] = r
203	            transition["discount"] = info.get("discount", np.array(1 - float(d)))
204	            add_to_cache(cache, env.id, transition)
205	
206	        if done.any():
207	            indices = [index for index, d in enumerate(done) if d]
208	            # logging for done episode
209	            for i in indices:
210	                save_episodes(directory, {envs[i].id: cache[envs[i].id]})
211	                length = len(cache[envs[i].id]["reward"]) - 1
212	                score = float(np.array(cache[envs[i].id]["reward"]).sum())
213	                video = cache[envs[i].id]["image"]
214	                # record logs given from environments
215	                for key in list(cache[envs[i].id].keys()):
216	                    if "log_" in key:
217	                        logger.scalar(
218	                            key, float(np.array(cache[envs[i].id][key]).sum())
219	                        )
220	                        # log items won't be used later
221	                        cache[envs[i].id].pop(key)
222	
223	                if not is_eval:
224	                    step_in_dataset = erase_over_episodes(cache, limit)
225	                    logger.scalar(f"dataset_size", step_in_dataset)
226	                    logger.scalar(f"train_return", score)
227	                    logger.scalar(f"train_length", length)
228	                    logger.scalar(f"train_episodes", len(cache))
229	                    logger.write(step=logger.step)
230	                else:
231	                    if not "eval_lengths" in locals():
232	                        eval_lengths = []
233	                        eval_scores = []
234	                        eval_done = False
235	                    # start counting scores for evaluation
236	                    eval_scores.append(score)
237	                    eval_lengths.append(length)
238	
239	                    score = sum(eval_scores) / len(eval_scores)
240	                    length = sum(eval_lengths) / len(eval_lengths)
241	                    logger.video(f"eval_policy", np.array(video)[None])
242	
243	                    if len(eval_scores) >= episodes and not eval_done:
244	                        logger.scalar(f"eval_return", score)
245	                        logger.scalar(f"eval_length", length)
246	                        logger.scalar(f"eval_episodes", len(eval_scores))
247	                        logger.write(step=logger.step)
248	                        eval_done = True
249	    if is_eval:
250	        # keep only last item for saving memory. this cache is used for video_pred later
251	        while len(cache) > 1:
252	            # FIFO
253	            cache.popitem(last=False)
254	    return (step - steps, episode - episodes, done, length, obs, agent_state, reward)
255	
256	
257	def add_to_cache(cache, id, transition):
258	    if id not in cache:
259	        cache[id] = dict()
260	        for key, val in transition.items():
261	            cache[id][key] = [convert(val)]
262	    else:
263	        for key, val in transition.items():
264	            if key not in cache[id]:
265	                # fill missing data(action, etc.) at second time
266	                cache[id][key] = [convert(0 * val)]
267	                cache[id][key].append(convert(val))
268	            else:
269	                cache[id][key].append(convert(val))
270	
271	
272	def erase_over_episodes(cache, dataset_size):
273	    step_in_dataset = 0
274	    for key, ep in reversed(sorted(cache.items(), key=lambda x: x[0])):
275	        if (
276	            not dataset_size
277	            or step_in_dataset + (len(ep["reward"]) - 1) <= dataset_size
278	        ):
279	            step_in_dataset += len(ep["reward"]) - 1
280	        else:
281	            del cache[key]
282	    return step_in_dataset
283	
284	
285	def convert(value, precision=32):
286	    value = np.array(value)
287	    if np.issubdtype(value.dtype, np.floating):
288	        dtype = {16: np.float16, 32: np.float32, 64: np.float64}[precision]
289	    elif np.issubdtype(value.dtype, np.signedinteger):
290	        dtype = {16: np.int16, 32: np.int32, 64: np.int64}[precision]
291	    elif np.issubdtype(value.dtype, np.uint8):
292	        dtype = np.uint8
293	    elif np.issubdtype(value.dtype, bool):
294	        dtype = bool
295	    else:
296	        raise NotImplementedError(value.dtype)
297	    return value.astype(dtype)
298	
299	
300	def save_episodes(directory, episodes):
301	    directory = pathlib.Path(directory).expanduser()
302	    directory.mkdir(parents=True, exist_ok=True)
303	    for filename, episode in episodes.items():
304	        length = len(episode["reward"])
305	        filename = directory / f"{filename}-{length}.npz"
306	        with io.BytesIO() as f1:
307	            np.savez_compressed(f1, **episode)
308	            f1.seek(0)
309	            with filename.open("wb") as f2:
310	                f2.write(f1.read())
311	    return True
312	
313	
314	def from_generator(generator, batch_size):
315	    while True:
316	        batch = []
317	        for _ in range(batch_size):
318	            batch.append(next(generator))
319	        data = {}
320	        for key in batch[0].keys():
321	            data[key] = []
322	            for i in range(batch_size):
323	                data[key].append(batch[i][key])
324	            data[key] = np.stack(data[key], 0)
325	        yield data
326	
327	
328	def sample_episodes(episodes, length, seed=0):
329	    np_random = np.random.RandomState(seed)
330	    while True:
331	        size = 0
332	        ret = None
333	        p = np.array(
334	            [len(next(iter(episode.values()))) for episode in episodes.values()]
335	        )
336	        p = p / np.sum(p)
337	        while size < length:
338	            episode = np_random.choice(list(episodes.values()), p=p)
339	            total = len(next(iter(episode.values())))
340	            # make sure at least one transition included
341	            if total < 2:
342	                continue
343	            if not ret:
344	                index = int(np_random.randint(0, total - 1))
345	                ret = {
346	                    k: v[index : min(index + length, total)].copy()
347	                    for k, v in episode.items()
348	                    if "log_" not in k
349	                }
350	                if "is_first" in ret:
351	                    ret["is_first"][0] = True
352	            else:
353	                # 'is_first' comes after 'is_last'
354	                index = 0
355	                possible = length - size
356	                ret = {
357	                    k: np.append(
358	                        ret[k], v[index : min(index + possible, total)].copy(), axis=0
359	                    )
360	                    for k, v in episode.items()
361	                    if "log_" not in k
362	                }
363	                if "is_first" in ret:
364	                    ret["is_first"][size] = True
365	            size = len(next(iter(ret.values())))
366	        yield ret
367	
368	
369	def load_episodes(directory, limit=None, reverse=True):
370	    directory = pathlib.Path(directory).expanduser()
371	    episodes = collections.OrderedDict()
372	    total = 0
373	    if reverse:
374	        for filename in reversed(sorted(directory.glob("*.npz"))):
375	            try:
376	                with filename.open("rb") as f:
377	                    episode = np.load(f)
378	                    episode = {k: episode[k] for k in episode.keys()}
379	            except Exception as e:
380	                print(f"Could not load episode: {e}")
381	                continue
382	            # extract only filename without extension
383	            episodes[str(os.path.splitext(os.path.basename(filename))[0])] = episode
384	            total += len(episode["reward"]) - 1
385	            if limit and total >= limit:
386	                break
387	    else:
388	        for filename in sorted(directory.glob("*.npz")):
389	            try:
390	                with filename.open("rb") as f:
391	                    episode = np.load(f)
392	                    episode = {k: episode[k] for k in episode.keys()}
393	            except Exception as e:
394	                print(f"Could not load episode: {e}")
395	                continue
396	            episodes[str(filename)] = episode
397	            total += len(episode["reward"]) - 1
398	            if limit and total >= limit:
399	                break
400	    return episodes
401	
402	
403	class SampleDist:
404	    def __init__(self, dist, samples=100):
405	        self._dist = dist
406	        self._samples = samples
407	
408	    @property
409	    def name(self):
410	        return "SampleDist"
411	
412	    def __getattr__(self, name):
413	        return getattr(self._dist, name)
414	
415	    def mean(self):
416	        samples = self._dist.sample(self._samples)
417	        return torch.mean(samples, 0)
418	
419	    def mode(self):
420	        sample = self._dist.sample(self._samples)
421	        logprob = self._dist.log_prob(sample)
422	        return sample[torch.argmax(logprob)][0]
423	
424	    def entropy(self):
425	        sample = self._dist.sample(self._samples)
426	        logprob = self.log_prob(sample)
427	        return -torch.mean(logprob, 0)
428	
429	
430	class OneHotDist(torchd.one_hot_categorical.OneHotCategorical):
431	    def __init__(self, logits=None, probs=None, unimix_ratio=0.0):
432	        if logits is not None and unimix_ratio > 0.0:
433	            probs = F.softmax(logits, dim=-1)
434	            probs = probs * (1.0 - unimix_ratio) + unimix_ratio / probs.shape[-1]
435	            logits = torch.log(probs)
436	            super().__init__(logits=logits, probs=None)
437	        else:
438	            super().__init__(logits=logits, probs=probs)
439	
440	    def mode(self):
441	        _mode = F.one_hot(
442	            torch.argmax(super().logits, axis=-1), super().logits.shape[-1]
443	        )
444	        return _mode.detach() + super().logits - super().logits.detach()
445	
446	    def sample(self, sample_shape=(), seed=None):
447	        if seed is not None:
448	            raise ValueError("need to check")
449	        sample = super().sample(sample_shape).detach()
450	        probs = super().probs
451	        while len(probs.shape) < len(sample.shape):
452	            probs = probs[None]
453	        sample += probs - probs.detach()
454	        return sample
455	
456	
457	class DiscDist:
458	    def __init__(
459	        self,
460	        logits,
461	        low=-20.0,
462	        high=20.0,
463	        transfwd=symlog,
464	        transbwd=symexp,
465	        device="cuda",
466	    ):
467	        self.logits = logits
468	        self.probs = torch.softmax(logits, -1)
469	        self.buckets = torch.linspace(low, high, steps=255, device=device)
470	        self.width = (self.buckets[-1] - self.buckets[0]) / 255
471	        self.transfwd = transfwd
472	        self.transbwd = transbwd
473	
474	    def mean(self):
475	        _mean = self.probs * self.buckets
476	        return self.transbwd(torch.sum(_mean, dim=-1, keepdim=True))
477	
478	    def mode(self):
479	        _mode = self.probs * self.buckets
480	        return self.transbwd(torch.sum(_mode, dim=-1, keepdim=True))
481	
482	    # Inside OneHotCategorical, log_prob is calculated using only max element in targets
483	    def log_prob(self, x):
484	        x = self.transfwd(x)
485	        # x(time, batch, 1)
486	        below = torch.sum((self.buckets <= x[..., None]).to(torch.int32), dim=-1) - 1
487	        above = len(self.buckets) - torch.sum(
488	            (self.buckets > x[..., None]).to(torch.int32), dim=-1
489	        )
490	        # this is implemented using clip at the original repo as the gradients are not backpropagated for the out of limits.
491	        below = torch.clip(below, 0, len(self.buckets) - 1)
492	        above = torch.clip(above, 0, len(self.buckets) - 1)
493	        equal = below == above
494	
495	        dist_to_below = torch.where(equal, 1, torch.abs(self.buckets[below] - x))
496	        dist_to_above = torch.where(equal, 1, torch.abs(self.buckets[above] - x))
497	        total = dist_to_below + dist_to_above
498	        weight_below = dist_to_above / total
499	        weight_above = dist_to_below / total
500	        target = (
501	            F.one_hot(below, num_classes=len(self.buckets)) * weight_below[..., None]
502	            + F.one_hot(above, num_classes=len(self.buckets)) * weight_above[..., None]
503	        )
504	        log_pred = self.logits - torch.logsumexp(self.logits, -1, keepdim=True)
505	        target = target.squeeze(-2)
506	
507	        return (target * log_pred).sum(-1)
508	
509	    def log_prob_target(self, target):
510	        log_pred = super().logits - torch.logsumexp(super().logits, -1, keepdim=True)
511	        return (target * log_pred).sum(-1)
512	
513	
514	class MSEDist:
515	    def __init__(self, mode, agg="sum"):
516	        self._mode = mode
517	        self._agg = agg
518	
519	    def mode(self):
520	        return self._mode
521	
522	    def mean(self):
523	        return self._mode
524	
525	    def log_prob(self, value):
526	        assert self._mode.shape == value.shape, (self._mode.shape, value.shape)
527	        distance = (self._mode - value) ** 2
528	        if self._agg == "mean":
529	            loss = distance.mean(list(range(len(distance.shape)))[2:])
530	        elif self._agg == "sum":
531	            loss = distance.sum(list(range(len(distance.shape)))[2:])
532	        else:
533	            raise NotImplementedError(self._agg)
534	        return -loss
535	
536	
537	class SymlogDist:
538	    def __init__(self, mode, dist="mse", agg="sum", tol=1e-8):
539	        self._mode = mode
540	        self._dist = dist
541	        self._agg = agg
542	        self._tol = tol
543	
544	    def mode(self):
545	        return symexp(self._mode)
546	
547	    def mean(self):
548	        return symexp(self._mode)
549	
550	    def log_prob(self, value):
551	        assert self._mode.shape == value.shape
552	        if self._dist == "mse":
553	            distance = (self._mode - symlog(value)) ** 2.0
554	            distance = torch.where(distance < self._tol, 0, distance)
555	        elif self._dist == "abs":
556	            distance = torch.abs(self._mode - symlog(value))
557	            distance = torch.where(distance < self._tol, 0, distance)
558	        else:
559	            raise NotImplementedError(self._dist)
560	        if self._agg == "mean":
561	            loss = distance.mean(list(range(len(distance.shape)))[2:])
562	        elif self._agg == "sum":
563	            loss = distance.sum(list(range(len(distance.shape)))[2:])
564	        else:
565	            raise NotImplementedError(self._agg)
566	        return -loss
567	
568	
569	class ContDist:
570	    def __init__(self, dist=None, absmax=None):
571	        super().__init__()
572	        self._dist = dist
573	        self.mean = dist.mean
574	        self.absmax = absmax
575	
576	    def __getattr__(self, name):
577	        return getattr(self._dist, name)
578	
579	    def entropy(self):
580	        return self._dist.entropy()
581	
582	    def mode(self):
583	        out = self._dist.mean
584	        if self.absmax is not None:
585	            out *= (self.absmax / torch.clip(torch.abs(out), min=self.absmax)).detach()
586	        return out
587	
588	    def sample(self, sample_shape=()):
589	        out = self._dist.rsample(sample_shape)
590	        if self.absmax is not None:
591	            out *= (self.absmax / torch.clip(torch.abs(out), min=self.absmax)).detach()
592	        return out
593	
594	    def log_prob(self, x):
595	        return self._dist.log_prob(x)
596	
597	
598	class Bernoulli:
599	    def __init__(self, dist=None):
600	        super().__init__()
601	        self._dist = dist
602	        self.mean = dist.mean
603	
604	    def __getattr__(self, name):
605	        return getattr(self._dist, name)
606	
607	    def entropy(self):
608	        return self._dist.entropy()
609	
610	    def mode(self):
611	        _mode = torch.round(self._dist.mean)
612	        return _mode.detach() + self._dist.mean - self._dist.mean.detach()
613	
614	    def sample(self, sample_shape=()):
615	        return self._dist.rsample(sample_shape)
616	
617	    def log_prob(self, x):
618	        _logits = self._dist.base_dist.logits
619	        log_probs0 = -F.softplus(_logits)
620	        log_probs1 = -F.softplus(-_logits)
621	
622	        return torch.sum(log_probs0 * (1 - x) + log_probs1 * x, -1)
623	
624	
625	class UnnormalizedHuber(torchd.normal.Normal):
626	    def __init__(self, loc, scale, threshold=1, **kwargs):
627	        super().__init__(loc, scale, **kwargs)
628	        self._threshold = threshold
629	
630	    def log_prob(self, event):
631	        return -(
632	            torch.sqrt((event - self.mean) ** 2 + self._threshold**2) - self._threshold
633	        )
634	
635	    def mode(self):
636	        return self.mean
637	
638	
639	class SafeTruncatedNormal(torchd.normal.Normal):
640	    def __init__(self, loc, scale, low, high, clip=1e-6, mult=1):
641	        super().__init__(loc, scale)
642	        self._low = low
643	        self._high = high
644	        self._clip = clip
645	        self._mult = mult
646	
647	    def sample(self, sample_shape):
648	        event = super().sample(sample_shape)
649	        if self._clip:
650	            clipped = torch.clip(event, self._low + self._clip, self._high - self._clip)
651	            event = event - event.detach() + clipped.detach()
652	        if self._mult:
653	            event *= self._mult
654	        return event
655	
656	
657	class TanhBijector(torchd.Transform):
658	    def __init__(self, validate_args=False, name="tanh"):
659	        super().__init__()
660	
661	    def _forward(self, x):
662	        return torch.tanh(x)
663	
664	    def _inverse(self, y):
665	        y = torch.where(
666	            (torch.abs(y) <= 1.0), torch.clamp(y, -0.99999997, 0.99999997), y
667	        )
668	        y = torch.atanh(y)
669	        return y
670	
671	    def _forward_log_det_jacobian(self, x):
672	        log2 = torch.math.log(2.0)
673	        return 2.0 * (log2 - x - torch.softplus(-2.0 * x))
674	
675	
676	def static_scan_for_lambda_return(fn, inputs, start):
677	    last = start
678	    indices = range(inputs[0].shape[0])
679	    indices = reversed(indices)
680	    flag = True
681	    for index in indices:
682	        # (inputs, pcont) -> (inputs[index], pcont[index])
683	        inp = lambda x: (_input[x] for _input in inputs)
684	        last = fn(last, *inp(index))
685	        if flag:
686	            outputs = last
687	            flag = False
688	        else:
689	            outputs = torch.cat([outputs, last], dim=-1)
690	    outputs = torch.reshape(outputs, [outputs.shape[0], outputs.shape[1], 1])
691	    outputs = torch.flip(outputs, [1])
692	    outputs = torch.unbind(outputs, dim=0)
693	    return outputs
694	
695	
696	def lambda_return(reward, value, pcont, bootstrap, lambda_, axis):
697	    # Setting lambda=1 gives a discounted Monte Carlo return.
698	    # Setting lambda=0 gives a fixed 1-step return.
699	    # assert reward.shape.ndims == value.shape.ndims, (reward.shape, value.shape)
700	    assert len(reward.shape) == len(value.shape), (reward.shape, value.shape)
701	    if isinstance(pcont, (int, float)):
702	        pcont = pcont * torch.ones_like(reward)
703	    dims = list(range(len(reward.shape)))
704	    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1 :]
705	    if axis != 0:
706	        reward = reward.permute(dims)
707	        value = value.permute(dims)
708	        pcont = pcont.permute(dims)
709	    if bootstrap is None:
710	        bootstrap = torch.zeros_like(value[-1])
711	    next_values = torch.cat([value[1:], bootstrap[None]], 0)
712	    inputs = reward + pcont * next_values * (1 - lambda_)
713	    # returns = static_scan(
714	    #    lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
715	    #    (inputs, pcont), bootstrap, reverse=True)
716	    # reimplement to optimize performance
717	    returns = static_scan_for_lambda_return(
718	        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg, (inputs, pcont), bootstrap
719	    )
720	    if axis != 0:
721	        returns = returns.permute(dims)
722	    return returns
723	
724	
725	def lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):
726	    """Lambda-return with variable temporal strides.
727	
728	    Reward is assumed to be cumulative-discounted (pre-computed during sub-sampling).
729	    Discount is raised to the power of dt: gamma^dt.
730	    """
731	    assert len(reward.shape) == len(value.shape), (reward.shape, value.shape)
732	    if isinstance(pcont, (int, float)):
733	        pcont = pcont * torch.ones_like(reward)
734	    if dt.dim() == 2:
735	        dt = dt.unsqueeze(-1)
736	    dt = dt.float()
737	
738	    dims = list(range(len(reward.shape)))
739	    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]
740	    if axis != 0:
741	        reward = reward.permute(dims)
742	        value = value.permute(dims)
743	        pcont = pcont.permute(dims)
744	        dt = dt.permute(dims)
745	
746	    if bootstrap is None:
747	        bootstrap = torch.zeros_like(value[-1])
748	
749	    pcont_adj = pcont ** dt
750	
751	    next_values = torch.cat([value[1:], bootstrap[None]], 0)
752	    inputs = reward + pcont_adj * next_values * (1 - lambda_)
753	
754	    returns = static_scan_for_lambda_return(
755	        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
756	        (inputs, pcont_adj), bootstrap
757	    )
758	    if axis != 0:
759	        returns = returns.permute(dims)
760	    return returns
761	
762	
763	def subsample_variable_dt(data, max_dt, discount):
764	    """Variable-dt sub-sampling of replay trajectories.
765	
766	    Samples per-element dt from log-uniform over [1, K]. Computes cumulative
767	    discounted reward and minimum continuation for each gap.
768	    """
769	    B, T = data["action"].shape[:2]
770	    device = data["action"].device
771	
772	    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))
773	    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)
774	
775	    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()
776	    T_sub = sub_len.max().item()
777	
778	    data_sub = {}
779	    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)
780	    reward_cum = torch.zeros(B, T_sub, *data["reward"].shape[2:], device=device)
781	    cont_min = torch.ones(B, T_sub, *data["cont"].shape[2:], device=device)
782	
783	    for b in range(B):
784	        dt_b = dt_per_elem[b].item()
785	        indices = list(range(0, T, dt_b))
786	        L = len(indices)
787	
788	        for key in data:
789	            if key not in data_sub:
790	                data_sub[key] = torch.zeros(
791	                    B, T_sub, *data[key].shape[2:],
792	                    dtype=data[key].dtype, device=device,
793	                )
794	            data_sub[key][b, :L] = data[key][b, indices]
795	
796	        for i, t_start in enumerate(indices[:-1]):
797	            t_end = min(t_start + dt_b, T)
798	            span = t_end - t_start
799	            gamma_powers = discount ** torch.arange(
800	                span, dtype=torch.float, device=device
801	            )
802	            r_slice = data["reward"][b, t_start:t_end]
803	            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)
804	            cont_min[b, i] = data["cont"][b, t_start:t_end].min(dim=0).values
805	
806	        dt_labels[b, :L] = dt_b
807	
808	    data_sub["reward"] = reward_cum
809	    data_sub["cont"] = cont_min
810	    return data_sub, dt_labels
811	
812	
813	class Optimizer:
814	    def __init__(
815	        self,
816	        name,
817	        parameters,
818	        lr,
819	        eps=1e-4,
820	        clip=None,
821	        wd=None,
822	        wd_pattern=r".*",
823	        opt="adam",
824	        use_amp=False,
825	    ):
826	        assert 0 <= wd < 1
827	        assert not clip or 1 <= clip
828	        self._name = name
829	        self._parameters = parameters
830	        self._clip = clip
831	        self._wd = wd
832	        self._wd_pattern = wd_pattern
833	        self._opt = {
834	            "adam": lambda: torch.optim.Adam(parameters, lr=lr, eps=eps),
835	            "nadam": lambda: NotImplemented(f"{opt} is not implemented"),
836	            "adamax": lambda: torch.optim.Adamax(parameters, lr=lr, eps=eps),
837	            "sgd": lambda: torch.optim.SGD(parameters, lr=lr),
838	            "momentum": lambda: torch.optim.SGD(parameters, lr=lr, momentum=0.9),
839	        }[opt]()
840	        self._scaler = torch.cuda.amp.GradScaler(enabled=use_amp)
841	
842	    def __call__(self, loss, params, retain_graph=True):
843	        assert len(loss.shape) == 0, loss.shape
844	        metrics = {}
845	        metrics[f"{self._name}_loss"] = loss.detach().cpu().numpy()
846	        self._opt.zero_grad()
847	        self._scaler.scale(loss).backward(retain_graph=retain_graph)
848	        self._scaler.unscale_(self._opt)
849	        # loss.backward(retain_graph=retain_graph)
850	        norm = torch.nn.utils.clip_grad_norm_(params, self._clip)
851	        if self._wd:
852	            self._apply_weight_decay(params)
853	        self._scaler.step(self._opt)
854	        self._scaler.update()
855	        # self._opt.step()
856	        self._opt.zero_grad()
857	        metrics[f"{self._name}_grad_norm"] = to_np(norm)
858	        return metrics
859	
860	    def _apply_weight_decay(self, varibs):
861	        nontrivial = self._wd_pattern != r".*"
862	        if nontrivial:
863	            raise NotImplementedError
864	        for var in varibs:
865	            var.data = (1 - self._wd) * var.data
866	
867	
868	def args_type(default):
869	    def parse_string(x):
870	        if default is None:
871	            return x
872	        if isinstance(default, bool):
873	            return bool(["False", "True"].index(x))
874	        if isinstance(default, int):
875	            return float(x) if ("e" in x or "." in x) else int(x)
876	        if isinstance(default, (list, tuple)):
877	            return tuple(args_type(default[0])(y) for y in x.split(","))
878	        return type(default)(x)
879	
880	    def parse_object(x):
881	        if isinstance(default, (list, tuple)):
882	            return tuple(x)
883	        return x
884	
885	    return lambda x: parse_string(x) if isinstance(x, str) else parse_object(x)
886	
887	
888	def static_scan(fn, inputs, start):
889	    last = start
890	    indices = range(inputs[0].shape[0])
891	    flag = True
892	    for index in indices:
893	        inp = lambda x: (_input[x] for _input in inputs)
894	        last = fn(last, *inp(index))
895	        if flag:
896	            if type(last) == type({}):
897	                outputs = {
898	                    key: value.clone().unsqueeze(0) for key, value in last.items()
899	                }
900	            else:
901	                outputs = []
902	                for _last in last:
903	                    if type(_last) == type({}):
904	                        outputs.append(
905	                            {
906	                                key: value.clone().unsqueeze(0)
907	                                for key, value in _last.items()
908	                            }
909	                        )
910	                    else:
911	                        outputs.append(_last.clone().unsqueeze(0))
912	            flag = False
913	        else:
914	            if type(last) == type({}):
915	                for key in last.keys():
916	                    outputs[key] = torch.cat(
917	                        [outputs[key], last[key].unsqueeze(0)], dim=0
918	                    )
919	            else:
920	                for j in range(len(outputs)):
921	                    if type(last[j]) == type({}):
922	                        for key in last[j].keys():
923	                            outputs[j][key] = torch.cat(
924	                                [outputs[j][key], last[j][key].unsqueeze(0)], dim=0
925	                            )
926	                    else:
927	                        outputs[j] = torch.cat(
928	                            [outputs[j], last[j].unsqueeze(0)], dim=0
929	                        )
930	    if type(last) == type({}):
931	        outputs = [outputs]
932	    return outputs
933	
934	
935	class Every:
936	    def __init__(self, every):
937	        self._every = every
938	        self._last = None
939	
940	    def __call__(self, step):
941	        if not self._every:
942	            return 0
943	        if self._last is None:
944	            self._last = step
945	            return 1
946	        count = int((step - self._last) / self._every)
947	        self._last += self._every * count
948	        return count
949	
950	
951	class Once:
952	    def __init__(self):
953	        self._once = True
954	
955	    def __call__(self):
956	        if self._once:
957	            self._once = False
958	            return True
959	        return False
960	
961	
962	class Until:
963	    def __init__(self, until):
964	        self._until = until
965	
966	    def __call__(self, step):
967	        if not self._until:
968	            return True
969	        return step < self._until
970	
971	
972	def weight_init(m):
973	    if isinstance(m, nn.Linear):
974	        in_num = m.in_features
975	        out_num = m.out_features
976	        denoms = (in_num + out_num) / 2.0
977	        scale = 1.0 / denoms
978	        std = np.sqrt(scale) / 0.87962566103423978
979	        nn.init.trunc_normal_(
980	            m.weight.data, mean=0.0, std=std, a=-2.0 * std, b=2.0 * std
981	        )
982	        if hasattr(m.bias, "data"):
983	            m.bias.data.fill_(0.0)
984	    elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
985	        space = m.kernel_size[0] * m.kernel_size[1]
986	        in_num = space * m.in_channels
987	        out_num = space * m.out_channels
988	        denoms = (in_num + out_num) / 2.0
989	        scale = 1.0 / denoms
990	        std = np.sqrt(scale) / 0.87962566103423978
991	        nn.init.trunc_normal_(
992	            m.weight.data, mean=0.0, std=std, a=-2.0 * std, b=2.0 * std
993	        )
994	        if hasattr(m.bias, "data"):
995	            m.bias.data.fill_(0.0)
996	    elif isinstance(m, nn.LayerNorm):
997	        m.weight.data.fill_(1.0)
998	        if hasattr(m.bias, "data"):
999	            m.bias.data.fill_(0.0)
1000	
1001	
1002	def uniform_weight_init(given_scale):
1003	    def f(m):
1004	        if isinstance(m, nn.Linear):
1005	            in_num = m.in_features
1006	            out_num = m.out_features
1007	            denoms = (in_num + out_num) / 2.0
1008	            scale = given_scale / denoms
1009	            limit = np.sqrt(3 * scale)
1010	            nn.init.uniform_(m.weight.data, a=-limit, b=limit)
1011	            if hasattr(m.bias, "data"):
1012	                m.bias.data.fill_(0.0)
1013	        elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
1014	            space = m.kernel_size[0] * m.kernel_size[1]
1015	            in_num = space * m.in_channels
1016	            out_num = space * m.out_channels
1017	            denoms = (in_num + out_num) / 2.0
1018	            scale = given_scale / denoms
1019	            limit = np.sqrt(3 * scale)
1020	            nn.init.uniform_(m.weight.data, a=-limit, b=limit)
1021	            if hasattr(m.bias, "data"):
1022	                m.bias.data.fill_(0.0)
1023	        elif isinstance(m, nn.LayerNorm):
1024	            m.weight.data.fill_(1.0)
1025	            if hasattr(m.bias, "data"):
1026	                m.bias.data.fill_(0.0)
1027	
1028	    return f
1029	
1030	
1031	def tensorstats(tensor, prefix=None):
1032	    metrics = {
1033	        "mean": to_np(torch.mean(tensor)),
1034	        "std": to_np(torch.std(tensor)),
1035	        "min": to_np(torch.min(tensor)),
1036	        "max": to_np(torch.max(tensor)),
1037	    }
1038	    if prefix:
1039	        metrics = {f"{prefix}_{k}": v for k, v in metrics.items()}
1040	    return metrics
1041	
1042	
1043	def set_seed_everywhere(seed):
1044	    torch.manual_seed(seed)
1045	    if torch.cuda.is_available():
1046	        torch.cuda.manual_seed_all(seed)
1047	    np.random.seed(seed)
1048	    random.seed(seed)
1049	
1050	
1051	def enable_deterministic_run():
1052	    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
1053	    torch.backends.cudnn.benchmark = False
1054	    torch.use_deterministic_algorithms(True)
1055	
1056	
1057	def recursively_collect_optim_state_dict(
1058	    obj, path="", optimizers_state_dicts=None, visited=None
1059	):
1060	    if optimizers_state_dicts is None:
1061	        optimizers_state_dicts = {}
1062	    if visited is None:
1063	        visited = set()
1064	    # avoid cyclic reference
1065	    if id(obj) in visited:
1066	        return optimizers_state_dicts
1067	    else:
1068	        visited.add(id(obj))
1069	    attrs = obj.__dict__
1070	    if isinstance(obj, torch.nn.Module):
1071	        attrs.update(
1072	            {k: attr for k, attr in obj.named_modules() if "." not in k and obj != attr}
1073	        )
1074	    for name, attr in attrs.items():
1075	        new_path = path + "." + name if path else name
1076	        if isinstance(attr, torch.optim.Optimizer):
1077	            optimizers_state_dicts[new_path] = attr.state_dict()
1078	        elif hasattr(attr, "__dict__"):
1079	            optimizers_state_dicts.update(
1080	                recursively_collect_optim_state_dict(
1081	                    attr, new_path, optimizers_state_dicts, visited
1082	                )
1083	            )
1084	    return optimizers_state_dicts
1085	
1086	
1087	def recursively_load_optim_state_dict(obj, optimizers_state_dicts):
1088	    for path, state_dict in optimizers_state_dicts.items():
1089	        keys = path.split(".")
1090	        obj_now = obj
1091	        for key in keys:
1092	            obj_now = getattr(obj_now, key)
1093	        obj_now.load_state_dict(state_dict)
1094	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "f7a6a810-2899-4a49-915c-c56d98a11159",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/tools.py",
      "content": "# Event-Gated Adaptive-Horizon DreamerV3 — Utility Functions\n# Modified from NM512/dreamerv3-torch.\n# Changes: added lambda_return_variable_dt and subsample_variable_dt.\n\nimport datetime\nimport collections\nimport io\nimport os\nimport json\nimport math\nimport pathlib\nimport re\nimport time\nimport random\n\nimport numpy as np\n\nimport torch\nfrom torch import nn\nfrom torch.nn import functional as F\nfrom torch import distributions as torchd\nfrom torch.utils.tensorboard import SummaryWriter\n\n\nto_np = lambda x: x.detach().cpu().numpy()\n\n\ndef symlog(x):\n    return torch.sign(x) * torch.log(torch.abs(x) + 1.0)\n\n\ndef symexp(x):\n    return torch.sign(x) * (torch.exp(torch.abs(x)) - 1.0)\n\n\nclass RequiresGrad:\n    def __init__(self, model):\n        self._model = model\n\n    def __enter__(self):\n        self._model.requires_grad_(requires_grad=True)\n\n    def __exit__(self, *args):\n        self._model.requires_grad_(requires_grad=False)\n\n\nclass TimeRecording:\n    def __init__(self, comment):\n        self._comment = comment\n\n    def __enter__(self):\n        self._st = torch.cuda.Event(enable_timing=True)\n        self._nd = torch.cuda.Event(enable_timing=True)\n        self._st.record()\n\n    def __exit__(self, *args):\n        self._nd.record()\n        torch.cuda.synchronize()\n        print(self._comment, self._st.elapsed_time(self._nd) / 1000)\n\n\nclass Logger:\n    def __init__(self, logdir, step):\n        self._logdir = logdir\n        self._writer = SummaryWriter(log_dir=str(logdir), max_queue=1000)\n        self._last_step = None\n        self._last_time = None\n        self._scalars = {}\n        self._images = {}\n        self._videos = {}\n        self.step = step\n\n    def scalar(self, name, value):\n        self._scalars[name] = float(value)\n\n    def image(self, name, value):\n        self._images[name] = np.array(value)\n\n    def video(self, name, value):\n        self._videos[name] = np.array(value)\n\n    def write(self, fps=False, step=False):\n        if not step:\n            step = self.step\n        scalars = list(self._scalars.items())\n        if fps:\n            scalars.append((\"fps\", self._compute_fps(step)))\n        print(f\"[{step}]\", \" / \".join(f\"{k} {v:.1f}\" for k, v in scalars))\n        with (self._logdir / \"metrics.jsonl\").open(\"a\") as f:\n            f.write(json.dumps({\"step\": step, **dict(scalars)}) + \"\\n\")\n        for name, value in scalars:\n            if \"/\" not in name:\n                self._writer.add_scalar(\"scalars/\" + name, value, step)\n            else:\n                self._writer.add_scalar(name, value, step)\n        for name, value in self._images.items():\n            self._writer.add_image(name, value, step)\n        for name, value in self._videos.items():\n            name = name if isinstance(name, str) else name.decode(\"utf-8\")\n            if np.issubdtype(value.dtype, np.floating):\n                value = np.clip(255 * value, 0, 255).astype(np.uint8)\n            B, T, H, W, C = value.shape\n            value = value.transpose(1, 4, 2, 0, 3).reshape((1, T, C, H, B * W))\n            self._writer.add_video(name, value, step, 16)\n\n        self._writer.flush()\n        self._scalars = {}\n        self._images = {}\n        self._videos = {}\n\n    def _compute_fps(self, step):\n        if self._last_step is None:\n            self._last_time = time.time()\n            self._last_step = step\n            return 0\n        steps = step - self._last_step\n        duration = time.time() - self._last_time\n        self._last_time += duration\n        self._last_step = step\n        return steps / duration\n\n    def offline_scalar(self, name, value, step):\n        self._writer.add_scalar(\"scalars/\" + name, value, step)\n\n    def offline_video(self, name, value, step):\n        if np.issubdtype(value.dtype, np.floating):\n            value = np.clip(255 * value, 0, 255).astype(np.uint8)\n        B, T, H, W, C = value.shape\n        value = value.transpose(1, 4, 2, 0, 3).reshape((1, T, C, H, B * W))\n        self._writer.add_video(name, value, step, 16)\n\n\ndef simulate(\n    agent,\n    envs,\n    cache,\n    directory,\n    logger,\n    is_eval=False,\n    limit=None,\n    steps=0,\n    episodes=0,\n    state=None,\n):\n    # initialize or unpack simulation state\n    if state is None:\n        step, episode = 0, 0\n        done = np.ones(len(envs), bool)\n        length = np.zeros(len(envs), np.int32)\n        obs = [None] * len(envs)\n        agent_state = None\n        reward = [0] * len(envs)\n    else:\n        step, episode, done, length, obs, agent_state, reward = state\n    while (steps and step < steps) or (episodes and episode < episodes):\n        # reset envs if necessary\n        if done.any():\n            indices = [index for index, d in enumerate(done) if d]\n            results = [envs[i].reset() for i in indices]\n            results = [r() for r in results]\n            for index, result in zip(indices, results):\n                t = result.copy()\n                t = {k: convert(v) for k, v in t.items()}\n                # action will be added to transition in add_to_cache\n                t[\"reward\"] = 0.0\n                t[\"discount\"] = 1.0\n                # initial state should be added to cache\n                add_to_cache(cache, envs[index].id, t)\n                # replace obs with done by initial state\n                obs[index] = result\n        # step agents\n        obs = {k: np.stack([o[k] for o in obs]) for k in obs[0] if \"log_\" not in k}\n        action, agent_state = agent(obs, done, agent_state)\n        if isinstance(action, dict):\n            action = [\n                {k: np.array(action[k][i].detach().cpu()) for k in action}\n                for i in range(len(envs))\n            ]\n        else:\n            action = np.array(action)\n        assert len(action) == len(envs)\n        # step envs\n        results = [e.step(a) for e, a in zip(envs, action)]\n        results = [r() for r in results]\n        obs, reward, done = zip(*[p[:3] for p in results])\n        obs = list(obs)\n        reward = list(reward)\n        done = np.stack(done)\n        episode += int(done.sum())\n        length += 1\n        step += len(envs)\n        length *= 1 - done\n        # add to cache\n        for a, result, env in zip(action, results, envs):\n            o, r, d, info = result\n            o = {k: convert(v) for k, v in o.items()}\n            transition = o.copy()\n            if isinstance(a, dict):\n                transition.update(a)\n            else:\n                transition[\"action\"] = a\n            transition[\"reward\"] = r\n            transition[\"discount\"] = info.get(\"discount\", np.array(1 - float(d)))\n            add_to_cache(cache, env.id, transition)\n\n        if done.any():\n            indices = [index for index, d in enumerate(done) if d]\n            # logging for done episode\n            for i in indices:\n                save_episodes(directory, {envs[i].id: cache[envs[i].id]})\n                length = len(cache[envs[i].id][\"reward\"]) - 1\n                score = float(np.array(cache[envs[i].id][\"reward\"]).sum())\n                video = cache[envs[i].id][\"image\"]\n                # record logs given from environments\n                for key in list(cache[envs[i].id].keys()):\n                    if \"log_\" in key:\n                        logger.scalar(\n                            key, float(np.array(cache[envs[i].id][key]).sum())\n                        )\n                        # log items won't be used later\n                        cache[envs[i].id].pop(key)\n\n                if not is_eval:\n                    step_in_dataset = erase_over_episodes(cache, limit)\n                    logger.scalar(f\"dataset_size\", step_in_dataset)\n                    logger.scalar(f\"train_return\", score)\n                    logger.scalar(f\"train_length\", length)\n                    logger.scalar(f\"train_episodes\", len(cache))\n                    logger.write(step=logger.step)\n                else:\n                    if not \"eval_lengths\" in locals():\n                        eval_lengths = []\n                        eval_scores = []\n                        eval_done = False\n                    # start counting scores for evaluation\n                    eval_scores.append(score)\n                    eval_lengths.append(length)\n\n                    score = sum(eval_scores) / len(eval_scores)\n                    length = sum(eval_lengths) / len(eval_lengths)\n                    logger.video(f\"eval_policy\", np.array(video)[None])\n\n                    if len(eval_scores) >= episodes and not eval_done:\n                        logger.scalar(f\"eval_return\", score)\n                        logger.scalar(f\"eval_length\", length)\n                        logger.scalar(f\"eval_episodes\", len(eval_scores))\n                        logger.write(step=logger.step)\n                        eval_done = True\n    if is_eval:\n        # keep only last item for saving memory. this cache is used for video_pred later\n        while len(cache) > 1:\n            # FIFO\n            cache.popitem(last=False)\n    return (step - steps, episode - episodes, done, length, obs, agent_state, reward)\n\n\ndef add_to_cache(cache, id, transition):\n    if id not in cache:\n        cache[id] = dict()\n        for key, val in transition.items():\n            cache[id][key] = [convert(val)]\n    else:\n        for key, val in transition.items():\n            if key not in cache[id]:\n                # fill missing data(action, etc.) at second time\n                cache[id][key] = [convert(0 * val)]\n                cache[id][key].append(convert(val))\n            else:\n                cache[id][key].append(convert(val))\n\n\ndef erase_over_episodes(cache, dataset_size):\n    step_in_dataset = 0\n    for key, ep in reversed(sorted(cache.items(), key=lambda x: x[0])):\n        if (\n            not dataset_size\n            or step_in_dataset + (len(ep[\"reward\"]) - 1) <= dataset_size\n        ):\n            step_in_dataset += len(ep[\"reward\"]) - 1\n        else:\n            del cache[key]\n    return step_in_dataset\n\n\ndef convert(value, precision=32):\n    value = np.array(value)\n    if np.issubdtype(value.dtype, np.floating):\n        dtype = {16: np.float16, 32: np.float32, 64: np.float64}[precision]\n    elif np.issubdtype(value.dtype, np.signedinteger):\n        dtype = {16: np.int16, 32: np.int32, 64: np.int64}[precision]\n    elif np.issubdtype(value.dtype, np.uint8):\n        dtype = np.uint8\n    elif np.issubdtype(value.dtype, bool):\n        dtype = bool\n    else:\n        raise NotImplementedError(value.dtype)\n    return value.astype(dtype)\n\n\ndef save_episodes(directory, episodes):\n    directory = pathlib.Path(directory).expanduser()\n    directory.mkdir(parents=True, exist_ok=True)\n    for filename, episode in episodes.items():\n        length = len(episode[\"reward\"])\n        filename = directory / f\"{filename}-{length}.npz\"\n        with io.BytesIO() as f1:\n            np.savez_compressed(f1, **episode)\n            f1.seek(0)\n            with filename.open(\"wb\") as f2:\n                f2.write(f1.read())\n    return True\n\n\ndef from_generator(generator, batch_size):\n    while True:\n        batch = []\n        for _ in range(batch_size):\n            batch.append(next(generator))\n        data = {}\n        for key in batch[0].keys():\n            data[key] = []\n            for i in range(batch_size):\n                data[key].append(batch[i][key])\n            data[key] = np.stack(data[key], 0)\n        yield data\n\n\ndef sample_episodes(episodes, length, seed=0):\n    np_random = np.random.RandomState(seed)\n    while True:\n        size = 0\n        ret = None\n        p = np.array(\n            [len(next(iter(episode.values()))) for episode in episodes.values()]\n        )\n        p = p / np.sum(p)\n        while size < length:\n            episode = np_random.choice(list(episodes.values()), p=p)\n            total = len(next(iter(episode.values())))\n            # make sure at least one transition included\n            if total < 2:\n                continue\n            if not ret:\n                index = int(np_random.randint(0, total - 1))\n                ret = {\n                    k: v[index : min(index + length, total)].copy()\n                    for k, v in episode.items()\n                    if \"log_\" not in k\n                }\n                if \"is_first\" in ret:\n                    ret[\"is_first\"][0] = True\n            else:\n                # 'is_first' comes after 'is_last'\n                index = 0\n                possible = length - size\n                ret = {\n                    k: np.append(\n                        ret[k], v[index : min(index + possible, total)].copy(), axis=0\n                    )\n                    for k, v in episode.items()\n                    if \"log_\" not in k\n                }\n                if \"is_first\" in ret:\n                    ret[\"is_first\"][size] = True\n            size = len(next(iter(ret.values())))\n        yield ret\n\n\ndef load_episodes(directory, limit=None, reverse=True):\n    directory = pathlib.Path(directory).expanduser()\n    episodes = collections.OrderedDict()\n    total = 0\n    if reverse:\n        for filename in reversed(sorted(directory.glob(\"*.npz\"))):\n            try:\n                with filename.open(\"rb\") as f:\n                    episode = np.load(f)\n                    episode = {k: episode[k] for k in episode.keys()}\n            except Exception as e:\n                print(f\"Could not load episode: {e}\")\n                continue\n            # extract only filename without extension\n            episodes[str(os.path.splitext(os.path.basename(filename))[0])] = episode\n            total += len(episode[\"reward\"]) - 1\n            if limit and total >= limit:\n                break\n    else:\n        for filename in sorted(directory.glob(\"*.npz\")):\n            try:\n                with filename.open(\"rb\") as f:\n                    episode = np.load(f)\n                    episode = {k: episode[k] for k in episode.keys()}\n            except Exception as e:\n                print(f\"Could not load episode: {e}\")\n                continue\n            episodes[str(filename)] = episode\n            total += len(episode[\"reward\"]) - 1\n            if limit and total >= limit:\n                break\n    return episodes\n\n\nclass SampleDist:\n    def __init__(self, dist, samples=100):\n        self._dist = dist\n        self._samples = samples\n\n    @property\n    def name(self):\n        return \"SampleDist\"\n\n    def __getattr__(self, name):\n        return getattr(self._dist, name)\n\n    def mean(self):\n        samples = self._dist.sample(self._samples)\n        return torch.mean(samples, 0)\n\n    def mode(self):\n        sample = self._dist.sample(self._samples)\n        logprob = self._dist.log_prob(sample)\n        return sample[torch.argmax(logprob)][0]\n\n    def entropy(self):\n        sample = self._dist.sample(self._samples)\n        logprob = self.log_prob(sample)\n        return -torch.mean(logprob, 0)\n\n\nclass OneHotDist(torchd.one_hot_categorical.OneHotCategorical):\n    def __init__(self, logits=None, probs=None, unimix_ratio=0.0):\n        if logits is not None and unimix_ratio > 0.0:\n            probs = F.softmax(logits, dim=-1)\n            probs = probs * (1.0 - unimix_ratio) + unimix_ratio / probs.shape[-1]\n            logits = torch.log(probs)\n            super().__init__(logits=logits, probs=None)\n        else:\n            super().__init__(logits=logits, probs=probs)\n\n    def mode(self):\n        _mode = F.one_hot(\n            torch.argmax(super().logits, axis=-1), super().logits.shape[-1]\n        )\n        return _mode.detach() + super().logits - super().logits.detach()\n\n    def sample(self, sample_shape=(), seed=None):\n        if seed is not None:\n            raise ValueError(\"need to check\")\n        sample = super().sample(sample_shape).detach()\n        probs = super().probs\n        while len(probs.shape) < len(sample.shape):\n            probs = probs[None]\n        sample += probs - probs.detach()\n        return sample\n\n\nclass DiscDist:\n    def __init__(\n        self,\n        logits,\n        low=-20.0,\n        high=20.0,\n        transfwd=symlog,\n        transbwd=symexp,\n        device=\"cuda\",\n    ):\n        self.logits = logits\n        self.probs = torch.softmax(logits, -1)\n        self.buckets = torch.linspace(low, high, steps=255, device=device)\n        self.width = (self.buckets[-1] - self.buckets[0]) / 255\n        self.transfwd = transfwd\n        self.transbwd = transbwd\n\n    def mean(self):\n        _mean = self.probs * self.buckets\n        return self.transbwd(torch.sum(_mean, dim=-1, keepdim=True))\n\n    def mode(self):\n        _mode = self.probs * self.buckets\n        return self.transbwd(torch.sum(_mode, dim=-1, keepdim=True))\n\n    # Inside OneHotCategorical, log_prob is calculated using only max element in targets\n    def log_prob(self, x):\n        x = self.transfwd(x)\n        # x(time, batch, 1)\n        below = torch.sum((self.buckets <= x[..., None]).to(torch.int32), dim=-1) - 1\n        above = len(self.buckets) - torch.sum(\n            (self.buckets > x[..., None]).to(torch.int32), dim=-1\n        )\n        # this is implemented using clip at the original repo as the gradients are not backpropagated for the out of limits.\n        below = torch.clip(below, 0, len(self.buckets) - 1)\n        above = torch.clip(above, 0, len(self.buckets) - 1)\n        equal = below == above\n\n        dist_to_below = torch.where(equal, 1, torch.abs(self.buckets[below] - x))\n        dist_to_above = torch.where(equal, 1, torch.abs(self.buckets[above] - x))\n        total = dist_to_below + dist_to_above\n        weight_below = dist_to_above / total\n        weight_above = dist_to_below / total\n        target = (\n            F.one_hot(below, num_classes=len(self.buckets)) * weight_below[..., None]\n            + F.one_hot(above, num_classes=len(self.buckets)) * weight_above[..., None]\n        )\n        log_pred = self.logits - torch.logsumexp(self.logits, -1, keepdim=True)\n        target = target.squeeze(-2)\n\n        return (target * log_pred).sum(-1)\n\n    def log_prob_target(self, target):\n        log_pred = super().logits - torch.logsumexp(super().logits, -1, keepdim=True)\n        return (target * log_pred).sum(-1)\n\n\nclass MSEDist:\n    def __init__(self, mode, agg=\"sum\"):\n        self._mode = mode\n        self._agg = agg\n\n    def mode(self):\n        return self._mode\n\n    def mean(self):\n        return self._mode\n\n    def log_prob(self, value):\n        assert self._mode.shape == value.shape, (self._mode.shape, value.shape)\n        distance = (self._mode - value) ** 2\n        if self._agg == \"mean\":\n            loss = distance.mean(list(range(len(distance.shape)))[2:])\n        elif self._agg == \"sum\":\n            loss = distance.sum(list(range(len(distance.shape)))[2:])\n        else:\n            raise NotImplementedError(self._agg)\n        return -loss\n\n\nclass SymlogDist:\n    def __init__(self, mode, dist=\"mse\", agg=\"sum\", tol=1e-8):\n        self._mode = mode\n        self._dist = dist\n        self._agg = agg\n        self._tol = tol\n\n    def mode(self):\n        return symexp(self._mode)\n\n    def mean(self):\n        return symexp(self._mode)\n\n    def log_prob(self, value):\n        assert self._mode.shape == value.shape\n        if self._dist == \"mse\":\n            distance = (self._mode - symlog(value)) ** 2.0\n            distance = torch.where(distance < self._tol, 0, distance)\n        elif self._dist == \"abs\":\n            distance = torch.abs(self._mode - symlog(value))\n            distance = torch.where(distance < self._tol, 0, distance)\n        else:\n            raise NotImplementedError(self._dist)\n        if self._agg == \"mean\":\n            loss = distance.mean(list(range(len(distance.shape)))[2:])\n        elif self._agg == \"sum\":\n            loss = distance.sum(list(range(len(distance.shape)))[2:])\n        else:\n            raise NotImplementedError(self._agg)\n        return -loss\n\n\nclass ContDist:\n    def __init__(self, dist=None, absmax=None):\n        super().__init__()\n        self._dist = dist\n        self.mean = dist.mean\n        self.absmax = absmax\n\n    def __getattr__(self, name):\n        return getattr(self._dist, name)\n\n    def entropy(self):\n        return self._dist.entropy()\n\n    def mode(self):\n        out = self._dist.mean\n        if self.absmax is not None:\n            out *= (self.absmax / torch.clip(torch.abs(out), min=self.absmax)).detach()\n        return out\n\n    def sample(self, sample_shape=()):\n        out = self._dist.rsample(sample_shape)\n        if self.absmax is not None:\n            out *= (self.absmax / torch.clip(torch.abs(out), min=self.absmax)).detach()\n        return out\n\n    def log_prob(self, x):\n        return self._dist.log_prob(x)\n\n\nclass Bernoulli:\n    def __init__(self, dist=None):\n        super().__init__()\n        self._dist = dist\n        self.mean = dist.mean\n\n    def __getattr__(self, name):\n        return getattr(self._dist, name)\n\n    def entropy(self):\n        return self._dist.entropy()\n\n    def mode(self):\n        _mode = torch.round(self._dist.mean)\n        return _mode.detach() + self._dist.mean - self._dist.mean.detach()\n\n    def sample(self, sample_shape=()):\n        return self._dist.rsample(sample_shape)\n\n    def log_prob(self, x):\n        _logits = self._dist.base_dist.logits\n        log_probs0 = -F.softplus(_logits)\n        log_probs1 = -F.softplus(-_logits)\n\n        return torch.sum(log_probs0 * (1 - x) + log_probs1 * x, -1)\n\n\nclass UnnormalizedHuber(torchd.normal.Normal):\n    def __init__(self, loc, scale, threshold=1, **kwargs):\n        super().__init__(loc, scale, **kwargs)\n        self._threshold = threshold\n\n    def log_prob(self, event):\n        return -(\n            torch.sqrt((event - self.mean) ** 2 + self._threshold**2) - self._threshold\n        )\n\n    def mode(self):\n        return self.mean\n\n\nclass SafeTruncatedNormal(torchd.normal.Normal):\n    def __init__(self, loc, scale, low, high, clip=1e-6, mult=1):\n        super().__init__(loc, scale)\n        self._low = low\n        self._high = high\n        self._clip = clip\n        self._mult = mult\n\n    def sample(self, sample_shape):\n        event = super().sample(sample_shape)\n        if self._clip:\n            clipped = torch.clip(event, self._low + self._clip, self._high - self._clip)\n            event = event - event.detach() + clipped.detach()\n        if self._mult:\n            event *= self._mult\n        return event\n\n\nclass TanhBijector(torchd.Transform):\n    def __init__(self, validate_args=False, name=\"tanh\"):\n        super().__init__()\n\n    def _forward(self, x):\n        return torch.tanh(x)\n\n    def _inverse(self, y):\n        y = torch.where(\n            (torch.abs(y) <= 1.0), torch.clamp(y, -0.99999997, 0.99999997), y\n        )\n        y = torch.atanh(y)\n        return y\n\n    def _forward_log_det_jacobian(self, x):\n        log2 = torch.math.log(2.0)\n        return 2.0 * (log2 - x - torch.softplus(-2.0 * x))\n\n\ndef static_scan_for_lambda_return(fn, inputs, start):\n    last = start\n    indices = range(inputs[0].shape[0])\n    indices = reversed(indices)\n    flag = True\n    for index in indices:\n        # (inputs, pcont) -> (inputs[index], pcont[index])\n        inp = lambda x: (_input[x] for _input in inputs)\n        last = fn(last, *inp(index))\n        if flag:\n            outputs = last\n            flag = False\n        else:\n            outputs = torch.cat([outputs, last], dim=-1)\n    outputs = torch.reshape(outputs, [outputs.shape[0], outputs.shape[1], 1])\n    outputs = torch.flip(outputs, [1])\n    outputs = torch.unbind(outputs, dim=0)\n    return outputs\n\n\ndef lambda_return(reward, value, pcont, bootstrap, lambda_, axis):\n    # Setting lambda=1 gives a discounted Monte Carlo return.\n    # Setting lambda=0 gives a fixed 1-step return.\n    # assert reward.shape.ndims == value.shape.ndims, (reward.shape, value.shape)\n    assert len(reward.shape) == len(value.shape), (reward.shape, value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1 :]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont * next_values * (1 - lambda_)\n    # returns = static_scan(\n    #    lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n    #    (inputs, pcont), bootstrap, reverse=True)\n    # reimplement to optimize performance\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg, (inputs, pcont), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n\n\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"Lambda-return with variable temporal strides.\n\n    Reward is assumed to be cumulative-discounted (pre-computed during sub-sampling).\n    Discount is raised to the power of dt: gamma^dt.\n    \"\"\"\n    assert len(reward.shape) == len(value.shape), (reward.shape, value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n\n\ndef subsample_variable_dt(data, max_dt, discount):\n    \"\"\"Variable-dt sub-sampling of replay trajectories.\n\n    Samples per-element dt from log-uniform over [1, K]. Computes cumulative\n    discounted reward and minimum continuation for each gap.\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)\n\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            span = t_end - t_start\n            gamma_powers = discount ** torch.arange(\n                span, dtype=torch.float, device=device\n            )\n            r_slice = data[\"reward\"][b, t_start:t_end]\n            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n\n\nclass Optimizer:\n    def __init__(\n        self,\n        name,\n        parameters,\n        lr,\n        eps=1e-4,\n        clip=None,\n        wd=None,\n        wd_pattern=r\".*\",\n        opt=\"adam\",\n        use_amp=False,\n    ):\n        assert 0 <= wd < 1\n        assert not clip or 1 <= clip\n        self._name = name\n        self._parameters = parameters\n        self._clip = clip\n        self._wd = wd\n        self._wd_pattern = wd_pattern\n        self._opt = {\n            \"adam\": lambda: torch.optim.Adam(parameters, lr=lr, eps=eps),\n            \"nadam\": lambda: NotImplemented(f\"{opt} is not implemented\"),\n            \"adamax\": lambda: torch.optim.Adamax(parameters, lr=lr, eps=eps),\n            \"sgd\": lambda: torch.optim.SGD(parameters, lr=lr),\n            \"momentum\": lambda: torch.optim.SGD(parameters, lr=lr, momentum=0.9),\n        }[opt]()\n        self._scaler = torch.cuda.amp.GradScaler(enabled=use_amp)\n\n    def __call__(self, loss, params, retain_graph=True):\n        assert len(loss.shape) == 0, loss.shape\n        metrics = {}\n        metrics[f\"{self._name}_loss\"] = loss.detach().cpu().numpy()\n        self._opt.zero_grad()\n        self._scaler.scale(loss).backward(retain_graph=retain_graph)\n        self._scaler.unscale_(self._opt)\n        # loss.backward(retain_graph=retain_graph)\n        norm = torch.nn.utils.clip_grad_norm_(params, self._clip)\n        if self._wd:\n            self._apply_weight_decay(params)\n        self._scaler.step(self._opt)\n        self._scaler.update()\n        # self._opt.step()\n        self._opt.zero_grad()\n        metrics[f\"{self._name}_grad_norm\"] = to_np(norm)\n        return metrics\n\n    def _apply_weight_decay(self, varibs):\n        nontrivial = self._wd_pattern != r\".*\"\n        if nontrivial:\n            raise NotImplementedError\n        for var in varibs:\n            var.data = (1 - self._wd) * var.data\n\n\ndef args_type(default):\n    def parse_string(x):\n        if default is None:\n            return x\n        if isinstance(default, bool):\n            return bool([\"False\", \"True\"].index(x))\n        if isinstance(default, int):\n            return float(x) if (\"e\" in x or \".\" in x) else int(x)\n        if isinstance(default, (list, tuple)):\n            return tuple(args_type(default[0])(y) for y in x.split(\",\"))\n        return type(default)(x)\n\n    def parse_object(x):\n        if isinstance(default, (list, tuple)):\n            return tuple(x)\n        return x\n\n    return lambda x: parse_string(x) if isinstance(x, str) else parse_object(x)\n\n\ndef static_scan(fn, inputs, start):\n    last = start\n    indices = range(inputs[0].shape[0])\n    flag = True\n    for index in indices:\n        inp = lambda x: (_input[x] for _input in inputs)\n        last = fn(last, *inp(index))\n        if flag:\n            if type(last) == type({}):\n                outputs = {\n                    key: value.clone().unsqueeze(0) for key, value in last.items()\n                }\n            else:\n                outputs = []\n                for _last in last:\n                    if type(_last) == type({}):\n                        outputs.append(\n                            {\n                                key: value.clone().unsqueeze(0)\n                                for key, value in _last.items()\n                            }\n                        )\n                    else:\n                        outputs.append(_last.clone().unsqueeze(0))\n            flag = False\n        else:\n            if type(last) == type({}):\n                for key in last.keys():\n                    outputs[key] = torch.cat(\n                        [outputs[key], last[key].unsqueeze(0)], dim=0\n                    )\n            else:\n                for j in range(len(outputs)):\n                    if type(last[j]) == type({}):\n                        for key in last[j].keys():\n                            outputs[j][key] = torch.cat(\n                                [outputs[j][key], last[j][key].unsqueeze(0)], dim=0\n                            )\n                    else:\n                        outputs[j] = torch.cat(\n                            [outputs[j], last[j].unsqueeze(0)], dim=0\n                        )\n    if type(last) == type({}):\n        outputs = [outputs]\n    return outputs\n\n\nclass Every:\n    def __init__(self, every):\n        self._every = every\n        self._last = None\n\n    def __call__(self, step):\n        if not self._every:\n            return 0\n        if self._last is None:\n            self._last = step\n            return 1\n        count = int((step - self._last) / self._every)\n        self._last += self._every * count\n        return count\n\n\nclass Once:\n    def __init__(self):\n        self._once = True\n\n    def __call__(self):\n        if self._once:\n            self._once = False\n            return True\n        return False\n\n\nclass Until:\n    def __init__(self, until):\n        self._until = until\n\n    def __call__(self, step):\n        if not self._until:\n            return True\n        return step < self._until\n\n\ndef weight_init(m):\n    if isinstance(m, nn.Linear):\n        in_num = m.in_features\n        out_num = m.out_features\n        denoms = (in_num + out_num) / 2.0\n        scale = 1.0 / denoms\n        std = np.sqrt(scale) / 0.87962566103423978\n        nn.init.trunc_normal_(\n            m.weight.data, mean=0.0, std=std, a=-2.0 * std, b=2.0 * std\n        )\n        if hasattr(m.bias, \"data\"):\n            m.bias.data.fill_(0.0)\n    elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):\n        space = m.kernel_size[0] * m.kernel_size[1]\n        in_num = space * m.in_channels\n        out_num = space * m.out_channels\n        denoms = (in_num + out_num) / 2.0\n        scale = 1.0 / denoms\n        std = np.sqrt(scale) / 0.87962566103423978\n        nn.init.trunc_normal_(\n            m.weight.data, mean=0.0, std=std, a=-2.0 * std, b=2.0 * std\n        )\n        if hasattr(m.bias, \"data\"):\n            m.bias.data.fill_(0.0)\n    elif isinstance(m, nn.LayerNorm):\n        m.weight.data.fill_(1.0)\n        if hasattr(m.bias, \"data\"):\n            m.bias.data.fill_(0.0)\n\n\ndef uniform_weight_init(given_scale):\n    def f(m):\n        if isinstance(m, nn.Linear):\n            in_num = m.in_features\n            out_num = m.out_features\n            denoms = (in_num + out_num) / 2.0\n            scale = given_scale / denoms\n            limit = np.sqrt(3 * scale)\n            nn.init.uniform_(m.weight.data, a=-limit, b=limit)\n            if hasattr(m.bias, \"data\"):\n                m.bias.data.fill_(0.0)\n        elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):\n            space = m.kernel_size[0] * m.kernel_size[1]\n            in_num = space * m.in_channels\n            out_num = space * m.out_channels\n            denoms = (in_num + out_num) / 2.0\n            scale = given_scale / denoms\n            limit = np.sqrt(3 * scale)\n            nn.init.uniform_(m.weight.data, a=-limit, b=limit)\n            if hasattr(m.bias, \"data\"):\n                m.bias.data.fill_(0.0)\n        elif isinstance(m, nn.LayerNorm):\n            m.weight.data.fill_(1.0)\n            if hasattr(m.bias, \"data\"):\n                m.bias.data.fill_(0.0)\n\n    return f\n\n\ndef tensorstats(tensor, prefix=None):\n    metrics = {\n        \"mean\": to_np(torch.mean(tensor)),\n        \"std\": to_np(torch.std(tensor)),\n        \"min\": to_np(torch.min(tensor)),\n        \"max\": to_np(torch.max(tensor)),\n    }\n    if prefix:\n        metrics = {f\"{prefix}_{k}\": v for k, v in metrics.items()}\n    return metrics\n\n\ndef set_seed_everywhere(seed):\n    torch.manual_seed(seed)\n    if torch.cuda.is_available():\n        torch.cuda.manual_seed_all(seed)\n    np.random.seed(seed)\n    random.seed(seed)\n\n\ndef enable_deterministic_run():\n    os.environ[\"CUBLAS_WORKSPACE_CONFIG\"] = \":4096:8\"\n    torch.backends.cudnn.benchmark = False\n    torch.use_deterministic_algorithms(True)\n\n\ndef recursively_collect_optim_state_dict(\n    obj, path=\"\", optimizers_state_dicts=None, visited=None\n):\n    if optimizers_state_dicts is None:\n        optimizers_state_dicts = {}\n    if visited is None:\n        visited = set()\n    # avoid cyclic reference\n    if id(obj) in visited:\n        return optimizers_state_dicts\n    else:\n        visited.add(id(obj))\n    attrs = obj.__dict__\n    if isinstance(obj, torch.nn.Module):\n        attrs.update(\n            {k: attr for k, attr in obj.named_modules() if \".\" not in k and obj != attr}\n        )\n    for name, attr in attrs.items():\n        new_path = path + \".\" + name if path else name\n        if isinstance(attr, torch.optim.Optimizer):\n            optimizers_state_dicts[new_path] = attr.state_dict()\n        elif hasattr(attr, \"__dict__\"):\n            optimizers_state_dicts.update(\n                recursively_collect_optim_state_dict(\n                    attr, new_path, optimizers_state_dicts, visited\n                )\n            )\n    return optimizers_state_dicts\n\n\ndef recursively_load_optim_state_dict(obj, optimizers_state_dicts):\n    for path, state_dict in optimizers_state_dicts.items():\n        keys = path.split(\".\")\n        obj_now = obj\n        for key in keys:\n            obj_now = getattr(obj_now, key)\n        obj_now.load_state_dict(state_dict)\n",
      "numLines": 1094,
      "startLine": 1,
      "totalLines": 1094
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
Now I have a thorough understanding of the implementation. Let me write the Method section draft based on the design document and actual code. I need to cover:

1. 3.1 Variable-Rate RSSM
2. 3.2 Event Gate
3. 3.3 Adapted λ-Returns
4. 3.4 Gate Collapse Prevention
5. 3.5 Comparison with Related Approaches

Let me write precise, academic-style content with LaTeX formulas that accurately reflect the code implementation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "eb7c6cb5-37c7-4d98-8990-f8500ab70f14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VxBgE7xrV6crsWUZKHm5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 49658,
      "cache_read_input_tokens": 23920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 49658
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

Now I'll check the artifacts directory exists and write the method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "edc25a89-6f4a-4a4e-8b18-3a9264d7e39c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VxBgE7xrV6crsWUZKHm5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 49658,
      "cache_read_input_tokens": 23920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 49658
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

<details open><summary>🔧 Tool call — Bash · `toolu_01GaDYKTi21z8gwfAserCQPQ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "ba35aedf-a680-4e8a-8d9a-15021d2bbe32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VxBgE7xrV6crsWUZKHm5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 49658,
      "cache_read_input_tokens": 23920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 49658
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

_source line 18 · 2026-05-13T06:37:21.539Z_

<details><summary>↩ Tool result · `toolu_01GaDYKTi21z8gwfAserCQPQ`</summary>

```text
_project
code
code_survey_dreamerv3.md
eval_mvp.py
exp_001_baseline
exp_002_event_gated
implementation_design.md
manifest.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "4558379d-2d81-4f79-a1ab-8ef051cb8dc3",
  "tool_use_result": {
    "stdout": "_project\ncode\ncode_survey_dreamerv3.md\neval_mvp.py\nexp_001_baseline\nexp_002_event_gated\nimplementation_design.md\nmanifest.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Write · `toolu_01B7a2tZYMYc7qTHi7vwZAPk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/method_section_draft.md",
  "content": "# 3. Method\n\nWe build on DreamerV3 \\citep{hafner2023dreamerv3}, a model-based reinforcement learning agent that learns a world model in a recurrent latent space (RSSM) and optimizes a policy purely through imagined rollouts. Our key contribution is an **event gate** that selects a per-step temporal stride $\\Delta t \\in \\{1, \\dots, K\\}$, enabling variable-rate imagination. When the latent state changes slowly, the gate skips multiple environment steps in a single model transition; when the state changes rapidly, it falls back to single-step updates. This extends the effective planning horizon without a proportional increase in computation. We describe the five components of our approach below.\n\n## 3.1 Variable-Rate RSSM\n\nThe standard RSSM in DreamerV3 maintains a deterministic recurrent state $h_t$ and a stochastic state $z_t$, updated at every environment step via a GRU cell:\n\n$$h_t = \\text{GRU}(h_{t-1}, [z_{t-1}; a_{t-1}]).$$\n\nWe extend this transition to accept a temporal stride $\\Delta t \\in \\{1, \\dots, K\\}$ that specifies how many environment steps the model traverses in a single recurrence. To inform the GRU of the stride magnitude, we introduce a learned embedding $e: \\{1, \\dots, K\\} \\to \\mathbb{R}^{d_e}$ via a lookup table $\\mathbf{E} \\in \\mathbb{R}^{K \\times d_e}$ (we use $K{=}8$, $d_e{=}32$). The modified transition becomes:\n\n$$h_t = \\text{GRU}\\!\\left(h_{t-1},\\; [z_{t-1};\\; a_{t-1};\\; e(\\Delta t)]\\right).$$\n\nThe GRU input is first projected through a linear layer followed by LayerNorm and SiLU activation before entering the recurrent cell, which absorbs the scale difference introduced by the additional embedding dimension. The stochastic state $z_t$ is then sampled from a categorical distribution (with uniform mixture) parameterized by an MLP applied to $h_t$, exactly as in DreamerV3.\n\nWhen $\\Delta t = 1$, the model reduces to the standard RSSM. The embedding weights are initialized near zero ($\\sigma = 0.01$) so that the initial model behavior is nearly identical to vanilla DreamerV3, ensuring stable early training.\n\n**Training with variable strides.** To teach the RSSM to predict across different temporal strides, we sub-sample replay trajectories at variable $\\Delta t$ during training (Section 3.4). Each sub-sampled trajectory carries per-step $\\Delta t$ labels that are passed through the observation loop to the GRU, allowing the model to learn stride-conditioned dynamics.\n\n## 3.2 Event Gate\n\nThe event gate is a lightweight MLP that examines the current latent state and decides the temporal stride for the next imagination step.\n\n**Architecture.** The gate takes as input the feature vector $f_t = [z_t; h_t] \\in \\mathbb{R}^{d_f}$ (where $d_f = d_z \\cdot C + d_h$; for DreamerV3's default configuration, $d_f = 32 \\times 32 + 512 = 1536$). It consists of two hidden layers of 256 units each, with LayerNorm and SiLU activations, followed by a linear projection to $K$ logits:\n\n$$\\ell_t = W_2\\,\\text{SiLU}\\!\\left(\\text{LN}(W_1\\,f_t)\\right) \\in \\mathbb{R}^K.$$\n\nThe output distribution over strides is obtained via Gumbel-Softmax:\n\n$$\\Delta t \\sim \\text{Gumbel-Softmax}(\\ell_t, \\tau),$$\n\nwhich provides differentiable sampling during training while producing hard (argmax) decisions during imagination. The temperature $\\tau$ is linearly annealed from $\\tau_0 = 5.0$ to $\\tau_{\\min} = 0.5$ over 200K training steps, transitioning from near-uniform exploration to confident stride selection.\n\n**Latent-state delta supervision.** Rather than relying solely on task reward to shape the gate, we provide a direct supervision signal derived from the rate of change in latent space. Let $\\delta_t = \\|f_t - f_{t-1}\\|_2$ be the L2 distance between consecutive feature vectors (with stop-gradient on both $f_t$ and $f_{t-1}$). We normalize $\\delta_t$ to $[0, 1]$ within each batch via min-max scaling and compute a preferred stride:\n\n$$\\Delta t^* = 1 + (K - 1)(1 - \\bar{\\delta}_t),$$\n\nwhere $\\bar{\\delta}_t$ is the normalized delta. Large state changes ($\\bar{\\delta}_t \\to 1$) yield $\\Delta t^* \\to 1$ (fine resolution); small changes ($\\bar{\\delta}_t \\to 0$) yield $\\Delta t^* \\to K$ (skip ahead). The supervision target is a soft categorical distribution formed by a Gaussian kernel centered at $\\Delta t^*$:\n\n$$q_t(k) \\propto \\exp\\!\\left(-\\frac{(k - \\Delta t^*)^2}{2\\sigma^2}\\right), \\quad k = 1, \\dots, K,$$\n\nwith $\\sigma = 1.0$. The gate supervision loss is the cross-entropy between the gate's predicted distribution and this soft target:\n\n$$\\mathcal{L}_{\\text{gate}} = -\\sum_{k=1}^{K} q_t(k) \\log p_{\\theta}(k \\mid f_t),$$\n\nwhere $p_{\\theta}(k \\mid f_t) = \\text{softmax}(\\ell_t)_k$. Crucially, the gate loss does not backpropagate into the RSSM: the input features are detached, so the gate learns to *read* the latent dynamics rather than *shape* them.\n\n## 3.3 Adapted $\\lambda$-Returns\n\nDreamerV3 computes $\\lambda$-returns over imagined trajectories with a fixed per-step discount $\\gamma$. With variable-rate imagination, each step spans $\\Delta t$ environment steps, requiring adaptations to both the reward aggregation and the discount factor.\n\n**Cumulative discounted reward.** When sub-sampling a replay trajectory at stride $\\Delta t$, we pre-compute the cumulative discounted reward for each gap:\n\n$$r_t^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k\\, r_{t+k}.$$\n\nThe reward head is trained to predict $r_t^{\\text{cum}}$ directly (the sub-sampled training data replaces per-step rewards with their cumulative-discounted aggregates), so no approximation is needed at imagination time.\n\n**Minimum continuation.** For the continuation signal across a gap, we take the conservative estimate:\n\n$$c_t^{\\min} = \\min_{k=0,\\dots,\\Delta t - 1} c_{t+k},$$\n\nso that if any frame within the gap is terminal, the entire interval is marked as terminal.\n\n**Variable-stride $\\lambda$-return.** The adapted $\\lambda$-return replaces the fixed discount $\\gamma$ with $\\gamma^{\\Delta t}$:\n\n$$V_t^{\\lambda} = r_t^{\\text{cum}} + \\gamma^{\\Delta t}\\!\\left[(1 - \\lambda)\\,V(s_{t+\\Delta t}) + \\lambda\\, V_{t+\\Delta t}^{\\lambda}\\right],$$\n\nwith the recursion terminating at the bootstrap value $V(s_H)$. This is computed via the same backward scan as the standard $\\lambda$-return, but with per-step adjusted discount $(\\gamma \\cdot c_t)^{\\Delta t}$ in place of $\\gamma \\cdot c_t$. When $\\Delta t = 1$ for all steps, this expression reduces exactly to the standard DreamerV3 $\\lambda$-return.\n\n**Importance weights.** The per-step weights used for the actor and value losses are similarly adjusted:\n\n$$w_t = \\prod_{i=0}^{t-1} (\\gamma \\cdot c_i)^{\\Delta t_i},$$\n\nso that steps further in effective time receive appropriately decayed weight.\n\n## 3.4 Gate Collapse Prevention\n\nA central failure mode is *gate collapse*, where the gate converges to a constant stride (typically $\\Delta t = 1$ or $\\Delta t = K$), eliminating the adaptive benefit. We employ three complementary countermeasures.\n\n**Entropy regularization.** We add an entropy bonus to the gate loss:\n\n$$\\mathcal{L}_{\\text{total}} = \\lambda_g\\,\\mathcal{L}_{\\text{gate}} - \\lambda_H\\,\\mathcal{H}[p_\\theta(\\cdot \\mid f_t)],$$\n\nwhere $\\mathcal{H}$ is the categorical entropy of the gate distribution and $\\lambda_H$ is annealed from 0.1 to 0.01 over 200K steps. The high initial $\\lambda_H$ prevents the gate from committing to a narrow $\\Delta t$ range before the RSSM has learned good multi-stride dynamics.\n\n**Three-phase curriculum.** We introduce the gate gradually:\n\n| Phase | Steps | Behavior |\n|-------|-------|----------|\n| 1 | $0$--$50\\text{K}$ | Gate frozen ($\\Delta t \\equiv 1$); gate loss weight $= 0$ |\n| 2 | $50\\text{K}$--$150\\text{K}$ | Gate loss linearly ramped from 0 to 1; gate active in imagination |\n| 3 | $> 150\\text{K}$ | Full gating; gate scale $= 1.0$ |\n\nPhase 1 allows the RSSM to first learn stable single-step dynamics identical to standard DreamerV3. Phase 2 gradually introduces multi-stride predictions, giving the RSSM time to adapt. Phase 3 permits unconstrained gate optimization.\n\nFormally, the gate scale factor is:\n\n$$\\alpha(s) = \\begin{cases} 0 & s < s_1 \\\\ (s - s_1) / (s_2 - s_1) & s_1 \\leq s < s_2 \\\\ 1 & s \\geq s_2 \\end{cases}$$\n\nwhere $s$ is the training step, $s_1 = 50\\text{K}$, and $s_2 = 150\\text{K}$.\n\n**Synchronized sub-sampling curriculum.** A naive implementation applies full variable-$\\Delta t$ sub-sampling from step 0, forcing the RSSM to train on multi-stride data while imagination only uses $\\Delta t = 1$ during Phase 1. This train--imagination mismatch degrades performance. We resolve it by tying the sub-sampling range to the curriculum schedule:\n\n$$\\Delta t_{\\max}^{\\text{eff}} = 1 + \\alpha(s) \\cdot (K - 1).$$\n\nDuring Phase 1, $\\Delta t_{\\max}^{\\text{eff}} = 1$ and the training data is identical to vanilla DreamerV3 (no sub-sampling). During Phase 2, the maximum stride ramps linearly from 1 to $K$, synchronizing the distribution of $\\Delta t$ in training data with the gate's expanding range in imagination. During Phase 3, the full log-uniform distribution over $\\{1, \\dots, K\\}$ is used.\n\n## 3.5 Comparison with Related Approaches\n\nOur method occupies a distinct point in the design space of temporal abstraction for model-based RL. We highlight the key differences with the most closely related approaches.\n\n**THICK** \\citep{romac2024thick} decomposes planning into a hierarchy of coarse sub-goals and fine-grained actions, with a fixed sub-goal horizon. In contrast, our approach operates within a single-level RSSM and learns a *per-step* temporal stride, avoiding the complexity of hierarchical world models while still achieving variable temporal resolution.\n\n**TAWM** \\citep{freed2024tawm} introduces time-aware world models that condition on a fixed or scheduled $\\Delta t$ to predict future states. Our event gate makes $\\Delta t$ *state-dependent*---the stride is chosen dynamically based on the current latent state rather than being fixed or globally scheduled, enabling the model to allocate temporal resolution where it is most needed within a single trajectory.\n\n**ASI** \\citep{anand2024asi} achieves temporal abstraction through action-space interpolation, blending between high-level actions at different time scales. Our method instead operates entirely in the latent state space: the GRU transitions across multiple environment steps in a single forward pass, providing temporal abstraction at the *dynamics* level rather than the action level.\n\n**LS-Imagine** \\citep{huang2024lsimagine} extends effective planning horizons by early termination of imagination rollouts when the value estimate becomes reliable. Our approach is complementary: rather than truncating rollouts, we *accelerate* them by taking larger temporal strides in predictable regions, covering the same effective time span in fewer imagination steps.\n\n**DyMoDreamer** dynamically selects among multiple world models of different granularities. Our method achieves variable temporal resolution within a *single* model by conditioning the GRU on the stride embedding, avoiding the overhead of maintaining and switching between multiple models.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "ed195db7-54a1-4285-81e0-e8148e76a853",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYV4kXq38KKrFXMEtUvg1Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2241,
      "cache_read_input_tokens": 73578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2241
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

_source line 20 · 2026-05-13T06:38:35.756Z_

<details><summary>↩ Tool result · `toolu_01B7a2tZYMYc7qTHi7vwZAPk`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/method_section_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "e2aefe87-15d8-494b-9b29-51f97dc2e155",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/method_section_draft.md",
    "content": "# 3. Method\n\nWe build on DreamerV3 \\citep{hafner2023dreamerv3}, a model-based reinforcement learning agent that learns a world model in a recurrent latent space (RSSM) and optimizes a policy purely through imagined rollouts. Our key contribution is an **event gate** that selects a per-step temporal stride $\\Delta t \\in \\{1, \\dots, K\\}$, enabling variable-rate imagination. When the latent state changes slowly, the gate skips multiple environment steps in a single model transition; when the state changes rapidly, it falls back to single-step updates. This extends the effective planning horizon without a proportional increase in computation. We describe the five components of our approach below.\n\n## 3.1 Variable-Rate RSSM\n\nThe standard RSSM in DreamerV3 maintains a deterministic recurrent state $h_t$ and a stochastic state $z_t$, updated at every environment step via a GRU cell:\n\n$$h_t = \\text{GRU}(h_{t-1}, [z_{t-1}; a_{t-1}]).$$\n\nWe extend this transition to accept a temporal stride $\\Delta t \\in \\{1, \\dots, K\\}$ that specifies how many environment steps the model traverses in a single recurrence. To inform the GRU of the stride magnitude, we introduce a learned embedding $e: \\{1, \\dots, K\\} \\to \\mathbb{R}^{d_e}$ via a lookup table $\\mathbf{E} \\in \\mathbb{R}^{K \\times d_e}$ (we use $K{=}8$, $d_e{=}32$). The modified transition becomes:\n\n$$h_t = \\text{GRU}\\!\\left(h_{t-1},\\; [z_{t-1};\\; a_{t-1};\\; e(\\Delta t)]\\right).$$\n\nThe GRU input is first projected through a linear layer followed by LayerNorm and SiLU activation before entering the recurrent cell, which absorbs the scale difference introduced by the additional embedding dimension. The stochastic state $z_t$ is then sampled from a categorical distribution (with uniform mixture) parameterized by an MLP applied to $h_t$, exactly as in DreamerV3.\n\nWhen $\\Delta t = 1$, the model reduces to the standard RSSM. The embedding weights are initialized near zero ($\\sigma = 0.01$) so that the initial model behavior is nearly identical to vanilla DreamerV3, ensuring stable early training.\n\n**Training with variable strides.** To teach the RSSM to predict across different temporal strides, we sub-sample replay trajectories at variable $\\Delta t$ during training (Section 3.4). Each sub-sampled trajectory carries per-step $\\Delta t$ labels that are passed through the observation loop to the GRU, allowing the model to learn stride-conditioned dynamics.\n\n## 3.2 Event Gate\n\nThe event gate is a lightweight MLP that examines the current latent state and decides the temporal stride for the next imagination step.\n\n**Architecture.** The gate takes as input the feature vector $f_t = [z_t; h_t] \\in \\mathbb{R}^{d_f}$ (where $d_f = d_z \\cdot C + d_h$; for DreamerV3's default configuration, $d_f = 32 \\times 32 + 512 = 1536$). It consists of two hidden layers of 256 units each, with LayerNorm and SiLU activations, followed by a linear projection to $K$ logits:\n\n$$\\ell_t = W_2\\,\\text{SiLU}\\!\\left(\\text{LN}(W_1\\,f_t)\\right) \\in \\mathbb{R}^K.$$\n\nThe output distribution over strides is obtained via Gumbel-Softmax:\n\n$$\\Delta t \\sim \\text{Gumbel-Softmax}(\\ell_t, \\tau),$$\n\nwhich provides differentiable sampling during training while producing hard (argmax) decisions during imagination. The temperature $\\tau$ is linearly annealed from $\\tau_0 = 5.0$ to $\\tau_{\\min} = 0.5$ over 200K training steps, transitioning from near-uniform exploration to confident stride selection.\n\n**Latent-state delta supervision.** Rather than relying solely on task reward to shape the gate, we provide a direct supervision signal derived from the rate of change in latent space. Let $\\delta_t = \\|f_t - f_{t-1}\\|_2$ be the L2 distance between consecutive feature vectors (with stop-gradient on both $f_t$ and $f_{t-1}$). We normalize $\\delta_t$ to $[0, 1]$ within each batch via min-max scaling and compute a preferred stride:\n\n$$\\Delta t^* = 1 + (K - 1)(1 - \\bar{\\delta}_t),$$\n\nwhere $\\bar{\\delta}_t$ is the normalized delta. Large state changes ($\\bar{\\delta}_t \\to 1$) yield $\\Delta t^* \\to 1$ (fine resolution); small changes ($\\bar{\\delta}_t \\to 0$) yield $\\Delta t^* \\to K$ (skip ahead). The supervision target is a soft categorical distribution formed by a Gaussian kernel centered at $\\Delta t^*$:\n\n$$q_t(k) \\propto \\exp\\!\\left(-\\frac{(k - \\Delta t^*)^2}{2\\sigma^2}\\right), \\quad k = 1, \\dots, K,$$\n\nwith $\\sigma = 1.0$. The gate supervision loss is the cross-entropy between the gate's predicted distribution and this soft target:\n\n$$\\mathcal{L}_{\\text{gate}} = -\\sum_{k=1}^{K} q_t(k) \\log p_{\\theta}(k \\mid f_t),$$\n\nwhere $p_{\\theta}(k \\mid f_t) = \\text{softmax}(\\ell_t)_k$. Crucially, the gate loss does not backpropagate into the RSSM: the input features are detached, so the gate learns to *read* the latent dynamics rather than *shape* them.\n\n## 3.3 Adapted $\\lambda$-Returns\n\nDreamerV3 computes $\\lambda$-returns over imagined trajectories with a fixed per-step discount $\\gamma$. With variable-rate imagination, each step spans $\\Delta t$ environment steps, requiring adaptations to both the reward aggregation and the discount factor.\n\n**Cumulative discounted reward.** When sub-sampling a replay trajectory at stride $\\Delta t$, we pre-compute the cumulative discounted reward for each gap:\n\n$$r_t^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k\\, r_{t+k}.$$\n\nThe reward head is trained to predict $r_t^{\\text{cum}}$ directly (the sub-sampled training data replaces per-step rewards with their cumulative-discounted aggregates), so no approximation is needed at imagination time.\n\n**Minimum continuation.** For the continuation signal across a gap, we take the conservative estimate:\n\n$$c_t^{\\min} = \\min_{k=0,\\dots,\\Delta t - 1} c_{t+k},$$\n\nso that if any frame within the gap is terminal, the entire interval is marked as terminal.\n\n**Variable-stride $\\lambda$-return.** The adapted $\\lambda$-return replaces the fixed discount $\\gamma$ with $\\gamma^{\\Delta t}$:\n\n$$V_t^{\\lambda} = r_t^{\\text{cum}} + \\gamma^{\\Delta t}\\!\\left[(1 - \\lambda)\\,V(s_{t+\\Delta t}) + \\lambda\\, V_{t+\\Delta t}^{\\lambda}\\right],$$\n\nwith the recursion terminating at the bootstrap value $V(s_H)$. This is computed via the same backward scan as the standard $\\lambda$-return, but with per-step adjusted discount $(\\gamma \\cdot c_t)^{\\Delta t}$ in place of $\\gamma \\cdot c_t$. When $\\Delta t = 1$ for all steps, this expression reduces exactly to the standard DreamerV3 $\\lambda$-return.\n\n**Importance weights.** The per-step weights used for the actor and value losses are similarly adjusted:\n\n$$w_t = \\prod_{i=0}^{t-1} (\\gamma \\cdot c_i)^{\\Delta t_i},$$\n\nso that steps further in effective time receive appropriately decayed weight.\n\n## 3.4 Gate Collapse Prevention\n\nA central failure mode is *gate collapse*, where the gate converges to a constant stride (typically $\\Delta t = 1$ or $\\Delta t = K$), eliminating the adaptive benefit. We employ three complementary countermeasures.\n\n**Entropy regularization.** We add an entropy bonus to the gate loss:\n\n$$\\mathcal{L}_{\\text{total}} = \\lambda_g\\,\\mathcal{L}_{\\text{gate}} - \\lambda_H\\,\\mathcal{H}[p_\\theta(\\cdot \\mid f_t)],$$\n\nwhere $\\mathcal{H}$ is the categorical entropy of the gate distribution and $\\lambda_H$ is annealed from 0.1 to 0.01 over 200K steps. The high initial $\\lambda_H$ prevents the gate from committing to a narrow $\\Delta t$ range before the RSSM has learned good multi-stride dynamics.\n\n**Three-phase curriculum.** We introduce the gate gradually:\n\n| Phase | Steps | Behavior |\n|-------|-------|----------|\n| 1 | $0$--$50\\text{K}$ | Gate frozen ($\\Delta t \\equiv 1$); gate loss weight $= 0$ |\n| 2 | $50\\text{K}$--$150\\text{K}$ | Gate loss linearly ramped from 0 to 1; gate active in imagination |\n| 3 | $> 150\\text{K}$ | Full gating; gate scale $= 1.0$ |\n\nPhase 1 allows the RSSM to first learn stable single-step dynamics identical to standard DreamerV3. Phase 2 gradually introduces multi-stride predictions, giving the RSSM time to adapt. Phase 3 permits unconstrained gate optimization.\n\nFormally, the gate scale factor is:\n\n$$\\alpha(s) = \\begin{cases} 0 & s < s_1 \\\\ (s - s_1) / (s_2 - s_1) & s_1 \\leq s < s_2 \\\\ 1 & s \\geq s_2 \\end{cases}$$\n\nwhere $s$ is the training step, $s_1 = 50\\text{K}$, and $s_2 = 150\\text{K}$.\n\n**Synchronized sub-sampling curriculum.** A naive implementation applies full variable-$\\Delta t$ sub-sampling from step 0, forcing the RSSM to train on multi-stride data while imagination only uses $\\Delta t = 1$ during Phase 1. This train--imagination mismatch degrades performance. We resolve it by tying the sub-sampling range to the curriculum schedule:\n\n$$\\Delta t_{\\max}^{\\text{eff}} = 1 + \\alpha(s) \\cdot (K - 1).$$\n\nDuring Phase 1, $\\Delta t_{\\max}^{\\text{eff}} = 1$ and the training data is identical to vanilla DreamerV3 (no sub-sampling). During Phase 2, the maximum stride ramps linearly from 1 to $K$, synchronizing the distribution of $\\Delta t$ in training data with the gate's expanding range in imagination. During Phase 3, the full log-uniform distribution over $\\{1, \\dots, K\\}$ is used.\n\n## 3.5 Comparison with Related Approaches\n\nOur method occupies a distinct point in the design space of temporal abstraction for model-based RL. We highlight the key differences with the most closely related approaches.\n\n**THICK** \\citep{romac2024thick} decomposes planning into a hierarchy of coarse sub-goals and fine-grained actions, with a fixed sub-goal horizon. In contrast, our approach operates within a single-level RSSM and learns a *per-step* temporal stride, avoiding the complexity of hierarchical world models while still achieving variable temporal resolution.\n\n**TAWM** \\citep{freed2024tawm} introduces time-aware world models that condition on a fixed or scheduled $\\Delta t$ to predict future states. Our event gate makes $\\Delta t$ *state-dependent*---the stride is chosen dynamically based on the current latent state rather than being fixed or globally scheduled, enabling the model to allocate temporal resolution where it is most needed within a single trajectory.\n\n**ASI** \\citep{anand2024asi} achieves temporal abstraction through action-space interpolation, blending between high-level actions at different time scales. Our method instead operates entirely in the latent state space: the GRU transitions across multiple environment steps in a single forward pass, providing temporal abstraction at the *dynamics* level rather than the action level.\n\n**LS-Imagine** \\citep{huang2024lsimagine} extends effective planning horizons by early termination of imagination rollouts when the value estimate becomes reliable. Our approach is complementary: rather than truncating rollouts, we *accelerate* them by taking larger temporal strides in predictable regions, covering the same effective time span in fewer imagination steps.\n\n**DyMoDreamer** dynamically selects among multiple world models of different granularities. Our method achieves variable temporal resolution within a *single* model by conditioning the GRU on the stride embedding, avoiding the overhead of maintaining and switching between multiple models.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 21_

Method section 初稿已写入 `artifacts/method_section_draft.md`。包含 5 个小节，所有公式基于实际代码实现，符号统一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "uuid": "602e67b8-aa64-4088-8de7-41033a3ffc29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQVCpzwuLNn7vdnQCRSpAR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3514,
      "cache_read_input_tokens": 75819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3514
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

_source line 22_

Method section 初稿已写入 `artifacts/method_section_draft.md`。包含 5 个小节，所有公式基于实际代码实现，符号统一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 95223,
  "duration_api_ms": 95820,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "4d5d466b-d3af-4f48-ac36-ebd1d9d221c3",
  "total_cost_usd": 0.6324835,
  "usage": {
    "input_tokens": 1935,
    "cache_creation_input_tokens": 67886,
    "cache_read_input_tokens": 184764,
    "output_tokens": 4166,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 67886,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 52,
        "cache_read_input_tokens": 75819,
        "cache_creation_input_tokens": 3514,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3514
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1919,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001989,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1935,
      "outputTokens": 4166,
      "cacheReadInputTokens": 184764,
      "cacheCreationInputTokens": 67886,
      "webSearchRequests": 0,
      "costUSD": 0.6304945,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ea97f20c-98e9-4b16-8db2-9ff01f426715"
}
```

</details>

---
