# sync dcgrpo trainer final v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_sync_dcgrpo_trainer_final_v2_20260518T125951.log`
- **Structured JSON:** [`b060f62c8c8b79f3b0ad.json`](../../sessions/b0/b060f62c8c8b79f3b0ad.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "692d3268-f898-434e-9fc1-8fa2678da477",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-3-projects-contrastive-entrain-calib/memory/"
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
    "resetsAt": 1779125400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "63162769-4785-4b9b-96d9-818644e74f8d",
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the local file, then sync it to the remote server via SSH.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "54b1812e-f297-425c-87d9-33d058dd4883",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GidfPd8qAqX4T9Z2jtD4Jr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12614,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12614
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

### Assistant

_source line 5_

读取本地文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "cdfb443a-4323-42cb-b0f3-91b1ca4f436d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GidfPd8qAqX4T9Z2jtD4Jr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12614,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12614
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01D8QiXVajnvqXffBJ1bFDmg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/dcgrpo_trainer.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "83338e88-5544-47c4-a91c-98b520038a76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GidfPd8qAqX4T9Z2jtD4Jr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12614,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12614
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

_source line 7 · 2026-05-18T13:00:06.163Z_

<details><summary>↩ Tool result · `toolu_01D8QiXVajnvqXffBJ1bFDmg`</summary>

```text
1	"""DCGRPOTrainer: Direction-Contrastive GRPO for sycophancy calibration.
2	
3	Inherits trl.GRPOTrainer, overrides reward computation to inject three signals:
4	  R1 (Direction Alignment)     -- dot(h, d_syc) at critical-turn hidden state
5	  R2 (Contrastive Consistency) -- sigmoid(R1_valid - R1_invalid) - 0.5
6	  R3 (Behavioral NLI)          -- DeBERTa entailment probability
7	
8	Overrides completion generation to support multi-turn dialogue with activation caching.
9	
10	Input:  Dataset with columns: prompt (3-turn dialogue), condition, pair_id
11	Output: LoRA-tuned policy model with reduced sycophantic capitulation
12	
13	Dependencies: trl>=0.15, transformers>=4.45, peft, torch
14	"""
15	
16	from __future__ import annotations
17	
18	import logging
19	from dataclasses import dataclass, field
20	from typing import Any
21	
22	import torch
23	import torch.nn as nn
24	import torch.nn.functional as F
25	from trl import GRPOConfig, GRPOTrainer
26	
27	logger = logging.getLogger(__name__)
28	
29	
30	# =====================================================================
31	# Activation Cache
32	# =====================================================================
33	
34	def _resolve_transformer_layers(model: nn.Module) -> nn.ModuleList:
35	    """Find transformer decoder layers, handling PEFT wrappers.
36	
37	    Supports Qwen/Llama/Mistral (model.model.layers layout).
38	    Unwraps PEFT indirection and handles transformers>=5.x where
39	    model.base_model returns the inner model directly.
40	    """
41	    candidate = model
42	    # PEFT wrapping: model.base_model.model.model.layers
43	    if hasattr(candidate, "base_model"):
44	        candidate = candidate.base_model
45	    if hasattr(candidate, "layers"):
46	        return candidate.layers
47	    if hasattr(candidate, "model"):
48	        inner = candidate.model
49	        if hasattr(inner, "layers"):
50	            return inner.layers
51	        if hasattr(inner, "model") and hasattr(inner.model, "layers"):
52	            return inner.model.layers
53	    raise AttributeError(
54	        f"Cannot locate transformer layers on {type(model).__name__}. "
55	        "Expected model.model.layers or model.base_model.model.model.layers."
56	    )
57	
58	
59	class ActivationCache:
60	    """Forward hook to cache hidden states at specified layers during generation."""
61	
62	    def __init__(self, target_layers: list[int]):
63	        self.target_layers = set(target_layers)
64	        self.cache: dict[int, torch.Tensor] = {}
65	        self.hooks: list = []
66	
67	    def register(self, model: nn.Module) -> None:
68	        """Attach forward hooks to target transformer layers."""
69	        self.remove()
70	        layers = _resolve_transformer_layers(model)
71	        for idx in sorted(self.target_layers):
72	            if idx >= len(layers):
73	                raise ValueError(
74	                    f"Layer {idx} out of range (model has {len(layers)} layers)"
75	                )
76	            self.hooks.append(
77	                layers[idx].register_forward_hook(self._make_hook(idx))
78	            )
79	        logger.info(
80	            "Activation hooks registered on layers %s", sorted(self.target_layers)
81	        )
82	
83	    def _make_hook(self, layer_idx: int):
84	        def fn(module, input, output):
85	            hidden = output[0] if isinstance(output, tuple) else output
86	            self.cache[layer_idx] = hidden.detach()
87	        return fn
88	
89	    def clear(self):
90	        self.cache = {}
91	
92	    def remove(self):
93	        for h in self.hooks:
94	            h.remove()
95	        self.hooks.clear()
96	        self.cache.clear()
97	
98	
99	# =====================================================================
100	# Configuration
101	# =====================================================================
102	
103	@dataclass
104	class DCGRPOConfig(GRPOConfig):
105	    """GRPOConfig extended with DC-GRPO reward and direction parameters.
106	
107	    Additional fields control the direction-contrastive reward mechanism:
108	    direction_path points to directions.pt from compute_directions.py,
109	    reward_layers selects which transformer layers to probe (default 19-27,
110	    the highest-AUROC range from MVP), and r1/r2/r3 weights set the
111	    relative contribution of each reward component.
112	    """
113	
114	    direction_path: str = ""
115	    reward_layers: list[int] = field(
116	        default_factory=lambda: list(range(19, 36))
117	    )
118	    reward_position: str = "asst_first"
119	
120	    r1_weight: float = 1.0
121	    r2_weight: float = 0.5
122	    r3_weight: float = 0.3
123	
124	    r3_model_name: str = "microsoft/deberta-v3-base"
125	    nli_batch_size: int = 16
126	
127	
128	# =====================================================================
129	# Placeholder reward for GRPOTrainer constructor
130	# =====================================================================
131	
132	def _noop_reward_fn(completions: list[str], **kwargs) -> list[float]:
133	    """Placeholder passed to super().__init__; actual rewards computed in override."""
134	    return [0.0] * len(completions)
135	
136	
137	class _DCRewardCallable:
138	    """Callable that computes combined R1+R2+R3 DC-GRPO rewards.
139	
140	    Plugged into TRL's reward_funcs after super().__init__. Receives prompts,
141	    completions, and dataset columns (condition, pair_id) from TRL's
142	    _calculate_rewards via **reward_kwargs. Runs a forward pass with hooks
143	    to extract activations for R1/R2.
144	    """
145	
146	    __name__ = "dc_grpo_reward"
147	
148	    def __init__(self, trainer: "DCGRPOTrainer"):
149	        self.trainer = trainer
150	
151	    def __call__(self, prompts, completions, **kwargs):
152	        conditions = kwargs.get("condition", ["unknown"] * len(completions))
153	        pair_ids = kwargs.get("pair_id", [str(i) for i in range(len(completions))])
154	
155	        t = self.trainer
156	        if t.d_syc is None:
157	            logger.warning("d_syc not loaded; returning R3-only rewards")
158	            r3 = t.compute_r3(completions, conditions)
159	            return [t._r3_w * s for s in r3]
160	
161	        tokenizer = t.processing_class
162	        t._prompt_lengths = [
163	            len(tokenizer.encode(p, add_special_tokens=False))
164	            for p in prompts
165	        ]
166	        full_texts = [p + c for p, c in zip(prompts, completions)]
167	        encoded = tokenizer(
168	            full_texts,
169	            padding=True,
170	            truncation=True,
171	            return_tensors="pt",
172	        ).to(t.model.device)
173	        positions = t._find_asst_first_positions(encoded.input_ids, tokenizer)
174	        batch_acts = t._extract_activations(
175	            encoded.input_ids, encoded.attention_mask, positions
176	        )
177	
178	        rewards, components = t.compute_rewards(
179	            completions, conditions, pair_ids, batch_acts
180	        )
181	
182	        t._reward_step += 1
183	        step = t._reward_step
184	
185	        if step <= 10:
186	            import statistics
187	            for name, values in components.items():
188	                if values:
189	                    mu = sum(values) / len(values)
190	                    sd = statistics.stdev(values) if len(values) > 1 else 0.0
191	                    logger.info(
192	                        "[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f",
193	                        step, name, mu, sd, min(values), max(values),
194	                    )
195	            if rewards:
196	                mu = sum(rewards) / len(rewards)
197	                sd = statistics.stdev(rewards) if len(rewards) > 1 else 0.0
198	                logger.info(
199	                    "[step %d] reward/combined  mean=%.4f  std=%.4f",
200	                    step, mu, sd,
201	                )
202	        else:
203	            for name, values in components.items():
204	                if values:
205	                    logger.info("reward/%s_mean=%.4f", name, sum(values) / len(values))
206	            if rewards:
207	                logger.info(
208	                    "reward/combined_mean=%.4f", sum(rewards) / len(rewards)
209	                )
210	
211	        return rewards
212	
213	
214	# =====================================================================
215	# DCGRPOTrainer
216	# =====================================================================
217	
218	class DCGRPOTrainer(GRPOTrainer):
219	    """Direction-Contrastive GRPO trainer for sycophancy calibration.
220	
221	    Reward signals:
222	      R1 = sign(condition) * dot(h, d_syc)         (direction alignment)
223	      R2 = sigmoid(R1_valid - R1_invalid) - 0.5    (contrastive consistency)
224	      R3 = NLI_entailment(completion, expected)     (behavioral appropriateness)
225	      R  = w1*R1 + w2*R2 + w3*R3
226	
227	    Data flow:
228	      generate_completions() caches activations via forward hooks.
229	      compute_rewards() reads cached activations for R1/R2, runs NLI for R3.
230	
231	    Expected dataset columns beyond "prompt":
232	      condition  -- "valid_correction" or "invalid_pressure"
233	      pair_id    -- links the two conditions of the same calibration pair
234	    """
235	
236	    def __init__(
237	        self,
238	        model: str | nn.Module,
239	        args: DCGRPOConfig,
240	        train_dataset: Any,
241	        eval_dataset: Any | None = None,
242	        processing_class: Any | None = None,
243	        peft_config: Any | None = None,
244	        **kwargs,
245	    ):
246	        # Store config before super().__init__ (which sets self.model)
247	        self._direction_path = args.direction_path
248	        self._reward_layers = args.reward_layers
249	        self._pos_idx = 1 if args.reward_position == "asst_first" else 0
250	        self._r1_w = args.r1_weight
251	        self._r2_w = args.r2_weight
252	        self._r3_w = args.r3_weight
253	        self._r3_model_name = args.r3_model_name
254	        self._nli_batch_size = args.nli_batch_size
255	
256	        # Populated after super().__init__
257	        self.d_syc: torch.Tensor | None = None
258	        self._act_cache: ActivationCache | None = None
259	        self._step_acts: list[dict[int, torch.Tensor]] | None = []
260	        self._nli_model: nn.Module | None = None
261	        self._nli_tokenizer: Any = None
262	        self._extraction_failures: int = 0
263	        self._prompt_lengths: list[int] = []
264	        self._reward_step: int = 0
265	
266	        super().__init__(
267	            model=model,
268	            reward_funcs=[_noop_reward_fn],
269	            args=args,
270	            train_dataset=train_dataset,
271	            eval_dataset=eval_dataset,
272	            processing_class=processing_class,
273	            peft_config=peft_config,
274	            **kwargs,
275	        )
276	
277	        # Post-init: self.model now exists
278	        self._load_directions()
279	        self._act_cache = ActivationCache(self._reward_layers)
280	        self._act_cache.register(self.model)
281	
282	        # Replace noop placeholder with actual DC-GRPO reward function
283	        self.reward_funcs = [_DCRewardCallable(self)]
284	        if hasattr(self, "reward_func_names"):
285	            self.reward_func_names = ["dc_grpo_reward"]
286	
287	    # -----------------------------------------------------------------
288	    # Direction loading
289	    # -----------------------------------------------------------------
290	
291	    def _load_directions(self) -> None:
292	        """Load d_syc direction vectors from directions.pt."""
293	        if not self._direction_path:
294	            logger.warning("No direction_path provided; R1/R2 will return 0.0")
295	            return
296	        data = torch.load(
297	            self._direction_path, map_location="cpu", weights_only=True
298	        )
299	        self.d_syc = data["d_syc"]  # (num_layers, 2, hidden_dim)
300	        logger.info(
301	            "Loaded d_syc shape=%s from %s",
302	            self.d_syc.shape,
303	            self._direction_path,
304	        )
305	
306	    def reload_directions(self, path: str) -> None:
307	        """Hot-reload directions after periodic recalibration.
308	
309	        Logs a warning per layer if cosine similarity between old and new
310	        directions drops below 0.7 (potential direction drift under LoRA).
311	        """
312	        old_d = self.d_syc
313	        self._direction_path = path
314	        self._load_directions()
315	
316	        if old_d is not None and self.d_syc is not None:
317	            for layer_idx in self._reward_layers:
318	                if layer_idx >= min(old_d.shape[0], self.d_syc.shape[0]):
319	                    continue
320	                cos = F.cosine_similarity(
321	                    old_d[layer_idx, self._pos_idx].unsqueeze(0),
322	                    self.d_syc[layer_idx, self._pos_idx].unsqueeze(0),
323	                ).item()
324	                if cos < 0.7:
325	                    logger.warning(
326	                        "Direction drift at layer %d: cosine=%.3f", layer_idx, cos
327	                    )
328	
329	    # -----------------------------------------------------------------
330	    # NLI model (lazy)
331	    # -----------------------------------------------------------------
332	
333	    def _ensure_nli_model(self) -> None:
334	        """Lazy-load DeBERTa NLI model for R3 scoring."""
335	        if self._nli_model is not None:
336	            return
337	        from transformers import (
338	            AutoModelForSequenceClassification,
339	            AutoTokenizer,
340	        )
341	
342	        self._nli_tokenizer = AutoTokenizer.from_pretrained(self._r3_model_name)
343	        self._nli_model = (
344	            AutoModelForSequenceClassification.from_pretrained(self._r3_model_name)
345	            .eval()
346	        )
347	        logger.info("Loaded NLI model: %s", self._r3_model_name)
348	
349	    # -----------------------------------------------------------------
350	    # Position finding
351	    # -----------------------------------------------------------------
352	
353	    def _find_asst_first_positions(
354	        self,
355	        input_ids: torch.Tensor,
356	        tokenizer: Any,
357	    ) -> list[int]:
358	        """Locate asst_first position using tokenize-based method.
359	
360	        Matches extract_activations_v2.py: asst_first = len(prompt_tokens) - 1,
361	        the last prompt token whose hidden state predicts the first generated
362	        content token. Uses self._prompt_lengths when available (set by
363	        generate_completions or _DCRewardCallable before calling this method).
364	        Falls back to scanning for the <|im_start|> assistant marker.
365	        """
366	        positions: list[int] = []
367	        for i in range(input_ids.shape[0]):
368	            seq_len = input_ids.shape[1]
369	            if self._prompt_lengths and i < len(self._prompt_lengths):
370	                pos = self._prompt_lengths[i] - 1
371	            else:
372	                im_start_id = tokenizer.convert_tokens_to_ids("<|im_start|>")
373	                ids_list = input_ids[i].tolist()
374	                pos = seq_len - 1
375	                for j in range(len(ids_list) - 1, -1, -1):
376	                    if ids_list[j] == im_start_id:
377	                        candidate = j + 2
378	                        if candidate < seq_len:
379	                            pos = candidate
380	                        break
381	            positions.append(min(pos, seq_len - 1))
382	        return positions
383	
384	    # -----------------------------------------------------------------
385	    # Activation extraction
386	    # -----------------------------------------------------------------
387	
388	    def _extract_activations(
389	        self,
390	        input_ids: torch.Tensor,
391	        attention_mask: torch.Tensor,
392	        positions: list[int],
393	    ) -> list[dict[int, torch.Tensor]]:
394	        """Forward pass to extract hidden states at asst_first positions.
395	
396	        Runs the full sequence through the model with hooks enabled, then
397	        reads the cached hidden state at each sample's designated position.
398	        This is a separate pass from generation (generate() uses KV cache
399	        and only exposes the latest-token hidden state per step).
400	
401	        Args:
402	            input_ids: (batch, seq_len) full sequences (prompt + completion).
403	            attention_mask: (batch, seq_len).
404	            positions: Per-sample token position for extraction.
405	
406	        Returns:
407	            List of per-sample dicts: {layer_idx: Tensor(hidden_dim,)}.
408	        """
409	        self._act_cache.clear()
410	        with torch.no_grad():
411	            self.model(input_ids=input_ids, attention_mask=attention_mask)
412	
413	        batch_acts: list[dict[int, torch.Tensor]] = []
414	        for sample_idx, pos in enumerate(positions):
415	            acts: dict[int, torch.Tensor] = {}
416	            for layer_idx in self._reward_layers:
417	                cached = self._act_cache.cache.get(layer_idx)
418	                if cached is not None:
419	                    acts[layer_idx] = cached[sample_idx, pos]
420	            batch_acts.append(acts)
421	
422	        self._act_cache.clear()
423	        return batch_acts
424	
425	    # -----------------------------------------------------------------
426	    # R1: Direction Alignment
427	    # -----------------------------------------------------------------
428	
429	    def compute_r1(
430	        self,
431	        activations: dict[int, torch.Tensor],
432	        condition: str,
433	    ) -> float:
434	        """Direction alignment reward for a single completion.
435	
436	        R1 = +dot(h, d_syc) for valid_correction   (reward genuine revision)
437	        R1 = -dot(h, d_syc) for invalid_pressure    (penalize capitulation)
438	
439	        Direction vectors are L2-normalized per the compute_directions.py
440	        convention, so dot product magnitude scales with activation norm
441	        (stronger internal signal produces stronger reward).
442	        Averaged across all reward_layers.
443	
444	        Args:
445	            activations: {layer_idx: Tensor(hidden_dim,)} at asst_first position.
446	            condition: "valid_correction" or "invalid_pressure".
447	
448	        Returns:
449	            Scalar R1 reward.
450	        """
451	        if self.d_syc is None:
452	            return 0.0
453	
454	        sign = 1.0 if condition == "valid_correction" else -1.0
455	        scores: list[float] = []
456	        for layer_idx in self._reward_layers:
457	            h = activations.get(layer_idx)
458	            if h is None:
459	                continue
460	            d = self.d_syc[layer_idx, self._pos_idx].to(h)
461	            scores.append(sign * torch.dot(h, d).item())
462	
463	        if not scores:
464	            return 0.0
465	        raw = sum(scores) / len(scores)
466	        return torch.tanh(torch.tensor(raw / 20.0)).item()
467	
468	    def compute_r1_batch(
469	        self,
470	        batch_activations: list[dict[int, torch.Tensor]],
471	        conditions: list[str],
472	    ) -> list[float]:
473	        """R1 for a batch of completions."""
474	        return [
475	            self.compute_r1(acts, cond)
476	            for acts, cond in zip(batch_activations, conditions)
477	        ]
478	
479	    # -----------------------------------------------------------------
480	    # R2: Contrastive Consistency
481	    # -----------------------------------------------------------------
482	
483	    def compute_r2(self, r1_valid: float, r1_invalid: float) -> float:
484	        """Rank-based contrastive reward for a condition pair.
485	
486	        R2 = sigmoid(R1_valid - R1_invalid) - 0.5
487	
488	        Positive when valid_correction R1 exceeds invalid_pressure R1 within
489	        the same calibration pair. S1 rank-based design avoids the
490	        d_gen = -d_syc degeneracy (see skeleton section 8).
491	
492	        Args:
493	            r1_valid: R1 from the valid_correction completion.
494	            r1_invalid: R1 from the invalid_pressure completion.
495	
496	        Returns:
497	            Scalar R2 in (-0.5, 0.5).
498	        """
499	        return torch.sigmoid(torch.tensor(r1_valid - r1_invalid)).item() - 0.5
500	
501	    def compute_r2_for_group(
502	        self,
503	        r1_scores: list[float],
504	        conditions: list[str],
505	        pair_ids: list[str],
506	    ) -> list[float]:
507	        """R2 for all completions in a training step, paired by pair_id.
508	
509	        Aggregates mean R1 per (pair_id, condition), then applies R2.
510	        All completions from the same pair receive the same R2 score.
511	        Completions without a paired counterpart get R2 = 0.
512	
513	        Args:
514	            r1_scores: R1 per completion (same order as conditions/pair_ids).
515	            conditions: Per-completion condition label.
516	            pair_ids: Per-completion pair identifier.
517	
518	        Returns:
519	            List of R2 scores, same length as input.
520	        """
521	        # Aggregate R1 by (pair_id, condition)
522	        pair_r1: dict[str, dict[str, list[float]]] = {}
523	        for r1, cond, pid in zip(r1_scores, conditions, pair_ids):
524	            pair_r1.setdefault(pid, {}).setdefault(cond, []).append(r1)
525	
526	        pair_means: dict[str, dict[str, float]] = {}
527	        for pid, cond_map in pair_r1.items():
528	            pair_means[pid] = {
529	                c: sum(vs) / len(vs) for c, vs in cond_map.items()
530	            }
531	
532	        r2_scores: list[float] = []
533	        for cond, pid in zip(conditions, pair_ids):
534	            means = pair_means.get(pid, {})
535	            r1_v = means.get("valid_correction")
536	            r1_i = means.get("invalid_pressure")
537	            if r1_v is not None and r1_i is not None:
538	                r2_scores.append(self.compute_r2(r1_v, r1_i))
539	            else:
540	                r2_scores.append(0.0)
541	        return r2_scores
542	
543	    # -----------------------------------------------------------------
544	    # R3: Behavioral NLI
545	    # -----------------------------------------------------------------
546	
547	    def compute_r3(
548	        self,
549	        completions: list[str],
550	        conditions: list[str],
551	    ) -> list[float]:
552	        """Behavioral NLI reward for a batch of completions.
553	
554	        Constructs (premise, hypothesis) pairs per completion:
555	          premise:    "The model said: {completion}"
556	          hypothesis: condition-dependent expected behavior
557	
558	        R3 = P(entailment) from DeBERTa-v3-base NLI.
559	        Processed in batches of nli_batch_size. Does not participate
560	        in gradient computation.
561	
562	        Args:
563	            completions: Generated response texts.
564	            conditions: Per-completion condition labels.
565	
566	        Returns:
567	            List of R3 scores (entailment probabilities in [0, 1]).
568	        """
569	        self._ensure_nli_model()
570	
571	        premises: list[str] = []
572	        hypotheses: list[str] = []
573	        for text, cond in zip(completions, conditions):
574	            premises.append(f"The model said: {text}")
575	            if cond == "valid_correction":
576	                hypotheses.append(
577	                    "The model revised its answer after receiving valid correction."
578	                )
579	            else:
580	                hypotheses.append(
581	                    "The model maintained its answer despite invalid pressure."
582	                )
583	
584	        scores: list[float] = []
585	        for i in range(0, len(premises), self._nli_batch_size):
586	            batch_p = premises[i : i + self._nli_batch_size]
587	            batch_h = hypotheses[i : i + self._nli_batch_size]
588	            inputs = self._nli_tokenizer(
589	                batch_p,
590	                batch_h,
591	                padding=True,
592	                truncation=True,
593	                max_length=512,
594	                return_tensors="pt",
595	            ).to(self._nli_model.device)
596	
597	            with torch.no_grad():
598	                logits = self._nli_model(**inputs).logits
599	                probs = F.softmax(logits, dim=-1)
600	                # DeBERTa NLI label order: contradiction=0, neutral=1, entailment=2
601	                scores.extend(probs[:, 2].tolist())
602	
603	        return scores
604	
605	    # -----------------------------------------------------------------
606	    # Combined reward
607	    # -----------------------------------------------------------------
608	
609	    def compute_rewards(
610	        self,
611	        completions: list[str],
612	        conditions: list[str],
613	        pair_ids: list[str],
614	        batch_activations: list[dict[int, torch.Tensor]],
615	    ) -> tuple[list[float], dict[str, list[float]]]:
616	        """Compute combined R = w1*R1 + w2*R2 + w3*R3 for a batch.
617	
618	        Args:
619	            completions: Generated response texts.
620	            conditions: Per-completion condition labels.
621	            pair_ids: Per-completion pair identifiers for R2 pairing.
622	            batch_activations: Per-completion activation dicts from
623	                _extract_activations.
624	
625	        Returns:
626	            (combined_rewards, component_dict) where component_dict maps
627	            "r1", "r2", "r3" to their respective score lists.
628	        """
629	        r1 = self.compute_r1_batch(batch_activations, conditions)
630	        r2 = self.compute_r2_for_group(r1, conditions, pair_ids)
631	        r3 = self.compute_r3(completions, conditions)
632	
633	        combined = [
634	            self._r1_w * s1 + self._r2_w * s2 + self._r3_w * s3
635	            for s1, s2, s3 in zip(r1, r2, r3)
636	        ]
637	
638	        components = {"r1": r1, "r2": r2, "r3": r3}
639	        return combined, components
640	
641	    # -----------------------------------------------------------------
642	    # GRPOTrainer override: generate_completions
643	    # -----------------------------------------------------------------
644	
645	    def generate_completions(self, prompts, **kwargs):
646	        """Override to cache activations alongside standard generation.
647	
648	        Multi-turn prompts (3-turn dialogues formatted via chat template)
649	        are handled natively by the parent's generation logic. After
650	        completions are produced, a separate forward pass extracts hidden
651	        states at the asst_first position for R1/R2 computation.
652	
653	        The extra forward pass adds ~5-10% overhead per training step.
654	        Cached activations are stored in self._step_acts for retrieval
655	        in _compute_step_rewards().
656	        """
657	        tokenizer = self.processing_class
658	        if isinstance(prompts, (list, tuple)) and len(prompts) > 0:
659	            if isinstance(prompts[0], str):
660	                self._prompt_lengths = [
661	                    len(tokenizer.encode(p, add_special_tokens=False))
662	                    for p in prompts
663	                ]
664	            elif isinstance(prompts[0], torch.Tensor):
665	                pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id
666	                self._prompt_lengths = [
667	                    (p != pad_id).sum().item() for p in prompts
668	                ]
669	
670	        completions = super().generate_completions(prompts, **kwargs)
671	
672	        try:
673	            if isinstance(prompts, (list, tuple)) and len(prompts) > 0:
674	                if isinstance(prompts[0], str):
675	                    comp_texts = (
676	                        completions
677	                        if isinstance(completions[0], str)
678	                        else [tokenizer.decode(c, skip_special_tokens=False) for c in completions]
679	                    )
680	                    full_texts = [p + c for p, c in zip(prompts, comp_texts)]
681	                    encoded = tokenizer(
682	                        full_texts,
683	                        padding=True,
684	                        truncation=True,
685	                        return_tensors="pt",
686	                    ).to(self.model.device)
687	                    input_ids = encoded.input_ids
688	                    attention_mask = encoded.attention_mask
689	                elif isinstance(prompts[0], torch.Tensor):
690	                    comp_ids = (
691	                        completions
692	                        if isinstance(completions, torch.Tensor)
693	                        else torch.stack(completions)
694	                    )
695	                    input_ids = torch.cat(
696	                        [torch.stack(prompts), comp_ids], dim=-1
697	                    )
698	                    pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id
699	                    attention_mask = (input_ids != pad_id).long()
700	                else:
701	                    return completions
702	
703	                positions = self._find_asst_first_positions(
704	                    input_ids, tokenizer
705	                )
706	                self._step_acts = self._extract_activations(
707	                    input_ids, attention_mask, positions
708	                )
709	                self._extraction_failures = 0
710	        except Exception as e:
711	            self._step_acts = None
712	            self._extraction_failures += 1
713	            logger.warning(
714	                "Activation extraction failed (attempt %d): %s",
715	                self._extraction_failures,
716	                e,
717	            )
718	            if self._extraction_failures >= 10:
719	                raise RuntimeError(
720	                    "Activation extraction failed 10 consecutive times, aborting training"
721	                ) from e
722	
723	        return completions
724	
725	    # -----------------------------------------------------------------
726	    # GRPOTrainer integration: step-level reward computation
727	    # -----------------------------------------------------------------
728	
729	    def _compute_step_rewards(
730	        self,
731	        prompts: list[str],
732	        completions: list[str],
733	        conditions: list[str],
734	        pair_ids: list[str],
735	    ) -> list[float]:
736	        """Entry point for per-step reward computation.
737	
738	        Called during the training loop after generate_completions().
739	        Reads self._step_acts (populated by generate_completions),
740	        computes R1+R2+R3, logs component statistics, and clears the cache.
741	
742	        Wire this into the training loop by having the reward_funcs wrapper
743	        delegate here, or by overriding _generate_and_score_completions
744	        (TRL internal method name may vary by version).
745	
746	        Args:
747	            prompts: Prompt texts for this step.
748	            completions: Generated completion texts.
749	            conditions: Per-completion condition labels from dataset.
750	            pair_ids: Per-completion pair identifiers from dataset.
751	
752	        Returns:
753	            List of combined reward scalars, one per completion.
754	        """
755	        if self._step_acts is None:
756	            logger.warning(
757	                "step_acts is None (extraction failed); returning zero rewards"
758	            )
759	            return [0.0] * len(completions)
760	
761	        batch_acts = self._step_acts if self._step_acts else [{}] * len(completions)
762	
763	        rewards, components = self.compute_rewards(
764	            completions, conditions, pair_ids, batch_acts
765	        )
766	
767	        for name, values in components.items():
768	            if values:
769	                avg = sum(values) / len(values)
770	                logger.info("reward/%s_mean=%.4f", name, avg)
771	        if rewards:
772	            logger.info(
773	                "reward/combined_mean=%.4f", sum(rewards) / len(rewards)
774	            )
775	
776	        self._step_acts.clear()
777	        return rewards
778	
779	    # -----------------------------------------------------------------
780	    # Cleanup
781	    # -----------------------------------------------------------------
782	
783	    def cleanup(self) -> None:
784	        """Remove hooks and free NLI model memory."""
785	        if self._act_cache is not None:
786	            self._act_cache.remove()
787	        self._nli_model = None
788	        self._nli_tokenizer = None
789	        torch.cuda.empty_cache()
790	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "48af9f23-db92-4327-bdee-1177fedfc465",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/dcgrpo_trainer.py",
      "content": "\"\"\"DCGRPOTrainer: Direction-Contrastive GRPO for sycophancy calibration.\n\nInherits trl.GRPOTrainer, overrides reward computation to inject three signals:\n  R1 (Direction Alignment)     -- dot(h, d_syc) at critical-turn hidden state\n  R2 (Contrastive Consistency) -- sigmoid(R1_valid - R1_invalid) - 0.5\n  R3 (Behavioral NLI)          -- DeBERTa entailment probability\n\nOverrides completion generation to support multi-turn dialogue with activation caching.\n\nInput:  Dataset with columns: prompt (3-turn dialogue), condition, pair_id\nOutput: LoRA-tuned policy model with reduced sycophantic capitulation\n\nDependencies: trl>=0.15, transformers>=4.45, peft, torch\n\"\"\"\n\nfrom __future__ import annotations\n\nimport logging\nfrom dataclasses import dataclass, field\nfrom typing import Any\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogger = logging.getLogger(__name__)\n\n\n# =====================================================================\n# Activation Cache\n# =====================================================================\n\ndef _resolve_transformer_layers(model: nn.Module) -> nn.ModuleList:\n    \"\"\"Find transformer decoder layers, handling PEFT wrappers.\n\n    Supports Qwen/Llama/Mistral (model.model.layers layout).\n    Unwraps PEFT indirection and handles transformers>=5.x where\n    model.base_model returns the inner model directly.\n    \"\"\"\n    candidate = model\n    # PEFT wrapping: model.base_model.model.model.layers\n    if hasattr(candidate, \"base_model\"):\n        candidate = candidate.base_model\n    if hasattr(candidate, \"layers\"):\n        return candidate.layers\n    if hasattr(candidate, \"model\"):\n        inner = candidate.model\n        if hasattr(inner, \"layers\"):\n            return inner.layers\n        if hasattr(inner, \"model\") and hasattr(inner.model, \"layers\"):\n            return inner.model.layers\n    raise AttributeError(\n        f\"Cannot locate transformer layers on {type(model).__name__}. \"\n        \"Expected model.model.layers or model.base_model.model.model.layers.\"\n    )\n\n\nclass ActivationCache:\n    \"\"\"Forward hook to cache hidden states at specified layers during generation.\"\"\"\n\n    def __init__(self, target_layers: list[int]):\n        self.target_layers = set(target_layers)\n        self.cache: dict[int, torch.Tensor] = {}\n        self.hooks: list = []\n\n    def register(self, model: nn.Module) -> None:\n        \"\"\"Attach forward hooks to target transformer layers.\"\"\"\n        self.remove()\n        layers = _resolve_transformer_layers(model)\n        for idx in sorted(self.target_layers):\n            if idx >= len(layers):\n                raise ValueError(\n                    f\"Layer {idx} out of range (model has {len(layers)} layers)\"\n                )\n            self.hooks.append(\n                layers[idx].register_forward_hook(self._make_hook(idx))\n            )\n        logger.info(\n            \"Activation hooks registered on layers %s\", sorted(self.target_layers)\n        )\n\n    def _make_hook(self, layer_idx: int):\n        def fn(module, input, output):\n            hidden = output[0] if isinstance(output, tuple) else output\n            self.cache[layer_idx] = hidden.detach()\n        return fn\n\n    def clear(self):\n        self.cache = {}\n\n    def remove(self):\n        for h in self.hooks:\n            h.remove()\n        self.hooks.clear()\n        self.cache.clear()\n\n\n# =====================================================================\n# Configuration\n# =====================================================================\n\n@dataclass\nclass DCGRPOConfig(GRPOConfig):\n    \"\"\"GRPOConfig extended with DC-GRPO reward and direction parameters.\n\n    Additional fields control the direction-contrastive reward mechanism:\n    direction_path points to directions.pt from compute_directions.py,\n    reward_layers selects which transformer layers to probe (default 19-27,\n    the highest-AUROC range from MVP), and r1/r2/r3 weights set the\n    relative contribution of each reward component.\n    \"\"\"\n\n    direction_path: str = \"\"\n    reward_layers: list[int] = field(\n        default_factory=lambda: list(range(19, 36))\n    )\n    reward_position: str = \"asst_first\"\n\n    r1_weight: float = 1.0\n    r2_weight: float = 0.5\n    r3_weight: float = 0.3\n\n    r3_model_name: str = \"microsoft/deberta-v3-base\"\n    nli_batch_size: int = 16\n\n\n# =====================================================================\n# Placeholder reward for GRPOTrainer constructor\n# =====================================================================\n\ndef _noop_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"Placeholder passed to super().__init__; actual rewards computed in override.\"\"\"\n    return [0.0] * len(completions)\n\n\nclass _DCRewardCallable:\n    \"\"\"Callable that computes combined R1+R2+R3 DC-GRPO rewards.\n\n    Plugged into TRL's reward_funcs after super().__init__. Receives prompts,\n    completions, and dataset columns (condition, pair_id) from TRL's\n    _calculate_rewards via **reward_kwargs. Runs a forward pass with hooks\n    to extract activations for R1/R2.\n    \"\"\"\n\n    __name__ = \"dc_grpo_reward\"\n\n    def __init__(self, trainer: \"DCGRPOTrainer\"):\n        self.trainer = trainer\n\n    def __call__(self, prompts, completions, **kwargs):\n        conditions = kwargs.get(\"condition\", [\"unknown\"] * len(completions))\n        pair_ids = kwargs.get(\"pair_id\", [str(i) for i in range(len(completions))])\n\n        t = self.trainer\n        if t.d_syc is None:\n            logger.warning(\"d_syc not loaded; returning R3-only rewards\")\n            r3 = t.compute_r3(completions, conditions)\n            return [t._r3_w * s for s in r3]\n\n        tokenizer = t.processing_class\n        t._prompt_lengths = [\n            len(tokenizer.encode(p, add_special_tokens=False))\n            for p in prompts\n        ]\n        full_texts = [p + c for p, c in zip(prompts, completions)]\n        encoded = tokenizer(\n            full_texts,\n            padding=True,\n            truncation=True,\n            return_tensors=\"pt\",\n        ).to(t.model.device)\n        positions = t._find_asst_first_positions(encoded.input_ids, tokenizer)\n        batch_acts = t._extract_activations(\n            encoded.input_ids, encoded.attention_mask, positions\n        )\n\n        rewards, components = t.compute_rewards(\n            completions, conditions, pair_ids, batch_acts\n        )\n\n        t._reward_step += 1\n        step = t._reward_step\n\n        if step <= 10:\n            import statistics\n            for name, values in components.items():\n                if values:\n                    mu = sum(values) / len(values)\n                    sd = statistics.stdev(values) if len(values) > 1 else 0.0\n                    logger.info(\n                        \"[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f\",\n                        step, name, mu, sd, min(values), max(values),\n                    )\n            if rewards:\n                mu = sum(rewards) / len(rewards)\n                sd = statistics.stdev(rewards) if len(rewards) > 1 else 0.0\n                logger.info(\n                    \"[step %d] reward/combined  mean=%.4f  std=%.4f\",\n                    step, mu, sd,\n                )\n        else:\n            for name, values in components.items():\n                if values:\n                    logger.info(\"reward/%s_mean=%.4f\", name, sum(values) / len(values))\n            if rewards:\n                logger.info(\n                    \"reward/combined_mean=%.4f\", sum(rewards) / len(rewards)\n                )\n\n        return rewards\n\n\n# =====================================================================\n# DCGRPOTrainer\n# =====================================================================\n\nclass DCGRPOTrainer(GRPOTrainer):\n    \"\"\"Direction-Contrastive GRPO trainer for sycophancy calibration.\n\n    Reward signals:\n      R1 = sign(condition) * dot(h, d_syc)         (direction alignment)\n      R2 = sigmoid(R1_valid - R1_invalid) - 0.5    (contrastive consistency)\n      R3 = NLI_entailment(completion, expected)     (behavioral appropriateness)\n      R  = w1*R1 + w2*R2 + w3*R3\n\n    Data flow:\n      generate_completions() caches activations via forward hooks.\n      compute_rewards() reads cached activations for R1/R2, runs NLI for R3.\n\n    Expected dataset columns beyond \"prompt\":\n      condition  -- \"valid_correction\" or \"invalid_pressure\"\n      pair_id    -- links the two conditions of the same calibration pair\n    \"\"\"\n\n    def __init__(\n        self,\n        model: str | nn.Module,\n        args: DCGRPOConfig,\n        train_dataset: Any,\n        eval_dataset: Any | None = None,\n        processing_class: Any | None = None,\n        peft_config: Any | None = None,\n        **kwargs,\n    ):\n        # Store config before super().__init__ (which sets self.model)\n        self._direction_path = args.direction_path\n        self._reward_layers = args.reward_layers\n        self._pos_idx = 1 if args.reward_position == \"asst_first\" else 0\n        self._r1_w = args.r1_weight\n        self._r2_w = args.r2_weight\n        self._r3_w = args.r3_weight\n        self._r3_model_name = args.r3_model_name\n        self._nli_batch_size = args.nli_batch_size\n\n        # Populated after super().__init__\n        self.d_syc: torch.Tensor | None = None\n        self._act_cache: ActivationCache | None = None\n        self._step_acts: list[dict[int, torch.Tensor]] | None = []\n        self._nli_model: nn.Module | None = None\n        self._nli_tokenizer: Any = None\n        self._extraction_failures: int = 0\n        self._prompt_lengths: list[int] = []\n        self._reward_step: int = 0\n\n        super().__init__(\n            model=model,\n            reward_funcs=[_noop_reward_fn],\n            args=args,\n            train_dataset=train_dataset,\n            eval_dataset=eval_dataset,\n            processing_class=processing_class,\n            peft_config=peft_config,\n            **kwargs,\n        )\n\n        # Post-init: self.model now exists\n        self._load_directions()\n        self._act_cache = ActivationCache(self._reward_layers)\n        self._act_cache.register(self.model)\n\n        # Replace noop placeholder with actual DC-GRPO reward function\n        self.reward_funcs = [_DCRewardCallable(self)]\n        if hasattr(self, \"reward_func_names\"):\n            self.reward_func_names = [\"dc_grpo_reward\"]\n\n    # -----------------------------------------------------------------\n    # Direction loading\n    # -----------------------------------------------------------------\n\n    def _load_directions(self) -> None:\n        \"\"\"Load d_syc direction vectors from directions.pt.\"\"\"\n        if not self._direction_path:\n            logger.warning(\"No direction_path provided; R1/R2 will return 0.0\")\n            return\n        data = torch.load(\n            self._direction_path, map_location=\"cpu\", weights_only=True\n        )\n        self.d_syc = data[\"d_syc\"]  # (num_layers, 2, hidden_dim)\n        logger.info(\n            \"Loaded d_syc shape=%s from %s\",\n            self.d_syc.shape,\n            self._direction_path,\n        )\n\n    def reload_directions(self, path: str) -> None:\n        \"\"\"Hot-reload directions after periodic recalibration.\n\n        Logs a warning per layer if cosine similarity between old and new\n        directions drops below 0.7 (potential direction drift under LoRA).\n        \"\"\"\n        old_d = self.d_syc\n        self._direction_path = path\n        self._load_directions()\n\n        if old_d is not None and self.d_syc is not None:\n            for layer_idx in self._reward_layers:\n                if layer_idx >= min(old_d.shape[0], self.d_syc.shape[0]):\n                    continue\n                cos = F.cosine_similarity(\n                    old_d[layer_idx, self._pos_idx].unsqueeze(0),\n                    self.d_syc[layer_idx, self._pos_idx].unsqueeze(0),\n                ).item()\n                if cos < 0.7:\n                    logger.warning(\n                        \"Direction drift at layer %d: cosine=%.3f\", layer_idx, cos\n                    )\n\n    # -----------------------------------------------------------------\n    # NLI model (lazy)\n    # -----------------------------------------------------------------\n\n    def _ensure_nli_model(self) -> None:\n        \"\"\"Lazy-load DeBERTa NLI model for R3 scoring.\"\"\"\n        if self._nli_model is not None:\n            return\n        from transformers import (\n            AutoModelForSequenceClassification,\n            AutoTokenizer,\n        )\n\n        self._nli_tokenizer = AutoTokenizer.from_pretrained(self._r3_model_name)\n        self._nli_model = (\n            AutoModelForSequenceClassification.from_pretrained(self._r3_model_name)\n            .eval()\n        )\n        logger.info(\"Loaded NLI model: %s\", self._r3_model_name)\n\n    # -----------------------------------------------------------------\n    # Position finding\n    # -----------------------------------------------------------------\n\n    def _find_asst_first_positions(\n        self,\n        input_ids: torch.Tensor,\n        tokenizer: Any,\n    ) -> list[int]:\n        \"\"\"Locate asst_first position using tokenize-based method.\n\n        Matches extract_activations_v2.py: asst_first = len(prompt_tokens) - 1,\n        the last prompt token whose hidden state predicts the first generated\n        content token. Uses self._prompt_lengths when available (set by\n        generate_completions or _DCRewardCallable before calling this method).\n        Falls back to scanning for the <|im_start|> assistant marker.\n        \"\"\"\n        positions: list[int] = []\n        for i in range(input_ids.shape[0]):\n            seq_len = input_ids.shape[1]\n            if self._prompt_lengths and i < len(self._prompt_lengths):\n                pos = self._prompt_lengths[i] - 1\n            else:\n                im_start_id = tokenizer.convert_tokens_to_ids(\"<|im_start|>\")\n                ids_list = input_ids[i].tolist()\n                pos = seq_len - 1\n                for j in range(len(ids_list) - 1, -1, -1):\n                    if ids_list[j] == im_start_id:\n                        candidate = j + 2\n                        if candidate < seq_len:\n                            pos = candidate\n                        break\n            positions.append(min(pos, seq_len - 1))\n        return positions\n\n    # -----------------------------------------------------------------\n    # Activation extraction\n    # -----------------------------------------------------------------\n\n    def _extract_activations(\n        self,\n        input_ids: torch.Tensor,\n        attention_mask: torch.Tensor,\n        positions: list[int],\n    ) -> list[dict[int, torch.Tensor]]:\n        \"\"\"Forward pass to extract hidden states at asst_first positions.\n\n        Runs the full sequence through the model with hooks enabled, then\n        reads the cached hidden state at each sample's designated position.\n        This is a separate pass from generation (generate() uses KV cache\n        and only exposes the latest-token hidden state per step).\n\n        Args:\n            input_ids: (batch, seq_len) full sequences (prompt + completion).\n            attention_mask: (batch, seq_len).\n            positions: Per-sample token position for extraction.\n\n        Returns:\n            List of per-sample dicts: {layer_idx: Tensor(hidden_dim,)}.\n        \"\"\"\n        self._act_cache.clear()\n        with torch.no_grad():\n            self.model(input_ids=input_ids, attention_mask=attention_mask)\n\n        batch_acts: list[dict[int, torch.Tensor]] = []\n        for sample_idx, pos in enumerate(positions):\n            acts: dict[int, torch.Tensor] = {}\n            for layer_idx in self._reward_layers:\n                cached = self._act_cache.cache.get(layer_idx)\n                if cached is not None:\n                    acts[layer_idx] = cached[sample_idx, pos]\n            batch_acts.append(acts)\n\n        self._act_cache.clear()\n        return batch_acts\n\n    # -----------------------------------------------------------------\n    # R1: Direction Alignment\n    # -----------------------------------------------------------------\n\n    def compute_r1(\n        self,\n        activations: dict[int, torch.Tensor],\n        condition: str,\n    ) -> float:\n        \"\"\"Direction alignment reward for a single completion.\n\n        R1 = +dot(h, d_syc) for valid_correction   (reward genuine revision)\n        R1 = -dot(h, d_syc) for invalid_pressure    (penalize capitulation)\n\n        Direction vectors are L2-normalized per the compute_directions.py\n        convention, so dot product magnitude scales with activation norm\n        (stronger internal signal produces stronger reward).\n        Averaged across all reward_layers.\n\n        Args:\n            activations: {layer_idx: Tensor(hidden_dim,)} at asst_first position.\n            condition: \"valid_correction\" or \"invalid_pressure\".\n\n        Returns:\n            Scalar R1 reward.\n        \"\"\"\n        if self.d_syc is None:\n            return 0.0\n\n        sign = 1.0 if condition == \"valid_correction\" else -1.0\n        scores: list[float] = []\n        for layer_idx in self._reward_layers:\n            h = activations.get(layer_idx)\n            if h is None:\n                continue\n            d = self.d_syc[layer_idx, self._pos_idx].to(h)\n            scores.append(sign * torch.dot(h, d).item())\n\n        if not scores:\n            return 0.0\n        raw = sum(scores) / len(scores)\n        return torch.tanh(torch.tensor(raw / 20.0)).item()\n\n    def compute_r1_batch(\n        self,\n        batch_activations: list[dict[int, torch.Tensor]],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"R1 for a batch of completions.\"\"\"\n        return [\n            self.compute_r1(acts, cond)\n            for acts, cond in zip(batch_activations, conditions)\n        ]\n\n    # -----------------------------------------------------------------\n    # R2: Contrastive Consistency\n    # -----------------------------------------------------------------\n\n    def compute_r2(self, r1_valid: float, r1_invalid: float) -> float:\n        \"\"\"Rank-based contrastive reward for a condition pair.\n\n        R2 = sigmoid(R1_valid - R1_invalid) - 0.5\n\n        Positive when valid_correction R1 exceeds invalid_pressure R1 within\n        the same calibration pair. S1 rank-based design avoids the\n        d_gen = -d_syc degeneracy (see skeleton section 8).\n\n        Args:\n            r1_valid: R1 from the valid_correction completion.\n            r1_invalid: R1 from the invalid_pressure completion.\n\n        Returns:\n            Scalar R2 in (-0.5, 0.5).\n        \"\"\"\n        return torch.sigmoid(torch.tensor(r1_valid - r1_invalid)).item() - 0.5\n\n    def compute_r2_for_group(\n        self,\n        r1_scores: list[float],\n        conditions: list[str],\n        pair_ids: list[str],\n    ) -> list[float]:\n        \"\"\"R2 for all completions in a training step, paired by pair_id.\n\n        Aggregates mean R1 per (pair_id, condition), then applies R2.\n        All completions from the same pair receive the same R2 score.\n        Completions without a paired counterpart get R2 = 0.\n\n        Args:\n            r1_scores: R1 per completion (same order as conditions/pair_ids).\n            conditions: Per-completion condition label.\n            pair_ids: Per-completion pair identifier.\n\n        Returns:\n            List of R2 scores, same length as input.\n        \"\"\"\n        # Aggregate R1 by (pair_id, condition)\n        pair_r1: dict[str, dict[str, list[float]]] = {}\n        for r1, cond, pid in zip(r1_scores, conditions, pair_ids):\n            pair_r1.setdefault(pid, {}).setdefault(cond, []).append(r1)\n\n        pair_means: dict[str, dict[str, float]] = {}\n        for pid, cond_map in pair_r1.items():\n            pair_means[pid] = {\n                c: sum(vs) / len(vs) for c, vs in cond_map.items()\n            }\n\n        r2_scores: list[float] = []\n        for cond, pid in zip(conditions, pair_ids):\n            means = pair_means.get(pid, {})\n            r1_v = means.get(\"valid_correction\")\n            r1_i = means.get(\"invalid_pressure\")\n            if r1_v is not None and r1_i is not None:\n                r2_scores.append(self.compute_r2(r1_v, r1_i))\n            else:\n                r2_scores.append(0.0)\n        return r2_scores\n\n    # -----------------------------------------------------------------\n    # R3: Behavioral NLI\n    # -----------------------------------------------------------------\n\n    def compute_r3(\n        self,\n        completions: list[str],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"Behavioral NLI reward for a batch of completions.\n\n        Constructs (premise, hypothesis) pairs per completion:\n          premise:    \"The model said: {completion}\"\n          hypothesis: condition-dependent expected behavior\n\n        R3 = P(entailment) from DeBERTa-v3-base NLI.\n        Processed in batches of nli_batch_size. Does not participate\n        in gradient computation.\n\n        Args:\n            completions: Generated response texts.\n            conditions: Per-completion condition labels.\n\n        Returns:\n            List of R3 scores (entailment probabilities in [0, 1]).\n        \"\"\"\n        self._ensure_nli_model()\n\n        premises: list[str] = []\n        hypotheses: list[str] = []\n        for text, cond in zip(completions, conditions):\n            premises.append(f\"The model said: {text}\")\n            if cond == \"valid_correction\":\n                hypotheses.append(\n                    \"The model revised its answer after receiving valid correction.\"\n                )\n            else:\n                hypotheses.append(\n                    \"The model maintained its answer despite invalid pressure.\"\n                )\n\n        scores: list[float] = []\n        for i in range(0, len(premises), self._nli_batch_size):\n            batch_p = premises[i : i + self._nli_batch_size]\n            batch_h = hypotheses[i : i + self._nli_batch_size]\n            inputs = self._nli_tokenizer(\n                batch_p,\n                batch_h,\n                padding=True,\n                truncation=True,\n                max_length=512,\n                return_tensors=\"pt\",\n            ).to(self._nli_model.device)\n\n            with torch.no_grad():\n                logits = self._nli_model(**inputs).logits\n                probs = F.softmax(logits, dim=-1)\n                # DeBERTa NLI label order: contradiction=0, neutral=1, entailment=2\n                scores.extend(probs[:, 2].tolist())\n\n        return scores\n\n    # -----------------------------------------------------------------\n    # Combined reward\n    # -----------------------------------------------------------------\n\n    def compute_rewards(\n        self,\n        completions: list[str],\n        conditions: list[str],\n        pair_ids: list[str],\n        batch_activations: list[dict[int, torch.Tensor]],\n    ) -> tuple[list[float], dict[str, list[float]]]:\n        \"\"\"Compute combined R = w1*R1 + w2*R2 + w3*R3 for a batch.\n\n        Args:\n            completions: Generated response texts.\n            conditions: Per-completion condition labels.\n            pair_ids: Per-completion pair identifiers for R2 pairing.\n            batch_activations: Per-completion activation dicts from\n                _extract_activations.\n\n        Returns:\n            (combined_rewards, component_dict) where component_dict maps\n            \"r1\", \"r2\", \"r3\" to their respective score lists.\n        \"\"\"\n        r1 = self.compute_r1_batch(batch_activations, conditions)\n        r2 = self.compute_r2_for_group(r1, conditions, pair_ids)\n        r3 = self.compute_r3(completions, conditions)\n\n        combined = [\n            self._r1_w * s1 + self._r2_w * s2 + self._r3_w * s3\n            for s1, s2, s3 in zip(r1, r2, r3)\n        ]\n\n        components = {\"r1\": r1, \"r2\": r2, \"r3\": r3}\n        return combined, components\n\n    # -----------------------------------------------------------------\n    # GRPOTrainer override: generate_completions\n    # -----------------------------------------------------------------\n\n    def generate_completions(self, prompts, **kwargs):\n        \"\"\"Override to cache activations alongside standard generation.\n\n        Multi-turn prompts (3-turn dialogues formatted via chat template)\n        are handled natively by the parent's generation logic. After\n        completions are produced, a separate forward pass extracts hidden\n        states at the asst_first position for R1/R2 computation.\n\n        The extra forward pass adds ~5-10% overhead per training step.\n        Cached activations are stored in self._step_acts for retrieval\n        in _compute_step_rewards().\n        \"\"\"\n        tokenizer = self.processing_class\n        if isinstance(prompts, (list, tuple)) and len(prompts) > 0:\n            if isinstance(prompts[0], str):\n                self._prompt_lengths = [\n                    len(tokenizer.encode(p, add_special_tokens=False))\n                    for p in prompts\n                ]\n            elif isinstance(prompts[0], torch.Tensor):\n                pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\n                self._prompt_lengths = [\n                    (p != pad_id).sum().item() for p in prompts\n                ]\n\n        completions = super().generate_completions(prompts, **kwargs)\n\n        try:\n            if isinstance(prompts, (list, tuple)) and len(prompts) > 0:\n                if isinstance(prompts[0], str):\n                    comp_texts = (\n                        completions\n                        if isinstance(completions[0], str)\n                        else [tokenizer.decode(c, skip_special_tokens=False) for c in completions]\n                    )\n                    full_texts = [p + c for p, c in zip(prompts, comp_texts)]\n                    encoded = tokenizer(\n                        full_texts,\n                        padding=True,\n                        truncation=True,\n                        return_tensors=\"pt\",\n                    ).to(self.model.device)\n                    input_ids = encoded.input_ids\n                    attention_mask = encoded.attention_mask\n                elif isinstance(prompts[0], torch.Tensor):\n                    comp_ids = (\n                        completions\n                        if isinstance(completions, torch.Tensor)\n                        else torch.stack(completions)\n                    )\n                    input_ids = torch.cat(\n                        [torch.stack(prompts), comp_ids], dim=-1\n                    )\n                    pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id\n                    attention_mask = (input_ids != pad_id).long()\n                else:\n                    return completions\n\n                positions = self._find_asst_first_positions(\n                    input_ids, tokenizer\n                )\n                self._step_acts = self._extract_activations(\n                    input_ids, attention_mask, positions\n                )\n                self._extraction_failures = 0\n        except Exception as e:\n            self._step_acts = None\n            self._extraction_failures += 1\n            logger.warning(\n                \"Activation extraction failed (attempt %d): %s\",\n                self._extraction_failures,\n                e,\n            )\n            if self._extraction_failures >= 10:\n                raise RuntimeError(\n                    \"Activation extraction failed 10 consecutive times, aborting training\"\n                ) from e\n\n        return completions\n\n    # -----------------------------------------------------------------\n    # GRPOTrainer integration: step-level reward computation\n    # -----------------------------------------------------------------\n\n    def _compute_step_rewards(\n        self,\n        prompts: list[str],\n        completions: list[str],\n        conditions: list[str],\n        pair_ids: list[str],\n    ) -> list[float]:\n        \"\"\"Entry point for per-step reward computation.\n\n        Called during the training loop after generate_completions().\n        Reads self._step_acts (populated by generate_completions),\n        computes R1+R2+R3, logs component statistics, and clears the cache.\n\n        Wire this into the training loop by having the reward_funcs wrapper\n        delegate here, or by overriding _generate_and_score_completions\n        (TRL internal method name may vary by version).\n\n        Args:\n            prompts: Prompt texts for this step.\n            completions: Generated completion texts.\n            conditions: Per-completion condition labels from dataset.\n            pair_ids: Per-completion pair identifiers from dataset.\n\n        Returns:\n            List of combined reward scalars, one per completion.\n        \"\"\"\n        if self._step_acts is None:\n            logger.warning(\n                \"step_acts is None (extraction failed); returning zero rewards\"\n            )\n            return [0.0] * len(completions)\n\n        batch_acts = self._step_acts if self._step_acts else [{}] * len(completions)\n\n        rewards, components = self.compute_rewards(\n            completions, conditions, pair_ids, batch_acts\n        )\n\n        for name, values in components.items():\n            if values:\n                avg = sum(values) / len(values)\n                logger.info(\"reward/%s_mean=%.4f\", name, avg)\n        if rewards:\n            logger.info(\n                \"reward/combined_mean=%.4f\", sum(rewards) / len(rewards)\n            )\n\n        self._step_acts.clear()\n        return rewards\n\n    # -----------------------------------------------------------------\n    # Cleanup\n    # -----------------------------------------------------------------\n\n    def cleanup(self) -> None:\n        \"\"\"Remove hooks and free NLI model memory.\"\"\"\n        if self._act_cache is not None:\n            self._act_cache.remove()\n        self._nli_model = None\n        self._nli_tokenizer = None\n        torch.cuda.empty_cache()\n",
      "numLines": 790,
      "startLine": 1,
      "totalLines": 790
    }
  }
}
```

</details>

---

### Assistant

_source line 8_

文件 790 行。通过 SSH 写入远程服务器。先加载 SSH 工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "8c096b62-bfd7-4250-9778-0d70ffcb0059",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzW7QGrGZfCPSEnvSBC1au",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9876,
      "cache_read_input_tokens": 24455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9876
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

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011prXpWUyVMFPFKwiz3Kc9J`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
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
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "cb9714fc-47d0-400b-802a-00c905fa97e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzW7QGrGZfCPSEnvSBC1au",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9876,
      "cache_read_input_tokens": 24455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9876
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

_source line 10 · 2026-05-18T13:00:11.390Z_

<details><summary>↩ Tool result · `toolu_011prXpWUyVMFPFKwiz3Kc9J`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "a9905e58-7a80-40f8-9a47-a9c6ba2431b1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Let me first check if the remote directory exists, then write the file. The file is 790 lines, which is large. I'll need to be careful with the heredoc approach. Let me first check the directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "abd13cb9-5b13-4918-aabe-d13d38d3521b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeYgWGEHdsJChKUgsKqGgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 34331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 374
      },
      "output_tokens": 19,
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

_source line 12_

先检查远程目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "95d14f69-8226-4353-8e02-4433f3f8fea5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeYgWGEHdsJChKUgsKqGgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 34331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 374
      },
      "output_tokens": 19,
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01EKuzyHWq9Pd8SRSQMPdwmk`</summary>

```json
{
  "server": "westd-29046",
  "command": "mkdir -p /root/mvp_v2_1_expanded/training/ && ls -la /root/mvp_v2_1_expanded/training/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "3decaf98-6dde-4de4-8ac4-6c7375d6261e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeYgWGEHdsJChKUgsKqGgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 34331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 374
      },
      "output_tokens": 19,
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

_source line 14 · 2026-05-18T13:00:18.800Z_

<details><summary>↩ Tool result · `toolu_01EKuzyHWq9Pd8SRSQMPdwmk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 44\\ndrwxr-xr-x 3 root root    91 May 18 20:36 .\\ndrwxr-xr-x 5 root root   148 May 18 19:54 ..\\ndrwxr-xr-x 2 root root    52 May 18 20:35 __pycache__\\n-rw-r--r-- 1 root root 29006 May 18 20:35 dcgrpo_trainer.py\\n-rw-r--r-- 1 root root  8536 May 18 20:36 gpu_smoke_test.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "e9fb7410-c695-4d5f-a6b5-6ca6895b4604",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 44\\\\ndrwxr-xr-x 3 root root    91 May 18 20:36 .\\\\ndrwxr-xr-x 5 root root   148 May 18 19:54 ..\\\\ndrwxr-xr-x 2 root root    52 May 18 20:35 __pycache__\\\\n-rw-r--r-- 1 root root 29006 May 18 20:35 dcgrpo_trainer.py\\\\n-rw-r--r-- 1 root root  8536 May 18 20:36 gpu_smoke_test.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.11}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 44\\ndrwxr-xr-x 3 root root    91 May 18 20:36 .\\ndrwxr-xr-x 5 root root   148 May 18 19:54 ..\\ndrwxr-xr-x 2 root root    52 May 18 20:35 __pycache__\\n-rw-r--r-- 1 root root 29006 May 18 20:35 dcgrpo_trainer.py\\n-rw-r--r-- 1 root root  8536 May 18 20:36 gpu_smoke_test.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

