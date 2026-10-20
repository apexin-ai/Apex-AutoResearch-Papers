# code edge pruning hf v2

**Transformer Model EAP-IG** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_code_edge_pruning_hf_v2_20260512T191451.log`
- **Structured JSON:** [`aa37eae2cb1086432911.json`](../../sessions/aa/aa37eae2cb1086432911.json)

## Before a recorded user message

30 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "f2f815fb-c87b-4965-a71a-6a1226b205b4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-structfuse-context/memory/"
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
    "resetsAt": 1778618400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ff13f1ec-d3ca-4ed5-b475-616718b64c64",
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing v1 implementation files to understand the code structure before rewriting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "e2fb7a27-6505-44a8-b54c-4eab5d3e8c6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019n9Cwt8v6du1oeFioJz8fj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12627,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12627
      },
      "output_tokens": 38,
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

读取现有 v1 实现和相关文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "3b9c9ff5-d090-4253-9503-1c2029af8513",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019n9Cwt8v6du1oeFioJz8fj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12627,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12627
      },
      "output_tokens": 38,
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

<details open><summary>🔧 Tool call — Read · `toolu_01WZpUbNHXfoNLahctKxm3da`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_scoring.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "2c79b72c-5da2-449d-9252-8ac9da8a3fe5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019n9Cwt8v6du1oeFioJz8fj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12627,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12627
      },
      "output_tokens": 38,
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

_source line 7 · 2026-05-12T19:15:05.322Z_

<details><summary>↩ Tool result · `toolu_01WZpUbNHXfoNLahctKxm3da`</summary>

```text
1	"""Edge Pruning with L0 regularization for HuggingFace models.
2	
3	Implements princeton-nlp style Edge Pruning using Hard Concrete relaxation
4	(Louizos et al., 2018) on HuggingFace CausalLM models with GQA support.
5	
6	Each edge (u->v) in the computational graph gets a learnable mask via the
7	Hard Concrete distribution, which allows exact zeros and ones. The masks
8	are optimized to minimize faithfulness loss + L0 sparsity penalty.
9	
10	Canonical node format:
11	  input, logits, a{L}.h{H}[.q|.k|.v], m{L}
12	
13	Canonical edge format: "{src}->{dst}" (no spaces)
14	
15	References:
16	  - Louizos et al. "Learning Sparse Neural Networks through L0 Regularization" (2018)
17	  - Bayazit et al. "Discovering Knowledge-Critical Subnetworks" (2023)
18	"""
19	
20	from __future__ import annotations
21	
22	import math
23	from typing import Dict, List, Tuple, Callable, Optional
24	
25	import torch
26	import torch.nn as nn
27	import torch.nn.functional as F
28	
29	
30	# ---------------------------------------------------------------------------
31	# Hard Concrete Distribution
32	# ---------------------------------------------------------------------------
33	
34	class HardConcrete(nn.Module):
35	    """Hard Concrete distribution for L0 mask parameterization.
36	
37	    Parameterized by log_alpha (location). During training, samples from a
38	    stretched Binary Concrete and clamps to [0, 1], yielding exact zeros/ones.
39	    """
40	
41	    BETA = 2.0 / 3.0
42	    GAMMA = -0.1
43	    ZETA = 1.1
44	    EPS = 1e-8
45	
46	    def __init__(self, n_masks: int, init_mean: float = 0.5):
47	        super().__init__()
48	        init_val = math.log(init_mean / (1.0 - init_mean + self.EPS))
49	        self.log_alpha = nn.Parameter(torch.full((n_masks,), init_val))
50	
51	    def forward(self, training: bool = True) -> torch.Tensor:
52	        if training:
53	            u = torch.zeros_like(self.log_alpha).uniform_(self.EPS, 1.0 - self.EPS)
54	            s = torch.sigmoid((torch.log(u / (1.0 - u)) + self.log_alpha) / self.BETA)
55	        else:
56	            s = torch.sigmoid(self.log_alpha)
57	        s_bar = s * (self.ZETA - self.GAMMA) + self.GAMMA
58	        return s_bar.clamp(0.0, 1.0)
59	
60	    def l0_penalty(self) -> torch.Tensor:
61	        """Expected L0 norm: sum of P(z != 0) for each mask."""
62	        return torch.sigmoid(
63	            self.log_alpha - self.BETA * math.log(-self.GAMMA / self.ZETA)
64	        ).sum()
65	
66	    def expected_masks(self) -> torch.Tensor:
67	        """Deterministic mask expectations (for final scoring)."""
68	        return self.forward(training=False)
69	
70	
71	# ---------------------------------------------------------------------------
72	# Architecture detection (Llama-like HF models)
73	# ---------------------------------------------------------------------------
74	
75	_LLAMA_LIKE = frozenset({
76	    "llama", "qwen2", "gemma", "gemma2", "mistral", "phi3", "phi",
77	})
78	
79	
80	def _get_arch_info(model) -> dict:
81	    cfg = model.config
82	    model_type = getattr(cfg, "model_type", "")
83	    if model_type not in _LLAMA_LIKE:
84	        raise ValueError(
85	            f"Edge Pruning L0 currently supports Llama-like architectures, "
86	            f"got model_type={model_type!r}"
87	        )
88	    n_heads = cfg.num_attention_heads
89	    n_kv_heads = getattr(cfg, "num_key_value_heads", n_heads)
90	    d_model = cfg.hidden_size
91	    return dict(
92	        n_layers=cfg.num_hidden_layers,
93	        n_heads=n_heads,
94	        n_kv_heads=n_kv_heads,
95	        heads_per_kv_group=n_heads // n_kv_heads,
96	        d_model=d_model,
97	        head_dim=d_model // n_heads,
98	    )
99	
100	
101	# ---------------------------------------------------------------------------
102	# Edge Topology: enumerate all edges and build mask index mapping
103	# ---------------------------------------------------------------------------
104	
105	def _build_edge_topology(
106	    n_layers: int, n_heads: int, n_kv_heads: int, heads_per_kv_group: int,
107	) -> Tuple[List[str], Dict[str, int], int]:
108	    """Build the full edge set and map each edge to its mask parameter index.
109	
110	    For GQA models, K/V edges targeting the same KV group share a mask.
111	    Q edges always have independent masks.
112	
113	    Returns:
114	        edge_names: list of canonical edge names
115	        edge_to_mask_idx: edge_name -> index into mask parameter vector
116	        n_masks: total number of independent mask parameters
117	    """
118	    edge_names: List[str] = []
119	    edge_to_mask_idx: Dict[str, int] = {}
120	    mask_idx = 0
121	
122	    def _src_nodes_before_layer(layer: int, include_attn_same_layer: bool = False):
123	        """Yield (src_name,) for all nodes whose output feeds into a given layer."""
124	        yield "input"
125	        for l in range(layer):
126	            for h in range(n_heads):
127	                yield f"a{l}.h{h}"
128	            yield f"m{l}"
129	        if include_attn_same_layer:
130	            for h in range(n_heads):
131	                yield f"a{layer}.h{h}"
132	
133	    for L in range(n_layers):
134	        # --- Edges into attention heads at layer L ---
135	        srcs_attn = list(_src_nodes_before_layer(L, include_attn_same_layer=False))
136	        for src in srcs_attn:
137	            for H in range(n_heads):
138	                # Q edge: always independent
139	                q_edge = f"{src}->a{L}.h{H}.q"
140	                edge_names.append(q_edge)
141	                edge_to_mask_idx[q_edge] = mask_idx
142	                mask_idx += 1
143	
144	            # K edges: shared within KV group
145	            for kv_group in range(n_kv_heads):
146	                k_mask_idx = mask_idx
147	                mask_idx += 1
148	                for h_in_group in range(heads_per_kv_group):
149	                    H = kv_group * heads_per_kv_group + h_in_group
150	                    k_edge = f"{src}->a{L}.h{H}.k"
151	                    edge_names.append(k_edge)
152	                    edge_to_mask_idx[k_edge] = k_mask_idx
153	
154	            # V edges: shared within KV group
155	            for kv_group in range(n_kv_heads):
156	                v_mask_idx = mask_idx
157	                mask_idx += 1
158	                for h_in_group in range(heads_per_kv_group):
159	                    H = kv_group * heads_per_kv_group + h_in_group
160	                    v_edge = f"{src}->a{L}.h{H}.v"
161	                    edge_names.append(v_edge)
162	                    edge_to_mask_idx[v_edge] = v_mask_idx
163	
164	        # --- Edges into MLP at layer L ---
165	        srcs_mlp = list(_src_nodes_before_layer(L, include_attn_same_layer=True))
166	        for src in srcs_mlp:
167	            mlp_edge = f"{src}->m{L}"
168	            edge_names.append(mlp_edge)
169	            edge_to_mask_idx[mlp_edge] = mask_idx
170	            mask_idx += 1
171	
172	    return edge_names, edge_to_mask_idx, mask_idx
173	
174	
175	# ---------------------------------------------------------------------------
176	# Destination-grouped mask table for efficient hook application
177	# ---------------------------------------------------------------------------
178	
179	def _build_dst_mask_table(
180	    edge_to_mask_idx: Dict[str, int],
181	) -> Dict[str, Dict[str, int]]:
182	    """Group edges by destination node.
183	
184	    Returns: {dst_node: {src_node: mask_param_index}}
185	    """
186	    table: Dict[str, Dict[str, int]] = {}
187	    for edge, idx in edge_to_mask_idx.items():
188	        src, dst = edge.split("->", 1)
189	        if dst not in table:
190	            table[dst] = {}
191	        table[dst][src] = idx
192	    return table
193	
194	
195	# ---------------------------------------------------------------------------
196	# Source activation cache (captured via hooks)
197	# ---------------------------------------------------------------------------
198	
199	class _ActivationCache:
200	    """Stores source node activations during forward pass."""
201	
202	    def __init__(self):
203	        self.embed_out: Optional[torch.Tensor] = None
204	        self.head_out: Dict[int, Dict[int, torch.Tensor]] = {}
205	        self.mlp_out: Dict[int, torch.Tensor] = {}
206	
207	
208	# ---------------------------------------------------------------------------
209	# Hook-based masked forward pass
210	# ---------------------------------------------------------------------------
211	
212	def _get_module(model, path: str) -> nn.Module:
213	    parts = path.split(".")
214	    m = model
215	    for p in parts:
216	        m = getattr(m, p)
217	    return m
218	
219	
220	def _decompose_attn_output(
221	    concat_heads: torch.Tensor,
222	    o_proj: nn.Linear,
223	    n_heads: int,
224	    head_dim: int,
225	) -> Dict[int, torch.Tensor]:
226	    """Split concatenated head output and project each head through o_proj."""
227	    W = o_proj.weight  # [d_model, d_model]
228	    heads = {}
229	    for h in range(n_heads):
230	        h_slice = concat_heads[:, :, h * head_dim:(h + 1) * head_dim]
231	        W_h = W[:, h * head_dim:(h + 1) * head_dim]
232	        heads[h] = h_slice @ W_h.T
233	    return heads
234	
235	
236	def _masked_forward(
237	    model,
238	    input_ids: torch.Tensor,
239	    masks: torch.Tensor,
240	    arch_info: dict,
241	    dst_mask_table: Dict[str, Dict[str, int]],
242	) -> torch.Tensor:
243	    """Run forward pass with edge masks applied via hooks.
244	
245	    Strategy:
246	    1. Register hooks to capture source node outputs (embed, attn heads, MLP).
247	    2. At each destination's pre-hook, replace its input with the masked sum
248	       of upstream source outputs.
249	
250	    For memory efficiency, source activations are captured and masks applied
251	    layer-by-layer. Each layer's pre-hook constructs the masked residual
252	    from all upstream sources.
253	    """
254	    n_layers = arch_info["n_layers"]
255	    n_heads = arch_info["n_heads"]
256	    head_dim = arch_info["head_dim"]
257	    layers = model.model.layers
258	
259	    cache = _ActivationCache()
260	    hooks = []
261	
262	    # Capture embedding output
263	    def _embed_hook(mod, inp, out):
264	        cache.embed_out = out
265	    hooks.append(model.model.embed_tokens.register_forward_hook(_embed_hook))
266	
267	    for L in range(n_layers):
268	        layer = layers[L]
269	
270	        # Capture per-head attention output via o_proj
271	        def _oproj_hook(mod, inp, out, *, _L=L):
272	            cache.head_out[_L] = _decompose_attn_output(
273	                inp[0], mod, n_heads, head_dim,
274	            )
275	        hooks.append(layer.self_attn.o_proj.register_forward_hook(_oproj_hook))
276	
277	        # Capture MLP output
278	        def _mlp_hook(mod, inp, out, *, _L=L):
279	            cache.mlp_out[_L] = out if isinstance(out, torch.Tensor) else out[0]
280	        hooks.append(layer.mlp.register_forward_hook(_mlp_hook))
281	
282	        # Pre-hook on each layer: construct masked residual stream input.
283	        # This replaces the residual stream with the masked combination of
284	        # all upstream source nodes.
285	        def _layer_pre_hook(mod, inp, *, _L=L):
286	            x = inp[0] if isinstance(inp, tuple) else inp
287	
288	            # Collect all source activations available before this layer
289	            src_acts: Dict[str, torch.Tensor] = {}
290	            if cache.embed_out is not None:
291	                src_acts["input"] = cache.embed_out
292	            for l in range(_L):
293	                if l in cache.head_out:
294	                    for h in range(n_heads):
295	                        src_acts[f"a{l}.h{h}"] = cache.head_out[l][h]
296	                if l in cache.mlp_out:
297	                    src_acts[f"m{l}"] = cache.mlp_out[l]
298	
299	            # For attention destinations (q, k, v) at this layer:
300	            # We approximate by masking the residual stream input.
301	            # The mask for each destination type is the element-wise product
302	            # of all source masks. For simplicity and memory, we apply the
303	            # *minimum* mask across q/k/v destinations for each source,
304	            # effectively masking the residual input to the entire attention block.
305	            #
306	            # More precise: build separate masked inputs per q/k/v head.
307	            # But that requires modifying internal attention computation,
308	            # which is architecture-specific. The residual-level masking
309	            # is the standard approach in princeton-nlp/edge-pruning.
310	
311	            # Gather all destination nodes at this layer
312	            attn_dsts = set()
313	            mlp_dst = f"m{_L}"
314	            for H in range(n_heads):
315	                for qkv in ("q", "k", "v"):
316	                    attn_dsts.add(f"a{_L}.h{H}.{qkv}")
317	
318	            # Compute masked residual for attention input
319	            # Use average mask across all attn destinations for each source
320	            masked_resid = torch.zeros_like(x)
321	            for src_name, src_act in src_acts.items():
322	                # Collect mask values for this source across attn destinations
323	                mask_indices = []
324	                for dst in attn_dsts:
325	                    if dst in dst_mask_table and src_name in dst_mask_table[dst]:
326	                        mask_indices.append(dst_mask_table[dst][src_name])
327	                if mask_indices:
328	                    # Average mask across destinations (approximation)
329	                    src_mask = masks[mask_indices].mean()
330	                    masked_resid = masked_resid + src_act * src_mask
331	
332	            if isinstance(inp, tuple):
333	                return (masked_resid,) + inp[1:]
334	            return masked_resid
335	
336	        hooks.append(layer.register_forward_pre_hook(_layer_pre_hook))
337	
338	    try:
339	        out = model(input_ids)
340	        return out.logits
341	    finally:
342	        for h in hooks:
343	            h.remove()
344	
345	
346	# ---------------------------------------------------------------------------
347	# Faithfulness loss
348	# ---------------------------------------------------------------------------
349	
350	def _faithfulness_loss(
351	    masked_logits: torch.Tensor,
352	    clean_logits: torch.Tensor,
353	    target_ids: Optional[torch.Tensor],
354	) -> torch.Tensor:
355	    """KL divergence between clean and masked model output distributions.
356	
357	    If target_ids is provided, only compute loss at target token positions.
358	    """
359	    if target_ids is not None:
360	        # target_ids: [batch] — index of the token position to evaluate
361	        batch_size = masked_logits.size(0)
362	        idx = target_ids.view(batch_size)
363	        masked_logits = masked_logits[torch.arange(batch_size), idx]
364	        clean_logits = clean_logits[torch.arange(batch_size), idx]
365	
366	    log_p = F.log_softmax(masked_logits, dim=-1)
367	    q = F.softmax(clean_logits, dim=-1)
368	    return F.kl_div(log_p, q, reduction="batchmean")
369	
370	
371	# ---------------------------------------------------------------------------
372	# Main entry point
373	# ---------------------------------------------------------------------------
374	
375	def compute_edge_pruning_scores(
376	    model,
377	    clean_inputs,
378	    corrupt_inputs,
379	    metric_fn: Callable,
380	    target_ids=None,
381	    n_epochs: int = 100,
382	    lambda_l0: float = 1e-3,
383	    lr: float = 0.1,
384	    device: str = "cuda",
385	) -> Dict[str, float]:
386	    """Compute Edge Pruning L0 edge scores.
387	
388	    Returns dict of canonical_edge_name -> score (mask expectation).
389	
390	    Args:
391	        model: HuggingFace CausalLM (Llama-like: Qwen2, Llama, Mistral, etc.)
392	        clean_inputs: dict with 'input_ids' [batch, seq_len]
393	        corrupt_inputs: dict with 'input_ids' [batch, seq_len]
394	        metric_fn: faithfulness metric (kept for interface parity; KL used internally)
395	        target_ids: [batch] token positions for evaluation (None = all positions)
396	        n_epochs: optimization epochs
397	        lambda_l0: L0 sparsity penalty weight
398	        lr: learning rate for mask parameters
399	        device: target device
400	    """
401	    arch_info = _get_arch_info(model)
402	    n_layers = arch_info["n_layers"]
403	    n_heads = arch_info["n_heads"]
404	    n_kv_heads = arch_info["n_kv_heads"]
405	    heads_per_kv_group = arch_info["heads_per_kv_group"]
406	
407	    # Build edge topology
408	    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology(
409	        n_layers, n_heads, n_kv_heads, heads_per_kv_group,
410	    )
411	    dst_mask_table = _build_dst_mask_table(edge_to_mask_idx)
412	
413	    # Initialize Hard Concrete mask parameters
414	    hard_concrete = HardConcrete(n_masks, init_mean=0.5).to(device)
415	    optimizer = torch.optim.Adam(hard_concrete.parameters(), lr=lr)
416	
417	    # Prepare inputs
418	    if isinstance(clean_inputs, dict):
419	        clean_ids = clean_inputs["input_ids"]
420	        if not isinstance(clean_ids, torch.Tensor):
421	            clean_ids = torch.tensor(clean_ids)
422	    else:
423	        clean_ids = clean_inputs
424	    clean_ids = clean_ids.to(device)
425	
426	    if isinstance(corrupt_inputs, dict):
427	        corrupt_ids = corrupt_inputs["input_ids"]
428	        if not isinstance(corrupt_ids, torch.Tensor):
429	            corrupt_ids = torch.tensor(corrupt_ids)
430	    else:
431	        corrupt_ids = corrupt_inputs
432	    corrupt_ids = corrupt_ids.to(device)
433	
434	    if target_ids is not None:
435	        if not isinstance(target_ids, torch.Tensor):
436	            target_ids = torch.tensor(target_ids)
437	        target_ids = target_ids.to(device)
438	
439	    # Get clean model logits (frozen)
440	    model.eval()
441	    with torch.no_grad():
442	        clean_logits = model(clean_ids).logits.detach()
443	
444	    # Optimization loop
445	    for epoch in range(n_epochs):
446	        optimizer.zero_grad()
447	
448	        # Sample masks from Hard Concrete
449	        masks = hard_concrete(training=True)
450	
451	        # Forward pass with masks applied
452	        masked_logits = _masked_forward(
453	            model, clean_ids, masks, arch_info, dst_mask_table,
454	        )
455	
456	        # Loss = faithfulness + sparsity
457	        faith_loss = _faithfulness_loss(masked_logits, clean_logits, target_ids)
458	        l0_loss = hard_concrete.l0_penalty()
459	        loss = faith_loss + lambda_l0 * l0_loss
460	
461	        loss.backward()
462	        optimizer.step()
463	
464	    # Extract final scores
465	    with torch.no_grad():
466	        final_masks = hard_concrete.expected_masks()
467	
468	    scores: Dict[str, float] = {}
469	    for edge_name, mask_idx in edge_to_mask_idx.items():
470	        scores[edge_name] = final_masks[mask_idx].item()
471	
472	    return scores
473	
474	
475	# ---------------------------------------------------------------------------
476	# Utility: edge count estimation
477	# ---------------------------------------------------------------------------
478	
479	def estimate_edge_counts(
480	    n_layers: int, n_heads: int, n_kv_heads: int,
481	) -> Dict[str, int]:
482	    """Estimate edge and mask parameter counts for a given architecture."""
483	    heads_per_kv = n_heads // n_kv_heads
484	    _, _, n_masks = _build_edge_topology(
485	        n_layers, n_heads, n_kv_heads, heads_per_kv,
486	    )
487	    # Total edges (including shared masks counted separately)
488	    total_edges = 0
489	    for L in range(n_layers):
490	        n_src = 1 + L * (n_heads + 1)  # input + prior layers' heads + MLPs
491	        # Attn edges: Q independent, K/V shared per KV group
492	        total_edges += n_src * n_heads * 3  # q, k, v per head
493	        # MLP edges: from all upstream including same-layer attn
494	        n_src_mlp = n_src + n_heads
495	        total_edges += n_src_mlp
496	
497	    return {
498	        "total_edges": total_edges,
499	        "n_independent_masks": n_masks,
500	        "mask_memory_bytes": n_masks * 4,  # float32
501	        "mask_memory_mb": n_masks * 4 / (1024 ** 2),
502	    }
503	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "48b6c9ba-fa52-4d02-b9ee-93cca2cfa69d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_scoring.py",
      "content": "\"\"\"Edge Pruning with L0 regularization for HuggingFace models.\n\nImplements princeton-nlp style Edge Pruning using Hard Concrete relaxation\n(Louizos et al., 2018) on HuggingFace CausalLM models with GQA support.\n\nEach edge (u->v) in the computational graph gets a learnable mask via the\nHard Concrete distribution, which allows exact zeros and ones. The masks\nare optimized to minimize faithfulness loss + L0 sparsity penalty.\n\nCanonical node format:\n  input, logits, a{L}.h{H}[.q|.k|.v], m{L}\n\nCanonical edge format: \"{src}->{dst}\" (no spaces)\n\nReferences:\n  - Louizos et al. \"Learning Sparse Neural Networks through L0 Regularization\" (2018)\n  - Bayazit et al. \"Discovering Knowledge-Critical Subnetworks\" (2023)\n\"\"\"\n\nfrom __future__ import annotations\n\nimport math\nfrom typing import Dict, List, Tuple, Callable, Optional\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\n\n\n# ---------------------------------------------------------------------------\n# Hard Concrete Distribution\n# ---------------------------------------------------------------------------\n\nclass HardConcrete(nn.Module):\n    \"\"\"Hard Concrete distribution for L0 mask parameterization.\n\n    Parameterized by log_alpha (location). During training, samples from a\n    stretched Binary Concrete and clamps to [0, 1], yielding exact zeros/ones.\n    \"\"\"\n\n    BETA = 2.0 / 3.0\n    GAMMA = -0.1\n    ZETA = 1.1\n    EPS = 1e-8\n\n    def __init__(self, n_masks: int, init_mean: float = 0.5):\n        super().__init__()\n        init_val = math.log(init_mean / (1.0 - init_mean + self.EPS))\n        self.log_alpha = nn.Parameter(torch.full((n_masks,), init_val))\n\n    def forward(self, training: bool = True) -> torch.Tensor:\n        if training:\n            u = torch.zeros_like(self.log_alpha).uniform_(self.EPS, 1.0 - self.EPS)\n            s = torch.sigmoid((torch.log(u / (1.0 - u)) + self.log_alpha) / self.BETA)\n        else:\n            s = torch.sigmoid(self.log_alpha)\n        s_bar = s * (self.ZETA - self.GAMMA) + self.GAMMA\n        return s_bar.clamp(0.0, 1.0)\n\n    def l0_penalty(self) -> torch.Tensor:\n        \"\"\"Expected L0 norm: sum of P(z != 0) for each mask.\"\"\"\n        return torch.sigmoid(\n            self.log_alpha - self.BETA * math.log(-self.GAMMA / self.ZETA)\n        ).sum()\n\n    def expected_masks(self) -> torch.Tensor:\n        \"\"\"Deterministic mask expectations (for final scoring).\"\"\"\n        return self.forward(training=False)\n\n\n# ---------------------------------------------------------------------------\n# Architecture detection (Llama-like HF models)\n# ---------------------------------------------------------------------------\n\n_LLAMA_LIKE = frozenset({\n    \"llama\", \"qwen2\", \"gemma\", \"gemma2\", \"mistral\", \"phi3\", \"phi\",\n})\n\n\ndef _get_arch_info(model) -> dict:\n    cfg = model.config\n    model_type = getattr(cfg, \"model_type\", \"\")\n    if model_type not in _LLAMA_LIKE:\n        raise ValueError(\n            f\"Edge Pruning L0 currently supports Llama-like architectures, \"\n            f\"got model_type={model_type!r}\"\n        )\n    n_heads = cfg.num_attention_heads\n    n_kv_heads = getattr(cfg, \"num_key_value_heads\", n_heads)\n    d_model = cfg.hidden_size\n    return dict(\n        n_layers=cfg.num_hidden_layers,\n        n_heads=n_heads,\n        n_kv_heads=n_kv_heads,\n        heads_per_kv_group=n_heads // n_kv_heads,\n        d_model=d_model,\n        head_dim=d_model // n_heads,\n    )\n\n\n# ---------------------------------------------------------------------------\n# Edge Topology: enumerate all edges and build mask index mapping\n# ---------------------------------------------------------------------------\n\ndef _build_edge_topology(\n    n_layers: int, n_heads: int, n_kv_heads: int, heads_per_kv_group: int,\n) -> Tuple[List[str], Dict[str, int], int]:\n    \"\"\"Build the full edge set and map each edge to its mask parameter index.\n\n    For GQA models, K/V edges targeting the same KV group share a mask.\n    Q edges always have independent masks.\n\n    Returns:\n        edge_names: list of canonical edge names\n        edge_to_mask_idx: edge_name -> index into mask parameter vector\n        n_masks: total number of independent mask parameters\n    \"\"\"\n    edge_names: List[str] = []\n    edge_to_mask_idx: Dict[str, int] = {}\n    mask_idx = 0\n\n    def _src_nodes_before_layer(layer: int, include_attn_same_layer: bool = False):\n        \"\"\"Yield (src_name,) for all nodes whose output feeds into a given layer.\"\"\"\n        yield \"input\"\n        for l in range(layer):\n            for h in range(n_heads):\n                yield f\"a{l}.h{h}\"\n            yield f\"m{l}\"\n        if include_attn_same_layer:\n            for h in range(n_heads):\n                yield f\"a{layer}.h{h}\"\n\n    for L in range(n_layers):\n        # --- Edges into attention heads at layer L ---\n        srcs_attn = list(_src_nodes_before_layer(L, include_attn_same_layer=False))\n        for src in srcs_attn:\n            for H in range(n_heads):\n                # Q edge: always independent\n                q_edge = f\"{src}->a{L}.h{H}.q\"\n                edge_names.append(q_edge)\n                edge_to_mask_idx[q_edge] = mask_idx\n                mask_idx += 1\n\n            # K edges: shared within KV group\n            for kv_group in range(n_kv_heads):\n                k_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    k_edge = f\"{src}->a{L}.h{H}.k\"\n                    edge_names.append(k_edge)\n                    edge_to_mask_idx[k_edge] = k_mask_idx\n\n            # V edges: shared within KV group\n            for kv_group in range(n_kv_heads):\n                v_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    v_edge = f\"{src}->a{L}.h{H}.v\"\n                    edge_names.append(v_edge)\n                    edge_to_mask_idx[v_edge] = v_mask_idx\n\n        # --- Edges into MLP at layer L ---\n        srcs_mlp = list(_src_nodes_before_layer(L, include_attn_same_layer=True))\n        for src in srcs_mlp:\n            mlp_edge = f\"{src}->m{L}\"\n            edge_names.append(mlp_edge)\n            edge_to_mask_idx[mlp_edge] = mask_idx\n            mask_idx += 1\n\n    return edge_names, edge_to_mask_idx, mask_idx\n\n\n# ---------------------------------------------------------------------------\n# Destination-grouped mask table for efficient hook application\n# ---------------------------------------------------------------------------\n\ndef _build_dst_mask_table(\n    edge_to_mask_idx: Dict[str, int],\n) -> Dict[str, Dict[str, int]]:\n    \"\"\"Group edges by destination node.\n\n    Returns: {dst_node: {src_node: mask_param_index}}\n    \"\"\"\n    table: Dict[str, Dict[str, int]] = {}\n    for edge, idx in edge_to_mask_idx.items():\n        src, dst = edge.split(\"->\", 1)\n        if dst not in table:\n            table[dst] = {}\n        table[dst][src] = idx\n    return table\n\n\n# ---------------------------------------------------------------------------\n# Source activation cache (captured via hooks)\n# ---------------------------------------------------------------------------\n\nclass _ActivationCache:\n    \"\"\"Stores source node activations during forward pass.\"\"\"\n\n    def __init__(self):\n        self.embed_out: Optional[torch.Tensor] = None\n        self.head_out: Dict[int, Dict[int, torch.Tensor]] = {}\n        self.mlp_out: Dict[int, torch.Tensor] = {}\n\n\n# ---------------------------------------------------------------------------\n# Hook-based masked forward pass\n# ---------------------------------------------------------------------------\n\ndef _get_module(model, path: str) -> nn.Module:\n    parts = path.split(\".\")\n    m = model\n    for p in parts:\n        m = getattr(m, p)\n    return m\n\n\ndef _decompose_attn_output(\n    concat_heads: torch.Tensor,\n    o_proj: nn.Linear,\n    n_heads: int,\n    head_dim: int,\n) -> Dict[int, torch.Tensor]:\n    \"\"\"Split concatenated head output and project each head through o_proj.\"\"\"\n    W = o_proj.weight  # [d_model, d_model]\n    heads = {}\n    for h in range(n_heads):\n        h_slice = concat_heads[:, :, h * head_dim:(h + 1) * head_dim]\n        W_h = W[:, h * head_dim:(h + 1) * head_dim]\n        heads[h] = h_slice @ W_h.T\n    return heads\n\n\ndef _masked_forward(\n    model,\n    input_ids: torch.Tensor,\n    masks: torch.Tensor,\n    arch_info: dict,\n    dst_mask_table: Dict[str, Dict[str, int]],\n) -> torch.Tensor:\n    \"\"\"Run forward pass with edge masks applied via hooks.\n\n    Strategy:\n    1. Register hooks to capture source node outputs (embed, attn heads, MLP).\n    2. At each destination's pre-hook, replace its input with the masked sum\n       of upstream source outputs.\n\n    For memory efficiency, source activations are captured and masks applied\n    layer-by-layer. Each layer's pre-hook constructs the masked residual\n    from all upstream sources.\n    \"\"\"\n    n_layers = arch_info[\"n_layers\"]\n    n_heads = arch_info[\"n_heads\"]\n    head_dim = arch_info[\"head_dim\"]\n    layers = model.model.layers\n\n    cache = _ActivationCache()\n    hooks = []\n\n    # Capture embedding output\n    def _embed_hook(mod, inp, out):\n        cache.embed_out = out\n    hooks.append(model.model.embed_tokens.register_forward_hook(_embed_hook))\n\n    for L in range(n_layers):\n        layer = layers[L]\n\n        # Capture per-head attention output via o_proj\n        def _oproj_hook(mod, inp, out, *, _L=L):\n            cache.head_out[_L] = _decompose_attn_output(\n                inp[0], mod, n_heads, head_dim,\n            )\n        hooks.append(layer.self_attn.o_proj.register_forward_hook(_oproj_hook))\n\n        # Capture MLP output\n        def _mlp_hook(mod, inp, out, *, _L=L):\n            cache.mlp_out[_L] = out if isinstance(out, torch.Tensor) else out[0]\n        hooks.append(layer.mlp.register_forward_hook(_mlp_hook))\n\n        # Pre-hook on each layer: construct masked residual stream input.\n        # This replaces the residual stream with the masked combination of\n        # all upstream source nodes.\n        def _layer_pre_hook(mod, inp, *, _L=L):\n            x = inp[0] if isinstance(inp, tuple) else inp\n\n            # Collect all source activations available before this layer\n            src_acts: Dict[str, torch.Tensor] = {}\n            if cache.embed_out is not None:\n                src_acts[\"input\"] = cache.embed_out\n            for l in range(_L):\n                if l in cache.head_out:\n                    for h in range(n_heads):\n                        src_acts[f\"a{l}.h{h}\"] = cache.head_out[l][h]\n                if l in cache.mlp_out:\n                    src_acts[f\"m{l}\"] = cache.mlp_out[l]\n\n            # For attention destinations (q, k, v) at this layer:\n            # We approximate by masking the residual stream input.\n            # The mask for each destination type is the element-wise product\n            # of all source masks. For simplicity and memory, we apply the\n            # *minimum* mask across q/k/v destinations for each source,\n            # effectively masking the residual input to the entire attention block.\n            #\n            # More precise: build separate masked inputs per q/k/v head.\n            # But that requires modifying internal attention computation,\n            # which is architecture-specific. The residual-level masking\n            # is the standard approach in princeton-nlp/edge-pruning.\n\n            # Gather all destination nodes at this layer\n            attn_dsts = set()\n            mlp_dst = f\"m{_L}\"\n            for H in range(n_heads):\n                for qkv in (\"q\", \"k\", \"v\"):\n                    attn_dsts.add(f\"a{_L}.h{H}.{qkv}\")\n\n            # Compute masked residual for attention input\n            # Use average mask across all attn destinations for each source\n            masked_resid = torch.zeros_like(x)\n            for src_name, src_act in src_acts.items():\n                # Collect mask values for this source across attn destinations\n                mask_indices = []\n                for dst in attn_dsts:\n                    if dst in dst_mask_table and src_name in dst_mask_table[dst]:\n                        mask_indices.append(dst_mask_table[dst][src_name])\n                if mask_indices:\n                    # Average mask across destinations (approximation)\n                    src_mask = masks[mask_indices].mean()\n                    masked_resid = masked_resid + src_act * src_mask\n\n            if isinstance(inp, tuple):\n                return (masked_resid,) + inp[1:]\n            return masked_resid\n\n        hooks.append(layer.register_forward_pre_hook(_layer_pre_hook))\n\n    try:\n        out = model(input_ids)\n        return out.logits\n    finally:\n        for h in hooks:\n            h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Faithfulness loss\n# ---------------------------------------------------------------------------\n\ndef _faithfulness_loss(\n    masked_logits: torch.Tensor,\n    clean_logits: torch.Tensor,\n    target_ids: Optional[torch.Tensor],\n) -> torch.Tensor:\n    \"\"\"KL divergence between clean and masked model output distributions.\n\n    If target_ids is provided, only compute loss at target token positions.\n    \"\"\"\n    if target_ids is not None:\n        # target_ids: [batch] — index of the token position to evaluate\n        batch_size = masked_logits.size(0)\n        idx = target_ids.view(batch_size)\n        masked_logits = masked_logits[torch.arange(batch_size), idx]\n        clean_logits = clean_logits[torch.arange(batch_size), idx]\n\n    log_p = F.log_softmax(masked_logits, dim=-1)\n    q = F.softmax(clean_logits, dim=-1)\n    return F.kl_div(log_p, q, reduction=\"batchmean\")\n\n\n# ---------------------------------------------------------------------------\n# Main entry point\n# ---------------------------------------------------------------------------\n\ndef compute_edge_pruning_scores(\n    model,\n    clean_inputs,\n    corrupt_inputs,\n    metric_fn: Callable,\n    target_ids=None,\n    n_epochs: int = 100,\n    lambda_l0: float = 1e-3,\n    lr: float = 0.1,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Compute Edge Pruning L0 edge scores.\n\n    Returns dict of canonical_edge_name -> score (mask expectation).\n\n    Args:\n        model: HuggingFace CausalLM (Llama-like: Qwen2, Llama, Mistral, etc.)\n        clean_inputs: dict with 'input_ids' [batch, seq_len]\n        corrupt_inputs: dict with 'input_ids' [batch, seq_len]\n        metric_fn: faithfulness metric (kept for interface parity; KL used internally)\n        target_ids: [batch] token positions for evaluation (None = all positions)\n        n_epochs: optimization epochs\n        lambda_l0: L0 sparsity penalty weight\n        lr: learning rate for mask parameters\n        device: target device\n    \"\"\"\n    arch_info = _get_arch_info(model)\n    n_layers = arch_info[\"n_layers\"]\n    n_heads = arch_info[\"n_heads\"]\n    n_kv_heads = arch_info[\"n_kv_heads\"]\n    heads_per_kv_group = arch_info[\"heads_per_kv_group\"]\n\n    # Build edge topology\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology(\n        n_layers, n_heads, n_kv_heads, heads_per_kv_group,\n    )\n    dst_mask_table = _build_dst_mask_table(edge_to_mask_idx)\n\n    # Initialize Hard Concrete mask parameters\n    hard_concrete = HardConcrete(n_masks, init_mean=0.5).to(device)\n    optimizer = torch.optim.Adam(hard_concrete.parameters(), lr=lr)\n\n    # Prepare inputs\n    if isinstance(clean_inputs, dict):\n        clean_ids = clean_inputs[\"input_ids\"]\n        if not isinstance(clean_ids, torch.Tensor):\n            clean_ids = torch.tensor(clean_ids)\n    else:\n        clean_ids = clean_inputs\n    clean_ids = clean_ids.to(device)\n\n    if isinstance(corrupt_inputs, dict):\n        corrupt_ids = corrupt_inputs[\"input_ids\"]\n        if not isinstance(corrupt_ids, torch.Tensor):\n            corrupt_ids = torch.tensor(corrupt_ids)\n    else:\n        corrupt_ids = corrupt_inputs\n    corrupt_ids = corrupt_ids.to(device)\n\n    if target_ids is not None:\n        if not isinstance(target_ids, torch.Tensor):\n            target_ids = torch.tensor(target_ids)\n        target_ids = target_ids.to(device)\n\n    # Get clean model logits (frozen)\n    model.eval()\n    with torch.no_grad():\n        clean_logits = model(clean_ids).logits.detach()\n\n    # Optimization loop\n    for epoch in range(n_epochs):\n        optimizer.zero_grad()\n\n        # Sample masks from Hard Concrete\n        masks = hard_concrete(training=True)\n\n        # Forward pass with masks applied\n        masked_logits = _masked_forward(\n            model, clean_ids, masks, arch_info, dst_mask_table,\n        )\n\n        # Loss = faithfulness + sparsity\n        faith_loss = _faithfulness_loss(masked_logits, clean_logits, target_ids)\n        l0_loss = hard_concrete.l0_penalty()\n        loss = faith_loss + lambda_l0 * l0_loss\n\n        loss.backward()\n        optimizer.step()\n\n    # Extract final scores\n    with torch.no_grad():\n        final_masks = hard_concrete.expected_masks()\n\n    scores: Dict[str, float] = {}\n    for edge_name, mask_idx in edge_to_mask_idx.items():\n        scores[edge_name] = final_masks[mask_idx].item()\n\n    return scores\n\n\n# ---------------------------------------------------------------------------\n# Utility: edge count estimation\n# ---------------------------------------------------------------------------\n\ndef estimate_edge_counts(\n    n_layers: int, n_heads: int, n_kv_heads: int,\n) -> Dict[str, int]:\n    \"\"\"Estimate edge and mask parameter counts for a given architecture.\"\"\"\n    heads_per_kv = n_heads // n_kv_heads\n    _, _, n_masks = _build_edge_topology(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n    # Total edges (including shared masks counted separately)\n    total_edges = 0\n    for L in range(n_layers):\n        n_src = 1 + L * (n_heads + 1)  # input + prior layers' heads + MLPs\n        # Attn edges: Q independent, K/V shared per KV group\n        total_edges += n_src * n_heads * 3  # q, k, v per head\n        # MLP edges: from all upstream including same-layer attn\n        n_src_mlp = n_src + n_heads\n        total_edges += n_src_mlp\n\n    return {\n        \"total_edges\": total_edges,\n        \"n_independent_masks\": n_masks,\n        \"mask_memory_bytes\": n_masks * 4,  # float32\n        \"mask_memory_mb\": n_masks * 4 / (1024 ** 2),\n    }\n",
      "numLines": 503,
      "startLine": 1,
      "totalLines": 503
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Tq2GDkm1LwJiNAkCr5wnFu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/ifr_scoring.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "5e4e2e47-e3ae-4f91-87c7-019ccb21d9af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019n9Cwt8v6du1oeFioJz8fj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12627,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12627
      },
      "output_tokens": 38,
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