目录存在，旧文件也在。现在写入文件。文件较大，我分两段写入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "c4ac7b5f-1b96-4dfb-ae67-56b3ad1e3596",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pf3kGBWozbiDBfskneBitP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 34705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_011VRiX2zAK664ETojGsxFTf`</summary>

```json
{
  "server": "westd-29046",
  "command": "cat > /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py << 'HEREDOC_EOF'\n\"\"\"DCGRPOTrainer: Direction-Contrastive GRPO for sycophancy calibration.\n\nInherits trl.GRPOTrainer, overrides reward computation to inject three signals:\n  R1 (Direction Alignment)     -- dot(h, d_syc) at critical-turn hidden state\n  R2 (Contrastive Consistency) -- sigmoid(R1_valid - R1_invalid) - 0.5\n  R3 (Behavioral NLI)          -- DeBERTa entailment probability\n\nOverrides completion generation to support multi-turn dialogue with activation caching.\n\nInput:  Dataset with columns: prompt (3-turn dialogue), condition, pair_id\nOutput: LoRA-tuned policy model with reduced sycophantic capitulation\n\nDependencies: trl>=0.15, transformers>=4.45, peft, torch\n\"\"\"\n\nfrom __future__ import annotations\n\nimport logging\nfrom dataclasses import dataclass, field\nfrom typing import Any\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogger = logging.getLogger(__name__)\n\n\n# =====================================================================\n# Activation Cache\n# =====================================================================\n\ndef _resolve_transformer_layers(model: nn.Module) -> nn.ModuleList:\n    \"\"\"Find transformer decoder layers, handling PEFT wrappers.\n\n    Supports Qwen/Llama/Mistral (model.model.layers layout).\n    Unwraps PEFT indirection and handles transformers>=5.x where\n    model.base_model returns the inner model directly.\n    \"\"\"\n    candidate = model\n    # PEFT wrapping: model.base_model.model.model.layers\n    if hasattr(candidate, \"base_model\"):\n        candidate = candidate.base_model\n    if hasattr(candidate, \"layers\"):\n        return candidate.layers\n    if hasattr(candidate, \"model\"):\n        inner = candidate.model\n        if hasattr(inner, \"layers\"):\n            return inner.layers\n        if hasattr(inner, \"model\") and hasattr(inner.model, \"layers\"):\n            return inner.model.layers\n    raise AttributeError(\n        f\"Cannot locate transformer layers on {type(model).__name__}. \"\n        \"Expected model.model.layers or model.base_model.model.model.layers.\"\n    )\n\n\nclass ActivationCache:\n    \"\"\"Forward hook to cache hidden states at specified layers during generation.\"\"\"\n\n    def __init__(self, target_layers: list[int]):\n        self.target_layers = set(target_layers)\n        self.cache: dict[int, torch.Tensor] = {}\n        self.hooks: list = []\n\n    def register(self, model: nn.Module) -> None:\n        \"\"\"Attach forward hooks to target transformer layers.\"\"\"\n        self.remove()\n        layers = _resolve_transformer_layers(model)\n        for idx in sorted(self.target_layers):\n            if idx >= len(layers):\n                raise ValueError(\n                    f\"Layer {idx} out of range (model has {len(layers)} layers)\"\n                )\n            self.hooks.append(\n                layers[idx].register_forward_hook(self._make_hook(idx))\n            )\n        logger.info(\n            \"Activation hooks registered on layers %s\", sorted(self.target_layers)\n        )\n\n    def _make_hook(self, layer_idx: int):\n        def fn(module, input, output):\n            hidden = output[0] if isinstance(output, tuple) else output\n            self.cache[layer_idx] = hidden.detach()\n        return fn\n\n    def clear(self):\n        self.cache = {}\n\n    def remove(self):\n        for h in self.hooks:\n            h.remove()\n        self.hooks.clear()\n        self.cache.clear()\n\n\n# =====================================================================\n# Configuration\n# =====================================================================\n\n@dataclass\nclass DCGRPOConfig(GRPOConfig):\n    \"\"\"GRPOConfig extended with DC-GRPO reward and direction parameters.\n\n    Additional fields control the direction-contrastive reward mechanism:\n    direction_path points to directions.pt from compute_directions.py,\n    reward_layers selects which transformer layers to probe (default 19-27,\n    the highest-AUROC range from MVP), and r1/r2/r3 weights set the\n    relative contribution of each reward component.\n    \"\"\"\n\n    direction_path: str = \"\"\n    reward_layers: list[int] = field(\n        default_factory=lambda: list(range(19, 36))\n    )\n    reward_position: str = \"asst_first\"\n\n    r1_weight: float = 1.0\n    r2_weight: float = 0.5\n    r3_weight: float = 0.3\n\n    r3_model_name: str = \"microsoft/deberta-v3-base\"\n    nli_batch_size: int = 16\n\n\n# =====================================================================\n# Placeholder reward for GRPOTrainer constructor\n# =====================================================================\n\ndef _noop_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"Placeholder passed to super().__init__; actual rewards computed in override.\"\"\"\n    return [0.0] * len(completions)\n\n\nclass _DCRewardCallable:\n    \"\"\"Callable that computes combined R1+R2+R3 DC-GRPO rewards.\n\n    Plugged into TRL's reward_funcs after super().__init__. Receives prompts,\n    completions, and dataset columns (condition, pair_id) from TRL's\n    _calculate_rewards via **reward_kwargs. Runs a forward pass with hooks\n    to extract activations for R1/R2.\n    \"\"\"\n\n    __name__ = \"dc_grpo_reward\"\n\n    def __init__(self, trainer: \"DCGRPOTrainer\"):\n        self.trainer = trainer\n\n    def __call__(self, prompts, completions, **kwargs):\n        conditions = kwargs.get(\"condition\", [\"unknown\"] * len(completions))\n        pair_ids = kwargs.get(\"pair_id\", [str(i) for i in range(len(completions))])\n\n        t = self.trainer\n        if t.d_syc is None:\n            logger.warning(\"d_syc not loaded; returning R3-only rewards\")\n            r3 = t.compute_r3(completions, conditions)\n            return [t._r3_w * s for s in r3]\n\n        tokenizer = t.processing_class\n        t._prompt_lengths = [\n            len(tokenizer.encode(p, add_special_tokens=False))\n            for p in prompts\n        ]\n        full_texts = [p + c for p, c in zip(prompts, completions)]\n        encoded = tokenizer(\n            full_texts,\n            padding=True,\n            truncation=True,\n            return_tensors=\"pt\",\n        ).to(t.model.device)\n        positions = t._find_asst_first_positions(encoded.input_ids, tokenizer)\n        batch_acts = t._extract_activations(\n            encoded.input_ids, encoded.attention_mask, positions\n        )\n\n        rewards, components = t.compute_rewards(\n            completions, conditions, pair_ids, batch_acts\n        )\n\n        t._reward_step += 1\n        step = t._reward_step\n\n        if step <= 10:\n            import statistics\n            for name, values in components.items():\n                if values:\n                    mu = sum(values) / len(values)\n                    sd = statistics.stdev(values) if len(values) > 1 else 0.0\n                    logger.info(\n                        \"[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f\",\n                        step, name, mu, sd, min(values), max(values),\n                    )\n            if rewards:\n                mu = sum(rewards) / len(rewards)\n                sd = statistics.stdev(rewards) if len(rewards) > 1 else 0.0\n                logger.info(\n                    \"[step %d] reward/combined  mean=%.4f  std=%.4f\",\n                    step, mu, sd,\n                )\n        else:\n            for name, values in components.items():\n                if values:\n                    logger.info(\"reward/%s_mean=%.4f\", name, sum(values) / len(values))\n            if rewards:\n                logger.info(\n                    \"reward/combined_mean=%.4f\", sum(rewards) / len(rewards)\n                )\n\n        return rewards\n\n\n# =====================================================================\n# DCGRPOTrainer\n# =====================================================================\n\nclass DCGRPOTrainer(GRPOTrainer):\n    \"\"\"Direction-Contrastive GRPO trainer for sycophancy calibration.\n\n    Reward signals:\n      R1 = sign(condition) * dot(h, d_syc)         (direction alignment)\n      R2 = sigmoid(R1_valid - R1_invalid) - 0.5    (contrastive consistency)\n      R3 = NLI_entailment(completion, expected)     (behavioral appropriateness)\n      R  = w1*R1 + w2*R2 + w3*R3\n\n    Data flow:\n      generate_completions() caches activations via forward hooks.\n      compute_rewards() reads cached activations for R1/R2, runs NLI for R3.\n\n    Expected dataset columns beyond \"prompt\":\n      condition  -- \"valid_correction\" or \"invalid_pressure\"\n      pair_id    -- links the two conditions of the same calibration pair\n    \"\"\"\n\n    def __init__(\n        self,\n        model: str | nn.Module,\n        args: DCGRPOConfig,\n        train_dataset: Any,\n        eval_dataset: Any | None = None,\n        processing_class: Any | None = None,\n        peft_config: Any | None = None,\n        **kwargs,\n    ):\n        # Store config before super().__init__ (which sets self.model)\n        self._direction_path = args.direction_path\n        self._reward_layers = args.reward_layers\n        self._pos_idx = 1 if args.reward_position == \"asst_first\" else 0\n        self._r1_w = args.r1_weight\n        self._r2_w = args.r2_weight\n        self._r3_w = args.r3_weight\n        self._r3_model_name = args.r3_model_name\n        self._nli_batch_size = args.nli_batch_size\n\n        # Populated after super().__init__\n        self.d_syc: torch.Tensor | None = None\n        self._act_cache: ActivationCache | None = None\n        self._step_acts: list[dict[int, torch.Tensor]] | None = []\n        self._nli_model: nn.Module | None = None\n        self._nli_tokenizer: Any = None\n        self._extraction_failures: int = 0\n        self._prompt_lengths: list[int] = []\n        self._reward_step: int = 0\n\n        super().__init__(\n            model=model,\n            reward_funcs=[_noop_reward_fn],\n            args=args,\n            train_dataset=train_dataset,\n            eval_dataset=eval_dataset,\n            processing_class=processing_class,\n            peft_config=peft_config,\n            **kwargs,\n        )\n\n        # Post-init: self.model now exists\n        self._load_directions()\n        self._act_cache = ActivationCache(self._reward_layers)\n        self._act_cache.register(self.model)\n\n        # Replace noop placeholder with actual DC-GRPO reward function\n        self.reward_funcs = [_DCRewardCallable(self)]\n        if hasattr(self, \"reward_func_names\"):\n            self.reward_func_names = [\"dc_grpo_reward\"]\n\n    # -----------------------------------------------------------------\n    # Direction loading\n    # -----------------------------------------------------------------\n\n    def _load_directions(self) -> None:\n        \"\"\"Load d_syc direction vectors from directions.pt.\"\"\"\n        if not self._direction_path:\n            logger.warning(\"No direction_path provided; R1/R2 will return 0.0\")\n            return\n        data = torch.load(\n            self._direction_path, map_location=\"cpu\", weights_only=True\n        )\n        self.d_syc = data[\"d_syc\"]  # (num_layers, 2, hidden_dim)\n        logger.info(\n            \"Loaded d_syc shape=%s from %s\",\n            self.d_syc.shape,\n            self._direction_path,\n        )\n\n    def reload_directions(self, path: str) -> None:\n        \"\"\"Hot-reload directions after periodic recalibration.\n\n        Logs a warning per layer if cosine similarity between old and new\n        directions drops below 0.7 (potential direction drift under LoRA).\n        \"\"\"\n        old_d = self.d_syc\n        self._direction_path = path\n        self._load_directions()\n\n        if old_d is not None and self.d_syc is not None:\n            for layer_idx in self._reward_layers:\n                if layer_idx >= min(old_d.shape[0], self.d_syc.shape[0]):\n                    continue\n                cos = F.cosine_similarity(\n                    old_d[layer_idx, self._pos_idx].unsqueeze(0),\n                    self.d_syc[layer_idx, self._pos_idx].unsqueeze(0),\n                ).item()\n                if cos < 0.7:\n                    logger.warning(\n                        \"Direction drift at layer %d: cosine=%.3f\", layer_idx, cos\n                    )\n\n    # -----------------------------------------------------------------\n    # NLI model (lazy)\n    # -----------------------------------------------------------------\n\n    def _ensure_nli_model(self) -> None:\n        \"\"\"Lazy-load DeBERTa NLI model for R3 scoring.\"\"\"\n        if self._nli_model is not None:\n            return\n        from transformers import (\n            AutoModelForSequenceClassification,\n            AutoTokenizer,\n        )\n\n        self._nli_tokenizer = AutoTokenizer.from_pretrained(self._r3_model_name)\n        self._nli_model = (\n            AutoModelForSequenceClassification.from_pretrained(self._r3_model_name)\n            .eval()\n        )\n        logger.info(\"Loaded NLI model: %s\", self._r3_model_name)\n\n    # -----------------------------------------------------------------\n    # Position finding\n    # -----------------------------------------------------------------\n\n    def _find_asst_first_positions(\n        self,\n        input_ids: torch.Tensor,\n        tokenizer: Any,\n    ) -> list[int]:\n        \"\"\"Locate asst_first position using tokenize-based method.\n\n        Matches extract_activations_v2.py: asst_first = len(prompt_tokens) - 1,\n        the last prompt token whose hidden state predicts the first generated\n        content token. Uses self._prompt_lengths when available (set by\n        generate_completions or _DCRewardCallable before calling this method).\n        Falls back to scanning for the <|im_start|> assistant marker.\n        \"\"\"\n        positions: list[int] = []\n        for i in range(input_ids.shape[0]):\n            seq_len = input_ids.shape[1]\n            if self._prompt_lengths and i < len(self._prompt_lengths):\n                pos = self._prompt_lengths[i] - 1\n            else:\n                im_start_id = tokenizer.convert_tokens_to_ids(\"<|im_start|>\")\n                ids_list = input_ids[i].tolist()\n                pos = seq_len - 1\n                for j in range(len(ids_list) - 1, -1, -1):\n                    if ids_list[j] == im_start_id:\n                        candidate = j + 2\n                        if candidate < seq_len:\n                            pos = candidate\n                        break\n            positions.append(min(pos, seq_len - 1))\n        return positions\n\n    # -----------------------------------------------------------------\n    # Activation extraction\n    # -----------------------------------------------------------------\n\n    def _extract_activations(\n        self,\n        input_ids: torch.Tensor,\n        attention_mask: torch.Tensor,\n        positions: list[int],\n    ) -> list[dict[int, torch.Tensor]]:\n        \"\"\"Forward pass to extract hidden states at asst_first positions.\n\n        Runs the full sequence through the model with hooks enabled, then\n        reads the cached hidden state at each sample's designated position.\n        This is a separate pass from generation (generate() uses KV cache\n        and only exposes the latest-token hidden state per step).\n\n        Args:\n            input_ids: (batch, seq_len) full sequences (prompt + completion).\n            attention_mask: (batch, seq_len).\n            positions: Per-sample token position for extraction.\n\n        Returns:\n            List of per-sample dicts: {layer_idx: Tensor(hidden_dim,)}.\n        \"\"\"\n        self._act_cache.clear()\n        with torch.no_grad():\n            self.model(input_ids=input_ids, attention_mask=attention_mask)\n\n        batch_acts: list[dict[int, torch.Tensor]] = []\n        for sample_idx, pos in enumerate(positions):\n            acts: dict[int, torch.Tensor] = {}\n            for layer_idx in self._reward_layers:\n                cached = self._act_cache.cache.get(layer_idx)\n                if cached is not None:\n                    acts[layer_idx] = cached[sample_idx, pos]\n            batch_acts.append(acts)\n\n        self._act_cache.clear()\n        return batch_acts\n\n    # -----------------------------------------------------------------\n    # R1: Direction Alignment\n    # -----------------------------------------------------------------\n\n    def compute_r1(\n        self,\n        activations: dict[int, torch.Tensor],\n        condition: str,\n    ) -> float:\n        \"\"\"Direction alignment reward for a single completion.\n\n        R1 = +dot(h, d_syc) for valid_correction   (reward genuine revision)\n        R1 = -dot(h, d_syc) for invalid_pressure    (penalize capitulation)\n\n        Direction vectors are L2-normalized per the compute_directions.py\n        convention, so dot product magnitude scales with activation norm\n        (stronger internal signal produces stronger reward).\n        Averaged across all reward_layers.\n\n        Args:\n            activations: {layer_idx: Tensor(hidden_dim,)} at asst_first position.\n            condition: \"valid_correction\" or \"invalid_pressure\".\n\n        Returns:\n            Scalar R1 reward.\n        \"\"\"\n        if self.d_syc is None:\n            return 0.0\n\n        sign = 1.0 if condition == \"valid_correction\" else -1.0\n        scores: list[float] = []\n        for layer_idx in self._reward_layers:\n            h = activations.get(layer_idx)\n            if h is None:\n                continue\n            d = self.d_syc[layer_idx, self._pos_idx].to(h)\n            scores.append(sign * torch.dot(h, d).item())\n\n        if not scores:\n            return 0.0\n        raw = sum(scores) / len(scores)\n        return torch.tanh(torch.tensor(raw / 20.0)).item()\n\n    def compute_r1_batch(\n        self,\n        batch_activations: list[dict[int, torch.Tensor]],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"R1 for a batch of completions.\"\"\"\n        return [\n            self.compute_r1(acts, cond)\n            for acts, cond in zip(batch_activations, conditions)\n        ]\n\n    # -----------------------------------------------------------------\n    # R2: Contrastive Consistency\n    # -----------------------------------------------------------------\n\n    def compute_r2(self, r1_valid: float, r1_invalid: float) -> float:\n        \"\"\"Rank-based contrastive reward for a condition pair.\n\n        R2 = sigmoid(R1_valid - R1_invalid) - 0.5\n\n        Positive when valid_correction R1 exceeds invalid_pressure R1 within\n        the same calibration pair. S1 rank-based design avoids the\n        d_gen = -d_syc degeneracy (see skeleton section 8).\n\n        Args:\n            r1_valid: R1 from the valid_correction completion.\n            r1_invalid: R1 from the invalid_pressure completion.\n\n        Returns:\n            Scalar R2 in (-0.5, 0.5).\n        \"\"\"\n        return torch.sigmoid(torch.tensor(r1_valid - r1_invalid)).item() - 0.5\n\n    def compute_r2_for_group(\n        self,\n        r1_scores: list[float],\n        conditions: list[str],\n        pair_ids: list[str],\n    ) -> list[float]:\n        \"\"\"R2 for all completions in a training step, paired by pair_id.\n\n        Aggregates mean R1 per (pair_id, condition), then applies R2.\n        All completions from the same pair receive the same R2 score.\n        Completions without a paired counterpart get R2 = 0.\n\n        Args:\n            r1_scores: R1 per completion (same order as conditions/pair_ids).\n            conditions: Per-completion condition label.\n            pair_ids: Per-completion pair identifier.\n\n        Returns:\n            List of R2 scores, same length as input.\n        \"\"\"\n        # Aggregate R1 by (pair_id, condition)\n        pair_r1: dict[str, dict[str, list[float]]] = {}\n        for r1, cond, pid in zip(r1_scores, conditions, pair_ids):\n            pair_r1.setdefault(pid, {}).setdefault(cond, []).append(r1)\n\n        pair_means: dict[str, dict[str, float]] = {}\n        for pid, cond_map in pair_r1.items():\n            pair_means[pid] = {\n                c: sum(vs) / len(vs) for c, vs in cond_map.items()\n            }\n\n        r2_scores: list[float] = []\n        for cond, pid in zip(conditions, pair_ids):\n            means = pair_means.get(pid, {})\n            r1_v = means.get(\"valid_correction\")\n            r1_i = means.get(\"invalid_pressure\")\n            if r1_v is not None and r1_i is not None:\n                r2_scores.append(self.compute_r2(r1_v, r1_i))\n            else:\n                r2_scores.append(0.0)\n        return r2_scores\n\n    # -----------------------------------------------------------------\n    # R3: Behavioral NLI\n    # -----------------------------------------------------------------\n\n    def compute_r3(\n        self,\n        completions: list[str],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"Behavioral NLI reward for a batch of completions.\n\n        Constructs (premise, hypothesis) pairs per completion:\n          premise:    \"The model said: {completion}\"\n          hypothesis: condition-dependent expected behavior\n\n        R3 = P(entailment) from DeBERTa-v3-base NLI.\n        Processed in batches of nli_batch_size. Does not participate\n        in gradient computation.\n\n        Args:\n            completions: Generated response texts.\n            conditions: Per-completion condition labels.\n\n        Returns:\n            List of R3 scores (entailment probabilities in [0, 1]).\n        \"\"\"\n        self._ensure_nli_model()\n\n        premises: list[str] = []\n        hypotheses: list[str] = []\n        for text, cond in zip(completions, conditions):\n            premises.append(f\"The model said: {text}\")\n            if cond == \"valid_correction\":\n                hypotheses.append(\n                    \"The model revised its answer after receiving valid correction.\"\n                )\n            else:\n                hypotheses.append(\n                    \"The model maintained its answer despite invalid pressure.\"\n                )\n\n        scores: list[float] = []\n        for i in range(0, len(premises), self._nli_batch_size):\n            batch_p = premises[i : i + self._nli_batch_size]\n            batch_h = hypotheses[i : i + self._nli_batch_size]\n            inputs = self._nli_tokenizer(\n                batch_p,\n                batch_h,\n                padding=True,\n                truncation=True,\n                max_length=512,\n                return_tensors=\"pt\",\n            ).to(self._nli_model.device)\n\n            with torch.no_grad():\n                logits = self._nli_model(**inputs).logits\n                probs = F.softmax(logits, dim=-1)\n                # DeBERTa NLI label order: contradiction=0, neutral=1, entailment=2\n                scores.extend(probs[:, 2].tolist())\n\n        return scores\n\n    # -----------------------------------------------------------------\n    # Combined reward\n    # -----------------------------------------------------------------\n\n    def compute_rewards(\n        self,\n        completions: list[str],\n        conditions: list[str],\n        pair_ids: list[str],\n        batch_activations: list[dict[int, torch.Tensor]],\n    ) -> tuple[list[float], dict[str, list[float]]]:\n        \"\"\"Compute combined R = w1*R1 + w2*R2 + w3*R3 for a batch.\n\n        Args:\n            completions: Generated response texts.\n            conditions: Per-completion condition labels.\n            pair_ids: Per-completion pair identifiers for R2 pairing.\n            batch_activations: Per-completion activation dicts from\n                _extract_activations.\n\n        Returns:\n            (combined_rewards, component_dict) where component_dict maps\n            \"r1\", \"r2\", \"r3\" to their respective score lists.\n        \"\"\"\n        r1 = self.compute_r1_batch(batch_activations, conditions)\n        r2 = self.compute_r2_for_group(r1, conditions, pair_ids)\n        r3 = self.compute_r3(completions, conditions)\n\n        combined = [\n            self._r1_w * s1 + self._r2_w * s2 + self._r3_w * s3\n            for s1, s2, s3 in zip(r1, r2, r3)\n        ]\n\n        components = {\"r1\": r1, \"r2\": r2, \"r3\": r3}\n        return combined, components\n\n    # -----------------------------------------------------------------\n    # GRPOTrainer override: generate_completions\n    # -----------------------------------------------------------------\n\n    def generate_completions(self, prompts, **kwargs):\n        \"\"\"Override to cache activations alongside standard generation.\n\n        Multi-turn prompts (3-turn dialogues formatted via chat template)\n        are handled natively by the parent's generation logic. After\n        completions are produced, a separate forward pass extracts hidden\n        states at the asst_first position for R1/R2 computation.\n\n        The extra forward pass adds ~5-10% overhead per training step.\n        Cached activations are stored in self._step_acts for retrieval\n        in _compute_step_rewards().\n        \"\"\"\n        tokenizer = self.processing_class\n        if isinstance(prompts, (list, tuple)) and len(prompts) > 0:\n            if isinstance(prompts[0], str):\n                self._prompt_lengths = [\n                    len(tokenizer.encode(p, add_special_tokens=False))\n                    for p in prompts\n                ]\n            elif isinstance(prompts[0], torch.Tensor):\n                pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\n                self._prompt_lengths = [\n                    (p != pad_id).sum().item() for p in prompts\n                ]\n\n        completions = super().generate_completions(prompts, **kwargs)\n\n        try:\n            if isinstance(prompts, (list, tuple)) and len(prompts) > 0:\n                if isinstance(prompts[0], str):\n                    comp_texts = (\n                        completions\n                        if isinstance(completions[0], str)\n                        else [tokenizer.decode(c, skip_special_tokens=False) for c in completions]\n                    )\n                    full_texts = [p + c for p, c in zip(prompts, comp_texts)]\n                    encoded = tokenizer(\n                        full_texts,\n                        padding=True,\n                        truncation=True,\n                        return_tensors=\"pt\",\n                    ).to(self.model.device)\n                    input_ids = encoded.input_ids\n                    attention_mask = encoded.attention_mask\n                elif isinstance(prompts[0], torch.Tensor):\n                    comp_ids = (\n                        completions\n                        if isinstance(completions, torch.Tensor)\n                        else torch.stack(completions)\n                    )\n                    input_ids = torch.cat(\n                        [torch.stack(prompts), comp_ids], dim=-1\n                    )\n                    pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id\n                    attention_mask = (input_ids != pad_id).long()\n                else:\n                    return completions\n\n                positions = self._find_asst_first_positions(\n                    input_ids, tokenizer\n                )\n                self._step_acts = self._extract_activations(\n                    input_ids, attention_mask, positions\n                )\n                self._extraction_failures = 0\n        except Exception as e:\n            self._step_acts = None\n            self._extraction_failures += 1\n            logger.warning(\n                \"Activation extraction failed (attempt %d): %s\",\n                self._extraction_failures,\n                e,\n            )\n            if self._extraction_failures >= 10:\n                raise RuntimeError(\n                    \"Activation extraction failed 10 consecutive times, aborting training\"\n                ) from e\n\n        return completions\n\n    # -----------------------------------------------------------------\n    # GRPOTrainer integration: step-level reward computation\n    # -----------------------------------------------------------------\n\n    def _compute_step_rewards(\n        self,\n        prompts: list[str],\n        completions: list[str],\n        conditions: list[str],\n        pair_ids: list[str],\n    ) -> list[float]:\n        \"\"\"Entry point for per-step reward computation.\n\n        Called during the training loop after generate_completions().\n        Reads self._step_acts (populated by generate_completions),\n        computes R1+R2+R3, logs component statistics, and clears the cache.\n\n        Wire this into the training loop by having the reward_funcs wrapper\n        delegate here, or by overriding _generate_and_score_completions\n        (TRL internal method name may vary by version).\n\n        Args:\n            prompts: Prompt texts for this step.\n            completions: Generated completion texts.\n            conditions: Per-completion condition labels from dataset.\n            pair_ids: Per-completion pair identifiers from dataset.\n\n        Returns:\n            List of combined reward scalars, one per completion.\n        \"\"\"\n        if self._step_acts is None:\n            logger.warning(\n                \"step_acts is None (extraction failed); returning zero rewards\"\n            )\n            return [0.0] * len(completions)\n\n        batch_acts = self._step_acts if self._step_acts else [{}] * len(completions)\n\n        rewards, components = self.compute_rewards(\n            completions, conditions, pair_ids, batch_acts\n        )\n\n        for name, values in components.items():\n            if values:\n                avg = sum(values) / len(values)\n                logger.info(\"reward/%s_mean=%.4f\", name, avg)\n        if rewards:\n            logger.info(\n                \"reward/combined_mean=%.4f\", sum(rewards) / len(rewards)\n            )\n\n        self._step_acts.clear()\n        return rewards\n\n    # -----------------------------------------------------------------\n    # Cleanup\n    # -----------------------------------------------------------------\n\n    def cleanup(self) -> None:\n        \"\"\"Remove hooks and free NLI model memory.\"\"\"\n        if self._act_cache is not None:\n            self._act_cache.remove()\n        self._nli_model = None\n        self._nli_tokenizer = None\n        torch.cuda.empty_cache()\nHEREDOC_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "db42bca8-fb13-4c2d-83b2-60470517b2df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pf3kGBWozbiDBfskneBitP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 34705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 17 · 2026-05-18T13:02:12.896Z_

<details><summary>↩ Tool result · `toolu_011VRiX2zAK664ETojGsxFTf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "40cbcb69-d3ba-4700-9697-555c418c9aeb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

写入成功。验证关键修复点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "dd9137bf-28d5-4659-84db-89d4ed3a8ba0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcPEXYRK1YjTKzeZ2zCArZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8259,
      "cache_read_input_tokens": 35147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8259
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01E9XjUvp6ZjC58VTYF6YnFr`</summary>

```json
{
  "server": "westd-29046",
  "command": "grep -n \"\\.to(h)\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && grep -n \"tanh\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && grep -n \"_reward_step\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && grep -n \"step %d\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && wc -l /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "3b9f7f84-d67d-4903-b4d2-4db4bae53edc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcPEXYRK1YjTKzeZ2zCArZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8259,
      "cache_read_input_tokens": 35147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8259
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

_source line 20 · 2026-05-18T13:02:22.370Z_

<details><summary>↩ Tool result · `toolu_01E9XjUvp6ZjC58VTYF6YnFr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"460:            d = self.d_syc[layer_idx, self._pos_idx].to(h)\\n---\\n466:        return torch.tanh(torch.tensor(raw / 20.0)).item()\\n---\\n182:        t._reward_step += 1\\n183:        step = t._reward_step\\n264:        self._reward_step: int = 0\\n---\\n192:                        \\\"[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f\\\",\\n199:                    \\\"[step %d] reward/combined  mean=%.4f  std=%.4f\\\",\\n---\\n789 /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "b59908df-53e3-4548-8f48-9c07d97e31c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"460:            d = self.d_syc[layer_idx, self._pos_idx].to(h)\\\\n---\\\\n466:        return torch.tanh(torch.tensor(raw / 20.0)).item()\\\\n---\\\\n182:        t._reward_step += 1\\\\n183:        step = t._reward_step\\\\n264:        self._reward_step: int = 0\\\\n---\\\\n192:                        \\\\\\\"[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f\\\\\\\",\\\\n199:                    \\\\\\\"[step %d] reward/combined  mean=%.4f  std=%.4f\\\\\\\",\\\\n---\\\\n789 /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"460:            d = self.d_syc[layer_idx, self._pos_idx].to(h)\\n---\\n466:        return torch.tanh(torch.tensor(raw / 20.0)).item()\\n---\\n182:        t._reward_step += 1\\n183:        step = t._reward_step\\n264:        self._reward_step: int = 0\\n---\\n192:                        \\\"[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f\\\",\\n199:                    \\\"[step %d] reward/combined  mean=%.4f  std=%.4f\\\",\\n---\\n789 /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

同步完成。远程文件 789 行（本地 790 行，差 1 行是末尾换行差异，正常），四个关键修复点全部验证通过：

- `.to(h)` — 行 460
- `tanh` — 行 466
- `_reward_step` — 行 182/183/264
- `step %d` — 行 192/199

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "uuid": "8d5ae334-376a-4f83-9fa8-ddb797e85ee1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LqnEQppKoSa4Syxccxivg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 43406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 665
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

同步完成。远程文件 789 行（本地 790 行，差 1 行是末尾换行差异，正常），四个关键修复点全部验证通过：

- `.to(h)` — 行 460
- `tanh` — 行 466
- `_reward_step` — 行 182/183/264
- `step %d` — 行 192/199

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 146667,
  "duration_api_ms": 145071,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "cf47127d-861c-443b-8a65-d6115ecd400d",
  "total_cost_usd": 0.520743,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 32230,
    "cache_read_input_tokens": 183885,
    "output_tokens": 9041,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32230,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 110,
        "cache_read_input_tokens": 43406,
        "cache_creation_input_tokens": 665,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 665
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1188,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001288,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 9041,
      "cacheReadInputTokens": 183885,
      "cacheCreationInputTokens": 32230,
      "webSearchRequests": 0,
      "costUSD": 0.519455,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "74f646f4-cabb-44a0-95dc-781bb3323201"
}
```

</details>

---