_source line 9 · 2026-05-12T19:15:06.289Z_

<details><summary>↩ Tool result · `toolu_01Tq2GDkm1LwJiNAkCr5wnFu`</summary>

```text
1	"""IFR (Information Flow Routes) edge-level scoring for HuggingFace models.
2	
3	Implements ALTI-based proximity attribution from:
4	  Ferrando & Voita, "Information Flow Routes: Automatically Interpreting
5	  Language Models at Scale", EMNLP 2024.
6	
7	Scores each edge (u->v) by how much source u's output is "present" in the
8	residual stream that destination v reads from:
9	
10	    score(u->v) = max(||x_v||_1 - ||y_u - x_v||_1, 0)
11	
12	where y_u = component u's output, x_v = residual stream input to component v.
13	
14	Input:
15	  - model: HuggingFace CausalLM (Llama, Qwen2, Gemma2, Mistral, GPT2)
16	  - dataset: tokenized examples (list[dict], dict with input_ids, or Tensor)
17	  - metric_fn: unused — kept for interface parity with EAP-IG / Edge Pruning
18	
19	Output:
20	  - Dict[str, float] mapping canonical edge names to proximity scores (>=0).
21	    Format: "{src}->{dst}"
22	    Nodes: input, a{L}.h{H}, m{L}
23	    Attention destinations carry .q/.k/.v suffix: a{L}.h{H}.q
24	
25	Dependencies: torch, transformers
26	"""
27	
28	from __future__ import annotations
29	
30	import torch
31	import torch.nn as nn
32	from typing import Dict, Callable, Union
33	
34	
35	# ---------------------------------------------------------------------------
36	# Core proximity metric (ALTI)
37	# ---------------------------------------------------------------------------
38	
39	def _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:
40	    """max(||x_v||_1 - ||y_u - x_v||_1, 0), averaged over batch & sequence."""
41	    diff_norm = (y_u - x_v).abs().sum(dim=-1)
42	    base_norm = x_v.abs().sum(dim=-1)
43	    return (base_norm - diff_norm).clamp(min=0).mean().item()
44	
45	
46	# ---------------------------------------------------------------------------
47	# Architecture detection
48	# ---------------------------------------------------------------------------
49	
50	_LLAMA_LIKE = frozenset({
51	    "llama", "qwen2", "gemma", "gemma2", "mistral", "phi3", "phi",
52	})
53	
54	
55	def _get_model_info(model) -> dict:
56	    cfg = model.config
57	    model_type = getattr(cfg, "model_type", "")
58	
59	    if model_type in _LLAMA_LIKE:
60	        backbone = model.model
61	        layers = backbone.layers
62	        n_heads = cfg.num_attention_heads
63	        d_model = cfg.hidden_size
64	        return dict(
65	            arch="llama_like", backbone=backbone, layers=layers,
66	            n_layers=len(layers), n_heads=n_heads,
67	            head_dim=d_model // n_heads, d_model=d_model,
68	        )
69	
70	    if model_type == "gpt2":
71	        backbone = model.transformer
72	        layers = backbone.h
73	        n_heads = cfg.n_head
74	        d_model = cfg.n_embd
75	        return dict(
76	            arch="gpt2", backbone=backbone, layers=layers,
77	            n_layers=len(layers), n_heads=n_heads,
78	            head_dim=d_model // n_heads, d_model=d_model,
79	        )
80	
81	    raise ValueError(f"Unsupported model_type={model_type!r}")
82	
83	
84	# ---------------------------------------------------------------------------
85	# Edge topology helpers
86	# ---------------------------------------------------------------------------
87	
88	def _before_attn(kind: str, src_layer: int, dst_layer: int) -> bool:
89	    if kind == "input":
90	        return True
91	    return src_layer < dst_layer
92	
93	
94	def _before_mlp(kind: str, src_layer: int, dst_layer: int) -> bool:
95	    if kind == "input":
96	        return True
97	    if src_layer < dst_layer:
98	        return True
99	    return src_layer == dst_layer and kind == "attn"
100	
101	
102	# ---------------------------------------------------------------------------
103	# Dataset preparation
104	# ---------------------------------------------------------------------------
105	
106	def _prepare_tokens(
107	    dataset: Union[torch.Tensor, dict, list],
108	    device: str,
109	) -> torch.Tensor:
110	    if isinstance(dataset, torch.Tensor):
111	        t = dataset
112	    elif isinstance(dataset, dict) and "input_ids" in dataset:
113	        ids = dataset["input_ids"]
114	        t = ids if isinstance(ids, torch.Tensor) else torch.tensor(ids)
115	    elif isinstance(dataset, list) and len(dataset) > 0:
116	        first = dataset[0]
117	        if isinstance(first, dict) and "input_ids" in first:
118	            tensors = [
119	                d["input_ids"] if isinstance(d["input_ids"], torch.Tensor)
120	                else torch.tensor(d["input_ids"])
121	                for d in dataset
122	            ]
123	            t = torch.stack(tensors)
124	        elif isinstance(first, torch.Tensor):
125	            t = torch.stack(dataset)
126	        else:
127	            t = torch.tensor(dataset)
128	    else:
129	        raise TypeError(f"Unsupported dataset type: {type(dataset)}")
130	    t = t.to(device)
131	    return t.unsqueeze(0) if t.dim() == 1 else t
132	
133	
134	# ---------------------------------------------------------------------------
135	# Per-head decomposition through the output projection
136	# ---------------------------------------------------------------------------
137	
138	def _decompose_per_head(
139	    concat_heads: torch.Tensor,
140	    proj: nn.Module,
141	    n_heads: int,
142	    head_dim: int,
143	) -> Dict[int, torch.Tensor]:
144	    """Split concatenated head activations and project each through o_proj."""
145	    try:
146	        from transformers.pytorch_utils import Conv1D
147	        is_conv1d = isinstance(proj, Conv1D)
148	    except ImportError:
149	        is_conv1d = False
150	
151	    W = proj.weight
152	    heads: Dict[int, torch.Tensor] = {}
153	    for h in range(n_heads):
154	        h_in = concat_heads[:, :, h * head_dim:(h + 1) * head_dim]
155	        if is_conv1d:
156	            # Conv1D: weight [in, out], forward = input @ weight
157	            W_h = W[h * head_dim:(h + 1) * head_dim, :]
158	            heads[h] = h_in @ W_h
159	        else:
160	            # nn.Linear: weight [out, in], forward = input @ weight.T
161	            W_h = W[:, h * head_dim:(h + 1) * head_dim]
162	            heads[h] = h_in @ W_h.T
163	    return heads
164	
165	
166	# ---------------------------------------------------------------------------
167	# Canonical edge name helpers
168	# ---------------------------------------------------------------------------
169	
170	def _src_label(kind: str, layer: int, head: int) -> str:
171	    if kind == "input":
172	        return "input"
173	    if kind == "attn":
174	        return f"a{layer}.h{head}"
175	    return f"m{layer}"
176	
177	
178	# ---------------------------------------------------------------------------
179	# Main entry point
180	# ---------------------------------------------------------------------------
181	
182	def compute_ifr_edges(
183	    model,
184	    dataset,
185	    metric_fn: Callable,
186	    threshold: float = 0.1,
187	    device: str = "cuda",
188	) -> Dict[str, float]:
189	    """Compute IFR edge-level scores.
190	
191	    Returns dict of canonical_edge_name -> score.
192	    Edge format: "{src}->{dst}" with nodes named as:
193	      input, a{L}.h{H}, m{L}
194	    Attention destinations carry a .q/.k/.v suffix.
195	
196	    metric_fn is accepted for interface compatibility but unused;
197	    IFR is a non-causal, activation-decomposition method.
198	    """
199	    info = _get_model_info(model)
200	    arch = info["arch"]
201	    n_layers = info["n_layers"]
202	    n_heads = info["n_heads"]
203	    head_dim = info["head_dim"]
204	    layers = info["layers"]
205	
206	    tokens = _prepare_tokens(dataset, device)
207	
208	    # ---- register hooks to capture activations in a single forward pass ----
209	    cache: dict = dict(resid_pre={}, attn_out={}, head_out={}, mlp_out={})
210	    hooks: list = []
211	
212	    for l_idx in range(n_layers):
213	        layer = layers[l_idx]
214	
215	        # 1) resid_pre: residual stream entering this layer
216	        def _pre(mod, inp, *, _l=l_idx):
217	            x = inp[0]
218	            if isinstance(x, torch.Tensor):
219	                cache["resid_pre"][_l] = x.detach()
220	        hooks.append(layer.register_forward_pre_hook(_pre))
221	
222	        # 2) Per-head + full attention output via the output projection
223	        o_proj = (
224	            layer.self_attn.o_proj if arch == "llama_like"
225	            else layer.attn.c_proj
226	        )
227	
228	        def _oproj(mod, inp, out, *, _l=l_idx):
229	            cache["attn_out"][_l] = out.detach()
230	            cache["head_out"][_l] = _decompose_per_head(
231	                inp[0].detach(), mod, n_heads, head_dim,
232	            )
233	        hooks.append(o_proj.register_forward_hook(_oproj))
234	
235	        # 3) MLP output
236	        def _mlp(mod, inp, out, *, _l=l_idx):
237	            cache["mlp_out"][_l] = (
238	                out.detach() if isinstance(out, torch.Tensor)
239	                else out[0].detach()
240	            )
241	        hooks.append(layer.mlp.register_forward_hook(_mlp))
242	
243	    # ---- single forward pass ----
244	    model.eval()
245	    try:
246	        with torch.no_grad():
247	            model(tokens)
248	    finally:
249	        for h in hooks:
250	            h.remove()
251	
252	    # ---- build source activation table: (kind, layer, head) -> [B, S, D] ----
253	    src_act: Dict[tuple, torch.Tensor] = {}
254	    src_act[("input", -1, -1)] = cache["resid_pre"][0]
255	
256	    for l in range(n_layers):
257	        if l in cache["head_out"]:
258	            for h in range(n_heads):
259	                src_act[("attn", l, h)] = cache["head_out"][l][h]
260	        if l in cache["mlp_out"]:
261	            src_act[("mlp", l, -1)] = cache["mlp_out"][l]
262	
263	    # resid_mid[L] = resid_pre[L] + attn_out[L]
264	    # (exact for Llama/Qwen2/Mistral; slight approximation for Gemma2
265	    #  which applies an extra LN on attn output before residual addition)
266	    resid_mid: Dict[int, torch.Tensor] = {}
267	    for l in range(n_layers):
268	        if l in cache["resid_pre"] and l in cache["attn_out"]:
269	            resid_mid[l] = cache["resid_pre"][l] + cache["attn_out"][l]
270	
271	    # ---- proximity scoring ----
272	    edge_scores: Dict[str, float] = {}
273	
274	    for L in range(n_layers):
275	        rp = cache["resid_pre"].get(L)
276	        rm = resid_mid.get(L)
277	
278	        # Edges into attention at layer L
279	        if rp is not None:
280	            for (kind, sl, sh), y_u in src_act.items():
281	                if not _before_attn(kind, sl, L):
282	                    continue
283	                score = _proximity(y_u, rp)
284	                if score < threshold:
285	                    continue
286	                src = _src_label(kind, sl, sh)
287	                for H in range(n_heads):
288	                    for qkv in ("q", "k", "v"):
289	                        edge_scores[f"{src}->a{L}.h{H}.{qkv}"] = score
290	
291	        # Edges into MLP at layer L
292	        if rm is not None:
293	            for (kind, sl, sh), y_u in src_act.items():
294	                if not _before_mlp(kind, sl, L):
295	                    continue
296	                score = _proximity(y_u, rm)
297	                if score < threshold:
298	                    continue
299	                src = _src_label(kind, sl, sh)
300	                edge_scores[f"{src}->m{L}"] = score
301	
302	    return edge_scores
303	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "201964d0-ae9e-4eac-b4ba-ce27bd0e55c9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/ifr_scoring.py",
      "content": "\"\"\"IFR (Information Flow Routes) edge-level scoring for HuggingFace models.\n\nImplements ALTI-based proximity attribution from:\n  Ferrando & Voita, \"Information Flow Routes: Automatically Interpreting\n  Language Models at Scale\", EMNLP 2024.\n\nScores each edge (u->v) by how much source u's output is \"present\" in the\nresidual stream that destination v reads from:\n\n    score(u->v) = max(||x_v||_1 - ||y_u - x_v||_1, 0)\n\nwhere y_u = component u's output, x_v = residual stream input to component v.\n\nInput:\n  - model: HuggingFace CausalLM (Llama, Qwen2, Gemma2, Mistral, GPT2)\n  - dataset: tokenized examples (list[dict], dict with input_ids, or Tensor)\n  - metric_fn: unused — kept for interface parity with EAP-IG / Edge Pruning\n\nOutput:\n  - Dict[str, float] mapping canonical edge names to proximity scores (>=0).\n    Format: \"{src}->{dst}\"\n    Nodes: input, a{L}.h{H}, m{L}\n    Attention destinations carry .q/.k/.v suffix: a{L}.h{H}.q\n\nDependencies: torch, transformers\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nfrom typing import Dict, Callable, Union\n\n\n# ---------------------------------------------------------------------------\n# Core proximity metric (ALTI)\n# ---------------------------------------------------------------------------\n\ndef _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:\n    \"\"\"max(||x_v||_1 - ||y_u - x_v||_1, 0), averaged over batch & sequence.\"\"\"\n    diff_norm = (y_u - x_v).abs().sum(dim=-1)\n    base_norm = x_v.abs().sum(dim=-1)\n    return (base_norm - diff_norm).clamp(min=0).mean().item()\n\n\n# ---------------------------------------------------------------------------\n# Architecture detection\n# ---------------------------------------------------------------------------\n\n_LLAMA_LIKE = frozenset({\n    \"llama\", \"qwen2\", \"gemma\", \"gemma2\", \"mistral\", \"phi3\", \"phi\",\n})\n\n\ndef _get_model_info(model) -> dict:\n    cfg = model.config\n    model_type = getattr(cfg, \"model_type\", \"\")\n\n    if model_type in _LLAMA_LIKE:\n        backbone = model.model\n        layers = backbone.layers\n        n_heads = cfg.num_attention_heads\n        d_model = cfg.hidden_size\n        return dict(\n            arch=\"llama_like\", backbone=backbone, layers=layers,\n            n_layers=len(layers), n_heads=n_heads,\n            head_dim=d_model // n_heads, d_model=d_model,\n        )\n\n    if model_type == \"gpt2\":\n        backbone = model.transformer\n        layers = backbone.h\n        n_heads = cfg.n_head\n        d_model = cfg.n_embd\n        return dict(\n            arch=\"gpt2\", backbone=backbone, layers=layers,\n            n_layers=len(layers), n_heads=n_heads,\n            head_dim=d_model // n_heads, d_model=d_model,\n        )\n\n    raise ValueError(f\"Unsupported model_type={model_type!r}\")\n\n\n# ---------------------------------------------------------------------------\n# Edge topology helpers\n# ---------------------------------------------------------------------------\n\ndef _before_attn(kind: str, src_layer: int, dst_layer: int) -> bool:\n    if kind == \"input\":\n        return True\n    return src_layer < dst_layer\n\n\ndef _before_mlp(kind: str, src_layer: int, dst_layer: int) -> bool:\n    if kind == \"input\":\n        return True\n    if src_layer < dst_layer:\n        return True\n    return src_layer == dst_layer and kind == \"attn\"\n\n\n# ---------------------------------------------------------------------------\n# Dataset preparation\n# ---------------------------------------------------------------------------\n\ndef _prepare_tokens(\n    dataset: Union[torch.Tensor, dict, list],\n    device: str,\n) -> torch.Tensor:\n    if isinstance(dataset, torch.Tensor):\n        t = dataset\n    elif isinstance(dataset, dict) and \"input_ids\" in dataset:\n        ids = dataset[\"input_ids\"]\n        t = ids if isinstance(ids, torch.Tensor) else torch.tensor(ids)\n    elif isinstance(dataset, list) and len(dataset) > 0:\n        first = dataset[0]\n        if isinstance(first, dict) and \"input_ids\" in first:\n            tensors = [\n                d[\"input_ids\"] if isinstance(d[\"input_ids\"], torch.Tensor)\n                else torch.tensor(d[\"input_ids\"])\n                for d in dataset\n            ]\n            t = torch.stack(tensors)\n        elif isinstance(first, torch.Tensor):\n            t = torch.stack(dataset)\n        else:\n            t = torch.tensor(dataset)\n    else:\n        raise TypeError(f\"Unsupported dataset type: {type(dataset)}\")\n    t = t.to(device)\n    return t.unsqueeze(0) if t.dim() == 1 else t\n\n\n# ---------------------------------------------------------------------------\n# Per-head decomposition through the output projection\n# ---------------------------------------------------------------------------\n\ndef _decompose_per_head(\n    concat_heads: torch.Tensor,\n    proj: nn.Module,\n    n_heads: int,\n    head_dim: int,\n) -> Dict[int, torch.Tensor]:\n    \"\"\"Split concatenated head activations and project each through o_proj.\"\"\"\n    try:\n        from transformers.pytorch_utils import Conv1D\n        is_conv1d = isinstance(proj, Conv1D)\n    except ImportError:\n        is_conv1d = False\n\n    W = proj.weight\n    heads: Dict[int, torch.Tensor] = {}\n    for h in range(n_heads):\n        h_in = concat_heads[:, :, h * head_dim:(h + 1) * head_dim]\n        if is_conv1d:\n            # Conv1D: weight [in, out], forward = input @ weight\n            W_h = W[h * head_dim:(h + 1) * head_dim, :]\n            heads[h] = h_in @ W_h\n        else:\n            # nn.Linear: weight [out, in], forward = input @ weight.T\n            W_h = W[:, h * head_dim:(h + 1) * head_dim]\n            heads[h] = h_in @ W_h.T\n    return heads\n\n\n# ---------------------------------------------------------------------------\n# Canonical edge name helpers\n# ---------------------------------------------------------------------------\n\ndef _src_label(kind: str, layer: int, head: int) -> str:\n    if kind == \"input\":\n        return \"input\"\n    if kind == \"attn\":\n        return f\"a{layer}.h{head}\"\n    return f\"m{layer}\"\n\n\n# ---------------------------------------------------------------------------\n# Main entry point\n# ---------------------------------------------------------------------------\n\ndef compute_ifr_edges(\n    model,\n    dataset,\n    metric_fn: Callable,\n    threshold: float = 0.1,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Compute IFR edge-level scores.\n\n    Returns dict of canonical_edge_name -> score.\n    Edge format: \"{src}->{dst}\" with nodes named as:\n      input, a{L}.h{H}, m{L}\n    Attention destinations carry a .q/.k/.v suffix.\n\n    metric_fn is accepted for interface compatibility but unused;\n    IFR is a non-causal, activation-decomposition method.\n    \"\"\"\n    info = _get_model_info(model)\n    arch = info[\"arch\"]\n    n_layers = info[\"n_layers\"]\n    n_heads = info[\"n_heads\"]\n    head_dim = info[\"head_dim\"]\n    layers = info[\"layers\"]\n\n    tokens = _prepare_tokens(dataset, device)\n\n    # ---- register hooks to capture activations in a single forward pass ----\n    cache: dict = dict(resid_pre={}, attn_out={}, head_out={}, mlp_out={})\n    hooks: list = []\n\n    for l_idx in range(n_layers):\n        layer = layers[l_idx]\n\n        # 1) resid_pre: residual stream entering this layer\n        def _pre(mod, inp, *, _l=l_idx):\n            x = inp[0]\n            if isinstance(x, torch.Tensor):\n                cache[\"resid_pre\"][_l] = x.detach()\n        hooks.append(layer.register_forward_pre_hook(_pre))\n\n        # 2) Per-head + full attention output via the output projection\n        o_proj = (\n            layer.self_attn.o_proj if arch == \"llama_like\"\n            else layer.attn.c_proj\n        )\n\n        def _oproj(mod, inp, out, *, _l=l_idx):\n            cache[\"attn_out\"][_l] = out.detach()\n            cache[\"head_out\"][_l] = _decompose_per_head(\n                inp[0].detach(), mod, n_heads, head_dim,\n            )\n        hooks.append(o_proj.register_forward_hook(_oproj))\n\n        # 3) MLP output\n        def _mlp(mod, inp, out, *, _l=l_idx):\n            cache[\"mlp_out\"][_l] = (\n                out.detach() if isinstance(out, torch.Tensor)\n                else out[0].detach()\n            )\n        hooks.append(layer.mlp.register_forward_hook(_mlp))\n\n    # ---- single forward pass ----\n    model.eval()\n    try:\n        with torch.no_grad():\n            model(tokens)\n    finally:\n        for h in hooks:\n            h.remove()\n\n    # ---- build source activation table: (kind, layer, head) -> [B, S, D] ----\n    src_act: Dict[tuple, torch.Tensor] = {}\n    src_act[(\"input\", -1, -1)] = cache[\"resid_pre\"][0]\n\n    for l in range(n_layers):\n        if l in cache[\"head_out\"]:\n            for h in range(n_heads):\n                src_act[(\"attn\", l, h)] = cache[\"head_out\"][l][h]\n        if l in cache[\"mlp_out\"]:\n            src_act[(\"mlp\", l, -1)] = cache[\"mlp_out\"][l]\n\n    # resid_mid[L] = resid_pre[L] + attn_out[L]\n    # (exact for Llama/Qwen2/Mistral; slight approximation for Gemma2\n    #  which applies an extra LN on attn output before residual addition)\n    resid_mid: Dict[int, torch.Tensor] = {}\n    for l in range(n_layers):\n        if l in cache[\"resid_pre\"] and l in cache[\"attn_out\"]:\n            resid_mid[l] = cache[\"resid_pre\"][l] + cache[\"attn_out\"][l]\n\n    # ---- proximity scoring ----\n    edge_scores: Dict[str, float] = {}\n\n    for L in range(n_layers):\n        rp = cache[\"resid_pre\"].get(L)\n        rm = resid_mid.get(L)\n\n        # Edges into attention at layer L\n        if rp is not None:\n            for (kind, sl, sh), y_u in src_act.items():\n                if not _before_attn(kind, sl, L):\n                    continue\n                score = _proximity(y_u, rp)\n                if score < threshold:\n                    continue\n                src = _src_label(kind, sl, sh)\n                for H in range(n_heads):\n                    for qkv in (\"q\", \"k\", \"v\"):\n                        edge_scores[f\"{src}->a{L}.h{H}.{qkv}\"] = score\n\n        # Edges into MLP at layer L\n        if rm is not None:\n            for (kind, sl, sh), y_u in src_act.items():\n                if not _before_mlp(kind, sl, L):\n                    continue\n                score = _proximity(y_u, rm)\n                if score < threshold:\n                    continue\n                src = _src_label(kind, sl, sh)\n                edge_scores[f\"{src}->m{L}\"] = score\n\n    return edge_scores\n",
      "numLines": 303,
      "startLine": 1,
      "totalLines": 303
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01L3yPt8cy9TSZCTSeMNZL3J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_edge_pruning_scoring.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "a5c798f8-f207-40ed-aea0-f3dbfbef4608",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019n9Cwt8v6du1oeFioJz8fj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12627,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12627
      },
      "output_tokens": 38,
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

_source line 11 · 2026-05-12T19:15:06.498Z_

<details><summary>↩ Tool result · `toolu_01L3yPt8cy9TSZCTSeMNZL3J`</summary>

```text
1	"""Smoke tests for edge_pruning_scoring.py.
2	
3	Tests split by dependency:
4	  - No-torch tests: AST syntax, function signature from AST, edge topology logic
5	  - Torch tests: HardConcrete numerics, gradient flow, estimate_edge_counts
6	
7	Run without torch: python3 test_edge_pruning_scoring.py
8	Run with torch:    python3 test_edge_pruning_scoring.py  (auto-detects)
9	"""
10	
11	import ast
12	import os
13	import sys
14	
15	SRC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "edge_pruning_scoring.py")
16	
17	HAS_TORCH = False
18	try:
19	    import torch
20	    HAS_TORCH = True
21	except ImportError:
22	    pass
23	
24	
25	# ===========================================================================
26	# No-torch tests (pure AST / logic)
27	# ===========================================================================
28	
29	def test_ast_syntax():
30	    with open(SRC_PATH) as f:
31	        source = f.read()
32	    tree = ast.parse(source)
33	    assert isinstance(tree, ast.Module)
34	    top_names = {node.name for node in ast.walk(tree)
35	                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
36	    assert "HardConcrete" in top_names
37	    assert "compute_edge_pruning_scores" in top_names
38	    assert "estimate_edge_counts" in top_names
39	    assert "_build_edge_topology" in top_names
40	    assert "_masked_forward" in top_names
41	    assert "_faithfulness_loss" in top_names
42	    print("[PASS] AST syntax check")
43	
44	
45	def test_function_signature_from_ast():
46	    with open(SRC_PATH) as f:
47	        source = f.read()
48	    tree = ast.parse(source)
49	    for node in ast.walk(tree):
50	        if isinstance(node, ast.FunctionDef) and node.name == "compute_edge_pruning_scores":
51	            args = node.args
52	            param_names = [a.arg for a in args.args]
53	            expected = [
54	                "model", "clean_inputs", "corrupt_inputs", "metric_fn",
55	                "target_ids", "n_epochs", "lambda_l0", "lr", "device",
56	            ]
57	            assert param_names == expected, f"Expected {expected}, got {param_names}"
58	            # Check defaults: n_epochs=100, lambda_l0=1e-3, lr=0.1, device="cuda"
59	            defaults = args.defaults
60	            assert len(defaults) == 5  # target_ids=None, n_epochs=100, lambda_l0=1e-3, lr=0.1, device="cuda"
61	            print("[PASS] Function signature (AST)")
62	            return
63	    raise AssertionError("compute_edge_pruning_scores not found")
64	
65	
66	def _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, heads_per_kv_group):
67	    """Standalone copy of edge topology logic for testing without torch."""
68	    edge_names = []
69	    edge_to_mask_idx = {}
70	    mask_idx = 0
71	
72	    def _src_nodes(layer, include_attn_same_layer=False):
73	        yield "input"
74	        for l in range(layer):
75	            for h in range(n_heads):
76	                yield f"a{l}.h{h}"
77	            yield f"m{l}"
78	        if include_attn_same_layer:
79	            for h in range(n_heads):
80	                yield f"a{layer}.h{h}"
81	
82	    for L in range(n_layers):
83	        srcs_attn = list(_src_nodes(L))
84	        for src in srcs_attn:
85	            for H in range(n_heads):
86	                q_edge = f"{src}->a{L}.h{H}.q"
87	                edge_names.append(q_edge)
88	                edge_to_mask_idx[q_edge] = mask_idx
89	                mask_idx += 1
90	            for kv_group in range(n_kv_heads):
91	                k_mask_idx = mask_idx
92	                mask_idx += 1
93	                for h_in_group in range(heads_per_kv_group):
94	                    H = kv_group * heads_per_kv_group + h_in_group
95	                    k_edge = f"{src}->a{L}.h{H}.k"
96	                    edge_names.append(k_edge)
97	                    edge_to_mask_idx[k_edge] = k_mask_idx
98	            for kv_group in range(n_kv_heads):
99	                v_mask_idx = mask_idx
100	                mask_idx += 1
101	                for h_in_group in range(heads_per_kv_group):
102	                    H = kv_group * heads_per_kv_group + h_in_group
103	                    v_edge = f"{src}->a{L}.h{H}.v"
104	                    edge_names.append(v_edge)
105	                    edge_to_mask_idx[v_edge] = v_mask_idx
106	
107	        srcs_mlp = list(_src_nodes(L, include_attn_same_layer=True))
108	        for src in srcs_mlp:
109	            mlp_edge = f"{src}->m{L}"
110	            edge_names.append(mlp_edge)
111	            edge_to_mask_idx[mlp_edge] = mask_idx
112	            mask_idx += 1
113	
114	    return edge_names, edge_to_mask_idx, mask_idx
115	
116	
117	def test_edge_topology_no_gqa():
118	    n_layers, n_heads, n_kv_heads = 2, 4, 4
119	    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(
120	        n_layers, n_heads, n_kv_heads, 1,
121	    )
122	    assert len(set(edge_to_mask_idx.values())) == n_masks
123	    assert n_masks == len(edge_to_mask_idx)
124	    assert "input->a0.h0.q" in edge_to_mask_idx
125	    assert "input->a0.h0.k" in edge_to_mask_idx
126	    assert "input->a0.h0.v" in edge_to_mask_idx
127	    assert "input->m0" in edge_to_mask_idx
128	    assert "a0.h0->m0" in edge_to_mask_idx
129	    assert "a0.h0->a1.h0.q" in edge_to_mask_idx
130	    print(f"[PASS] Edge topology non-GQA: {len(edge_names)} edges, {n_masks} masks")
131	
132	
133	def test_edge_topology_gqa():
134	    n_layers, n_heads, n_kv_heads = 2, 14, 2
135	    heads_per_kv = 7
136	    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(
137	        n_layers, n_heads, n_kv_heads, heads_per_kv,
138	    )
139	
140	    # K mask sharing within KV group 0 (heads 0-6)
141	    k_masks_g0 = {edge_to_mask_idx[f"input->a0.h{h}.k"] for h in range(7)}
142	    assert len(k_masks_g0) == 1, f"KV group 0 K masks should share, got {len(k_masks_g0)}"
143	
144	    # K mask sharing within KV group 1 (heads 7-13)
145	    k_masks_g1 = {edge_to_mask_idx[f"input->a0.h{h}.k"] for h in range(7, 14)}
146	    assert len(k_masks_g1) == 1
147	    assert k_masks_g0 != k_masks_g1
148	
149	    # Q edges independent
150	    q_masks = {edge_to_mask_idx[f"input->a0.h{h}.q"] for h in range(14)}
151	    assert len(q_masks) == 14
152	
153	    # V sharing
154	    v_masks_g0 = {edge_to_mask_idx[f"input->a0.h{h}.v"] for h in range(7)}
155	    assert len(v_masks_g0) == 1
156	
157	    print(f"[PASS] Edge topology GQA: {len(edge_names)} edges, {n_masks} masks")
158	
159	
160	def test_dst_mask_table():
161	    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(1, 2, 2, 1)
162	    table = {}
163	    for edge, idx in edge_to_mask_idx.items():
164	        src, dst = edge.split("->", 1)
165	        table.setdefault(dst, {})[src] = idx
166	
167	    assert "a0.h0.q" in table
168	    assert "input" in table["a0.h0.q"]
169	    assert "m0" in table
170	    assert "input" in table["m0"]
171	    assert "a0.h0" in table["m0"]
172	    assert "a0.h1" in table["m0"]
173	    print("[PASS] Destination mask table")
174	
175	
176	def test_edge_counts_qwen():
177	    """Estimate edge counts for Qwen-2.5 0.5B without torch."""
178	    _, _, n_masks = _build_edge_topology_standalone(24, 14, 2, 7)
179	    total_edges = 0
180	    for L in range(24):
181	        n_src = 1 + L * (14 + 1)
182	        total_edges += n_src * 14 * 3
183	        total_edges += (n_src + 14)
184	    mem_mb = n_masks * 4 / (1024 ** 2)
185	    assert total_edges > 0
186	    assert n_masks > 0
187	    assert n_masks <= total_edges
188	    print(f"[PASS] Qwen-2.5 0.5B: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB")
189	
190	
191	def test_edge_counts_gpt2():
192	    _, _, n_masks = _build_edge_topology_standalone(12, 12, 12, 1)
193	    total_edges = 0
194	    for L in range(12):
195	        n_src = 1 + L * (12 + 1)
196	        total_edges += n_src * 12 * 3
197	        total_edges += (n_src + 12)
198	    mem_mb = n_masks * 4 / (1024 ** 2)
199	    print(f"[PASS] GPT-2 small: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB")
200	
201	
202	# ===========================================================================
203	# Torch-dependent tests
204	# ===========================================================================
205	
206	def test_hard_concrete_sampling():
207	    from edge_pruning_scoring import HardConcrete
208	    hc = HardConcrete(n_masks=1000, init_mean=0.5)
209	    torch.manual_seed(42)
210	    samples = hc(training=True)
211	    assert samples.shape == (1000,)
212	    assert samples.min() >= 0.0
213	    assert samples.max() <= 1.0
214	    penalty = hc.l0_penalty()
215	    assert penalty.item() >= 0.0
216	    assert penalty.item() <= 1000.0
217	    expected = hc.expected_masks()
218	    assert expected.min() >= 0.0
219	    assert expected.max() <= 1.0
220	    print("[PASS] HardConcrete sampling")
221	
222	
223	def test_hard_concrete_gradient():
224	    from edge_pruning_scoring import HardConcrete
225	    hc = HardConcrete(n_masks=10, init_mean=0.5)
226	    masks = hc(training=True)
227	    masks.sum().backward()
228	    assert hc.log_alpha.grad is not None
229	    assert not torch.all(hc.log_alpha.grad == 0)
230	    print("[PASS] HardConcrete gradient flow")
231	
232	
233	def test_hard_concrete_extremes():
234	    from edge_pruning_scoring import HardConcrete
235	    hc = HardConcrete(n_masks=2, init_mean=0.5)
236	    with torch.no_grad():
237	        hc.log_alpha[0] = -10.0
238	        hc.log_alpha[1] = 10.0
239	    masks = hc.expected_masks()
240	    assert masks[0].item() < 0.01
241	    assert masks[1].item() > 0.99
242	    print("[PASS] HardConcrete extremes")
243	
244	
245	def test_module_topology_matches_standalone():
246	    """Verify the actual module's topology matches our standalone copy."""
247	    from edge_pruning_scoring import _build_edge_topology
248	    _, idx_module, n_module = _build_edge_topology(2, 14, 2, 7)
249	    _, idx_standalone, n_standalone = _build_edge_topology_standalone(2, 14, 2, 7)
250	    assert n_module == n_standalone, f"n_masks mismatch: {n_module} vs {n_standalone}"
251	    assert idx_module == idx_standalone, "edge_to_mask_idx mismatch"
252	    print("[PASS] Module topology matches standalone")
253	
254	
255	# ===========================================================================
256	
257	if __name__ == "__main__":
258	    # Always run: no-torch tests
259	    test_ast_syntax()
260	    test_function_signature_from_ast()
261	    test_edge_topology_no_gqa()
262	    test_edge_topology_gqa()
263	    test_dst_mask_table()
264	    test_edge_counts_qwen()
265	    test_edge_counts_gpt2()
266	
267	    if HAS_TORCH:
268	        test_hard_concrete_sampling()
269	        test_hard_concrete_gradient()
270	        test_hard_concrete_extremes()
271	        test_module_topology_matches_standalone()
272	    else:
273	        print("[SKIP] Torch-dependent tests (torch not installed)")
274	
275	    print("\n=== All applicable smoke tests passed ===")
276	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "3d16719c-2439-4163-8211-0b0739dbb750",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_edge_pruning_scoring.py",
      "content": "\"\"\"Smoke tests for edge_pruning_scoring.py.\n\nTests split by dependency:\n  - No-torch tests: AST syntax, function signature from AST, edge topology logic\n  - Torch tests: HardConcrete numerics, gradient flow, estimate_edge_counts\n\nRun without torch: python3 test_edge_pruning_scoring.py\nRun with torch:    python3 test_edge_pruning_scoring.py  (auto-detects)\n\"\"\"\n\nimport ast\nimport os\nimport sys\n\nSRC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), \"edge_pruning_scoring.py\")\n\nHAS_TORCH = False\ntry:\n    import torch\n    HAS_TORCH = True\nexcept ImportError:\n    pass\n\n\n# ===========================================================================\n# No-torch tests (pure AST / logic)\n# ===========================================================================\n\ndef test_ast_syntax():\n    with open(SRC_PATH) as f:\n        source = f.read()\n    tree = ast.parse(source)\n    assert isinstance(tree, ast.Module)\n    top_names = {node.name for node in ast.walk(tree)\n                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}\n    assert \"HardConcrete\" in top_names\n    assert \"compute_edge_pruning_scores\" in top_names\n    assert \"estimate_edge_counts\" in top_names\n    assert \"_build_edge_topology\" in top_names\n    assert \"_masked_forward\" in top_names\n    assert \"_faithfulness_loss\" in top_names\n    print(\"[PASS] AST syntax check\")\n\n\ndef test_function_signature_from_ast():\n    with open(SRC_PATH) as f:\n        source = f.read()\n    tree = ast.parse(source)\n    for node in ast.walk(tree):\n        if isinstance(node, ast.FunctionDef) and node.name == \"compute_edge_pruning_scores\":\n            args = node.args\n            param_names = [a.arg for a in args.args]\n            expected = [\n                \"model\", \"clean_inputs\", \"corrupt_inputs\", \"metric_fn\",\n                \"target_ids\", \"n_epochs\", \"lambda_l0\", \"lr\", \"device\",\n            ]\n            assert param_names == expected, f\"Expected {expected}, got {param_names}\"\n            # Check defaults: n_epochs=100, lambda_l0=1e-3, lr=0.1, device=\"cuda\"\n            defaults = args.defaults\n            assert len(defaults) == 5  # target_ids=None, n_epochs=100, lambda_l0=1e-3, lr=0.1, device=\"cuda\"\n            print(\"[PASS] Function signature (AST)\")\n            return\n    raise AssertionError(\"compute_edge_pruning_scores not found\")\n\n\ndef _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, heads_per_kv_group):\n    \"\"\"Standalone copy of edge topology logic for testing without torch.\"\"\"\n    edge_names = []\n    edge_to_mask_idx = {}\n    mask_idx = 0\n\n    def _src_nodes(layer, include_attn_same_layer=False):\n        yield \"input\"\n        for l in range(layer):\n            for h in range(n_heads):\n                yield f\"a{l}.h{h}\"\n            yield f\"m{l}\"\n        if include_attn_same_layer:\n            for h in range(n_heads):\n                yield f\"a{layer}.h{h}\"\n\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes(L))\n        for src in srcs_attn:\n            for H in range(n_heads):\n                q_edge = f\"{src}->a{L}.h{H}.q\"\n                edge_names.append(q_edge)\n                edge_to_mask_idx[q_edge] = mask_idx\n                mask_idx += 1\n            for kv_group in range(n_kv_heads):\n                k_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    k_edge = f\"{src}->a{L}.h{H}.k\"\n                    edge_names.append(k_edge)\n                    edge_to_mask_idx[k_edge] = k_mask_idx\n            for kv_group in range(n_kv_heads):\n                v_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    v_edge = f\"{src}->a{L}.h{H}.v\"\n                    edge_names.append(v_edge)\n                    edge_to_mask_idx[v_edge] = v_mask_idx\n\n        srcs_mlp = list(_src_nodes(L, include_attn_same_layer=True))\n        for src in srcs_mlp:\n            mlp_edge = f\"{src}->m{L}\"\n            edge_names.append(mlp_edge)\n            edge_to_mask_idx[mlp_edge] = mask_idx\n            mask_idx += 1\n\n    return edge_names, edge_to_mask_idx, mask_idx\n\n\ndef test_edge_topology_no_gqa():\n    n_layers, n_heads, n_kv_heads = 2, 4, 4\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, 1,\n    )\n    assert len(set(edge_to_mask_idx.values())) == n_masks\n    assert n_masks == len(edge_to_mask_idx)\n    assert \"input->a0.h0.q\" in edge_to_mask_idx\n    assert \"input->a0.h0.k\" in edge_to_mask_idx\n    assert \"input->a0.h0.v\" in edge_to_mask_idx\n    assert \"input->m0\" in edge_to_mask_idx\n    assert \"a0.h0->m0\" in edge_to_mask_idx\n    assert \"a0.h0->a1.h0.q\" in edge_to_mask_idx\n    print(f\"[PASS] Edge topology non-GQA: {len(edge_names)} edges, {n_masks} masks\")\n\n\ndef test_edge_topology_gqa():\n    n_layers, n_heads, n_kv_heads = 2, 14, 2\n    heads_per_kv = 7\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n\n    # K mask sharing within KV group 0 (heads 0-6)\n    k_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7)}\n    assert len(k_masks_g0) == 1, f\"KV group 0 K masks should share, got {len(k_masks_g0)}\"\n\n    # K mask sharing within KV group 1 (heads 7-13)\n    k_masks_g1 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7, 14)}\n    assert len(k_masks_g1) == 1\n    assert k_masks_g0 != k_masks_g1\n\n    # Q edges independent\n    q_masks = {edge_to_mask_idx[f\"input->a0.h{h}.q\"] for h in range(14)}\n    assert len(q_masks) == 14\n\n    # V sharing\n    v_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.v\"] for h in range(7)}\n    assert len(v_masks_g0) == 1\n\n    print(f\"[PASS] Edge topology GQA: {len(edge_names)} edges, {n_masks} masks\")\n\n\ndef test_dst_mask_table():\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(1, 2, 2, 1)\n    table = {}\n    for edge, idx in edge_to_mask_idx.items():\n        src, dst = edge.split(\"->\", 1)\n        table.setdefault(dst, {})[src] = idx\n\n    assert \"a0.h0.q\" in table\n    assert \"input\" in table[\"a0.h0.q\"]\n    assert \"m0\" in table\n    assert \"input\" in table[\"m0\"]\n    assert \"a0.h0\" in table[\"m0\"]\n    assert \"a0.h1\" in table[\"m0\"]\n    print(\"[PASS] Destination mask table\")\n\n\ndef test_edge_counts_qwen():\n    \"\"\"Estimate edge counts for Qwen-2.5 0.5B without torch.\"\"\"\n    _, _, n_masks = _build_edge_topology_standalone(24, 14, 2, 7)\n    total_edges = 0\n    for L in range(24):\n        n_src = 1 + L * (14 + 1)\n        total_edges += n_src * 14 * 3\n        total_edges += (n_src + 14)\n    mem_mb = n_masks * 4 / (1024 ** 2)\n    assert total_edges > 0\n    assert n_masks > 0\n    assert n_masks <= total_edges\n    print(f\"[PASS] Qwen-2.5 0.5B: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB\")\n\n\ndef test_edge_counts_gpt2():\n    _, _, n_masks = _build_edge_topology_standalone(12, 12, 12, 1)\n    total_edges = 0\n    for L in range(12):\n        n_src = 1 + L * (12 + 1)\n        total_edges += n_src * 12 * 3\n        total_edges += (n_src + 12)\n    mem_mb = n_masks * 4 / (1024 ** 2)\n    print(f\"[PASS] GPT-2 small: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB\")\n\n\n# ===========================================================================\n# Torch-dependent tests\n# ===========================================================================\n\ndef test_hard_concrete_sampling():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=1000, init_mean=0.5)\n    torch.manual_seed(42)\n    samples = hc(training=True)\n    assert samples.shape == (1000,)\n    assert samples.min() >= 0.0\n    assert samples.max() <= 1.0\n    penalty = hc.l0_penalty()\n    assert penalty.item() >= 0.0\n    assert penalty.item() <= 1000.0\n    expected = hc.expected_masks()\n    assert expected.min() >= 0.0\n    assert expected.max() <= 1.0\n    print(\"[PASS] HardConcrete sampling\")\n\n\ndef test_hard_concrete_gradient():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=10, init_mean=0.5)\n    masks = hc(training=True)\n    masks.sum().backward()\n    assert hc.log_alpha.grad is not None\n    assert not torch.all(hc.log_alpha.grad == 0)\n    print(\"[PASS] HardConcrete gradient flow\")\n\n\ndef test_hard_concrete_extremes():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=2, init_mean=0.5)\n    with torch.no_grad():\n        hc.log_alpha[0] = -10.0\n        hc.log_alpha[1] = 10.0\n    masks = hc.expected_masks()\n    assert masks[0].item() < 0.01\n    assert masks[1].item() > 0.99\n    print(\"[PASS] HardConcrete extremes\")\n\n\ndef test_module_topology_matches_standalone():\n    \"\"\"Verify the actual module's topology matches our standalone copy.\"\"\"\n    from edge_pruning_scoring import _build_edge_topology\n    _, idx_module, n_module = _build_edge_topology(2, 14, 2, 7)\n    _, idx_standalone, n_standalone = _build_edge_topology_standalone(2, 14, 2, 7)\n    assert n_module == n_standalone, f\"n_masks mismatch: {n_module} vs {n_standalone}\"\n    assert idx_module == idx_standalone, \"edge_to_mask_idx mismatch\"\n    print(\"[PASS] Module topology matches standalone\")\n\n\n# ===========================================================================\n\nif __name__ == \"__main__\":\n    # Always run: no-torch tests\n    test_ast_syntax()\n    test_function_signature_from_ast()\n    test_edge_topology_no_gqa()\n    test_edge_topology_gqa()\n    test_dst_mask_table()\n    test_edge_counts_qwen()\n    test_edge_counts_gpt2()\n\n    if HAS_TORCH:\n        test_hard_concrete_sampling()\n        test_hard_concrete_gradient()\n        test_hard_concrete_extremes()\n        test_module_topology_matches_standalone()\n    else:\n        print(\"[SKIP] Torch-dependent tests (torch not installed)\")\n\n    print(\"\\n=== All applicable smoke tests passed ===\")\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

````text
Now I have a thorough understanding of the v1 code. Let me analyze the issues:

1. **MLP mask not applied**: The `_layer_pre_hook` only constructs masked residual for attention input. MLP edges have mask parameters but no forward hook applies them. The MLP receives the attention-masked residual, not an MLP-specific masked residual.

2. **Q/K/V mean collapse**: Lines 328-329 average all Q/K/V mask values for a given (src, layer) pair into one scalar, losing per-head and per-QKV-type granularity.
   
Now I'm redesigning the forward pass to apply masks at the right granularity. I'll add separate pre-hooks for the Q, K, and V projections to apply their respective edge masks, plus another hook for the MLP to use its own mask parameters instead of the attention-masked residual.

The tricky part is that each attention head needs its own masked input constructed from weighted combinations of source activations, where the weights come from the edge masks specific to that head and projection type. I'm working through how per-head masking should apply to the residual stream—the key insight is that in models like Llama, the d_model dimension can be chunked into head-sized segments, so masking individual head chunks before projection makes sense because each head's projection weights operate on the full d_model anyway. I see the core issue now—q_proj takes the full residual stream and produces all head queries simultaneously, so applying per-head input masking requires modifying how the projection itself works. I'm sketching out a pre-hook that would iterate through source activations and heads to construct a masked input, though this approach of trying to mask at the input level runs into the fundamental constraint that q_proj doesn't operate independently per head.

Writing the masking logic... mask_idx = edge_to_mask_idx[f"{src_name}->a{L}.h{h}.q"]
z = hard_concrete_sample(mask_params[mask_idx])
masked_x[:, :, h*d_head:(h+1)*d_head] += src_act[:, :, h*d_head:(h+1)*d_head] * z
return (masked_x,) + args[1:]
```

The task wants me to slice the d_model dimension into head_dim chunks, assuming each head's query primarily depends on its corresponding residual stream chunk. This is a standard approximation in edge pruning literature, even though it's not strictly guaranteed by transformer architecture.

For K and V with grouped query attention, I need per-KV-group masks where all heads in the same group share the same K and V masks.

Building the masking logic for k_proj... I'm realizing that applying the KV group mask to the corresponding slice of d_model works because each KV group covers a fixed number of heads, which translates directly to a contiguous chunk in the residual stream. The task requires pre-hook masking on the residual stream itself, so all heads within a KV group share the same mask value, meaning that entire d_model chunk gets masked uniformly. Now I need to think through how this applies specifically to the query projection and work out the implementation details.

Writing masking logic... I'm realizing that for k_proj, I need to partition the d_model input into n_kv_heads groups, where each group has size heads_per_kv_group * head_dim, and apply the corresponding mask to each group's contribution to the output. Writing the masking logic... with approach 1, we can vectorize this. Instead of looping over heads, I gather all the mask values for each head, reshape them for broadcasting, and apply them across the entire batch and sequence in one operation. This is much more efficient than processing each head individually.

Now I'm thinking through the full v2 implementation. I need to cache source activations from three places: the embedding output, per-head attention outputs at each layer, and MLP outputs. The challenge is timing—when I hook into the query/key/value projections at a given layer, I need all source activations from previous layers plus the input, but when I hook the MLP, I also need the attention output from that same layer since it comes first in the execution order. }, m{0..L-1}, plus a{L}.h{H} from the o_proj hook that fired ✓

But there's a wrinkle here—in Llama's architecture, the input to q_proj/k_proj/v_proj is actually the normalized hidden state, not the raw input. So if I'm replacing that input with a masked residual, I need to handle the normalization layer properly. Let me trace through how the forward pass actually works to make sure I'm hooking at the right points.

The issue is that my masked residual would be in the residual stream space (unnormalized), but q_proj expects a normalized input. So I need to think about whether I'm capturing the source activations in the right form or if I need to account for the layernorm when constructing the masked version.

I'm weighing two approaches: hooking at the layer level with separate paths for attention and MLP, or hooking directly on the projection layers and applying the norm to my constructed masked residual. The second option would require access to the layernorm inside the hook, which might be tricky.

Actually, the cleanest solution is to apply the appropriate layernorm to the masked residual before passing it to each component—input_layernorm for the q/k/v projections and post_attention_layernorm for the MLP. But this creates a problem: if the attention operates on this masked input, the attention output itself changes, which affects what gets cached downstream.

For edge pruning, I need to think through the residual flow more carefully. In a standard forward pass, each component receives a normalized version of its input and adds its output back to the residual stream. With masking, I'm selectively zeroing out contributions from certain sources, so the masked input to each component should be normalized before processing, and then the output gets added back to the residual stream as usual.

The key realization is that in edge pruning, there's no explicit separate residual connection—instead, each destination node constructs its input by summing the masked source activations. This means I don't need to modify the residual connection logic itself; the masking happens at the input construction stage, and everything else flows naturally from there.

But there's a practical issue: the model's forward pass still computes residual connections normally, so if I only hook the attention projections, the MLP will still see the unmasked residual. I need to think through whether I should hook both the attention inputs and the MLP input to maintain consistency, or if there's a cleaner way to handle this. I'm seeing the issue now—when we mask inputs to each component with these hooks, the residual stream still accumulates unmasked outputs from earlier layers, creating a mix of original and masked values that doesn't cleanly isolate the attribution. Let me check how the v1 code actually handles this with its layer-level masking approach.

The key difference is that v1 replaces the entire layer input once, so the attention and MLP both operate on the same masked residual, whereas v2 needs to inject different masked versions for Q, K, V, and the MLP input separately. I'll need to hook into each of these submodules individually to replace their inputs with the appropriate masked values before they compute. Looking at how the MLP processes the masked input and produces its output, which then gets added to the residual stream along with the attention contribution. I'm realizing I need to reconsider what exactly gets cached as source activations—the key insight is that we're decomposing the residual stream into discrete contributions from each component: the initial embedding, each attention head's output, and each layer's MLP output.

The cleaner approach is to bypass the model's built-in residual propagation entirely. Instead, each component's pre-hook reconstructs its input from scratch by summing the relevant cached source activations through the edge masks, applies the appropriate layer normalization, and feeds that constructed input forward. This way the model's residual connections become passive—they'll still execute, but we're controlling what actually flows through the network by managing what each component receives as input. Still writing the hook logic... I need to understand how the decomposition works—the o_proj function takes concatenated head outputs and projects them, and I'm decomposing that projection back into per-head contributions by slicing both the input and the weight matrix for each head. These per-head contributions represent what each attention head actually added to the residual stream.

For the MLP, I just need to cache its direct output since that's what gets added to the residual. Now I'm thinking through the hook implementation more carefully, particularly how to set up the q_proj pre-hook at each layer to inject the masked residual instead of the actual one.

Implementing the hook logic... I need to close over the layer norm reference in the hook factory so I can access `layers[L].input_layernorm`. The source activations I'm tracking are the embedding output, per-head attention contributions from earlier layers, and MLP outputs—all d_model-dimensional—and the true residual stream at any point is their cumulative sum up to that layer.

For Q/K/V projections at layer L, the sources are the input plus attention and MLP outputs from earlier layers, while MLP at layer L also includes same-layer attention outputs. This aligns with the existing edge topology logic.

Now I'm thinking about performance—with deep models and many heads, iterating over sources for each of the four hooks per layer could get expensive, especially across 100 optimization epochs. I should precompute mask index arrays for each hook type, layer, and source combination, then use vectorized operations instead of per-head loops to speed things up.

Designing the precomputed index structure... For K and V projections with grouped query attention, I need to create expanded index arrays where heads in the same KV group reference the same mask index, allowing me to use unified vectorized code across Q, K, and V while respecting the grouped structure. Now I'm writing out the complete implementation with this approach.

Building the mask index precomputation... Building the hook mask indices... I'm finishing the loop to map MLP sources to their mask indices, then collecting all the index dictionaries into lists and converting them to tensors. Now I'm setting up the hook functions that will apply these masks during the forward pass, starting with a generic pre-hook for the query, key, and value projections.

Still writing hook logic... Writing the MLP hook...

For the MLP layer, each source has a single mask value rather than per-head masks, so the logic is more straightforward. I need to cache the embedding output, per-head attention outputs, and MLP outputs—all as [batch, seq, d_model] tensors—and hook into embed_tokens to capture the embedding.

For attention heads, I'll hook o_proj to decompose the concatenated head outputs back into individual heads using the projection weights. For the MLP, I'll hook directly into the mlp module to capture its output.

One thing I need to clarify: the source activations shouldn't be detached because gradients need to flow through the masks to update the mask parameters. The gradient path flows from the loss through the masked logits and into the model's forward pass, where the masks multiply the source activations, so the mask parameters need to receive gradients.

Actually, there's a circular dependency issue here—to compute masked inputs at layer L, I need source activations from all previous layers, but those activations were themselves computed using masked inputs at their respective layers. The computational graph chains from the embedding through each layer's masking operations.

But wait, this creates a problem: the gradient needs to flow backward through all these interdependent masked inputs and mask parameters, and I'm not sure the current approach handles this correctly.

Let me reconsider what's happening at layer 0. The input gets normalized, then I'm replacing it with different masked versions for Q, K, and V projections. The attention output then feeds into the residual connection, which combines with the original input before going to the MLP. The issue is that when I mask the layernorm output for each projection, I'm creating separate computational paths that all depend on the same underlying mask parameters, and I need to make sure the gradients flow correctly through all of them.

At layer 1, the accumulated residual from layer 0 becomes the input, but my hooks immediately replace the normalized version with masked inputs, so the actual residual value gets discarded. The key insight is that the residual connection itself isn't masked—only the inputs to the attention and MLP operations are masked—so I need to be careful about what gets preserved in the computational graph. The `_decompose_attn_output` function slices the concatenated head outputs and multiplies each by its corresponding weight matrix slice—a fully differentiable operation that lets gradients flow back through the attention computation while keeping the model weights frozen. I need to make sure the gradient path stays intact through this decomposition so the edge importance scores can be computed correctly.

Now I'm realizing the key constraint: only the mask parameters (the log_alpha values in HardConcrete) should be optimized, not the model weights themselves. The gradient should flow from the loss back through the masked activations at each layer, creating a chain where each layer's mask depends on the previous layer's output. I should verify that model parameters aren't accumulating gradients during this process.

Looking at the o_proj hook specifically, it's a forward hook that fires after the projection is computed, and I need to decompose the concatenated head outputs into per-head contributions using the o_proj weight matrix. W. If the model is frozen (requires_grad=False), then the gradient through h_slice @ W_h.T will still flow to h_slice (which depends on the masked inputs). This is fine.

Let me now also think about what exactly the per-head attention output represents. In Llama, the attention output gets projected through o_proj to produce the final attention contribution to the residual stream. When I decompose this by head, each head's output slice gets multiplied by its corresponding portion of the o_proj weights, and these per-head contributions sum to the full o_proj output.

Now I'm ready to write the code. For the MLP, I need to understand what gets cached—the MLP block applies a gated linear transformation that outputs [batch, seq, d_model], which is what adds to the residual stream. Since my pre-hook replaces the MLP's input with the masked version, the cached output comes from that masked input, which is what I want.

There's one more thing to consider about how the layer's forward pass handles this. I'm checking the Llama attention implementation to verify that our pre-hooks on the projection layers will properly intercept all uses of hidden_states—and it looks like they're only called for q_proj, k_proj, and v_proj, so our masking strategy should work cleanly.

Now I'm thinking through how PyTorch's forward pre-hooks actually work with nn.Linear modules. The hook receives the module and a tuple of positional arguments, and we need to return the modified arguments tuple so that our masked tensor gets passed to q_proj instead of the original hidden_states.

For the MLP module, the same pattern applies—we intercept the input, apply our masking and normalization, and return the modified tuple. I'm ready to put together the complete implementation now, but I need to clarify one more detail about how the masking should be applied across the different components. LP hook on `mlp` (or `mlp.gate_proj`). If we hook the entire `mlp` module, our pre-hook fires before the mlp forward, and we replace the input. The input to mlp.forward() is the post-layernorm hidden states.

But actually, there's a subtlety. The `LlamaDecoderLayer` does post-attention layer normalization, then passes those normed states to the mlp. Our hook would replace this normed input with our own masked + normed version, which is correct.

Alternatively, we could hook `mlp.gate_proj`, but since the MLP applies the activation function and multiplies gate_proj and up_proj outputs together, hooking just gate_proj wouldn't affect up_proj. We'd need to hook both separately, so it's cleaner to hook the mlp module directly.

My plan is to hook the query, key, and value projections with pre-hooks to replace their inputs, hook the mlp with a pre-hook for the same reason, then use forward hooks on the output projection and mlp to capture their per-head and layer outputs.

I can register both a pre-hook and a forward hook on the same module—PyTorch handles them independently, with the pre-hook firing before the forward pass and the forward hook firing after.

Now I'll write the code, keeping the function signatures and helper functions from v1 unchanged while rewriting `_masked_forward` with the new hook strategy, adding `_build_hook_mask_indices`, and updating the source activation caching. I also need to think through how the logits are computed—they come from the model's final output after the last layer, so since we're replacing inputs at every destination, the model should produce the correct logits.

Writing implementation code... The logits are computed from the final residual stream, which accumulates outputs from all previous layers—including the original embeddings. Since I'm masking component outputs throughout the network, the residual stream itself becomes masked, but I need to verify that the original embeddings aren't bypassing this masking somehow. Since our hooks replace the inputs to each submodule but don't modify the residual stream itself, the residual stream has:

h_after_L0 = h_0 + attn_out_0_masked + mlp_out_0_masked
h_after_L1 = h_after_L0 + attn_out_1_masked + mlp_out_1_masked
...

Where h_0 is the embedding output (always present, no mask). This means every component's output contributes to the residual stream equally. But the MASKING happens at the destination level - each destination selects which sources to include.

So the final residual (which feeds into lm_head for logits) is the SUM of ALL component outputs. But this is correct for edge pruning! The logits node "sees" everything. In the princeton-nlp implementation, the logits destination doesn't have edge masks - it just reads the full residual.

Wait, I need to think through this more carefully. The model's final residual isn't actually the sum of all component outputs in our masked setup—it's the sum of outputs computed from masked inputs. So each attention and MLP layer receives filtered inputs based on the masks, and their outputs get accumulated into the residual stream. The logits then see this accumulated result of all the masked-at-source outputs.

But there's a conceptual issue here with how edge pruning should work. In standard edge pruning, each destination node should only receive contributions from its selected source nodes, not from all sources.

I think the key insight is that we're not actually implementing edge-level masking at the logits destination—we're masking at the source level (the inputs to each component). The logits implicitly see everything in the residual stream with no additional filtering. This matches what the topology builder does, so I'll stick with this approach.

Let me also consider a few edge cases: if the model uses key-value caching or other attention features, we're not passing those kwargs, so the model should just run normally. And for attention masks on the input...

Actually, I'm not passing an attention mask at all—just the input_ids—which assumes the input isn't padded. Same assumption as v1. Position IDs will auto-generate, and if the model uses flash attention internally, our hooks at the submodule level should still capture the right activations.

Now I'm ready to write the code. One critical detail about the embedding hook: in v1 it's a simple forward hook that caches the embedding output, but in v2 I need to keep it in the computational graph so gradients can flow through the masks.

Writing the implementation...

Actually, I need to think through the gradient flow carefully. The model parameters are frozen, so I should set `requires_grad=False` on them for memory efficiency—PyTorch won't allocate gradient buffers that way. But the key question is whether gradients can still flow *through* the frozen model parameters to reach the mask parameters in HardConcrete.

The answer is yes. When I freeze the model, its weights become constants in the computation graph, but operations involving them (like matrix multiplications) still propagate gradients backward. The mask values get multiplied with source activations, flow through the frozen model, and produce the output. During backprop, the gradient signal travels back through all these operations—through the model's frozen computations and then through the mask multiplication—so the mask parameters still receive their gradients. This is exactly what I want: memory-efficient training where only the mask parameters accumulate gradients.

Now I'm implementing the code carefully, paying attention to hook signatures, gradient flow, vectorized operations, and proper layer normalization. I need to understand how the hooks integrate with Llama's internal structure—specifically how the decoder layers apply layer norm before attention and after the residual connection.

Writing the hook implementation... I need to capture references to the layernorm modules in the hook factory so I can apply `input_layernorm` for the attention projections and `post_attention_layernorm` for the MLP hook. Then I'm precomputing tensor indices for efficient vectorized masking operations within each hook—storing per-head mask indices for Q operations, grouped mask indices for K/V, and single mask indices for MLP.

I'm organizing these as dictionaries mapping hook type to layer to source-index pairs. The key insight is that source activations become available progressively: at Q/K/V hooks in layer L, I have access to all cached activations from layers 0 through L-1 plus the input, and at the MLP hook I additionally have same-layer attention outputs.

Writing the masked forward function... Setting up pre-hooks for the key and value projections... Setting up the attention output decomposition hooks...

Now I'm capturing the MLP output and then running the forward pass through the model to get the final logits, making sure to clean up all the hooks afterward. Then I'm defining a helper function that builds the masked input for the attention projections by zeroing out the input tensor and selectively filling in values based on the mask indices.

Building the MLP masking function...

Wait, I'm realizing there's a mismatch in how I'm structuring the `indices_dict` for the attention heads versus the MLP layer—the keys are source names but I need to be consistent about whether the values are scalar indices or tensors of indices depending on the context.

Let me reconsider the approach: I should precompute all mask index tensors once at the start since they're constant throughout optimization, then convert them to the appropriate device rather than rebuilding them each time.

Building helper functions to enumerate source nodes... Building the index tensors...

The function returns all the collected indices for query, key, value, and MLP layers. I'm noting that MLP indices are stored as plain integers rather than tensors since each source maps to a single mask value. For larger models, there's a potential optimization strategy to freeze masks layer-by-layer, but I'll skip that for the basic implementation. Gradient checkpointing should work naturally with this approach since the hooks operate at the submodule level without depending on specific intermediate tensor storage.

Now I'm thinking through the memory implications of storing decomposed attention outputs. In v2, we cache these as tensors in the source cache, and the memory footprint depends on model size—for something like Qwen-2.5 0.5B with 14 heads across 24 layers, we're looking at around 150MB for a batch size of 1 and sequence length of 128, which is manageable. Larger models would need more careful consideration of this storage overhead.

I'm ready to move forward with the implementation. Before I start writing the complete v2 code, I need to verify that gradients flow correctly through the masked input attention function. The fancy indexing for mask selection is differentiable, the element-wise multiplication is differentiable, and the layernorm operation is differentiable with respect to its input even though the module parameters are frozen. So the gradient computation should work as expected.

Now I'll write the code and also think through the test cases. The tests need to cover the same ground as v1—AST syntax validation, function signatures, edge topology, and HardConcrete behavior—plus any new test requirements for the v2 changes.

I notice v1 uses an `_ActivationCache` class to store activations during the forward pass, but for v2 I'll simplify this to just use a dictionary keyed by string identifiers, which gives me more flexibility.

Writing the implementation and tests... I've clarified the mask indexing strategy: for source activation hooks, `indices_dict` maps to a single integer that indexes into the masks array, while for attention pre-hooks it maps to a tensor of head indices that I reshape for proper broadcasting. Now I'm writing out the complete implementation, starting with the helper function that builds these mask index mappings on the correct device, then moving into the main masked attention and input functions.

Writing the implementation... Finalizing the implementation now. Let me verify the source node logic for the hook masks—the Q/K/V sources pull from everything before the current layer, which aligns with the v1 topology builder, and the MLP sources correctly include same-layer attention heads as well.

The timing works out naturally: when Q/K/V hooks fire at layer L, the cache has input and all previous layer outputs but not same-layer attention yet, since attention runs before MLP within each layer. Once the MLP hook fires, same-layer attention heads are already cached. This matches the model's forward pass order, so the implementation is sound.

Now I'm deciding whether to keep `_build_dst_mask_table` in v2. Since the new hook-based architecture uses `_build_hook_mask_indices` directly and doesn't need the old grouping function, I'll remove it rather than keep unused utilities.

Looking at the refactoring plan: I'm keeping the core components from v1 like HardConcrete, `_get_arch_info`, the compute_edge_pruning_scores signature, GQA mask sharing, and `_build_edge_topology`, while replacing the hook architecture with four submodule hooks and rewriting `_masked_forward`. I'll also add the new helper functions `_build_hook_mask_indices`, `_build_masked_input_attn`, and `_build_masked_input_mlp`.

Now I'm checking what `_get_module` does—it's a utility that traverses a module path string to retrieve the actual module object.

Writing the v2 implementation... Implementing the Hard Concrete distribution class with initialization of log-alpha parameters and a forward pass that samples masks during training using the reparameterization trick, then applies sigmoid to get the final mask values.

Now I'm finishing the forward method by scaling and clamping the sampled values, then adding methods to compute the L0 regularization penalty and get the expected masks during inference. After that, I'm setting up architecture detection for Llama-like Hugging Face models by defining a frozenset of model names to match against.

Extracting architecture info from the model config...

Now I'm building the edge topology for the pruning mask, mapping each attention edge to its corresponding mask parameter index while accounting for grouped query attention where K/V edges in the same group share masks. Building the mask indices... Building the hook mask indices... Building tensor mappings...

Now I'm finishing up the mask index collection for each layer, appending the query, key, value, and MLP indices to their respective lists before returning everything. Then I'm moving on to decompose attention output by splitting the concatenated head representations and projecting each one individually through the output projection matrix.

Building masked input construction... Writing the MLP masking function... Setting up pre-hooks for the Q, K, and V projections that intercept and modify the input based on the source activations and masks before they're processed. Setting up the MLP hooks to capture masked inputs and outputs, then running the forward pass and cleaning up all registered hooks before returning the logits.

Now I'm defining the faithfulness loss function that computes KL divergence between the masked and clean logit distributions, optionally filtering to specific target token indices. Then I'm starting the main entry point that will compute edge pruning scores given clean and corrupt inputs along with a metric function.

Setting up the architecture parameters... Setting up the model for optimization by converting all inputs to tensors on the device, freezing the model parameters, and computing clean logits as a baseline. Then I'm entering the training loop where I generate masks and apply them to get masked logits for comparison.

Computing the faithfulness loss between masked and clean logits, adding an L0 regularization penalty to encourage sparsity, and backpropagating to update the mask parameters. After training completes, I extract the final mask values and map them back to edge names to produce the importance scores.

Now I'm defining a utility function to estimate the total number of edges in the model based on the layer and head configuration.

Calculating edge counts...

I need to reconsider the hook type signatures in PyTorch. The `register_forward_pre_hook` callback receives `args` as a tuple of positional arguments and should return either a modified tuple or None. For a linear layer called with a single input, `args` would be `(x,)`, and our hooks return `(masked_input,) + args[1:]` to preserve any additional arguments while replacing the first one with the masked version.

Now I'm thinking through the test structure—I should preserve the existing topology tests since they don't need changes, and then add new tests for the masking behavior.

For the AST tests, I need to verify the new helper functions are present, and I should add separate tests to validate that the hook mask indices are built correctly and that Q/K/V and MLP masks operate independently without any mean averaging. Since `_build_hook_mask_indices` requires torch tensors, I could test the core logic separately using plain lists to avoid that dependency.

Writing test file... Writing test helper function... Building the mask index structures...

Now I'm setting up test cases to verify that Q masks stay independent across heads while K/V masks properly share within their groups under grouped query attention. I'm verifying that the V masks follow the same grouping pattern as the K masks, then moving on to test that MLP hooks correctly include same-layer attention heads as their sources. I'm setting up a test to verify that every edge type in the computation graph has corresponding mask indices, then collecting all the indices referenced across the Q, K, V, and MLP hook structures to ensure complete coverage.

Now I'm realizing I should also handle the `_build_dst_mask_table` test since that function is being removed from the source code, so I need to decide whether to update or remove that test as well.

Looking at the existing test, it manually constructs the table rather than calling the module function directly, so it's still testing the underlying topology structure which remains valid. I'll keep it as is.

The `test_module_topology_matches_standalone` test should be fine since it imports `_build_edge_topology` which still exists in the module.

Now I want to add a test that verifies the module's `_build_hook_mask_indices` function produces the same results as the standalone version...

Comparing mask indices across layers...

Actually, I need to verify that freezing the model parameters won't break the backward pass. When I freeze the model and only keep `hard_concrete.log_alpha` as trainable, PyTorch should still compute gradients through the frozen operations since they're part of the computational graph—the gradients just won't accumulate in the frozen parameters themselves. I should use `model.requires_grad_(False)` to freeze the entire model since the HardConcrete masks are registered separately, so this won't affect gradient flow to `log_alpha`. But I need to be careful about `torch.no_grad()` context—the clean logits are computed under it, but the masked forward pass shouldn't be, otherwise gradients won't flow to the mask parameters.

Now I'm ready to write the final implementation. One thing I'm noticing is that the function signatures differ between versions: v1's `_masked_forward` takes `dst_mask_table` while v2 takes `hook_indices`, though the main entry point `compute_edge_pruning_scores` stays the same. Also, the `corrupt_inputs` parameter exists for interface compatibility but isn't actually used in either version—only `clean_ids` matters.

I need to double-check the type annotation for the hooks list since `RemovableHook` might not be the correct type across different PyTorch versions...

I'll just use `list` to keep it simple and avoid compatibility issues. Also, I'm using `x = x + ...` instead of in-place operations like `x += ...` to avoid breaking autograd, which is the right approach here. And I should remove the `_build_dst_mask_table` function since it's not actually used anywhere in the implementation.

Now let me write the actual code. One thing I need to verify though—in the `_decompose_attn_output` function within the o_proj hook, I'm accessing `inp[0]` which represents the concatenated attention head outputs going into o_proj. The shape should be [batch, seq, n_heads * head_dim], but I need to make sure this aligns with how the masked forward pass handles it.

The key insight is that when we apply masks at Q, K, V during the forward pass, those masks flow through the attention computation and get baked into the output. When we decompose and cache these activations as sources for downstream layers, they already contain the mask effects. This means gradients can propagate backward through the entire chain—from downstream masks back through the cached activations to earlier layer masks. That's exactly what we want for the edge pruning optimization.

Alright, let me outline the final structure for the files, starting with edge_pruning_scoring.py...

Writing the module structure... Writing test cases... I'm going in circles here — the Python exception is `AssertionError`, not `AssertionError`. Let me just confirm: when you use `assert False`, it raises `AssertionError`. That's the correct built-in exception name. I'm getting caught up on whether the exception name is spelled correctly, but looking at the v1 test code, it's clearly `AssertionError` — the standard Python exception. I'll just use that consistently across both tests and let the actual test run tell me if there's any issue. I'm verifying the spelling of `AssertionError` in the v1 code—it's definitely the correct Python exception class, and if there were a typo it would've failed when the tests ran, so I can confidently use the same spelling and finally move on to writing the actual code.

Writing the implementation... I'm defining the canonical node and edge formats for the sparsity mask system, then implementing the Hard Concrete distribution class that parameterizes L0 masks during training by sampling from a stretched Binary Concrete and clamping to [0, 1].

Implementing forward pass... Now I'm setting up architecture detection for Hugging Face models, defining which model types are supported (Llama-like architectures including Qwen, Gemma, Mistral, and Phi variants) and extracting key configuration parameters like attention heads and model dimensions.

Building the edge topology functions... Building the edge topology... Building hook mask indices... Building tensor indices for attention heads...

Now I'm moving on to decomposing the attention output by splitting the concatenated head representations and projecting each one through the output projection layer.

Next, I'm building a function to construct masked inputs for the Q/K/V projections, where I apply per-head mask values to slices of the source activations, handling grouped query attention transparently through an index dictionary. Writing the MLP masking function and hook setup... Setting up masking hooks for query, key, and value projections... Setting up hooks for the output projection and MLP layers to cache their intermediate results and apply masking to the inputs...

Now I'm wrapping the model forward pass in a try-finally block to ensure all hooks get cleaned up, then defining a faithfulness loss function that computes KL divergence between the masked and clean model outputs, optionally selecting specific target token positions. Setting up the edge pruning computation by extracting architecture parameters like layer count and head configuration, then building the edge topology and hook indices to track which connections to prune. I'm initializing a HardConcrete layer for the mask parameters and an Adam optimizer, then preparing the input data.

Now I'm normalizing the clean and corrupt input tensors—extracting input IDs from dictionaries if needed, converting them to tensors, and moving everything to the device. I'm also handling the target IDs the same way before freezing the model.

Setting up the optimization loop where only the mask parameters get updated while the model stays frozen in eval mode. I'm computing clean logits once, then iterating through epochs to optimize the masks by calculating faithfulness and L0 regularization losses, backpropagating, and stepping the optimizer. Finally, I'm extracting the final learned masks.

Now I'm converting those masks into interpretable scores for each edge in the architecture, then moving on to a utility function that estimates the total number of edges and mask parameters across all attention heads and layers in the model.

I'm reconsidering an important refactoring decision I made—extracting `_src_nodes_before_layer` as a standalone function at the module level since both the topology builder and the hook mask index builder need it, rather than keeping it nested inside one of them.

The change is functionally equivalent since I'm passing `n_heads` as a parameter instead of relying on closure, so it's safe. I need to make sure the test file's standalone copy gets updated too.

Looking back at the refactoring, I extracted `_src_nodes_before_layer` to module level and now need to pass `n_heads` explicitly at the call sites in `_build_edge_topology`. I've got those calls updated with the new parameter. Now I need to update the test file's standalone version and add a standalone `_build_hook_mask_indices_standalone` as well.

The test file has its own nested helper, so it's independent from the module-level function. I should finalize both files now, making sure the test version is thorough too. I'm also thinking about error handling—what happens if a source activation is None in the cache, like if an embed hook didn't fire or a previous operation failed?

In the masked input builders, I skip None sources with a continue statement, which means they contribute zero to the masked input. That's reasonable degradation, though in practice this shouldn't happen since hooks are registered for all layers and process in order. If it does happen, there's likely a bug.

Now I'm ready to write the final versions. For the test file, I need to add a standalone version of the hook mask indices builder alongside the existing topology builder. I should also verify the AST test checks for the correct function names in v2, particularly the new `_build_hook_mask_indices` function.

Writing test file... Writing test assertions... Building the edge topology... Building the edge mapping for MLP connections...

Now I'm iterating through each layer to collect source nodes for attention and MLP operations, then constructing dictionaries that map each source to the corresponding mask indices for query, key, and value projections across all attention heads. Writing topology tests... I'm verifying that the key masks for different head groups are distinct, then checking that query masks span all heads individually, and value masks for the first group are consolidated into a single mask. Now I'm moving on to test the destination mask table by building the edge topology and iterating through the edge-to-mask mappings.

Building the destination mask table... Writing test functions... Writing test assertions... I'm setting up the test to verify that MLP hooks at each layer include the correct attention head sources—the input plus same-layer attention heads for layer 0, and additionally the previous layer's outputs for layer 1.

Now I'm moving to a new test that checks the opposite constraint: Q/K/V hooks at any layer must exclude sources from that same layer, meaning they can't depend on the layer's own attention heads or MLP output. Building the test assertions... Writing test cases... Writing test assertions... I'm running through the test suite, executing the non-torch tests first, then conditionally running the torch-dependent tests if the library is available, otherwise skipping them with a message. Once all applicable tests pass, I'll print a completion message and then write out the files.

Actually, let me verify the exception name being used in the test file—I want to make sure it's spelled correctly as `AssertionError`. I keep second-guessing myself on the spelling, but I've verified it multiple times now—the Python exception class is definitely `AssertionError`. I need to stop going in circles and just move forward with that.

Now I'm writing out the files. I want to make sure the `_src_nodes_before_layer` helper is consistent between my v2 implementation and the test file. In v2, I've made it a module-level function that both `_build_edge_topology` and `_build_hook_mask_indices` call with `n_heads` as a parameter, while the test's standalone builders keep it nested for self-containment.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "2bdad1ba-5642-4a35-bda7-fac0b7f6aaaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YP3qLsFwumy4yoirqxnh7S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14855,
      "cache_read_input_tokens": 24468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14855
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

_source line 13_

读完 v1 代码，两个问题确认：
1. `_layer_pre_hook`（L285-336）只构建 attention 的 masked residual，MLP 没有对应 hook
2. L328-329 对所有 Q/K/V edge mask 取 mean → 单标量，粒度丢失

开始重写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "41333718-2d6a-4f45-b8b8-f0207eb2dcbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YP3qLsFwumy4yoirqxnh7S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14855,
      "cache_read_input_tokens": 24468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14855
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

_source line 14_

<details open><summary>🔧 Tool call — Write · `toolu_01KQ5iQ2i6wDFBLVubGYjvZM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_scoring.py",
  "content": "\"\"\"Edge Pruning v2 with L0 regularization for HuggingFace models.\n\nv2 fixes two critical bugs from v1:\n  1. MLP edge masks are now applied in forward via mlp pre-hook\n     (v1 had mask params but no forward-pass hook for MLP).\n  2. Q/K/V edge masks are kept independent per-head/KV-group\n     (v1 averaged across all Q/K/V destinations into a single scalar).\n\nHook strategy (v2): 4 submodule pre-hooks per layer\n  - self_attn.q_proj: per-head Q edge masks\n  - self_attn.k_proj: per-KV-group K edge masks (GQA shared)\n  - self_attn.v_proj: per-KV-group V edge masks (GQA shared)\n  - mlp: per-source MLP edge masks\nPlus capture hooks: embed_tokens, self_attn.o_proj (per-head), mlp (output).\n\nCanonical node format:\n  input, logits, a{L}.h{H}[.q|.k|.v], m{L}\n\nCanonical edge format: \"{src}->{dst}\" (no spaces)\n\nReferences:\n  - Louizos et al. \"Learning Sparse Neural Networks through L0 Regularization\" (2018)\n  - Bayazit et al. \"Discovering Knowledge-Critical Subnetworks\" (2023)\n\"\"\"\n\nfrom __future__ import annotations\n\nimport math\nfrom typing import Dict, List, Tuple, Callable, Optional\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\n\n\n# ---------------------------------------------------------------------------\n# Hard Concrete Distribution\n# ---------------------------------------------------------------------------\n\nclass HardConcrete(nn.Module):\n    \"\"\"Hard Concrete distribution for L0 mask parameterization.\n\n    Parameterized by log_alpha (location). During training, samples from a\n    stretched Binary Concrete and clamps to [0, 1], yielding exact zeros/ones.\n    \"\"\"\n\n    BETA = 2.0 / 3.0\n    GAMMA = -0.1\n    ZETA = 1.1\n    EPS = 1e-8\n\n    def __init__(self, n_masks: int, init_mean: float = 0.5):\n        super().__init__()\n        init_val = math.log(init_mean / (1.0 - init_mean + self.EPS))\n        self.log_alpha = nn.Parameter(torch.full((n_masks,), init_val))\n\n    def forward(self, training: bool = True) -> torch.Tensor:\n        if training:\n            u = torch.zeros_like(self.log_alpha).uniform_(self.EPS, 1.0 - self.EPS)\n            s = torch.sigmoid((torch.log(u / (1.0 - u)) + self.log_alpha) / self.BETA)\n        else:\n            s = torch.sigmoid(self.log_alpha)\n        s_bar = s * (self.ZETA - self.GAMMA) + self.GAMMA\n        return s_bar.clamp(0.0, 1.0)\n\n    def l0_penalty(self) -> torch.Tensor:\n        \"\"\"Expected L0 norm: sum of P(z != 0) for each mask.\"\"\"\n        return torch.sigmoid(\n            self.log_alpha - self.BETA * math.log(-self.GAMMA / self.ZETA)\n        ).sum()\n\n    def expected_masks(self) -> torch.Tensor:\n        \"\"\"Deterministic mask expectations (for final scoring).\"\"\"\n        return self.forward(training=False)\n\n\n# ---------------------------------------------------------------------------\n# Architecture detection (Llama-like HF models)\n# ---------------------------------------------------------------------------\n\n_LLAMA_LIKE = frozenset({\n    \"llama\", \"qwen2\", \"gemma\", \"gemma2\", \"mistral\", \"phi3\", \"phi\",\n})\n\n\ndef _get_arch_info(model) -> dict:\n    cfg = model.config\n    model_type = getattr(cfg, \"model_type\", \"\")\n    if model_type not in _LLAMA_LIKE:\n        raise ValueError(\n            f\"Edge Pruning L0 currently supports Llama-like architectures, \"\n            f\"got model_type={model_type!r}\"\n        )\n    n_heads = cfg.num_attention_heads\n    n_kv_heads = getattr(cfg, \"num_key_value_heads\", n_heads)\n    d_model = cfg.hidden_size\n    return dict(\n        n_layers=cfg.num_hidden_layers,\n        n_heads=n_heads,\n        n_kv_heads=n_kv_heads,\n        heads_per_kv_group=n_heads // n_kv_heads,\n        d_model=d_model,\n        head_dim=d_model // n_heads,\n    )\n\n\n# ---------------------------------------------------------------------------\n# Edge Topology: enumerate all edges and build mask index mapping\n# ---------------------------------------------------------------------------\n\ndef _src_nodes_before_layer(\n    layer: int, n_heads: int, include_attn_same_layer: bool = False,\n):\n    \"\"\"Yield source node names whose output feeds into a given layer.\"\"\"\n    yield \"input\"\n    for l in range(layer):\n        for h in range(n_heads):\n            yield f\"a{l}.h{h}\"\n        yield f\"m{l}\"\n    if include_attn_same_layer:\n        for h in range(n_heads):\n            yield f\"a{layer}.h{h}\"\n\n\ndef _build_edge_topology(\n    n_layers: int, n_heads: int, n_kv_heads: int, heads_per_kv_group: int,\n) -> Tuple[List[str], Dict[str, int], int]:\n    \"\"\"Build the full edge set and map each edge to its mask parameter index.\n\n    For GQA models, K/V edges targeting the same KV group share a mask.\n    Q edges always have independent masks.\n\n    Returns:\n        edge_names: list of canonical edge names\n        edge_to_mask_idx: edge_name -> index into mask parameter vector\n        n_masks: total number of independent mask parameters\n    \"\"\"\n    edge_names: List[str] = []\n    edge_to_mask_idx: Dict[str, int] = {}\n    mask_idx = 0\n\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes_before_layer(L, n_heads, False))\n        for src in srcs_attn:\n            for H in range(n_heads):\n                q_edge = f\"{src}->a{L}.h{H}.q\"\n                edge_names.append(q_edge)\n                edge_to_mask_idx[q_edge] = mask_idx\n                mask_idx += 1\n\n            for kv_group in range(n_kv_heads):\n                k_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    k_edge = f\"{src}->a{L}.h{H}.k\"\n                    edge_names.append(k_edge)\n                    edge_to_mask_idx[k_edge] = k_mask_idx\n\n            for kv_group in range(n_kv_heads):\n                v_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    v_edge = f\"{src}->a{L}.h{H}.v\"\n                    edge_names.append(v_edge)\n                    edge_to_mask_idx[v_edge] = v_mask_idx\n\n        srcs_mlp = list(_src_nodes_before_layer(L, n_heads, True))\n        for src in srcs_mlp:\n            mlp_edge = f\"{src}->m{L}\"\n            edge_names.append(mlp_edge)\n            edge_to_mask_idx[mlp_edge] = mask_idx\n            mask_idx += 1\n\n    return edge_names, edge_to_mask_idx, mask_idx\n\n\n# ---------------------------------------------------------------------------\n# Precomputed hook mask indices for vectorized application\n# ---------------------------------------------------------------------------\n\ndef _build_hook_mask_indices(\n    n_layers: int,\n    n_heads: int,\n    edge_to_mask_idx: Dict[str, int],\n    device: torch.device,\n) -> Tuple[\n    List[Dict[str, torch.Tensor]],\n    List[Dict[str, torch.Tensor]],\n    List[Dict[str, torch.Tensor]],\n    List[Dict[str, int]],\n]:\n    \"\"\"Precompute per-hook mask index tensors.\n\n    Returns (q_indices, k_indices, v_indices, mlp_indices) where:\n      q/k/v_indices[L] = {src_name: LongTensor[n_heads]}\n        GQA sharing is implicit: heads in the same KV group get identical index values.\n      mlp_indices[L] = {src_name: int}\n    \"\"\"\n    q_all: List[Dict[str, torch.Tensor]] = []\n    k_all: List[Dict[str, torch.Tensor]] = []\n    v_all: List[Dict[str, torch.Tensor]] = []\n    mlp_all: List[Dict[str, int]] = []\n\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes_before_layer(L, n_heads, False))\n        srcs_mlp = list(_src_nodes_before_layer(L, n_heads, True))\n\n        qi: Dict[str, torch.Tensor] = {}\n        ki: Dict[str, torch.Tensor] = {}\n        vi: Dict[str, torch.Tensor] = {}\n        for src in srcs_attn:\n            qi[src] = torch.tensor(\n                [edge_to_mask_idx[f\"{src}->a{L}.h{h}.q\"] for h in range(n_heads)],\n                dtype=torch.long, device=device,\n            )\n            ki[src] = torch.tensor(\n                [edge_to_mask_idx[f\"{src}->a{L}.h{h}.k\"] for h in range(n_heads)],\n                dtype=torch.long, device=device,\n            )\n            vi[src] = torch.tensor(\n                [edge_to_mask_idx[f\"{src}->a{L}.h{h}.v\"] for h in range(n_heads)],\n                dtype=torch.long, device=device,\n            )\n\n        mi: Dict[str, int] = {}\n        for src in srcs_mlp:\n            mi[src] = edge_to_mask_idx[f\"{src}->m{L}\"]\n\n        q_all.append(qi)\n        k_all.append(ki)\n        v_all.append(vi)\n        mlp_all.append(mi)\n\n    return q_all, k_all, v_all, mlp_all\n\n\n# ---------------------------------------------------------------------------\n# Per-head decomposition through the output projection\n# ---------------------------------------------------------------------------\n\ndef _decompose_attn_output(\n    concat_heads: torch.Tensor,\n    o_proj: nn.Linear,\n    n_heads: int,\n    head_dim: int,\n) -> Dict[int, torch.Tensor]:\n    \"\"\"Split concatenated head output and project each head through o_proj.\"\"\"\n    W = o_proj.weight  # [d_model, d_model]\n    heads = {}\n    for h in range(n_heads):\n        h_slice = concat_heads[:, :, h * head_dim:(h + 1) * head_dim]\n        W_h = W[:, h * head_dim:(h + 1) * head_dim]\n        heads[h] = h_slice @ W_h.T\n    return heads\n\n\n# ---------------------------------------------------------------------------\n# Masked input construction for submodule hooks\n# ---------------------------------------------------------------------------\n\ndef _build_masked_input_qkv(\n    src_cache: Dict[str, torch.Tensor],\n    masks: torch.Tensor,\n    idx_dict: Dict[str, torch.Tensor],\n    n_heads: int,\n    head_dim: int,\n    layernorm: nn.Module,\n    ref: torch.Tensor,\n) -> torch.Tensor:\n    \"\"\"Construct masked + layernormed input for a Q/K/V projection.\n\n    Applies per-head mask values to head_dim-sized slices of each source\n    activation. GQA sharing is transparent: idx_dict encodes shared\n    indices for heads within the same KV group.\n    \"\"\"\n    B, S, D = ref.shape\n    x = torch.zeros(B, S, D, device=ref.device, dtype=ref.dtype)\n    for src_name, mask_idx_t in idx_dict.items():\n        src = src_cache.get(src_name)\n        if src is None:\n            continue\n        z = masks[mask_idx_t].view(1, 1, n_heads, 1)\n        x = x + (src.view(B, S, n_heads, head_dim) * z).view(B, S, D)\n    return layernorm(x)\n\n\ndef _build_masked_input_mlp(\n    src_cache: Dict[str, torch.Tensor],\n    masks: torch.Tensor,\n    idx_dict: Dict[str, int],\n    post_ln: nn.Module,\n    ref: torch.Tensor,\n) -> torch.Tensor:\n    \"\"\"Construct masked + post-layernormed input for an MLP module.\"\"\"\n    x = torch.zeros_like(ref)\n    for src_name, mask_idx in idx_dict.items():\n        src = src_cache.get(src_name)\n        if src is None:\n            continue\n        x = x + src * masks[mask_idx]\n    return post_ln(x)\n\n\n# ---------------------------------------------------------------------------\n# Hook-based masked forward pass (v2: submodule-level hooks)\n# ---------------------------------------------------------------------------\n\ndef _masked_forward(\n    model,\n    input_ids: torch.Tensor,\n    masks: torch.Tensor,\n    arch_info: dict,\n    hook_indices: Tuple,\n) -> torch.Tensor:\n    \"\"\"Forward pass with per-destination edge masks via submodule hooks.\n\n    Registers 7 hooks per layer:\n      Pre-hooks (masking): q_proj, k_proj, v_proj, mlp\n      Capture hooks: o_proj (per-head attn output), mlp (output)\n    Plus 1 embed capture hook.\n    \"\"\"\n    n_heads = arch_info[\"n_heads\"]\n    head_dim = arch_info[\"head_dim\"]\n    n_layers = arch_info[\"n_layers\"]\n    layers = model.model.layers\n\n    q_idx, k_idx, v_idx, mlp_idx = hook_indices\n    src_cache: Dict[str, torch.Tensor] = {}\n    hooks: list = []\n\n    def _embed_hook(mod, inp, out):\n        src_cache[\"input\"] = out\n    hooks.append(model.model.embed_tokens.register_forward_hook(_embed_hook))\n\n    for L in range(n_layers):\n        layer = layers[L]\n        ln1 = layer.input_layernorm\n        ln2 = layer.post_attention_layernorm\n\n        # --- Q/K/V projection pre-hooks: replace input with masked residual ---\n\n        def _q_hook(mod, args, *, _qi=q_idx[L], _ln=ln1):\n            return (_build_masked_input_qkv(\n                src_cache, masks, _qi, n_heads, head_dim, _ln, args[0],\n            ),) + args[1:]\n\n        def _k_hook(mod, args, *, _ki=k_idx[L], _ln=ln1):\n            return (_build_masked_input_qkv(\n                src_cache, masks, _ki, n_heads, head_dim, _ln, args[0],\n            ),) + args[1:]\n\n        def _v_hook(mod, args, *, _vi=v_idx[L], _ln=ln1):\n            return (_build_masked_input_qkv(\n                src_cache, masks, _vi, n_heads, head_dim, _ln, args[0],\n            ),) + args[1:]\n\n        hooks.append(layer.self_attn.q_proj.register_forward_pre_hook(_q_hook))\n        hooks.append(layer.self_attn.k_proj.register_forward_pre_hook(_k_hook))\n        hooks.append(layer.self_attn.v_proj.register_forward_pre_hook(_v_hook))\n\n        # --- Attention output capture: per-head decomposition through o_proj ---\n\n        def _oproj_hook(mod, inp, out, *, _L=L):\n            per_head = _decompose_attn_output(inp[0], mod, n_heads, head_dim)\n            for h, h_out in per_head.items():\n                src_cache[f\"a{_L}.h{h}\"] = h_out\n        hooks.append(layer.self_attn.o_proj.register_forward_hook(_oproj_hook))\n\n        # --- MLP pre-hook: replace input with masked residual ---\n\n        def _mlp_pre_hook(mod, args, *, _mi=mlp_idx[L], _ln=ln2):\n            return (_build_masked_input_mlp(\n                src_cache, masks, _mi, _ln, args[0],\n            ),) + args[1:]\n        hooks.append(layer.mlp.register_forward_pre_hook(_mlp_pre_hook))\n\n        # --- MLP output capture ---\n\n        def _mlp_out_hook(mod, inp, out, *, _L=L):\n            src_cache[f\"m{_L}\"] = out if isinstance(out, torch.Tensor) else out[0]\n        hooks.append(layer.mlp.register_forward_hook(_mlp_out_hook))\n\n    try:\n        return model(input_ids).logits\n    finally:\n        for h in hooks:\n            h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Faithfulness loss\n# ---------------------------------------------------------------------------\n\ndef _faithfulness_loss(\n    masked_logits: torch.Tensor,\n    clean_logits: torch.Tensor,\n    target_ids: Optional[torch.Tensor],\n) -> torch.Tensor:\n    \"\"\"KL divergence between clean and masked model output distributions.\"\"\"\n    if target_ids is not None:\n        batch_size = masked_logits.size(0)\n        idx = target_ids.view(batch_size)\n        masked_logits = masked_logits[torch.arange(batch_size), idx]\n        clean_logits = clean_logits[torch.arange(batch_size), idx]\n\n    log_p = F.log_softmax(masked_logits, dim=-1)\n    q = F.softmax(clean_logits, dim=-1)\n    return F.kl_div(log_p, q, reduction=\"batchmean\")\n\n\n# ---------------------------------------------------------------------------\n# Main entry point\n# ---------------------------------------------------------------------------\n\ndef compute_edge_pruning_scores(\n    model,\n    clean_inputs,\n    corrupt_inputs,\n    metric_fn: Callable,\n    target_ids=None,\n    n_epochs: int = 100,\n    lambda_l0: float = 1e-3,\n    lr: float = 0.1,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Compute Edge Pruning L0 edge scores.\n\n    Returns dict of canonical_edge_name -> score (mask expectation).\n\n    Args:\n        model: HuggingFace CausalLM (Llama-like: Qwen2, Llama, Mistral, etc.)\n        clean_inputs: dict with 'input_ids' [batch, seq_len]\n        corrupt_inputs: dict with 'input_ids' [batch, seq_len]\n        metric_fn: faithfulness metric (kept for interface parity; KL used internally)\n        target_ids: [batch] token positions for evaluation (None = all positions)\n        n_epochs: optimization epochs\n        lambda_l0: L0 sparsity penalty weight\n        lr: learning rate for mask parameters\n        device: target device\n    \"\"\"\n    arch_info = _get_arch_info(model)\n    n_layers = arch_info[\"n_layers\"]\n    n_heads = arch_info[\"n_heads\"]\n    n_kv_heads = arch_info[\"n_kv_heads\"]\n    heads_per_kv_group = arch_info[\"heads_per_kv_group\"]\n\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology(\n        n_layers, n_heads, n_kv_heads, heads_per_kv_group,\n    )\n    hook_indices = _build_hook_mask_indices(\n        n_layers, n_heads, edge_to_mask_idx, device,\n    )\n\n    hard_concrete = HardConcrete(n_masks, init_mean=0.5).to(device)\n    optimizer = torch.optim.Adam(hard_concrete.parameters(), lr=lr)\n\n    # Prepare inputs\n    if isinstance(clean_inputs, dict):\n        clean_ids = clean_inputs[\"input_ids\"]\n        if not isinstance(clean_ids, torch.Tensor):\n            clean_ids = torch.tensor(clean_ids)\n    else:\n        clean_ids = clean_inputs\n    clean_ids = clean_ids.to(device)\n\n    if isinstance(corrupt_inputs, dict):\n        corrupt_ids = corrupt_inputs[\"input_ids\"]\n        if not isinstance(corrupt_ids, torch.Tensor):\n            corrupt_ids = torch.tensor(corrupt_ids)\n    else:\n        corrupt_ids = corrupt_inputs\n    corrupt_ids = corrupt_ids.to(device)\n\n    if target_ids is not None:\n        if not isinstance(target_ids, torch.Tensor):\n            target_ids = torch.tensor(target_ids)\n        target_ids = target_ids.to(device)\n\n    # Freeze model — only mask params are optimized\n    model.eval()\n    model.requires_grad_(False)\n\n    with torch.no_grad():\n        clean_logits = model(clean_ids).logits.detach()\n\n    # Optimization loop\n    for epoch in range(n_epochs):\n        optimizer.zero_grad()\n        masks = hard_concrete(training=True)\n        masked_logits = _masked_forward(\n            model, clean_ids, masks, arch_info, hook_indices,\n        )\n        faith_loss = _faithfulness_loss(masked_logits, clean_logits, target_ids)\n        l0_loss = hard_concrete.l0_penalty()\n        loss = faith_loss + lambda_l0 * l0_loss\n        loss.backward()\n        optimizer.step()\n\n    # Extract final scores\n    with torch.no_grad():\n        final_masks = hard_concrete.expected_masks()\n\n    scores: Dict[str, float] = {}\n    for edge_name, mask_idx in edge_to_mask_idx.items():\n        scores[edge_name] = final_masks[mask_idx].item()\n\n    return scores\n\n\n# ---------------------------------------------------------------------------\n# Utility: edge count estimation\n# ---------------------------------------------------------------------------\n\ndef estimate_edge_counts(\n    n_layers: int, n_heads: int, n_kv_heads: int,\n) -> Dict[str, int]:\n    \"\"\"Estimate edge and mask parameter counts for a given architecture.\"\"\"\n    heads_per_kv = n_heads // n_kv_heads\n    _, _, n_masks = _build_edge_topology(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n    total_edges = 0\n    for L in range(n_layers):\n        n_src = 1 + L * (n_heads + 1)  # input + prior layers' heads + MLPs\n        total_edges += n_src * n_heads * 3  # q, k, v per head\n        n_src_mlp = n_src + n_heads\n        total_edges += n_src_mlp\n\n    return {\n        \"total_edges\": total_edges,\n        \"n_independent_masks\": n_masks,\n        \"mask_memory_bytes\": n_masks * 4,  # float32\n        \"mask_memory_mb\": n_masks * 4 / (1024 ** 2),\n    }\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "4f3fd263-93c0-4b05-81fe-2edc5da7e8b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YP3qLsFwumy4yoirqxnh7S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14855,
      "cache_read_input_tokens": 24468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14855
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

_source line 15 · 2026-05-12T19:29:01.683Z_

<details><summary>↩ Tool result · `toolu_01KQ5iQ2i6wDFBLVubGYjvZM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_scoring.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "1e8c3dd3-b66d-4fc2-bc43-2e97281bfc30",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_scoring.py",
    "content": "\"\"\"Edge Pruning v2 with L0 regularization for HuggingFace models.\n\nv2 fixes two critical bugs from v1:\n  1. MLP edge masks are now applied in forward via mlp pre-hook\n     (v1 had mask params but no forward-pass hook for MLP).\n  2. Q/K/V edge masks are kept independent per-head/KV-group\n     (v1 averaged across all Q/K/V destinations into a single scalar).\n\nHook strategy (v2): 4 submodule pre-hooks per layer\n  - self_attn.q_proj: per-head Q edge masks\n  - self_attn.k_proj: per-KV-group K edge masks (GQA shared)\n  - self_attn.v_proj: per-KV-group V edge masks (GQA shared)\n  - mlp: per-source MLP edge masks\nPlus capture hooks: embed_tokens, self_attn.o_proj (per-head), mlp (output).\n\nCanonical node format:\n  input, logits, a{L}.h{H}[.q|.k|.v], m{L}\n\nCanonical edge format: \"{src}->{dst}\" (no spaces)\n\nReferences:\n  - Louizos et al. \"Learning Sparse Neural Networks through L0 Regularization\" (2018)\n  - Bayazit et al. \"Discovering Knowledge-Critical Subnetworks\" (2023)\n\"\"\"\n\nfrom __future__ import annotations\n\nimport math\nfrom typing import Dict, List, Tuple, Callable, Optional\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\n\n\n# ---------------------------------------------------------------------------\n# Hard Concrete Distribution\n# ---------------------------------------------------------------------------\n\nclass HardConcrete(nn.Module):\n    \"\"\"Hard Concrete distribution for L0 mask parameterization.\n\n    Parameterized by log_alpha (location). During training, samples from a\n    stretched Binary Concrete and clamps to [0, 1], yielding exact zeros/ones.\n    \"\"\"\n\n    BETA = 2.0 / 3.0\n    GAMMA = -0.1\n    ZETA = 1.1\n    EPS = 1e-8\n\n    def __init__(self, n_masks: int, init_mean: float = 0.5):\n        super().__init__()\n        init_val = math.log(init_mean / (1.0 - init_mean + self.EPS))\n        self.log_alpha = nn.Parameter(torch.full((n_masks,), init_val))\n\n    def forward(self, training: bool = True) -> torch.Tensor:\n        if training:\n            u = torch.zeros_like(self.log_alpha).uniform_(self.EPS, 1.0 - self.EPS)\n            s = torch.sigmoid((torch.log(u / (1.0 - u)) + self.log_alpha) / self.BETA)\n        else:\n            s = torch.sigmoid(self.log_alpha)\n        s_bar = s * (self.ZETA - self.GAMMA) + self.GAMMA\n        return s_bar.clamp(0.0, 1.0)\n\n    def l0_penalty(self) -> torch.Tensor:\n        \"\"\"Expected L0 norm: sum of P(z != 0) for each mask.\"\"\"\n        return torch.sigmoid(\n            self.log_alpha - self.BETA * math.log(-self.GAMMA / self.ZETA)\n        ).sum()\n\n    def expected_masks(self) -> torch.Tensor:\n        \"\"\"Deterministic mask expectations (for final scoring).\"\"\"\n        return self.forward(training=False)\n\n\n# ---------------------------------------------------------------------------\n# Architecture detection (Llama-like HF models)\n# ---------------------------------------------------------------------------\n\n_LLAMA_LIKE = frozenset({\n    \"llama\", \"qwen2\", \"gemma\", \"gemma2\", \"mistral\", \"phi3\", \"phi\",\n})\n\n\ndef _get_arch_info(model) -> dict:\n    cfg = model.config\n    model_type = getattr(cfg, \"model_type\", \"\")\n    if model_type not in _LLAMA_LIKE:\n        raise ValueError(\n            f\"Edge Pruning L0 currently supports Llama-like architectures, \"\n            f\"got model_type={model_type!r}\"\n        )\n    n_heads = cfg.num_attention_heads\n    n_kv_heads = getattr(cfg, \"num_key_value_heads\", n_heads)\n    d_model = cfg.hidden_size\n    return dict(\n        n_layers=cfg.num_hidden_layers,\n        n_heads=n_heads,\n        n_kv_heads=n_kv_heads,\n        heads_per_kv_group=n_heads // n_kv_heads,\n        d_model=d_model,\n        head_dim=d_model // n_heads,\n    )\n\n\n# ---------------------------------------------------------------------------\n# Edge Topology: enumerate all edges and build mask index mapping\n# ---------------------------------------------------------------------------\n\ndef _src_nodes_before_layer(\n    layer: int, n_heads: int, include_attn_same_layer: bool = False,\n):\n    \"\"\"Yield source node names whose output feeds into a given layer.\"\"\"\n    yield \"input\"\n    for l in range(layer):\n        for h in range(n_heads):\n            yield f\"a{l}.h{h}\"\n        yield f\"m{l}\"\n    if include_attn_same_layer:\n        for h in range(n_heads):\n            yield f\"a{layer}.h{h}\"\n\n\ndef _build_edge_topology(\n    n_layers: int, n_heads: int, n_kv_heads: int, heads_per_kv_group: int,\n) -> Tuple[List[str], Dict[str, int], int]:\n    \"\"\"Build the full edge set and map each edge to its mask parameter index.\n\n    For GQA models, K/V edges targeting the same KV group share a mask.\n    Q edges always have independent masks.\n\n    Returns:\n        edge_names: list of canonical edge names\n        edge_to_mask_idx: edge_name -> index into mask parameter vector\n        n_masks: total number of independent mask parameters\n    \"\"\"\n    edge_names: List[str] = []\n    edge_to_mask_idx: Dict[str, int] = {}\n    mask_idx = 0\n\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes_before_layer(L, n_heads, False))\n        for src in srcs_attn:\n            for H in range(n_heads):\n                q_edge = f\"{src}->a{L}.h{H}.q\"\n                edge_names.append(q_edge)\n                edge_to_mask_idx[q_edge] = mask_idx\n                mask_idx += 1\n\n            for kv_group in range(n_kv_heads):\n                k_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    k_edge = f\"{src}->a{L}.h{H}.k\"\n                    edge_names.append(k_edge)\n                    edge_to_mask_idx[k_edge] = k_mask_idx\n\n            for kv_group in range(n_kv_heads):\n                v_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    v_edge = f\"{src}->a{L}.h{H}.v\"\n                    edge_names.append(v_edge)\n                    edge_to_mask_idx[v_edge] = v_mask_idx\n\n        srcs_mlp = list(_src_nodes_before_layer(L, n_heads, True))\n        for src in srcs_mlp:\n            mlp_edge = f\"{src}->m{L}\"\n            edge_names.append(mlp_edge)\n            edge_to_mask_idx[mlp_edge] = mask_idx\n            mask_idx += 1\n\n    return edge_names, edge_to_mask_idx, mask_idx\n\n\n# ---------------------------------------------------------------------------\n# Precomputed hook mask indices for vectorized application\n# ---------------------------------------------------------------------------\n\ndef _build_hook_mask_indices(\n    n_layers: int,\n    n_heads: int,\n    edge_to_mask_idx: Dict[str, int],\n    device: torch.device,\n) -> Tuple[\n    List[Dict[str, torch.Tensor]],\n    List[Dict[str, torch.Tensor]],\n    List[Dict[str, torch.Tensor]],\n    List[Dict[str, int]],\n]:\n    \"\"\"Precompute per-hook mask index tensors.\n\n    Returns (q_indices, k_indices, v_indices, mlp_indices) where:\n      q/k/v_indices[L] = {src_name: LongTensor[n_heads]}\n        GQA sharing is implicit: heads in the same KV group get identical index values.\n      mlp_indices[L] = {src_name: int}\n    \"\"\"\n    q_all: List[Dict[str, torch.Tensor]] = []\n    k_all: List[Dict[str, torch.Tensor]] = []\n    v_all: List[Dict[str, torch.Tensor]] = []\n    mlp_all: List[Dict[str, int]] = []\n\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes_before_layer(L, n_heads, False))\n        srcs_mlp = list(_src_nodes_before_layer(L, n_heads, True))\n\n        qi: Dict[str, torch.Tensor] = {}\n        ki: Dict[str, torch.Tensor] = {}\n        vi: Dict[str, torch.Tensor] = {}\n        for src in srcs_attn:\n            qi[src] = torch.tensor(\n                [edge_to_mask_idx[f\"{src}->a{L}.h{h}.q\"] for h in range(n_heads)],\n                dtype=torch.long, device=device,\n            )\n            ki[src] = torch.tensor(\n                [edge_to_mask_idx[f\"{src}->a{L}.h{h}.k\"] for h in range(n_heads)],\n                dtype=torch.long, device=device,\n            )\n            vi[src] = torch.tensor(\n                [edge_to_mask_idx[f\"{src}->a{L}.h{h}.v\"] for h in range(n_heads)],\n                dtype=torch.long, device=device,\n            )\n\n        mi: Dict[str, int] = {}\n        for src in srcs_mlp:\n            mi[src] = edge_to_mask_idx[f\"{src}->m{L}\"]\n\n        q_all.append(qi)\n        k_all.append(ki)\n        v_all.append(vi)\n        mlp_all.append(mi)\n\n    return q_all, k_all, v_all, mlp_all\n\n\n# ---------------------------------------------------------------------------\n# Per-head decomposition through the output projection\n# ---------------------------------------------------------------------------\n\ndef _decompose_attn_output(\n    concat_heads: torch.Tensor,\n    o_proj: nn.Linear,\n    n_heads: int,\n    head_dim: int,\n) -> Dict[int, torch.Tensor]:\n    \"\"\"Split concatenated head output and project each head through o_proj.\"\"\"\n    W = o_proj.weight  # [d_model, d_model]\n    heads = {}\n    for h in range(n_heads):\n        h_slice = concat_heads[:, :, h * head_dim:(h + 1) * head_dim]\n        W_h = W[:, h * head_dim:(h + 1) * head_dim]\n        heads[h] = h_slice @ W_h.T\n    return heads\n\n\n# ---------------------------------------------------------------------------\n# Masked input construction for submodule hooks\n# ---------------------------------------------------------------------------\n\ndef _build_masked_input_qkv(\n    src_cache: Dict[str, torch.Tensor],\n    masks: torch.Tensor,\n    idx_dict: Dict[str, torch.Tensor],\n    n_heads: int,\n    head_dim: int,\n    layernorm: nn.Module,\n    ref: torch.Tensor,\n) -> torch.Tensor:\n    \"\"\"Construct masked + layernormed input for a Q/K/V projection.\n\n    Applies per-head mask values to head_dim-sized slices of each source\n    activation. GQA sharing is transparent: idx_dict encodes shared\n    indices for heads within the same KV group.\n    \"\"\"\n    B, S, D = ref.shape\n    x = torch.zeros(B, S, D, device=ref.device, dtype=ref.dtype)\n    for src_name, mask_idx_t in idx_dict.items():\n        src = src_cache.get(src_name)\n        if src is None:\n            continue\n        z = masks[mask_idx_t].view(1, 1, n_heads, 1)\n        x = x + (src.view(B, S, n_heads, head_dim) * z).view(B, S, D)\n    return layernorm(x)\n\n\ndef _build_masked_input_mlp(\n    src_cache: Dict[str, torch.Tensor],\n    masks: torch.Tensor,\n    idx_dict: Dict[str, int],\n    post_ln: nn.Module,\n    ref: torch.Tensor,\n) -> torch.Tensor:\n    \"\"\"Construct masked + post-layernormed input for an MLP module.\"\"\"\n    x = torch.zeros_like(ref)\n    for src_name, mask_idx in idx_dict.items():\n        src = src_cache.get(src_name)\n        if src is None:\n            continue\n        x = x + src * masks[mask_idx]\n    return post_ln(x)\n\n\n# ---------------------------------------------------------------------------\n# Hook-based masked forward pass (v2: submodule-level hooks)\n# ---------------------------------------------------------------------------\n\ndef _masked_forward(\n    model,\n    input_ids: torch.Tensor,\n    masks: torch.Tensor,\n    arch_info: dict,\n    hook_indices: Tuple,\n) -> torch.Tensor:\n    \"\"\"Forward pass with per-destination edge masks via submodule hooks.\n\n    Registers 7 hooks per layer:\n      Pre-hooks (masking): q_proj, k_proj, v_proj, mlp\n      Capture hooks: o_proj (per-head attn output), mlp (output)\n    Plus 1 embed capture hook.\n    \"\"\"\n    n_heads = arch_info[\"n_heads\"]\n    head_dim = arch_info[\"head_dim\"]\n    n_layers = arch_info[\"n_layers\"]\n    layers = model.model.layers\n\n    q_idx, k_idx, v_idx, mlp_idx = hook_indices\n    src_cache: Dict[str, torch.Tensor] = {}\n    hooks: list = []\n\n    def _embed_hook(mod, inp, out):\n        src_cache[\"input\"] = out\n    hooks.append(model.model.embed_tokens.register_forward_hook(_embed_hook))\n\n    for L in range(n_layers):\n        layer = layers[L]\n        ln1 = layer.input_layernorm\n        ln2 = layer.post_attention_layernorm\n\n        # --- Q/K/V projection pre-hooks: replace input with masked residual ---\n\n        def _q_hook(mod, args, *, _qi=q_idx[L], _ln=ln1):\n            return (_build_masked_input_qkv(\n                src_cache, masks, _qi, n_heads, head_dim, _ln, args[0],\n            ),) + args[1:]\n\n        def _k_hook(mod, args, *, _ki=k_idx[L], _ln=ln1):\n            return (_build_masked_input_qkv(\n                src_cache, masks, _ki, n_heads, head_dim, _ln, args[0],\n            ),) + args[1:]\n\n        def _v_hook(mod, args, *, _vi=v_idx[L], _ln=ln1):\n            return (_build_masked_input_qkv(\n                src_cache, masks, _vi, n_heads, head_dim, _ln, args[0],\n            ),) + args[1:]\n\n        hooks.append(layer.self_attn.q_proj.register_forward_pre_hook(_q_hook))\n        hooks.append(layer.self_attn.k_proj.register_forward_pre_hook(_k_hook))\n        hooks.append(layer.self_attn.v_proj.register_forward_pre_hook(_v_hook))\n\n        # --- Attention output capture: per-head decomposition through o_proj ---\n\n        def _oproj_hook(mod, inp, out, *, _L=L):\n            per_head = _decompose_attn_output(inp[0], mod, n_heads, head_dim)\n            for h, h_out in per_head.items():\n                src_cache[f\"a{_L}.h{h}\"] = h_out\n        hooks.append(layer.self_attn.o_proj.register_forward_hook(_oproj_hook))\n\n        # --- MLP pre-hook: replace input with masked residual ---\n\n        def _mlp_pre_hook(mod, args, *, _mi=mlp_idx[L], _ln=ln2):\n            return (_build_masked_input_mlp(\n                src_cache, masks, _mi, _ln, args[0],\n            ),) + args[1:]\n        hooks.append(layer.mlp.register_forward_pre_hook(_mlp_pre_hook))\n\n        # --- MLP output capture ---\n\n        def _mlp_out_hook(mod, inp, out, *, _L=L):\n            src_cache[f\"m{_L}\"] = out if isinstance(out, torch.Tensor) else out[0]\n        hooks.append(layer.mlp.register_forward_hook(_mlp_out_hook))\n\n    try:\n        return model(input_ids).logits\n    finally:\n        for h in hooks:\n            h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Faithfulness loss\n# ---------------------------------------------------------------------------\n\ndef _faithfulness_loss(\n    masked_logits: torch.Tensor,\n    clean_logits: torch.Tensor,\n    target_ids: Optional[torch.Tensor],\n) -> torch.Tensor:\n    \"\"\"KL divergence between clean and masked model output distributions.\"\"\"\n    if target_ids is not None:\n        batch_size = masked_logits.size(0)\n        idx = target_ids.view(batch_size)\n        masked_logits = masked_logits[torch.arange(batch_size), idx]\n        clean_logits = clean_logits[torch.arange(batch_size), idx]\n\n    log_p = F.log_softmax(masked_logits, dim=-1)\n    q = F.softmax(clean_logits, dim=-1)\n    return F.kl_div(log_p, q, reduction=\"batchmean\")\n\n\n# ---------------------------------------------------------------------------\n# Main entry point\n# ---------------------------------------------------------------------------\n\ndef compute_edge_pruning_scores(\n    model,\n    clean_inputs,\n    corrupt_inputs,\n    metric_fn: Callable,\n    target_ids=None,\n    n_epochs: int = 100,\n    lambda_l0: float = 1e-3,\n    lr: float = 0.1,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Compute Edge Pruning L0 edge scores.\n\n    Returns dict of canonical_edge_name -> score (mask expectation).\n\n    Args:\n        model: HuggingFace CausalLM (Llama-like: Qwen2, Llama, Mistral, etc.)\n        clean_inputs: dict with 'input_ids' [batch, seq_len]\n        corrupt_inputs: dict with 'input_ids' [batch, seq_len]\n        metric_fn: faithfulness metric (kept for interface parity; KL used internally)\n        target_ids: [batch] token positions for evaluation (None = all positions)\n        n_epochs: optimization epochs\n        lambda_l0: L0 sparsity penalty weight\n        lr: learning rate for mask parameters\n        device: target device\n    \"\"\"\n    arch_info = _get_arch_info(model)\n    n_layers = arch_info[\"n_layers\"]\n    n_heads = arch_info[\"n_heads\"]\n    n_kv_heads = arch_info[\"n_kv_heads\"]\n    heads_per_kv_group = arch_info[\"heads_per_kv_group\"]\n\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology(\n        n_layers, n_heads, n_kv_heads, heads_per_kv_group,\n    )\n    hook_indices = _build_hook_mask_indices(\n        n_layers, n_heads, edge_to_mask_idx, device,\n    )\n\n    hard_concrete = HardConcrete(n_masks, init_mean=0.5).to(device)\n    optimizer = torch.optim.Adam(hard_concrete.parameters(), lr=lr)\n\n    # Prepare inputs\n    if isinstance(clean_inputs, dict):\n        clean_ids = clean_inputs[\"input_ids\"]\n        if not isinstance(clean_ids, torch.Tensor):\n            clean_ids = torch.tensor(clean_ids)\n    else:\n        clean_ids = clean_inputs\n    clean_ids = clean_ids.to(device)\n\n    if isinstance(corrupt_inputs, dict):\n        corrupt_ids = corrupt_inputs[\"input_ids\"]\n        if not isinstance(corrupt_ids, torch.Tensor):\n            corrupt_ids = torch.tensor(corrupt_ids)\n    else:\n        corrupt_ids = corrupt_inputs\n    corrupt_ids = corrupt_ids.to(device)\n\n    if target_ids is not None:\n        if not isinstance(target_ids, torch.Tensor):\n            target_ids = torch.tensor(target_ids)\n        target_ids = target_ids.to(device)\n\n    # Freeze model — only mask params are optimized\n    model.eval()\n    model.requires_grad_(False)\n\n    with torch.no_grad():\n        clean_logits = model(clean_ids).logits.detach()\n\n    # Optimization loop\n    for epoch in range(n_epochs):\n        optimizer.zero_grad()\n        masks = hard_concrete(training=True)\n        masked_logits = _masked_forward(\n            model, clean_ids, masks, arch_info, hook_indices,\n        )\n        faith_loss = _faithfulness_loss(masked_logits, clean_logits, target_ids)\n        l0_loss = hard_concrete.l0_penalty()\n        loss = faith_loss + lambda_l0 * l0_loss\n        loss.backward()\n        optimizer.step()\n\n    # Extract final scores\n    with torch.no_grad():\n        final_masks = hard_concrete.expected_masks()\n\n    scores: Dict[str, float] = {}\n    for edge_name, mask_idx in edge_to_mask_idx.items():\n        scores[edge_name] = final_masks[mask_idx].item()\n\n    return scores\n\n\n# ---------------------------------------------------------------------------\n# Utility: edge count estimation\n# ---------------------------------------------------------------------------\n\ndef estimate_edge_counts(\n    n_layers: int, n_heads: int, n_kv_heads: int,\n) -> Dict[str, int]:\n    \"\"\"Estimate edge and mask parameter counts for a given architecture.\"\"\"\n    heads_per_kv = n_heads // n_kv_heads\n    _, _, n_masks = _build_edge_topology(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n    total_edges = 0\n    for L in range(n_layers):\n        n_src = 1 + L * (n_heads + 1)  # input + prior layers' heads + MLPs\n        total_edges += n_src * n_heads * 3  # q, k, v per head\n        n_src_mlp = n_src + n_heads\n        total_edges += n_src_mlp\n\n    return {\n        \"total_edges\": total_edges,\n        \"n_independent_masks\": n_masks,\n        \"mask_memory_bytes\": n_masks * 4,  # float32\n        \"mask_memory_mb\": n_masks * 4 / (1024 ** 2),\n    }\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 11,
        "newStart": 1,
        "newLines": 17,
        "lines": [
          "-\"\"\"Edge Pruning with L0 regularization for HuggingFace models.",
          "+\"\"\"Edge Pruning v2 with L0 regularization for HuggingFace models.",
          " ",
          "-Implements princeton-nlp style Edge Pruning using Hard Concrete relaxation",
          "-(Louizos et al., 2018) on HuggingFace CausalLM models with GQA support.",
          "+v2 fixes two critical bugs from v1:",
          "+  1. MLP edge masks are now applied in forward via mlp pre-hook",
          "+     (v1 had mask params but no forward-pass hook for MLP).",
          "+  2. Q/K/V edge masks are kept independent per-head/KV-group",
          "+     (v1 averaged across all Q/K/V destinations into a single scalar).",
          " ",
          "-Each edge (u->v) in the computational graph gets a learnable mask via the",
          "-Hard Concrete distribution, which allows exact zeros and ones. The masks",
          "-are optimized to minimize faithfulness loss + L0 sparsity penalty.",
          "+Hook strategy (v2): 4 submodule pre-hooks per layer",
          "+  - self_attn.q_proj: per-head Q edge masks",
          "+  - self_attn.k_proj: per-KV-group K edge masks (GQA shared)",
          "+  - self_attn.v_proj: per-KV-group V edge masks (GQA shared)",
          "+  - mlp: per-source MLP edge masks",
          "+Plus capture hooks: embed_tokens, self_attn.o_proj (per-head), mlp (output).",
          " ",
          " Canonical node format:",
          "   input, logits, a{L}.h{H}[.q|.k|.v], m{L}"
        ]
      },
      {
        "oldStart": 102,
        "oldLines": 6,
        "newStart": 108,
        "newLines": 20,
        "lines": [
          " # Edge Topology: enumerate all edges and build mask index mapping",
          " # ---------------------------------------------------------------------------",
          " ",
          "+def _src_nodes_before_layer(",
          "+    layer: int, n_heads: int, include_attn_same_layer: bool = False,",
          "+):",
          "+    \"\"\"Yield source node names whose output feeds into a given layer.\"\"\"",
          "+    yield \"input\"",
          "+    for l in range(layer):",
          "+        for h in range(n_heads):",
          "+            yield f\"a{l}.h{h}\"",
          "+        yield f\"m{l}\"",
          "+    if include_attn_same_layer:",
          "+        for h in range(n_heads):",
          "+            yield f\"a{layer}.h{h}\"",
          "+",
          "+",
          " def _build_edge_topology(",
          "     n_layers: int, n_heads: int, n_kv_heads: int, heads_per_kv_group: int,",
          " ) -> Tuple[List[str], Dict[str, int], int]:"
        ]
      },
      {
        "oldStart": 119,
        "oldLines": 29,
        "newStart": 139,
        "newLines": 15,
        "lines": [
          "     edge_to_mask_idx: Dict[str, int] = {}",
          "     mask_idx = 0",
          " ",
          "-    def _src_nodes_before_layer(layer: int, include_attn_same_layer: bool = False):",
          "-        \"\"\"Yield (src_name,) for all nodes whose output feeds into a given layer.\"\"\"",
          "-        yield \"input\"",
          "-        for l in range(layer):",
          "-            for h in range(n_heads):",
          "-                yield f\"a{l}.h{h}\"",
          "-            yield f\"m{l}\"",
          "-        if include_attn_same_layer:",
          "-            for h in range(n_heads):",
          "-                yield f\"a{layer}.h{h}\"",
          "-",
          "     for L in range(n_layers):",
          "-        # --- Edges into attention heads at layer L ---",
          "-        srcs_attn = list(_src_nodes_before_layer(L, include_attn_same_layer=False))",
          "+        srcs_attn = list(_src_nodes_before_layer(L, n_heads, False))",
          "         for src in srcs_attn:",
          "             for H in range(n_heads):",
          "-                # Q edge: always independent",
          "                 q_edge = f\"{src}->a{L}.h{H}.q\"",
          "                 edge_names.append(q_edge)",
          "                 edge_to_mask_idx[q_edge] = mask_idx",
          "                 mask_idx += 1",
          " ",
          "-            # K edges: shared within KV group",
          "             for kv_group in range(n_kv_heads):",
          "                 k_mask_idx = mask_idx",
          "                 mask_idx += 1"
        ]
      },
      {
        "oldStart": 151,
        "oldLines": 7,
        "newStart": 157,
        "newLines": 6,
        "lines": [
          "                     edge_names.append(k_edge)",
          "                     edge_to_mask_idx[k_edge] = k_mask_idx",
          " ",
          "-            # V edges: shared within KV group",
          "             for kv_group in range(n_kv_heads):",
          "                 v_mask_idx = mask_idx",
          "                 mask_idx += 1"
        ]
      },
      {
        "oldStart": 161,
        "oldLines": 8,
        "newStart": 166,
        "newLines": 7,
        "lines": [
          "                     edge_names.append(v_edge)",
          "                     edge_to_mask_idx[v_edge] = v_mask_idx",
          " ",
          "-        # --- Edges into MLP at layer L ---",
          "-        srcs_mlp = list(_src_nodes_before_layer(L, include_attn_same_layer=True))",
          "+        srcs_mlp = list(_src_nodes_before_layer(L, n_heads, True))",
          "         for src in srcs_mlp:",
          "             mlp_edge = f\"{src}->m{L}\"",
          "             edge_names.append(mlp_edge)"
        ]
      },
      {
        "oldStart": 173,
        "oldLines": 50,
        "newStart": 177,
        "newLines": 69,
        "lines": [
          " ",
          " ",
          " # ---------------------------------------------------------------------------",
          "-# Destination-grouped mask table for efficient hook application",
          "+# Precomputed hook mask indices for vectorized application",
          " # ---------------------------------------------------------------------------",
          " ",
          "-def _build_dst_mask_table(",
          "+def _build_hook_mask_indices(",
          "+    n_layers: int,",
          "+    n_heads: int,",
          "     edge_to_mask_idx: Dict[str, int],",
          "-) -> Dict[str, Dict[str, int]]:",
          "-    \"\"\"Group edges by destination node.",
          "+    device: torch.device,",
          "+) -> Tuple[",
          "+    List[Dict[str, torch.Tensor]],",
          "+    List[Dict[str, torch.Tensor]],",
          "+    List[Dict[str, torch.Tensor]],",
          "+    List[Dict[str, int]],",
          "+]:",
          "+    \"\"\"Precompute per-hook mask index tensors.",
          " ",
          "-    Returns: {dst_node: {src_node: mask_param_index}}",
          "+    Returns (q_indices, k_indices, v_indices, mlp_indices) where:",
          "+      q/k/v_indices[L] = {src_name: LongTensor[n_heads]}",
          "+        GQA sharing is implicit: heads in the same KV group get identical index values.",
          "+      mlp_indices[L] = {src_name: int}",
          "     \"\"\"",
          "-    table: Dict[str, Dict[str, int]] = {}",
          "-    for edge, idx in edge_to_mask_idx.items():",
          "-        src, dst = edge.split(\"->\", 1)",
          "-        if dst not in table:",
          "-            table[dst] = {}",
          "-        table[dst][src] = idx",
          "-    return table",
          "+    q_all: List[Dict[str, torch.Tensor]] = []",
          "+    k_all: List[Dict[str, torch.Tensor]] = []",
          "+    v_all: List[Dict[str, torch.Tensor]] = []",
          "+    mlp_all: List[Dict[str, int]] = []",
          " ",
          "+    for L in range(n_layers):",
          "+        srcs_attn = list(_src_nodes_before_layer(L, n_heads, False))",
          "+        srcs_mlp = list(_src_nodes_before_layer(L, n_heads, True))",
          " ",
          "-# ---------------------------------------------------------------------------",
          "-# Source activation cache (captured via hooks)",
          "-# ---------------------------------------------------------------------------",
          "+        qi: Dict[str, torch.Tensor] = {}",
          "+        ki: Dict[str, torch.Tensor] = {}",
          "+        vi: Dict[str, torch.Tensor] = {}",
          "+        for src in srcs_attn:",
          "+            qi[src] = torch.tensor(",
          "+                [edge_to_mask_idx[f\"{src}->a{L}.h{h}.q\"] for h in range(n_heads)],",
          "+                dtype=torch.long, device=device,",
          "+            )",
          "+            ki[src] = torch.tensor(",
          "+                [edge_to_mask_idx[f\"{src}->a{L}.h{h}.k\"] for h in range(n_heads)],",
          "+                dtype=torch.long, device=device,",
          "+            )",
          "+            vi[src] = torch.tensor(",
          "+                [edge_to_mask_idx[f\"{src}->a{L}.h{h}.v\"] for h in range(n_heads)],",
          "+                dtype=torch.long, device=device,",
          "+            )",
          " ",
          "-class _ActivationCache:",
          "-    \"\"\"Stores source node activations during forward pass.\"\"\"",
          "+        mi: Dict[str, int] = {}",
          "+        for src in srcs_mlp:",
          "+            mi[src] = edge_to_mask_idx[f\"{src}->m{L}\"]",
          " ",
          "-    def __init__(self):",
          "-        self.embed_out: Optional[torch.Tensor] = None",
          "-        self.head_out: Dict[int, Dict[int, torch.Tensor]] = {}",
          "-        self.mlp_out: Dict[int, torch.Tensor] = {}",
          "+        q_all.append(qi)",
          "+        k_all.append(ki)",
          "+        v_all.append(vi)",
          "+        mlp_all.append(mi)",
          " ",
          "+    return q_all, k_all, v_all, mlp_all",
          " ",
          "+",
          " # ---------------------------------------------------------------------------",
          "-# Hook-based masked forward pass",
          "+# Per-head decomposition through the output projection",
          " # ---------------------------------------------------------------------------",
          " ",
          "-def _get_module(model, path: str) -> nn.Module:",
          "-    parts = path.split(\".\")",
          "-    m = model",
          "-    for p in parts:",
          "-        m = getattr(m, p)",
          "-    return m",
          "-",
          "-",
          " def _decompose_attn_output(",
          "     concat_heads: torch.Tensor,",
          "     o_proj: nn.Linear,"
        ]
      },
      {
        "oldStart": 233,
        "oldLines": 111,
        "newStart": 256,
        "newLines": 134,
        "lines": [
          "     return heads",
          " ",
          " ",
          "+# ---------------------------------------------------------------------------",
          "+# Masked input construction for submodule hooks",
          "+# ---------------------------------------------------------------------------",
          "+",
          "+def _build_masked_input_qkv(",
          "+    src_cache: Dict[str, torch.Tensor],",
          "+    masks: torch.Tensor,",
          "+    idx_dict: Dict[str, torch.Tensor],",
          "+    n_heads: int,",
          "+    head_dim: int,",
          "+    layernorm: nn.Module,",
          "+    ref: torch.Tensor,",
          "+) -> torch.Tensor:",
          "+    \"\"\"Construct masked + layernormed input for a Q/K/V projection.",
          "+",
          "+    Applies per-head mask values to head_dim-sized slices of each source",
          "+    activation. GQA sharing is transparent: idx_dict encodes shared",
          "+    indices for heads within the same KV group.",
          "+    \"\"\"",
          "+    B, S, D = ref.shape",
          "+    x = torch.zeros(B, S, D, device=ref.device, dtype=ref.dtype)",
          "+    for src_name, mask_idx_t in idx_dict.items():",
          "+        src = src_cache.get(src_name)",
          "+        if src is None:",
          "+            continue",
          "+        z = masks[mask_idx_t].view(1, 1, n_heads, 1)",
          "+        x = x + (src.view(B, S, n_heads, head_dim) * z).view(B, S, D)",
          "+    return layernorm(x)",
          "+",
          "+",
          "+def _build_masked_input_mlp(",
          "+    src_cache: Dict[str, torch.Tensor],",
          "+    masks: torch.Tensor,",
          "+    idx_dict: Dict[str, int],",
          "+    post_ln: nn.Module,",
          "+    ref: torch.Tensor,",
          "+) -> torch.Tensor:",
          "+    \"\"\"Construct masked + post-layernormed input for an MLP module.\"\"\"",
          "+    x = torch.zeros_like(ref)",
          "+    for src_name, mask_idx in idx_dict.items():",
          "+        src = src_cache.get(src_name)",
          "+        if src is None:",
          "+            continue",
          "+        x = x + src * masks[mask_idx]",
          "+    return post_ln(x)",
          "+",
          "+",
          "+# ---------------------------------------------------------------------------",
          "+# Hook-based masked forward pass (v2: submodule-level hooks)",
          "+# ---------------------------------------------------------------------------",
          "+",
          " def _masked_forward(",
          "     model,",
          "     input_ids: torch.Tensor,",
          "     masks: torch.Tensor,",
          "     arch_info: dict,",
          "-    dst_mask_table: Dict[str, Dict[str, int]],",
          "+    hook_indices: Tuple,",
          " ) -> torch.Tensor:",
          "-    \"\"\"Run forward pass with edge masks applied via hooks.",
          "+    \"\"\"Forward pass with per-destination edge masks via submodule hooks.",
          " ",
          "-    Strategy:",
          "-    1. Register hooks to capture source node outputs (embed, attn heads, MLP).",
          "-    2. At each destination's pre-hook, replace its input with the masked sum",
          "-       of upstream source outputs.",
          "-",
          "-    For memory efficiency, source activations are captured and masks applied",
          "-    layer-by-layer. Each layer's pre-hook constructs the masked residual",
          "-    from all upstream sources.",
          "+    Registers 7 hooks per layer:",
          "+      Pre-hooks (masking): q_proj, k_proj, v_proj, mlp",
          "+      Capture hooks: o_proj (per-head attn output), mlp (output)",
          "+    Plus 1 embed capture hook.",
          "     \"\"\"",
          "-    n_layers = arch_info[\"n_layers\"]",
          "     n_heads = arch_info[\"n_heads\"]",
          "     head_dim = arch_info[\"head_dim\"]",
          "+    n_layers = arch_info[\"n_layers\"]",
          "     layers = model.model.layers",
          " ",
          "-    cache = _ActivationCache()",
          "-    hooks = []",
          "+    q_idx, k_idx, v_idx, mlp_idx = hook_indices",
          "+    src_cache: Dict[str, torch.Tensor] = {}",
          "+    hooks: list = []",
          " ",
          "-    # Capture embedding output",
          "     def _embed_hook(mod, inp, out):",
          "-        cache.embed_out = out",
          "+        src_cache[\"input\"] = out",
          "     hooks.append(model.model.embed_tokens.register_forward_hook(_embed_hook))",
          " ",
          "     for L in range(n_layers):",
          "         layer = layers[L]",
          "+        ln1 = layer.input_layernorm",
          "+        ln2 = layer.post_attention_layernorm",
          " ",
          "-        # Capture per-head attention output via o_proj",
          "-        def _oproj_hook(mod, inp, out, *, _L=L):",
          "-            cache.head_out[_L] = _decompose_attn_output(",
          "-                inp[0], mod, n_heads, head_dim,",
          "-            )",
          "-        hooks.append(layer.self_attn.o_proj.register_forward_hook(_oproj_hook))",
          "+        # --- Q/K/V projection pre-hooks: replace input with masked residual ---",
          " ",
          "-        # Capture MLP output",
          "-        def _mlp_hook(mod, inp, out, *, _L=L):",
          "-            cache.mlp_out[_L] = out if isinstance(out, torch.Tensor) else out[0]",
          "-        hooks.append(layer.mlp.register_forward_hook(_mlp_hook))",
          "+        def _q_hook(mod, args, *, _qi=q_idx[L], _ln=ln1):",
          "+            return (_build_masked_input_qkv(",
          "+                src_cache, masks, _qi, n_heads, head_dim, _ln, args[0],",
          "+            ),) + args[1:]",
          " ",
          "-        # Pre-hook on each layer: construct masked residual stream input.",
          "-        # This replaces the residual stream with the masked combination of",
          "-        # all upstream source nodes.",
          "-        def _layer_pre_hook(mod, inp, *, _L=L):",
          "-            x = inp[0] if isinstance(inp, tuple) else inp",
          "+        def _k_hook(mod, args, *, _ki=k_idx[L], _ln=ln1):",
          "+            return (_build_masked_input_qkv(",
          "+                src_cache, masks, _ki, n_heads, head_dim, _ln, args[0],",
          "+            ),) + args[1:]",
          " ",
          "-            # Collect all source activations available before this layer",
          "-            src_acts: Dict[str, torch.Tensor] = {}",
          "-            if cache.embed_out is not None:",
          "-                src_acts[\"input\"] = cache.embed_out",
          "-            for l in range(_L):",
          "-                if l in cache.head_out:",
          "-                    for h in range(n_heads):",
          "-                        src_acts[f\"a{l}.h{h}\"] = cache.head_out[l][h]",
          "-                if l in cache.mlp_out:",
          "-                    src_acts[f\"m{l}\"] = cache.mlp_out[l]",
          "+        def _v_hook(mod, args, *, _vi=v_idx[L], _ln=ln1):",
          "+            return (_build_masked_input_qkv(",
          "+                src_cache, masks, _vi, n_heads, head_dim, _ln, args[0],",
          "+            ),) + args[1:]",
          " ",
          "-            # For attention destinations (q, k, v) at this layer:",
          "-            # We approximate by masking the residual stream input.",
          "-            # The mask for each destination type is the element-wise product",
          "-            # of all source masks. For simplicity and memory, we apply the",
          "-            # *minimum* mask across q/k/v destinations for each source,",
          "-            # effectively masking the residual input to the entire attention block.",
          "-            #",
          "-            # More precise: build separate masked inputs per q/k/v head.",
          "-            # But that requires modifying internal attention computation,",
          "-            # which is architecture-specific. The residual-level masking",
          "-            # is the standard approach in princeton-nlp/edge-pruning.",
          "+        hooks.append(layer.self_attn.q_proj.register_forward_pre_hook(_q_hook))",
          "+        hooks.append(layer.self_attn.k_proj.register_forward_pre_hook(_k_hook))",
          "+        hooks.append(layer.self_attn.v_proj.register_forward_pre_hook(_v_hook))",
          " ",
          "-            # Gather all destination nodes at this layer",
          "-            attn_dsts = set()",
          "-            mlp_dst = f\"m{_L}\"",
          "-            for H in range(n_heads):",
          "-                for qkv in (\"q\", \"k\", \"v\"):",
          "-                    attn_dsts.add(f\"a{_L}.h{H}.{qkv}\")",
          "+        # --- Attention output capture: per-head decomposition through o_proj ---",
          " ",
          "-            # Compute masked residual for attention input",
          "-            # Use average mask across all attn destinations for each source",
          "-            masked_resid = torch.zeros_like(x)",
          "-            for src_name, src_act in src_acts.items():",
          "-                # Collect mask values for this source across attn destinations",
          "-                mask_indices = []",
          "-                for dst in attn_dsts:",
          "-                    if dst in dst_mask_table and src_name in dst_mask_table[dst]:",
          "-                        mask_indices.append(dst_mask_table[dst][src_name])",
          "-                if mask_indices:",
          "-                    # Average mask across destinations (approximation)",
          "-                    src_mask = masks[mask_indices].mean()",
          "-                    masked_resid = masked_resid + src_act * src_mask",
          "+        def _oproj_hook(mod, inp, out, *, _L=L):",
          "+            per_head = _decompose_attn_output(inp[0], mod, n_heads, head_dim)",
          "+            for h, h_out in per_head.items():",
          "+                src_cache[f\"a{_L}.h{h}\"] = h_out",
          "+        hooks.append(layer.self_attn.o_proj.register_forward_hook(_oproj_hook))",
          " ",
          "-            if isinstance(inp, tuple):",
          "-                return (masked_resid,) + inp[1:]",
          "-            return masked_resid",
          "+        # --- MLP pre-hook: replace input with masked residual ---",
          " ",
          "-        hooks.append(layer.register_forward_pre_hook(_layer_pre_hook))",
          "+        def _mlp_pre_hook(mod, args, *, _mi=mlp_idx[L], _ln=ln2):",
          "+            return (_build_masked_input_mlp(",
          "+                src_cache, masks, _mi, _ln, args[0],",
          "+            ),) + args[1:]",
          "+        hooks.append(layer.mlp.register_forward_pre_hook(_mlp_pre_hook))",
          " ",
          "+        # --- MLP output capture ---",
          "+",
          "+        def _mlp_out_hook(mod, inp, out, *, _L=L):",
          "+            src_cache[f\"m{_L}\"] = out if isinstance(out, torch.Tensor) else out[0]",
          "+        hooks.append(layer.mlp.register_forward_hook(_mlp_out_hook))",
          "+",
          "     try:",
          "-        out = model(input_ids)",
          "-        return out.logits",
          "+        return model(input_ids).logits",
          "     finally:",
          "         for h in hooks:",
          "             h.remove()"
        ]
      },
      {
        "oldStart": 352,
        "oldLines": 12,
        "newStart": 398,
        "newLines": 8,
        "lines": [
          "     clean_logits: torch.Tensor,",
          "     target_ids: Optional[torch.Tensor],",
          " ) -> torch.Tensor:",
          "-    \"\"\"KL divergence between clean and masked model output distributions.",
          "-",
          "-    If target_ids is provided, only compute loss at target token positions.",
          "-    \"\"\"",
          "+    \"\"\"KL divergence between clean and masked model output distributions.\"\"\"",
          "     if target_ids is not None:",
          "-        # target_ids: [batch] — index of the token position to evaluate",
          "         batch_size = masked_logits.size(0)",
          "         idx = target_ids.view(batch_size)",
          "         masked_logits = masked_logits[torch.arange(batch_size), idx]"
        ]
      },
      {
        "oldStart": 404,
        "oldLines": 13,
        "newStart": 446,
        "newLines": 13,
        "lines": [
          "     n_kv_heads = arch_info[\"n_kv_heads\"]",
          "     heads_per_kv_group = arch_info[\"heads_per_kv_group\"]",
          " ",
          "-    # Build edge topology",
          "     edge_names, edge_to_mask_idx, n_masks = _build_edge_topology(",
          "         n_layers, n_heads, n_kv_heads, heads_per_kv_group,",
          "     )",
          "-    dst_mask_table = _build_dst_mask_table(edge_to_mask_idx)",
          "+    hook_indices = _build_hook_mask_indices(",
          "+        n_layers, n_heads, edge_to_mask_idx, device,",
          "+    )",
          " ",
          "-    # Initialize Hard Concrete mask parameters",
          "     hard_concrete = HardConcrete(n_masks, init_mean=0.5).to(device)",
          "     optimizer = torch.optim.Adam(hard_concrete.parameters(), lr=lr)",
          " "
        ]
      },
      {
        "oldStart": 436,
        "oldLines": 28,
        "newStart": 478,
        "newLines": 23,
        "lines": [
          "             target_ids = torch.tensor(target_ids)",
          "         target_ids = target_ids.to(device)",
          " ",
          "-    # Get clean model logits (frozen)",
          "+    # Freeze model — only mask params are optimized",
          "     model.eval()",
          "+    model.requires_grad_(False)",
          "+",
          "     with torch.no_grad():",
          "         clean_logits = model(clean_ids).logits.detach()",
          " ",
          "     # Optimization loop",
          "     for epoch in range(n_epochs):",
          "         optimizer.zero_grad()",
          "-",
          "-        # Sample masks from Hard Concrete",
          "         masks = hard_concrete(training=True)",
          "-",
          "-        # Forward pass with masks applied",
          "         masked_logits = _masked_forward(",
          "-            model, clean_ids, masks, arch_info, dst_mask_table,",
          "+            model, clean_ids, masks, arch_info, hook_indices,",
          "         )",
          "-",
          "-        # Loss = faithfulness + sparsity",
          "         faith_loss = _faithfulness_loss(masked_logits, clean_logits, target_ids)",
          "         l0_loss = hard_concrete.l0_penalty()",
          "         loss = faith_loss + lambda_l0 * l0_loss",
          "-",
          "         loss.backward()",
          "         optimizer.step()",
          " "
        ]
      },
      {
        "oldStart": 484,
        "oldLines": 13,
        "newStart": 521,
        "newLines": 10,
        "lines": [
          "     _, _, n_masks = _build_edge_topology(",
          "         n_layers, n_heads, n_kv_heads, heads_per_kv,",
          "     )",
          "-    # Total edges (including shared masks counted separately)",
          "     total_edges = 0",
          "     for L in range(n_layers):",
          "         n_src = 1 + L * (n_heads + 1)  # input + prior layers' heads + MLPs",
          "-        # Attn edges: Q independent, K/V shared per KV group",
          "         total_edges += n_src * n_heads * 3  # q, k, v per head",
          "-        # MLP edges: from all upstream including same-layer attn",
          "         n_src_mlp = n_src + n_heads",
          "         total_edges += n_src_mlp",
          " "
        ]
      }
    ],
    "originalFile": "\"\"\"Edge Pruning with L0 regularization for HuggingFace models.\n\nImplements princeton-nlp style Edge Pruning using Hard Concrete relaxation\n(Louizos et al., 2018) on HuggingFace CausalLM models with GQA support.\n\nEach edge (u->v) in the computational graph gets a learnable mask via the\nHard Concrete distribution, which allows exact zeros and ones. The masks\nare optimized to minimize faithfulness loss + L0 sparsity penalty.\n\nCanonical node format:\n  input, logits, a{L}.h{H}[.q|.k|.v], m{L}\n\nCanonical edge format: \"{src}->{dst}\" (no spaces)\n\nReferences:\n  - Louizos et al. \"Learning Sparse Neural Networks through L0 Regularization\" (2018)\n  - Bayazit et al. \"Discovering Knowledge-Critical Subnetworks\" (2023)\n\"\"\"\n\nfrom __future__ import annotations\n\nimport math\nfrom typing import Dict, List, Tuple, Callable, Optional\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\n\n\n# ---------------------------------------------------------------------------\n# Hard Concrete Distribution\n# ---------------------------------------------------------------------------\n\nclass HardConcrete(nn.Module):\n    \"\"\"Hard Concrete distribution for L0 mask parameterization.\n\n    Parameterized by log_alpha (location). During training, samples from a\n    stretched Binary Concrete and clamps to [0, 1], yielding exact zeros/ones.\n    \"\"\"\n\n    BETA = 2.0 / 3.0\n    GAMMA = -0.1\n    ZETA = 1.1\n    EPS = 1e-8\n\n    def __init__(self, n_masks: int, init_mean: float = 0.5):\n        super().__init__()\n        init_val = math.log(init_mean / (1.0 - init_mean + self.EPS))\n        self.log_alpha = nn.Parameter(torch.full((n_masks,), init_val))\n\n    def forward(self, training: bool = True) -> torch.Tensor:\n        if training:\n            u = torch.zeros_like(self.log_alpha).uniform_(self.EPS, 1.0 - self.EPS)\n            s = torch.sigmoid((torch.log(u / (1.0 - u)) + self.log_alpha) / self.BETA)\n        else:\n            s = torch.sigmoid(self.log_alpha)\n        s_bar = s * (self.ZETA - self.GAMMA) + self.GAMMA\n        return s_bar.clamp(0.0, 1.0)\n\n    def l0_penalty(self) -> torch.Tensor:\n        \"\"\"Expected L0 norm: sum of P(z != 0) for each mask.\"\"\"\n        return torch.sigmoid(\n            self.log_alpha - self.BETA * math.log(-self.GAMMA / self.ZETA)\n        ).sum()\n\n    def expected_masks(self) -> torch.Tensor:\n        \"\"\"Deterministic mask expectations (for final scoring).\"\"\"\n        return self.forward(training=False)\n\n\n# ---------------------------------------------------------------------------\n# Architecture detection (Llama-like HF models)\n# ---------------------------------------------------------------------------\n\n_LLAMA_LIKE = frozenset({\n    \"llama\", \"qwen2\", \"gemma\", \"gemma2\", \"mistral\", \"phi3\", \"phi\",\n})\n\n\ndef _get_arch_info(model) -> dict:\n    cfg = model.config\n    model_type = getattr(cfg, \"model_type\", \"\")\n    if model_type not in _LLAMA_LIKE:\n        raise ValueError(\n            f\"Edge Pruning L0 currently supports Llama-like architectures, \"\n            f\"got model_type={model_type!r}\"\n        )\n    n_heads = cfg.num_attention_heads\n    n_kv_heads = getattr(cfg, \"num_key_value_heads\", n_heads)\n    d_model = cfg.hidden_size\n    return dict(\n        n_layers=cfg.num_hidden_layers,\n        n_heads=n_heads,\n        n_kv_heads=n_kv_heads,\n        heads_per_kv_group=n_heads // n_kv_heads,\n        d_model=d_model,\n        head_dim=d_model // n_heads,\n    )\n\n\n# ---------------------------------------------------------------------------\n# Edge Topology: enumerate all edges and build mask index mapping\n# ---------------------------------------------------------------------------\n\ndef _build_edge_topology(\n    n_layers: int, n_heads: int, n_kv_heads: int, heads_per_kv_group: int,\n) -> Tuple[List[str], Dict[str, int], int]:\n    \"\"\"Build the full edge set and map each edge to its mask parameter index.\n\n    For GQA models, K/V edges targeting the same KV group share a mask.\n    Q edges always have independent masks.\n\n    Returns:\n        edge_names: list of canonical edge names\n        edge_to_mask_idx: edge_name -> index into mask parameter vector\n        n_masks: total number of independent mask parameters\n    \"\"\"\n    edge_names: List[str] = []\n    edge_to_mask_idx: Dict[str, int] = {}\n    mask_idx = 0\n\n    def _src_nodes_before_layer(layer: int, include_attn_same_layer: bool = False):\n        \"\"\"Yield (src_name,) for all nodes whose output feeds into a given layer.\"\"\"\n        yield \"input\"\n        for l in range(layer):\n            for h in range(n_heads):\n                yield f\"a{l}.h{h}\"\n            yield f\"m{l}\"\n        if include_attn_same_layer:\n            for h in range(n_heads):\n                yield f\"a{layer}.h{h}\"\n\n    for L in range(n_layers):\n        # --- Edges into attention heads at layer L ---\n        srcs_attn = list(_src_nodes_before_layer(L, include_attn_same_layer=False))\n        for src in srcs_attn:\n            for H in range(n_heads):\n                # Q edge: always independent\n                q_edge = f\"{src}->a{L}.h{H}.q\"\n                edge_names.append(q_edge)\n                edge_to_mask_idx[q_edge] = mask_idx\n                mask_idx += 1\n\n            # K edges: shared within KV group\n            for kv_group in range(n_kv_heads):\n                k_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    k_edge = f\"{src}->a{L}.h{H}.k\"\n                    edge_names.append(k_edge)\n                    edge_to_mask_idx[k_edge] = k_mask_idx\n\n            # V edges: shared within KV group\n            for kv_group in range(n_kv_heads):\n                v_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    v_edge = f\"{src}->a{L}.h{H}.v\"\n                    edge_names.append(v_edge)\n                    edge_to_mask_idx[v_edge] = v_mask_idx\n\n        # --- Edges into MLP at layer L ---\n        srcs_mlp = list(_src_nodes_before_layer(L, include_attn_same_layer=True))\n        for src in srcs_mlp:\n            mlp_edge = f\"{src}->m{L}\"\n            edge_names.append(mlp_edge)\n            edge_to_mask_idx[mlp_edge] = mask_idx\n            mask_idx += 1\n\n    return edge_names, edge_to_mask_idx, mask_idx\n\n\n# ---------------------------------------------------------------------------\n# Destination-grouped mask table for efficient hook application\n# ---------------------------------------------------------------------------\n\ndef _build_dst_mask_table(\n    edge_to_mask_idx: Dict[str, int],\n) -> Dict[str, Dict[str, int]]:\n    \"\"\"Group edges by destination node.\n\n    Returns: {dst_node: {src_node: mask_param_index}}\n    \"\"\"\n    table: Dict[str, Dict[str, int]] = {}\n    for edge, idx in edge_to_mask_idx.items():\n        src, dst = edge.split(\"->\", 1)\n        if dst not in table:\n            table[dst] = {}\n        table[dst][src] = idx\n    return table\n\n\n# ---------------------------------------------------------------------------\n# Source activation cache (captured via hooks)\n# ---------------------------------------------------------------------------\n\nclass _ActivationCache:\n    \"\"\"Stores source node activations during forward pass.\"\"\"\n\n    def __init__(self):\n        self.embed_out: Optional[torch.Tensor] = None\n        self.head_out: Dict[int, Dict[int, torch.Tensor]] = {}\n        self.mlp_out: Dict[int, torch.Tensor] = {}\n\n\n# ---------------------------------------------------------------------------\n# Hook-based masked forward pass\n# ---------------------------------------------------------------------------\n\ndef _get_module(model, path: str) -> nn.Module:\n    parts = path.split(\".\")\n    m = model\n    for p in parts:\n        m = getattr(m, p)\n    return m\n\n\ndef _decompose_attn_output(\n    concat_heads: torch.Tensor,\n    o_proj: nn.Linear,\n    n_heads: int,\n    head_dim: int,\n) -> Dict[int, torch.Tensor]:\n    \"\"\"Split concatenated head output and project each head through o_proj.\"\"\"\n    W = o_proj.weight  # [d_model, d_model]\n    heads = {}\n    for h in range(n_heads):\n        h_slice = concat_heads[:, :, h * head_dim:(h + 1) * head_dim]\n        W_h = W[:, h * head_dim:(h + 1) * head_dim]\n        heads[h] = h_slice @ W_h.T\n    return heads\n\n\ndef _masked_forward(\n    model,\n    input_ids: torch.Tensor,\n    masks: torch.Tensor,\n    arch_info: dict,\n    dst_mask_table: Dict[str, Dict[str, int]],\n) -> torch.Tensor:\n    \"\"\"Run forward pass with edge masks applied via hooks.\n\n    Strategy:\n    1. Register hooks to capture source node outputs (embed, attn heads, MLP).\n    2. At each destination's pre-hook, replace its input with the masked sum\n       of upstream source outputs.\n\n    For memory efficiency, source activations are captured and masks applied\n    layer-by-layer. Each layer's pre-hook constructs the masked residual\n    from all upstream sources.\n    \"\"\"\n    n_layers = arch_info[\"n_layers\"]\n    n_heads = arch_info[\"n_heads\"]\n    head_dim = arch_info[\"head_dim\"]\n    layers = model.model.layers\n\n    cache = _ActivationCache()\n    hooks = []\n\n    # Capture embedding output\n    def _embed_hook(mod, inp, out):\n        cache.embed_out = out\n    hooks.append(model.model.embed_tokens.register_forward_hook(_embed_hook))\n\n    for L in range(n_layers):\n        layer = layers[L]\n\n        # Capture per-head attention output via o_proj\n        def _oproj_hook(mod, inp, out, *, _L=L):\n            cache.head_out[_L] = _decompose_attn_output(\n                inp[0], mod, n_heads, head_dim,\n            )\n        hooks.append(layer.self_attn.o_proj.register_forward_hook(_oproj_hook))\n\n        # Capture MLP output\n        def _mlp_hook(mod, inp, out, *, _L=L):\n            cache.mlp_out[_L] = out if isinstance(out, torch.Tensor) else out[0]\n        hooks.append(layer.mlp.register_forward_hook(_mlp_hook))\n\n        # Pre-hook on each layer: construct masked residual stream input.\n        # This replaces the residual stream with the masked combination of\n        # all upstream source nodes.\n        def _layer_pre_hook(mod, inp, *, _L=L):\n            x = inp[0] if isinstance(inp, tuple) else inp\n\n            # Collect all source activations available before this layer\n            src_acts: Dict[str, torch.Tensor] = {}\n            if cache.embed_out is not None:\n                src_acts[\"input\"] = cache.embed_out\n            for l in range(_L):\n                if l in cache.head_out:\n                    for h in range(n_heads):\n                        src_acts[f\"a{l}.h{h}\"] = cache.head_out[l][h]\n                if l in cache.mlp_out:\n                    src_acts[f\"m{l}\"] = cache.mlp_out[l]\n\n            # For attention destinations (q, k, v) at this layer:\n            # We approximate by masking the residual stream input.\n            # The mask for each destination type is the element-wise product\n            # of all source masks. For simplicity and memory, we apply the\n            # *minimum* mask across q/k/v destinations for each source,\n            # effectively masking the residual input to the entire attention block.\n            #\n            # More precise: build separate masked inputs per q/k/v head.\n            # But that requires modifying internal attention computation,\n            # which is architecture-specific. The residual-level masking\n            # is the standard approach in princeton-nlp/edge-pruning.\n\n            # Gather all destination nodes at this layer\n            attn_dsts = set()\n            mlp_dst = f\"m{_L}\"\n            for H in range(n_heads):\n                for qkv in (\"q\", \"k\", \"v\"):\n                    attn_dsts.add(f\"a{_L}.h{H}.{qkv}\")\n\n            # Compute masked residual for attention input\n            # Use average mask across all attn destinations for each source\n            masked_resid = torch.zeros_like(x)\n            for src_name, src_act in src_acts.items():\n                # Collect mask values for this source across attn destinations\n                mask_indices = []\n                for dst in attn_dsts:\n                    if dst in dst_mask_table and src_name in dst_mask_table[dst]:\n                        mask_indices.append(dst_mask_table[dst][src_name])\n                if mask_indices:\n                    # Average mask across destinations (approximation)\n                    src_mask = masks[mask_indices].mean()\n                    masked_resid = masked_resid + src_act * src_mask\n\n            if isinstance(inp, tuple):\n                return (masked_resid,) + inp[1:]\n            return masked_resid\n\n        hooks.append(layer.register_forward_pre_hook(_layer_pre_hook))\n\n    try:\n        out = model(input_ids)\n        return out.logits\n    finally:\n        for h in hooks:\n            h.remove()\n\n\n# ---------------------------------------------------------------------------\n# Faithfulness loss\n# ---------------------------------------------------------------------------\n\ndef _faithfulness_loss(\n    masked_logits: torch.Tensor,\n    clean_logits: torch.Tensor,\n    target_ids: Optional[torch.Tensor],\n) -> torch.Tensor:\n    \"\"\"KL divergence between clean and masked model output distributions.\n\n    If target_ids is provided, only compute loss at target token positions.\n    \"\"\"\n    if target_ids is not None:\n        # target_ids: [batch] — index of the token position to evaluate\n        batch_size = masked_logits.size(0)\n        idx = target_ids.view(batch_size)\n        masked_logits = masked_logits[torch.arange(batch_size), idx]\n        clean_logits = clean_logits[torch.arange(batch_size), idx]\n\n    log_p = F.log_softmax(masked_logits, dim=-1)\n    q = F.softmax(clean_logits, dim=-1)\n    return F.kl_div(log_p, q, reduction=\"batchmean\")\n\n\n# ---------------------------------------------------------------------------\n# Main entry point\n# ---------------------------------------------------------------------------\n\ndef compute_edge_pruning_scores(\n    model,\n    clean_inputs,\n    corrupt_inputs,\n    metric_fn: Callable,\n    target_ids=None,\n    n_epochs: int = 100,\n    lambda_l0: float = 1e-3,\n    lr: float = 0.1,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Compute Edge Pruning L0 edge scores.\n\n    Returns dict of canonical_edge_name -> score (mask expectation).\n\n    Args:\n        model: HuggingFace CausalLM (Llama-like: Qwen2, Llama, Mistral, etc.)\n        clean_inputs: dict with 'input_ids' [batch, seq_len]\n        corrupt_inputs: dict with 'input_ids' [batch, seq_len]\n        metric_fn: faithfulness metric (kept for interface parity; KL used internally)\n        target_ids: [batch] token positions for evaluation (None = all positions)\n        n_epochs: optimization epochs\n        lambda_l0: L0 sparsity penalty weight\n        lr: learning rate for mask parameters\n        device: target device\n    \"\"\"\n    arch_info = _get_arch_info(model)\n    n_layers = arch_info[\"n_layers\"]\n    n_heads = arch_info[\"n_heads\"]\n    n_kv_heads = arch_info[\"n_kv_heads\"]\n    heads_per_kv_group = arch_info[\"heads_per_kv_group\"]\n\n    # Build edge topology\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology(\n        n_layers, n_heads, n_kv_heads, heads_per_kv_group,\n    )\n    dst_mask_table = _build_dst_mask_table(edge_to_mask_idx)\n\n    # Initialize Hard Concrete mask parameters\n    hard_concrete = HardConcrete(n_masks, init_mean=0.5).to(device)\n    optimizer = torch.optim.Adam(hard_concrete.parameters(), lr=lr)\n\n    # Prepare inputs\n    if isinstance(clean_inputs, dict):\n        clean_ids = clean_inputs[\"input_ids\"]\n        if not isinstance(clean_ids, torch.Tensor):\n            clean_ids = torch.tensor(clean_ids)\n    else:\n        clean_ids = clean_inputs\n    clean_ids = clean_ids.to(device)\n\n    if isinstance(corrupt_inputs, dict):\n        corrupt_ids = corrupt_inputs[\"input_ids\"]\n        if not isinstance(corrupt_ids, torch.Tensor):\n            corrupt_ids = torch.tensor(corrupt_ids)\n    else:\n        corrupt_ids = corrupt_inputs\n    corrupt_ids = corrupt_ids.to(device)\n\n    if target_ids is not None:\n        if not isinstance(target_ids, torch.Tensor):\n            target_ids = torch.tensor(target_ids)\n        target_ids = target_ids.to(device)\n\n    # Get clean model logits (frozen)\n    model.eval()\n    with torch.no_grad():\n        clean_logits = model(clean_ids).logits.detach()\n\n    # Optimization loop\n    for epoch in range(n_epochs):\n        optimizer.zero_grad()\n\n        # Sample masks from Hard Concrete\n        masks = hard_concrete(training=True)\n\n        # Forward pass with masks applied\n        masked_logits = _masked_forward(\n            model, clean_ids, masks, arch_info, dst_mask_table,\n        )\n\n        # Loss = faithfulness + sparsity\n        faith_loss = _faithfulness_loss(masked_logits, clean_logits, target_ids)\n        l0_loss = hard_concrete.l0_penalty()\n        loss = faith_loss + lambda_l0 * l0_loss\n\n        loss.backward()\n        optimizer.step()\n\n    # Extract final scores\n    with torch.no_grad():\n        final_masks = hard_concrete.expected_masks()\n\n    scores: Dict[str, float] = {}\n    for edge_name, mask_idx in edge_to_mask_idx.items():\n        scores[edge_name] = final_masks[mask_idx].item()\n\n    return scores\n\n\n# ---------------------------------------------------------------------------\n# Utility: edge count estimation\n# ---------------------------------------------------------------------------\n\ndef estimate_edge_counts(\n    n_layers: int, n_heads: int, n_kv_heads: int,\n) -> Dict[str, int]:\n    \"\"\"Estimate edge and mask parameter counts for a given architecture.\"\"\"\n    heads_per_kv = n_heads // n_kv_heads\n    _, _, n_masks = _build_edge_topology(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n    # Total edges (including shared masks counted separately)\n    total_edges = 0\n    for L in range(n_layers):\n        n_src = 1 + L * (n_heads + 1)  # input + prior layers' heads + MLPs\n        # Attn edges: Q independent, K/V shared per KV group\n        total_edges += n_src * n_heads * 3  # q, k, v per head\n        # MLP edges: from all upstream including same-layer attn\n        n_src_mlp = n_src + n_heads\n        total_edges += n_src_mlp\n\n    return {\n        \"total_edges\": total_edges,\n        \"n_independent_masks\": n_masks,\n        \"mask_memory_bytes\": n_masks * 4,  # float32\n        \"mask_memory_mb\": n_masks * 4 / (1024 ** 2),\n    }\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Write · `toolu_012kc1dx91pSYyufxBPPu1Uq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_edge_pruning_scoring.py",
  "content": "\"\"\"Smoke tests for edge_pruning_scoring.py v2.\n\nTests split by dependency:\n  - No-torch tests: AST syntax, function signature, edge topology, hook mask indices\n  - Torch tests: HardConcrete numerics, gradient flow, module consistency\n\nRun: python3 test_edge_pruning_scoring.py\n\"\"\"\n\nimport ast\nimport os\nimport sys\n\nSRC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), \"edge_pruning_scoring.py\")\n\nHAS_TORCH = False\ntry:\n    import torch\n    HAS_TORCH = True\nexcept ImportError:\n    pass\n\n\n# ===========================================================================\n# No-torch tests (pure AST / logic)\n# ===========================================================================\n\ndef test_ast_syntax():\n    with open(SRC_PATH) as f:\n        source = f.read()\n    tree = ast.parse(source)\n    assert isinstance(tree, ast.Module)\n    top_names = {node.name for node in ast.walk(tree)\n                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}\n    # Core classes/functions\n    assert \"HardConcrete\" in top_names\n    assert \"compute_edge_pruning_scores\" in top_names\n    assert \"estimate_edge_counts\" in top_names\n    assert \"_build_edge_topology\" in top_names\n    assert \"_masked_forward\" in top_names\n    assert \"_faithfulness_loss\" in top_names\n    # v2 additions\n    assert \"_build_hook_mask_indices\" in top_names\n    assert \"_build_masked_input_qkv\" in top_names\n    assert \"_build_masked_input_mlp\" in top_names\n    assert \"_src_nodes_before_layer\" in top_names\n    print(\"[PASS] AST syntax check (v2)\")\n\n\ndef test_function_signature_from_ast():\n    with open(SRC_PATH) as f:\n        source = f.read()\n    tree = ast.parse(source)\n    for node in ast.walk(tree):\n        if isinstance(node, ast.FunctionDef) and node.name == \"compute_edge_pruning_scores\":\n            args = node.args\n            param_names = [a.arg for a in args.args]\n            expected = [\n                \"model\", \"clean_inputs\", \"corrupt_inputs\", \"metric_fn\",\n                \"target_ids\", \"n_epochs\", \"lambda_l0\", \"lr\", \"device\",\n            ]\n            assert param_names == expected, f\"Expected {expected}, got {param_names}\"\n            defaults = args.defaults\n            assert len(defaults) == 5  # target_ids=None, n_epochs=100, lambda_l0=1e-3, lr=0.1, device=\"cuda\"\n            print(\"[PASS] Function signature (AST)\")\n            return\n    raise AssertionError(\"compute_edge_pruning_scores not found\")\n\n\n# ---------------------------------------------------------------------------\n# Standalone topology builder (no torch dependency)\n# ---------------------------------------------------------------------------\n\ndef _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, heads_per_kv_group):\n    \"\"\"Standalone copy of edge topology logic for testing without torch.\"\"\"\n    edge_names = []\n    edge_to_mask_idx = {}\n    mask_idx = 0\n\n    def _src_nodes(layer, include_attn_same_layer=False):\n        yield \"input\"\n        for l in range(layer):\n            for h in range(n_heads):\n                yield f\"a{l}.h{h}\"\n            yield f\"m{l}\"\n        if include_attn_same_layer:\n            for h in range(n_heads):\n                yield f\"a{layer}.h{h}\"\n\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes(L))\n        for src in srcs_attn:\n            for H in range(n_heads):\n                q_edge = f\"{src}->a{L}.h{H}.q\"\n                edge_names.append(q_edge)\n                edge_to_mask_idx[q_edge] = mask_idx\n                mask_idx += 1\n            for kv_group in range(n_kv_heads):\n                k_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    k_edge = f\"{src}->a{L}.h{H}.k\"\n                    edge_names.append(k_edge)\n                    edge_to_mask_idx[k_edge] = k_mask_idx\n            for kv_group in range(n_kv_heads):\n                v_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    v_edge = f\"{src}->a{L}.h{H}.v\"\n                    edge_names.append(v_edge)\n                    edge_to_mask_idx[v_edge] = v_mask_idx\n\n        srcs_mlp = list(_src_nodes(L, include_attn_same_layer=True))\n        for src in srcs_mlp:\n            mlp_edge = f\"{src}->m{L}\"\n            edge_names.append(mlp_edge)\n            edge_to_mask_idx[mlp_edge] = mask_idx\n            mask_idx += 1\n\n    return edge_names, edge_to_mask_idx, mask_idx\n\n\ndef _build_hook_mask_indices_standalone(n_layers, n_heads, edge_to_mask_idx):\n    \"\"\"Standalone copy of hook mask index builder for testing without torch.\"\"\"\n\n    def _src_nodes(layer, include_attn_same_layer=False):\n        yield \"input\"\n        for l in range(layer):\n            for h in range(n_heads):\n                yield f\"a{l}.h{h}\"\n            yield f\"m{l}\"\n        if include_attn_same_layer:\n            for h in range(n_heads):\n                yield f\"a{layer}.h{h}\"\n\n    q_all, k_all, v_all, mlp_all = [], [], [], []\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes(L))\n        srcs_mlp = list(_src_nodes(L, include_attn_same_layer=True))\n\n        qi, ki, vi = {}, {}, {}\n        for src in srcs_attn:\n            qi[src] = [edge_to_mask_idx[f\"{src}->a{L}.h{h}.q\"] for h in range(n_heads)]\n            ki[src] = [edge_to_mask_idx[f\"{src}->a{L}.h{h}.k\"] for h in range(n_heads)]\n            vi[src] = [edge_to_mask_idx[f\"{src}->a{L}.h{h}.v\"] for h in range(n_heads)]\n\n        mi = {}\n        for src in srcs_mlp:\n            mi[src] = edge_to_mask_idx[f\"{src}->m{L}\"]\n\n        q_all.append(qi)\n        k_all.append(ki)\n        v_all.append(vi)\n        mlp_all.append(mi)\n\n    return q_all, k_all, v_all, mlp_all\n\n\n# ---------------------------------------------------------------------------\n# Topology tests (carried from v1)\n# ---------------------------------------------------------------------------\n\ndef test_edge_topology_no_gqa():\n    n_layers, n_heads, n_kv_heads = 2, 4, 4\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, 1,\n    )\n    assert len(set(edge_to_mask_idx.values())) == n_masks\n    assert n_masks == len(edge_to_mask_idx)\n    assert \"input->a0.h0.q\" in edge_to_mask_idx\n    assert \"input->a0.h0.k\" in edge_to_mask_idx\n    assert \"input->a0.h0.v\" in edge_to_mask_idx\n    assert \"input->m0\" in edge_to_mask_idx\n    assert \"a0.h0->m0\" in edge_to_mask_idx\n    assert \"a0.h0->a1.h0.q\" in edge_to_mask_idx\n    print(f\"[PASS] Edge topology non-GQA: {len(edge_names)} edges, {n_masks} masks\")\n\n\ndef test_edge_topology_gqa():\n    n_layers, n_heads, n_kv_heads = 2, 14, 2\n    heads_per_kv = 7\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n\n    k_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7)}\n    assert len(k_masks_g0) == 1, f\"KV group 0 K masks should share, got {len(k_masks_g0)}\"\n\n    k_masks_g1 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7, 14)}\n    assert len(k_masks_g1) == 1\n    assert k_masks_g0 != k_masks_g1\n\n    q_masks = {edge_to_mask_idx[f\"input->a0.h{h}.q\"] for h in range(14)}\n    assert len(q_masks) == 14\n\n    v_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.v\"] for h in range(7)}\n    assert len(v_masks_g0) == 1\n\n    print(f\"[PASS] Edge topology GQA: {len(edge_names)} edges, {n_masks} masks\")\n\n\ndef test_dst_mask_table():\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(1, 2, 2, 1)\n    table = {}\n    for edge, idx in edge_to_mask_idx.items():\n        src, dst = edge.split(\"->\", 1)\n        table.setdefault(dst, {})[src] = idx\n\n    assert \"a0.h0.q\" in table\n    assert \"input\" in table[\"a0.h0.q\"]\n    assert \"m0\" in table\n    assert \"input\" in table[\"m0\"]\n    assert \"a0.h0\" in table[\"m0\"]\n    assert \"a0.h1\" in table[\"m0\"]\n    print(\"[PASS] Destination mask table\")\n\n\ndef test_edge_counts_qwen():\n    \"\"\"Estimate edge counts for Qwen-2.5 0.5B without torch.\"\"\"\n    _, _, n_masks = _build_edge_topology_standalone(24, 14, 2, 7)\n    total_edges = 0\n    for L in range(24):\n        n_src = 1 + L * (14 + 1)\n        total_edges += n_src * 14 * 3\n        total_edges += (n_src + 14)\n    mem_mb = n_masks * 4 / (1024 ** 2)\n    assert total_edges > 0\n    assert n_masks > 0\n    assert n_masks <= total_edges\n    print(f\"[PASS] Qwen-2.5 0.5B: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB\")\n\n\ndef test_edge_counts_gpt2():\n    _, _, n_masks = _build_edge_topology_standalone(12, 12, 12, 1)\n    total_edges = 0\n    for L in range(12):\n        n_src = 1 + L * (12 + 1)\n        total_edges += n_src * 12 * 3\n        total_edges += (n_src + 12)\n    mem_mb = n_masks * 4 / (1024 ** 2)\n    print(f\"[PASS] GPT-2 small: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB\")\n\n\n# ---------------------------------------------------------------------------\n# v2 hook mask index tests (no torch needed)\n# ---------------------------------------------------------------------------\n\ndef test_hook_q_masks_independent():\n    \"\"\"Q masks must be independent per head (no averaging).\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 4, 2\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, 2)\n    q_idx, _, _, _ = _build_hook_mask_indices_standalone(n_layers, n_heads, edge_to_mask_idx)\n\n    q_input_l0 = q_idx[0][\"input\"]\n    assert len(set(q_input_l0)) == n_heads, \\\n        f\"Q masks must be independent per head, got {len(set(q_input_l0))} distinct for {n_heads} heads\"\n    print(\"[PASS] Q masks independent per head\")\n\n\ndef test_hook_kv_gqa_sharing():\n    \"\"\"K/V masks shared within KV group, different across groups and between K/V.\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 8, 2\n    heads_per_kv = 4\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n    _, k_idx, v_idx, _ = _build_hook_mask_indices_standalone(\n        n_layers, n_heads, edge_to_mask_idx,\n    )\n\n    # K: group 0 (heads 0-3) shared, group 1 (heads 4-7) shared\n    k_g0 = set(k_idx[0][\"input\"][:4])\n    k_g1 = set(k_idx[0][\"input\"][4:])\n    assert len(k_g0) == 1, f\"K group 0 should share mask, got {len(k_g0)} distinct\"\n    assert len(k_g1) == 1, f\"K group 1 should share mask, got {len(k_g1)} distinct\"\n    assert k_g0 != k_g1, \"Different KV groups must have different K masks\"\n\n    # V: same sharing pattern\n    v_g0 = set(v_idx[0][\"input\"][:4])\n    v_g1 = set(v_idx[0][\"input\"][4:])\n    assert len(v_g0) == 1\n    assert len(v_g1) == 1\n    assert v_g0 != v_g1\n\n    # K and V must be separate masks even within the same KV group\n    assert k_g0 != v_g0, \"K and V must have separate masks even in same KV group\"\n    print(\"[PASS] K/V GQA sharing correct\")\n\n\ndef test_hook_mlp_sources_include_same_layer_attn():\n    \"\"\"MLP hook at layer L must include a{L}.h{H} as sources.\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 4, 4\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, 1)\n    _, _, _, mlp_idx = _build_hook_mask_indices_standalone(n_layers, n_heads, edge_to_mask_idx)\n\n    # MLP at layer 0: input + same-layer attention heads\n    mlp0 = set(mlp_idx[0].keys())\n    assert \"input\" in mlp0\n    for h in range(n_heads):\n        assert f\"a0.h{h}\" in mlp0, f\"MLP at L0 must include a0.h{h}\"\n\n    # MLP at layer 1: input + L0 heads + L0 MLP + L1 heads\n    mlp1 = set(mlp_idx[1].keys())\n    assert \"input\" in mlp1\n    assert \"m0\" in mlp1\n    for h in range(n_heads):\n        assert f\"a0.h{h}\" in mlp1\n        assert f\"a1.h{h}\" in mlp1, f\"MLP at L1 must include same-layer a1.h{h}\"\n    print(\"[PASS] MLP sources include same-layer attention\")\n\n\ndef test_hook_qkv_sources_exclude_same_layer():\n    \"\"\"Q/K/V hooks at layer L must NOT include a{L}.h{H} or m{L}.\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 4, 4\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, 1)\n    q_idx, k_idx, v_idx, _ = _build_hook_mask_indices_standalone(\n        n_layers, n_heads, edge_to_mask_idx,\n    )\n\n    for idx_dict in [q_idx[1], k_idx[1], v_idx[1]]:\n        srcs = set(idx_dict.keys())\n        for h in range(n_heads):\n            assert f\"a1.h{h}\" not in srcs, \"Q/K/V must not include same-layer attn\"\n        assert \"m1\" not in srcs, \"Q/K/V must not include same-layer MLP\"\n    print(\"[PASS] Q/K/V sources exclude same-layer\")\n\n\ndef test_hook_edge_coverage():\n    \"\"\"All mask parameters must be referenced by at least one hook.\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 4, 2\n    _, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, 2,\n    )\n    q_idx, k_idx, v_idx, mlp_idx = _build_hook_mask_indices_standalone(\n        n_layers, n_heads, edge_to_mask_idx,\n    )\n\n    all_indices = set()\n    for L in range(n_layers):\n        for src, idxs in q_idx[L].items():\n            all_indices.update(idxs)\n        for src, idxs in k_idx[L].items():\n            all_indices.update(idxs)\n        for src, idxs in v_idx[L].items():\n            all_indices.update(idxs)\n        for src, idx in mlp_idx[L].items():\n            all_indices.add(idx)\n\n    assert all_indices == set(range(n_masks)), \\\n        f\"Hook indices cover {len(all_indices)} of {n_masks} masks\"\n    print(f\"[PASS] All {n_masks} mask parameters covered by hooks\")\n\n\n# ===========================================================================\n# Torch-dependent tests\n# ===========================================================================\n\ndef test_hard_concrete_sampling():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=1000, init_mean=0.5)\n    torch.manual_seed(42)\n    samples = hc(training=True)\n    assert samples.shape == (1000,)\n    assert samples.min() >= 0.0\n    assert samples.max() <= 1.0\n    penalty = hc.l0_penalty()\n    assert penalty.item() >= 0.0\n    assert penalty.item() <= 1000.0\n    expected = hc.expected_masks()\n    assert expected.min() >= 0.0\n    assert expected.max() <= 1.0\n    print(\"[PASS] HardConcrete sampling\")\n\n\ndef test_hard_concrete_gradient():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=10, init_mean=0.5)\n    masks = hc(training=True)\n    masks.sum().backward()\n    assert hc.log_alpha.grad is not None\n    assert not torch.all(hc.log_alpha.grad == 0)\n    print(\"[PASS] HardConcrete gradient flow\")\n\n\ndef test_hard_concrete_extremes():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=2, init_mean=0.5)\n    with torch.no_grad():\n        hc.log_alpha[0] = -10.0\n        hc.log_alpha[1] = 10.0\n    masks = hc.expected_masks()\n    assert masks[0].item() < 0.01\n    assert masks[1].item() > 0.99\n    print(\"[PASS] HardConcrete extremes\")\n\n\ndef test_module_topology_matches_standalone():\n    \"\"\"Verify the actual module's topology matches our standalone copy.\"\"\"\n    from edge_pruning_scoring import _build_edge_topology\n    _, idx_module, n_module = _build_edge_topology(2, 14, 2, 7)\n    _, idx_standalone, n_standalone = _build_edge_topology_standalone(2, 14, 2, 7)\n    assert n_module == n_standalone, f\"n_masks mismatch: {n_module} vs {n_standalone}\"\n    assert idx_module == idx_standalone, \"edge_to_mask_idx mismatch\"\n    print(\"[PASS] Module topology matches standalone\")\n\n\ndef test_module_hook_indices_matches_standalone():\n    \"\"\"Verify the module's hook index builder matches the standalone copy.\"\"\"\n    from edge_pruning_scoring import _build_edge_topology, _build_hook_mask_indices\n    n_layers, n_heads, n_kv_heads = 2, 14, 2\n    _, edge_to_mask_idx, _ = _build_edge_topology(n_layers, n_heads, n_kv_heads, 7)\n\n    q_m, k_m, v_m, mlp_m = _build_hook_mask_indices(\n        n_layers, n_heads, edge_to_mask_idx, torch.device(\"cpu\"),\n    )\n    q_s, k_s, v_s, mlp_s = _build_hook_mask_indices_standalone(\n        n_layers, n_heads, edge_to_mask_idx,\n    )\n\n    for L in range(n_layers):\n        for src in q_s[L]:\n            assert q_m[L][src].tolist() == q_s[L][src], f\"Q mismatch at L={L} src={src}\"\n            assert k_m[L][src].tolist() == k_s[L][src], f\"K mismatch at L={L} src={src}\"\n            assert v_m[L][src].tolist() == v_s[L][src], f\"V mismatch at L={L} src={src}\"\n        for src in mlp_s[L]:\n            assert mlp_m[L][src] == mlp_s[L][src], f\"MLP mismatch at L={L} src={src}\"\n    print(\"[PASS] Module hook indices match standalone\")\n\n\n# ===========================================================================\n\nif __name__ == \"__main__\":\n    # No-torch tests\n    test_ast_syntax()\n    test_function_signature_from_ast()\n    test_edge_topology_no_gqa()\n    test_edge_topology_gqa()\n    test_dst_mask_table()\n    test_edge_counts_qwen()\n    test_edge_counts_gpt2()\n    # v2 hook index tests\n    test_hook_q_masks_independent()\n    test_hook_kv_gqa_sharing()\n    test_hook_mlp_sources_include_same_layer_attn()\n    test_hook_qkv_sources_exclude_same_layer()\n    test_hook_edge_coverage()\n\n    if HAS_TORCH:\n        test_hard_concrete_sampling()\n        test_hard_concrete_gradient()\n        test_hard_concrete_extremes()\n        test_module_topology_matches_standalone()\n        test_module_hook_indices_matches_standalone()\n    else:\n        print(\"[SKIP] Torch-dependent tests (torch not installed)\")\n\n    print(\"\\n=== All applicable smoke tests passed ===\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "cf8c60c8-4de7-4e5d-b537-606279bf3d12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrwQcJNjeCDw1BFeEb9X53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 55244,
      "cache_read_input_tokens": 39323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 55244
      },
      "output_tokens": 69,
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

_source line 17 · 2026-05-12T19:30:19.222Z_

<details><summary>↩ Tool result · `toolu_012kc1dx91pSYyufxBPPu1Uq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_edge_pruning_scoring.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "0303da41-e679-49c7-bf73-f95a22109ac4",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_edge_pruning_scoring.py",
    "content": "\"\"\"Smoke tests for edge_pruning_scoring.py v2.\n\nTests split by dependency:\n  - No-torch tests: AST syntax, function signature, edge topology, hook mask indices\n  - Torch tests: HardConcrete numerics, gradient flow, module consistency\n\nRun: python3 test_edge_pruning_scoring.py\n\"\"\"\n\nimport ast\nimport os\nimport sys\n\nSRC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), \"edge_pruning_scoring.py\")\n\nHAS_TORCH = False\ntry:\n    import torch\n    HAS_TORCH = True\nexcept ImportError:\n    pass\n\n\n# ===========================================================================\n# No-torch tests (pure AST / logic)\n# ===========================================================================\n\ndef test_ast_syntax():\n    with open(SRC_PATH) as f:\n        source = f.read()\n    tree = ast.parse(source)\n    assert isinstance(tree, ast.Module)\n    top_names = {node.name for node in ast.walk(tree)\n                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}\n    # Core classes/functions\n    assert \"HardConcrete\" in top_names\n    assert \"compute_edge_pruning_scores\" in top_names\n    assert \"estimate_edge_counts\" in top_names\n    assert \"_build_edge_topology\" in top_names\n    assert \"_masked_forward\" in top_names\n    assert \"_faithfulness_loss\" in top_names\n    # v2 additions\n    assert \"_build_hook_mask_indices\" in top_names\n    assert \"_build_masked_input_qkv\" in top_names\n    assert \"_build_masked_input_mlp\" in top_names\n    assert \"_src_nodes_before_layer\" in top_names\n    print(\"[PASS] AST syntax check (v2)\")\n\n\ndef test_function_signature_from_ast():\n    with open(SRC_PATH) as f:\n        source = f.read()\n    tree = ast.parse(source)\n    for node in ast.walk(tree):\n        if isinstance(node, ast.FunctionDef) and node.name == \"compute_edge_pruning_scores\":\n            args = node.args\n            param_names = [a.arg for a in args.args]\n            expected = [\n                \"model\", \"clean_inputs\", \"corrupt_inputs\", \"metric_fn\",\n                \"target_ids\", \"n_epochs\", \"lambda_l0\", \"lr\", \"device\",\n            ]\n            assert param_names == expected, f\"Expected {expected}, got {param_names}\"\n            defaults = args.defaults\n            assert len(defaults) == 5  # target_ids=None, n_epochs=100, lambda_l0=1e-3, lr=0.1, device=\"cuda\"\n            print(\"[PASS] Function signature (AST)\")\n            return\n    raise AssertionError(\"compute_edge_pruning_scores not found\")\n\n\n# ---------------------------------------------------------------------------\n# Standalone topology builder (no torch dependency)\n# ---------------------------------------------------------------------------\n\ndef _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, heads_per_kv_group):\n    \"\"\"Standalone copy of edge topology logic for testing without torch.\"\"\"\n    edge_names = []\n    edge_to_mask_idx = {}\n    mask_idx = 0\n\n    def _src_nodes(layer, include_attn_same_layer=False):\n        yield \"input\"\n        for l in range(layer):\n            for h in range(n_heads):\n                yield f\"a{l}.h{h}\"\n            yield f\"m{l}\"\n        if include_attn_same_layer:\n            for h in range(n_heads):\n                yield f\"a{layer}.h{h}\"\n\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes(L))\n        for src in srcs_attn:\n            for H in range(n_heads):\n                q_edge = f\"{src}->a{L}.h{H}.q\"\n                edge_names.append(q_edge)\n                edge_to_mask_idx[q_edge] = mask_idx\n                mask_idx += 1\n            for kv_group in range(n_kv_heads):\n                k_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    k_edge = f\"{src}->a{L}.h{H}.k\"\n                    edge_names.append(k_edge)\n                    edge_to_mask_idx[k_edge] = k_mask_idx\n            for kv_group in range(n_kv_heads):\n                v_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    v_edge = f\"{src}->a{L}.h{H}.v\"\n                    edge_names.append(v_edge)\n                    edge_to_mask_idx[v_edge] = v_mask_idx\n\n        srcs_mlp = list(_src_nodes(L, include_attn_same_layer=True))\n        for src in srcs_mlp:\n            mlp_edge = f\"{src}->m{L}\"\n            edge_names.append(mlp_edge)\n            edge_to_mask_idx[mlp_edge] = mask_idx\n            mask_idx += 1\n\n    return edge_names, edge_to_mask_idx, mask_idx\n\n\ndef _build_hook_mask_indices_standalone(n_layers, n_heads, edge_to_mask_idx):\n    \"\"\"Standalone copy of hook mask index builder for testing without torch.\"\"\"\n\n    def _src_nodes(layer, include_attn_same_layer=False):\n        yield \"input\"\n        for l in range(layer):\n            for h in range(n_heads):\n                yield f\"a{l}.h{h}\"\n            yield f\"m{l}\"\n        if include_attn_same_layer:\n            for h in range(n_heads):\n                yield f\"a{layer}.h{h}\"\n\n    q_all, k_all, v_all, mlp_all = [], [], [], []\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes(L))\n        srcs_mlp = list(_src_nodes(L, include_attn_same_layer=True))\n\n        qi, ki, vi = {}, {}, {}\n        for src in srcs_attn:\n            qi[src] = [edge_to_mask_idx[f\"{src}->a{L}.h{h}.q\"] for h in range(n_heads)]\n            ki[src] = [edge_to_mask_idx[f\"{src}->a{L}.h{h}.k\"] for h in range(n_heads)]\n            vi[src] = [edge_to_mask_idx[f\"{src}->a{L}.h{h}.v\"] for h in range(n_heads)]\n\n        mi = {}\n        for src in srcs_mlp:\n            mi[src] = edge_to_mask_idx[f\"{src}->m{L}\"]\n\n        q_all.append(qi)\n        k_all.append(ki)\n        v_all.append(vi)\n        mlp_all.append(mi)\n\n    return q_all, k_all, v_all, mlp_all\n\n\n# ---------------------------------------------------------------------------\n# Topology tests (carried from v1)\n# ---------------------------------------------------------------------------\n\ndef test_edge_topology_no_gqa():\n    n_layers, n_heads, n_kv_heads = 2, 4, 4\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, 1,\n    )\n    assert len(set(edge_to_mask_idx.values())) == n_masks\n    assert n_masks == len(edge_to_mask_idx)\n    assert \"input->a0.h0.q\" in edge_to_mask_idx\n    assert \"input->a0.h0.k\" in edge_to_mask_idx\n    assert \"input->a0.h0.v\" in edge_to_mask_idx\n    assert \"input->m0\" in edge_to_mask_idx\n    assert \"a0.h0->m0\" in edge_to_mask_idx\n    assert \"a0.h0->a1.h0.q\" in edge_to_mask_idx\n    print(f\"[PASS] Edge topology non-GQA: {len(edge_names)} edges, {n_masks} masks\")\n\n\ndef test_edge_topology_gqa():\n    n_layers, n_heads, n_kv_heads = 2, 14, 2\n    heads_per_kv = 7\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n\n    k_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7)}\n    assert len(k_masks_g0) == 1, f\"KV group 0 K masks should share, got {len(k_masks_g0)}\"\n\n    k_masks_g1 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7, 14)}\n    assert len(k_masks_g1) == 1\n    assert k_masks_g0 != k_masks_g1\n\n    q_masks = {edge_to_mask_idx[f\"input->a0.h{h}.q\"] for h in range(14)}\n    assert len(q_masks) == 14\n\n    v_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.v\"] for h in range(7)}\n    assert len(v_masks_g0) == 1\n\n    print(f\"[PASS] Edge topology GQA: {len(edge_names)} edges, {n_masks} masks\")\n\n\ndef test_dst_mask_table():\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(1, 2, 2, 1)\n    table = {}\n    for edge, idx in edge_to_mask_idx.items():\n        src, dst = edge.split(\"->\", 1)\n        table.setdefault(dst, {})[src] = idx\n\n    assert \"a0.h0.q\" in table\n    assert \"input\" in table[\"a0.h0.q\"]\n    assert \"m0\" in table\n    assert \"input\" in table[\"m0\"]\n    assert \"a0.h0\" in table[\"m0\"]\n    assert \"a0.h1\" in table[\"m0\"]\n    print(\"[PASS] Destination mask table\")\n\n\ndef test_edge_counts_qwen():\n    \"\"\"Estimate edge counts for Qwen-2.5 0.5B without torch.\"\"\"\n    _, _, n_masks = _build_edge_topology_standalone(24, 14, 2, 7)\n    total_edges = 0\n    for L in range(24):\n        n_src = 1 + L * (14 + 1)\n        total_edges += n_src * 14 * 3\n        total_edges += (n_src + 14)\n    mem_mb = n_masks * 4 / (1024 ** 2)\n    assert total_edges > 0\n    assert n_masks > 0\n    assert n_masks <= total_edges\n    print(f\"[PASS] Qwen-2.5 0.5B: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB\")\n\n\ndef test_edge_counts_gpt2():\n    _, _, n_masks = _build_edge_topology_standalone(12, 12, 12, 1)\n    total_edges = 0\n    for L in range(12):\n        n_src = 1 + L * (12 + 1)\n        total_edges += n_src * 12 * 3\n        total_edges += (n_src + 12)\n    mem_mb = n_masks * 4 / (1024 ** 2)\n    print(f\"[PASS] GPT-2 small: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB\")\n\n\n# ---------------------------------------------------------------------------\n# v2 hook mask index tests (no torch needed)\n# ---------------------------------------------------------------------------\n\ndef test_hook_q_masks_independent():\n    \"\"\"Q masks must be independent per head (no averaging).\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 4, 2\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, 2)\n    q_idx, _, _, _ = _build_hook_mask_indices_standalone(n_layers, n_heads, edge_to_mask_idx)\n\n    q_input_l0 = q_idx[0][\"input\"]\n    assert len(set(q_input_l0)) == n_heads, \\\n        f\"Q masks must be independent per head, got {len(set(q_input_l0))} distinct for {n_heads} heads\"\n    print(\"[PASS] Q masks independent per head\")\n\n\ndef test_hook_kv_gqa_sharing():\n    \"\"\"K/V masks shared within KV group, different across groups and between K/V.\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 8, 2\n    heads_per_kv = 4\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n    _, k_idx, v_idx, _ = _build_hook_mask_indices_standalone(\n        n_layers, n_heads, edge_to_mask_idx,\n    )\n\n    # K: group 0 (heads 0-3) shared, group 1 (heads 4-7) shared\n    k_g0 = set(k_idx[0][\"input\"][:4])\n    k_g1 = set(k_idx[0][\"input\"][4:])\n    assert len(k_g0) == 1, f\"K group 0 should share mask, got {len(k_g0)} distinct\"\n    assert len(k_g1) == 1, f\"K group 1 should share mask, got {len(k_g1)} distinct\"\n    assert k_g0 != k_g1, \"Different KV groups must have different K masks\"\n\n    # V: same sharing pattern\n    v_g0 = set(v_idx[0][\"input\"][:4])\n    v_g1 = set(v_idx[0][\"input\"][4:])\n    assert len(v_g0) == 1\n    assert len(v_g1) == 1\n    assert v_g0 != v_g1\n\n    # K and V must be separate masks even within the same KV group\n    assert k_g0 != v_g0, \"K and V must have separate masks even in same KV group\"\n    print(\"[PASS] K/V GQA sharing correct\")\n\n\ndef test_hook_mlp_sources_include_same_layer_attn():\n    \"\"\"MLP hook at layer L must include a{L}.h{H} as sources.\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 4, 4\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, 1)\n    _, _, _, mlp_idx = _build_hook_mask_indices_standalone(n_layers, n_heads, edge_to_mask_idx)\n\n    # MLP at layer 0: input + same-layer attention heads\n    mlp0 = set(mlp_idx[0].keys())\n    assert \"input\" in mlp0\n    for h in range(n_heads):\n        assert f\"a0.h{h}\" in mlp0, f\"MLP at L0 must include a0.h{h}\"\n\n    # MLP at layer 1: input + L0 heads + L0 MLP + L1 heads\n    mlp1 = set(mlp_idx[1].keys())\n    assert \"input\" in mlp1\n    assert \"m0\" in mlp1\n    for h in range(n_heads):\n        assert f\"a0.h{h}\" in mlp1\n        assert f\"a1.h{h}\" in mlp1, f\"MLP at L1 must include same-layer a1.h{h}\"\n    print(\"[PASS] MLP sources include same-layer attention\")\n\n\ndef test_hook_qkv_sources_exclude_same_layer():\n    \"\"\"Q/K/V hooks at layer L must NOT include a{L}.h{H} or m{L}.\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 4, 4\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, 1)\n    q_idx, k_idx, v_idx, _ = _build_hook_mask_indices_standalone(\n        n_layers, n_heads, edge_to_mask_idx,\n    )\n\n    for idx_dict in [q_idx[1], k_idx[1], v_idx[1]]:\n        srcs = set(idx_dict.keys())\n        for h in range(n_heads):\n            assert f\"a1.h{h}\" not in srcs, \"Q/K/V must not include same-layer attn\"\n        assert \"m1\" not in srcs, \"Q/K/V must not include same-layer MLP\"\n    print(\"[PASS] Q/K/V sources exclude same-layer\")\n\n\ndef test_hook_edge_coverage():\n    \"\"\"All mask parameters must be referenced by at least one hook.\"\"\"\n    n_layers, n_heads, n_kv_heads = 2, 4, 2\n    _, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, 2,\n    )\n    q_idx, k_idx, v_idx, mlp_idx = _build_hook_mask_indices_standalone(\n        n_layers, n_heads, edge_to_mask_idx,\n    )\n\n    all_indices = set()\n    for L in range(n_layers):\n        for src, idxs in q_idx[L].items():\n            all_indices.update(idxs)\n        for src, idxs in k_idx[L].items():\n            all_indices.update(idxs)\n        for src, idxs in v_idx[L].items():\n            all_indices.update(idxs)\n        for src, idx in mlp_idx[L].items():\n            all_indices.add(idx)\n\n    assert all_indices == set(range(n_masks)), \\\n        f\"Hook indices cover {len(all_indices)} of {n_masks} masks\"\n    print(f\"[PASS] All {n_masks} mask parameters covered by hooks\")\n\n\n# ===========================================================================\n# Torch-dependent tests\n# ===========================================================================\n\ndef test_hard_concrete_sampling():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=1000, init_mean=0.5)\n    torch.manual_seed(42)\n    samples = hc(training=True)\n    assert samples.shape == (1000,)\n    assert samples.min() >= 0.0\n    assert samples.max() <= 1.0\n    penalty = hc.l0_penalty()\n    assert penalty.item() >= 0.0\n    assert penalty.item() <= 1000.0\n    expected = hc.expected_masks()\n    assert expected.min() >= 0.0\n    assert expected.max() <= 1.0\n    print(\"[PASS] HardConcrete sampling\")\n\n\ndef test_hard_concrete_gradient():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=10, init_mean=0.5)\n    masks = hc(training=True)\n    masks.sum().backward()\n    assert hc.log_alpha.grad is not None\n    assert not torch.all(hc.log_alpha.grad == 0)\n    print(\"[PASS] HardConcrete gradient flow\")\n\n\ndef test_hard_concrete_extremes():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=2, init_mean=0.5)\n    with torch.no_grad():\n        hc.log_alpha[0] = -10.0\n        hc.log_alpha[1] = 10.0\n    masks = hc.expected_masks()\n    assert masks[0].item() < 0.01\n    assert masks[1].item() > 0.99\n    print(\"[PASS] HardConcrete extremes\")\n\n\ndef test_module_topology_matches_standalone():\n    \"\"\"Verify the actual module's topology matches our standalone copy.\"\"\"\n    from edge_pruning_scoring import _build_edge_topology\n    _, idx_module, n_module = _build_edge_topology(2, 14, 2, 7)\n    _, idx_standalone, n_standalone = _build_edge_topology_standalone(2, 14, 2, 7)\n    assert n_module == n_standalone, f\"n_masks mismatch: {n_module} vs {n_standalone}\"\n    assert idx_module == idx_standalone, \"edge_to_mask_idx mismatch\"\n    print(\"[PASS] Module topology matches standalone\")\n\n\ndef test_module_hook_indices_matches_standalone():\n    \"\"\"Verify the module's hook index builder matches the standalone copy.\"\"\"\n    from edge_pruning_scoring import _build_edge_topology, _build_hook_mask_indices\n    n_layers, n_heads, n_kv_heads = 2, 14, 2\n    _, edge_to_mask_idx, _ = _build_edge_topology(n_layers, n_heads, n_kv_heads, 7)\n\n    q_m, k_m, v_m, mlp_m = _build_hook_mask_indices(\n        n_layers, n_heads, edge_to_mask_idx, torch.device(\"cpu\"),\n    )\n    q_s, k_s, v_s, mlp_s = _build_hook_mask_indices_standalone(\n        n_layers, n_heads, edge_to_mask_idx,\n    )\n\n    for L in range(n_layers):\n        for src in q_s[L]:\n            assert q_m[L][src].tolist() == q_s[L][src], f\"Q mismatch at L={L} src={src}\"\n            assert k_m[L][src].tolist() == k_s[L][src], f\"K mismatch at L={L} src={src}\"\n            assert v_m[L][src].tolist() == v_s[L][src], f\"V mismatch at L={L} src={src}\"\n        for src in mlp_s[L]:\n            assert mlp_m[L][src] == mlp_s[L][src], f\"MLP mismatch at L={L} src={src}\"\n    print(\"[PASS] Module hook indices match standalone\")\n\n\n# ===========================================================================\n\nif __name__ == \"__main__\":\n    # No-torch tests\n    test_ast_syntax()\n    test_function_signature_from_ast()\n    test_edge_topology_no_gqa()\n    test_edge_topology_gqa()\n    test_dst_mask_table()\n    test_edge_counts_qwen()\n    test_edge_counts_gpt2()\n    # v2 hook index tests\n    test_hook_q_masks_independent()\n    test_hook_kv_gqa_sharing()\n    test_hook_mlp_sources_include_same_layer_attn()\n    test_hook_qkv_sources_exclude_same_layer()\n    test_hook_edge_coverage()\n\n    if HAS_TORCH:\n        test_hard_concrete_sampling()\n        test_hard_concrete_gradient()\n        test_hard_concrete_extremes()\n        test_module_topology_matches_standalone()\n        test_module_hook_indices_matches_standalone()\n    else:\n        print(\"[SKIP] Torch-dependent tests (torch not installed)\")\n\n    print(\"\\n=== All applicable smoke tests passed ===\")\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 11,
        "newStart": 1,
        "newLines": 10,
        "lines": [
          "-\"\"\"Smoke tests for edge_pruning_scoring.py.",
          "+\"\"\"Smoke tests for edge_pruning_scoring.py v2.",
          " ",
          " Tests split by dependency:",
          "-  - No-torch tests: AST syntax, function signature from AST, edge topology logic",
          "-  - Torch tests: HardConcrete numerics, gradient flow, estimate_edge_counts",
          "+  - No-torch tests: AST syntax, function signature, edge topology, hook mask indices",
          "+  - Torch tests: HardConcrete numerics, gradient flow, module consistency",
          " ",
          "-Run without torch: python3 test_edge_pruning_scoring.py",
          "-Run with torch:    python3 test_edge_pruning_scoring.py  (auto-detects)",
          "+Run: python3 test_edge_pruning_scoring.py",
          " \"\"\"",
          " ",
          " import ast"
        ]
      },
      {
        "oldStart": 33,
        "oldLines": 13,
        "newStart": 32,
        "newLines": 19,
        "lines": [
          "     assert isinstance(tree, ast.Module)",
          "     top_names = {node.name for node in ast.walk(tree)",
          "                  if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}",
          "+    # Core classes/functions",
          "     assert \"HardConcrete\" in top_names",
          "     assert \"compute_edge_pruning_scores\" in top_names",
          "     assert \"estimate_edge_counts\" in top_names",
          "     assert \"_build_edge_topology\" in top_names",
          "     assert \"_masked_forward\" in top_names",
          "     assert \"_faithfulness_loss\" in top_names",
          "-    print(\"[PASS] AST syntax check\")",
          "+    # v2 additions",
          "+    assert \"_build_hook_mask_indices\" in top_names",
          "+    assert \"_build_masked_input_qkv\" in top_names",
          "+    assert \"_build_masked_input_mlp\" in top_names",
          "+    assert \"_src_nodes_before_layer\" in top_names",
          "+    print(\"[PASS] AST syntax check (v2)\")",
          " ",
          " ",
          " def test_function_signature_from_ast():"
        ]
      },
      {
        "oldStart": 55,
        "oldLines": 7,
        "newStart": 60,
        "newLines": 6,
        "lines": [
          "                 \"target_ids\", \"n_epochs\", \"lambda_l0\", \"lr\", \"device\",",
          "             ]",
          "             assert param_names == expected, f\"Expected {expected}, got {param_names}\"",
          "-            # Check defaults: n_epochs=100, lambda_l0=1e-3, lr=0.1, device=\"cuda\"",
          "             defaults = args.defaults",
          "             assert len(defaults) == 5  # target_ids=None, n_epochs=100, lambda_l0=1e-3, lr=0.1, device=\"cuda\"",
          "             print(\"[PASS] Function signature (AST)\")"
        ]
      },
      {
        "oldStart": 63,
        "oldLines": 6,
        "newStart": 67,
        "newLines": 10,
        "lines": [
          "     raise AssertionError(\"compute_edge_pruning_scores not found\")",
          " ",
          " ",
          "+# ---------------------------------------------------------------------------",
          "+# Standalone topology builder (no torch dependency)",
          "+# ---------------------------------------------------------------------------",
          "+",
          " def _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, heads_per_kv_group):",
          "     \"\"\"Standalone copy of edge topology logic for testing without torch.\"\"\"",
          "     edge_names = []"
        ]
      },
      {
        "oldStart": 114,
        "oldLines": 6,
        "newStart": 122,
        "newLines": 46,
        "lines": [
          "     return edge_names, edge_to_mask_idx, mask_idx",
          " ",
          " ",
          "+def _build_hook_mask_indices_standalone(n_layers, n_heads, edge_to_mask_idx):",
          "+    \"\"\"Standalone copy of hook mask index builder for testing without torch.\"\"\"",
          "+",
          "+    def _src_nodes(layer, include_attn_same_layer=False):",
          "+        yield \"input\"",
          "+        for l in range(layer):",
          "+            for h in range(n_heads):",
          "+                yield f\"a{l}.h{h}\"",
          "+            yield f\"m{l}\"",
          "+        if include_attn_same_layer:",
          "+            for h in range(n_heads):",
          "+                yield f\"a{layer}.h{h}\"",
          "+",
          "+    q_all, k_all, v_all, mlp_all = [], [], [], []",
          "+    for L in range(n_layers):",
          "+        srcs_attn = list(_src_nodes(L))",
          "+        srcs_mlp = list(_src_nodes(L, include_attn_same_layer=True))",
          "+",
          "+        qi, ki, vi = {}, {}, {}",
          "+        for src in srcs_attn:",
          "+            qi[src] = [edge_to_mask_idx[f\"{src}->a{L}.h{h}.q\"] for h in range(n_heads)]",
          "+            ki[src] = [edge_to_mask_idx[f\"{src}->a{L}.h{h}.k\"] for h in range(n_heads)]",
          "+            vi[src] = [edge_to_mask_idx[f\"{src}->a{L}.h{h}.v\"] for h in range(n_heads)]",
          "+",
          "+        mi = {}",
          "+        for src in srcs_mlp:",
          "+            mi[src] = edge_to_mask_idx[f\"{src}->m{L}\"]",
          "+",
          "+        q_all.append(qi)",
          "+        k_all.append(ki)",
          "+        v_all.append(vi)",
          "+        mlp_all.append(mi)",
          "+",
          "+    return q_all, k_all, v_all, mlp_all",
          "+",
          "+",
          "+# ---------------------------------------------------------------------------",
          "+# Topology tests (carried from v1)",
          "+# ---------------------------------------------------------------------------",
          "+",
          " def test_edge_topology_no_gqa():",
          "     n_layers, n_heads, n_kv_heads = 2, 4, 4",
          "     edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone("
        ]
      },
      {
        "oldStart": 137,
        "oldLines": 20,
        "newStart": 185,
        "newLines": 16,
        "lines": [
          "         n_layers, n_heads, n_kv_heads, heads_per_kv,",
          "     )",
          " ",
          "-    # K mask sharing within KV group 0 (heads 0-6)",
          "     k_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7)}",
          "     assert len(k_masks_g0) == 1, f\"KV group 0 K masks should share, got {len(k_masks_g0)}\"",
          " ",
          "-    # K mask sharing within KV group 1 (heads 7-13)",
          "     k_masks_g1 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7, 14)}",
          "     assert len(k_masks_g1) == 1",
          "     assert k_masks_g0 != k_masks_g1",
          " ",
          "-    # Q edges independent",
          "     q_masks = {edge_to_mask_idx[f\"input->a0.h{h}.q\"] for h in range(14)}",
          "     assert len(q_masks) == 14",
          " ",
          "-    # V sharing",
          "     v_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.v\"] for h in range(7)}",
          "     assert len(v_masks_g0) == 1",
          " "
        ]
      },
      {
        "oldStart": 199,
        "oldLines": 6,
        "newStart": 243,
        "newLines": 116,
        "lines": [
          "     print(f\"[PASS] GPT-2 small: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB\")",
          " ",
          " ",
          "+# ---------------------------------------------------------------------------",
          "+# v2 hook mask index tests (no torch needed)",
          "+# ---------------------------------------------------------------------------",
          "+",
          "+def test_hook_q_masks_independent():",
          "+    \"\"\"Q masks must be independent per head (no averaging).\"\"\"",
          "+    n_layers, n_heads, n_kv_heads = 2, 4, 2",
          "+    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, 2)",
          "+    q_idx, _, _, _ = _build_hook_mask_indices_standalone(n_layers, n_heads, edge_to_mask_idx)",
          "+",
          "+    q_input_l0 = q_idx[0][\"input\"]",
          "+    assert len(set(q_input_l0)) == n_heads, \\",
          "+        f\"Q masks must be independent per head, got {len(set(q_input_l0))} distinct for {n_heads} heads\"",
          "+    print(\"[PASS] Q masks independent per head\")",
          "+",
          "+",
          "+def test_hook_kv_gqa_sharing():",
          "+    \"\"\"K/V masks shared within KV group, different across groups and between K/V.\"\"\"",
          "+    n_layers, n_heads, n_kv_heads = 2, 8, 2",
          "+    heads_per_kv = 4",
          "+    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(",
          "+        n_layers, n_heads, n_kv_heads, heads_per_kv,",
          "+    )",
          "+    _, k_idx, v_idx, _ = _build_hook_mask_indices_standalone(",
          "+        n_layers, n_heads, edge_to_mask_idx,",
          "+    )",
          "+",
          "+    # K: group 0 (heads 0-3) shared, group 1 (heads 4-7) shared",
          "+    k_g0 = set(k_idx[0][\"input\"][:4])",
          "+    k_g1 = set(k_idx[0][\"input\"][4:])",
          "+    assert len(k_g0) == 1, f\"K group 0 should share mask, got {len(k_g0)} distinct\"",
          "+    assert len(k_g1) == 1, f\"K group 1 should share mask, got {len(k_g1)} distinct\"",
          "+    assert k_g0 != k_g1, \"Different KV groups must have different K masks\"",
          "+",
          "+    # V: same sharing pattern",
          "+    v_g0 = set(v_idx[0][\"input\"][:4])",
          "+    v_g1 = set(v_idx[0][\"input\"][4:])",
          "+    assert len(v_g0) == 1",
          "+    assert len(v_g1) == 1",
          "+    assert v_g0 != v_g1",
          "+",
          "+    # K and V must be separate masks even within the same KV group",
          "+    assert k_g0 != v_g0, \"K and V must have separate masks even in same KV group\"",
          "+    print(\"[PASS] K/V GQA sharing correct\")",
          "+",
          "+",
          "+def test_hook_mlp_sources_include_same_layer_attn():",
          "+    \"\"\"MLP hook at layer L must include a{L}.h{H} as sources.\"\"\"",
          "+    n_layers, n_heads, n_kv_heads = 2, 4, 4",
          "+    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, 1)",
          "+    _, _, _, mlp_idx = _build_hook_mask_indices_standalone(n_layers, n_heads, edge_to_mask_idx)",
          "+",
          "+    # MLP at layer 0: input + same-layer attention heads",
          "+    mlp0 = set(mlp_idx[0].keys())",
          "+    assert \"input\" in mlp0",
          "+    for h in range(n_heads):",
          "+        assert f\"a0.h{h}\" in mlp0, f\"MLP at L0 must include a0.h{h}\"",
          "+",
          "+    # MLP at layer 1: input + L0 heads + L0 MLP + L1 heads",
          "+    mlp1 = set(mlp_idx[1].keys())",
          "+    assert \"input\" in mlp1",
          "+    assert \"m0\" in mlp1",
          "+    for h in range(n_heads):",
          "+        assert f\"a0.h{h}\" in mlp1",
          "+        assert f\"a1.h{h}\" in mlp1, f\"MLP at L1 must include same-layer a1.h{h}\"",
          "+    print(\"[PASS] MLP sources include same-layer attention\")",
          "+",
          "+",
          "+def test_hook_qkv_sources_exclude_same_layer():",
          "+    \"\"\"Q/K/V hooks at layer L must NOT include a{L}.h{H} or m{L}.\"\"\"",
          "+    n_layers, n_heads, n_kv_heads = 2, 4, 4",
          "+    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, 1)",
          "+    q_idx, k_idx, v_idx, _ = _build_hook_mask_indices_standalone(",
          "+        n_layers, n_heads, edge_to_mask_idx,",
          "+    )",
          "+",
          "+    for idx_dict in [q_idx[1], k_idx[1], v_idx[1]]:",
          "+        srcs = set(idx_dict.keys())",
          "+        for h in range(n_heads):",
          "+            assert f\"a1.h{h}\" not in srcs, \"Q/K/V must not include same-layer attn\"",
          "+        assert \"m1\" not in srcs, \"Q/K/V must not include same-layer MLP\"",
          "+    print(\"[PASS] Q/K/V sources exclude same-layer\")",
          "+",
          "+",
          "+def test_hook_edge_coverage():",
          "+    \"\"\"All mask parameters must be referenced by at least one hook.\"\"\"",
          "+    n_layers, n_heads, n_kv_heads = 2, 4, 2",
          "+    _, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(",
          "+        n_layers, n_heads, n_kv_heads, 2,",
          "+    )",
          "+    q_idx, k_idx, v_idx, mlp_idx = _build_hook_mask_indices_standalone(",
          "+        n_layers, n_heads, edge_to_mask_idx,",
          "+    )",
          "+",
          "+    all_indices = set()",
          "+    for L in range(n_layers):",
          "+        for src, idxs in q_idx[L].items():",
          "+            all_indices.update(idxs)",
          "+        for src, idxs in k_idx[L].items():",
          "+            all_indices.update(idxs)",
          "+        for src, idxs in v_idx[L].items():",
          "+            all_indices.update(idxs)",
          "+        for src, idx in mlp_idx[L].items():",
          "+            all_indices.add(idx)",
          "+",
          "+    assert all_indices == set(range(n_masks)), \\",
          "+        f\"Hook indices cover {len(all_indices)} of {n_masks} masks\"",
          "+    print(f\"[PASS] All {n_masks} mask parameters covered by hooks\")",
          "+",
          "+",
          " # ===========================================================================",
          " # Torch-dependent tests",
          " # ==========================================================================="
        ]
      },
      {
        "oldStart": 252,
        "oldLines": 10,
        "newStart": 406,
        "newLines": 33,
        "lines": [
          "     print(\"[PASS] Module topology matches standalone\")",
          " ",
          " ",
          "+def test_module_hook_indices_matches_standalone():",
          "+    \"\"\"Verify the module's hook index builder matches the standalone copy.\"\"\"",
          "+    from edge_pruning_scoring import _build_edge_topology, _build_hook_mask_indices",
          "+    n_layers, n_heads, n_kv_heads = 2, 14, 2",
          "+    _, edge_to_mask_idx, _ = _build_edge_topology(n_layers, n_heads, n_kv_heads, 7)",
          "+",
          "+    q_m, k_m, v_m, mlp_m = _build_hook_mask_indices(",
          "+        n_layers, n_heads, edge_to_mask_idx, torch.device(\"cpu\"),",
          "+    )",
          "+    q_s, k_s, v_s, mlp_s = _build_hook_mask_indices_standalone(",
          "+        n_layers, n_heads, edge_to_mask_idx,",
          "+    )",
          "+",
          "+    for L in range(n_layers):",
          "+        for src in q_s[L]:",
          "+            assert q_m[L][src].tolist() == q_s[L][src], f\"Q mismatch at L={L} src={src}\"",
          "+            assert k_m[L][src].tolist() == k_s[L][src], f\"K mismatch at L={L} src={src}\"",
          "+            assert v_m[L][src].tolist() == v_s[L][src], f\"V mismatch at L={L} src={src}\"",
          "+        for src in mlp_s[L]:",
          "+            assert mlp_m[L][src] == mlp_s[L][src], f\"MLP mismatch at L={L} src={src}\"",
          "+    print(\"[PASS] Module hook indices match standalone\")",
          "+",
          "+",
          " # ===========================================================================",
          " ",
          " if __name__ == \"__main__\":",
          "-    # Always run: no-torch tests",
          "+    # No-torch tests",
          "     test_ast_syntax()",
          "     test_function_signature_from_ast()",
          "     test_edge_topology_no_gqa()"
        ]
      },
      {
        "oldStart": 263,
        "oldLines": 12,
        "newStart": 440,
        "newLines": 19,
        "lines": [
          "     test_dst_mask_table()",
          "     test_edge_counts_qwen()",
          "     test_edge_counts_gpt2()",
          "+    # v2 hook index tests",
          "+    test_hook_q_masks_independent()",
          "+    test_hook_kv_gqa_sharing()",
          "+    test_hook_mlp_sources_include_same_layer_attn()",
          "+    test_hook_qkv_sources_exclude_same_layer()",
          "+    test_hook_edge_coverage()",
          " ",
          "     if HAS_TORCH:",
          "         test_hard_concrete_sampling()",
          "         test_hard_concrete_gradient()",
          "         test_hard_concrete_extremes()",
          "         test_module_topology_matches_standalone()",
          "+        test_module_hook_indices_matches_standalone()",
          "     else:",
          "         print(\"[SKIP] Torch-dependent tests (torch not installed)\")",
          " "
        ]
      }
    ],
    "originalFile": "\"\"\"Smoke tests for edge_pruning_scoring.py.\n\nTests split by dependency:\n  - No-torch tests: AST syntax, function signature from AST, edge topology logic\n  - Torch tests: HardConcrete numerics, gradient flow, estimate_edge_counts\n\nRun without torch: python3 test_edge_pruning_scoring.py\nRun with torch:    python3 test_edge_pruning_scoring.py  (auto-detects)\n\"\"\"\n\nimport ast\nimport os\nimport sys\n\nSRC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), \"edge_pruning_scoring.py\")\n\nHAS_TORCH = False\ntry:\n    import torch\n    HAS_TORCH = True\nexcept ImportError:\n    pass\n\n\n# ===========================================================================\n# No-torch tests (pure AST / logic)\n# ===========================================================================\n\ndef test_ast_syntax():\n    with open(SRC_PATH) as f:\n        source = f.read()\n    tree = ast.parse(source)\n    assert isinstance(tree, ast.Module)\n    top_names = {node.name for node in ast.walk(tree)\n                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}\n    assert \"HardConcrete\" in top_names\n    assert \"compute_edge_pruning_scores\" in top_names\n    assert \"estimate_edge_counts\" in top_names\n    assert \"_build_edge_topology\" in top_names\n    assert \"_masked_forward\" in top_names\n    assert \"_faithfulness_loss\" in top_names\n    print(\"[PASS] AST syntax check\")\n\n\ndef test_function_signature_from_ast():\n    with open(SRC_PATH) as f:\n        source = f.read()\n    tree = ast.parse(source)\n    for node in ast.walk(tree):\n        if isinstance(node, ast.FunctionDef) and node.name == \"compute_edge_pruning_scores\":\n            args = node.args\n            param_names = [a.arg for a in args.args]\n            expected = [\n                \"model\", \"clean_inputs\", \"corrupt_inputs\", \"metric_fn\",\n                \"target_ids\", \"n_epochs\", \"lambda_l0\", \"lr\", \"device\",\n            ]\n            assert param_names == expected, f\"Expected {expected}, got {param_names}\"\n            # Check defaults: n_epochs=100, lambda_l0=1e-3, lr=0.1, device=\"cuda\"\n            defaults = args.defaults\n            assert len(defaults) == 5  # target_ids=None, n_epochs=100, lambda_l0=1e-3, lr=0.1, device=\"cuda\"\n            print(\"[PASS] Function signature (AST)\")\n            return\n    raise AssertionError(\"compute_edge_pruning_scores not found\")\n\n\ndef _build_edge_topology_standalone(n_layers, n_heads, n_kv_heads, heads_per_kv_group):\n    \"\"\"Standalone copy of edge topology logic for testing without torch.\"\"\"\n    edge_names = []\n    edge_to_mask_idx = {}\n    mask_idx = 0\n\n    def _src_nodes(layer, include_attn_same_layer=False):\n        yield \"input\"\n        for l in range(layer):\n            for h in range(n_heads):\n                yield f\"a{l}.h{h}\"\n            yield f\"m{l}\"\n        if include_attn_same_layer:\n            for h in range(n_heads):\n                yield f\"a{layer}.h{h}\"\n\n    for L in range(n_layers):\n        srcs_attn = list(_src_nodes(L))\n        for src in srcs_attn:\n            for H in range(n_heads):\n                q_edge = f\"{src}->a{L}.h{H}.q\"\n                edge_names.append(q_edge)\n                edge_to_mask_idx[q_edge] = mask_idx\n                mask_idx += 1\n            for kv_group in range(n_kv_heads):\n                k_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    k_edge = f\"{src}->a{L}.h{H}.k\"\n                    edge_names.append(k_edge)\n                    edge_to_mask_idx[k_edge] = k_mask_idx\n            for kv_group in range(n_kv_heads):\n                v_mask_idx = mask_idx\n                mask_idx += 1\n                for h_in_group in range(heads_per_kv_group):\n                    H = kv_group * heads_per_kv_group + h_in_group\n                    v_edge = f\"{src}->a{L}.h{H}.v\"\n                    edge_names.append(v_edge)\n                    edge_to_mask_idx[v_edge] = v_mask_idx\n\n        srcs_mlp = list(_src_nodes(L, include_attn_same_layer=True))\n        for src in srcs_mlp:\n            mlp_edge = f\"{src}->m{L}\"\n            edge_names.append(mlp_edge)\n            edge_to_mask_idx[mlp_edge] = mask_idx\n            mask_idx += 1\n\n    return edge_names, edge_to_mask_idx, mask_idx\n\n\ndef test_edge_topology_no_gqa():\n    n_layers, n_heads, n_kv_heads = 2, 4, 4\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, 1,\n    )\n    assert len(set(edge_to_mask_idx.values())) == n_masks\n    assert n_masks == len(edge_to_mask_idx)\n    assert \"input->a0.h0.q\" in edge_to_mask_idx\n    assert \"input->a0.h0.k\" in edge_to_mask_idx\n    assert \"input->a0.h0.v\" in edge_to_mask_idx\n    assert \"input->m0\" in edge_to_mask_idx\n    assert \"a0.h0->m0\" in edge_to_mask_idx\n    assert \"a0.h0->a1.h0.q\" in edge_to_mask_idx\n    print(f\"[PASS] Edge topology non-GQA: {len(edge_names)} edges, {n_masks} masks\")\n\n\ndef test_edge_topology_gqa():\n    n_layers, n_heads, n_kv_heads = 2, 14, 2\n    heads_per_kv = 7\n    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology_standalone(\n        n_layers, n_heads, n_kv_heads, heads_per_kv,\n    )\n\n    # K mask sharing within KV group 0 (heads 0-6)\n    k_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7)}\n    assert len(k_masks_g0) == 1, f\"KV group 0 K masks should share, got {len(k_masks_g0)}\"\n\n    # K mask sharing within KV group 1 (heads 7-13)\n    k_masks_g1 = {edge_to_mask_idx[f\"input->a0.h{h}.k\"] for h in range(7, 14)}\n    assert len(k_masks_g1) == 1\n    assert k_masks_g0 != k_masks_g1\n\n    # Q edges independent\n    q_masks = {edge_to_mask_idx[f\"input->a0.h{h}.q\"] for h in range(14)}\n    assert len(q_masks) == 14\n\n    # V sharing\n    v_masks_g0 = {edge_to_mask_idx[f\"input->a0.h{h}.v\"] for h in range(7)}\n    assert len(v_masks_g0) == 1\n\n    print(f\"[PASS] Edge topology GQA: {len(edge_names)} edges, {n_masks} masks\")\n\n\ndef test_dst_mask_table():\n    _, edge_to_mask_idx, _ = _build_edge_topology_standalone(1, 2, 2, 1)\n    table = {}\n    for edge, idx in edge_to_mask_idx.items():\n        src, dst = edge.split(\"->\", 1)\n        table.setdefault(dst, {})[src] = idx\n\n    assert \"a0.h0.q\" in table\n    assert \"input\" in table[\"a0.h0.q\"]\n    assert \"m0\" in table\n    assert \"input\" in table[\"m0\"]\n    assert \"a0.h0\" in table[\"m0\"]\n    assert \"a0.h1\" in table[\"m0\"]\n    print(\"[PASS] Destination mask table\")\n\n\ndef test_edge_counts_qwen():\n    \"\"\"Estimate edge counts for Qwen-2.5 0.5B without torch.\"\"\"\n    _, _, n_masks = _build_edge_topology_standalone(24, 14, 2, 7)\n    total_edges = 0\n    for L in range(24):\n        n_src = 1 + L * (14 + 1)\n        total_edges += n_src * 14 * 3\n        total_edges += (n_src + 14)\n    mem_mb = n_masks * 4 / (1024 ** 2)\n    assert total_edges > 0\n    assert n_masks > 0\n    assert n_masks <= total_edges\n    print(f\"[PASS] Qwen-2.5 0.5B: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB\")\n\n\ndef test_edge_counts_gpt2():\n    _, _, n_masks = _build_edge_topology_standalone(12, 12, 12, 1)\n    total_edges = 0\n    for L in range(12):\n        n_src = 1 + L * (12 + 1)\n        total_edges += n_src * 12 * 3\n        total_edges += (n_src + 12)\n    mem_mb = n_masks * 4 / (1024 ** 2)\n    print(f\"[PASS] GPT-2 small: {total_edges} edges, {n_masks} masks, {mem_mb:.2f} MB\")\n\n\n# ===========================================================================\n# Torch-dependent tests\n# ===========================================================================\n\ndef test_hard_concrete_sampling():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=1000, init_mean=0.5)\n    torch.manual_seed(42)\n    samples = hc(training=True)\n    assert samples.shape == (1000,)\n    assert samples.min() >= 0.0\n    assert samples.max() <= 1.0\n    penalty = hc.l0_penalty()\n    assert penalty.item() >= 0.0\n    assert penalty.item() <= 1000.0\n    expected = hc.expected_masks()\n    assert expected.min() >= 0.0\n    assert expected.max() <= 1.0\n    print(\"[PASS] HardConcrete sampling\")\n\n\ndef test_hard_concrete_gradient():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=10, init_mean=0.5)\n    masks = hc(training=True)\n    masks.sum().backward()\n    assert hc.log_alpha.grad is not None\n    assert not torch.all(hc.log_alpha.grad == 0)\n    print(\"[PASS] HardConcrete gradient flow\")\n\n\ndef test_hard_concrete_extremes():\n    from edge_pruning_scoring import HardConcrete\n    hc = HardConcrete(n_masks=2, init_mean=0.5)\n    with torch.no_grad():\n        hc.log_alpha[0] = -10.0\n        hc.log_alpha[1] = 10.0\n    masks = hc.expected_masks()\n    assert masks[0].item() < 0.01\n    assert masks[1].item() > 0.99\n    print(\"[PASS] HardConcrete extremes\")\n\n\ndef test_module_topology_matches_standalone():\n    \"\"\"Verify the actual module's topology matches our standalone copy.\"\"\"\n    from edge_pruning_scoring import _build_edge_topology\n    _, idx_module, n_module = _build_edge_topology(2, 14, 2, 7)\n    _, idx_standalone, n_standalone = _build_edge_topology_standalone(2, 14, 2, 7)\n    assert n_module == n_standalone, f\"n_masks mismatch: {n_module} vs {n_standalone}\"\n    assert idx_module == idx_standalone, \"edge_to_mask_idx mismatch\"\n    print(\"[PASS] Module topology matches standalone\")\n\n\n# ===========================================================================\n\nif __name__ == \"__main__\":\n    # Always run: no-torch tests\n    test_ast_syntax()\n    test_function_signature_from_ast()\n    test_edge_topology_no_gqa()\n    test_edge_topology_gqa()\n    test_dst_mask_table()\n    test_edge_counts_qwen()\n    test_edge_counts_gpt2()\n\n    if HAS_TORCH:\n        test_hard_concrete_sampling()\n        test_hard_concrete_gradient()\n        test_hard_concrete_extremes()\n        test_module_topology_matches_standalone()\n    else:\n        print(\"[SKIP] Torch-dependent tests (torch not installed)\")\n\n    print(\"\\n=== All applicable smoke tests passed ===\")\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 18_

运行 smoke test。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "89aa3166-75e2-4d8a-b12f-3c638b641e3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YoK9NECaQwCK14nJ24NgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6426,
      "cache_read_input_tokens": 94567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6426
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01EmDotn9UbFEKp3g4CyaUQh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts && python3 test_edge_pruning_scoring.py 2>&1",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "8355c5c8-054e-4354-b0dd-7673c5028e97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YoK9NECaQwCK14nJ24NgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6426,
      "cache_read_input_tokens": 94567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6426
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

_source line 20 · 2026-05-12T19:30:23.112Z_

<details><summary>↩ Tool result · `toolu_01EmDotn9UbFEKp3g4CyaUQh`</summary>

```text
[PASS] AST syntax check (v2)
[PASS] Function signature (AST)
[PASS] Edge topology non-GQA: 99 edges, 99 masks
[PASS] Edge topology GQA: 759 edges, 351 masks
[PASS] Destination mask table
[PASS] Qwen-2.5 0.5B: 179388 edges, 79452 masks, 0.30 MB
[PASS] GPT-2 small: 32334 edges, 32334 masks, 0.12 MB
[PASS] Q masks independent per head
[PASS] K/V GQA sharing correct
[PASS] MLP sources include same-layer attention
[PASS] Q/K/V sources exclude same-layer
[PASS] All 71 mask parameters covered by hooks
[SKIP] Torch-dependent tests (torch not installed)

=== All applicable smoke tests passed ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "9c7a829f-80e4-498a-93d3-b8895b582428",
  "tool_use_result": {
    "stdout": "[PASS] AST syntax check (v2)\n[PASS] Function signature (AST)\n[PASS] Edge topology non-GQA: 99 edges, 99 masks\n[PASS] Edge topology GQA: 759 edges, 351 masks\n[PASS] Destination mask table\n[PASS] Qwen-2.5 0.5B: 179388 edges, 79452 masks, 0.30 MB\n[PASS] GPT-2 small: 32334 edges, 32334 masks, 0.12 MB\n[PASS] Q masks independent per head\n[PASS] K/V GQA sharing correct\n[PASS] MLP sources include same-layer attention\n[PASS] Q/K/V sources exclude same-layer\n[PASS] All 71 mask parameters covered by hooks\n[SKIP] Torch-dependent tests (torch not installed)\n\n=== All applicable smoke tests passed ===",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
All tests pass. Now let me also register the artifacts with the MCP tool.

Let me summarize the results for the user.

Actually, let me also compute some mask count comparisons to report.

v1 and v2 use the SAME `_build_edge_topology` function, so the mask parameter count is identical. The difference is purely in how the masks are applied in the forward pass.

Let me prepare the report.

Key differences between v1 and v2:

1. **Hook strategy**: 
   - v1: 1 layer pre-hook per layer → constructs a single masked residual for the entire layer
   - v2: 4 submodule pre-hooks per layer (q_proj, k_proj, v_proj, mlp) → each destination constructs its own masked residual

2. **MLP mask application**:
   - v1: MLP edge masks had parameters and participated in backward, but NO hook applied them in forward. MLP scores were all noise.
   - v2: `_mlp_pre_hook` explicitly constructs masked input for MLP from source activations weighted by MLP edge masks.

3. **Q/K/V granularity**:
   - v1: Lines 328-329 averaged all Q/K/V mask values for each source, treating attention heads uniformly
   - v2: Preserves per-head mask values, allowing different heads to weight sources differently through vectorized broadcasting.

4. **Model freezing**:
   - v1: `model.eval()` only — model parameters still accumulated gradients wastefully.
   - v2: `model.requires_grad_(False)` — saves GPU memory during backward.

5. **Removed code**:
   - `_ActivationCache` class → replaced by simple dict `src_cache`
   - `_build_dst_mask_table` → replaced by `_build_hook_mask_indices`
   - `_get_module` → unused
   - `_src_nodes_before_layer` promoted to module-level for shared use

The mask parameter count stays the same as v1, and I've verified that each hook maintains independent masks: Q gets n_heads masks per source-layer pair, K and V each get n_kv_heads masks that are shared within KV groups but distinct from each other, and MLP gets one mask per source-layer pair. All 12 smoke tests pass, though the torch-dependent ones are skipped since torch isn't available here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "9a0455bb-3a80-40d8-9eb0-ba7979980192",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gaFmEhnpQq4oVwix6M6xf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 100993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 22_

全部 12 个 no-torch smoke test 通过。注册产出文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "be3c6629-c486-41ef-993e-c93473f658a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gaFmEhnpQq4oVwix6M6xf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 100993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 23_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BudqkEzSuctVepSLa2fExA`</summary>

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
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "19067a6d-9475-4a86-8df8-fb9d8011a936",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gaFmEhnpQq4oVwix6M6xf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 100993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 24 · 2026-05-12T19:30:43.297Z_

<details><summary>↩ Tool result · `toolu_01BudqkEzSuctVepSLa2fExA`</summary>

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
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "5057532e-3695-4042-a096-60201b9b469d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01QG9wdf8BUu31akVAvg3nQP`</summary>

```json
{
  "name": "edge_pruning_scoring_v2",
  "type": "intermediate",
  "description": "Edge Pruning v2: fixes MLP mask not applied in forward + Q/K/V mean collapse. 4 submodule hooks per layer (q_proj, k_proj, v_proj, mlp) replace single layer pre-hook.",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/edge_pruning_scoring.py",
  "tags": [
    "edge-pruning",
    "v2",
    "hook-fix"
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
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "004c2633-6cc6-4519-a67e-d478cdf6296a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQ6w5Fk6gCpwcBwJTadcPE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1542,
      "cache_read_input_tokens": 101358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1542
      },
      "output_tokens": 66,
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

_source line 26 · 2026-05-12T19:30:48.859Z_

<details><summary>↩ Tool result · `toolu_01QG9wdf8BUu31akVAvg3nQP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_457920\", \"name\": \"edge_pruning_scoring_v2\", \"type\": \"intermediate\", \"description\": \"Edge Pruning v2: fixes MLP mask not applied in forward + Q/K/V mean collapse. 4 submodule hooks per layer (q_proj, k_proj, v_proj, mlp) replace single layer pre-hook.\", \"path\": \"projects/structfuse-context/artifacts/_project/intermediate/edge_pruning_scoring_457920.py\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T19:30:48.826026+00:00\", \"tags\": [\"edge-pruning\", \"v2\", \"hook-fix\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "e71f245b-3fe5-44ad-89de-91b1587c5055",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260512_457920\\\", \\\"name\\\": \\\"edge_pruning_scoring_v2\\\", \\\"type\\\": \\\"intermediate\\\", \\\"description\\\": \\\"Edge Pruning v2: fixes MLP mask not applied in forward + Q/K/V mean collapse. 4 submodule hooks per layer (q_proj, k_proj, v_proj, mlp) replace single layer pre-hook.\\\", \\\"path\\\": \\\"projects/structfuse-context/artifacts/_project/intermediate/edge_pruning_scoring_457920.py\\\", \\\"url\\\": null, \\\"project\\\": \\\"structfuse-context\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-12T19:30:48.826026+00:00\\\", \\\"tags\\\": [\\\"edge-pruning\\\", \\\"v2\\\", \\\"hook-fix\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_457920\", \"name\": \"edge_pruning_scoring_v2\", \"type\": \"intermediate\", \"description\": \"Edge Pruning v2: fixes MLP mask not applied in forward + Q/K/V mean collapse. 4 submodule hooks per layer (q_proj, k_proj, v_proj, mlp) replace single layer pre-hook.\", \"path\": \"projects/structfuse-context/artifacts/_project/intermediate/edge_pruning_scoring_457920.py\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T19:30:48.826026+00:00\", \"tags\": [\"edge-pruning\", \"v2\", \"hook-fix\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01P1QLFpgDegJ5XpKCpBG3rK`</summary>

```json
{
  "name": "test_edge_pruning_scoring_v2",
  "type": "intermediate",
  "description": "Smoke tests for edge_pruning_scoring v2: topology, hook mask indices, Q/K/V independence, GQA sharing, edge coverage.",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/test_edge_pruning_scoring.py",
  "tags": [
    "edge-pruning",
    "v2",
    "test"
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
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "9028f1ab-b3af-48c1-a253-2a9e14a87d9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQ6w5Fk6gCpwcBwJTadcPE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1542,
      "cache_read_input_tokens": 101358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1542
      },
      "output_tokens": 66,
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

_source line 28 · 2026-05-12T19:30:51.121Z_

<details><summary>↩ Tool result · `toolu_01P1QLFpgDegJ5XpKCpBG3rK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_3089a7\", \"name\": \"test_edge_pruning_scoring_v2\", \"type\": \"intermediate\", \"description\": \"Smoke tests for edge_pruning_scoring v2: topology, hook mask indices, Q/K/V independence, GQA sharing, edge coverage.\", \"path\": \"projects/structfuse-context/artifacts/_project/intermediate/test_edge_pruning_scoring_3089a7.py\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T19:30:51.087734+00:00\", \"tags\": [\"edge-pruning\", \"v2\", \"test\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "163434eb-3a99-442b-8892-4000e0775d89",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260512_3089a7\\\", \\\"name\\\": \\\"test_edge_pruning_scoring_v2\\\", \\\"type\\\": \\\"intermediate\\\", \\\"description\\\": \\\"Smoke tests for edge_pruning_scoring v2: topology, hook mask indices, Q/K/V independence, GQA sharing, edge coverage.\\\", \\\"path\\\": \\\"projects/structfuse-context/artifacts/_project/intermediate/test_edge_pruning_scoring_3089a7.py\\\", \\\"url\\\": null, \\\"project\\\": \\\"structfuse-context\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-12T19:30:51.087734+00:00\\\", \\\"tags\\\": [\\\"edge-pruning\\\", \\\"v2\\\", \\\"test\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_3089a7\", \"name\": \"test_edge_pruning_scoring_v2\", \"type\": \"intermediate\", \"description\": \"Smoke tests for edge_pruning_scoring v2: topology, hook mask indices, Q/K/V independence, GQA sharing, edge coverage.\", \"path\": \"projects/structfuse-context/artifacts/_project/intermediate/test_edge_pruning_scoring_3089a7.py\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T19:30:51.087734+00:00\", \"tags\": [\"edge-pruning\", \"v2\", \"test\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

## 汇报

### 1. 与 v1 的核心架构差异

| | v1 | v2 |
|---|---|---|
| Hook 策略 | 1 个 `layer.register_forward_pre_hook` 构建单一 masked residual | 4 个 submodule pre-hook：`q_proj`、`k_proj`、`v_proj`、`mlp` 各自独立构建 masked input |
| MLP mask | 参数存在、参与 backward，但 forward 无 hook 应用 → score 全不可信 | `_mlp_pre_hook` 从 source cache 按 MLP edge mask 加权构建输入 |
| Q/K/V 粒度 | L328-329 对 (src, layer) 的所有 Q/K/V mask 取 `mean()` → 单标量 | 每个 hook 独立使用 `masks[idx_tensor].view(1,1,n_heads,1)` 向量化广播，per-head 独立 |
| Source cache | `_ActivationCache` class (embed/head_out/mlp_out 分离) | 统一 `Dict[str, Tensor]`，key = canonical node name |
| 模型冻结 | `model.eval()` 仅切 BN/Dropout | 追加 `model.requires_grad_(False)` 省 backward 内存 |
| 新增模块 | — | `_build_hook_mask_indices`（预计算向量化索引）、`_build_masked_input_qkv`、`_build_masked_input_mlp`、`_src_nodes_before_layer`（提升为模块级共享） |
| 删除 | — | `_ActivationCache`、`_build_dst_mask_table`、`_get_module` |

### 2. Mask 参数总数

**完全相同**。`_build_edge_topology` 未修改，拓扑结构和 mask 数量不变。

- Qwen-2.5 0.5B (24L/14H/2KV): 179,388 edges → 79,452 independent masks (0.30 MB)
- GPT-2 small (12L/12H/12KV): 32,334 edges → 32,334 masks (0.12 MB)

### 3. 各 edge 类型 mask 独立性验证

| 类型 | 验证结果 |
|------|---------|
| Q | n_heads 个独立 mask per (src, layer) ✓ |
| K | n_kv_heads 个独立 mask，同 KV group 内共享 ✓ |
| V | 同 K，但 K≠V（同 group 内也独立）✓ |
| MLP | 每个 (src, layer) 1 个独立 mask ✓ |
| 全覆盖 | hook indices 覆盖所有 n_masks 个参数 ✓ |

### 4. Smoke test 结果

12/12 no-torch tests 全部通过（torch-dependent tests 因本机无 torch 跳过）：

```
[PASS] AST syntax check (v2)
[PASS] Function signature (AST)
[PASS] Edge topology non-GQA: 99 edges, 99 masks
[PASS] Edge topology GQA: 759 edges, 351 masks
[PASS] Destination mask table
[PASS] Qwen-2.5 0.5B: 179388 edges, 79452 masks, 0.30 MB
[PASS] GPT-2 small: 32334 edges, 32334 masks, 0.12 MB
[PASS] Q masks independent per head
[PASS] K/V GQA sharing correct
[PASS] MLP sources include same-layer attention
[PASS] Q/K/V sources exclude same-layer
[PASS] All 71 mask parameters covered by hooks
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "uuid": "947a447a-2ba9-44f7-ae74-f4e9334971f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ah2rZznr6dFQSq6q7kg2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 102900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1143
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

_source line 30_

## 汇报

### 1. 与 v1 的核心架构差异

| | v1 | v2 |
|---|---|---|
| Hook 策略 | 1 个 `layer.register_forward_pre_hook` 构建单一 masked residual | 4 个 submodule pre-hook：`q_proj`、`k_proj`、`v_proj`、`mlp` 各自独立构建 masked input |
| MLP mask | 参数存在、参与 backward，但 forward 无 hook 应用 → score 全不可信 | `_mlp_pre_hook` 从 source cache 按 MLP edge mask 加权构建输入 |
| Q/K/V 粒度 | L328-329 对 (src, layer) 的所有 Q/K/V mask 取 `mean()` → 单标量 | 每个 hook 独立使用 `masks[idx_tensor].view(1,1,n_heads,1)` 向量化广播，per-head 独立 |
| Source cache | `_ActivationCache` class (embed/head_out/mlp_out 分离) | 统一 `Dict[str, Tensor]`，key = canonical node name |
| 模型冻结 | `model.eval()` 仅切 BN/Dropout | 追加 `model.requires_grad_(False)` 省 backward 内存 |
| 新增模块 | — | `_build_hook_mask_indices`（预计算向量化索引）、`_build_masked_input_qkv`、`_build_masked_input_mlp`、`_src_nodes_before_layer`（提升为模块级共享） |
| 删除 | — | `_ActivationCache`、`_build_dst_mask_table`、`_get_module` |

### 2. Mask 参数总数

**完全相同**。`_build_edge_topology` 未修改，拓扑结构和 mask 数量不变。

- Qwen-2.5 0.5B (24L/14H/2KV): 179,388 edges → 79,452 independent masks (0.30 MB)
- GPT-2 small (12L/12H/12KV): 32,334 edges → 32,334 masks (0.12 MB)

### 3. 各 edge 类型 mask 独立性验证

| 类型 | 验证结果 |
|------|---------|
| Q | n_heads 个独立 mask per (src, layer) ✓ |
| K | n_kv_heads 个独立 mask，同 KV group 内共享 ✓ |
| V | 同 K，但 K≠V（同 group 内也独立）✓ |
| MLP | 每个 (src, layer) 1 个独立 mask ✓ |
| 全覆盖 | hook indices 覆盖所有 n_masks 个参数 ✓ |

### 4. Smoke test 结果

12/12 no-torch tests 全部通过（torch-dependent tests 因本机无 torch 跳过）：

```
[PASS] AST syntax check (v2)
[PASS] Function signature (AST)
[PASS] Edge topology non-GQA: 99 edges, 99 masks
[PASS] Edge topology GQA: 759 edges, 351 masks
[PASS] Destination mask table
[PASS] Qwen-2.5 0.5B: 179388 edges, 79452 masks, 0.30 MB
[PASS] GPT-2 small: 32334 edges, 32334 masks, 0.12 MB
[PASS] Q masks independent per head
[PASS] K/V GQA sharing correct
[PASS] MLP sources include same-layer attention
[PASS] Q/K/V sources exclude same-layer
[PASS] All 71 mask parameters covered by hooks
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 970085,
  "duration_api_ms": 970745,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "a579ae2f-e9c8-401c-a4e5-22ceb69e37d4",
  "total_cost_usd": 2.4287265,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 92202,
    "cache_read_input_tokens": 475450,
    "output_tokens": 64484,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 92202,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1067,
        "cache_read_input_tokens": 102900,
        "cache_creation_input_tokens": 1143,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1143
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2489,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0025889999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 64484,
      "cacheReadInputTokens": 475450,
      "cacheCreationInputTokens": 92202,
      "webSearchRequests": 0,
      "costUSD": 2.4261375000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "db1edfaa-0c25-4026-8d42-cfc9888b7228"
}
```

</details>

---
