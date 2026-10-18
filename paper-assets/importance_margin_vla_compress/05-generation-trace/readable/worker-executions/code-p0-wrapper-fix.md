# code p0 wrapper fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_code_p0_wrapper_fix_20260515T120324.log`
- **Structured JSON:** [`0f774d03fb16e0aee63e.json`](../../sessions/0f/0f774d03fb16e0aee63e.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts",
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
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
  "uuid": "495073cc-2f59-4c57-ad24-14383c2647b2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress-artifacts/memory/"
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
    "resetsAt": 1778863800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2c2e7291-adca-432d-8740-0031c81010d1",
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c"
}
```

---

### Assistant

_source line 4_

I'll start by reading the architecture report and the current source files to understand the codebase, then clone lerobot to study the real API.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "fa9033d5-be79-4703-9d9f-64867dcdc420",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhJ2P93aZLr7DrkXDoNU7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12715,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12715
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

<details open><summary>🔧 Tool call — Read · `toolu_019TCjMByHnM7nreN5HmbsJF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/architecture_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "80775d78-c59b-452d-8285-5386caffeae4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhJ2P93aZLr7DrkXDoNU7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12715,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12715
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

_source line 6 · 2026-05-15T12:03:36.848Z_

<details><summary>↩ Tool result · `toolu_019TCjMByHnM7nreN5HmbsJF`</summary>

````text
1	# SmolVLA Architecture & ACIS Integration Report
2	
3	## 1. SmolVLA Architecture Overview
4	
5	### 1.1 Visual Encoder
6	
7	**Encoder**: SigLIP vision transformer (`smolvlm_vision`)
8	
9	| Parameter | Value |
10	|-----------|-------|
11	| hidden_size | 768 |
12	| image_size | 512 |
13	| patch_size | 16 |
14	| num_attention_heads | 12 |
15	| Patches per image | (512/16)² = **1024** |
16	
17	**Raw output shape**: `(B, 1024, 768)`
18	
19	**Pixel Shuffle + Projection** (`SmolVLMConnector`):
20	- `scale_factor = 4` → sequence reduction 16x: 1024 → **64 tokens**
21	- Channel increase 16x: 768 → 768×16 = 12288
22	- `SmolVLMSimpleMLP`: `nn.Linear(12288, 960, bias=False)`
23	
24	**Final visual token shape per image**: `(B, 64, 960)`
25	
26	```python
27	# transformers/models/smolvlm/modeling_smolvlm.py
28	class SmolVLMSimpleMLP(nn.Module):
29	    def __init__(self, config):
30	        input_size = config.vision_config.hidden_size * (config.scale_factor**2)  # 12288
31	        output_size = config.text_config.hidden_size  # 960
32	        self.proj = nn.Linear(input_size, output_size, bias=False)
33	
34	class SmolVLMConnector(nn.Module):
35	    def __init__(self, config):
36	        self.scale_factor = config.scale_factor  # 4
37	        self.modality_projection = SmolVLMSimpleMLP(config)
38	
39	    def pixel_shuffle(self, x, scale_factor=2):
40	        bsz, seq, embed_dim = x.size()
41	        height = width = int(seq**0.5)  # 32
42	        # Rearrange spatial → channels, reducing seq by scale_factor²
43	        ...
44	        return x  # (B, 64, 12288)
45	
46	    def forward(self, image_hidden_states):
47	        image_hidden_states = self.pixel_shuffle(image_hidden_states, self.scale_factor)
48	        image_hidden_states = self.modality_projection(image_hidden_states)
49	        return image_hidden_states  # (B, 64, 960)
50	```
51	
52	**Multi-camera input**: Multiple camera views supported. Each image wrapped with special tokens (`fake_image_token`, `global_image_token`). LIBERO uses 2 cameras (agentview + wrist).
53	
54	```python
55	# SmolVLMWithExpertModel
56	def embed_image(self, image: torch.Tensor):
57	    image_hidden_states = self.get_vlm_model().vision_model(
58	        pixel_values=image.to(dtype=self.get_vlm_model().vision_model.dtype),
59	        patch_attention_mask=None,
60	    ).last_hidden_state                                    # (B, 1024, 768)
61	    image_hidden_states = self.get_vlm_model().connector(image_hidden_states)
62	    return image_hidden_states                             # (B, 64, 960)
63	```
64	
65	### 1.2 Language Model / Backbone
66	
67	**LLM**: SmolLM2 (Llama-architecture variant, `VLlama3ForCausalLM`)
68	
69	| Parameter | Value |
70	|-----------|-------|
71	| hidden_size | **960** |
72	| num_hidden_layers | 32 (full); SmolVLA uses **16** (`num_vlm_layers`) |
73	| num_attention_heads | 15 |
74	| num_key_value_heads | 5 (GQA) |
75	| head_dim | 64 |
76	| intermediate_size | 2560 |
77	| max_position_embeddings | 8192 |
78	| rope_theta | 100000 |
79	
80	**Input embedding dimension**: **960**
81	
82	**Prefix construction** (in `embed_prefix()`):
83	```
84	[img_start_tokens] + [64 visual tokens] + [img_end_token]   × num_cameras
85	+ [language tokens]  (tokenizer_max_length=48)
86	+ [state token]      (nn.Linear(32, 960) from proprioceptive state)
87	```
88	
89	All embeddings scaled by `√960` before concatenation. Attention: bidirectional for image+language tokens, causal for state token.
90	
91	### 1.3 Action Head (Expert)
92	
93	**Architecture**: Flow-Matching Transformer with interleaved cross-attention and self-attention.
94	
95	**Class**: `SmolVLMWithExpertModel.lm_expert` — separate Llama-architecture transformer
96	
97	| Parameter | Value |
98	|-----------|-------|
99	| expert_hidden_size | int(960 × 0.75) = **720** |
100	| intermediate_size | **1792** |
101	| num_expert_layers | **16** (same as num_vlm_layers) |
102	| self_attn_every_n_layers | 2 |
103	
104	**Layer interleaving pattern**:
105	- Even layers (0, 2, 4, ...): **self-attention** (prefix + suffix tokens concatenated)
106	- Odd layers (1, 3, 5, ...): **cross-attention** (expert Q attends to VLM K,V)
107	
108	Cross-attention K,V project from VLM dim (320 = 5×64) to expert dim:
109	```python
110	self.lm_expert.layers[layer_idx].self_attn.k_proj = nn.Linear(320, ..., bias=False)
111	self.lm_expert.layers[layer_idx].self_attn.v_proj = nn.Linear(320, ..., bias=False)
112	```
113	
114	**Action embedding** (in `embed_suffix()`):
115	```python
116	self.action_in_proj  = nn.Linear(32, 720)    # noisy actions → expert dim
117	self.action_out_proj = nn.Linear(720, 32)    # expert output → action dim
118	self.action_time_mlp_in  = nn.Linear(1440, 720)  # concat(action_emb, time_emb) → expert dim
119	self.action_time_mlp_out = nn.Linear(720, 720)
120	
121	# Forward:
122	action_emb = self.action_in_proj(noisy_actions)            # (B, 50, 720)
123	time_emb = sinusoidal(timestep, dim=720)                   # (B, 1, 720) → expand to (B, 50, 720)
124	action_time_emb = cat([action_emb, time_emb], dim=2)       # (B, 50, 1440)
125	action_time_emb = silu(self.action_time_mlp_in(action_time_emb))  # (B, 50, 720)
126	action_time_emb = self.action_time_mlp_out(action_time_emb)       # (B, 50, 720)
127	```
128	
129	**Output**: Continuous, `chunk_size=50` steps, `max_action_dim=32` (padded; LIBERO actual: 7D = 6D EEF delta + 1D gripper).
130	
131	## 2. Forward Pass Data Flow
132	
133	### 2.1 Training (`VLAFlowMatching.forward`)
134	
135	```
136	Input: images, lang_tokens, state, actions
137	
138	1. Sample noise ~ N(0,1),  shape (B, 50, 32)
139	2. Sample time ~ Beta(1.5, 1.0) * 0.999 + 0.001
140	3. x_t = time * noise + (1 - time) * actions        # noisy interpolation
141	4. u_t = noise - actions                             # target velocity field
142	
143	5. embed_prefix(images, lang_tokens, state):
144	   a. vision_model(images) → (B, 1024, 768)         # SigLIP
145	   b. connector(·) → (B, 64, 960)                   # pixel shuffle + projection
146	   c. Concat: [img_special + 64_vis + img_end] × cameras + lang_emb + state_emb
147	   → prefix_embs: (B, prefix_len, 960)
148	
149	6. embed_suffix(x_t, time):
150	   a. action_in_proj(x_t) → (B, 50, 720)
151	   b. sinusoidal time embedding → (B, 50, 720)
152	   c. MLP(cat(action, time)) → (B, 50, 720)
153	   → suffix_embs: (B, 50, 720)
154	
155	7. Construct 2D attention mask + position_ids
156	
157	8. vlm_with_expert.forward([prefix_embs, suffix_embs]):
158	   For each layer i in 0..15:
159	     if i % 2 == 0:  # self-attention
160	       concat(prefix, suffix) → joint self-attention → split back
161	     else:            # cross-attention
162	       VLM processes prefix → KV
163	       Expert Q attends to VLM KV
164	   → (prefix_out, suffix_out)
165	
166	9. suffix_out = suffix_out[:, -50:]                  # last chunk_size tokens
167	10. v_t = action_out_proj(suffix_out)                # (B, 50, 32)
168	11. loss = F.mse_loss(u_t, v_t, reduction="none")    # masked by actions_is_pad
169	```
170	
171	### 2.2 Inference (`VLAFlowMatching.sample_actions`)
172	
173	```
174	1. Encode prefix once → cache KV
175	2. x_t = noise ~ N(0,1)
176	3. For step in range(num_steps=10):
177	     time = 1.0 - step/10
178	     v_t = denoise_step(x_t, time, cached_KV)
179	     x_t = x_t + (-1/10) * v_t       # Euler integration
180	4. Return x_t as predicted actions
181	```
182	
183	KV-caching: prefix encoded once, denoising steps only process suffix with cross-attention to cached prefix KV.
184	
185	## 3. Key Classes and File Paths
186	
187	### LeRobot repo (`huggingface/lerobot`)
188	
189	| Class | File |
190	|-------|------|
191	| `SmolVLAPolicy` | `lerobot/policies/smolvla/modeling_smolvla.py` |
192	| `SmolVLAConfig` | `lerobot/policies/smolvla/configuration_smolvla.py` |
193	| `VLAFlowMatching` | `lerobot/policies/smolvla/modeling_smolvla.py` |
194	| `SmolVLMWithExpertModel` | `lerobot/policies/smolvla/smolvlm_with_expert.py` |
195	
196	### Transformers repo (`huggingface/transformers`)
197	
198	| Class | File |
199	|-------|------|
200	| `SmolVLMForConditionalGeneration` | `transformers/models/smolvlm/modeling_smolvlm.py` |
201	| `SmolVLMConnector` | `transformers/models/smolvlm/modeling_smolvlm.py` |
202	| `SmolVLMSimpleMLP` | `transformers/models/smolvlm/modeling_smolvlm.py` |
203	| `SmolVLMVisionTransformer` (SigLIP) | `transformers/models/smolvlm/modeling_smolvlm.py` |
204	
205	### Training
206	
207	| Item | Detail |
208	|------|--------|
209	| Entry point | `lerobot/scripts/lerobot_train.py` → `train(cfg: TrainPipelineConfig)` |
210	| CLI | `lerobot-train` |
211	| Loss | MSE: `F.mse_loss(u_t, v_t)` where u_t = noise - actions |
212	| Time sampling | Beta(α=1.5, β=1.0) scaled to [0.001, 1.0] |
213	| Optimizer | AdamW, lr=1e-4, betas=(0.9, 0.95), weight_decay=1e-10 |
214	| Scheduler | Cosine decay, warmup=1000, decay_steps=30000, decay_lr=2.5e-6 |
215	| Grad clip | 10.0 |
216	
217	## 4. LoRA Configuration
218	
219	Default targets (`_get_default_peft_targets`):
220	```python
221	target_modules = r"(model\.vlm_with_expert\.lm_expert\..*\.(q|v)_proj|model\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))"
222	```
223	
224	Targets:
225	- All **Q and V projections** in the expert transformer
226	- **state_proj**, **action_in_proj**, **action_out_proj**, **action_time_mlp_in**, **action_time_mlp_out**
227	
228	Default training mode: `train_expert_only=True`, `freeze_vision_encoder=True`, `train_state_proj=True`. VLM backbone frozen.
229	
230	## 5. LIBERO Dataset
231	
232	**HuggingFace repo**: `HuggingFaceVLA/libero`
233	
234	| Field | Shape / Type |
235	|-------|-------------|
236	| `observation.state` | 8D (EEF pos 3D + axis-angle 3D + gripper qpos 2D) |
237	| `observation.images.image` | agentview camera, HWC uint8 |
238	| `observation.images.image2` | wrist camera, HWC uint8 |
239	| actions | 7D (6D EEF delta + 1D gripper), padded to 32D internally |
240	| action range | Box(-1, 1, shape=(7,)) |
241	
242	**Data format**: LeRobotDataset v3.0 — chunked Parquet (tabular) + MP4 (video frames).
243	
244	**Loading**: `make_dataset(cfg)` creates `LeRobotDataset` from Hub repo_id.
245	
246	**Training command**:
247	```bash
248	lerobot-train \
249	  --policy.type=smolvla \
250	  --policy.load_vlm_weights=true \
251	  --dataset.repo_id=HuggingFaceVLA/libero \
252	  --env.type=libero \
253	  --env.task=libero_10 \
254	  --steps=100000 \
255	  --batch_size=4
256	```
257	
258	## 6. ACIS Insertion Point Analysis
259	
260	### 6.1 Existing Compression
261	
262	SmolVLA already has:
263	- **Pixel shuffle**: 1024 → 64 tokens (16x spatial reduction)
264	- **VLM layer skipping**: uses 16 of 32 layers
265	
266	No dynamic token pruning exists in the codebase.
267	
268	### 6.2 ACIS Cross-Attention Module: `s_i = CrossAttn(a_query, v_i)`
269	
270	#### Where to get `v_i` (visual tokens)
271	
272	**Option A — Post-connector (recommended)**:
273	- Location: output of `SmolVLMConnector.forward()` in `embed_image()`
274	- Shape: `(B, 64, 960)` per camera
275	- Advantage: already in LLM embedding space (dim=960), semantically rich after SigLIP + projection
276	- These are the tokens that enter the prefix embeddings
277	
278	**Option B — Post-VLM-encoding**:
279	- Location: after VLM prefix forward pass (the cached KV states)
280	- Shape: `(B, prefix_len, num_kv_heads, head_dim)` per layer
281	- Advantage: contextualized by language tokens via self-attention
282	- Disadvantage: entangled with non-visual tokens, need to extract visual positions
283	
284	**Recommendation: Option A** — cleaner, shape is known, tokens are identifiable.
285	
286	#### Where to get `a_query` (action conditioning)
287	
288	**Option A — From `embed_suffix()` output (recommended)**:
289	- Location: after `action_time_mlp_out` in `embed_suffix()`
290	- Shape: `(B, chunk_size, 720)` — need projection to match v_i dim
291	- Contains action + time information, semantically represents "what action is being predicted"
292	- Available before the expert transformer processes it
293	
294	**Option B — From expert intermediate layer**:
295	- Location: output of an early expert layer (e.g., layer 2 or 4)
296	- Shape: `(B, chunk_size, 720)`
297	- Advantage: richer representation after some self/cross-attention
298	- Disadvantage: creates a circular dependency (expert output depends on prefix, but ACIS modifies prefix based on expert)
299	
300	**Option C — Learnable query (simplest)**:
301	- `a_query = nn.Parameter(torch.randn(1, num_queries, 960))`
302	- No dependency on actual actions during forward pass
303	- Trained end-to-end to predict importance
304	
305	**Recommendation: Option A** for training (action-conditioned), **Option C** as simpler baseline.
306	
307	#### Insertion Point in Code
308	
309	```python
310	# In SmolVLMWithExpertModel or VLAFlowMatching
311	
312	# STEP 1: Get visual tokens (before prefix assembly)
313	vis_tokens = self.embed_image(images)          # (B, 64, 960) per camera
314	# → all cameras: (B, num_cameras * 64, 960)
315	
316	# STEP 2: Get action query
317	suffix_embs = self.embed_suffix(x_t, time)     # (B, 50, 720)
318	a_query = self.acis_query_proj(suffix_embs)     # (B, 50, 960) or pool to (B, 1, 960)
319	
320	# STEP 3: ACIS cross-attention
321	# s_i = CrossAttn(a_query, v_i)
322	importance_scores = self.acis_module(
323	    query=a_query,                              # (B, Q, 960)
324	    key=vis_tokens,                             # (B, N_vis, 960)
325	    value=vis_tokens                            # (B, N_vis, 960)
326	)                                               # → (B, N_vis) scores
327	
328	# STEP 4: Soft top-k selection
329	soft_mask = differentiable_topk(importance_scores, k=k)  # (B, N_vis)
330	
331	# STEP 5: Apply mask to visual tokens
332	vis_tokens_pruned = vis_tokens * soft_mask.unsqueeze(-1)  # soft weighting
333	# OR: select top-k indices for hard pruning
334	
335	# STEP 6: Continue with prefix assembly using pruned tokens
336	prefix_embs = self.embed_prefix_with_pruned_vis(vis_tokens_pruned, lang, state)
337	```
338	
339	#### Specific Code Modifications
340	
341	**File**: `lerobot/policies/smolvla/smolvlm_with_expert.py`
342	
343	1. Add ACIS module to `SmolVLMWithExpertModel.__init__()`:
344	```python
345	self.acis_query_proj = nn.Linear(720, 960)  # expert dim → VLM dim
346	self.acis_cross_attn = nn.MultiheadAttention(
347	    embed_dim=960, num_heads=8, kdim=960, vdim=960, batch_first=True
348	)
349	self.acis_score_head = nn.Linear(960, 1)  # output per-token score
350	```
351	
352	2. Modify forward flow in `VLAFlowMatching.forward()` (in `modeling_smolvla.py`):
353	   - After `embed_image()` and `embed_suffix()`, compute ACIS scores
354	   - Apply soft top-k mask
355	   - Rebuild prefix with masked visual tokens
356	
357	3. Add ACIS modules to LoRA target regex:
358	```python
359	target_modules = r"(...|model\.acis_.*)"
360	```
361	
362	### 6.3 Forward Pass Modification Summary
363	
364	```
365	Original:  images → SigLIP → connector → embed_prefix → VLM+Expert → loss
366	Modified:  images → SigLIP → connector → [ACIS scoring → soft top-k] → embed_prefix → VLM+Expert → loss + IMM_loss
367	                                              ↑
368	                                     action query from embed_suffix()
369	```
370	
371	### 6.4 IMM Loss Integration
372	
373	The IMM loss adds to the existing flow matching MSE loss:
374	
375	```python
376	# Original loss
377	loss_fm = F.mse_loss(u_t, v_t, reduction="none")  # flow matching
378	
379	# IMM auxiliary losses (computed from ACIS scores)
380	loss_margin = margin_loss(importance_scores, kept_mask, pruned_mask, margin=δ)
381	loss_calibration = calibration_loss(importance_scores, reconstruction_error)
382	
383	# Total
384	loss = loss_fm + λ_margin * loss_margin + λ_cal * loss_calibration
385	```
386	
387	## 7. Differentiable Soft Top-K: Method Comparison
388	
389	### 7.1 Methods Surveyed
390	
391	#### Sigmoid + Implicit Differentiation (Thomas Ahle)
392	
393	Binary-search for shift `t` such that `Σ σ(x_i + t) = k`, return `σ(x_i + t)`. Backward via implicit differentiation: `J = diag(v) - vv^T/‖v‖₁`.
394	
395	- **Impl**: [gist, 20 lines](https://gist.github.com/thomasahle/4c1e85e5842d01b007a8d10f5fed3a18), zero deps
396	- **Gradient**: Exact Jacobian, deterministic, zero variance
397	- **Complexity**: O(n × B) forward (B≈64 binary search steps), O(n) backward
398	- **Constraint**: Σp_i = k **exactly** satisfied
399	- **Issues**: Binary search not maximally GPU-efficient; elements near threshold get soft (ambiguous) values
400	
401	#### DFTopK (arXiv Oct 2025)
402	
403	Sigmoid on scores shifted by midpoint of k-th and (k+1)-th largest: `σ((x - (x[k]+x[k+1])/2) / τ)`.
404	
405	- **Impl**: [github.com/zhangzhen97/DFTOPK](https://github.com/zhangzhen97/DFTOPK)
406	- **Gradient**: Deterministic, localized uncertainty at boundary
407	- **Complexity**: O(n) average (Introselect)
408	- **Constraint**: Σp_i ≈ k (approximate)
409	- **Issues**: τ requires tuning
410	
411	#### LapSum (ICML 2025)
412	
413	Differentiable top-k via CDF of sum of Laplace distributions. Threshold `b` found such that `Σ Lap_α(b - r_i) = w`.
414	
415	- **Impl**: [github.com/gmum/LapSum](https://github.com/gmum/LapSum), `pip install lapsum`
416	- **Gradient**: Exact, deterministic, zero variance
417	- **Complexity**: O(n log n), O(n) backward
418	- **Constraint**: Exact
419	- **Issues**: α hyperparameter; requires library
420	
421	#### Gumbel Top-k (Subset Sampling)
422	
423	Iterative Gumbel-perturbed softmax k times with masking. Used in **LightVLA**.
424	
425	- **Impl**: ~20 lines; UvA DL Notebooks `SubsetOperator`
426	- **Gradient**: Stochastic (Gumbel noise), reparameterizable, STE for hard mode
427	- **Complexity**: O(n × k) — k sequential softmax ops
428	- **Constraint**: Exact k elements (hard mode)
429	- **Issues**: k=150 means 150 sequential ops; variance from noise
430	
431	#### SOFT (Optimal Transport, NeurIPS 2020)
432	
433	Top-k as Entropic OT via Sinkhorn iterations.
434	
435	- **Impl**: ~120 lines gist, no pip package
436	- **Gradient**: Biased (controlled by ε)
437	- **Complexity**: O(n × k × T), T=50-200 Sinkhorn iterations
438	- **Constraint**: Exact (doubly stochastic)
439	- **Issues**: NaN instability for small ε; slow
440	
441	#### NeuralSort / SoftSort
442	
443	Full n×n permutation matrix relaxation. O(n²) time and memory.
444	
445	- **Issues**: Produces full permutation matrix — overkill for top-k; n=500 → 250K entries
446	
447	#### Temperature Sigmoid (baseline)
448	
449	`σ(α · (s_i - kth_percentile) / τ)` with τ annealing.
450	
451	- **Impl**: 5 lines, zero deps
452	- **Gradient**: Biased; no gradient through `kthvalue`
453	- **Complexity**: O(n log n) or O(n) with `torch.kthvalue`
454	- **Issues**: Σp_i ≠ k; gradient vanishing at low τ
455	
456	### 7.2 Comparison Table
457	
458	| Method | Complexity | Gradient | Exact Σ=k | Variance | Code | VLA Proven |
459	|--------|-----------|----------|-----------|----------|------|------------|
460	| **Sigmoid+ImplDiff** | O(n) | Exact | **Yes** | Zero | 20 lines | No |
461	| **DFTopK** | O(n) | Deterministic | Approx | Zero | ~50 lines | No |
462	| **LapSum** | O(n log n) | Exact | **Yes** | Zero | Library | No |
463	| **Gumbel Top-k** | O(n·k) | STE | Yes (hard) | High | 20 lines | **Yes** |
464	| **SOFT (OT)** | O(n·k·T) | Biased | Yes | Zero | 120 lines | No |
465	| **NeuralSort** | O(n²) | Biased | N/A | Zero | Library | No |
466	| **SoftSort** | O(n²) | Biased | N/A | Zero | 3 lines | No |
467	| **Temp Sigmoid** | O(n) | Biased | No | Zero | 5 lines | Indirect |
468	
469	### 7.3 Recommendation
470	
471	**Primary: Sigmoid + Implicit Differentiation**
472	
473	- 20 lines of PyTorch, zero dependencies, passes `torch.autograd.gradcheck`
474	- Exact Jacobian, zero variance — critical for stable LoRA fine-tuning
475	- Exactly satisfies Σp_i = k
476	- O(n) backward; forward binary search negligible vs VLA forward pass
477	- Soft probabilities usable as token weights; binarize with STE at inference
478	
479	```python
480	# Reference implementation (Thomas Ahle)
481	# https://gist.github.com/thomasahle/4c1e85e5842d01b007a8d10f5fed3a18
482	
483	class TopK(torch.autograd.Function):
484	    @staticmethod
485	    def forward(ctx, x, k):
486	        # Binary search for threshold t such that sum(sigmoid(x + t)) = k
487	        lo, hi = -1000.0, 1000.0
488	        for _ in range(64):
489	            mid = (lo + hi) / 2
490	            if torch.sigmoid(x + mid).sum(-1).item() < k:
491	                lo = mid
492	            else:
493	                hi = mid
494	        t = (lo + hi) / 2
495	        p = torch.sigmoid(x + t)
496	        ctx.save_for_backward(p)
497	        return p
498	
499	    @staticmethod
500	    def backward(ctx, grad_output):
501	        p, = ctx.saved_tensors
502	        v = p * (1 - p)  # sigmoid derivative
503	        # Implicit differentiation of constraint sum(p) = k
504	        grad = v * (grad_output - (v * grad_output).sum(-1, keepdim=True) / v.sum(-1, keepdim=True))
505	        return grad, None
506	```
507	
508	**Secondary: DFTopK** — for citation in paper (published method), O(n) complexity, similar sigmoid approach but uses `torch.kthvalue`.
509	
510	**Fallback: Gumbel Top-k** — if stochastic gradients prove beneficial for exploration during LoRA training. Proven in LightVLA.
511	
512	### 7.4 Key Related Work
513	
514	- **LightVLA** (arXiv:2509.12594): Gumbel-softmax VLA token pruning, LoRA rank 32, 59% FLOP reduction, 2.9% task success improvement
515	- **AutoSelect** (arXiv:2603.07135): Soft top-k + variance-preserving noise gating for LLaVA, 0.69ms overhead, 96.5% accuracy retention at 88.9% pruning
516	- **DiffRate** (ICCV 2023): Differentiable compression rate for ViT ([github.com/OpenGVLab/DiffRate](https://github.com/OpenGVLab/DiffRate))
517	
518	## 8. Token Compression Integration: FastV-Style Pruning
519	
520	### 8.1 How It Maps to SmolVLA
521	
522	FastV prunes visual tokens at an intermediate LLM layer based on attention from text tokens. In SmolVLA:
523	
524	**Option 1 — Prune before VLM+Expert forward (ACIS approach)**:
525	- After `embed_image()` returns `(B, 64, 960)`, score with ACIS, mask/select, then build prefix
526	- Pros: clean, modular, no VLM modification
527	- Cons: scores computed without LLM context
528	
529	**Option 2 — Prune in VLM KV cache (inference optimization)**:
530	- After prefix encoding, prune KV entries for low-importance visual tokens
531	- Modify `past_key_values[layer]["key_states"]` and `["value_states"]`
532	- Shape: `(B, prefix_len, num_kv_heads, head_dim)` → remove rows for pruned visual positions
533	- Pros: reduces computation in all subsequent denoising steps
534	- Cons: requires tracking visual token positions within prefix
535	
536	**Option 3 — Mid-layer pruning (FastV-faithful)**:
537	- In `SmolVLMWithExpertModel.forward()`, after layer N, compute attention scores from state/language tokens to visual tokens, prune, continue
538	- Requires modifying the layer-by-layer loop
539	
540	**Recommendation**: Option 1 (ACIS before prefix) for training. At inference, additionally apply Option 2 (KV cache pruning) for efficiency.
541	
542	### 8.2 Visual Token Position Tracking
543	
544	Prefix layout for LIBERO (2 cameras):
545	```
546	[img_start(2)] [vis_0..63(64)] [img_end(1)]  → camera 1: tokens 0..66
547	[img_start(2)] [vis_0..63(64)] [img_end(1)]  → camera 2: tokens 67..133
548	[lang_tokens(48)]                              → tokens 134..181
549	[state_token(1)]                               → token 182
550	```
551	
552	Visual token indices: `[2:66]` and `[69:133]` (64 tokens each, offset by special tokens).
553	
554	## 9. Summary: ACIS Integration Blueprint
555	
556	```
557	┌─────────┐     ┌──────────┐     ┌───────────────┐
558	│  Images  │────→│  SigLIP  │────→│  Connector    │──→ vis_tokens (B, 64×C, 960)
559	└─────────┘     └──────────┘     │  (PixelShuffle│
560	                                  │   + MLP)      │
561	                                  └───────────────┘
562	                                          │
563	                                          ▼
564	┌─────────────┐                 ┌─────────────────┐
565	│ embed_suffix │──a_query──────→│  ACIS Module    │
566	│ (noisy act + │  (B,Q,960)     │  CrossAttn +    │──→ importance_scores (B, N_vis)
567	│  time emb)   │                │  Score Head     │
568	└─────────────┘                 └─────────────────┘
569	                                          │
570	                                          ▼
571	                                ┌─────────────────┐
572	                                │  Soft Top-K     │──→ soft_mask (B, N_vis)
573	                                │  (Sigmoid+Impl) │
574	                                └─────────────────┘
575	                                          │
576	                                          ▼
577	                                ┌─────────────────┐
578	                                │  Apply Mask     │──→ pruned_vis (B, K, 960)
579	                                └─────────────────┘
580	                                          │
581	                                          ▼
582	                                ┌─────────────────┐
583	                                │  embed_prefix   │──→ prefix_embs (B, prefix_len', 960)
584	                                │  (+ lang + state│
585	                                └─────────────────┘
586	                                          │
587	                                          ▼
588	                                ┌─────────────────┐
589	                                │  VLM + Expert   │──→ v_t (B, 50, 32)
590	                                │  (16 layers)    │
591	                                └─────────────────┘
592	                                          │
593	                                          ▼
594	                                ┌─────────────────┐
595	                                │  Loss:          │
596	                                │  MSE(u_t, v_t)  │
597	                                │  + λ·L_margin   │
598	                                │  + λ·L_calibr   │
599	                                └─────────────────┘
600	```
601	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "dcfdd895-c70f-4215-8426-f7a61bf7e6b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/architecture_report.md",
      "content": "# SmolVLA Architecture & ACIS Integration Report\n\n## 1. SmolVLA Architecture Overview\n\n### 1.1 Visual Encoder\n\n**Encoder**: SigLIP vision transformer (`smolvlm_vision`)\n\n| Parameter | Value |\n|-----------|-------|\n| hidden_size | 768 |\n| image_size | 512 |\n| patch_size | 16 |\n| num_attention_heads | 12 |\n| Patches per image | (512/16)² = **1024** |\n\n**Raw output shape**: `(B, 1024, 768)`\n\n**Pixel Shuffle + Projection** (`SmolVLMConnector`):\n- `scale_factor = 4` → sequence reduction 16x: 1024 → **64 tokens**\n- Channel increase 16x: 768 → 768×16 = 12288\n- `SmolVLMSimpleMLP`: `nn.Linear(12288, 960, bias=False)`\n\n**Final visual token shape per image**: `(B, 64, 960)`\n\n```python\n# transformers/models/smolvlm/modeling_smolvlm.py\nclass SmolVLMSimpleMLP(nn.Module):\n    def __init__(self, config):\n        input_size = config.vision_config.hidden_size * (config.scale_factor**2)  # 12288\n        output_size = config.text_config.hidden_size  # 960\n        self.proj = nn.Linear(input_size, output_size, bias=False)\n\nclass SmolVLMConnector(nn.Module):\n    def __init__(self, config):\n        self.scale_factor = config.scale_factor  # 4\n        self.modality_projection = SmolVLMSimpleMLP(config)\n\n    def pixel_shuffle(self, x, scale_factor=2):\n        bsz, seq, embed_dim = x.size()\n        height = width = int(seq**0.5)  # 32\n        # Rearrange spatial → channels, reducing seq by scale_factor²\n        ...\n        return x  # (B, 64, 12288)\n\n    def forward(self, image_hidden_states):\n        image_hidden_states = self.pixel_shuffle(image_hidden_states, self.scale_factor)\n        image_hidden_states = self.modality_projection(image_hidden_states)\n        return image_hidden_states  # (B, 64, 960)\n```\n\n**Multi-camera input**: Multiple camera views supported. Each image wrapped with special tokens (`fake_image_token`, `global_image_token`). LIBERO uses 2 cameras (agentview + wrist).\n\n```python\n# SmolVLMWithExpertModel\ndef embed_image(self, image: torch.Tensor):\n    image_hidden_states = self.get_vlm_model().vision_model(\n        pixel_values=image.to(dtype=self.get_vlm_model().vision_model.dtype),\n        patch_attention_mask=None,\n    ).last_hidden_state                                    # (B, 1024, 768)\n    image_hidden_states = self.get_vlm_model().connector(image_hidden_states)\n    return image_hidden_states                             # (B, 64, 960)\n```\n\n### 1.2 Language Model / Backbone\n\n**LLM**: SmolLM2 (Llama-architecture variant, `VLlama3ForCausalLM`)\n\n| Parameter | Value |\n|-----------|-------|\n| hidden_size | **960** |\n| num_hidden_layers | 32 (full); SmolVLA uses **16** (`num_vlm_layers`) |\n| num_attention_heads | 15 |\n| num_key_value_heads | 5 (GQA) |\n| head_dim | 64 |\n| intermediate_size | 2560 |\n| max_position_embeddings | 8192 |\n| rope_theta | 100000 |\n\n**Input embedding dimension**: **960**\n\n**Prefix construction** (in `embed_prefix()`):\n```\n[img_start_tokens] + [64 visual tokens] + [img_end_token]   × num_cameras\n+ [language tokens]  (tokenizer_max_length=48)\n+ [state token]      (nn.Linear(32, 960) from proprioceptive state)\n```\n\nAll embeddings scaled by `√960` before concatenation. Attention: bidirectional for image+language tokens, causal for state token.\n\n### 1.3 Action Head (Expert)\n\n**Architecture**: Flow-Matching Transformer with interleaved cross-attention and self-attention.\n\n**Class**: `SmolVLMWithExpertModel.lm_expert` — separate Llama-architecture transformer\n\n| Parameter | Value |\n|-----------|-------|\n| expert_hidden_size | int(960 × 0.75) = **720** |\n| intermediate_size | **1792** |\n| num_expert_layers | **16** (same as num_vlm_layers) |\n| self_attn_every_n_layers | 2 |\n\n**Layer interleaving pattern**:\n- Even layers (0, 2, 4, ...): **self-attention** (prefix + suffix tokens concatenated)\n- Odd layers (1, 3, 5, ...): **cross-attention** (expert Q attends to VLM K,V)\n\nCross-attention K,V project from VLM dim (320 = 5×64) to expert dim:\n```python\nself.lm_expert.layers[layer_idx].self_attn.k_proj = nn.Linear(320, ..., bias=False)\nself.lm_expert.layers[layer_idx].self_attn.v_proj = nn.Linear(320, ..., bias=False)\n```\n\n**Action embedding** (in `embed_suffix()`):\n```python\nself.action_in_proj  = nn.Linear(32, 720)    # noisy actions → expert dim\nself.action_out_proj = nn.Linear(720, 32)    # expert output → action dim\nself.action_time_mlp_in  = nn.Linear(1440, 720)  # concat(action_emb, time_emb) → expert dim\nself.action_time_mlp_out = nn.Linear(720, 720)\n\n# Forward:\naction_emb = self.action_in_proj(noisy_actions)            # (B, 50, 720)\ntime_emb = sinusoidal(timestep, dim=720)                   # (B, 1, 720) → expand to (B, 50, 720)\naction_time_emb = cat([action_emb, time_emb], dim=2)       # (B, 50, 1440)\naction_time_emb = silu(self.action_time_mlp_in(action_time_emb))  # (B, 50, 720)\naction_time_emb = self.action_time_mlp_out(action_time_emb)       # (B, 50, 720)\n```\n\n**Output**: Continuous, `chunk_size=50` steps, `max_action_dim=32` (padded; LIBERO actual: 7D = 6D EEF delta + 1D gripper).\n\n## 2. Forward Pass Data Flow\n\n### 2.1 Training (`VLAFlowMatching.forward`)\n\n```\nInput: images, lang_tokens, state, actions\n\n1. Sample noise ~ N(0,1),  shape (B, 50, 32)\n2. Sample time ~ Beta(1.5, 1.0) * 0.999 + 0.001\n3. x_t = time * noise + (1 - time) * actions        # noisy interpolation\n4. u_t = noise - actions                             # target velocity field\n\n5. embed_prefix(images, lang_tokens, state):\n   a. vision_model(images) → (B, 1024, 768)         # SigLIP\n   b. connector(·) → (B, 64, 960)                   # pixel shuffle + projection\n   c. Concat: [img_special + 64_vis + img_end] × cameras + lang_emb + state_emb\n   → prefix_embs: (B, prefix_len, 960)\n\n6. embed_suffix(x_t, time):\n   a. action_in_proj(x_t) → (B, 50, 720)\n   b. sinusoidal time embedding → (B, 50, 720)\n   c. MLP(cat(action, time)) → (B, 50, 720)\n   → suffix_embs: (B, 50, 720)\n\n7. Construct 2D attention mask + position_ids\n\n8. vlm_with_expert.forward([prefix_embs, suffix_embs]):\n   For each layer i in 0..15:\n     if i % 2 == 0:  # self-attention\n       concat(prefix, suffix) → joint self-attention → split back\n     else:            # cross-attention\n       VLM processes prefix → KV\n       Expert Q attends to VLM KV\n   → (prefix_out, suffix_out)\n\n9. suffix_out = suffix_out[:, -50:]                  # last chunk_size tokens\n10. v_t = action_out_proj(suffix_out)                # (B, 50, 32)\n11. loss = F.mse_loss(u_t, v_t, reduction=\"none\")    # masked by actions_is_pad\n```\n\n### 2.2 Inference (`VLAFlowMatching.sample_actions`)\n\n```\n1. Encode prefix once → cache KV\n2. x_t = noise ~ N(0,1)\n3. For step in range(num_steps=10):\n     time = 1.0 - step/10\n     v_t = denoise_step(x_t, time, cached_KV)\n     x_t = x_t + (-1/10) * v_t       # Euler integration\n4. Return x_t as predicted actions\n```\n\nKV-caching: prefix encoded once, denoising steps only process suffix with cross-attention to cached prefix KV.\n\n## 3. Key Classes and File Paths\n\n### LeRobot repo (`huggingface/lerobot`)\n\n| Class | File |\n|-------|------|\n| `SmolVLAPolicy` | `lerobot/policies/smolvla/modeling_smolvla.py` |\n| `SmolVLAConfig` | `lerobot/policies/smolvla/configuration_smolvla.py` |\n| `VLAFlowMatching` | `lerobot/policies/smolvla/modeling_smolvla.py` |\n| `SmolVLMWithExpertModel` | `lerobot/policies/smolvla/smolvlm_with_expert.py` |\n\n### Transformers repo (`huggingface/transformers`)\n\n| Class | File |\n|-------|------|\n| `SmolVLMForConditionalGeneration` | `transformers/models/smolvlm/modeling_smolvlm.py` |\n| `SmolVLMConnector` | `transformers/models/smolvlm/modeling_smolvlm.py` |\n| `SmolVLMSimpleMLP` | `transformers/models/smolvlm/modeling_smolvlm.py` |\n| `SmolVLMVisionTransformer` (SigLIP) | `transformers/models/smolvlm/modeling_smolvlm.py` |\n\n### Training\n\n| Item | Detail |\n|------|--------|\n| Entry point | `lerobot/scripts/lerobot_train.py` → `train(cfg: TrainPipelineConfig)` |\n| CLI | `lerobot-train` |\n| Loss | MSE: `F.mse_loss(u_t, v_t)` where u_t = noise - actions |\n| Time sampling | Beta(α=1.5, β=1.0) scaled to [0.001, 1.0] |\n| Optimizer | AdamW, lr=1e-4, betas=(0.9, 0.95), weight_decay=1e-10 |\n| Scheduler | Cosine decay, warmup=1000, decay_steps=30000, decay_lr=2.5e-6 |\n| Grad clip | 10.0 |\n\n## 4. LoRA Configuration\n\nDefault targets (`_get_default_peft_targets`):\n```python\ntarget_modules = r\"(model\\.vlm_with_expert\\.lm_expert\\..*\\.(q|v)_proj|model\\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))\"\n```\n\nTargets:\n- All **Q and V projections** in the expert transformer\n- **state_proj**, **action_in_proj**, **action_out_proj**, **action_time_mlp_in**, **action_time_mlp_out**\n\nDefault training mode: `train_expert_only=True`, `freeze_vision_encoder=True`, `train_state_proj=True`. VLM backbone frozen.\n\n## 5. LIBERO Dataset\n\n**HuggingFace repo**: `HuggingFaceVLA/libero`\n\n| Field | Shape / Type |\n|-------|-------------|\n| `observation.state` | 8D (EEF pos 3D + axis-angle 3D + gripper qpos 2D) |\n| `observation.images.image` | agentview camera, HWC uint8 |\n| `observation.images.image2` | wrist camera, HWC uint8 |\n| actions | 7D (6D EEF delta + 1D gripper), padded to 32D internally |\n| action range | Box(-1, 1, shape=(7,)) |\n\n**Data format**: LeRobotDataset v3.0 — chunked Parquet (tabular) + MP4 (video frames).\n\n**Loading**: `make_dataset(cfg)` creates `LeRobotDataset` from Hub repo_id.\n\n**Training command**:\n```bash\nlerobot-train \\\n  --policy.type=smolvla \\\n  --policy.load_vlm_weights=true \\\n  --dataset.repo_id=HuggingFaceVLA/libero \\\n  --env.type=libero \\\n  --env.task=libero_10 \\\n  --steps=100000 \\\n  --batch_size=4\n```\n\n## 6. ACIS Insertion Point Analysis\n\n### 6.1 Existing Compression\n\nSmolVLA already has:\n- **Pixel shuffle**: 1024 → 64 tokens (16x spatial reduction)\n- **VLM layer skipping**: uses 16 of 32 layers\n\nNo dynamic token pruning exists in the codebase.\n\n### 6.2 ACIS Cross-Attention Module: `s_i = CrossAttn(a_query, v_i)`\n\n#### Where to get `v_i` (visual tokens)\n\n**Option A — Post-connector (recommended)**:\n- Location: output of `SmolVLMConnector.forward()` in `embed_image()`\n- Shape: `(B, 64, 960)` per camera\n- Advantage: already in LLM embedding space (dim=960), semantically rich after SigLIP + projection\n- These are the tokens that enter the prefix embeddings\n\n**Option B — Post-VLM-encoding**:\n- Location: after VLM prefix forward pass (the cached KV states)\n- Shape: `(B, prefix_len, num_kv_heads, head_dim)` per layer\n- Advantage: contextualized by language tokens via self-attention\n- Disadvantage: entangled with non-visual tokens, need to extract visual positions\n\n**Recommendation: Option A** — cleaner, shape is known, tokens are identifiable.\n\n#### Where to get `a_query` (action conditioning)\n\n**Option A — From `embed_suffix()` output (recommended)**:\n- Location: after `action_time_mlp_out` in `embed_suffix()`\n- Shape: `(B, chunk_size, 720)` — need projection to match v_i dim\n- Contains action + time information, semantically represents \"what action is being predicted\"\n- Available before the expert transformer processes it\n\n**Option B — From expert intermediate layer**:\n- Location: output of an early expert layer (e.g., layer 2 or 4)\n- Shape: `(B, chunk_size, 720)`\n- Advantage: richer representation after some self/cross-attention\n- Disadvantage: creates a circular dependency (expert output depends on prefix, but ACIS modifies prefix based on expert)\n\n**Option C — Learnable query (simplest)**:\n- `a_query = nn.Parameter(torch.randn(1, num_queries, 960))`\n- No dependency on actual actions during forward pass\n- Trained end-to-end to predict importance\n\n**Recommendation: Option A** for training (action-conditioned), **Option C** as simpler baseline.\n\n#### Insertion Point in Code\n\n```python\n# In SmolVLMWithExpertModel or VLAFlowMatching\n\n# STEP 1: Get visual tokens (before prefix assembly)\nvis_tokens = self.embed_image(images)          # (B, 64, 960) per camera\n# → all cameras: (B, num_cameras * 64, 960)\n\n# STEP 2: Get action query\nsuffix_embs = self.embed_suffix(x_t, time)     # (B, 50, 720)\na_query = self.acis_query_proj(suffix_embs)     # (B, 50, 960) or pool to (B, 1, 960)\n\n# STEP 3: ACIS cross-attention\n# s_i = CrossAttn(a_query, v_i)\nimportance_scores = self.acis_module(\n    query=a_query,                              # (B, Q, 960)\n    key=vis_tokens,                             # (B, N_vis, 960)\n    value=vis_tokens                            # (B, N_vis, 960)\n)                                               # → (B, N_vis) scores\n\n# STEP 4: Soft top-k selection\nsoft_mask = differentiable_topk(importance_scores, k=k)  # (B, N_vis)\n\n# STEP 5: Apply mask to visual tokens\nvis_tokens_pruned = vis_tokens * soft_mask.unsqueeze(-1)  # soft weighting\n# OR: select top-k indices for hard pruning\n\n# STEP 6: Continue with prefix assembly using pruned tokens\nprefix_embs = self.embed_prefix_with_pruned_vis(vis_tokens_pruned, lang, state)\n```\n\n#### Specific Code Modifications\n\n**File**: `lerobot/policies/smolvla/smolvlm_with_expert.py`\n\n1. Add ACIS module to `SmolVLMWithExpertModel.__init__()`:\n```python\nself.acis_query_proj = nn.Linear(720, 960)  # expert dim → VLM dim\nself.acis_cross_attn = nn.MultiheadAttention(\n    embed_dim=960, num_heads=8, kdim=960, vdim=960, batch_first=True\n)\nself.acis_score_head = nn.Linear(960, 1)  # output per-token score\n```\n\n2. Modify forward flow in `VLAFlowMatching.forward()` (in `modeling_smolvla.py`):\n   - After `embed_image()` and `embed_suffix()`, compute ACIS scores\n   - Apply soft top-k mask\n   - Rebuild prefix with masked visual tokens\n\n3. Add ACIS modules to LoRA target regex:\n```python\ntarget_modules = r\"(...|model\\.acis_.*)\"\n```\n\n### 6.3 Forward Pass Modification Summary\n\n```\nOriginal:  images → SigLIP → connector → embed_prefix → VLM+Expert → loss\nModified:  images → SigLIP → connector → [ACIS scoring → soft top-k] → embed_prefix → VLM+Expert → loss + IMM_loss\n                                              ↑\n                                     action query from embed_suffix()\n```\n\n### 6.4 IMM Loss Integration\n\nThe IMM loss adds to the existing flow matching MSE loss:\n\n```python\n# Original loss\nloss_fm = F.mse_loss(u_t, v_t, reduction=\"none\")  # flow matching\n\n# IMM auxiliary losses (computed from ACIS scores)\nloss_margin = margin_loss(importance_scores, kept_mask, pruned_mask, margin=δ)\nloss_calibration = calibration_loss(importance_scores, reconstruction_error)\n\n# Total\nloss = loss_fm + λ_margin * loss_margin + λ_cal * loss_calibration\n```\n\n## 7. Differentiable Soft Top-K: Method Comparison\n\n### 7.1 Methods Surveyed\n\n#### Sigmoid + Implicit Differentiation (Thomas Ahle)\n\nBinary-search for shift `t` such that `Σ σ(x_i + t) = k`, return `σ(x_i + t)`. Backward via implicit differentiation: `J = diag(v) - vv^T/‖v‖₁`.\n\n- **Impl**: [gist, 20 lines](https://gist.github.com/thomasahle/4c1e85e5842d01b007a8d10f5fed3a18), zero deps\n- **Gradient**: Exact Jacobian, deterministic, zero variance\n- **Complexity**: O(n × B) forward (B≈64 binary search steps), O(n) backward\n- **Constraint**: Σp_i = k **exactly** satisfied\n- **Issues**: Binary search not maximally GPU-efficient; elements near threshold get soft (ambiguous) values\n\n#### DFTopK (arXiv Oct 2025)\n\nSigmoid on scores shifted by midpoint of k-th and (k+1)-th largest: `σ((x - (x[k]+x[k+1])/2) / τ)`.\n\n- **Impl**: [github.com/zhangzhen97/DFTOPK](https://github.com/zhangzhen97/DFTOPK)\n- **Gradient**: Deterministic, localized uncertainty at boundary\n- **Complexity**: O(n) average (Introselect)\n- **Constraint**: Σp_i ≈ k (approximate)\n- **Issues**: τ requires tuning\n\n#### LapSum (ICML 2025)\n\nDifferentiable top-k via CDF of sum of Laplace distributions. Threshold `b` found such that `Σ Lap_α(b - r_i) = w`.\n\n- **Impl**: [github.com/gmum/LapSum](https://github.com/gmum/LapSum), `pip install lapsum`\n- **Gradient**: Exact, deterministic, zero variance\n- **Complexity**: O(n log n), O(n) backward\n- **Constraint**: Exact\n- **Issues**: α hyperparameter; requires library\n\n#### Gumbel Top-k (Subset Sampling)\n\nIterative Gumbel-perturbed softmax k times with masking. Used in **LightVLA**.\n\n- **Impl**: ~20 lines; UvA DL Notebooks `SubsetOperator`\n- **Gradient**: Stochastic (Gumbel noise), reparameterizable, STE for hard mode\n- **Complexity**: O(n × k) — k sequential softmax ops\n- **Constraint**: Exact k elements (hard mode)\n- **Issues**: k=150 means 150 sequential ops; variance from noise\n\n#### SOFT (Optimal Transport, NeurIPS 2020)\n\nTop-k as Entropic OT via Sinkhorn iterations.\n\n- **Impl**: ~120 lines gist, no pip package\n- **Gradient**: Biased (controlled by ε)\n- **Complexity**: O(n × k × T), T=50-200 Sinkhorn iterations\n- **Constraint**: Exact (doubly stochastic)\n- **Issues**: NaN instability for small ε; slow\n\n#### NeuralSort / SoftSort\n\nFull n×n permutation matrix relaxation. O(n²) time and memory.\n\n- **Issues**: Produces full permutation matrix — overkill for top-k; n=500 → 250K entries\n\n#### Temperature Sigmoid (baseline)\n\n`σ(α · (s_i - kth_percentile) / τ)` with τ annealing.\n\n- **Impl**: 5 lines, zero deps\n- **Gradient**: Biased; no gradient through `kthvalue`\n- **Complexity**: O(n log n) or O(n) with `torch.kthvalue`\n- **Issues**: Σp_i ≠ k; gradient vanishing at low τ\n\n### 7.2 Comparison Table\n\n| Method | Complexity | Gradient | Exact Σ=k | Variance | Code | VLA Proven |\n|--------|-----------|----------|-----------|----------|------|------------|\n| **Sigmoid+ImplDiff** | O(n) | Exact | **Yes** | Zero | 20 lines | No |\n| **DFTopK** | O(n) | Deterministic | Approx | Zero | ~50 lines | No |\n| **LapSum** | O(n log n) | Exact | **Yes** | Zero | Library | No |\n| **Gumbel Top-k** | O(n·k) | STE | Yes (hard) | High | 20 lines | **Yes** |\n| **SOFT (OT)** | O(n·k·T) | Biased | Yes | Zero | 120 lines | No |\n| **NeuralSort** | O(n²) | Biased | N/A | Zero | Library | No |\n| **SoftSort** | O(n²) | Biased | N/A | Zero | 3 lines | No |\n| **Temp Sigmoid** | O(n) | Biased | No | Zero | 5 lines | Indirect |\n\n### 7.3 Recommendation\n\n**Primary: Sigmoid + Implicit Differentiation**\n\n- 20 lines of PyTorch, zero dependencies, passes `torch.autograd.gradcheck`\n- Exact Jacobian, zero variance — critical for stable LoRA fine-tuning\n- Exactly satisfies Σp_i = k\n- O(n) backward; forward binary search negligible vs VLA forward pass\n- Soft probabilities usable as token weights; binarize with STE at inference\n\n```python\n# Reference implementation (Thomas Ahle)\n# https://gist.github.com/thomasahle/4c1e85e5842d01b007a8d10f5fed3a18\n\nclass TopK(torch.autograd.Function):\n    @staticmethod\n    def forward(ctx, x, k):\n        # Binary search for threshold t such that sum(sigmoid(x + t)) = k\n        lo, hi = -1000.0, 1000.0\n        for _ in range(64):\n            mid = (lo + hi) / 2\n            if torch.sigmoid(x + mid).sum(-1).item() < k:\n                lo = mid\n            else:\n                hi = mid\n        t = (lo + hi) / 2\n        p = torch.sigmoid(x + t)\n        ctx.save_for_backward(p)\n        return p\n\n    @staticmethod\n    def backward(ctx, grad_output):\n        p, = ctx.saved_tensors\n        v = p * (1 - p)  # sigmoid derivative\n        # Implicit differentiation of constraint sum(p) = k\n        grad = v * (grad_output - (v * grad_output).sum(-1, keepdim=True) / v.sum(-1, keepdim=True))\n        return grad, None\n```\n\n**Secondary: DFTopK** — for citation in paper (published method), O(n) complexity, similar sigmoid approach but uses `torch.kthvalue`.\n\n**Fallback: Gumbel Top-k** — if stochastic gradients prove beneficial for exploration during LoRA training. Proven in LightVLA.\n\n### 7.4 Key Related Work\n\n- **LightVLA** (arXiv:2509.12594): Gumbel-softmax VLA token pruning, LoRA rank 32, 59% FLOP reduction, 2.9% task success improvement\n- **AutoSelect** (arXiv:2603.07135): Soft top-k + variance-preserving noise gating for LLaVA, 0.69ms overhead, 96.5% accuracy retention at 88.9% pruning\n- **DiffRate** (ICCV 2023): Differentiable compression rate for ViT ([github.com/OpenGVLab/DiffRate](https://github.com/OpenGVLab/DiffRate))\n\n## 8. Token Compression Integration: FastV-Style Pruning\n\n### 8.1 How It Maps to SmolVLA\n\nFastV prunes visual tokens at an intermediate LLM layer based on attention from text tokens. In SmolVLA:\n\n**Option 1 — Prune before VLM+Expert forward (ACIS approach)**:\n- After `embed_image()` returns `(B, 64, 960)`, score with ACIS, mask/select, then build prefix\n- Pros: clean, modular, no VLM modification\n- Cons: scores computed without LLM context\n\n**Option 2 — Prune in VLM KV cache (inference optimization)**:\n- After prefix encoding, prune KV entries for low-importance visual tokens\n- Modify `past_key_values[layer][\"key_states\"]` and `[\"value_states\"]`\n- Shape: `(B, prefix_len, num_kv_heads, head_dim)` → remove rows for pruned visual positions\n- Pros: reduces computation in all subsequent denoising steps\n- Cons: requires tracking visual token positions within prefix\n\n**Option 3 — Mid-layer pruning (FastV-faithful)**:\n- In `SmolVLMWithExpertModel.forward()`, after layer N, compute attention scores from state/language tokens to visual tokens, prune, continue\n- Requires modifying the layer-by-layer loop\n\n**Recommendation**: Option 1 (ACIS before prefix) for training. At inference, additionally apply Option 2 (KV cache pruning) for efficiency.\n\n### 8.2 Visual Token Position Tracking\n\nPrefix layout for LIBERO (2 cameras):\n```\n[img_start(2)] [vis_0..63(64)] [img_end(1)]  → camera 1: tokens 0..66\n[img_start(2)] [vis_0..63(64)] [img_end(1)]  → camera 2: tokens 67..133\n[lang_tokens(48)]                              → tokens 134..181\n[state_token(1)]                               → token 182\n```\n\nVisual token indices: `[2:66]` and `[69:133]` (64 tokens each, offset by special tokens).\n\n## 9. Summary: ACIS Integration Blueprint\n\n```\n┌─────────┐     ┌──────────┐     ┌───────────────┐\n│  Images  │────→│  SigLIP  │────→│  Connector    │──→ vis_tokens (B, 64×C, 960)\n└─────────┘     └──────────┘     │  (PixelShuffle│\n                                  │   + MLP)      │\n                                  └───────────────┘\n                                          │\n                                          ▼\n┌─────────────┐                 ┌─────────────────┐\n│ embed_suffix │──a_query──────→│  ACIS Module    │\n│ (noisy act + │  (B,Q,960)     │  CrossAttn +    │──→ importance_scores (B, N_vis)\n│  time emb)   │                │  Score Head     │\n└─────────────┘                 └─────────────────┘\n                                          │\n                                          ▼\n                                ┌─────────────────┐\n                                │  Soft Top-K     │──→ soft_mask (B, N_vis)\n                                │  (Sigmoid+Impl) │\n                                └─────────────────┘\n                                          │\n                                          ▼\n                                ┌─────────────────┐\n                                │  Apply Mask     │──→ pruned_vis (B, K, 960)\n                                └─────────────────┘\n                                          │\n                                          ▼\n                                ┌─────────────────┐\n                                │  embed_prefix   │──→ prefix_embs (B, prefix_len', 960)\n                                │  (+ lang + state│\n                                └─────────────────┘\n                                          │\n                                          ▼\n                                ┌─────────────────┐\n                                │  VLM + Expert   │──→ v_t (B, 50, 32)\n                                │  (16 layers)    │\n                                └─────────────────┘\n                                          │\n                                          ▼\n                                ┌─────────────────┐\n                                │  Loss:          │\n                                │  MSE(u_t, v_t)  │\n                                │  + λ·L_margin   │\n                                │  + λ·L_calibr   │\n                                └─────────────────┘\n```\n",
      "numLines": 601,
      "startLine": 1,
      "totalLines": 601
    }
  }
}
````

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_016FGriupXrNuGkWS92VJGPD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/smolvla_wrapper.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "995fdf9b-d728-4d99-ae81-9aab624093a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhJ2P93aZLr7DrkXDoNU7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12715,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12715
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

_source line 8 · 2026-05-15T12:03:37.311Z_

<details><summary>↩ Tool result · `toolu_016FGriupXrNuGkWS92VJGPD`</summary>

```text
1	"""IMMSmolVLAWrapper — wraps SmolVLA forward pass with ACIS scoring + token selection.
2	
3	Data flow:
4	  Original:  images → SigLIP → connector → embed_prefix → VLM+Expert → loss
5	  Modified:  images → SigLIP → connector → [ACIS → soft top-k → mask] → embed_prefix → VLM+Expert → loss + L_margin
6	
7	Design: wrapper pattern — never modifies the original SmolVLA model code.
8	Depends: acis.ACIS, losses.IMMTotalLoss, token_selection.MarginAwareTokenSelector.
9	"""
10	
11	from __future__ import annotations
12	
13	import torch
14	import torch.nn as nn
15	import torch.nn.functional as F
16	from torch import Tensor
17	from typing import Any, Dict, Optional, Tuple
18	
19	from .acis import ACIS
20	from .losses import IMMTotalLoss
21	from .token_selection import MarginAwareTokenSelector
22	
23	
24	class IMMSmolVLAWrapper(nn.Module):
25	    def __init__(
26	        self,
27	        smolvla_model: nn.Module,
28	        acis_config: Optional[Dict[str, Any]] = None,
29	        imm_config: Optional[Dict[str, Any]] = None,
30	    ):
31	        """
32	        Args:
33	            smolvla_model: original SmolVLA/VLAFlowMatching model instance.
34	            acis_config: kwargs for ACIS (visual_dim, action_dim, num_heads, dropout).
35	            imm_config: kwargs for IMMTotalLoss + k_ratio.
36	                        Expected keys: lambda_margin, delta, warmup_steps, temperature,
37	                        method, k_ratio.
38	        """
39	        super().__init__()
40	        self.model = smolvla_model
41	        acis_config = acis_config or {}
42	        imm_config = imm_config or {}
43	
44	        self.acis = ACIS(**acis_config)
45	
46	        self.k_ratio = imm_config.pop("k_ratio", 0.5)
47	        selector_temp = imm_config.pop("selector_temperature", 1.0)
48	
49	        self.imm_loss = IMMTotalLoss(**imm_config)
50	        self.token_selector = MarginAwareTokenSelector(temperature=selector_temp)
51	
52	    def forward(
53	        self, batch: Dict[str, Tensor], step: int = 0
54	    ) -> Tuple[Tensor, Dict[str, Any]]:
55	        """
56	        Full forward with ACIS scoring and IMM loss.
57	
58	        Args:
59	            batch: dict with at least 'images', 'actions', and any other keys
60	                   expected by the underlying SmolVLA model.
61	            step: current training step (for lambda warmup).
62	        Returns:
63	            total_loss: scalar.
64	            info: dict with all diagnostics.
65	        """
66	        # 1. Visual encoding
67	        vis_tokens = self.model.embed_image(batch["images"])  # (B, N_vis, 960)
68	
69	        # 2. Flow-matching noise schedule
70	        actions = batch["actions"]
71	        B = actions.shape[0]
72	        time = torch.rand(B, device=actions.device, dtype=actions.dtype)
73	        noise = torch.randn_like(actions)
74	        x_t = (1 - time.view(B, 1, 1)) * actions + time.view(B, 1, 1) * noise
75	
76	        # 3. Action embeddings (query for ACIS)
77	        suffix_embs = self.model.embed_suffix(x_t, time)  # (B, 50, 720)
78	
79	        # 4. ACIS scoring
80	        importance_scores = self.acis(suffix_embs, vis_tokens)  # (B, N_vis)
81	
82	        # 5. Token selection
83	        N_vis = vis_tokens.shape[1]
84	        k = max(1, int(N_vis * self.k_ratio))
85	        selected_tokens, mask, sel_info = self.token_selector(
86	            importance_scores, vis_tokens, k, training=self.training
87	        )
88	
89	        # 6. Build prefix with selected tokens and run VLM + Expert
90	        prefix_embs = self._build_prefix(selected_tokens, batch)
91	        v_t = self._expert_forward(prefix_embs, suffix_embs)
92	
93	        # 7. Flow matching loss: predict vector field u_t = noise - actions
94	        u_t = noise - actions
95	        action_loss = F.mse_loss(v_t, u_t)
96	
97	        # 8. IMM total loss
98	        total_loss, imm_info = self.imm_loss(action_loss, importance_scores, k, step)
99	
100	        info = {
101	            **sel_info,
102	            **imm_info,
103	            "importance_scores": importance_scores.detach(),
104	            "k": k,
105	            "k_ratio": self.k_ratio,
106	            "lipschitz_estimate": self.acis.get_lipschitz_estimate(),
107	        }
108	        return total_loss, info
109	
110	    def forward_baseline(self, batch: Dict[str, Tensor]) -> Tuple[Tensor, Dict[str, Any]]:
111	        """Baseline forward: no ACIS, no token selection, action loss only."""
112	        vis_tokens = self.model.embed_image(batch["images"])
113	        actions = batch["actions"]
114	        B = actions.shape[0]
115	        time = torch.rand(B, device=actions.device, dtype=actions.dtype)
116	        noise = torch.randn_like(actions)
117	        x_t = (1 - time.view(B, 1, 1)) * actions + time.view(B, 1, 1) * noise
118	
119	        suffix_embs = self.model.embed_suffix(x_t, time)
120	        prefix_embs = self._build_prefix(vis_tokens, batch)
121	        v_t = self._expert_forward(prefix_embs, suffix_embs)
122	
123	        u_t = noise - actions
124	        action_loss = F.mse_loss(v_t, u_t)
125	        return action_loss, {"action_loss": action_loss.detach()}
126	
127	    def _build_prefix(self, vis_tokens: Tensor, batch: Dict[str, Tensor]) -> Tensor:
128	        """Construct prefix embeddings from visual tokens + language + state."""
129	        if hasattr(self.model, "embed_prefix"):
130	            lang = batch.get("lang_tokens", None)
131	            state = batch.get("state", None)
132	            return self.model.embed_prefix(vis_tokens, lang, state)
133	        return vis_tokens
134	
135	    def _expert_forward(self, prefix_embs: Tensor, suffix_embs: Tensor) -> Tensor:
136	        """Run VLM backbone + expert head."""
137	        if hasattr(self.model, "expert_forward"):
138	            return self.model.expert_forward(prefix_embs, suffix_embs)
139	        if hasattr(self.model, "forward_expert"):
140	            return self.model.forward_expert(prefix_embs, suffix_embs)
141	        raise AttributeError(
142	            "SmolVLA model has no expert_forward or forward_expert method. "
143	            "Check the model API and update _expert_forward accordingly."
144	        )
145	
146	
147	class _MockSmolVLA(nn.Module):
148	    """Minimal mock for standalone testing."""
149	
150	    def __init__(self, visual_dim: int = 960, action_dim: int = 720,
151	                 raw_action_dim: int = 32, action_tokens: int = 50):
152	        super().__init__()
153	        self.proj = nn.Linear(visual_dim, visual_dim)
154	        self.suffix_proj = nn.Linear(raw_action_dim + 1, action_dim)
155	        self.expert = nn.Linear(visual_dim + action_dim, raw_action_dim)
156	        self.action_dim = action_dim
157	        self.raw_action_dim = raw_action_dim
158	        self.action_tokens = action_tokens
159	
160	    def embed_image(self, images: Tensor) -> Tensor:
161	        B = images.shape[0]
162	        return self.proj(torch.randn(B, 128, 960, device=images.device))
163	
164	    def embed_suffix(self, x_t: Tensor, time: Tensor) -> Tensor:
165	        B, T, D = x_t.shape
166	        time_emb = time.unsqueeze(-1).unsqueeze(-1).expand(B, T, 1)
167	        inp = torch.cat([x_t, time_emb], dim=-1)  # (B, T, D+1)
168	        return self.suffix_proj(inp)               # (B, T, action_dim=720)
169	
170	    def embed_prefix(self, vis_tokens: Tensor, lang: Any = None, state: Any = None) -> Tensor:
171	        return vis_tokens
172	
173	    def expert_forward(self, prefix: Tensor, suffix: Tensor) -> Tensor:
174	        B = prefix.shape[0]
175	        p = prefix.mean(dim=1)   # (B, 960)
176	        s = suffix.mean(dim=1)   # (B, 720)
177	        out = self.expert(torch.cat([p, s], dim=-1))  # (B, raw_action_dim)
178	        return out.unsqueeze(1).expand(B, suffix.shape[1], self.raw_action_dim)
179	
180	
181	if __name__ == "__main__":
182	    torch.manual_seed(42)
183	    B = 2
184	
185	    mock = _MockSmolVLA()
186	    wrapper = IMMSmolVLAWrapper(
187	        mock,
188	        acis_config={"visual_dim": 960, "action_dim": 720, "num_heads": 8},
189	        imm_config={"lambda_margin": 0.1, "delta": 0.5, "warmup_steps": 100, "k_ratio": 0.5},
190	    )
191	
192	    batch = {
193	        "images": torch.randn(B, 2, 3, 224, 224),
194	        "actions": torch.randn(B, 50, 32),
195	    }
196	
197	    wrapper.train()
198	    total_loss, info = wrapper(batch, step=50)
199	    total_loss.backward()
200	    print(f"[train] total_loss={total_loss.item():.4f}, k={info['k']}, "
201	          f"lipschitz={info['lipschitz_estimate']:.4f}")
202	
203	    base_loss, base_info = wrapper.forward_baseline(batch)
204	    print(f"[baseline] action_loss={base_loss.item():.4f}")
205	    print("All wrapper tests passed!")
206	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "aed14155-d4ce-4761-b9f0-ba96f49f751d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/smolvla_wrapper.py",
      "content": "\"\"\"IMMSmolVLAWrapper — wraps SmolVLA forward pass with ACIS scoring + token selection.\n\nData flow:\n  Original:  images → SigLIP → connector → embed_prefix → VLM+Expert → loss\n  Modified:  images → SigLIP → connector → [ACIS → soft top-k → mask] → embed_prefix → VLM+Expert → loss + L_margin\n\nDesign: wrapper pattern — never modifies the original SmolVLA model code.\nDepends: acis.ACIS, losses.IMMTotalLoss, token_selection.MarginAwareTokenSelector.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom torch import Tensor\nfrom typing import Any, Dict, Optional, Tuple\n\nfrom .acis import ACIS\nfrom .losses import IMMTotalLoss\nfrom .token_selection import MarginAwareTokenSelector\n\n\nclass IMMSmolVLAWrapper(nn.Module):\n    def __init__(\n        self,\n        smolvla_model: nn.Module,\n        acis_config: Optional[Dict[str, Any]] = None,\n        imm_config: Optional[Dict[str, Any]] = None,\n    ):\n        \"\"\"\n        Args:\n            smolvla_model: original SmolVLA/VLAFlowMatching model instance.\n            acis_config: kwargs for ACIS (visual_dim, action_dim, num_heads, dropout).\n            imm_config: kwargs for IMMTotalLoss + k_ratio.\n                        Expected keys: lambda_margin, delta, warmup_steps, temperature,\n                        method, k_ratio.\n        \"\"\"\n        super().__init__()\n        self.model = smolvla_model\n        acis_config = acis_config or {}\n        imm_config = imm_config or {}\n\n        self.acis = ACIS(**acis_config)\n\n        self.k_ratio = imm_config.pop(\"k_ratio\", 0.5)\n        selector_temp = imm_config.pop(\"selector_temperature\", 1.0)\n\n        self.imm_loss = IMMTotalLoss(**imm_config)\n        self.token_selector = MarginAwareTokenSelector(temperature=selector_temp)\n\n    def forward(\n        self, batch: Dict[str, Tensor], step: int = 0\n    ) -> Tuple[Tensor, Dict[str, Any]]:\n        \"\"\"\n        Full forward with ACIS scoring and IMM loss.\n\n        Args:\n            batch: dict with at least 'images', 'actions', and any other keys\n                   expected by the underlying SmolVLA model.\n            step: current training step (for lambda warmup).\n        Returns:\n            total_loss: scalar.\n            info: dict with all diagnostics.\n        \"\"\"\n        # 1. Visual encoding\n        vis_tokens = self.model.embed_image(batch[\"images\"])  # (B, N_vis, 960)\n\n        # 2. Flow-matching noise schedule\n        actions = batch[\"actions\"]\n        B = actions.shape[0]\n        time = torch.rand(B, device=actions.device, dtype=actions.dtype)\n        noise = torch.randn_like(actions)\n        x_t = (1 - time.view(B, 1, 1)) * actions + time.view(B, 1, 1) * noise\n\n        # 3. Action embeddings (query for ACIS)\n        suffix_embs = self.model.embed_suffix(x_t, time)  # (B, 50, 720)\n\n        # 4. ACIS scoring\n        importance_scores = self.acis(suffix_embs, vis_tokens)  # (B, N_vis)\n\n        # 5. Token selection\n        N_vis = vis_tokens.shape[1]\n        k = max(1, int(N_vis * self.k_ratio))\n        selected_tokens, mask, sel_info = self.token_selector(\n            importance_scores, vis_tokens, k, training=self.training\n        )\n\n        # 6. Build prefix with selected tokens and run VLM + Expert\n        prefix_embs = self._build_prefix(selected_tokens, batch)\n        v_t = self._expert_forward(prefix_embs, suffix_embs)\n\n        # 7. Flow matching loss: predict vector field u_t = noise - actions\n        u_t = noise - actions\n        action_loss = F.mse_loss(v_t, u_t)\n\n        # 8. IMM total loss\n        total_loss, imm_info = self.imm_loss(action_loss, importance_scores, k, step)\n\n        info = {\n            **sel_info,\n            **imm_info,\n            \"importance_scores\": importance_scores.detach(),\n            \"k\": k,\n            \"k_ratio\": self.k_ratio,\n            \"lipschitz_estimate\": self.acis.get_lipschitz_estimate(),\n        }\n        return total_loss, info\n\n    def forward_baseline(self, batch: Dict[str, Tensor]) -> Tuple[Tensor, Dict[str, Any]]:\n        \"\"\"Baseline forward: no ACIS, no token selection, action loss only.\"\"\"\n        vis_tokens = self.model.embed_image(batch[\"images\"])\n        actions = batch[\"actions\"]\n        B = actions.shape[0]\n        time = torch.rand(B, device=actions.device, dtype=actions.dtype)\n        noise = torch.randn_like(actions)\n        x_t = (1 - time.view(B, 1, 1)) * actions + time.view(B, 1, 1) * noise\n\n        suffix_embs = self.model.embed_suffix(x_t, time)\n        prefix_embs = self._build_prefix(vis_tokens, batch)\n        v_t = self._expert_forward(prefix_embs, suffix_embs)\n\n        u_t = noise - actions\n        action_loss = F.mse_loss(v_t, u_t)\n        return action_loss, {\"action_loss\": action_loss.detach()}\n\n    def _build_prefix(self, vis_tokens: Tensor, batch: Dict[str, Tensor]) -> Tensor:\n        \"\"\"Construct prefix embeddings from visual tokens + language + state.\"\"\"\n        if hasattr(self.model, \"embed_prefix\"):\n            lang = batch.get(\"lang_tokens\", None)\n            state = batch.get(\"state\", None)\n            return self.model.embed_prefix(vis_tokens, lang, state)\n        return vis_tokens\n\n    def _expert_forward(self, prefix_embs: Tensor, suffix_embs: Tensor) -> Tensor:\n        \"\"\"Run VLM backbone + expert head.\"\"\"\n        if hasattr(self.model, \"expert_forward\"):\n            return self.model.expert_forward(prefix_embs, suffix_embs)\n        if hasattr(self.model, \"forward_expert\"):\n            return self.model.forward_expert(prefix_embs, suffix_embs)\n        raise AttributeError(\n            \"SmolVLA model has no expert_forward or forward_expert method. \"\n            \"Check the model API and update _expert_forward accordingly.\"\n        )\n\n\nclass _MockSmolVLA(nn.Module):\n    \"\"\"Minimal mock for standalone testing.\"\"\"\n\n    def __init__(self, visual_dim: int = 960, action_dim: int = 720,\n                 raw_action_dim: int = 32, action_tokens: int = 50):\n        super().__init__()\n        self.proj = nn.Linear(visual_dim, visual_dim)\n        self.suffix_proj = nn.Linear(raw_action_dim + 1, action_dim)\n        self.expert = nn.Linear(visual_dim + action_dim, raw_action_dim)\n        self.action_dim = action_dim\n        self.raw_action_dim = raw_action_dim\n        self.action_tokens = action_tokens\n\n    def embed_image(self, images: Tensor) -> Tensor:\n        B = images.shape[0]\n        return self.proj(torch.randn(B, 128, 960, device=images.device))\n\n    def embed_suffix(self, x_t: Tensor, time: Tensor) -> Tensor:\n        B, T, D = x_t.shape\n        time_emb = time.unsqueeze(-1).unsqueeze(-1).expand(B, T, 1)\n        inp = torch.cat([x_t, time_emb], dim=-1)  # (B, T, D+1)\n        return self.suffix_proj(inp)               # (B, T, action_dim=720)\n\n    def embed_prefix(self, vis_tokens: Tensor, lang: Any = None, state: Any = None) -> Tensor:\n        return vis_tokens\n\n    def expert_forward(self, prefix: Tensor, suffix: Tensor) -> Tensor:\n        B = prefix.shape[0]\n        p = prefix.mean(dim=1)   # (B, 960)\n        s = suffix.mean(dim=1)   # (B, 720)\n        out = self.expert(torch.cat([p, s], dim=-1))  # (B, raw_action_dim)\n        return out.unsqueeze(1).expand(B, suffix.shape[1], self.raw_action_dim)\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B = 2\n\n    mock = _MockSmolVLA()\n    wrapper = IMMSmolVLAWrapper(\n        mock,\n        acis_config={\"visual_dim\": 960, \"action_dim\": 720, \"num_heads\": 8},\n        imm_config={\"lambda_margin\": 0.1, \"delta\": 0.5, \"warmup_steps\": 100, \"k_ratio\": 0.5},\n    )\n\n    batch = {\n        \"images\": torch.randn(B, 2, 3, 224, 224),\n        \"actions\": torch.randn(B, 50, 32),\n    }\n\n    wrapper.train()\n    total_loss, info = wrapper(batch, step=50)\n    total_loss.backward()\n    print(f\"[train] total_loss={total_loss.item():.4f}, k={info['k']}, \"\n          f\"lipschitz={info['lipschitz_estimate']:.4f}\")\n\n    base_loss, base_info = wrapper.forward_baseline(batch)\n    print(f\"[baseline] action_loss={base_loss.item():.4f}\")\n    print(\"All wrapper tests passed!\")\n",
      "numLines": 206,
      "startLine": 1,
      "totalLines": 206
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01BWQh4paXLVkMHDjugT7EMj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/evaluate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "853d99ae-1f23-4a5c-a026-6f2deb9f30be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhJ2P93aZLr7DrkXDoNU7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12715,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12715
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

_source line 10 · 2026-05-15T12:03:37.673Z_

<details><summary>↩ Tool result · `toolu_01BWQh4paXLVkMHDjugT7EMj`</summary>

```text
1	"""IMM Evaluation Pipeline.
2	
3	Evaluates trained models under:
4	  - Clean vs perturbed inputs (Gaussian noise eps in {0.01, 0.02, 0.05})
5	  - With/without ACIS-based 50% token pruning
6	  - Metrics: margin stats, top-k preservation rate, L*eps/Delta_k, Kendall tau, certified bound
7	
8	Usage:
9	    python evaluate.py --checkpoint path/to/ckpt --config configs/imm_anchor.yaml --gpu 0
10	    python evaluate.py --checkpoint path/to/baseline --config configs/baseline.yaml --output results/baseline.json
11	
12	Depends: lerobot, torch, imm.
13	"""
14	
15	from __future__ import annotations
16	
17	import argparse
18	import json
19	import logging
20	import sys
21	from pathlib import Path
22	from typing import Any, Dict, List
23	
24	import torch
25	import torch.nn.functional as F
26	import yaml
27	
28	ARTIFACTS_DIR = Path(__file__).resolve().parent
29	sys.path.insert(0, str(ARTIFACTS_DIR))
30	
31	from imm.metrics import (
32	    certified_bound,
33	    compute_empirical_lipschitz,
34	    compute_margin,
35	    kendall_tau_distance,
36	    l_eps_delta_ratio,
37	    margin_statistics,
38	    topk_preservation_rate,
39	)
40	
41	logging.basicConfig(
42	    level=logging.INFO,
43	    format="%(asctime)s [%(levelname)s] %(message)s",
44	    datefmt="%Y-%m-%d %H:%M:%S",
45	)
46	log = logging.getLogger(__name__)
47	
48	
49	def parse_args():
50	    parser = argparse.ArgumentParser(description="IMM evaluation for SmolVLA on LIBERO")
51	    parser.add_argument("--checkpoint", type=str, required=True, help="Path to checkpoint file or directory")
52	    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file")
53	    parser.add_argument("--gpu", type=int, default=0, help="GPU index")
54	    parser.add_argument("--output", type=str, default=None, help="Path to save results JSON (default: results/&lt;run>.json)")
55	    parser.add_argument("--max_batches", type=int, default=100, help="Max batches to evaluate")
56	    parser.add_argument("--lipschitz_samples", type=int, default=100, help="Samples for empirical Lipschitz estimation")
57	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
58	    return parser.parse_args()
59	
60	
61	def load_config(config_path: str) -> Dict[str, Any]:
62	    """Load YAML config with _base_ inheritance."""
63	    import copy
64	    config_path = Path(config_path)
65	    with open(config_path) as f:
66	        config = yaml.safe_load(f)
67	    if "_base_" in config:
68	        base_path = config_path.parent / config.pop("_base_")
69	        base_config = load_config(str(base_path))
70	        for k, v in config.items():
71	            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):
72	                base_config[k].update(v)
73	            else:
74	                base_config[k] = v
75	        return base_config
76	    return config
77	
78	
79	def load_model_and_checkpoint(config: Dict[str, Any], checkpoint_path: str, device: torch.device):
80	    """Load SmolVLA policy, optionally wrap with IMM, then load checkpoint weights."""
81	    from train import load_smolvla_policy, wrap_with_imm
82	
83	    policy = load_smolvla_policy(config, device)
84	    imm_enabled = config.get("imm", {}).get("enabled", False)
85	
86	    if imm_enabled:
87	        model = wrap_with_imm(policy, config)
88	        model.to(device)
89	    else:
90	        model = policy
91	
92	    ckpt_path = Path(checkpoint_path)
93	    if ckpt_path.is_dir():
94	        ckpt_path = ckpt_path / "checkpoint.pt"
95	
96	    log.info("Loading checkpoint from %s", ckpt_path)
97	    state = torch.load(ckpt_path, map_location=device, weights_only=False)
98	    model.load_state_dict(state["model_state_dict"], strict=False)
99	
100	    model.eval()
101	    return model, imm_enabled
102	
103	
104	def compute_importance_scores(model, batch: Dict[str, torch.Tensor], imm_enabled: bool):
105	    """Extract ACIS importance scores from the model.
106	
107	    Returns (scores, k) or (None, None) for baseline models.
108	    """
109	    if not imm_enabled:
110	        return None, None
111	
112	    vis_tokens = model.model.embed_image(batch["images"])
113	
114	    actions = batch["actions"]
115	    B = actions.shape[0]
116	    time = torch.rand(B, device=actions.device, dtype=actions.dtype)
117	    noise = torch.randn_like(actions)
118	    x_t = (1 - time.view(B, 1, 1)) * actions + time.view(B, 1, 1) * noise
119	
120	    suffix_embs = model.model.embed_suffix(x_t, time)
121	
122	    scores = model.acis(suffix_embs, vis_tokens)
123	    N_vis = vis_tokens.shape[1]
124	    k = max(1, int(N_vis * model.k_ratio))
125	
126	    return scores, k
127	
128	
129	def perturb_images(batch: Dict[str, torch.Tensor], epsilon: float) -> Dict[str, torch.Tensor]:
130	    """Add Gaussian noise to image tensors in batch."""
131	    batch_noisy = {}
132	    for key, val in batch.items():
133	        if isinstance(val, torch.Tensor) and "image" in key.lower() and val.is_floating_point():
134	            batch_noisy[key] = (val + epsilon * torch.randn_like(val)).clamp(0, 1)
135	        else:
136	            batch_noisy[key] = val
137	    return batch_noisy
138	
139	
140	def estimate_lipschitz(model, dataloader, device: torch.device, max_batches: int = 10, num_samples: int = 100) -> float:
141	    """Estimate empirical Lipschitz constant of ACIS scorer."""
142	    if not hasattr(model, "acis"):
143	        return 0.0
144	
145	    L_max = 0.0
146	    for batch_idx, batch in enumerate(dataloader):
147	        if batch_idx >= max_batches:
148	            break
149	        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
150	
151	        vis_tokens = model.model.embed_image(batch["images"])
152	        actions = batch["actions"]
153	        B = actions.shape[0]
154	        time = torch.rand(B, device=actions.device, dtype=actions.dtype)
155	        noise = torch.randn_like(actions)
156	        x_t = (1 - time.view(B, 1, 1)) * actions + time.view(B, 1, 1) * noise
157	        a_query = model.model.embed_suffix(x_t, time)
158	
159	        L = compute_empirical_lipschitz(
160	            model.acis, vis_tokens, a_query,
161	            num_samples=num_samples, epsilon=0.001,
162	        )
163	        L_max = max(L_max, L)
164	
165	    log.info("Empirical Lipschitz constant: %.4f", L_max)
166	    return L_max
167	
168	
169	@torch.no_grad()
170	def evaluate_full(
171	    model,
172	    dataloader,
173	    config: Dict[str, Any],
174	    device: torch.device,
175	    imm_enabled: bool,
176	    lipschitz_const: float,
177	    max_batches: int = 100,
178	):
179	    """Full evaluation matrix: 4 noise levels x 2 pruning modes = 8 conditions."""
180	    eval_cfg = config.get("evaluation", {})
181	    epsilons = eval_cfg.get("perturbations", [0.0, 0.01, 0.02, 0.05])
182	    pruning_ratio = eval_cfg.get("pruning_ratio", 0.5)
183	
184	    results = {}
185	    action_losses = []
186	
187	    for epsilon in epsilons:
188	        for pruning in [False, True]:
189	            condition = f"eps{epsilon}_prune{pruning}"
190	            log.info("Evaluating condition: %s", condition)
191	
192	            all_margins = []
193	            all_preservation = []
194	            all_kendall = []
195	            all_certified = []
196	            all_led_ratio = []
197	            all_action_loss = []
198	
199	            for batch_idx, batch in enumerate(dataloader):
200	                if batch_idx >= max_batches:
201	                    break
202	                batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
203	
204	                # Clean scores
205	                scores_clean, k = compute_importance_scores(model, batch, imm_enabled)
206	
207	                if not imm_enabled:
208	                    if hasattr(model, "forward_baseline"):
209	                        loss, info = model.forward_baseline(batch)
210	                    else:
211	                        output = model(batch)
212	                        loss = output["loss"] if isinstance(output, dict) else (output[0] if isinstance(output, tuple) else output)
213	                        info = {}
214	                    loss_val = info.get("action_loss", loss)
215	                    all_action_loss.append(loss_val.item() if isinstance(loss_val, torch.Tensor) else loss_val)
216	                    continue
217	
218	                # Perturbed batch
219	                if epsilon > 0:
220	                    batch_noisy = perturb_images(batch, epsilon)
221	                    scores_pert, _ = compute_importance_scores(model, batch_noisy, imm_enabled)
222	                else:
223	                    scores_pert = scores_clean
224	
225	                # Metrics
226	                margin = compute_margin(scores_clean, k)
227	                pres = topk_preservation_rate(scores_clean, scores_pert, k)
228	                kendall = kendall_tau_distance(scores_clean, scores_pert, k)
229	                cert = certified_bound(margin, lipschitz_const, max(epsilon, 0.01), k)
230	                led = l_eps_delta_ratio(lipschitz_const, max(epsilon, 0.01), margin, k)
231	
232	                all_margins.append(margin.cpu())
233	                all_preservation.append(pres.cpu())
234	                all_kendall.append(kendall.cpu())
235	                all_certified.append(cert.cpu())
236	                all_led_ratio.append(led.cpu())
237	
238	                # Action loss under this condition
239	                if pruning:
240	                    model.train(False)
241	                    eval_batch = batch_noisy if epsilon > 0 else batch
242	                    _, info = model(eval_batch, step=0)
243	                    all_action_loss.append(info["action_loss"].item())
244	                else:
245	                    _, info = model(batch if epsilon == 0 else perturb_images(batch, epsilon), step=0)
246	                    all_action_loss.append(info["action_loss"].item())
247	
248	            cond_results = {
249	                "action_loss": sum(all_action_loss) / max(len(all_action_loss), 1),
250	            }
251	
252	            if imm_enabled and all_margins:
253	                margins_cat = torch.cat(all_margins)
254	                pres_cat = torch.cat(all_preservation)
255	                kendall_cat = torch.cat(all_kendall)
256	                cert_cat = torch.cat(all_certified)
257	                led_cat = torch.cat(all_led_ratio)
258	
259	                cond_results.update({
260	                    "margin_mean": margins_cat.mean().item(),
261	                    "margin_median": margins_cat.median().item(),
262	                    "margin_std": margins_cat.std().item(),
263	                    "margin_min": margins_cat.min().item(),
264	                    "margin_max": margins_cat.max().item(),
265	                    "preservation_rate": pres_cat.mean().item(),
266	                    "kendall_tau": kendall_cat.mean().item(),
267	                    "certified_bound_mean": cert_cat.mean().item(),
268	                    "certified_bound_max": cert_cat.max().item(),
269	                    "l_eps_delta_ratio_mean": led_cat.mean().item(),
270	                    "l_eps_delta_ratio_median": led_cat.median().item(),
271	                })
272	
273	            results[condition] = cond_results
274	            log.info("  %s: %s", condition, {k: f"{v:.4f}" for k, v in cond_results.items()})
275	
276	    return results
277	
278	
279	def main():
280	    args = parse_args()
281	
282	    import numpy as np
283	    import random
284	    random.seed(args.seed)
285	    np.random.seed(args.seed)
286	    torch.manual_seed(args.seed)
287	
288	    config = load_config(args.config)
289	    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
290	
291	    model, imm_enabled = load_model_and_checkpoint(config, args.checkpoint, device)
292	
293	    from train import load_dataset, make_dataloader
294	    dataset = load_dataset(config)
295	    dataloader = make_dataloader(dataset, {
296	        **config,
297	        "training": {**config.get("training", {}), "batch_size": config.get("training", {}).get("eval_batch_size", 4)},
298	    })
299	
300	    # Lipschitz estimation
301	    lipschitz_const = 0.0
302	    spectral_lipschitz = 0.0
303	    if imm_enabled and hasattr(model, "acis"):
304	        spectral_lipschitz = model.acis.get_lipschitz_estimate()
305	        log.info("Spectral Lipschitz estimate: %.4f", spectral_lipschitz)
306	        lipschitz_const = estimate_lipschitz(model, dataloader, device, max_batches=10, num_samples=args.lipschitz_samples)
307	
308	    results = evaluate_full(model, dataloader, config, device, imm_enabled, lipschitz_const, max_batches=args.max_batches)
309	
310	    results["_meta"] = {
311	        "checkpoint": args.checkpoint,
312	        "config": args.config,
313	        "imm_enabled": imm_enabled,
314	        "lipschitz_empirical": lipschitz_const,
315	        "lipschitz_spectral": spectral_lipschitz,
316	        "max_batches": args.max_batches,
317	        "seed": args.seed,
318	    }
319	
320	    # Summary: compare clean vs perturbed L*eps/Delta_k ratio
321	    if imm_enabled:
322	        clean_key = "eps0.0_pruneFalse"
323	        if clean_key in results and "l_eps_delta_ratio_mean" in results.get(clean_key, {}):
324	            log.info("=== Gate Metric Summary ===")
325	            for cond, data in results.items():
326	                if cond.startswith("_"):
327	                    continue
328	                led = data.get("l_eps_delta_ratio_mean", float("nan"))
329	                pres = data.get("preservation_rate", float("nan"))
330	                log.info("  %s: L*eps*k/Delta_k=%.4f, preservation=%.4f", cond, led, pres)
331	
332	    # Save results
333	    output_path = args.output
334	    if output_path is None:
335	        results_dir = Path("results")
336	        results_dir.mkdir(exist_ok=True)
337	        ckpt_name = Path(args.checkpoint).stem
338	        output_path = results_dir / f"eval_{ckpt_name}.json"
339	    else:
340	        output_path = Path(output_path)
341	        output_path.parent.mkdir(parents=True, exist_ok=True)
342	
343	    with open(output_path, "w") as f:
344	        json.dump(results, f, indent=2, default=str)
345	    log.info("Results saved to %s", output_path)
346	
347	
348	if __name__ == "__main__":
349	    main()
350	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "ab559dbc-af11-4ff9-8dc7-5817f62a3076",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/evaluate.py",
      "content": "\"\"\"IMM Evaluation Pipeline.\n\nEvaluates trained models under:\n  - Clean vs perturbed inputs (Gaussian noise eps in {0.01, 0.02, 0.05})\n  - With/without ACIS-based 50% token pruning\n  - Metrics: margin stats, top-k preservation rate, L*eps/Delta_k, Kendall tau, certified bound\n\nUsage:\n    python evaluate.py --checkpoint path/to/ckpt --config configs/imm_anchor.yaml --gpu 0\n    python evaluate.py --checkpoint path/to/baseline --config configs/baseline.yaml --output results/baseline.json\n\nDepends: lerobot, torch, imm.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport sys\nfrom pathlib import Path\nfrom typing import Any, Dict, List\n\nimport torch\nimport torch.nn.functional as F\nimport yaml\n\nARTIFACTS_DIR = Path(__file__).resolve().parent\nsys.path.insert(0, str(ARTIFACTS_DIR))\n\nfrom imm.metrics import (\n    certified_bound,\n    compute_empirical_lipschitz,\n    compute_margin,\n    kendall_tau_distance,\n    l_eps_delta_ratio,\n    margin_statistics,\n    topk_preservation_rate,\n)\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(description=\"IMM evaluation for SmolVLA on LIBERO\")\n    parser.add_argument(\"--checkpoint\", type=str, required=True, help=\"Path to checkpoint file or directory\")\n    parser.add_argument(\"--config\", type=str, required=True, help=\"Path to YAML config file\")\n    parser.add_argument(\"--gpu\", type=int, default=0, help=\"GPU index\")\n    parser.add_argument(\"--output\", type=str, default=None, help=\"Path to save results JSON (default: results/&lt;run>.json)\")\n    parser.add_argument(\"--max_batches\", type=int, default=100, help=\"Max batches to evaluate\")\n    parser.add_argument(\"--lipschitz_samples\", type=int, default=100, help=\"Samples for empirical Lipschitz estimation\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    return parser.parse_args()\n\n\ndef load_config(config_path: str) -> Dict[str, Any]:\n    \"\"\"Load YAML config with _base_ inheritance.\"\"\"\n    import copy\n    config_path = Path(config_path)\n    with open(config_path) as f:\n        config = yaml.safe_load(f)\n    if \"_base_\" in config:\n        base_path = config_path.parent / config.pop(\"_base_\")\n        base_config = load_config(str(base_path))\n        for k, v in config.items():\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\n                base_config[k].update(v)\n            else:\n                base_config[k] = v\n        return base_config\n    return config\n\n\ndef load_model_and_checkpoint(config: Dict[str, Any], checkpoint_path: str, device: torch.device):\n    \"\"\"Load SmolVLA policy, optionally wrap with IMM, then load checkpoint weights.\"\"\"\n    from train import load_smolvla_policy, wrap_with_imm\n\n    policy = load_smolvla_policy(config, device)\n    imm_enabled = config.get(\"imm\", {}).get(\"enabled\", False)\n\n    if imm_enabled:\n        model = wrap_with_imm(policy, config)\n        model.to(device)\n    else:\n        model = policy\n\n    ckpt_path = Path(checkpoint_path)\n    if ckpt_path.is_dir():\n        ckpt_path = ckpt_path / \"checkpoint.pt\"\n\n    log.info(\"Loading checkpoint from %s\", ckpt_path)\n    state = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model.load_state_dict(state[\"model_state_dict\"], strict=False)\n\n    model.eval()\n    return model, imm_enabled\n\n\ndef compute_importance_scores(model, batch: Dict[str, torch.Tensor], imm_enabled: bool):\n    \"\"\"Extract ACIS importance scores from the model.\n\n    Returns (scores, k) or (None, None) for baseline models.\n    \"\"\"\n    if not imm_enabled:\n        return None, None\n\n    vis_tokens = model.model.embed_image(batch[\"images\"])\n\n    actions = batch[\"actions\"]\n    B = actions.shape[0]\n    time = torch.rand(B, device=actions.device, dtype=actions.dtype)\n    noise = torch.randn_like(actions)\n    x_t = (1 - time.view(B, 1, 1)) * actions + time.view(B, 1, 1) * noise\n\n    suffix_embs = model.model.embed_suffix(x_t, time)\n\n    scores = model.acis(suffix_embs, vis_tokens)\n    N_vis = vis_tokens.shape[1]\n    k = max(1, int(N_vis * model.k_ratio))\n\n    return scores, k\n\n\ndef perturb_images(batch: Dict[str, torch.Tensor], epsilon: float) -> Dict[str, torch.Tensor]:\n    \"\"\"Add Gaussian noise to image tensors in batch.\"\"\"\n    batch_noisy = {}\n    for key, val in batch.items():\n        if isinstance(val, torch.Tensor) and \"image\" in key.lower() and val.is_floating_point():\n            batch_noisy[key] = (val + epsilon * torch.randn_like(val)).clamp(0, 1)\n        else:\n            batch_noisy[key] = val\n    return batch_noisy\n\n\ndef estimate_lipschitz(model, dataloader, device: torch.device, max_batches: int = 10, num_samples: int = 100) -> float:\n    \"\"\"Estimate empirical Lipschitz constant of ACIS scorer.\"\"\"\n    if not hasattr(model, \"acis\"):\n        return 0.0\n\n    L_max = 0.0\n    for batch_idx, batch in enumerate(dataloader):\n        if batch_idx >= max_batches:\n            break\n        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}\n\n        vis_tokens = model.model.embed_image(batch[\"images\"])\n        actions = batch[\"actions\"]\n        B = actions.shape[0]\n        time = torch.rand(B, device=actions.device, dtype=actions.dtype)\n        noise = torch.randn_like(actions)\n        x_t = (1 - time.view(B, 1, 1)) * actions + time.view(B, 1, 1) * noise\n        a_query = model.model.embed_suffix(x_t, time)\n\n        L = compute_empirical_lipschitz(\n            model.acis, vis_tokens, a_query,\n            num_samples=num_samples, epsilon=0.001,\n        )\n        L_max = max(L_max, L)\n\n    log.info(\"Empirical Lipschitz constant: %.4f\", L_max)\n    return L_max\n\n\n@torch.no_grad()\ndef evaluate_full(\n    model,\n    dataloader,\n    config: Dict[str, Any],\n    device: torch.device,\n    imm_enabled: bool,\n    lipschitz_const: float,\n    max_batches: int = 100,\n):\n    \"\"\"Full evaluation matrix: 4 noise levels x 2 pruning modes = 8 conditions.\"\"\"\n    eval_cfg = config.get(\"evaluation\", {})\n    epsilons = eval_cfg.get(\"perturbations\", [0.0, 0.01, 0.02, 0.05])\n    pruning_ratio = eval_cfg.get(\"pruning_ratio\", 0.5)\n\n    results = {}\n    action_losses = []\n\n    for epsilon in epsilons:\n        for pruning in [False, True]:\n            condition = f\"eps{epsilon}_prune{pruning}\"\n            log.info(\"Evaluating condition: %s\", condition)\n\n            all_margins = []\n            all_preservation = []\n            all_kendall = []\n            all_certified = []\n            all_led_ratio = []\n            all_action_loss = []\n\n            for batch_idx, batch in enumerate(dataloader):\n                if batch_idx >= max_batches:\n                    break\n                batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}\n\n                # Clean scores\n                scores_clean, k = compute_importance_scores(model, batch, imm_enabled)\n\n                if not imm_enabled:\n                    if hasattr(model, \"forward_baseline\"):\n                        loss, info = model.forward_baseline(batch)\n                    else:\n                        output = model(batch)\n                        loss = output[\"loss\"] if isinstance(output, dict) else (output[0] if isinstance(output, tuple) else output)\n                        info = {}\n                    loss_val = info.get(\"action_loss\", loss)\n                    all_action_loss.append(loss_val.item() if isinstance(loss_val, torch.Tensor) else loss_val)\n                    continue\n\n                # Perturbed batch\n                if epsilon > 0:\n                    batch_noisy = perturb_images(batch, epsilon)\n                    scores_pert, _ = compute_importance_scores(model, batch_noisy, imm_enabled)\n                else:\n                    scores_pert = scores_clean\n\n                # Metrics\n                margin = compute_margin(scores_clean, k)\n                pres = topk_preservation_rate(scores_clean, scores_pert, k)\n                kendall = kendall_tau_distance(scores_clean, scores_pert, k)\n                cert = certified_bound(margin, lipschitz_const, max(epsilon, 0.01), k)\n                led = l_eps_delta_ratio(lipschitz_const, max(epsilon, 0.01), margin, k)\n\n                all_margins.append(margin.cpu())\n                all_preservation.append(pres.cpu())\n                all_kendall.append(kendall.cpu())\n                all_certified.append(cert.cpu())\n                all_led_ratio.append(led.cpu())\n\n                # Action loss under this condition\n                if pruning:\n                    model.train(False)\n                    eval_batch = batch_noisy if epsilon > 0 else batch\n                    _, info = model(eval_batch, step=0)\n                    all_action_loss.append(info[\"action_loss\"].item())\n                else:\n                    _, info = model(batch if epsilon == 0 else perturb_images(batch, epsilon), step=0)\n                    all_action_loss.append(info[\"action_loss\"].item())\n\n            cond_results = {\n                \"action_loss\": sum(all_action_loss) / max(len(all_action_loss), 1),\n            }\n\n            if imm_enabled and all_margins:\n                margins_cat = torch.cat(all_margins)\n                pres_cat = torch.cat(all_preservation)\n                kendall_cat = torch.cat(all_kendall)\n                cert_cat = torch.cat(all_certified)\n                led_cat = torch.cat(all_led_ratio)\n\n                cond_results.update({\n                    \"margin_mean\": margins_cat.mean().item(),\n                    \"margin_median\": margins_cat.median().item(),\n                    \"margin_std\": margins_cat.std().item(),\n                    \"margin_min\": margins_cat.min().item(),\n                    \"margin_max\": margins_cat.max().item(),\n                    \"preservation_rate\": pres_cat.mean().item(),\n                    \"kendall_tau\": kendall_cat.mean().item(),\n                    \"certified_bound_mean\": cert_cat.mean().item(),\n                    \"certified_bound_max\": cert_cat.max().item(),\n                    \"l_eps_delta_ratio_mean\": led_cat.mean().item(),\n                    \"l_eps_delta_ratio_median\": led_cat.median().item(),\n                })\n\n            results[condition] = cond_results\n            log.info(\"  %s: %s\", condition, {k: f\"{v:.4f}\" for k, v in cond_results.items()})\n\n    return results\n\n\ndef main():\n    args = parse_args()\n\n    import numpy as np\n    import random\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    config = load_config(args.config)\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n\n    model, imm_enabled = load_model_and_checkpoint(config, args.checkpoint, device)\n\n    from train import load_dataset, make_dataloader\n    dataset = load_dataset(config)\n    dataloader = make_dataloader(dataset, {\n        **config,\n        \"training\": {**config.get(\"training\", {}), \"batch_size\": config.get(\"training\", {}).get(\"eval_batch_size\", 4)},\n    })\n\n    # Lipschitz estimation\n    lipschitz_const = 0.0\n    spectral_lipschitz = 0.0\n    if imm_enabled and hasattr(model, \"acis\"):\n        spectral_lipschitz = model.acis.get_lipschitz_estimate()\n        log.info(\"Spectral Lipschitz estimate: %.4f\", spectral_lipschitz)\n        lipschitz_const = estimate_lipschitz(model, dataloader, device, max_batches=10, num_samples=args.lipschitz_samples)\n\n    results = evaluate_full(model, dataloader, config, device, imm_enabled, lipschitz_const, max_batches=args.max_batches)\n\n    results[\"_meta\"] = {\n        \"checkpoint\": args.checkpoint,\n        \"config\": args.config,\n        \"imm_enabled\": imm_enabled,\n        \"lipschitz_empirical\": lipschitz_const,\n        \"lipschitz_spectral\": spectral_lipschitz,\n        \"max_batches\": args.max_batches,\n        \"seed\": args.seed,\n    }\n\n    # Summary: compare clean vs perturbed L*eps/Delta_k ratio\n    if imm_enabled:\n        clean_key = \"eps0.0_pruneFalse\"\n        if clean_key in results and \"l_eps_delta_ratio_mean\" in results.get(clean_key, {}):\n            log.info(\"=== Gate Metric Summary ===\")\n            for cond, data in results.items():\n                if cond.startswith(\"_\"):\n                    continue\n                led = data.get(\"l_eps_delta_ratio_mean\", float(\"nan\"))\n                pres = data.get(\"preservation_rate\", float(\"nan\"))\n                log.info(\"  %s: L*eps*k/Delta_k=%.4f, preservation=%.4f\", cond, led, pres)\n\n    # Save results\n    output_path = args.output\n    if output_path is None:\n        results_dir = Path(\"results\")\n        results_dir.mkdir(exist_ok=True)\n        ckpt_name = Path(args.checkpoint).stem\n        output_path = results_dir / f\"eval_{ckpt_name}.json\"\n    else:\n        output_path = Path(output_path)\n        output_path.parent.mkdir(parents=True, exist_ok=True)\n\n    with open(output_path, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n    log.info(\"Results saved to %s\", output_path)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 350,
      "startLine": 1,
      "totalLines": 350
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the existing modules that I should NOT modify, and the train.py to understand how the wrapper is called. Then I'll clone lerobot to study the real API.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "2fa5508e-5c4d-4a43-9797-a72c84742a3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wu8dgR6bbmbjWJ1duWVXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17968
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

_source line 12_

Let me read the other key files and clone lerobot in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "568ea49f-4873-47a8-ada1-2b3ef71593b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wu8dgR6bbmbjWJ1duWVXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17968
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01Nqg2qpbnA5KUpnrrh9UjXE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/acis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "60e21001-2ca4-4b8b-9b9f-a8e328be366c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wu8dgR6bbmbjWJ1duWVXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17968
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

_source line 14 · 2026-05-15T12:03:44.272Z_

<details><summary>↩ Tool result · `toolu_01Nqg2qpbnA5KUpnrrh9UjXE`</summary>

```text
1	"""Action-Conditioned Importance Scoring (ACIS).
2	
3	Cross-attention scorer: a_query (action representations) attend to visual tokens,
4	producing per-token importance scores. All linear layers are wrapped with spectral
5	normalization to control the module's Lipschitz constant, which is required for
6	the certified bound k·ε·L/Δ_k to be meaningful.
7	
8	Inputs:  a_query (B, Q, action_dim), visual_tokens (B, N, visual_dim).
9	Outputs: importance_scores (B, N).
10	Depends: torch, spectral_norm.
11	"""
12	
13	from __future__ import annotations
14	
15	import torch
16	import torch.nn as nn
17	from torch import Tensor
18	from torch.nn.utils import spectral_norm
19	from typing import Tuple
20	
21	
22	class ACIS(nn.Module):
23	    def __init__(
24	        self,
25	        visual_dim: int = 960,
26	        action_dim: int = 720,
27	        num_heads: int = 8,
28	        dropout: float = 0.0,
29	    ):
30	        super().__init__()
31	        assert visual_dim % num_heads == 0
32	        self.visual_dim = visual_dim
33	        self.num_heads = num_heads
34	        self.head_dim = visual_dim // num_heads
35	        self.scale = self.head_dim ** -0.5
36	
37	        self.query_proj = spectral_norm(nn.Linear(action_dim, visual_dim))
38	        self.q_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))
39	        self.k_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))
40	        self.v_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))
41	        self.score_head = spectral_norm(nn.Linear(visual_dim, 1))
42	        self.dropout = nn.Dropout(dropout)
43	
44	    def forward(self, a_query: Tensor, visual_tokens: Tensor) -> Tensor:
45	        """
46	        Args:
47	            a_query: (B, Q, action_dim) action representations from embed_suffix.
48	            visual_tokens: (B, N, visual_dim) visual tokens from embed_image.
49	        Returns:
50	            importance_scores: (B, N) per-token scores.
51	        """
52	        B, N, _ = visual_tokens.shape
53	        Q = a_query.shape[1]
54	        H, d = self.num_heads, self.head_dim
55	
56	        q = self.q_proj(self.query_proj(a_query))       # (B, Q, D)
57	        k = self.k_proj(visual_tokens)                   # (B, N, D)
58	        v = self.v_proj(visual_tokens)                   # (B, N, D)
59	
60	        q = q.view(B, Q, H, d).transpose(1, 2)          # (B, H, Q, d)
61	        k = k.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)
62	        v = v.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)
63	
64	        attn_weights = torch.matmul(q, k.transpose(-2, -1)) * self.scale  # (B, H, Q, N)
65	        attn_weights = attn_weights.softmax(dim=-1)
66	        attn_weights = self.dropout(attn_weights)
67	
68	        # Per-visual-token importance: average attention received across queries and heads
69	        token_importance = attn_weights.mean(dim=(1, 2))  # (B, N)
70	
71	        # Contextual representation per visual token via transposed attention
72	        # v^T @ attn^T → each visual token gets a context vector
73	        attn_t = attn_weights.transpose(-2, -1)           # (B, H, N, Q)
74	        context = torch.matmul(attn_t, q)                 # (B, H, N, d)
75	        context = context.transpose(1, 2).reshape(B, N, self.visual_dim)  # (B, N, D)
76	
77	        score_logits = self.score_head(context).squeeze(-1)  # (B, N)
78	
79	        # Combine learned score with attention-based importance
80	        importance_scores = score_logits + token_importance
81	
82	        return importance_scores
83	
84	    def get_lipschitz_estimate(self) -> float:
85	        """Product of spectral norms across all SN-wrapped layers."""
86	        L = 1.0
87	        for module in self.modules():
88	            if hasattr(module, "weight_orig"):
89	                sigma = torch.linalg.norm(module.weight, ord=2).item()
90	                L *= sigma
91	        return L
92	
93	
94	if __name__ == "__main__":
95	    torch.manual_seed(42)
96	    B, N, Q = 2, 128, 50
97	    vis = torch.randn(B, N, 960)
98	    a_q = torch.randn(B, Q, 720)
99	
100	    acis = ACIS(visual_dim=960, action_dim=720)
101	    scores = acis(a_q, vis)
102	    print(f"ACIS: scores shape={scores.shape}, range=[{scores.min():.3f}, {scores.max():.3f}]")
103	
104	    L = acis.get_lipschitz_estimate()
105	    print(f"Lipschitz estimate: {L:.4f}")
106	
107	    scores.sum().backward()
108	    print(f"ACIS grad OK: query_proj={acis.query_proj.weight_orig.grad is not None}")
109	    print("All ACIS tests passed!")
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "6990bbc5-4abc-40f0-85ad-045123b6e446",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/acis.py",
      "content": "\"\"\"Action-Conditioned Importance Scoring (ACIS).\n\nCross-attention scorer: a_query (action representations) attend to visual tokens,\nproducing per-token importance scores. All linear layers are wrapped with spectral\nnormalization to control the module's Lipschitz constant, which is required for\nthe certified bound k·ε·L/Δ_k to be meaningful.\n\nInputs:  a_query (B, Q, action_dim), visual_tokens (B, N, visual_dim).\nOutputs: importance_scores (B, N).\nDepends: torch, spectral_norm.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nfrom torch import Tensor\nfrom torch.nn.utils import spectral_norm\nfrom typing import Tuple\n\n\nclass ACIS(nn.Module):\n    def __init__(\n        self,\n        visual_dim: int = 960,\n        action_dim: int = 720,\n        num_heads: int = 8,\n        dropout: float = 0.0,\n    ):\n        super().__init__()\n        assert visual_dim % num_heads == 0\n        self.visual_dim = visual_dim\n        self.num_heads = num_heads\n        self.head_dim = visual_dim // num_heads\n        self.scale = self.head_dim ** -0.5\n\n        self.query_proj = spectral_norm(nn.Linear(action_dim, visual_dim))\n        self.q_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))\n        self.k_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))\n        self.v_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))\n        self.score_head = spectral_norm(nn.Linear(visual_dim, 1))\n        self.dropout = nn.Dropout(dropout)\n\n    def forward(self, a_query: Tensor, visual_tokens: Tensor) -> Tensor:\n        \"\"\"\n        Args:\n            a_query: (B, Q, action_dim) action representations from embed_suffix.\n            visual_tokens: (B, N, visual_dim) visual tokens from embed_image.\n        Returns:\n            importance_scores: (B, N) per-token scores.\n        \"\"\"\n        B, N, _ = visual_tokens.shape\n        Q = a_query.shape[1]\n        H, d = self.num_heads, self.head_dim\n\n        q = self.q_proj(self.query_proj(a_query))       # (B, Q, D)\n        k = self.k_proj(visual_tokens)                   # (B, N, D)\n        v = self.v_proj(visual_tokens)                   # (B, N, D)\n\n        q = q.view(B, Q, H, d).transpose(1, 2)          # (B, H, Q, d)\n        k = k.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)\n        v = v.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)\n\n        attn_weights = torch.matmul(q, k.transpose(-2, -1)) * self.scale  # (B, H, Q, N)\n        attn_weights = attn_weights.softmax(dim=-1)\n        attn_weights = self.dropout(attn_weights)\n\n        # Per-visual-token importance: average attention received across queries and heads\n        token_importance = attn_weights.mean(dim=(1, 2))  # (B, N)\n\n        # Contextual representation per visual token via transposed attention\n        # v^T @ attn^T → each visual token gets a context vector\n        attn_t = attn_weights.transpose(-2, -1)           # (B, H, N, Q)\n        context = torch.matmul(attn_t, q)                 # (B, H, N, d)\n        context = context.transpose(1, 2).reshape(B, N, self.visual_dim)  # (B, N, D)\n\n        score_logits = self.score_head(context).squeeze(-1)  # (B, N)\n\n        # Combine learned score with attention-based importance\n        importance_scores = score_logits + token_importance\n\n        return importance_scores\n\n    def get_lipschitz_estimate(self) -> float:\n        \"\"\"Product of spectral norms across all SN-wrapped layers.\"\"\"\n        L = 1.0\n        for module in self.modules():\n            if hasattr(module, \"weight_orig\"):\n                sigma = torch.linalg.norm(module.weight, ord=2).item()\n                L *= sigma\n        return L\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B, N, Q = 2, 128, 50\n    vis = torch.randn(B, N, 960)\n    a_q = torch.randn(B, Q, 720)\n\n    acis = ACIS(visual_dim=960, action_dim=720)\n    scores = acis(a_q, vis)\n    print(f\"ACIS: scores shape={scores.shape}, range=[{scores.min():.3f}, {scores.max():.3f}]\")\n\n    L = acis.get_lipschitz_estimate()\n    print(f\"Lipschitz estimate: {L:.4f}\")\n\n    scores.sum().backward()\n    print(f\"ACIS grad OK: query_proj={acis.query_proj.weight_orig.grad is not None}\")\n    print(\"All ACIS tests passed!\")\n",
      "numLines": 110,
      "startLine": 1,
      "totalLines": 110
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_011thMbCAuUqUfSB21MD9jSV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/losses.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "9c125d51-c5e2-4d06-aebc-e6d02f439239",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wu8dgR6bbmbjWJ1duWVXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17968
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

_source line 16 · 2026-05-15T12:03:44.771Z_

<details><summary>↩ Tool result · `toolu_011thMbCAuUqUfSB21MD9jSV`</summary>

```text
1	"""Importance Margin Maximization losses.
2	
3	MarginMaximizationLoss: hinge loss  max(0, delta - (s_{(k)} - s_{(k+1)})).
4	IMMTotalLoss:           L_action + lambda * L_margin  with linear lambda warmup.
5	
6	Inputs:  (B, N) importance scores, integer k.
7	Depends: soft_topk.SoftTopK.
8	"""
9	
10	from __future__ import annotations
11	
12	import torch
13	import torch.nn as nn
14	from torch import Tensor
15	from typing import Dict, Tuple
16	
17	from .soft_topk import SoftTopK
18	
19	
20	class MarginMaximizationLoss(nn.Module):
21	    """Hinge loss: L_margin = mean(max(0, delta - (s_{(k)} - s_{(k+1)})))."""
22	
23	    def __init__(self, delta: float = 1.0, temperature: float = 1.0, method: str = "sigmoid"):
24	        super().__init__()
25	        self.delta = delta
26	        self.soft_topk = SoftTopK(temperature=temperature, method=method)
27	
28	    def forward(self, importance_scores: Tensor, k: int) -> Tuple[Tensor, Dict[str, Tensor]]:
29	        """
30	        Args:
31	            importance_scores: (B, N) per-token importance scores.
32	            k: number of tokens to retain.
33	        Returns:
34	            loss: scalar hinge loss.
35	            info: dict with margin, s_k, s_k_plus_1, mask for logging.
36	        """
37	        mask, s_k, s_k_plus_1 = self.soft_topk(importance_scores, k)
38	
39	        margin = s_k - s_k_plus_1  # (B,)
40	        hinge = torch.clamp(self.delta - margin, min=0.0)  # (B,)
41	        loss = hinge.mean()
42	
43	        info = {
44	            "margin": margin.detach(),
45	            "s_k": s_k.detach(),
46	            "s_k_plus_1": s_k_plus_1.detach(),
47	            "hinge": hinge.detach(),
48	            "mask": mask.detach(),
49	        }
50	        return loss, info
51	
52	
53	class IMMTotalLoss(nn.Module):
54	    """L_total = L_action + lambda * L_margin, with linear lambda warmup."""
55	
56	    def __init__(
57	        self,
58	        lambda_margin: float = 0.1,
59	        delta: float = 1.0,
60	        warmup_steps: int = 1000,
61	        temperature: float = 1.0,
62	        method: str = "sigmoid",
63	    ):
64	        super().__init__()
65	        self.lambda_margin = lambda_margin
66	        self.warmup_steps = warmup_steps
67	        self.margin_loss = MarginMaximizationLoss(delta=delta, temperature=temperature, method=method)
68	
69	    def _get_lambda(self, step: int) -> float:
70	        if self.warmup_steps <= 0:
71	            return self.lambda_margin
72	        return self.lambda_margin * min(1.0, step / self.warmup_steps)
73	
74	    def forward(
75	        self, action_loss: Tensor, importance_scores: Tensor, k: int, step: int
76	    ) -> Tuple[Tensor, Dict[str, Tensor]]:
77	        """
78	        Args:
79	            action_loss: scalar task loss (e.g. action prediction).
80	            importance_scores: (B, N).
81	            k: retention count.
82	            step: current training step (for warmup).
83	        Returns:
84	            total_loss: scalar.
85	            info: dict with all sub-losses and diagnostics.
86	        """
87	        lam = self._get_lambda(step)
88	        margin_loss, margin_info = self.margin_loss(importance_scores, k)
89	        total = action_loss + lam * margin_loss
90	
91	        info = {
92	            **margin_info,
93	            "action_loss": action_loss.detach(),
94	            "margin_loss": margin_loss.detach(),
95	            "total_loss": total.detach(),
96	            "lambda": torch.tensor(lam),
97	        }
98	        return total, info
99	
100	
101	if __name__ == "__main__":
102	    torch.manual_seed(42)
103	    B, N, k = 4, 64, 16
104	    scores = torch.randn(B, N, requires_grad=True)
105	    action_loss = torch.tensor(1.5, requires_grad=True)
106	
107	    mmr = MarginMaximizationLoss(delta=0.5, temperature=0.5)
108	    loss, info = mmr(scores, k)
109	    loss.backward()
110	    print(f"MMR: loss={loss.item():.4f}, margin_mean={info['margin'].mean().item():.4f}, "
111	          f"grad OK={scores.grad is not None}")
112	    scores.grad = None
113	
114	    total_loss_fn = IMMTotalLoss(lambda_margin=0.1, delta=0.5, warmup_steps=100, temperature=0.5)
115	    total, tinfo = total_loss_fn(action_loss, scores, k, step=50)
116	    total.backward()
117	    print(f"Total: loss={total.item():.4f}, lambda={tinfo['lambda'].item():.4f}, "
118	          f"grad OK={scores.grad is not None}")
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "bd864ce2-eacb-42c6-b5f5-85f72c569fb7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/losses.py",
      "content": "\"\"\"Importance Margin Maximization losses.\n\nMarginMaximizationLoss: hinge loss  max(0, delta - (s_{(k)} - s_{(k+1)})).\nIMMTotalLoss:           L_action + lambda * L_margin  with linear lambda warmup.\n\nInputs:  (B, N) importance scores, integer k.\nDepends: soft_topk.SoftTopK.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nfrom torch import Tensor\nfrom typing import Dict, Tuple\n\nfrom .soft_topk import SoftTopK\n\n\nclass MarginMaximizationLoss(nn.Module):\n    \"\"\"Hinge loss: L_margin = mean(max(0, delta - (s_{(k)} - s_{(k+1)}))).\"\"\"\n\n    def __init__(self, delta: float = 1.0, temperature: float = 1.0, method: str = \"sigmoid\"):\n        super().__init__()\n        self.delta = delta\n        self.soft_topk = SoftTopK(temperature=temperature, method=method)\n\n    def forward(self, importance_scores: Tensor, k: int) -> Tuple[Tensor, Dict[str, Tensor]]:\n        \"\"\"\n        Args:\n            importance_scores: (B, N) per-token importance scores.\n            k: number of tokens to retain.\n        Returns:\n            loss: scalar hinge loss.\n            info: dict with margin, s_k, s_k_plus_1, mask for logging.\n        \"\"\"\n        mask, s_k, s_k_plus_1 = self.soft_topk(importance_scores, k)\n\n        margin = s_k - s_k_plus_1  # (B,)\n        hinge = torch.clamp(self.delta - margin, min=0.0)  # (B,)\n        loss = hinge.mean()\n\n        info = {\n            \"margin\": margin.detach(),\n            \"s_k\": s_k.detach(),\n            \"s_k_plus_1\": s_k_plus_1.detach(),\n            \"hinge\": hinge.detach(),\n            \"mask\": mask.detach(),\n        }\n        return loss, info\n\n\nclass IMMTotalLoss(nn.Module):\n    \"\"\"L_total = L_action + lambda * L_margin, with linear lambda warmup.\"\"\"\n\n    def __init__(\n        self,\n        lambda_margin: float = 0.1,\n        delta: float = 1.0,\n        warmup_steps: int = 1000,\n        temperature: float = 1.0,\n        method: str = \"sigmoid\",\n    ):\n        super().__init__()\n        self.lambda_margin = lambda_margin\n        self.warmup_steps = warmup_steps\n        self.margin_loss = MarginMaximizationLoss(delta=delta, temperature=temperature, method=method)\n\n    def _get_lambda(self, step: int) -> float:\n        if self.warmup_steps <= 0:\n            return self.lambda_margin\n        return self.lambda_margin * min(1.0, step / self.warmup_steps)\n\n    def forward(\n        self, action_loss: Tensor, importance_scores: Tensor, k: int, step: int\n    ) -> Tuple[Tensor, Dict[str, Tensor]]:\n        \"\"\"\n        Args:\n            action_loss: scalar task loss (e.g. action prediction).\n            importance_scores: (B, N).\n            k: retention count.\n            step: current training step (for warmup).\n        Returns:\n            total_loss: scalar.\n            info: dict with all sub-losses and diagnostics.\n        \"\"\"\n        lam = self._get_lambda(step)\n        margin_loss, margin_info = self.margin_loss(importance_scores, k)\n        total = action_loss + lam * margin_loss\n\n        info = {\n            **margin_info,\n            \"action_loss\": action_loss.detach(),\n            \"margin_loss\": margin_loss.detach(),\n            \"total_loss\": total.detach(),\n            \"lambda\": torch.tensor(lam),\n        }\n        return total, info\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B, N, k = 4, 64, 16\n    scores = torch.randn(B, N, requires_grad=True)\n    action_loss = torch.tensor(1.5, requires_grad=True)\n\n    mmr = MarginMaximizationLoss(delta=0.5, temperature=0.5)\n    loss, info = mmr(scores, k)\n    loss.backward()\n    print(f\"MMR: loss={loss.item():.4f}, margin_mean={info['margin'].mean().item():.4f}, \"\n          f\"grad OK={scores.grad is not None}\")\n    scores.grad = None\n\n    total_loss_fn = IMMTotalLoss(lambda_margin=0.1, delta=0.5, warmup_steps=100, temperature=0.5)\n    total, tinfo = total_loss_fn(action_loss, scores, k, step=50)\n    total.backward()\n    print(f\"Total: loss={total.item():.4f}, lambda={tinfo['lambda'].item():.4f}, \"\n          f\"grad OK={scores.grad is not None}\")\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01CDNjDFRAKAEK1KQjGosUX3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/token_selection.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "e3ec15db-babf-4900-86b1-c69b0e4d349d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wu8dgR6bbmbjWJ1duWVXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17968
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

_source line 18 · 2026-05-15T12:03:45.750Z_

<details><summary>↩ Tool result · `toolu_01CDNjDFRAKAEK1KQjGosUX3`</summary>

```text
1	"""Margin-aware token selection: soft masking (train) / hard prune+merge (inference).
2	
3	Training: applies soft sigmoid mask to visual tokens (fully differentiable).
4	Inference: three-partition — preserve (top-k), prune (bottom), merge (borderline) —
5	           borderline tokens are weighted-averaged into their nearest preserved token.
6	
7	Inputs:  (B, N) scores, (B, N, D) visual tokens, integer k.
8	Depends: soft_topk.SoftTopK.
9	"""
10	
11	from __future__ import annotations
12	
13	import torch
14	import torch.nn as nn
15	import torch.nn.functional as F
16	from torch import Tensor
17	from typing import Dict, Tuple, Optional
18	
19	from .soft_topk import SoftTopK
20	
21	
22	class MarginAwareTokenSelector(nn.Module):
23	    def __init__(self, temperature: float = 1.0, merge_weight_temp: float = 0.5):
24	        super().__init__()
25	        self.soft_topk = SoftTopK(temperature=temperature, method="sigmoid")
26	        self.merge_weight_temp = merge_weight_temp
27	
28	    def forward(
29	        self,
30	        importance_scores: Tensor,
31	        visual_tokens: Tensor,
32	        k: int,
33	        training: bool = True,
34	    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:
35	        """
36	        Args:
37	            importance_scores: (B, N) per-token scores.
38	            visual_tokens:     (B, N, D) visual token embeddings.
39	            k: number of tokens to retain.
40	            training: soft mask (True) or hard prune/merge (False).
41	        Returns:
42	            selected_tokens: (B, N, D) soft-masked  or  (B, K', D) hard-selected.
43	            selection_mask:  (B, N) soft or binary mask.
44	            info: dict with diagnostic stats.
45	        """
46	        if training:
47	            return self._soft_forward(importance_scores, visual_tokens, k)
48	        return self._hard_forward(importance_scores, visual_tokens, k)
49	
50	    # ------------------------------------------------------------------
51	    def _soft_forward(
52	        self, scores: Tensor, tokens: Tensor, k: int
53	    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:
54	        mask, s_k, s_k1 = self.soft_topk(scores, k)
55	        selected = tokens * mask.unsqueeze(-1)  # (B, N, D)
56	        info = {
57	            "mode": torch.tensor(0),  # 0 = soft
58	            "mask_sum": mask.sum(-1).detach(),
59	            "margin": (s_k - s_k1).detach(),
60	        }
61	        return selected, mask, info
62	
63	    # ------------------------------------------------------------------
64	    def _hard_forward(
65	        self, scores: Tensor, tokens: Tensor, k: int
66	    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:
67	        B, N, D = tokens.shape
68	
69	        sorted_scores, sorted_idx = torch.sort(scores, dim=-1, descending=True)
70	        s_k = sorted_scores[:, k - 1]          # (B,) k-th largest score
71	        s_k_plus_1 = sorted_scores[:, k]       # (B,) (k+1)-th largest score
72	        delta_k = s_k - s_k_plus_1             # (B,) margin
73	
74	        threshold_high = (s_k + delta_k / 2).unsqueeze(-1)   # (B, 1)
75	        threshold_low = (s_k - delta_k / 2).unsqueeze(-1)    # (B, 1)
76	
77	        # Fixed top-k as preserved tokens (output length stays k)
78	        preserve_idx = sorted_idx[:, :k]                                 # (B, k)
79	        preserved_tokens = torch.gather(tokens, 1, preserve_idx.unsqueeze(-1).expand(-1, -1, D))
80	
81	        is_topk = torch.zeros(B, N, device=scores.device, dtype=torch.bool)
82	        is_topk.scatter_(1, preserve_idx, True)
83	
84	        # Margin-aware three-partition for non-top-k tokens
85	        borderline_mask = ~is_topk & (scores >= threshold_low.squeeze(-1)) & (scores <= threshold_high.squeeze(-1))
86	        prune_mask = ~is_topk & (scores < threshold_low.squeeze(-1))
87	        preserve_mask = is_topk
88	
89	        # Merge borderline tokens into nearest preserved token
90	        merged_tokens = self._merge_borderline_tokens(
91	            tokens, scores, preserved_tokens, preserve_idx, borderline_mask
92	        )
93	
94	        binary_mask = preserve_mask.float()
95	        info = {
96	            "mode": torch.tensor(1),  # 1 = hard
97	            "num_preserved": preserve_mask.sum(-1).float().detach(),
98	            "num_pruned": prune_mask.sum(-1).float().detach(),
99	            "num_merged": borderline_mask.sum(-1).float().detach(),
100	            "delta_k": delta_k.detach(),
101	        }
102	        return merged_tokens, binary_mask, info
103	
104	    # ------------------------------------------------------------------
105	    def _merge_borderline_tokens(
106	        self,
107	        tokens: Tensor,
108	        scores: Tensor,
109	        preserved_tokens: Tensor,
110	        preserve_idx: Tensor,
111	        borderline_mask: Tensor,
112	    ) -> Tensor:
113	        """Weighted-merge each borderline token into cosine-nearest preserved token."""
114	        B, N, D = tokens.shape
115	        K = preserved_tokens.shape[1]
116	
117	        num_borderline = borderline_mask.sum(-1)  # (B,)
118	        if num_borderline.sum() == 0:
119	            return preserved_tokens
120	
121	        # Cosine similarity: borderline -> preserved
122	        preserved_norm = F.normalize(preserved_tokens, dim=-1)  # (B, K, D)
123	        tokens_norm = F.normalize(tokens, dim=-1)               # (B, N, D)
124	
125	        # Similarity of all tokens to preserved tokens: (B, N, K)
126	        sim = torch.bmm(tokens_norm, preserved_norm.transpose(1, 2))
127	
128	        # For each borderline token, find best preserved match
129	        best_match = sim.argmax(dim=-1)  # (B, N) — index into K
130	
131	        # Importance-based merge weights
132	        preserve_scores = torch.gather(scores, 1, preserve_idx)  # (B, K)
133	
134	        merged = preserved_tokens.clone()
135	        # TODO: vectorize this loop for better GPU efficiency
136	        for b in range(B):
137	            border_idx = borderline_mask[b].nonzero(as_tuple=True)[0]
138	            if border_idx.numel() == 0:
139	                continue
140	            for idx in border_idx:
141	                target = best_match[b, idx].item()
142	                w_border = torch.sigmoid(scores[b, idx] / (self.merge_weight_temp + 1e-8))
143	                w_orig = torch.sigmoid(preserve_scores[b, target] / (self.merge_weight_temp + 1e-8))
144	                total_w = w_orig + w_border + 1e-8
145	                merged[b, target] = (w_orig / total_w) * merged[b, target] + (w_border / total_w) * tokens[b, idx]
146	
147	        return merged
148	
149	
150	if __name__ == "__main__":
151	    torch.manual_seed(42)
152	    B, N, D, k = 2, 32, 64, 8
153	    scores = torch.randn(B, N, requires_grad=True)
154	    tokens = torch.randn(B, N, D)
155	
156	    selector = MarginAwareTokenSelector(temperature=0.5)
157	
158	    # Training mode
159	    sel_train, mask_train, info_train = selector(scores, tokens, k, training=True)
160	    sel_train.sum().backward()
161	    print(f"[train] shape={sel_train.shape}, mask_sum={info_train['mask_sum']}, "
162	          f"grad OK={scores.grad is not None}")
163	    scores.grad = None
164	
165	    # Inference mode
166	    with torch.no_grad():
167	        sel_inf, mask_inf, info_inf = selector(scores, tokens, k, training=False)
168	    print(f"[infer] shape={sel_inf.shape}, preserved={info_inf['num_preserved']}, "
169	          f"pruned={info_inf['num_pruned']}, merged={info_inf['num_merged']}")
170	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "1d5f5a67-5533-401a-8204-980455cb918f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/token_selection.py",
      "content": "\"\"\"Margin-aware token selection: soft masking (train) / hard prune+merge (inference).\n\nTraining: applies soft sigmoid mask to visual tokens (fully differentiable).\nInference: three-partition — preserve (top-k), prune (bottom), merge (borderline) —\n           borderline tokens are weighted-averaged into their nearest preserved token.\n\nInputs:  (B, N) scores, (B, N, D) visual tokens, integer k.\nDepends: soft_topk.SoftTopK.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom torch import Tensor\nfrom typing import Dict, Tuple, Optional\n\nfrom .soft_topk import SoftTopK\n\n\nclass MarginAwareTokenSelector(nn.Module):\n    def __init__(self, temperature: float = 1.0, merge_weight_temp: float = 0.5):\n        super().__init__()\n        self.soft_topk = SoftTopK(temperature=temperature, method=\"sigmoid\")\n        self.merge_weight_temp = merge_weight_temp\n\n    def forward(\n        self,\n        importance_scores: Tensor,\n        visual_tokens: Tensor,\n        k: int,\n        training: bool = True,\n    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:\n        \"\"\"\n        Args:\n            importance_scores: (B, N) per-token scores.\n            visual_tokens:     (B, N, D) visual token embeddings.\n            k: number of tokens to retain.\n            training: soft mask (True) or hard prune/merge (False).\n        Returns:\n            selected_tokens: (B, N, D) soft-masked  or  (B, K', D) hard-selected.\n            selection_mask:  (B, N) soft or binary mask.\n            info: dict with diagnostic stats.\n        \"\"\"\n        if training:\n            return self._soft_forward(importance_scores, visual_tokens, k)\n        return self._hard_forward(importance_scores, visual_tokens, k)\n\n    # ------------------------------------------------------------------\n    def _soft_forward(\n        self, scores: Tensor, tokens: Tensor, k: int\n    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:\n        mask, s_k, s_k1 = self.soft_topk(scores, k)\n        selected = tokens * mask.unsqueeze(-1)  # (B, N, D)\n        info = {\n            \"mode\": torch.tensor(0),  # 0 = soft\n            \"mask_sum\": mask.sum(-1).detach(),\n            \"margin\": (s_k - s_k1).detach(),\n        }\n        return selected, mask, info\n\n    # ------------------------------------------------------------------\n    def _hard_forward(\n        self, scores: Tensor, tokens: Tensor, k: int\n    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:\n        B, N, D = tokens.shape\n\n        sorted_scores, sorted_idx = torch.sort(scores, dim=-1, descending=True)\n        s_k = sorted_scores[:, k - 1]          # (B,) k-th largest score\n        s_k_plus_1 = sorted_scores[:, k]       # (B,) (k+1)-th largest score\n        delta_k = s_k - s_k_plus_1             # (B,) margin\n\n        threshold_high = (s_k + delta_k / 2).unsqueeze(-1)   # (B, 1)\n        threshold_low = (s_k - delta_k / 2).unsqueeze(-1)    # (B, 1)\n\n        # Fixed top-k as preserved tokens (output length stays k)\n        preserve_idx = sorted_idx[:, :k]                                 # (B, k)\n        preserved_tokens = torch.gather(tokens, 1, preserve_idx.unsqueeze(-1).expand(-1, -1, D))\n\n        is_topk = torch.zeros(B, N, device=scores.device, dtype=torch.bool)\n        is_topk.scatter_(1, preserve_idx, True)\n\n        # Margin-aware three-partition for non-top-k tokens\n        borderline_mask = ~is_topk & (scores >= threshold_low.squeeze(-1)) & (scores <= threshold_high.squeeze(-1))\n        prune_mask = ~is_topk & (scores < threshold_low.squeeze(-1))\n        preserve_mask = is_topk\n\n        # Merge borderline tokens into nearest preserved token\n        merged_tokens = self._merge_borderline_tokens(\n            tokens, scores, preserved_tokens, preserve_idx, borderline_mask\n        )\n\n        binary_mask = preserve_mask.float()\n        info = {\n            \"mode\": torch.tensor(1),  # 1 = hard\n            \"num_preserved\": preserve_mask.sum(-1).float().detach(),\n            \"num_pruned\": prune_mask.sum(-1).float().detach(),\n            \"num_merged\": borderline_mask.sum(-1).float().detach(),\n            \"delta_k\": delta_k.detach(),\n        }\n        return merged_tokens, binary_mask, info\n\n    # ------------------------------------------------------------------\n    def _merge_borderline_tokens(\n        self,\n        tokens: Tensor,\n        scores: Tensor,\n        preserved_tokens: Tensor,\n        preserve_idx: Tensor,\n        borderline_mask: Tensor,\n    ) -> Tensor:\n        \"\"\"Weighted-merge each borderline token into cosine-nearest preserved token.\"\"\"\n        B, N, D = tokens.shape\n        K = preserved_tokens.shape[1]\n\n        num_borderline = borderline_mask.sum(-1)  # (B,)\n        if num_borderline.sum() == 0:\n            return preserved_tokens\n\n        # Cosine similarity: borderline -> preserved\n        preserved_norm = F.normalize(preserved_tokens, dim=-1)  # (B, K, D)\n        tokens_norm = F.normalize(tokens, dim=-1)               # (B, N, D)\n\n        # Similarity of all tokens to preserved tokens: (B, N, K)\n        sim = torch.bmm(tokens_norm, preserved_norm.transpose(1, 2))\n\n        # For each borderline token, find best preserved match\n        best_match = sim.argmax(dim=-1)  # (B, N) — index into K\n\n        # Importance-based merge weights\n        preserve_scores = torch.gather(scores, 1, preserve_idx)  # (B, K)\n\n        merged = preserved_tokens.clone()\n        # TODO: vectorize this loop for better GPU efficiency\n        for b in range(B):\n            border_idx = borderline_mask[b].nonzero(as_tuple=True)[0]\n            if border_idx.numel() == 0:\n                continue\n            for idx in border_idx:\n                target = best_match[b, idx].item()\n                w_border = torch.sigmoid(scores[b, idx] / (self.merge_weight_temp + 1e-8))\n                w_orig = torch.sigmoid(preserve_scores[b, target] / (self.merge_weight_temp + 1e-8))\n                total_w = w_orig + w_border + 1e-8\n                merged[b, target] = (w_orig / total_w) * merged[b, target] + (w_border / total_w) * tokens[b, idx]\n\n        return merged\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B, N, D, k = 2, 32, 64, 8\n    scores = torch.randn(B, N, requires_grad=True)\n    tokens = torch.randn(B, N, D)\n\n    selector = MarginAwareTokenSelector(temperature=0.5)\n\n    # Training mode\n    sel_train, mask_train, info_train = selector(scores, tokens, k, training=True)\n    sel_train.sum().backward()\n    print(f\"[train] shape={sel_train.shape}, mask_sum={info_train['mask_sum']}, \"\n          f\"grad OK={scores.grad is not None}\")\n    scores.grad = None\n\n    # Inference mode\n    with torch.no_grad():\n        sel_inf, mask_inf, info_inf = selector(scores, tokens, k, training=False)\n    print(f\"[infer] shape={sel_inf.shape}, preserved={info_inf['num_preserved']}, \"\n          f\"pruned={info_inf['num_pruned']}, merged={info_inf['num_merged']}\")\n",
      "numLines": 170,
      "startLine": 1,
      "totalLines": 170
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_012JL1Tiojq8CuuHM2pBfW5S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "3a801e1f-ebdb-41eb-86a3-4eab1bbaef6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wu8dgR6bbmbjWJ1duWVXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17968
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

_source line 20 · 2026-05-15T12:03:46.287Z_

<details><summary>↩ Tool result · `toolu_012JL1Tiojq8CuuHM2pBfW5S`</summary>

```text
1	"""IMM Training Pipeline for SmolVLA + LIBERO.
2	
3	Usage:
4	    python train.py --config configs/baseline.yaml
5	    python train.py --config configs/imm_anchor.yaml
6	    python train.py --config configs/imm_anchor.yaml --resume checkpoints/imm_anchor/latest
7	
8	Two modes:
9	  - Baseline: L_action only (flow matching MSE), no ACIS/margin loss.
10	  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.
11	
12	Depends: lerobot, torch, wandb, peft.
13	"""
14	
15	from __future__ import annotations
16	
17	import argparse
18	import copy
19	import json
20	import logging
21	import os
22	import signal
23	import sys
24	import time
25	from pathlib import Path
26	from typing import Any, Dict, Optional
27	
28	import torch
29	import torch.nn.functional as F
30	import wandb
31	import yaml
32	
33	logging.basicConfig(
34	    level=logging.INFO,
35	    format="%(asctime)s [%(levelname)s] %(message)s",
36	    datefmt="%Y-%m-%d %H:%M:%S",
37	)
38	log = logging.getLogger(__name__)
39	
40	ARTIFACTS_DIR = Path(__file__).resolve().parent
41	
42	
43	def parse_args():
44	    parser = argparse.ArgumentParser(description="IMM training for SmolVLA on LIBERO")
45	    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file")
46	    parser.add_argument("--resume", type=str, default=None, help="Path to checkpoint dir to resume from")
47	    parser.add_argument("--gpu", type=int, default=0, help="GPU index (use CUDA_VISIBLE_DEVICES for physical mapping)")
48	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
49	    parser.add_argument("--wandb_project", type=str, default="imm-vla-compress", help="W&B project name")
50	    parser.add_argument("--wandb_run", type=str, default=None, help="W&B run name (auto-generated if None)")
51	    return parser.parse_args()
52	
53	
54	def load_config(config_path: str) -> Dict[str, Any]:
55	    """Load YAML config with _base_ inheritance support."""
56	    config_path = Path(config_path)
57	    with open(config_path) as f:
58	        config = yaml.safe_load(f)
59	
60	    if "_base_" in config:
61	        base_path = config_path.parent / config.pop("_base_")
62	        base_config = load_config(str(base_path))
63	        base_config = deep_merge(base_config, config)
64	        return base_config
65	
66	    return config
67	
68	
69	def deep_merge(base: Dict, override: Dict) -> Dict:
70	    """Recursively merge override into base."""
71	    result = copy.deepcopy(base)
72	    for k, v in override.items():
73	        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
74	            result[k] = deep_merge(result[k], v)
75	        else:
76	            result[k] = copy.deepcopy(v)
77	    return result
78	
79	
80	def set_seed(seed: int):
81	    import random
82	    import numpy as np
83	
84	    random.seed(seed)
85	    np.random.seed(seed)
86	    torch.manual_seed(seed)
87	    if torch.cuda.is_available():
88	        torch.cuda.manual_seed_all(seed)
89	
90	
91	def load_smolvla_policy(config: Dict[str, Any], device: torch.device):
92	    """Load SmolVLAPolicy via LeRobot API and apply LoRA."""
93	    from lerobot.common.policies.smolvla.configuration_smolvla import SmolVLAConfig
94	    from lerobot.common.policies.smolvla.modeling_smolvla import SmolVLAPolicy
95	
96	    model_cfg = config["model"]
97	
98	    policy_config = SmolVLAConfig()
99	    if model_cfg.get("pretrained"):
100	        policy_config.pretrained_path = model_cfg["pretrained"]
101	
102	    policy = SmolVLAPolicy(policy_config, dataset_stats=None)
103	
104	    lora_cfg = model_cfg.get("lora", {})
105	    if lora_cfg.get("rank", 0) > 0:
106	        from peft import LoraConfig, get_peft_model
107	
108	        peft_config = LoraConfig(
109	            r=lora_cfg["rank"],
110	            lora_alpha=lora_cfg.get("alpha", lora_cfg["rank"] * 2),
111	            lora_dropout=lora_cfg.get("dropout", 0.05),
112	            target_modules=lora_cfg.get(
113	                "target_modules_regex",
114	                r"(model\.vlm_with_expert\.lm_expert\..*\.(q|v)_proj"
115	                r"|model\.(state_proj|action_in_proj|action_out_proj"
116	                r"|action_time_mlp_in|action_time_mlp_out))",
117	            ),
118	            bias="none",
119	        )
120	        policy.model = get_peft_model(policy.model, peft_config)
121	        log.info(
122	            "LoRA applied: rank=%d, alpha=%d, trainable params: %s",
123	            lora_cfg["rank"],
124	            peft_config.lora_alpha,
125	            sum(p.numel() for p in policy.model.parameters() if p.requires_grad),
126	        )
127	
128	    policy.to(device)
129	    return policy
130	
131	
132	def load_dataset(config: Dict[str, Any]):
133	    """Load LIBERO dataset via LeRobot API."""
134	    from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
135	
136	    ds_cfg = config["dataset"]
137	    dataset = LeRobotDataset(
138	        repo_id=ds_cfg["repo_id"],
139	        episodes=ds_cfg.get("episodes", None),
140	    )
141	    return dataset
142	
143	
144	def make_dataloader(dataset, config: Dict[str, Any]):
145	    from torch.utils.data import DataLoader
146	
147	    train_cfg = config["training"]
148	    return DataLoader(
149	        dataset,
150	        batch_size=train_cfg.get("batch_size", 4),
151	        shuffle=True,
152	        num_workers=train_cfg.get("num_workers", 4),
153	        pin_memory=True,
154	        drop_last=True,
155	    )
156	
157	
158	def make_optimizer(model, config: Dict[str, Any]):
159	    train_cfg = config["training"]
160	    params = [p for p in model.parameters() if p.requires_grad]
161	    return torch.optim.AdamW(
162	        params,
163	        lr=train_cfg.get("lr", 1e-4),
164	        betas=tuple(train_cfg.get("betas", [0.9, 0.95])),
165	        weight_decay=train_cfg.get("weight_decay", 1e-10),
166	    )
167	
168	
169	def make_scheduler(optimizer, config: Dict[str, Any]):
170	    from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR
171	
172	    train_cfg = config["training"]
173	    warmup_steps = train_cfg.get("warmup_steps", 1000)
174	    total_steps = train_cfg.get("total_steps", 30000)
175	    decay_lr = train_cfg.get("decay_lr", 2.5e-6)
176	
177	    warmup = LinearLR(optimizer, start_factor=1e-8, end_factor=1.0, total_iters=warmup_steps)
178	    cosine = CosineAnnealingLR(optimizer, T_max=total_steps - warmup_steps, eta_min=decay_lr)
179	    return SequentialLR(optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps])
180	
181	
182	def wrap_with_imm(policy, config: Dict[str, Any]):
183	    """Wrap SmolVLAPolicy.model with IMMSmolVLAWrapper."""
184	    sys.path.insert(0, str(ARTIFACTS_DIR))
185	    from imm.smolvla_wrapper import IMMSmolVLAWrapper
186	
187	    imm_cfg = config["imm"]
188	    acis_cfg = config.get("acis", {})
189	
190	    imm_kwargs = {
191	        "lambda_margin": imm_cfg.get("lambda_margin", 0.1),
192	        "delta": imm_cfg.get("delta", 1.0),
193	        "warmup_steps": imm_cfg.get("warmup_steps", 1000),
194	        "temperature": imm_cfg.get("temperature", 1.0),
195	        "method": imm_cfg.get("soft_topk_method", "sigmoid"),
196	        "k_ratio": imm_cfg.get("k_ratio", 0.5),
197	    }
198	
199	    wrapper = IMMSmolVLAWrapper(
200	        smolvla_model=policy.model,
201	        acis_config=acis_cfg,
202	        imm_config=imm_kwargs,
203	    )
204	    return wrapper
205	
206	
207	def save_checkpoint(
208	    model,
209	    optimizer,
210	    scheduler,
211	    step: int,
212	    config: Dict[str, Any],
213	    info: Optional[Dict] = None,
214	    output_dir: Optional[str] = None,
215	):
216	    """Save checkpoint. Non-fatal on failure."""
217	    if output_dir is None:
218	        output_dir = config["training"].get("output_dir", "checkpoints")
219	    ckpt_dir = Path(output_dir) / f"step_{step:06d}"
220	    try:
221	        ckpt_dir.mkdir(parents=True, exist_ok=True)
222	
223	        state = {
224	            "step": step,
225	            "model_state_dict": model.state_dict(),
226	            "optimizer_state_dict": optimizer.state_dict(),
227	            "scheduler_state_dict": scheduler.state_dict(),
228	            "config": config,
229	        }
230	        if info:
231	            state["margin_stats"] = {
232	                k: v.cpu() if isinstance(v, torch.Tensor) else v
233	                for k, v in info.items()
234	                if k in ("margin", "s_k", "s_k_plus_1", "lambda", "action_loss", "margin_loss")
235	            }
236	
237	        torch.save(state, ckpt_dir / "checkpoint.pt")
238	
239	        latest_link = Path(output_dir) / "latest"
240	        if latest_link.exists() or latest_link.is_symlink():
241	            latest_link.unlink()
242	        latest_link.symlink_to(ckpt_dir.name)
243	
244	        log.info("Checkpoint saved: %s", ckpt_dir)
245	    except Exception as e:
246	        log.warning("Failed to save checkpoint at step %d: %s", step, e)
247	
248	
249	def load_checkpoint(
250	    path: str,
251	    model,
252	    optimizer,
253	    scheduler,
254	    device: torch.device,
255	) -> int:
256	    """Load checkpoint and return the step to resume from."""
257	    ckpt_path = Path(path)
258	    if ckpt_path.is_dir():
259	        ckpt_path = ckpt_path / "checkpoint.pt"
260	
261	    log.info("Resuming from %s", ckpt_path)
262	    state = torch.load(ckpt_path, map_location=device, weights_only=False)
263	
264	    model.load_state_dict(state["model_state_dict"])
265	    optimizer.load_state_dict(state["optimizer_state_dict"])
266	    scheduler.load_state_dict(state["scheduler_state_dict"])
267	
268	    start_step = state["step"] + 1
269	    log.info("Resumed at step %d", start_step)
270	    return start_step
271	
272	
273	@torch.no_grad()
274	def evaluate(model, dataloader, step: int, config: Dict[str, Any], device: torch.device, imm_enabled: bool):
275	    """Run validation pass and return metrics dict."""
276	    sys.path.insert(0, str(ARTIFACTS_DIR))
277	    from imm.metrics import compute_margin, margin_statistics, topk_preservation_rate, l_eps_delta_ratio
278	
279	    model.eval()
280	    eval_cfg = config.get("evaluation", {})
281	    epsilons = eval_cfg.get("perturbations", [0.0, 0.01, 0.02, 0.05])
282	    pruning_ratio = eval_cfg.get("pruning_ratio", 0.5)
283	    max_batches = eval_cfg.get("max_eval_batches", 50)
284	
285	    results = {}
286	    total_action_loss = 0.0
287	    n_batches = 0
288	
289	    for batch_idx, batch in enumerate(dataloader):
290	        if batch_idx >= max_batches:
291	            break
292	        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
293	
294	        if imm_enabled:
295	            _, info = model(batch, step=step)
296	            total_action_loss += info["action_loss"].item()
297	
298	            scores = info["importance_scores"]
299	            k = info["k"]
300	
301	            for eps in epsilons:
302	                key = f"eps_{eps}"
303	                if key not in results:
304	                    results[key] = {"margins": [], "preservation": []}
305	
306	                if eps > 0:
307	                    batch_noisy = {k_: v.clone() if isinstance(v, torch.Tensor) else v for k_, v in batch.items()}
308	                    for img_key in [k_ for k_ in batch_noisy if "image" in k_.lower()]:
309	                        if isinstance(batch_noisy[img_key], torch.Tensor) and batch_noisy[img_key].is_floating_point():
310	                            batch_noisy[img_key] = (batch_noisy[img_key] + eps * torch.randn_like(batch_noisy[img_key])).clamp(0, 1)
311	                    _, info_noisy = model(batch_noisy, step=step)
312	                    scores_noisy = info_noisy["importance_scores"]
313	                else:
314	                    scores_noisy = scores
315	
316	                margin = compute_margin(scores, k)
317	                pres = topk_preservation_rate(scores, scores_noisy, k)
318	                results[key]["margins"].append(margin.cpu())
319	                results[key]["preservation"].append(pres.cpu())
320	        else:
321	            loss, info = model.forward_baseline(batch) if hasattr(model, "forward_baseline") else (model(batch), {})
322	            if isinstance(loss, tuple):
323	                loss = loss[0]
324	            total_action_loss += (info.get("action_loss", loss) if isinstance(info, dict) else loss).item()
325	
326	        n_batches += 1
327	
328	    metrics = {"eval/action_loss": total_action_loss / max(n_batches, 1)}
329	
330	    if imm_enabled:
331	        for eps_key, data in results.items():
332	            margins = torch.cat(data["margins"])
333	            pres = torch.cat(data["preservation"])
334	            metrics[f"eval/{eps_key}/margin_mean"] = margins.mean().item()
335	            metrics[f"eval/{eps_key}/margin_median"] = margins.median().item()
336	            metrics[f"eval/{eps_key}/margin_std"] = margins.std().item()
337	            metrics[f"eval/{eps_key}/preservation_rate"] = pres.mean().item()
338	
339	    model.train()
340	    return metrics
341	
342	
343	class GracefulExit:
344	    """Handle SIGINT/SIGTERM for graceful checkpoint saving."""
345	
346	    def __init__(self):
347	        self.should_exit = False
348	        signal.signal(signal.SIGINT, self._handler)
349	        signal.signal(signal.SIGTERM, self._handler)
350	
351	    def _handler(self, signum, frame):
352	        log.info("Received signal %d, will exit after current step", signum)
353	        self.should_exit = True
354	
355	
356	def main():
357	    args = parse_args()
358	    config = load_config(args.config)
359	    set_seed(args.seed)
360	
361	    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
362	    log.info("Device: %s", device)
363	
364	    train_cfg = config["training"]
365	    total_steps = train_cfg.get("total_steps", 30000)
366	    eval_every = train_cfg.get("eval_every", 2000)
367	    save_every = train_cfg.get("save_every", 5000)
368	    log_every = train_cfg.get("log_every", 50)
369	    grad_clip = train_cfg.get("grad_clip", 10.0)
370	
371	    imm_enabled = config.get("imm", {}).get("enabled", False)
372	
373	    output_dir = train_cfg.get("output_dir", f"checkpoints/{'imm' if imm_enabled else 'baseline'}")
374	    config["training"]["output_dir"] = output_dir
375	
376	    # Model
377	    log.info("Loading SmolVLA policy...")
378	    policy = load_smolvla_policy(config, device)
379	
380	    if imm_enabled:
381	        log.info("Wrapping with IMMSmolVLAWrapper (delta=%.2f, lambda=%.2f)",
382	                 config["imm"].get("delta", 1.0), config["imm"].get("lambda_margin", 0.1))
383	        model = wrap_with_imm(policy, config)
384	        model.to(device)
385	    else:
386	        model = policy
387	
388	    # Dataset
389	    log.info("Loading dataset...")
390	    dataset = load_dataset(config)
391	    dataloader = make_dataloader(dataset, config)
392	    dataloader_iter = iter(dataloader)
393	
394	    eval_dataset = load_dataset(config)
395	    eval_dataloader = make_dataloader(eval_dataset, {**config, "training": {**train_cfg, "batch_size": train_cfg.get("eval_batch_size", train_cfg.get("batch_size", 4))}})
396	
397	    # Optimizer / Scheduler
398	    optimizer = make_optimizer(model, config)
399	    scheduler = make_scheduler(optimizer, config)
400	
401	    # Resume
402	    start_step = 0
403	    if args.resume:
404	        start_step = load_checkpoint(args.resume, model, optimizer, scheduler, device)
405	
406	    # W&B
407	    run_name = args.wandb_run or (f"{'imm' if imm_enabled else 'baseline'}_seed{args.seed}")
408	    wandb.init(project=args.wandb_project, name=run_name, config=config, resume="allow")
409	
410	    # Training loop
411	    graceful = GracefulExit()
412	    model.train()
413	    t0 = time.time()
414	    last_info = None
415	
416	    log.info("Starting training from step %d to %d", start_step, total_steps)
417	
418	    for step in range(start_step, total_steps):
419	        try:
420	            batch = next(dataloader_iter)
421	        except StopIteration:
422	            dataloader_iter = iter(dataloader)
423	            batch = next(dataloader_iter)
424	
425	        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
426	
427	        if imm_enabled:
428	            total_loss, info = model(batch, step=step)
429	            last_info = info
430	        else:
431	            if hasattr(model, "forward_baseline"):
432	                total_loss, info = model.forward_baseline(batch)
433	                last_info = info
434	            else:
435	                output = model(batch)
436	                if isinstance(output, dict):
437	                    total_loss = output["loss"]
438	                    info = {"action_loss": total_loss.detach()}
439	                elif isinstance(output, tuple):
440	                    total_loss = output[0]
441	                    info = output[1] if len(output) > 1 else {"action_loss": total_loss.detach()}
442	                else:
443	                    total_loss = output
444	                    info = {"action_loss": total_loss.detach()}
445	                last_info = info
446	
447	        optimizer.zero_grad()
448	        total_loss.backward()
449	        grad_norm = torch.nn.utils.clip_grad_norm_(
450	            [p for p in model.parameters() if p.requires_grad], grad_clip
451	        )
452	        optimizer.step()
453	        scheduler.step()
454	
455	        # Logging
456	        if step % log_every == 0:
457	            log_dict = {
458	                "train/total_loss": total_loss.item(),
459	                "train/grad_norm": grad_norm.item() if isinstance(grad_norm, torch.Tensor) else grad_norm,
460	                "train/lr": optimizer.param_groups[0]["lr"],
461	                "train/step": step,
462	            }
463	
464	            if imm_enabled and isinstance(last_info, dict):
465	                log_dict.update({
466	                    "train/action_loss": last_info.get("action_loss", torch.tensor(0.0)).item(),
467	                    "train/margin_loss": last_info.get("margin_loss", torch.tensor(0.0)).item(),
468	                    "train/lambda": last_info.get("lambda", torch.tensor(0.0)).item(),
469	                })
470	                if "margin" in last_info:
471	                    margins = last_info["margin"]
472	                    log_dict.update({
473	                        "margin/mean": margins.mean().item(),
474	                        "margin/median": margins.median().item(),
475	                        "margin/std": margins.std().item(),
476	                        "margin/min": margins.min().item(),
477	                        "margin/max": margins.max().item(),
478	                    })
479	                    log_dict["margin/histogram"] = wandb.Histogram(margins.cpu().numpy())
480	                if "importance_scores" in last_info:
481	                    scores = last_info["importance_scores"]
482	                    k = last_info.get("k", int(scores.shape[1] * 0.5))
483	                    topk_vals, _ = torch.topk(scores, k, dim=-1)
484	                    log_dict["scores/topk_mean"] = topk_vals.mean().item()
485	                if "lipschitz_estimate" in last_info:
486	                    L = last_info["lipschitz_estimate"]
487	                    if "margin" in last_info:
488	                        eps_test = 0.01
489	                        k_val = last_info.get("k", 64)
490	                        ratio = L * eps_test * k_val / margins.clamp(min=1e-8)
491	                        log_dict["gate/L_eps_delta_ratio_mean"] = ratio.mean().item()
492	                        log_dict["gate/lipschitz_estimate"] = L
493	            else:
494	                if isinstance(last_info, dict) and "action_loss" in last_info:
495	                    log_dict["train/action_loss"] = last_info["action_loss"].item() if isinstance(last_info["action_loss"], torch.Tensor) else last_info["action_loss"]
496	
497	            wandb.log(log_dict, step=step)
498	
499	            elapsed = time.time() - t0
500	            steps_done = step - start_step + 1
501	            sps = steps_done / elapsed if elapsed > 0 else 0
502	            log.info(
503	                "step=%d/%d  loss=%.4f  lr=%.2e  grad=%.2f  sps=%.1f",
504	                step, total_steps, total_loss.item(),
505	                optimizer.param_groups[0]["lr"], grad_norm, sps,
506	            )
507	
508	        # Eval
509	        if step > 0 and step % eval_every == 0:
510	            log.info("Running evaluation at step %d...", step)
511	            eval_metrics = evaluate(model, eval_dataloader, step, config, device, imm_enabled)
512	            wandb.log(eval_metrics, step=step)
513	            for k, v in eval_metrics.items():
514	                log.info("  %s: %.4f", k, v)
515	
516	        # Checkpoint
517	        if step > 0 and step % save_every == 0:
518	            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir)
519	
520	        if graceful.should_exit:
521	            log.info("Graceful exit at step %d", step)
522	            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir)
523	            break
524	
525	    # Final checkpoint
526	    if not graceful.should_exit:
527	        save_checkpoint(model, optimizer, scheduler, total_steps - 1, config, last_info, output_dir)
528	
529	    wandb.finish()
530	    log.info("Training complete.")
531	
532	
533	if __name__ == "__main__":
534	    main()
535	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "866c40c8-7db0-488c-93cf-358926866503",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/train.py",
      "content": "\"\"\"IMM Training Pipeline for SmolVLA + LIBERO.\n\nUsage:\n    python train.py --config configs/baseline.yaml\n    python train.py --config configs/imm_anchor.yaml\n    python train.py --config configs/imm_anchor.yaml --resume checkpoints/imm_anchor/latest\n\nTwo modes:\n  - Baseline: L_action only (flow matching MSE), no ACIS/margin loss.\n  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.\n\nDepends: lerobot, torch, wandb, peft.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport copy\nimport json\nimport logging\nimport os\nimport signal\nimport sys\nimport time\nfrom pathlib import Path\nfrom typing import Any, Dict, Optional\n\nimport torch\nimport torch.nn.functional as F\nimport wandb\nimport yaml\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nARTIFACTS_DIR = Path(__file__).resolve().parent\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(description=\"IMM training for SmolVLA on LIBERO\")\n    parser.add_argument(\"--config\", type=str, required=True, help=\"Path to YAML config file\")\n    parser.add_argument(\"--resume\", type=str, default=None, help=\"Path to checkpoint dir to resume from\")\n    parser.add_argument(\"--gpu\", type=int, default=0, help=\"GPU index (use CUDA_VISIBLE_DEVICES for physical mapping)\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--wandb_project\", type=str, default=\"imm-vla-compress\", help=\"W&B project name\")\n    parser.add_argument(\"--wandb_run\", type=str, default=None, help=\"W&B run name (auto-generated if None)\")\n    return parser.parse_args()\n\n\ndef load_config(config_path: str) -> Dict[str, Any]:\n    \"\"\"Load YAML config with _base_ inheritance support.\"\"\"\n    config_path = Path(config_path)\n    with open(config_path) as f:\n        config = yaml.safe_load(f)\n\n    if \"_base_\" in config:\n        base_path = config_path.parent / config.pop(\"_base_\")\n        base_config = load_config(str(base_path))\n        base_config = deep_merge(base_config, config)\n        return base_config\n\n    return config\n\n\ndef deep_merge(base: Dict, override: Dict) -> Dict:\n    \"\"\"Recursively merge override into base.\"\"\"\n    result = copy.deepcopy(base)\n    for k, v in override.items():\n        if k in result and isinstance(result[k], dict) and isinstance(v, dict):\n            result[k] = deep_merge(result[k], v)\n        else:\n            result[k] = copy.deepcopy(v)\n    return result\n\n\ndef set_seed(seed: int):\n    import random\n    import numpy as np\n\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    if torch.cuda.is_available():\n        torch.cuda.manual_seed_all(seed)\n\n\ndef load_smolvla_policy(config: Dict[str, Any], device: torch.device):\n    \"\"\"Load SmolVLAPolicy via LeRobot API and apply LoRA.\"\"\"\n    from lerobot.common.policies.smolvla.configuration_smolvla import SmolVLAConfig\n    from lerobot.common.policies.smolvla.modeling_smolvla import SmolVLAPolicy\n\n    model_cfg = config[\"model\"]\n\n    policy_config = SmolVLAConfig()\n    if model_cfg.get(\"pretrained\"):\n        policy_config.pretrained_path = model_cfg[\"pretrained\"]\n\n    policy = SmolVLAPolicy(policy_config, dataset_stats=None)\n\n    lora_cfg = model_cfg.get(\"lora\", {})\n    if lora_cfg.get(\"rank\", 0) > 0:\n        from peft import LoraConfig, get_peft_model\n\n        peft_config = LoraConfig(\n            r=lora_cfg[\"rank\"],\n            lora_alpha=lora_cfg.get(\"alpha\", lora_cfg[\"rank\"] * 2),\n            lora_dropout=lora_cfg.get(\"dropout\", 0.05),\n            target_modules=lora_cfg.get(\n                \"target_modules_regex\",\n                r\"(model\\.vlm_with_expert\\.lm_expert\\..*\\.(q|v)_proj\"\n                r\"|model\\.(state_proj|action_in_proj|action_out_proj\"\n                r\"|action_time_mlp_in|action_time_mlp_out))\",\n            ),\n            bias=\"none\",\n        )\n        policy.model = get_peft_model(policy.model, peft_config)\n        log.info(\n            \"LoRA applied: rank=%d, alpha=%d, trainable params: %s\",\n            lora_cfg[\"rank\"],\n            peft_config.lora_alpha,\n            sum(p.numel() for p in policy.model.parameters() if p.requires_grad),\n        )\n\n    policy.to(device)\n    return policy\n\n\ndef load_dataset(config: Dict[str, Any]):\n    \"\"\"Load LIBERO dataset via LeRobot API.\"\"\"\n    from lerobot.common.datasets.lerobot_dataset import LeRobotDataset\n\n    ds_cfg = config[\"dataset\"]\n    dataset = LeRobotDataset(\n        repo_id=ds_cfg[\"repo_id\"],\n        episodes=ds_cfg.get(\"episodes\", None),\n    )\n    return dataset\n\n\ndef make_dataloader(dataset, config: Dict[str, Any]):\n    from torch.utils.data import DataLoader\n\n    train_cfg = config[\"training\"]\n    return DataLoader(\n        dataset,\n        batch_size=train_cfg.get(\"batch_size\", 4),\n        shuffle=True,\n        num_workers=train_cfg.get(\"num_workers\", 4),\n        pin_memory=True,\n        drop_last=True,\n    )\n\n\ndef make_optimizer(model, config: Dict[str, Any]):\n    train_cfg = config[\"training\"]\n    params = [p for p in model.parameters() if p.requires_grad]\n    return torch.optim.AdamW(\n        params,\n        lr=train_cfg.get(\"lr\", 1e-4),\n        betas=tuple(train_cfg.get(\"betas\", [0.9, 0.95])),\n        weight_decay=train_cfg.get(\"weight_decay\", 1e-10),\n    )\n\n\ndef make_scheduler(optimizer, config: Dict[str, Any]):\n    from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR\n\n    train_cfg = config[\"training\"]\n    warmup_steps = train_cfg.get(\"warmup_steps\", 1000)\n    total_steps = train_cfg.get(\"total_steps\", 30000)\n    decay_lr = train_cfg.get(\"decay_lr\", 2.5e-6)\n\n    warmup = LinearLR(optimizer, start_factor=1e-8, end_factor=1.0, total_iters=warmup_steps)\n    cosine = CosineAnnealingLR(optimizer, T_max=total_steps - warmup_steps, eta_min=decay_lr)\n    return SequentialLR(optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps])\n\n\ndef wrap_with_imm(policy, config: Dict[str, Any]):\n    \"\"\"Wrap SmolVLAPolicy.model with IMMSmolVLAWrapper.\"\"\"\n    sys.path.insert(0, str(ARTIFACTS_DIR))\n    from imm.smolvla_wrapper import IMMSmolVLAWrapper\n\n    imm_cfg = config[\"imm\"]\n    acis_cfg = config.get(\"acis\", {})\n\n    imm_kwargs = {\n        \"lambda_margin\": imm_cfg.get(\"lambda_margin\", 0.1),\n        \"delta\": imm_cfg.get(\"delta\", 1.0),\n        \"warmup_steps\": imm_cfg.get(\"warmup_steps\", 1000),\n        \"temperature\": imm_cfg.get(\"temperature\", 1.0),\n        \"method\": imm_cfg.get(\"soft_topk_method\", \"sigmoid\"),\n        \"k_ratio\": imm_cfg.get(\"k_ratio\", 0.5),\n    }\n\n    wrapper = IMMSmolVLAWrapper(\n        smolvla_model=policy.model,\n        acis_config=acis_cfg,\n        imm_config=imm_kwargs,\n    )\n    return wrapper\n\n\ndef save_checkpoint(\n    model,\n    optimizer,\n    scheduler,\n    step: int,\n    config: Dict[str, Any],\n    info: Optional[Dict] = None,\n    output_dir: Optional[str] = None,\n):\n    \"\"\"Save checkpoint. Non-fatal on failure.\"\"\"\n    if output_dir is None:\n        output_dir = config[\"training\"].get(\"output_dir\", \"checkpoints\")\n    ckpt_dir = Path(output_dir) / f\"step_{step:06d}\"\n    try:\n        ckpt_dir.mkdir(parents=True, exist_ok=True)\n\n        state = {\n            \"step\": step,\n            \"model_state_dict\": model.state_dict(),\n            \"optimizer_state_dict\": optimizer.state_dict(),\n            \"scheduler_state_dict\": scheduler.state_dict(),\n            \"config\": config,\n        }\n        if info:\n            state[\"margin_stats\"] = {\n                k: v.cpu() if isinstance(v, torch.Tensor) else v\n                for k, v in info.items()\n                if k in (\"margin\", \"s_k\", \"s_k_plus_1\", \"lambda\", \"action_loss\", \"margin_loss\")\n            }\n\n        torch.save(state, ckpt_dir / \"checkpoint.pt\")\n\n        latest_link = Path(output_dir) / \"latest\"\n        if latest_link.exists() or latest_link.is_symlink():\n            latest_link.unlink()\n        latest_link.symlink_to(ckpt_dir.name)\n\n        log.info(\"Checkpoint saved: %s\", ckpt_dir)\n    except Exception as e:\n        log.warning(\"Failed to save checkpoint at step %d: %s\", step, e)\n\n\ndef load_checkpoint(\n    path: str,\n    model,\n    optimizer,\n    scheduler,\n    device: torch.device,\n) -> int:\n    \"\"\"Load checkpoint and return the step to resume from.\"\"\"\n    ckpt_path = Path(path)\n    if ckpt_path.is_dir():\n        ckpt_path = ckpt_path / \"checkpoint.pt\"\n\n    log.info(\"Resuming from %s\", ckpt_path)\n    state = torch.load(ckpt_path, map_location=device, weights_only=False)\n\n    model.load_state_dict(state[\"model_state_dict\"])\n    optimizer.load_state_dict(state[\"optimizer_state_dict\"])\n    scheduler.load_state_dict(state[\"scheduler_state_dict\"])\n\n    start_step = state[\"step\"] + 1\n    log.info(\"Resumed at step %d\", start_step)\n    return start_step\n\n\n@torch.no_grad()\ndef evaluate(model, dataloader, step: int, config: Dict[str, Any], device: torch.device, imm_enabled: bool):\n    \"\"\"Run validation pass and return metrics dict.\"\"\"\n    sys.path.insert(0, str(ARTIFACTS_DIR))\n    from imm.metrics import compute_margin, margin_statistics, topk_preservation_rate, l_eps_delta_ratio\n\n    model.eval()\n    eval_cfg = config.get(\"evaluation\", {})\n    epsilons = eval_cfg.get(\"perturbations\", [0.0, 0.01, 0.02, 0.05])\n    pruning_ratio = eval_cfg.get(\"pruning_ratio\", 0.5)\n    max_batches = eval_cfg.get(\"max_eval_batches\", 50)\n\n    results = {}\n    total_action_loss = 0.0\n    n_batches = 0\n\n    for batch_idx, batch in enumerate(dataloader):\n        if batch_idx >= max_batches:\n            break\n        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}\n\n        if imm_enabled:\n            _, info = model(batch, step=step)\n            total_action_loss += info[\"action_loss\"].item()\n\n            scores = info[\"importance_scores\"]\n            k = info[\"k\"]\n\n            for eps in epsilons:\n                key = f\"eps_{eps}\"\n                if key not in results:\n                    results[key] = {\"margins\": [], \"preservation\": []}\n\n                if eps > 0:\n                    batch_noisy = {k_: v.clone() if isinstance(v, torch.Tensor) else v for k_, v in batch.items()}\n                    for img_key in [k_ for k_ in batch_noisy if \"image\" in k_.lower()]:\n                        if isinstance(batch_noisy[img_key], torch.Tensor) and batch_noisy[img_key].is_floating_point():\n                            batch_noisy[img_key] = (batch_noisy[img_key] + eps * torch.randn_like(batch_noisy[img_key])).clamp(0, 1)\n                    _, info_noisy = model(batch_noisy, step=step)\n                    scores_noisy = info_noisy[\"importance_scores\"]\n                else:\n                    scores_noisy = scores\n\n                margin = compute_margin(scores, k)\n                pres = topk_preservation_rate(scores, scores_noisy, k)\n                results[key][\"margins\"].append(margin.cpu())\n                results[key][\"preservation\"].append(pres.cpu())\n        else:\n            loss, info = model.forward_baseline(batch) if hasattr(model, \"forward_baseline\") else (model(batch), {})\n            if isinstance(loss, tuple):\n                loss = loss[0]\n            total_action_loss += (info.get(\"action_loss\", loss) if isinstance(info, dict) else loss).item()\n\n        n_batches += 1\n\n    metrics = {\"eval/action_loss\": total_action_loss / max(n_batches, 1)}\n\n    if imm_enabled:\n        for eps_key, data in results.items():\n            margins = torch.cat(data[\"margins\"])\n            pres = torch.cat(data[\"preservation\"])\n            metrics[f\"eval/{eps_key}/margin_mean\"] = margins.mean().item()\n            metrics[f\"eval/{eps_key}/margin_median\"] = margins.median().item()\n            metrics[f\"eval/{eps_key}/margin_std\"] = margins.std().item()\n            metrics[f\"eval/{eps_key}/preservation_rate\"] = pres.mean().item()\n\n    model.train()\n    return metrics\n\n\nclass GracefulExit:\n    \"\"\"Handle SIGINT/SIGTERM for graceful checkpoint saving.\"\"\"\n\n    def __init__(self):\n        self.should_exit = False\n        signal.signal(signal.SIGINT, self._handler)\n        signal.signal(signal.SIGTERM, self._handler)\n\n    def _handler(self, signum, frame):\n        log.info(\"Received signal %d, will exit after current step\", signum)\n        self.should_exit = True\n\n\ndef main():\n    args = parse_args()\n    config = load_config(args.config)\n    set_seed(args.seed)\n\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    log.info(\"Device: %s\", device)\n\n    train_cfg = config[\"training\"]\n    total_steps = train_cfg.get(\"total_steps\", 30000)\n    eval_every = train_cfg.get(\"eval_every\", 2000)\n    save_every = train_cfg.get(\"save_every\", 5000)\n    log_every = train_cfg.get(\"log_every\", 50)\n    grad_clip = train_cfg.get(\"grad_clip\", 10.0)\n\n    imm_enabled = config.get(\"imm\", {}).get(\"enabled\", False)\n\n    output_dir = train_cfg.get(\"output_dir\", f\"checkpoints/{'imm' if imm_enabled else 'baseline'}\")\n    config[\"training\"][\"output_dir\"] = output_dir\n\n    # Model\n    log.info(\"Loading SmolVLA policy...\")\n    policy = load_smolvla_policy(config, device)\n\n    if imm_enabled:\n        log.info(\"Wrapping with IMMSmolVLAWrapper (delta=%.2f, lambda=%.2f)\",\n                 config[\"imm\"].get(\"delta\", 1.0), config[\"imm\"].get(\"lambda_margin\", 0.1))\n        model = wrap_with_imm(policy, config)\n        model.to(device)\n    else:\n        model = policy\n\n    # Dataset\n    log.info(\"Loading dataset...\")\n    dataset = load_dataset(config)\n    dataloader = make_dataloader(dataset, config)\n    dataloader_iter = iter(dataloader)\n\n    eval_dataset = load_dataset(config)\n    eval_dataloader = make_dataloader(eval_dataset, {**config, \"training\": {**train_cfg, \"batch_size\": train_cfg.get(\"eval_batch_size\", train_cfg.get(\"batch_size\", 4))}})\n\n    # Optimizer / Scheduler\n    optimizer = make_optimizer(model, config)\n    scheduler = make_scheduler(optimizer, config)\n\n    # Resume\n    start_step = 0\n    if args.resume:\n        start_step = load_checkpoint(args.resume, model, optimizer, scheduler, device)\n\n    # W&B\n    run_name = args.wandb_run or (f\"{'imm' if imm_enabled else 'baseline'}_seed{args.seed}\")\n    wandb.init(project=args.wandb_project, name=run_name, config=config, resume=\"allow\")\n\n    # Training loop\n    graceful = GracefulExit()\n    model.train()\n    t0 = time.time()\n    last_info = None\n\n    log.info(\"Starting training from step %d to %d\", start_step, total_steps)\n\n    for step in range(start_step, total_steps):\n        try:\n            batch = next(dataloader_iter)\n        except StopIteration:\n            dataloader_iter = iter(dataloader)\n            batch = next(dataloader_iter)\n\n        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}\n\n        if imm_enabled:\n            total_loss, info = model(batch, step=step)\n            last_info = info\n        else:\n            if hasattr(model, \"forward_baseline\"):\n                total_loss, info = model.forward_baseline(batch)\n                last_info = info\n            else:\n                output = model(batch)\n                if isinstance(output, dict):\n                    total_loss = output[\"loss\"]\n                    info = {\"action_loss\": total_loss.detach()}\n                elif isinstance(output, tuple):\n                    total_loss = output[0]\n                    info = output[1] if len(output) > 1 else {\"action_loss\": total_loss.detach()}\n                else:\n                    total_loss = output\n                    info = {\"action_loss\": total_loss.detach()}\n                last_info = info\n\n        optimizer.zero_grad()\n        total_loss.backward()\n        grad_norm = torch.nn.utils.clip_grad_norm_(\n            [p for p in model.parameters() if p.requires_grad], grad_clip\n        )\n        optimizer.step()\n        scheduler.step()\n\n        # Logging\n        if step % log_every == 0:\n            log_dict = {\n                \"train/total_loss\": total_loss.item(),\n                \"train/grad_norm\": grad_norm.item() if isinstance(grad_norm, torch.Tensor) else grad_norm,\n                \"train/lr\": optimizer.param_groups[0][\"lr\"],\n                \"train/step\": step,\n            }\n\n            if imm_enabled and isinstance(last_info, dict):\n                log_dict.update({\n                    \"train/action_loss\": last_info.get(\"action_loss\", torch.tensor(0.0)).item(),\n                    \"train/margin_loss\": last_info.get(\"margin_loss\", torch.tensor(0.0)).item(),\n                    \"train/lambda\": last_info.get(\"lambda\", torch.tensor(0.0)).item(),\n                })\n                if \"margin\" in last_info:\n                    margins = last_info[\"margin\"]\n                    log_dict.update({\n                        \"margin/mean\": margins.mean().item(),\n                        \"margin/median\": margins.median().item(),\n                        \"margin/std\": margins.std().item(),\n                        \"margin/min\": margins.min().item(),\n                        \"margin/max\": margins.max().item(),\n                    })\n                    log_dict[\"margin/histogram\"] = wandb.Histogram(margins.cpu().numpy())\n                if \"importance_scores\" in last_info:\n                    scores = last_info[\"importance_scores\"]\n                    k = last_info.get(\"k\", int(scores.shape[1] * 0.5))\n                    topk_vals, _ = torch.topk(scores, k, dim=-1)\n                    log_dict[\"scores/topk_mean\"] = topk_vals.mean().item()\n                if \"lipschitz_estimate\" in last_info:\n                    L = last_info[\"lipschitz_estimate\"]\n                    if \"margin\" in last_info:\n                        eps_test = 0.01\n                        k_val = last_info.get(\"k\", 64)\n                        ratio = L * eps_test * k_val / margins.clamp(min=1e-8)\n                        log_dict[\"gate/L_eps_delta_ratio_mean\"] = ratio.mean().item()\n                        log_dict[\"gate/lipschitz_estimate\"] = L\n            else:\n                if isinstance(last_info, dict) and \"action_loss\" in last_info:\n                    log_dict[\"train/action_loss\"] = last_info[\"action_loss\"].item() if isinstance(last_info[\"action_loss\"], torch.Tensor) else last_info[\"action_loss\"]\n\n            wandb.log(log_dict, step=step)\n\n            elapsed = time.time() - t0\n            steps_done = step - start_step + 1\n            sps = steps_done / elapsed if elapsed > 0 else 0\n            log.info(\n                \"step=%d/%d  loss=%.4f  lr=%.2e  grad=%.2f  sps=%.1f\",\n                step, total_steps, total_loss.item(),\n                optimizer.param_groups[0][\"lr\"], grad_norm, sps,\n            )\n\n        # Eval\n        if step > 0 and step % eval_every == 0:\n            log.info(\"Running evaluation at step %d...\", step)\n            eval_metrics = evaluate(model, eval_dataloader, step, config, device, imm_enabled)\n            wandb.log(eval_metrics, step=step)\n            for k, v in eval_metrics.items():\n                log.info(\"  %s: %.4f\", k, v)\n\n        # Checkpoint\n        if step > 0 and step % save_every == 0:\n            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir)\n\n        if graceful.should_exit:\n            log.info(\"Graceful exit at step %d\", step)\n            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir)\n            break\n\n    # Final checkpoint\n    if not graceful.should_exit:\n        save_checkpoint(model, optimizer, scheduler, total_steps - 1, config, last_info, output_dir)\n\n    wandb.finish()\n    log.info(\"Training complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 535,
      "startLine": 1,
      "totalLines": 535
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01GHsXUXNMQr3qxPSUnf1hcw`</summary>

```json
{
  "command": "git clone --depth 1 https://github.com/huggingface/lerobot.git /tmp/lerobot 2>&1 | tail -3",
  "description": "Clone lerobot repo for API reference",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "848ba8a8-6c03-439f-a5f0-876bca8468db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wu8dgR6bbmbjWJ1duWVXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 24556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17968
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

_source line 22 · 2026-05-15T12:03:48.561Z_

<details><summary>↩ Tool result · `toolu_01GHsXUXNMQr3qxPSUnf1hcw`</summary>

```text
Cloning into '/tmp/lerobot'...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "4300a12b-f829-4db1-84e3-2d3a70c2d241",
  "tool_use_result": {
    "stdout": "Cloning into '/tmp/lerobot'...",
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

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me read the lerobot source code to understand the real API. Let me find the key files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "e7494220-aaa5-4484-9353-f1784839e701",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mh1SBnW1jiMoHBLjeKjv5A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13787,
      "cache_read_input_tokens": 42524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13787
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

Now let me study the real lerobot SmolVLA API.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "7515ec1e-a73f-45f1-b474-6aea652fa1a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mh1SBnW1jiMoHBLjeKjv5A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13787,
      "cache_read_input_tokens": 42524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13787
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

<details open><summary>🔧 Tool call — Glob · `toolu_01KUq16TDoazDnzKpDNnvcu5`</summary>

```json
{
  "pattern": "**/smolvla/**/*.py",
  "path": "/tmp/lerobot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "77afd088-244f-456f-8a39-a6273c2f1f4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mh1SBnW1jiMoHBLjeKjv5A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13787,
      "cache_read_input_tokens": 42524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13787
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

_source line 26 · 2026-05-15T12:03:52.370Z_

<details><summary>↩ Tool result · `toolu_01KUq16TDoazDnzKpDNnvcu5`</summary>

```text
/tmp/lerobot/examples/tutorial/smolvla/using_smolvla_example.py
/tmp/lerobot/src/lerobot/policies/smolvla/smolvlm_with_expert.py
/tmp/lerobot/src/lerobot/policies/smolvla/processor_smolvla.py
/tmp/lerobot/src/lerobot/policies/smolvla/modeling_smolvla.py
/tmp/lerobot/src/lerobot/policies/smolvla/configuration_smolvla.py
/tmp/lerobot/src/lerobot/policies/smolvla/__init__.py
/tmp/lerobot/tests/policies/smolvla/test_smolvla_rtc.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "c60b573b-bcda-4316-9f92-6a69a7d7b2f8",
  "tool_use_result": {
    "filenames": [
      "/tmp/lerobot/examples/tutorial/smolvla/using_smolvla_example.py",
      "/tmp/lerobot/src/lerobot/policies/smolvla/smolvlm_with_expert.py",
      "/tmp/lerobot/src/lerobot/policies/smolvla/processor_smolvla.py",
      "/tmp/lerobot/src/lerobot/policies/smolvla/modeling_smolvla.py",
      "/tmp/lerobot/src/lerobot/policies/smolvla/configuration_smolvla.py",
      "/tmp/lerobot/src/lerobot/policies/smolvla/__init__.py",
      "/tmp/lerobot/tests/policies/smolvla/test_smolvla_rtc.py"
    ],
    "durationMs": 14,
    "numFiles": 7,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_012LTQYX8CAxVm1SnfkMFkxd`</summary>

```json
{
  "file_path": "/tmp/lerobot/src/lerobot/policies/smolvla/modeling_smolvla.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "e6130094-7747-41c5-8383-745ba1e430a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRn6TVoDkF1nvcjdvRSNZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 332,
      "cache_read_input_tokens": 56311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 332
      },
      "output_tokens": 62,
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

<details open><summary>🔧 Tool call — Read · `toolu_01YKhpsKjqUqCJwjZ1hz1nXQ`</summary>

```json
{
  "file_path": "/tmp/lerobot/src/lerobot/policies/smolvla/smolvlm_with_expert.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "5a19a4ad-c9e3-4623-8116-53a165dfa54a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRn6TVoDkF1nvcjdvRSNZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 332,
      "cache_read_input_tokens": 56311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 332
      },
      "output_tokens": 62,
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

_source line 29 · 2026-05-15T12:03:55.320Z_

<details><summary>↩ Tool result · `toolu_01YKhpsKjqUqCJwjZ1hz1nXQ`</summary>

```text
1	# Copyright 2025 The HuggingFace Inc. team. All rights reserved.
2	#
3	# Licensed under the Apache License, Version 2.0 (the "License");
4	# you may not use this file except in compliance with the License.
5	# You may obtain a copy of the License at
6	#
7	#     http://www.apache.org/licenses/LICENSE-2.0
8	#
9	# Unless required by applicable law or agreed to in writing, software
10	# distributed under the License is distributed on an "AS IS" BASIS,
11	# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
12	# See the License for the specific language governing permissions and
13	# limitations under the License.
14	
15	import copy
16	from typing import TYPE_CHECKING
17	
18	import torch
19	from torch import nn
20	
21	from lerobot.utils.import_utils import _transformers_available, require_package
22	
23	if TYPE_CHECKING or _transformers_available:
24	    from transformers import (
25	        AutoConfig,
26	        AutoModel,
27	        AutoModelForImageTextToText,
28	        AutoProcessor,
29	        SmolVLMForConditionalGeneration,
30	    )
31	else:
32	    AutoConfig = None
33	    AutoModel = None
34	    AutoModelForImageTextToText = None
35	    AutoProcessor = None
36	    SmolVLMForConditionalGeneration = None
37	
38	
39	def apply_rope(x, positions, max_wavelength=10_000):
40	    """
41	    Applies RoPE positions [B, L] to x [B, L, H, D].
42	    """
43	    d_half = x.shape[-1] // 2
44	    device = x.device
45	    dtype = x.dtype
46	    x = x.to(torch.float32)
47	
48	    freq_exponents = (2.0 / x.shape[-1]) * torch.arange(d_half, dtype=torch.float32, device=device)
49	    timescale = max_wavelength**freq_exponents
50	    radians = positions[..., None].to(torch.float32) / timescale[None, None, :].to(torch.float32)
51	
52	    radians = radians[..., None, :]
53	
54	    sin = torch.sin(radians)  # .to(dtype=dtype)
55	    cos = torch.cos(radians)  # .to(dtype=dtype)
56	
57	    x1, x2 = x.split(d_half, dim=-1)
58	    res = torch.empty_like(x)
59	    res[..., :d_half] = x1 * cos - x2 * sin
60	    res[..., d_half:] = x2 * cos + x1 * sin
61	
62	    return res.to(dtype)
63	
64	
65	def get_intermediate_size(hidden_dim, ffn_dim_multiplier=4, multiple_of=256):
66	    hidden_dim = int(2 * hidden_dim / 3)
67	    hidden_dim = int(ffn_dim_multiplier * hidden_dim)
68	    hidden_dim = multiple_of * ((hidden_dim + multiple_of - 1) // multiple_of)
69	    return hidden_dim
70	
71	
72	class SmolVLMWithExpertModel(nn.Module):
73	    def __init__(
74	        self,
75	        model_id: str = "HuggingFaceTB/SmolVLM2-500M-Video-Instruct",
76	        load_vlm_weights: bool = True,
77	        train_expert_only: bool = True,
78	        freeze_vision_encoder: bool = False,
79	        attention_mode: str = "self_attn",
80	        num_expert_layers: int = -1,
81	        num_vlm_layers: int = -1,
82	        self_attn_every_n_layers: int = -1,
83	        expert_width_multiplier: float = 0.5,
84	        device: str = "auto",
85	    ):
86	        super().__init__()
87	        require_package("transformers", extra="smolvla")
88	        if load_vlm_weights:
89	            print(f"Loading  {model_id} weights ...")
90	            self.vlm = AutoModelForImageTextToText.from_pretrained(
91	                model_id,
92	                torch_dtype="bfloat16",
93	                low_cpu_mem_usage=True,
94	            )
95	            config = self.vlm.config
96	        else:
97	            config = AutoConfig.from_pretrained(model_id)
98	            self.vlm = SmolVLMForConditionalGeneration(config=config)
99	        self.processor = AutoProcessor.from_pretrained(model_id)
100	        if num_vlm_layers > 0:
101	            print(f"Reducing the number of VLM layers to {num_vlm_layers} ...")
102	            self.get_vlm_model().text_model.layers = self.get_vlm_model().text_model.layers[:num_vlm_layers]
103	        self.num_vlm_layers = len(self.get_vlm_model().text_model.layers)
104	        self.config = config
105	        # Smaller lm expert
106	        lm_expert_config = copy.deepcopy(config.text_config)
107	        hidden_size = lm_expert_config.hidden_size
108	        lm_expert_config.hidden_size = int(hidden_size * expert_width_multiplier)  # hidden_size // 2
109	        lm_expert_config.intermediate_size = get_intermediate_size(int(hidden_size * expert_width_multiplier))
110	        lm_expert_config.num_hidden_layers = self.num_vlm_layers
111	        if num_expert_layers > 0:
112	            assert len(self.get_vlm_model().text_model.layers) % num_expert_layers == 0, (
113	                f"Number of layers in the VLM {len(self.get_vlm_model().text_model.layers)} are not multiple of num_expert_layers {num_expert_layers}"
114	            )
115	            lm_expert_config.num_hidden_layers = num_expert_layers
116	        self.lm_expert = AutoModel.from_config(lm_expert_config)
117	
118	        self.num_expert_layers = len(self.lm_expert.layers)
119	        self.self_attn_every_n_layers = self_attn_every_n_layers
120	        if "cross" in attention_mode:
121	            # Reshape qkv projections to have the same input dimension as the vlm
122	            for layer_idx in range(len(self.lm_expert.layers)):
123	                if self.self_attn_every_n_layers > 0 and layer_idx % self.self_attn_every_n_layers == 0:
124	                    continue
125	                self.lm_expert.layers[layer_idx].self_attn.k_proj = nn.Linear(
126	                    config.text_config.num_key_value_heads * config.text_config.head_dim,
127	                    lm_expert_config.num_key_value_heads * lm_expert_config.head_dim,
128	                    bias=lm_expert_config.attention_bias,
129	                )
130	                self.lm_expert.layers[layer_idx].self_attn.v_proj = nn.Linear(
131	                    config.text_config.num_key_value_heads * config.text_config.head_dim,
132	                    lm_expert_config.num_key_value_heads * lm_expert_config.head_dim,
133	                    bias=lm_expert_config.attention_bias,
134	                )
135	        # Remove unused embed_tokens
136	        self.lm_expert.embed_tokens = None
137	
138	        self.num_attention_heads = self.config.text_config.num_attention_heads
139	        self.num_key_value_heads = self.config.text_config.num_key_value_heads
140	
141	        self.freeze_vision_encoder = freeze_vision_encoder
142	        self.train_expert_only = train_expert_only
143	        self.attention_mode = attention_mode
144	        self.expert_hidden_size = lm_expert_config.hidden_size
145	        self.set_requires_grad()
146	
147	    def get_vlm_model(self):
148	        return self.vlm.model
149	
150	    def set_requires_grad(self):
151	        if self.freeze_vision_encoder:
152	            self.get_vlm_model().vision_model.eval()
153	            for params in self.get_vlm_model().vision_model.parameters():
154	                params.requires_grad = False
155	        if self.train_expert_only:
156	            self.vlm.eval()
157	            for params in self.vlm.parameters():
158	                params.requires_grad = False
159	        else:
160	            # To avoid unused params issue with distributed training
161	            last_layers = [self.num_vlm_layers - 1]
162	            if (
163	                self.num_vlm_layers != self.num_expert_layers
164	                and self.num_vlm_layers % self.num_expert_layers == 0
165	            ):
166	                last_layers.append(self.num_vlm_layers - 2)
167	            frozen_layers = [
168	                "lm_head",
169	                "text_model.model.norm.weight",
170	            ]
171	            for layer in last_layers:
172	                frozen_layers.append(f"text_model.model.layers.{layer}.")
173	
174	            for name, params in self.vlm.named_parameters():
175	                if any(k in name for k in frozen_layers):
176	                    params.requires_grad = False
177	        # To avoid unused params issue with distributed training
178	        for name, params in self.lm_expert.named_parameters():
179	            if "lm_head" in name:
180	                params.requires_grad = False
181	
182	    def train(self, mode: bool = True):
183	        super().train(mode)
184	
185	        if self.freeze_vision_encoder:
186	            self.get_vlm_model().vision_model.eval()
187	
188	        if self.train_expert_only:
189	            self.vlm.eval()
190	
191	    def embed_image(self, image: torch.Tensor):
192	        patch_attention_mask = None
193	        # Get sequence from the vision encoder
194	        image_hidden_states = (
195	            self.get_vlm_model()
196	            .vision_model(
197	                pixel_values=image.to(dtype=self.get_vlm_model().vision_model.dtype),
198	                patch_attention_mask=patch_attention_mask,
199	            )
200	            .last_hidden_state
201	        )
202	        # Modality projection & resampling
203	        image_hidden_states = self.get_vlm_model().connector(image_hidden_states)
204	        return image_hidden_states
205	
206	    def embed_language_tokens(self, tokens: torch.Tensor):
207	        return self.get_vlm_model().text_model.get_input_embeddings()(tokens)
208	
209	    def forward_attn_layer(
210	        self,
211	        model_layers,
212	        inputs_embeds,
213	        layer_idx,
214	        position_ids,
215	        attention_mask,
216	        batch_size,
217	        head_dim,
218	        use_cache: bool = True,
219	        fill_kv_cache: bool = True,
220	        past_key_values=None,
221	    ) -> list[torch.Tensor]:
222	        query_states = []
223	        key_states = []
224	        value_states = []
225	        for i, hidden_states in enumerate(inputs_embeds):
226	            layer = model_layers[i][layer_idx]
227	            if hidden_states is None or layer is None:
228	                continue
229	            hidden_states = layer.input_layernorm(hidden_states)
230	
231	            input_shape = hidden_states.shape[:-1]
232	            hidden_shape = (*input_shape, -1, layer.self_attn.head_dim)
233	
234	            hidden_states = hidden_states.to(dtype=layer.self_attn.q_proj.weight.dtype)
235	            query_state = layer.self_attn.q_proj(hidden_states).view(hidden_shape)
236	            key_state = layer.self_attn.k_proj(hidden_states).view(hidden_shape)
237	            value_state = layer.self_attn.v_proj(hidden_states).view(hidden_shape)
238	
239	            query_states.append(query_state)
240	            key_states.append(key_state)
241	            value_states.append(value_state)
242	
243	        # B,L,H,D with L sequence length, H number of heads, D head dim
244	        # concatenate on the number of embeddings/tokens
245	        query_states = torch.cat(query_states, dim=1)
246	        key_states = torch.cat(key_states, dim=1)
247	        value_states = torch.cat(value_states, dim=1)
248	        seq_len = query_states.shape[1]
249	        if seq_len < position_ids.shape[1]:
250	            _position_ids = position_ids[:, :seq_len]
251	            _attention_mask = attention_mask[:, :seq_len, :seq_len]
252	        else:
253	            _position_ids = position_ids
254	            _attention_mask = attention_mask
255	
256	        attention_mask_ = _attention_mask
257	        position_ids_ = _position_ids
258	
259	        query_states = apply_rope(query_states, position_ids_)
260	        key_states = apply_rope(key_states, position_ids_)
261	
262	        if use_cache and past_key_values is None:
263	            past_key_values = {}
264	
265	        if use_cache:
266	            if fill_kv_cache:
267	                past_key_values[layer_idx] = {
268	                    "key_states": key_states,
269	                    "value_states": value_states,
270	                }
271	            else:
272	                # TODO here, some optimization can be done - similar to a `StaticCache` we can declare the `max_len` before.
273	                # so we create an empty cache, with just one cuda malloc, and if (in autoregressive case) we reach
274	                # the max len, then we (for instance) double the cache size. This implementation already exists
275	                # in `transformers`. (molbap)
276	                key_states = torch.cat([past_key_values[layer_idx]["key_states"], key_states], dim=1)
277	                value_states = torch.cat([past_key_values[layer_idx]["value_states"], value_states], dim=1)
278	
279	        attention_interface = self.get_attention_interface()
280	
281	        att_output = attention_interface(
282	            attention_mask_, batch_size, head_dim, query_states, key_states, value_states
283	        )
284	        return [att_output], past_key_values
285	
286	    def forward_cross_attn_layer(
287	        self,
288	        model_layers,
289	        inputs_embeds,
290	        layer_idx,
291	        position_ids,
292	        attention_mask,
293	        batch_size,
294	        head_dim,
295	        use_cache: bool = True,
296	        fill_kv_cache: bool = True,
297	        past_key_values=None,
298	    ) -> list[torch.Tensor]:
299	        attention_interface = self.get_attention_interface()
300	
301	        att_outputs = []
302	        assert len(inputs_embeds) == 2 or (use_cache and past_key_values is not None and not fill_kv_cache), (
303	            f"Both len(inputs_embeds) == {len(inputs_embeds)} and past_key_values is {past_key_values}"
304	        )
305	
306	        if len(inputs_embeds) == 2 and not past_key_values:
307	            # Prefix attention
308	            seq_len = inputs_embeds[0].shape[1]
309	            position_id, expert_position_id = position_ids[:, :seq_len], position_ids[:, seq_len:]
310	            prefix_attention_mask = attention_mask[:, :seq_len, :seq_len]
311	
312	            layer = model_layers[0][layer_idx]
313	
314	            hidden_states = layer.input_layernorm(inputs_embeds[0])
315	
316	            input_shape = hidden_states.shape[:-1]
317	            hidden_shape = (*input_shape, -1, layer.self_attn.head_dim)
318	
319	            hidden_states = hidden_states.to(dtype=layer.self_attn.q_proj.weight.dtype)
320	            query_state = layer.self_attn.q_proj(hidden_states).view(hidden_shape)
321	            key_state = layer.self_attn.k_proj(hidden_states).view(hidden_shape)
322	            value_states = layer.self_attn.v_proj(hidden_states).view(hidden_shape)
323	
324	            # B,L,H,D with L sequence length, H number of heads, D head dim
325	            query_states = apply_rope(query_state, position_id)
326	            key_states = apply_rope(key_state, position_id)
327	
328	            att_output = attention_interface(
329	                prefix_attention_mask, batch_size, head_dim, query_states, key_states, value_states
330	            )
331	            att_outputs.append(att_output)
332	        else:
333	            expert_position_id = position_ids
334	
335	        if use_cache and past_key_values is None:
336	            past_key_values = {}
337	
338	        if use_cache:
339	            if fill_kv_cache:
340	                past_key_values[layer_idx] = {
341	                    "key_states": key_states,
342	                    "value_states": value_states,
343	                }
344	            else:
345	                # TODO here, some optimization can be done - similar to a `StaticCache` we can declare the `max_len` before.
346	                # so we create an empty cache, with just one cuda malloc, and if (in autoregressive case) we reach
347	                # the max len, then we (for instance) double the cache size. This implementation already exists
348	                # in `transformers`. (molbap)
349	                key_states = past_key_values[layer_idx]["key_states"]
350	                value_states = past_key_values[layer_idx]["value_states"]
351	
352	        # Expert
353	        expert_layer = model_layers[1][layer_idx]
354	        if expert_layer is not None:
355	            expert_hidden_states = expert_layer.input_layernorm(inputs_embeds[1])
356	
357	            expert_input_shape = expert_hidden_states.shape[:-1]
358	            expert_hidden_shape = (*expert_input_shape, -1, expert_layer.self_attn.head_dim)
359	
360	            expert_hidden_states = expert_hidden_states.to(dtype=expert_layer.self_attn.q_proj.weight.dtype)
361	            expert_query_state = expert_layer.self_attn.q_proj(expert_hidden_states).view(expert_hidden_shape)
362	
363	            _key_states = key_states.to(dtype=expert_layer.self_attn.k_proj.weight.dtype).view(
364	                *key_states.shape[:2], -1
365	            )
366	            expert_key_states = expert_layer.self_attn.k_proj(_key_states).view(
367	                *_key_states.shape[:-1], -1, expert_layer.self_attn.head_dim
368	            )  # k_proj should have same dim as kv
369	
370	            _value_states = value_states.to(dtype=expert_layer.self_attn.v_proj.weight.dtype).view(
371	                *value_states.shape[:2], -1
372	            )
373	            expert_value_states = expert_layer.self_attn.v_proj(_value_states).view(
374	                *_value_states.shape[:-1], -1, expert_layer.self_attn.head_dim
375	            )
376	
377	            expert_position_id = (
378	                expert_position_id - torch.min(expert_position_id, dim=1, keepdim=True).values
379	            )  # start from 0
380	            expert_attention_mask = attention_mask[
381	                :, -inputs_embeds[1].shape[1] :, : expert_key_states.shape[1] :
382	            ]  # take into account kv
383	
384	            expert_query_states = apply_rope(expert_query_state, expert_position_id)
385	
386	            att_output = attention_interface(
387	                expert_attention_mask,
388	                batch_size,
389	                head_dim,
390	                expert_query_states,
391	                expert_key_states,
392	                expert_value_states,
393	            )
394	            att_outputs.append(att_output)
395	        else:
396	            att_outputs.append(None)
397	
398	        # att_output = att_output.to(dtype=models[i].dtype)
399	        return att_outputs, past_key_values
400	
401	    def get_model_layers(self, models: list) -> list:
402	        vlm_layers = []
403	        expert_layers = []
404	        multiple_of = self.num_vlm_layers // self.num_expert_layers
405	        for i in range(self.num_vlm_layers):
406	            if multiple_of > 0 and i > 0 and i % multiple_of != 0:
407	                expert_layer = None
408	            else:
409	                expert_layer_index = i // multiple_of if multiple_of > 0 else i
410	                expert_layer = models[1].layers[expert_layer_index]
411	            vlm_layers.append(models[0].layers[i])
412	            expert_layers.append(expert_layer)
413	        return [vlm_layers, expert_layers]
414	
415	    def forward(
416	        self,
417	        attention_mask: torch.Tensor | None = None,
418	        position_ids: torch.LongTensor | None = None,
419	        past_key_values: list[torch.FloatTensor] | None = None,
420	        inputs_embeds: list[torch.FloatTensor] = None,
421	        use_cache: bool | None = None,
422	        fill_kv_cache: bool | None = None,
423	    ):
424	        models = [self.get_vlm_model().text_model, self.lm_expert]
425	        model_layers = self.get_model_layers(models)
426	        for hidden_states in inputs_embeds:
427	            # TODO this is very inefficient
428	            # dtype is always the same, batch size too (if > 1 len)
429	            # device could be trickier in multi gpu edge cases but that's it
430	            if hidden_states is None:
431	                continue
432	            batch_size = hidden_states.shape[0]
433	
434	        # RMSNorm
435	        num_layers = self.num_vlm_layers
436	        head_dim = self.vlm.config.text_config.head_dim
437	        for layer_idx in range(num_layers):
438	            if (
439	                fill_kv_cache
440	                or "cross" not in self.attention_mode
441	                or (self.self_attn_every_n_layers > 0 and layer_idx % self.self_attn_every_n_layers == 0)
442	            ):
443	                att_outputs, past_key_values = self.forward_attn_layer(
444	                    model_layers,
445	                    inputs_embeds,
446	                    layer_idx,
447	                    position_ids,
448	                    attention_mask,
449	                    batch_size,
450	                    head_dim,
451	                    use_cache=use_cache,
452	                    fill_kv_cache=fill_kv_cache,
453	                    past_key_values=past_key_values,
454	                )
455	            else:
456	                att_outputs, past_key_values = self.forward_cross_attn_layer(
457	                    model_layers,
458	                    inputs_embeds,
459	                    layer_idx,
460	                    position_ids,
461	                    attention_mask,
462	                    batch_size,
463	                    head_dim,
464	                    use_cache=use_cache,
465	                    fill_kv_cache=fill_kv_cache,
466	                    past_key_values=past_key_values,
467	                )
468	            outputs_embeds = []
469	            start = 0
470	            for i, hidden_states in enumerate(inputs_embeds):
471	                layer = model_layers[i][layer_idx]
472	                att_output = (
473	                    att_outputs[i] if i < len(att_outputs) else att_outputs[0]
474	                )  # in case of self_attn
475	                if hidden_states is not None:
476	                    if layer is None:
477	                        outputs_embeds.append(hidden_states)
478	                        continue
479	                    end = start + hidden_states.shape[1]
480	
481	                    if att_output.dtype != layer.self_attn.o_proj.weight.dtype:
482	                        att_output = att_output.to(layer.self_attn.o_proj.weight.dtype)
483	                    att_out = att_output[:, start:end]
484	                    out_emb = layer.self_attn.o_proj(att_out)
485	
486	                    out_emb += hidden_states
487	                    after_first_residual = out_emb.clone()
488	
489	                    out_emb = layer.post_attention_layernorm(out_emb)
490	                    out_emb = layer.mlp(out_emb)
491	
492	                    out_emb += after_first_residual
493	
494	                    outputs_embeds.append(out_emb)
495	
496	                    start = end if len(att_outputs) == 1 else 0
497	                else:
498	                    outputs_embeds.append(None)
499	
500	            inputs_embeds = outputs_embeds
501	
502	        # final norm
503	        outputs_embeds = []
504	        for i, hidden_states in enumerate(inputs_embeds):
505	            if hidden_states is not None:
506	                out_emb = models[i].norm(hidden_states)
507	                outputs_embeds.append(out_emb)
508	            else:
509	                outputs_embeds.append(None)
510	        return outputs_embeds, past_key_values
511	
512	    def get_attention_interface(self):
513	        attention_interface = self.eager_attention_forward
514	        return attention_interface
515	
516	    def eager_attention_forward(
517	        self, attention_mask, batch_size, head_dim, query_states, key_states, value_states
518	    ):
519	        num_att_heads = self.num_attention_heads
520	        num_key_value_heads = self.num_key_value_heads
521	        num_key_value_groups = num_att_heads // num_key_value_heads
522	
523	        sequence_length = key_states.shape[1]
524	
525	        key_states = key_states[:, :, :, None, :].expand(
526	            batch_size, sequence_length, num_key_value_heads, num_key_value_groups, head_dim
527	        )
528	        key_states = key_states.reshape(
529	            batch_size, sequence_length, num_key_value_heads * num_key_value_groups, head_dim
530	        )
531	
532	        value_states = value_states[:, :, :, None, :].expand(
533	            batch_size, sequence_length, num_key_value_heads, num_key_value_groups, head_dim
534	        )
535	        value_states = value_states.reshape(
536	            batch_size, sequence_length, num_key_value_heads * num_key_value_groups, head_dim
537	        )
538	
539	        # Attention here is upcasted to float32 to match the original eager implementation.
540	        query_states = query_states.to(dtype=torch.float32)
541	        key_states = key_states.to(dtype=torch.float32)
542	
543	        query_states = query_states.transpose(1, 2)
544	        key_states = key_states.transpose(1, 2)
545	
546	        att_weights = torch.matmul(query_states, key_states.transpose(2, 3))
547	        att_weights *= head_dim**-0.5
548	
549	        att_weights = att_weights.to(dtype=torch.float32)
550	        big_neg = torch.finfo(att_weights.dtype).min  # -2.3819763e38  # See gemma/modules.py
551	        masked_att_weights = torch.where(attention_mask[:, None, :, :], att_weights, big_neg)
552	        probs = nn.functional.softmax(masked_att_weights, dim=-1)
553	        probs = probs.to(dtype=value_states.dtype)
554	
555	        att_output = torch.matmul(probs, value_states.permute(0, 2, 1, 3))
556	
557	        att_output = att_output.permute(0, 2, 1, 3)
558	        # we use -1 because sequence length can change
559	        att_output = att_output.reshape(batch_size, -1, num_key_value_heads * num_key_value_groups * head_dim)
560	
561	        return att_output
562	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "b3f7e97b-2ddf-444b-a61a-889d08fce773",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/lerobot/src/lerobot/policies/smolvla/smolvlm_with_expert.py",
      "content": "# Copyright 2025 The HuggingFace Inc. team. All rights reserved.\n#\n# Licensed under the Apache License, Version 2.0 (the \"License\");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#     http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an \"AS IS\" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n\nimport copy\nfrom typing import TYPE_CHECKING\n\nimport torch\nfrom torch import nn\n\nfrom lerobot.utils.import_utils import _transformers_available, require_package\n\nif TYPE_CHECKING or _transformers_available:\n    from transformers import (\n        AutoConfig,\n        AutoModel,\n        AutoModelForImageTextToText,\n        AutoProcessor,\n        SmolVLMForConditionalGeneration,\n    )\nelse:\n    AutoConfig = None\n    AutoModel = None\n    AutoModelForImageTextToText = None\n    AutoProcessor = None\n    SmolVLMForConditionalGeneration = None\n\n\ndef apply_rope(x, positions, max_wavelength=10_000):\n    \"\"\"\n    Applies RoPE positions [B, L] to x [B, L, H, D].\n    \"\"\"\n    d_half = x.shape[-1] // 2\n    device = x.device\n    dtype = x.dtype\n    x = x.to(torch.float32)\n\n    freq_exponents = (2.0 / x.shape[-1]) * torch.arange(d_half, dtype=torch.float32, device=device)\n    timescale = max_wavelength**freq_exponents\n    radians = positions[..., None].to(torch.float32) / timescale[None, None, :].to(torch.float32)\n\n    radians = radians[..., None, :]\n\n    sin = torch.sin(radians)  # .to(dtype=dtype)\n    cos = torch.cos(radians)  # .to(dtype=dtype)\n\n    x1, x2 = x.split(d_half, dim=-1)\n    res = torch.empty_like(x)\n    res[..., :d_half] = x1 * cos - x2 * sin\n    res[..., d_half:] = x2 * cos + x1 * sin\n\n    return res.to(dtype)\n\n\ndef get_intermediate_size(hidden_dim, ffn_dim_multiplier=4, multiple_of=256):\n    hidden_dim = int(2 * hidden_dim / 3)\n    hidden_dim = int(ffn_dim_multiplier * hidden_dim)\n    hidden_dim = multiple_of * ((hidden_dim + multiple_of - 1) // multiple_of)\n    return hidden_dim\n\n\nclass SmolVLMWithExpertModel(nn.Module):\n    def __init__(\n        self,\n        model_id: str = \"HuggingFaceTB/SmolVLM2-500M-Video-Instruct\",\n        load_vlm_weights: bool = True,\n        train_expert_only: bool = True,\n        freeze_vision_encoder: bool = False,\n        attention_mode: str = \"self_attn\",\n        num_expert_layers: int = -1,\n        num_vlm_layers: int = -1,\n        self_attn_every_n_layers: int = -1,\n        expert_width_multiplier: float = 0.5,\n        device: str = \"auto\",\n    ):\n        super().__init__()\n        require_package(\"transformers\", extra=\"smolvla\")\n        if load_vlm_weights:\n            print(f\"Loading  {model_id} weights ...\")\n            self.vlm = AutoModelForImageTextToText.from_pretrained(\n                model_id,\n                torch_dtype=\"bfloat16\",\n                low_cpu_mem_usage=True,\n            )\n            config = self.vlm.config\n        else:\n            config = AutoConfig.from_pretrained(model_id)\n            self.vlm = SmolVLMForConditionalGeneration(config=config)\n        self.processor = AutoProcessor.from_pretrained(model_id)\n        if num_vlm_layers > 0:\n            print(f\"Reducing the number of VLM layers to {num_vlm_layers} ...\")\n            self.get_vlm_model().text_model.layers = self.get_vlm_model().text_model.layers[:num_vlm_layers]\n        self.num_vlm_layers = len(self.get_vlm_model().text_model.layers)\n        self.config = config\n        # Smaller lm expert\n        lm_expert_config = copy.deepcopy(config.text_config)\n        hidden_size = lm_expert_config.hidden_size\n        lm_expert_config.hidden_size = int(hidden_size * expert_width_multiplier)  # hidden_size // 2\n        lm_expert_config.intermediate_size = get_intermediate_size(int(hidden_size * expert_width_multiplier))\n        lm_expert_config.num_hidden_layers = self.num_vlm_layers\n        if num_expert_layers > 0:\n            assert len(self.get_vlm_model().text_model.layers) % num_expert_layers == 0, (\n                f\"Number of layers in the VLM {len(self.get_vlm_model().text_model.layers)} are not multiple of num_expert_layers {num_expert_layers}\"\n            )\n            lm_expert_config.num_hidden_layers = num_expert_layers\n        self.lm_expert = AutoModel.from_config(lm_expert_config)\n\n        self.num_expert_layers = len(self.lm_expert.layers)\n        self.self_attn_every_n_layers = self_attn_every_n_layers\n        if \"cross\" in attention_mode:\n            # Reshape qkv projections to have the same input dimension as the vlm\n            for layer_idx in range(len(self.lm_expert.layers)):\n                if self.self_attn_every_n_layers > 0 and layer_idx % self.self_attn_every_n_layers == 0:\n                    continue\n                self.lm_expert.layers[layer_idx].self_attn.k_proj = nn.Linear(\n                    config.text_config.num_key_value_heads * config.text_config.head_dim,\n                    lm_expert_config.num_key_value_heads * lm_expert_config.head_dim,\n                    bias=lm_expert_config.attention_bias,\n                )\n                self.lm_expert.layers[layer_idx].self_attn.v_proj = nn.Linear(\n                    config.text_config.num_key_value_heads * config.text_config.head_dim,\n                    lm_expert_config.num_key_value_heads * lm_expert_config.head_dim,\n                    bias=lm_expert_config.attention_bias,\n                )\n        # Remove unused embed_tokens\n        self.lm_expert.embed_tokens = None\n\n        self.num_attention_heads = self.config.text_config.num_attention_heads\n        self.num_key_value_heads = self.config.text_config.num_key_value_heads\n\n        self.freeze_vision_encoder = freeze_vision_encoder\n        self.train_expert_only = train_expert_only\n        self.attention_mode = attention_mode\n        self.expert_hidden_size = lm_expert_config.hidden_size\n        self.set_requires_grad()\n\n    def get_vlm_model(self):\n        return self.vlm.model\n\n    def set_requires_grad(self):\n        if self.freeze_vision_encoder:\n            self.get_vlm_model().vision_model.eval()\n            for params in self.get_vlm_model().vision_model.parameters():\n                params.requires_grad = False\n        if self.train_expert_only:\n            self.vlm.eval()\n            for params in self.vlm.parameters():\n                params.requires_grad = False\n        else:\n            # To avoid unused params issue with distributed training\n            last_layers = [self.num_vlm_layers - 1]\n            if (\n                self.num_vlm_layers != self.num_expert_layers\n                and self.num_vlm_layers % self.num_expert_layers == 0\n            ):\n                last_layers.append(self.num_vlm_layers - 2)\n            frozen_layers = [\n                \"lm_head\",\n                \"text_model.model.norm.weight\",\n            ]\n            for layer in last_layers:\n                frozen_layers.append(f\"text_model.model.layers.{layer}.\")\n\n            for name, params in self.vlm.named_parameters():\n                if any(k in name for k in frozen_layers):\n                    params.requires_grad = False\n        # To avoid unused params issue with distributed training\n        for name, params in self.lm_expert.named_parameters():\n            if \"lm_head\" in name:\n                params.requires_grad = False\n\n    def train(self, mode: bool = True):\n        super().train(mode)\n\n        if self.freeze_vision_encoder:\n            self.get_vlm_model().vision_model.eval()\n\n        if self.train_expert_only:\n            self.vlm.eval()\n\n    def embed_image(self, image: torch.Tensor):\n        patch_attention_mask = None\n        # Get sequence from the vision encoder\n        image_hidden_states = (\n            self.get_vlm_model()\n            .vision_model(\n                pixel_values=image.to(dtype=self.get_vlm_model().vision_model.dtype),\n                patch_attention_mask=patch_attention_mask,\n            )\n            .last_hidden_state\n        )\n        # Modality projection & resampling\n        image_hidden_states = self.get_vlm_model().connector(image_hidden_states)\n        return image_hidden_states\n\n    def embed_language_tokens(self, tokens: torch.Tensor):\n        return self.get_vlm_model().text_model.get_input_embeddings()(tokens)\n\n    def forward_attn_layer(\n        self,\n        model_layers,\n        inputs_embeds,\n        layer_idx,\n        position_ids,\n        attention_mask,\n        batch_size,\n        head_dim,\n        use_cache: bool = True,\n        fill_kv_cache: bool = True,\n        past_key_values=None,\n    ) -> list[torch.Tensor]:\n        query_states = []\n        key_states = []\n        value_states = []\n        for i, hidden_states in enumerate(inputs_embeds):\n            layer = model_layers[i][layer_idx]\n            if hidden_states is None or layer is None:\n                continue\n            hidden_states = layer.input_layernorm(hidden_states)\n\n            input_shape = hidden_states.shape[:-1]\n            hidden_shape = (*input_shape, -1, layer.self_attn.head_dim)\n\n            hidden_states = hidden_states.to(dtype=layer.self_attn.q_proj.weight.dtype)\n            query_state = layer.self_attn.q_proj(hidden_states).view(hidden_shape)\n            key_state = layer.self_attn.k_proj(hidden_states).view(hidden_shape)\n            value_state = layer.self_attn.v_proj(hidden_states).view(hidden_shape)\n\n            query_states.append(query_state)\n            key_states.append(key_state)\n            value_states.append(value_state)\n\n        # B,L,H,D with L sequence length, H number of heads, D head dim\n        # concatenate on the number of embeddings/tokens\n        query_states = torch.cat(query_states, dim=1)\n        key_states = torch.cat(key_states, dim=1)\n        value_states = torch.cat(value_states, dim=1)\n        seq_len = query_states.shape[1]\n        if seq_len < position_ids.shape[1]:\n            _position_ids = position_ids[:, :seq_len]\n            _attention_mask = attention_mask[:, :seq_len, :seq_len]\n        else:\n            _position_ids = position_ids\n            _attention_mask = attention_mask\n\n        attention_mask_ = _attention_mask\n        position_ids_ = _position_ids\n\n        query_states = apply_rope(query_states, position_ids_)\n        key_states = apply_rope(key_states, position_ids_)\n\n        if use_cache and past_key_values is None:\n            past_key_values = {}\n\n        if use_cache:\n            if fill_kv_cache:\n                past_key_values[layer_idx] = {\n                    \"key_states\": key_states,\n                    \"value_states\": value_states,\n                }\n            else:\n                # TODO here, some optimization can be done - similar to a `StaticCache` we can declare the `max_len` before.\n                # so we create an empty cache, with just one cuda malloc, and if (in autoregressive case) we reach\n                # the max len, then we (for instance) double the cache size. This implementation already exists\n                # in `transformers`. (molbap)\n                key_states = torch.cat([past_key_values[layer_idx][\"key_states\"], key_states], dim=1)\n                value_states = torch.cat([past_key_values[layer_idx][\"value_states\"], value_states], dim=1)\n\n        attention_interface = self.get_attention_interface()\n\n        att_output = attention_interface(\n            attention_mask_, batch_size, head_dim, query_states, key_states, value_states\n        )\n        return [att_output], past_key_values\n\n    def forward_cross_attn_layer(\n        self,\n        model_layers,\n        inputs_embeds,\n        layer_idx,\n        position_ids,\n        attention_mask,\n        batch_size,\n        head_dim,\n        use_cache: bool = True,\n        fill_kv_cache: bool = True,\n        past_key_values=None,\n    ) -> list[torch.Tensor]:\n        attention_interface = self.get_attention_interface()\n\n        att_outputs = []\n        assert len(inputs_embeds) == 2 or (use_cache and past_key_values is not None and not fill_kv_cache), (\n            f\"Both len(inputs_embeds) == {len(inputs_embeds)} and past_key_values is {past_key_values}\"\n        )\n\n        if len(inputs_embeds) == 2 and not past_key_values:\n            # Prefix attention\n            seq_len = inputs_embeds[0].shape[1]\n            position_id, expert_position_id = position_ids[:, :seq_len], position_ids[:, seq_len:]\n            prefix_attention_mask = attention_mask[:, :seq_len, :seq_len]\n\n            layer = model_layers[0][layer_idx]\n\n            hidden_states = layer.input_layernorm(inputs_embeds[0])\n\n            input_shape = hidden_states.shape[:-1]\n            hidden_shape = (*input_shape, -1, layer.self_attn.head_dim)\n\n            hidden_states = hidden_states.to(dtype=layer.self_attn.q_proj.weight.dtype)\n            query_state = layer.self_attn.q_proj(hidden_states).view(hidden_shape)\n            key_state = layer.self_attn.k_proj(hidden_states).view(hidden_shape)\n            value_states = layer.self_attn.v_proj(hidden_states).view(hidden_shape)\n\n            # B,L,H,D with L sequence length, H number of heads, D head dim\n            query_states = apply_rope(query_state, position_id)\n            key_states = apply_rope(key_state, position_id)\n\n            att_output = attention_interface(\n                prefix_attention_mask, batch_size, head_dim, query_states, key_states, value_states\n            )\n            att_outputs.append(att_output)\n        else:\n            expert_position_id = position_ids\n\n        if use_cache and past_key_values is None:\n            past_key_values = {}\n\n        if use_cache:\n            if fill_kv_cache:\n                past_key_values[layer_idx] = {\n                    \"key_states\": key_states,\n                    \"value_states\": value_states,\n                }\n            else:\n                # TODO here, some optimization can be done - similar to a `StaticCache` we can declare the `max_len` before.\n                # so we create an empty cache, with just one cuda malloc, and if (in autoregressive case) we reach\n                # the max len, then we (for instance) double the cache size. This implementation already exists\n                # in `transformers`. (molbap)\n                key_states = past_key_values[layer_idx][\"key_states\"]\n                value_states = past_key_values[layer_idx][\"value_states\"]\n\n        # Expert\n        expert_layer = model_layers[1][layer_idx]\n        if expert_layer is not None:\n            expert_hidden_states = expert_layer.input_layernorm(inputs_embeds[1])\n\n            expert_input_shape = expert_hidden_states.shape[:-1]\n            expert_hidden_shape = (*expert_input_shape, -1, expert_layer.self_attn.head_dim)\n\n            expert_hidden_states = expert_hidden_states.to(dtype=expert_layer.self_attn.q_proj.weight.dtype)\n            expert_query_state = expert_layer.self_attn.q_proj(expert_hidden_states).view(expert_hidden_shape)\n\n            _key_states = key_states.to(dtype=expert_layer.self_attn.k_proj.weight.dtype).view(\n                *key_states.shape[:2], -1\n            )\n            expert_key_states = expert_layer.self_attn.k_proj(_key_states).view(\n                *_key_states.shape[:-1], -1, expert_layer.self_attn.head_dim\n            )  # k_proj should have same dim as kv\n\n            _value_states = value_states.to(dtype=expert_layer.self_attn.v_proj.weight.dtype).view(\n                *value_states.shape[:2], -1\n            )\n            expert_value_states = expert_layer.self_attn.v_proj(_value_states).view(\n                *_value_states.shape[:-1], -1, expert_layer.self_attn.head_dim\n            )\n\n            expert_position_id = (\n                expert_position_id - torch.min(expert_position_id, dim=1, keepdim=True).values\n            )  # start from 0\n            expert_attention_mask = attention_mask[\n                :, -inputs_embeds[1].shape[1] :, : expert_key_states.shape[1] :\n            ]  # take into account kv\n\n            expert_query_states = apply_rope(expert_query_state, expert_position_id)\n\n            att_output = attention_interface(\n                expert_attention_mask,\n                batch_size,\n                head_dim,\n                expert_query_states,\n                expert_key_states,\n                expert_value_states,\n            )\n            att_outputs.append(att_output)\n        else:\n            att_outputs.append(None)\n\n        # att_output = att_output.to(dtype=models[i].dtype)\n        return att_outputs, past_key_values\n\n    def get_model_layers(self, models: list) -> list:\n        vlm_layers = []\n        expert_layers = []\n        multiple_of = self.num_vlm_layers // self.num_expert_layers\n        for i in range(self.num_vlm_layers):\n            if multiple_of > 0 and i > 0 and i % multiple_of != 0:\n                expert_layer = None\n            else:\n                expert_layer_index = i // multiple_of if multiple_of > 0 else i\n                expert_layer = models[1].layers[expert_layer_index]\n            vlm_layers.append(models[0].layers[i])\n            expert_layers.append(expert_layer)\n        return [vlm_layers, expert_layers]\n\n    def forward(\n        self,\n        attention_mask: torch.Tensor | None = None,\n        position_ids: torch.LongTensor | None = None,\n        past_key_values: list[torch.FloatTensor] | None = None,\n        inputs_embeds: list[torch.FloatTensor] = None,\n        use_cache: bool | None = None,\n        fill_kv_cache: bool | None = None,\n    ):\n        models = [self.get_vlm_model().text_model, self.lm_expert]\n        model_layers = self.get_model_layers(models)\n        for hidden_states in inputs_embeds:\n            # TODO this is very inefficient\n            # dtype is always the same, batch size too (if > 1 len)\n            # device could be trickier in multi gpu edge cases but that's it\n            if hidden_states is None:\n                continue\n            batch_size = hidden_states.shape[0]\n\n        # RMSNorm\n        num_layers = self.num_vlm_layers\n        head_dim = self.vlm.config.text_config.head_dim\n        for layer_idx in range(num_layers):\n            if (\n                fill_kv_cache\n                or \"cross\" not in self.attention_mode\n                or (self.self_attn_every_n_layers > 0 and layer_idx % self.self_attn_every_n_layers == 0)\n            ):\n                att_outputs, past_key_values = self.forward_attn_layer(\n                    model_layers,\n                    inputs_embeds,\n                    layer_idx,\n                    position_ids,\n                    attention_mask,\n                    batch_size,\n                    head_dim,\n                    use_cache=use_cache,\n                    fill_kv_cache=fill_kv_cache,\n                    past_key_values=past_key_values,\n                )\n            else:\n                att_outputs, past_key_values = self.forward_cross_attn_layer(\n                    model_layers,\n                    inputs_embeds,\n                    layer_idx,\n                    position_ids,\n                    attention_mask,\n                    batch_size,\n                    head_dim,\n                    use_cache=use_cache,\n                    fill_kv_cache=fill_kv_cache,\n                    past_key_values=past_key_values,\n                )\n            outputs_embeds = []\n            start = 0\n            for i, hidden_states in enumerate(inputs_embeds):\n                layer = model_layers[i][layer_idx]\n                att_output = (\n                    att_outputs[i] if i < len(att_outputs) else att_outputs[0]\n                )  # in case of self_attn\n                if hidden_states is not None:\n                    if layer is None:\n                        outputs_embeds.append(hidden_states)\n                        continue\n                    end = start + hidden_states.shape[1]\n\n                    if att_output.dtype != layer.self_attn.o_proj.weight.dtype:\n                        att_output = att_output.to(layer.self_attn.o_proj.weight.dtype)\n                    att_out = att_output[:, start:end]\n                    out_emb = layer.self_attn.o_proj(att_out)\n\n                    out_emb += hidden_states\n                    after_first_residual = out_emb.clone()\n\n                    out_emb = layer.post_attention_layernorm(out_emb)\n                    out_emb = layer.mlp(out_emb)\n\n                    out_emb += after_first_residual\n\n                    outputs_embeds.append(out_emb)\n\n                    start = end if len(att_outputs) == 1 else 0\n                else:\n                    outputs_embeds.append(None)\n\n            inputs_embeds = outputs_embeds\n\n        # final norm\n        outputs_embeds = []\n        for i, hidden_states in enumerate(inputs_embeds):\n            if hidden_states is not None:\n                out_emb = models[i].norm(hidden_states)\n                outputs_embeds.append(out_emb)\n            else:\n                outputs_embeds.append(None)\n        return outputs_embeds, past_key_values\n\n    def get_attention_interface(self):\n        attention_interface = self.eager_attention_forward\n        return attention_interface\n\n    def eager_attention_forward(\n        self, attention_mask, batch_size, head_dim, query_states, key_states, value_states\n    ):\n        num_att_heads = self.num_attention_heads\n        num_key_value_heads = self.num_key_value_heads\n        num_key_value_groups = num_att_heads // num_key_value_heads\n\n        sequence_length = key_states.shape[1]\n\n        key_states = key_states[:, :, :, None, :].expand(\n            batch_size, sequence_length, num_key_value_heads, num_key_value_groups, head_dim\n        )\n        key_states = key_states.reshape(\n            batch_size, sequence_length, num_key_value_heads * num_key_value_groups, head_dim\n        )\n\n        value_states = value_states[:, :, :, None, :].expand(\n            batch_size, sequence_length, num_key_value_heads, num_key_value_groups, head_dim\n        )\n        value_states = value_states.reshape(\n            batch_size, sequence_length, num_key_value_heads * num_key_value_groups, head_dim\n        )\n\n        # Attention here is upcasted to float32 to match the original eager implementation.\n        query_states = query_states.to(dtype=torch.float32)\n        key_states = key_states.to(dtype=torch.float32)\n\n        query_states = query_states.transpose(1, 2)\n        key_states = key_states.transpose(1, 2)\n\n        att_weights = torch.matmul(query_states, key_states.transpose(2, 3))\n        att_weights *= head_dim**-0.5\n\n        att_weights = att_weights.to(dtype=torch.float32)\n        big_neg = torch.finfo(att_weights.dtype).min  # -2.3819763e38  # See gemma/modules.py\n        masked_att_weights = torch.where(attention_mask[:, None, :, :], att_weights, big_neg)\n        probs = nn.functional.softmax(masked_att_weights, dim=-1)\n        probs = probs.to(dtype=value_states.dtype)\n\n        att_output = torch.matmul(probs, value_states.permute(0, 2, 1, 3))\n\n        att_output = att_output.permute(0, 2, 1, 3)\n        # we use -1 because sequence length can change\n        att_output = att_output.reshape(batch_size, -1, num_key_value_heads * num_key_value_groups * head_dim)\n\n        return att_output\n",
      "numLines": 562,
      "startLine": 1,
      "totalLines": 562
    }
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T12:03:55.468Z_

<details><summary>↩ Tool result · `toolu_012LTQYX8CAxVm1SnfkMFkxd`</summary>

````text
1	#!/usr/bin/env python
2	
3	# Copyright 2025 HuggingFace Inc. team. All rights reserved.
4	#
5	# Licensed under the Apache License, Version 2.0 (the "License");
6	# you may not use this file except in compliance with the License.
7	# You may obtain a copy of the License at
8	#
9	#     http://www.apache.org/licenses/LICENSE-2.0
10	#
11	# Unless required by applicable law or agreed to in writing, software
12	# distributed under the License is distributed on an "AS IS" BASIS,
13	# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
14	# See the License for the specific language governing permissions and
15	# limitations under the License.
16	
17	"""
18	SmolVLA:
19	
20	[Paper](https://huggingface.co/papers/2506.01844)
21	
22	Designed by Hugging Face.
23	
24	Install smolvla extra dependencies:
25	```bash
26	pip install -e ".[smolvla]"
27	```
28	
29	Example of finetuning the smolvla pretrained model (`smolvla_base`):
30	```bash
31	lerobot-train \
32	--policy.path=lerobot/smolvla_base \
33	--dataset.repo_id=&lt;USER>/svla_so100_task1_v3 \
34	--batch_size=64 \
35	--steps=200000
36	```
37	
38	Example of finetuning a smolVLA. SmolVLA is composed of a pretrained VLM,
39	and an action expert.
40	```bash
41	lerobot-train \
42	--policy.type=smolvla \
43	--dataset.repo_id=&lt;USER>/svla_so100_task1_v3 \
44	--batch_size=64 \
45	--steps=200000
46	```
47	
48	Example of using the smolvla pretrained model outside LeRobot training framework:
49	```python
50	policy = SmolVLAPolicy.from_pretrained("lerobot/smolvla_base")
51	```
52	
53	"""
54	
55	import math
56	from collections import deque
57	from typing import TypedDict, Unpack
58	
59	import torch
60	import torch.nn.functional as F  # noqa: N812
61	from torch import Tensor, nn
62	
63	from lerobot.utils.constants import ACTION, OBS_LANGUAGE_ATTENTION_MASK, OBS_LANGUAGE_TOKENS, OBS_STATE
64	from lerobot.utils.device_utils import get_safe_dtype
65	from lerobot.utils.import_utils import require_package
66	
67	from ..pretrained import PreTrainedPolicy
68	from ..rtc.modeling_rtc import RTCProcessor
69	from ..utils import (
70	    populate_queues,
71	)
72	from .configuration_smolvla import SmolVLAConfig
73	from .smolvlm_with_expert import SmolVLMWithExpertModel
74	
75	
76	class ActionSelectKwargs(TypedDict, total=False):
77	    inference_delay: int | None
78	    prev_chunk_left_over: Tensor | None
79	    execution_horizon: int | None
80	
81	
82	def create_sinusoidal_pos_embedding(
83	    time: torch.tensor, dimension: int, min_period: float, max_period: float, device="cpu"
84	) -> Tensor:
85	    """Computes sine-cosine positional embedding vectors for scalar positions."""
86	    if dimension % 2 != 0:
87	        raise ValueError(f"dimension ({dimension}) must be divisible by 2")
88	
89	    if time.ndim != 1:
90	        raise ValueError("The time tensor is expected to be of shape `(batch_size, )`.")
91	
92	    dtype = get_safe_dtype(torch.float64, device.type)
93	    fraction = torch.linspace(0.0, 1.0, dimension // 2, dtype=dtype, device=device)
94	    period = min_period * (max_period / min_period) ** fraction
95	
96	    # Compute the outer product
97	    scaling_factor = 1.0 / period * 2 * math.pi
98	    sin_input = scaling_factor[None, :] * time[:, None]
99	    pos_emb = torch.cat([torch.sin(sin_input), torch.cos(sin_input)], dim=1)
100	    return pos_emb
101	
102	
103	def make_att_2d_masks(pad_masks, att_masks):
104	    """Copied from big_vision.
105	
106	    Tokens can attend to valid inputs tokens which have a cumulative mask_ar
107	    smaller or equal to theirs. This way `mask_ar` int[B, N] can be used to
108	    setup several types of attention, for example:
109	
110	      [[1 1 1 1 1 1]]: pure causal attention.
111	
112	      [[0 0 0 1 1 1]]: prefix-lm attention. The first 3 tokens can attend between
113	          themselves and the last 3 tokens have a causal attention. The first
114	          entry could also be a 1 without changing behaviour.
115	
116	      [[1 0 1 0 1 0 0 1 0 0]]: causal attention between 4 blocks. Tokens of a
117	          block can attend all previous blocks and all tokens on the same block.
118	
119	    Args:
120	      input_mask: bool[B, N] true if its part of the input, false if padding.
121	      mask_ar: int32[B, N] mask that's 1 where previous tokens cannot depend on
122	        it and 0 where it shares the same attention mask as the previous token.
123	    """
124	    if att_masks.ndim != 2:
125	        raise ValueError(att_masks.ndim)
126	    if pad_masks.ndim != 2:
127	        raise ValueError(pad_masks.ndim)
128	
129	    cumsum = torch.cumsum(att_masks, dim=1)
130	    att_2d_masks = cumsum[:, None, :] <= cumsum[:, :, None]
131	    pad_2d_masks = pad_masks[:, None, :] * pad_masks[:, :, None]
132	    att_2d_masks = att_2d_masks & pad_2d_masks
133	    return att_2d_masks
134	
135	
136	def resize_with_pad(img, width, height, pad_value=-1):
137	    # assume no-op when width height fits already
138	    if img.ndim != 4:
139	        raise ValueError(f"(b,c,h,w) expected, but {img.shape}")
140	
141	    cur_height, cur_width = img.shape[2:]
142	
143	    ratio = max(cur_width / width, cur_height / height)
144	    resized_height = int(cur_height / ratio)
145	    resized_width = int(cur_width / ratio)
146	    resized_img = F.interpolate(
147	        img, size=(resized_height, resized_width), mode="bilinear", align_corners=False
148	    )
149	
150	    pad_height = max(0, int(height - resized_height))
151	    pad_width = max(0, int(width - resized_width))
152	
153	    # pad on left and top of image
154	    padded_img = F.pad(resized_img, (pad_width, 0, pad_height, 0), value=pad_value)
155	    return padded_img
156	
157	
158	def pad_vector(vector, new_dim):
159	    """Can be (batch_size x sequence_length x features_dimension)
160	    or (batch_size x features_dimension)
161	    """
162	    if vector.shape[-1] == new_dim:
163	        return vector
164	    shape = list(vector.shape)
165	    current_dim = shape[-1]
166	    shape[-1] = new_dim
167	    new_vector = torch.zeros(*shape, dtype=vector.dtype, device=vector.device)
168	    new_vector[..., :current_dim] = vector
169	    return new_vector
170	
171	
172	def normalize(x, min_val, max_val):
173	    return (x - min_val) / (max_val - min_val)
174	
175	
176	def unnormalize(x, min_val, max_val):
177	    return x * (max_val - min_val) + min_val
178	
179	
180	def safe_arcsin(value):
181	    # This ensures that the input stays within
182	    # [−1,1] to avoid invalid values for arcsin
183	    return torch.arcsin(torch.clamp(value, -1.0, 1.0))
184	
185	
186	def aloha_gripper_to_angular(value):
187	    # Aloha transforms the gripper positions into a linear space. The following code
188	    # reverses this transformation to be consistent with smolvla which is pretrained in
189	    # angular space.
190	    #
191	    # These values are coming from the Aloha code:
192	    # PUPPET_GRIPPER_POSITION_OPEN, PUPPET_GRIPPER_POSITION_CLOSED
193	    value = unnormalize(value, min_val=0.01844, max_val=0.05800)
194	
195	    # This is the inverse of the angular to linear transformation inside the Interbotix code.
196	    def linear_to_radian(linear_position, arm_length, horn_radius):
197	        value = (horn_radius**2 + linear_position**2 - arm_length**2) / (2 * horn_radius * linear_position)
198	        return safe_arcsin(value)
199	
200	    # The constants are taken from the Interbotix code.
201	    value = linear_to_radian(value, arm_length=0.036, horn_radius=0.022)
202	
203	    # Normalize to [0, 1].
204	    # The values 0.4 and 1.5 were measured on an actual Trossen robot.
205	    return normalize(value, min_val=0.4, max_val=1.5)
206	
207	
208	def aloha_gripper_from_angular(value):
209	    # Convert from the gripper position used by smolvla to the gripper position that is used by Aloha.
210	    # Note that the units are still angular but the range is different.
211	
212	    # The values 0.4 and 1.5 were measured on an actual Trossen robot.
213	    value = unnormalize(value, min_val=0.4, max_val=1.5)
214	
215	    # These values are coming from the Aloha code:
216	    # PUPPET_GRIPPER_JOINT_OPEN, PUPPET_GRIPPER_JOINT_CLOSE
217	    return normalize(value, min_val=-0.6213, max_val=1.4910)
218	
219	
220	def aloha_gripper_from_angular_inv(value):
221	    # Directly inverts the gripper_from_angular function.
222	    value = unnormalize(value, min_val=-0.6213, max_val=1.4910)
223	    return normalize(value, min_val=0.4, max_val=1.5)
224	
225	
226	class SmolVLAPolicy(PreTrainedPolicy):
227	    """Wrapper class around VLAFlowMatching model to train and run inference within LeRobot."""
228	
229	    config_class = SmolVLAConfig
230	    name = "smolvla"
231	
232	    def __init__(
233	        self,
234	        config: SmolVLAConfig,
235	        **kwargs,
236	    ):
237	        """
238	        Args:
239	            config: Policy configuration class instance or None, in which case the default instantiation of
240	                    the configuration class is used.
241	        """
242	
243	        require_package("transformers", extra="smolvla")
244	        super().__init__(config)
245	        config.validate_features()
246	        self.config = config
247	        self.init_rtc_processor()
248	        self.model = VLAFlowMatching(config, rtc_processor=self.rtc_processor)
249	        self.reset()
250	
251	    def reset(self):
252	        """This should be called whenever the environment is reset."""
253	        self._queues = {
254	            ACTION: deque(maxlen=self.config.n_action_steps),
255	        }
256	
257	    def init_rtc_processor(self):
258	        """Initialize RTC processor if RTC is enabled in config."""
259	        self.rtc_processor = None
260	
261	        # Lets create processor if the config provided
262	        # If RTC is not enabled - we still can track the denoising data
263	        if self.config.rtc_config is not None:
264	            self.rtc_processor = RTCProcessor(self.config.rtc_config)
265	
266	            # In case of calling init_rtc_processor after the model is created
267	            # We need to set the rtc_processor to the model
268	            # During the normal initialization process the model is not created yet
269	            model_value = getattr(self, "model", None)
270	            if model_value is not None:
271	                model_value.rtc_processor = self.rtc_processor
272	
273	    def get_optim_params(self) -> dict:
274	        return self.parameters()
275	
276	    def _get_action_chunk(
277	        self, batch: dict[str, Tensor], noise: Tensor | None = None, **kwargs: Unpack[ActionSelectKwargs]
278	    ) -> Tensor:
279	        # TODO: Check if this for loop is needed.
280	        # Context: In fact, self.queues contains only ACTION field, and in inference, we don't have action in the batch
281	        # In the case of offline inference, we have the action in the batch
282	        # that why without the k != ACTION check, it will raise an error because we are trying to stack
283	        # on an empty container.
284	        for k in batch:
285	            if k in self._queues and k != ACTION:
286	                batch[k] = torch.stack(list(self._queues[k]), dim=1)
287	
288	        images, img_masks = self.prepare_images(batch)
289	        state = self.prepare_state(batch)
290	        lang_tokens = batch[f"{OBS_LANGUAGE_TOKENS}"]
291	        lang_masks = batch[f"{OBS_LANGUAGE_ATTENTION_MASK}"]
292	
293	        actions = self.model.sample_actions(
294	            images, img_masks, lang_tokens, lang_masks, state, noise=noise, **kwargs
295	        )
296	
297	        # Unpad actions
298	        original_action_dim = self.config.action_feature.shape[0]
299	        actions = actions[:, :, :original_action_dim]
300	
301	        if self.config.adapt_to_pi_aloha:
302	            actions = self._pi_aloha_encode_actions(actions)
303	
304	        return actions
305	
306	    def _prepare_batch(self, batch: dict[str, Tensor]) -> dict[str, Tensor]:
307	        if self.config.adapt_to_pi_aloha:
308	            batch[OBS_STATE] = self._pi_aloha_decode_state(batch[OBS_STATE])
309	
310	        return batch
311	
312	    @torch.no_grad()
313	    def predict_action_chunk(
314	        self, batch: dict[str, Tensor], noise: Tensor | None = None, **kwargs: Unpack[ActionSelectKwargs]
315	    ) -> Tensor:
316	        self.eval()
317	
318	        batch = self._prepare_batch(batch)
319	        self._queues = populate_queues(self._queues, batch, exclude_keys=[ACTION])
320	
321	        actions = self._get_action_chunk(batch, noise, **kwargs)
322	        return actions
323	
324	    @torch.no_grad()
325	    def select_action(
326	        self, batch: dict[str, Tensor], noise: Tensor | None = None, **kwargs: Unpack[ActionSelectKwargs]
327	    ) -> Tensor:
328	        """Select a single action given environment observations.
329	
330	        This method wraps `select_actions` in order to return one action at a time for execution in the
331	        environment. It works by managing the actions in a queue and only calling `select_actions` when the
332	        queue is empty.
333	        """
334	
335	        assert not self._rtc_enabled(), (
336	            "RTC is not supported for select_action, use it with predict_action_chunk"
337	        )
338	
339	        self.eval()
340	        batch = self._prepare_batch(batch)
341	        self._queues = populate_queues(self._queues, batch, exclude_keys=[ACTION])
342	
343	        if self._check_get_actions_condition():
344	            actions = self._get_action_chunk(batch, noise)
345	
346	            # `self.predict_action_chunk` returns a (batch_size, n_action_steps, action_dim) tensor, but the queue
347	            # effectively has shape (n_action_steps, batch_size, *), hence the transpose.
348	            self._queues[ACTION].extend(actions.transpose(0, 1)[: self.config.n_action_steps])
349	
350	        return self._queues[ACTION].popleft()
351	
352	    def _check_get_actions_condition(self) -> bool:
353	        return len(self._queues[ACTION]) == 0
354	
355	    def _rtc_enabled(self) -> bool:
356	        return self.config.rtc_config is not None and self.config.rtc_config.enabled
357	
358	    def forward(
359	        self, batch: dict[str, Tensor], noise=None, time=None, reduction: str = "mean"
360	    ) -> dict[str, Tensor]:
361	        """Do a full training forward pass to compute the loss.
362	
363	        Args:
364	            batch: Training batch containing observations and actions.
365	            noise: Optional noise tensor for flow matching.
366	            time: Optional time tensor for flow matching.
367	            reduction: How to reduce the loss. Options:
368	                - "mean": Return scalar mean loss (default, backward compatible)
369	                - "none": Return per-sample losses of shape (batch_size,) for RA-BC weighting
370	        """
371	        if self.config.adapt_to_pi_aloha:
372	            batch[OBS_STATE] = self._pi_aloha_decode_state(batch[OBS_STATE])
373	            batch[ACTION] = self._pi_aloha_encode_actions_inv(batch[ACTION])
374	
375	        images, img_masks = self.prepare_images(batch)
376	        state = self.prepare_state(batch)
377	        lang_tokens = batch[f"{OBS_LANGUAGE_TOKENS}"]
378	        lang_masks = batch[f"{OBS_LANGUAGE_ATTENTION_MASK}"]
379	        actions = self.prepare_action(batch)
380	        actions_is_pad = batch.get("action_is_pad")
381	        loss_dict = {}
382	        losses = self.model.forward(images, img_masks, lang_tokens, lang_masks, state, actions, noise, time)
383	        original_action_dim = self.config.action_feature.shape[0]
384	        losses = losses[:, :, :original_action_dim]
385	        loss_dict["losses_after_forward"] = losses.clone().mean().item()
386	
387	        if actions_is_pad is not None:
388	            in_episode_bound = ~actions_is_pad
389	            losses = losses * in_episode_bound.unsqueeze(-1)
390	            loss_dict["losses_after_in_ep_bound"] = losses.clone().mean().item()
391	
392	        # Remove padding
393	        losses = losses[:, :, : self.config.max_action_dim]
394	        loss_dict["losses_after_rm_padding"] = losses.clone().mean().item()
395	
396	        if reduction == "none":
397	            # Return per-sample losses (B,) by averaging over valid (time, action) entries
398	            if actions_is_pad is None:
399	                per_sample_loss = losses.mean(dim=(1, 2))
400	            else:
401	                num_valid = ((~actions_is_pad).sum(dim=1) * losses.shape[-1]).clamp_min(1)
402	                per_sample_loss = losses.sum(dim=(1, 2)) / num_valid
403	            loss_dict["loss"] = per_sample_loss.mean().item()
404	            return per_sample_loss, loss_dict
405	        else:
406	            # Default: return scalar mean loss over valid (time, action) entries
407	            if actions_is_pad is None:
408	                loss = losses.mean()
409	            else:
410	                num_valid = ((~actions_is_pad).sum() * losses.shape[-1]).clamp_min(1)
411	                loss = losses.sum() / num_valid
412	            loss_dict["loss"] = loss.item()
413	            return loss, loss_dict
414	
415	    def prepare_images(self, batch):
416	        """Apply SmolVLA preprocessing to the images, like resizing to 224x224 and padding to keep aspect ratio, and
417	        convert pixel range from [0.0, 1.0] to [-1.0, 1.0] as requested by SigLIP.
418	        """
419	        images = []
420	        img_masks = []
421	        present_img_keys = [key for key in self.config.image_features if key in batch]
422	        missing_img_keys = [key for key in self.config.image_features if key not in batch]
423	
424	        if len(present_img_keys) == 0:
425	            raise ValueError(
426	                f"All image features are missing from the batch. At least one expected. (batch: {batch.keys()}) (image_features:{self.config.image_features})"
427	            )
428	        # Preprocess image features present in the batch
429	        for key in present_img_keys:
430	            img = batch[key][:, -1, :, :, :] if batch[key].ndim == 5 else batch[key]
431	            if self.config.resize_imgs_with_padding is not None:
432	                img = resize_with_pad(img, *self.config.resize_imgs_with_padding, pad_value=0)
433	
434	            # Normalize from range [0,1] to [-1,1] as expacted by siglip
435	            img = img * 2.0 - 1.0
436	
437	            bsize = img.shape[0]
438	            device = img.device
439	            if f"{key}_padding_mask" in batch:
440	                mask = batch[f"{key}_padding_mask"].bool()
441	            else:
442	                mask = torch.ones(bsize, dtype=torch.bool, device=device)
443	            images.append(img)
444	            img_masks.append(mask)
445	
446	        # Create image features not present in the batch
447	        # as fully 0 padded images.
448	        for num_empty_cameras in range(len(missing_img_keys)):
449	            if num_empty_cameras >= self.config.empty_cameras:
450	                break
451	            img = torch.ones_like(img) * -1
452	            mask = torch.zeros_like(mask)
453	            images.append(img)
454	            img_masks.append(mask)
455	        return images, img_masks
456	
457	    def _pi_aloha_decode_state(self, state):
458	        # Flip the joints.
459	        for motor_idx in [1, 2, 8, 9]:
460	            state[:, motor_idx] *= -1
461	        # Reverse the gripper transformation that is being applied by the Aloha runtime.
462	        for motor_idx in [6, 13]:
463	            state[:, motor_idx] = aloha_gripper_to_angular(state[:, motor_idx])
464	        return state
465	
466	    def _pi_aloha_encode_actions(self, actions):
467	        # Flip the joints.
468	        for motor_idx in [1, 2, 8, 9]:
469	            actions[:, :, motor_idx] *= -1
470	        # Reverse the gripper transformation that is being applied by the Aloha runtime.
471	        for motor_idx in [6, 13]:
472	            actions[:, :, motor_idx] = aloha_gripper_from_angular(actions[:, :, motor_idx])
473	        return actions
474	
475	    def _pi_aloha_encode_actions_inv(self, actions):
476	        # Flip the joints again.
477	        for motor_idx in [1, 2, 8, 9]:
478	            actions[:, :, motor_idx] *= -1
479	        # Reverse the gripper transformation that is being applied by the Aloha runtime.
480	        for motor_idx in [6, 13]:
481	            actions[:, :, motor_idx] = aloha_gripper_from_angular_inv(actions[:, :, motor_idx])
482	        return actions
483	
484	    def prepare_state(self, batch):
485	        """Pad state"""
486	        state = batch[OBS_STATE][:, -1, :] if batch[OBS_STATE].ndim > 2 else batch[OBS_STATE]
487	        state = pad_vector(state, self.config.max_state_dim)
488	        return state
489	
490	    def prepare_action(self, batch):
491	        """Pad action"""
492	        actions = pad_vector(batch[ACTION], self.config.max_action_dim)
493	        return actions
494	
495	    def _get_default_peft_targets(self) -> dict[str, any]:
496	        """Return default PEFT target modules for SmolVLA fine-tuning."""
497	        common_projections = (
498	            "state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out"
499	        )
500	        target_modules = rf"(model\.vlm_with_expert\.lm_expert\..*\.(q|v)_proj|model\.({common_projections}))"
501	        return {
502	            "target_modules": target_modules,
503	            "modules_to_save": [],
504	        }
505	
506	    def _validate_peft_config(self, peft_config) -> None:
507	        """Validate PEFT configuration for SmolVLA."""
508	        super()._validate_peft_config(peft_config)
509	        if not self.config.load_vlm_weights:
510	            import logging
511	
512	            logging.warning(
513	                "Training SmolVLA from scratch using PEFT. This is unlikely to yield good results. "
514	                "Set `load_vlm_weights=True` to fine-tune the existing policy."
515	            )
516	
517	
518	def pad_tensor(tensor, max_len, pad_value=0):
519	    """
520	    Efficiently pads a tensor along sequence dimension to match max_len.
521	
522	    Args:
523	        tensor (torch.Tensor): Shape (B, L, ...) or (B, L).
524	        max_len (int): Fixed sequence length.
525	        pad_value (int/float): Value for padding.
526	
527	    Returns:
528	        torch.Tensor: Shape (B, max_len, ...) or (B, max_len).
529	    """
530	    b, d = tensor.shape[:2]
531	
532	    # Create a padded tensor of max_len and copy the existing values
533	    padded_tensor = torch.full(
534	        (b, max_len, *tensor.shape[2:]), pad_value, dtype=tensor.dtype, device=tensor.device
535	    )
536	    padded_tensor[:, :d] = tensor  # Efficient in-place copy
537	
538	    return padded_tensor
539	
540	
541	class VLAFlowMatching(nn.Module):
542	    """
543	    SmolVLA
544	
545	    [Paper]()
546	
547	    Designed by Hugging Face.
548	    ┌──────────────────────────────┐
549	    │                 actions      │
550	    │                    ▲         │
551	    │ ┌─────────┐      ┌─|────┐    │
552	    │ |         │────► │      │    │
553	    │ |         │ kv   │      │    │
554	    │ |         │────► │Action│    │
555	    │ |   VLM   │cache │Expert│    |
556	    │ │         │────► |      │    │
557	    │ │         │      │      │    │
558	    │ └▲──▲───▲─┘      └───▲──┘    |
559	    │  │  |   |            │       |
560	    │  |  |   |          noise     │
561	    │  │  │ state                  │
562	    │  │ language tokens           │
563	    │  image(s)                    │
564	    └──────────────────────────────┘
565	    """
566	
567	    def __init__(self, config: SmolVLAConfig, rtc_processor: RTCProcessor | None = None):
568	        super().__init__()
569	        self.config = config
570	
571	        self.vlm_with_expert = SmolVLMWithExpertModel(
572	            model_id=self.config.vlm_model_name,
573	            freeze_vision_encoder=self.config.freeze_vision_encoder,
574	            train_expert_only=self.config.train_expert_only,
575	            load_vlm_weights=self.config.load_vlm_weights,
576	            attention_mode=self.config.attention_mode,
577	            num_expert_layers=self.config.num_expert_layers,
578	            num_vlm_layers=self.config.num_vlm_layers,
579	            self_attn_every_n_layers=self.config.self_attn_every_n_layers,
580	            expert_width_multiplier=self.config.expert_width_multiplier,
581	            device=self.config.device if self.config.device is not None else "auto",
582	        )
583	        self.state_proj = nn.Linear(
584	            self.config.max_state_dim, self.vlm_with_expert.config.text_config.hidden_size
585	        )
586	        self.action_in_proj = nn.Linear(self.config.max_action_dim, self.vlm_with_expert.expert_hidden_size)
587	        self.action_out_proj = nn.Linear(self.vlm_with_expert.expert_hidden_size, self.config.max_action_dim)
588	
589	        self.action_time_mlp_in = nn.Linear(
590	            self.vlm_with_expert.expert_hidden_size * 2, self.vlm_with_expert.expert_hidden_size
591	        )
592	        self.action_time_mlp_out = nn.Linear(
593	            self.vlm_with_expert.expert_hidden_size, self.vlm_with_expert.expert_hidden_size
594	        )
595	
596	        self.set_requires_grad()
597	        self.fake_image_token = self.vlm_with_expert.processor.tokenizer.fake_image_token_id
598	        self.global_image_token = self.vlm_with_expert.processor.tokenizer.global_image_token_id
599	        self.global_image_start_token = torch.tensor(
600	            [self.fake_image_token, self.global_image_token], dtype=torch.long
601	        )
602	
603	        self.add_image_special_tokens = self.config.add_image_special_tokens
604	        self.image_end_token = torch.tensor([self.fake_image_token], dtype=torch.long)
605	        self.prefix_length = self.config.prefix_length
606	        self.rtc_processor = rtc_processor
607	
608	        # Compile model if requested
609	        if config.compile_model:
610	            torch.set_float32_matmul_precision("high")
611	            self.sample_actions = torch.compile(self.sample_actions, mode=config.compile_mode)
612	            self.forward = torch.compile(self.forward, mode=config.compile_mode)
613	
614	    def _rtc_enabled(self):
615	        return self.config.rtc_config is not None and self.config.rtc_config.enabled
616	
617	    def set_requires_grad(self):
618	        for params in self.state_proj.parameters():
619	            params.requires_grad = self.config.train_state_proj
620	
621	    def sample_noise(self, shape, device):
622	        noise = torch.normal(
623	            mean=0.0,
624	            std=1.0,
625	            size=shape,
626	            dtype=torch.float32,
627	            device=device,
628	        )
629	        return noise
630	
631	    def sample_time(self, bsize, device):
632	        beta_dist = torch.distributions.Beta(concentration1=1.5, concentration0=1.0)
633	        time_beta = beta_dist.sample((bsize,)).to(device=device, dtype=torch.float32)
634	        time = time_beta * 0.999 + 0.001
635	        return time
636	
637	    def embed_prefix(
638	        self, images, img_masks, lang_tokens, lang_masks, state: torch.Tensor = None
639	    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
640	        """Embed images with SigLIP and language tokens with embedding layer to prepare
641	        for SmolVLM transformer processing.
642	        """
643	        embs = []
644	        pad_masks = []
645	        att_masks = []
646	        for _img_idx, (
647	            img,
648	            img_mask,
649	        ) in enumerate(zip(images, img_masks, strict=False)):
650	            if self.add_image_special_tokens:
651	                image_start_token = (
652	                    self.vlm_with_expert.embed_language_tokens(
653	                        self.global_image_start_token.to(device=self.vlm_with_expert.vlm.device)
654	                    )
655	                    .unsqueeze(0)
656	                    .expand(img.shape[0], -1, -1)
657	                )
658	                image_start_mask = torch.ones_like(
659	                    image_start_token[:, :, 0], dtype=torch.bool, device=image_start_token.device
660	                )
661	                att_masks += [0] * (image_start_mask.shape[-1])
662	                embs.append(image_start_token)
663	                pad_masks.append(image_start_mask)
664	
665	            img_emb = self.vlm_with_expert.embed_image(img)
666	            img_emb = img_emb
667	
668	            # Normalize image embeddings
669	            img_emb_dim = img_emb.shape[-1]
670	            img_emb = img_emb * torch.tensor(img_emb_dim**0.5, dtype=img_emb.dtype, device=img_emb.device)
671	
672	            bsize, num_img_embs = img_emb.shape[:2]
673	            img_mask = img_mask[:, None].expand(bsize, num_img_embs)
674	
675	            embs.append(img_emb)
676	            pad_masks.append(img_mask)
677	
678	            att_masks += [0] * (num_img_embs)
679	            if self.add_image_special_tokens:
680	                image_end_token = (
681	                    self.vlm_with_expert.embed_language_tokens(
682	                        self.image_end_token.to(device=self.vlm_with_expert.vlm.device)
683	                    )
684	                    .unsqueeze(0)
685	                    .expand(img.shape[0], -1, -1)
686	                )
687	                image_end_mask = torch.ones_like(
688	                    image_end_token[:, :, 0], dtype=torch.bool, device=image_end_token.device
689	                )
690	                embs.append(image_end_token)
691	                pad_masks.append(image_end_mask)
692	                att_masks += [0] * (image_end_mask.shape[1])
693	        lang_emb = self.vlm_with_expert.embed_language_tokens(lang_tokens)
694	        # Normalize language embeddings
695	        lang_emb_dim = lang_emb.shape[-1]
696	        lang_emb = lang_emb * math.sqrt(lang_emb_dim)
697	
698	        embs.append(lang_emb)
699	        pad_masks.append(lang_masks)
700	
701	        num_lang_embs = lang_emb.shape[1]
702	        att_masks += [0] * num_lang_embs
703	
704	        state_emb = self.state_proj(state)
705	        state_emb = state_emb[:, None, :] if state_emb.ndim == 2 else state_emb
706	        embs.append(state_emb)
707	        bsize = state_emb.shape[0]
708	        device = state_emb.device
709	
710	        states_seq_len = state_emb.shape[1]
711	        state_mask = torch.ones(bsize, states_seq_len, dtype=torch.bool, device=device)
712	        pad_masks.append(state_mask)
713	
714	        # Set attention masks so that image and language inputs do not attend to state or actions
715	        att_masks += [1] * (states_seq_len)
716	        embs = torch.cat(embs, dim=1)
717	        pad_masks = torch.cat(pad_masks, dim=1)
718	        att_masks = torch.tensor(att_masks, dtype=torch.bool, device=pad_masks.device)
719	        att_masks = att_masks[None, :]
720	
721	        seq_len = pad_masks.shape[1]
722	        if seq_len < self.prefix_length:
723	            embs = pad_tensor(embs, self.prefix_length, pad_value=0)
724	            pad_masks = pad_tensor(pad_masks, self.prefix_length, pad_value=0)
725	            att_masks = pad_tensor(att_masks, self.prefix_length, pad_value=0)
726	
727	        att_masks = att_masks.expand(bsize, -1)
728	
729	        return embs, pad_masks, att_masks
730	
731	    def embed_suffix(self, noisy_actions, timestep):
732	        """Embed state, noisy_actions, timestep to prepare for Expert Gemma processing."""
733	        embs = []
734	        pad_masks = []
735	        att_masks = []
736	
737	        # Fuse timestep + action information using an MLP
738	        action_emb = self.action_in_proj(noisy_actions)
739	        device = action_emb.device
740	        bsize = action_emb.shape[0]
741	        dtype = action_emb.dtype
742	        # Embed timestep using sine-cosine positional encoding with sensitivity in the range [0, 1]
743	        time_emb = create_sinusoidal_pos_embedding(
744	            timestep,
745	            self.vlm_with_expert.expert_hidden_size,
746	            self.config.min_period,
747	            self.config.max_period,
748	            device=device,
749	        )
750	        time_emb = time_emb.type(dtype=dtype)
751	
752	        time_emb = time_emb[:, None, :].expand_as(action_emb)
753	        action_time_emb = torch.cat([action_emb, time_emb], dim=2)
754	
755	        action_time_emb = self.action_time_mlp_in(action_time_emb)
756	        action_time_emb = F.silu(action_time_emb)  # swish == silu
757	        action_time_emb = self.action_time_mlp_out(action_time_emb)
758	
759	        # Add to input tokens
760	        embs.append(action_time_emb)
761	
762	        bsize, action_time_dim = action_time_emb.shape[:2]
763	        action_time_mask = torch.ones(bsize, action_time_dim, dtype=torch.bool, device=device)
764	        pad_masks.append(action_time_mask)
765	
766	        # Set attention masks so that image, language and state inputs do not attend to action tokens
767	        att_masks += [1] * self.config.chunk_size
768	        embs = torch.cat(embs, dim=1)
769	        pad_masks = torch.cat(pad_masks, dim=1)
770	        att_masks = torch.tensor(att_masks, dtype=embs.dtype, device=embs.device)
771	        att_masks = att_masks[None, :].expand(bsize, len(att_masks))
772	        return embs, pad_masks, att_masks
773	
774	    def forward(
775	        self, images, img_masks, lang_tokens, lang_masks, state, actions, noise=None, time=None
776	    ) -> Tensor:
777	        """Do a full training forward pass and compute the loss (batch_size x num_steps x num_motors)"""
778	        if noise is None:
779	            noise = self.sample_noise(actions.shape, actions.device)
780	
781	        if time is None:
782	            time = self.sample_time(actions.shape[0], actions.device)
783	
784	        time_expanded = time[:, None, None]
785	        x_t = time_expanded * noise + (1 - time_expanded) * actions
786	        u_t = noise - actions
787	        prefix_embs, prefix_pad_masks, prefix_att_masks = self.embed_prefix(
788	            images, img_masks, lang_tokens, lang_masks, state=state
789	        )
790	        suffix_embs, suffix_pad_masks, suffix_att_masks = self.embed_suffix(x_t, time)
791	
792	        pad_masks = torch.cat([prefix_pad_masks, suffix_pad_masks], dim=1)
793	        att_masks = torch.cat([prefix_att_masks, suffix_att_masks], dim=1)
794	
795	        att_2d_masks = make_att_2d_masks(pad_masks, att_masks)
796	        position_ids = torch.cumsum(pad_masks, dim=1) - 1
797	        (_, suffix_out), _ = self.vlm_with_expert.forward(
798	            attention_mask=att_2d_masks,
799	            position_ids=position_ids,
800	            past_key_values=None,
801	            inputs_embeds=[prefix_embs, suffix_embs],
802	            use_cache=False,
803	            fill_kv_cache=False,
804	        )
805	        suffix_out = suffix_out[:, -self.config.chunk_size :]
806	        # Original openpi code, upcast attention output
807	        suffix_out = suffix_out.to(dtype=torch.float32)
808	        v_t = self.action_out_proj(suffix_out)
809	        losses = F.mse_loss(u_t, v_t, reduction="none")
810	        return losses
811	
812	    def sample_actions(
813	        self,
814	        images,
815	        img_masks,
816	        lang_tokens,
817	        lang_masks,
818	        state,
819	        noise=None,
820	        **kwargs: Unpack[ActionSelectKwargs],
821	    ) -> Tensor:
822	        """Do a full inference forward and compute the action (batch_size x num_steps x num_motors)"""
823	        bsize = state.shape[0]
824	        device = state.device
825	
826	        if noise is None:
827	            actions_shape = (bsize, self.config.chunk_size, self.config.max_action_dim)
828	            noise = self.sample_noise(actions_shape, device)
829	
830	        prefix_embs, prefix_pad_masks, prefix_att_masks = self.embed_prefix(
831	            images, img_masks, lang_tokens, lang_masks, state=state
832	        )
833	        prefix_att_2d_masks = make_att_2d_masks(prefix_pad_masks, prefix_att_masks)
834	        prefix_position_ids = torch.cumsum(prefix_pad_masks, dim=1) - 1
835	        # Compute image and language key value cache
836	        _, past_key_values = self.vlm_with_expert.forward(
837	            attention_mask=prefix_att_2d_masks,
838	            position_ids=prefix_position_ids,
839	            past_key_values=None,
840	            inputs_embeds=[prefix_embs, None],
841	            use_cache=self.config.use_cache,
842	            fill_kv_cache=True,
843	        )
844	        num_steps = self.config.num_steps
845	        dt = -1.0 / num_steps
846	
847	        x_t = noise
848	        for step in range(num_steps):
849	            time = 1.0 + step * dt
850	            time_tensor = torch.tensor(time, dtype=torch.float32, device=device).expand(bsize)
851	
852	            def denoise_step_partial_call(input_x_t, current_timestep=time_tensor):
853	                return self.denoise_step(
854	                    x_t=input_x_t,
855	                    prefix_pad_masks=prefix_pad_masks,
856	                    past_key_values=past_key_values,
857	                    timestep=current_timestep,
858	                )
859	
860	            if self._rtc_enabled():
861	                inference_delay = kwargs.get("inference_delay")
862	                prev_chunk_left_over = kwargs.get("prev_chunk_left_over")
863	                execution_horizon = kwargs.get("execution_horizon")
864	
865	                v_t = self.rtc_processor.denoise_step(
866	                    x_t=x_t,
867	                    prev_chunk_left_over=prev_chunk_left_over,
868	                    inference_delay=inference_delay,
869	                    time=time,
870	                    original_denoise_step_partial=denoise_step_partial_call,
871	                    execution_horizon=execution_horizon,
872	                )
873	            else:
874	                v_t = denoise_step_partial_call(x_t)
875	
876	            x_t = x_t + dt * v_t
877	
878	            if self.rtc_processor is not None and self.rtc_processor.is_debug_enabled():
879	                self.rtc_processor.track(time=time, x_t=x_t, v_t=v_t)
880	
881	        return x_t
882	
883	    def denoise_step(
884	        self,
885	        prefix_pad_masks,
886	        past_key_values,
887	        x_t,
888	        timestep,
889	    ):
890	        """Apply one denoising step of the noise `x_t` at a given timestep."""
891	        suffix_embs, suffix_pad_masks, suffix_att_masks = self.embed_suffix(x_t, timestep)
892	
893	        suffix_len = suffix_pad_masks.shape[1]
894	        batch_size = prefix_pad_masks.shape[0]
895	        prefix_len = prefix_pad_masks.shape[1]
896	        prefix_pad_2d_masks = prefix_pad_masks[:, None, :].expand(batch_size, suffix_len, prefix_len)
897	
898	        suffix_att_2d_masks = make_att_2d_masks(suffix_pad_masks, suffix_att_masks)
899	
900	        full_att_2d_masks = torch.cat([prefix_pad_2d_masks, suffix_att_2d_masks], dim=2)
901	        prefix_offsets = torch.sum(prefix_pad_masks, dim=-1)[:, None]
902	        position_ids = prefix_offsets + torch.cumsum(suffix_pad_masks, dim=1) - 1
903	
904	        outputs_embeds, _ = self.vlm_with_expert.forward(
905	            attention_mask=full_att_2d_masks,
906	            position_ids=position_ids,
907	            past_key_values=past_key_values,
908	            inputs_embeds=[None, suffix_embs],
909	            use_cache=self.config.use_cache,
910	            fill_kv_cache=False,
911	        )
912	        suffix_out = outputs_embeds[1]
913	        suffix_out = suffix_out[:, -self.config.chunk_size :]
914	        suffix_out = suffix_out.to(dtype=torch.float32)
915	        v_t = self.action_out_proj(suffix_out)
916	        return v_t
917	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4500fe-6a1a-47d9-9d46-34a341e3644c",
  "uuid": "c1527bf0-1473-4989-9561-9ace3a496abb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/lerobot/src/lerobot/policies/smolvla/modeling_smolvla.py",
      "content": "#!/usr/bin/env python\n\n# Copyright 2025 HuggingFace Inc. team. All rights reserved.\n#\n# Licensed under the Apache License, Version 2.0 (the \"License\");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#     http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an \"AS IS\" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n\n\"\"\"\nSmolVLA:\n\n[Paper](https://huggingface.co/papers/2506.01844)\n\nDesigned by Hugging Face.\n\nInstall smolvla extra dependencies:\n```bash\npip install -e \".[smolvla]\"\n```\n\nExample of finetuning the smolvla pretrained model (`smolvla_base`):\n```bash\nlerobot-train \\\n--policy.path=lerobot/smolvla_base \\\n--dataset.repo_id=&lt;USER>/svla_so100_task1_v3 \\\n--batch_size=64 \\\n--steps=200000\n```\n\nExample of finetuning a smolVLA. SmolVLA is composed of a pretrained VLM,\nand an action expert.\n```bash\nlerobot-train \\\n--policy.type=smolvla \\\n--dataset.repo_id=&lt;USER>/svla_so100_task1_v3 \\\n--batch_size=64 \\\n--steps=200000\n```\n\nExample of using the smolvla pretrained model outside LeRobot training framework:\n```python\npolicy = SmolVLAPolicy.from_pretrained(\"lerobot/smolvla_base\")\n```\n\n\"\"\"\n\nimport math\nfrom collections import deque\nfrom typing import TypedDict, Unpack\n\nimport torch\nimport torch.nn.functional as F  # noqa: N812\nfrom torch import Tensor, nn\n\nfrom lerobot.utils.constants import ACTION, OBS_LANGUAGE_ATTENTION_MASK, OBS_LANGUAGE_TOKENS, OBS_STATE\nfrom lerobot.utils.device_utils import get_safe_dtype\nfrom lerobot.utils.import_utils import require_package\n\nfrom ..pretrained import PreTrainedPolicy\nfrom ..rtc.modeling_rtc import RTCProcessor\nfrom ..utils import (\n    populate_queues,\n)\nfrom .configuration_smolvla import SmolVLAConfig\nfrom .smolvlm_with_expert import SmolVLMWithExpertModel\n\n\nclass ActionSelectKwargs(TypedDict, total=False):\n    inference_delay: int | None\n    prev_chunk_left_over: Tensor | None\n    execution_horizon: int | None\n\n\ndef create_sinusoidal_pos_embedding(\n    time: torch.tensor, dimension: int, min_period: float, max_period: float, device=\"cpu\"\n) -> Tensor:\n    \"\"\"Computes sine-cosine positional embedding vectors for scalar positions.\"\"\"\n    if dimension % 2 != 0:\n        raise ValueError(f\"dimension ({dimension}) must be divisible by 2\")\n\n    if time.ndim != 1:\n        raise ValueError(\"The time tensor is expected to be of shape `(batch_size, )`.\")\n\n    dtype = get_safe_dtype(torch.float64, device.type)\n    fraction = torch.linspace(0.0, 1.0, dimension // 2, dtype=dtype, device=device)\n    period = min_period * (max_period / min_period) ** fraction\n\n    # Compute the outer product\n    scaling_factor = 1.0 / period * 2 * math.pi\n    sin_input = scaling_factor[None, :] * time[:, None]\n    pos_emb = torch.cat([torch.sin(sin_input), torch.cos(sin_input)], dim=1)\n    return pos_emb\n\n\ndef make_att_2d_masks(pad_masks, att_masks):\n    \"\"\"Copied from big_vision.\n\n    Tokens can attend to valid inputs tokens which have a cumulative mask_ar\n    smaller or equal to theirs. This way `mask_ar` int[B, N] can be used to\n    setup several types of attention, for example:\n\n      [[1 1 1 1 1 1]]: pure causal attention.\n\n      [[0 0 0 1 1 1]]: prefix-lm attention. The first 3 tokens can attend between\n          themselves and the last 3 tokens have a causal attention. The first\n          entry could also be a 1 without changing behaviour.\n\n      [[1 0 1 0 1 0 0 1 0 0]]: causal attention between 4 blocks. Tokens of a\n          block can attend all previous blocks and all tokens on the same block.\n\n    Args:\n      input_mask: bool[B, N] true if its part of the input, false if padding.\n      mask_ar: int32[B, N] mask that's 1 where previous tokens cannot depend on\n        it and 0 where it shares the same attention mask as the previous token.\n    \"\"\"\n    if att_masks.ndim != 2:\n        raise ValueError(att_masks.ndim)\n    if pad_masks.ndim != 2:\n        raise ValueError(pad_masks.ndim)\n\n    cumsum = torch.cumsum(att_masks, dim=1)\n    att_2d_masks = cumsum[:, None, :] <= cumsum[:, :, None]\n    pad_2d_masks = pad_masks[:, None, :] * pad_masks[:, :, None]\n    att_2d_masks = att_2d_masks & pad_2d_masks\n    return att_2d_masks\n\n\ndef resize_with_pad(img, width, height, pad_value=-1):\n    # assume no-op when width height fits already\n    if img.ndim != 4:\n        raise ValueError(f\"(b,c,h,w) expected, but {img.shape}\")\n\n    cur_height, cur_width = img.shape[2:]\n\n    ratio = max(cur_width / width, cur_height / height)\n    resized_height = int(cur_height / ratio)\n    resized_width = int(cur_width / ratio)\n    resized_img = F.interpolate(\n        img, size=(resized_height, resized_width), mode=\"bilinear\", align_corners=False\n    )\n\n    pad_height = max(0, int(height - resized_height))\n    pad_width = max(0, int(width - resized_width))\n\n    # pad on left and top of image\n    padded_img = F.pad(resized_img, (pad_width, 0, pad_height, 0), value=pad_value)\n    return padded_img\n\n\ndef pad_vector(vector, new_dim):\n    \"\"\"Can be (batch_size x sequence_length x features_dimension)\n    or (batch_size x features_dimension)\n    \"\"\"\n    if vector.shape[-1] == new_dim:\n        return vector\n    shape = list(vector.shape)\n    current_dim = shape[-1]\n    shape[-1] = new_dim\n    new_vector = torch.zeros(*shape, dtype=vector.dtype, device=vector.device)\n    new_vector[..., :current_dim] = vector\n    return new_vector\n\n\ndef normalize(x, min_val, max_val):\n    return (x - min_val) / (max_val - min_val)\n\n\ndef unnormalize(x, min_val, max_val):\n    return x * (max_val - min_val) + min_val\n\n\ndef safe_arcsin(value):\n    # This ensures that the input stays within\n    # [−1,1] to avoid invalid values for arcsin\n    return torch.arcsin(torch.clamp(value, -1.0, 1.0))\n\n\ndef aloha_gripper_to_angular(value):\n    # Aloha transforms the gripper positions into a linear space. The following code\n    # reverses this transformation to be consistent with smolvla which is pretrained in\n    # angular space.\n    #\n    # These values are coming from the Aloha code:\n    # PUPPET_GRIPPER_POSITION_OPEN, PUPPET_GRIPPER_POSITION_CLOSED\n    value = unnormalize(value, min_val=0.01844, max_val=0.05800)\n\n    # This is the inverse of the angular to linear transformation inside the Interbotix code.\n    def linear_to_radian(linear_position, arm_length, horn_radius):\n        value = (horn_radius**2 + linear_position**2 - arm_length**2) / (2 * horn_radius * linear_position)\n        return safe_arcsin(value)\n\n    # The constants are taken from the Interbotix code.\n    value = linear_to_radian(value, arm_length=0.036, horn_radius=0.022)\n\n    # Normalize to [0, 1].\n    # The values 0.4 and 1.5 were measured on an actual Trossen robot.\n    return normalize(value, min_val=0.4, max_val=1.5)\n\n\ndef aloha_gripper_from_angular(value):\n    # Convert from the gripper position used by smolvla to the gripper position that is used by Aloha.\n    # Note that the units are still angular but the range is different.\n\n    # The values 0.4 and 1.5 were measured on an actual Trossen robot.\n    value = unnormalize(value, min_val=0.4, max_val=1.5)\n\n    # These values are coming from the Aloha code:\n    # PUPPET_GRIPPER_JOINT_OPEN, PUPPET_GRIPPER_JOINT_CLOSE\n    return normalize(value, min_val=-0.6213, max_val=1.4910)\n\n\ndef aloha_gripper_from_angular_inv(value):\n    # Directly inverts the gripper_from_angular function.\n    value = unnormalize(value, min_val=-0.6213, max_val=1.4910)\n    return normalize(value, min_val=0.4, max_val=1.5)\n\n\nclass SmolVLAPolicy(PreTrainedPolicy):\n    \"\"\"Wrapper class around VLAFlowMatching model to train and run inference within LeRobot.\"\"\"\n\n    config_class = SmolVLAConfig\n    name = \"smolvla\"\n\n    def __init__(\n        self,\n        config: SmolVLAConfig,\n        **kwargs,\n    ):\n        \"\"\"\n        Args:\n            config: Policy configuration class instance or None, in which case the default instantiation of\n                    the configuration class is used.\n        \"\"\"\n\n        require_package(\"transformers\", extra=\"smolvla\")\n        super().__init__(config)\n        config.validate_features()\n        self.config = config\n        self.init_rtc_processor()\n        self.model = VLAFlowMatching(config, rtc_processor=self.rtc_processor)\n        self.reset()\n\n    def reset(self):\n        \"\"\"This should be called whenever the environment is reset.\"\"\"\n        self._queues = {\n            ACTION: deque(maxlen=self.config.n_action_steps),\n        }\n\n    def init_rtc_processor(self):\n        \"\"\"Initialize RTC processor if RTC is enabled in config.\"\"\"\n        self.rtc_processor = None\n\n        # Lets create processor if the config provided\n        # If RTC is not enabled - we still can track the denoising data\n        if self.config.rtc_config is not None:\n            self.rtc_processor = RTCProcessor(self.config.rtc_config)\n\n            # In case of calling init_rtc_processor after the model is created\n            # We need to set the rtc_processor to the model\n            # During the normal initialization process the model is not created yet\n            model_value = getattr(self, \"model\", None)\n            if model_value is not None:\n                model_value.rtc_processor = self.rtc_processor\n\n    def get_optim_params(self) -> dict:\n        return self.parameters()\n\n    def _get_action_chunk(\n        self, batch: dict[str, Tensor], noise: Tensor | None = None, **kwargs: Unpack[ActionSelectKwargs]\n    ) -> Tensor:\n        # TODO: Check if this for loop is needed.\n        # Context: In fact, self.queues contains only ACTION field, and in inference, we don't have action in the batch\n        # In the case of offline inference, we have the action in the batch\n        # that why without the k != ACTION check, it will raise an error because we are trying to stack\n        # on an empty container.\n        for k in batch:\n            if k in self._queues and k != ACTION:\n                batch[k] = torch.stack(list(self._queues[k]), dim=1)\n\n        images, img_masks = self.prepare_images(batch)\n        state = self.prepare_state(batch)\n        lang_tokens = batch[f\"{OBS_LANGUAGE_TOKENS}\"]\n        lang_masks = batch[f\"{OBS_LANGUAGE_ATTENTION_MASK}\"]\n\n        actions = self.model.sample_actions(\n            images, img_masks, lang_tokens, lang_masks, state, noise=noise, **kwargs\n        )\n\n        # Unpad actions\n        original_action_dim = self.config.action_feature.shape[0]\n        actions = actions[:, :, :original_action_dim]\n\n        if self.config.adapt_to_pi_aloha:\n            actions = self._pi_aloha_encode_actions(actions)\n\n        return actions\n\n    def _prepare_batch(self, batch: dict[str, Tensor]) -> dict[str, Tensor]:\n        if self.config.adapt_to_pi_aloha:\n            batch[OBS_STATE] = self._pi_aloha_decode_state(batch[OBS_STATE])\n\n        return batch\n\n    @torch.no_grad()\n    def predict_action_chunk(\n        self, batch: dict[str, Tensor], noise: Tensor | None = None, **kwargs: Unpack[ActionSelectKwargs]\n    ) -> Tensor:\n        self.eval()\n\n        batch = self._prepare_batch(batch)\n        self._queues = populate_queues(self._queues, batch, exclude_keys=[ACTION])\n\n        actions = self._get_action_chunk(batch, noise, **kwargs)\n        return actions\n\n    @torch.no_grad()\n    def select_action(\n        self, batch: dict[str, Tensor], noise: Tensor | None = None, **kwargs: Unpack[ActionSelectKwargs]\n    ) -> Tensor:\n        \"\"\"Select a single action given environment observations.\n\n        This method wraps `select_actions` in order to return one action at a time for execution in the\n        environment. It works by managing the actions in a queue and only calling `select_actions` when the\n        queue is empty.\n        \"\"\"\n\n        assert not self._rtc_enabled(), (\n            \"RTC is not supported for select_action, use it with predict_action_chunk\"\n        )\n\n        self.eval()\n        batch = self._prepare_batch(batch)\n        self._queues = populate_queues(self._queues, batch, exclude_keys=[ACTION])\n\n        if self._check_get_actions_condition():\n            actions = self._get_action_chunk(batch, noise)\n\n            # `self.predict_action_chunk` returns a (batch_size, n_action_steps, action_dim) tensor, but the queue\n            # effectively has shape (n_action_steps, batch_size, *), hence the transpose.\n            self._queues[ACTION].extend(actions.transpose(0, 1)[: self.config.n_action_steps])\n\n        return self._queues[ACTION].popleft()\n\n    def _check_get_actions_condition(self) -> bool:\n        return len(self._queues[ACTION]) == 0\n\n    def _rtc_enabled(self) -> bool:\n        return self.config.rtc_config is not None and self.config.rtc_config.enabled\n\n    def forward(\n        self, batch: dict[str, Tensor], noise=None, time=None, reduction: str = \"mean\"\n    ) -> dict[str, Tensor]:\n        \"\"\"Do a full training forward pass to compute the loss.\n\n        Args:\n            batch: Training batch containing observations and actions.\n            noise: Optional noise tensor for flow matching.\n            time: Optional time tensor for flow matching.\n            reduction: How to reduce the loss. Options:\n                - \"mean\": Return scalar mean loss (default, backward compatible)\n                - \"none\": Return per-sample losses of shape (batch_size,) for RA-BC weighting\n        \"\"\"\n        if self.config.adapt_to_pi_aloha:\n            batch[OBS_STATE] = self._pi_aloha_decode_state(batch[OBS_STATE])\n            batch[ACTION] = self._pi_aloha_encode_actions_inv(batch[ACTION])\n\n        images, img_masks = self.prepare_images(batch)\n        state = self.prepare_state(batch)\n        lang_tokens = batch[f\"{OBS_LANGUAGE_TOKENS}\"]\n        lang_masks = batch[f\"{OBS_LANGUAGE_ATTENTION_MASK}\"]\n        actions = self.prepare_action(batch)\n        actions_is_pad = batch.get(\"action_is_pad\")\n        loss_dict = {}\n        losses = self.model.forward(images, img_masks, lang_tokens, lang_masks, state, actions, noise, time)\n        original_action_dim = self.config.action_feature.shape[0]\n        losses = losses[:, :, :original_action_dim]\n        loss_dict[\"losses_after_forward\"] = losses.clone().mean().item()\n\n        if actions_is_pad is not None:\n            in_episode_bound = ~actions_is_pad\n            losses = losses * in_episode_bound.unsqueeze(-1)\n            loss_dict[\"losses_after_in_ep_bound\"] = losses.clone().mean().item()\n\n        # Remove padding\n        losses = losses[:, :, : self.config.max_action_dim]\n        loss_dict[\"losses_after_rm_padding\"] = losses.clone().mean().item()\n\n        if reduction == \"none\":\n            # Return per-sample losses (B,) by averaging over valid (time, action) entries\n            if actions_is_pad is None:\n                per_sample_loss = losses.mean(dim=(1, 2))\n            else:\n                num_valid = ((~actions_is_pad).sum(dim=1) * losses.shape[-1]).clamp_min(1)\n                per_sample_loss = losses.sum(dim=(1, 2)) / num_valid\n            loss_dict[\"loss\"] = per_sample_loss.mean().item()\n            return per_sample_loss, loss_dict\n        else:\n            # Default: return scalar mean loss over valid (time, action) entries\n            if actions_is_pad is None:\n                loss = losses.mean()\n            else:\n                num_valid = ((~actions_is_pad).sum() * losses.shape[-1]).clamp_min(1)\n                loss = losses.sum() / num_valid\n            loss_dict[\"loss\"] = loss.item()\n            return loss, loss_dict\n\n    def prepare_images(self, batch):\n        \"\"\"Apply SmolVLA preprocessing to the images, like resizing to 224x224 and padding to keep aspect ratio, and\n        convert pixel range from [0.0, 1.0] to [-1.0, 1.0] as requested by SigLIP.\n        \"\"\"\n        images = []\n        img_masks = []\n        present_img_keys = [key for key in self.config.image_features if key in batch]\n        missing_img_keys = [key for key in self.config.image_features if key not in batch]\n\n        if len(present_img_keys) == 0:\n            raise ValueError(\n                f\"All image features are missing from the batch. At least one expected. (batch: {batch.keys()}) (image_features:{self.config.image_features})\"\n            )\n        # Preprocess image features present in the batch\n        for key in present_img_keys:\n            img = batch[key][:, -1, :, :, :] if batch[key].ndim == 5 else batch[key]\n            if self.config.resize_imgs_with_padding is not None:\n                img = resize_with_pad(img, *self.config.resize_imgs_with_padding, pad_value=0)\n\n            # Normalize from range [0,1] to [-1,1] as expacted by siglip\n            img = img * 2.0 - 1.0\n\n            bsize = img.shape[0]\n            device = img.device\n            if f\"{key}_padding_mask\" in batch:\n                mask = batch[f\"{key}_padding_mask\"].bool()\n            else:\n                mask = torch.ones(bsize, dtype=torch.bool, device=device)\n            images.append(img)\n            img_masks.append(mask)\n\n        # Create image features not present in the batch\n        # as fully 0 padded images.\n        for num_empty_cameras in range(len(missing_img_keys)):\n            if num_empty_cameras >= self.config.empty_cameras:\n                break\n            img = torch.ones_like(img) * -1\n            mask = torch.zeros_like(mask)\n            images.append(img)\n            img_masks.append(mask)\n        return images, img_masks\n\n    def _pi_aloha_decode_state(self, state):\n        # Flip the joints.\n        for motor_idx in [1, 2, 8, 9]:\n            state[:, motor_idx] *= -1\n        # Reverse the gripper transformation that is being applied by the Aloha runtime.\n        for motor_idx in [6, 13]:\n            state[:, motor_idx] = aloha_gripper_to_angular(state[:, motor_idx])\n        return state\n\n    def _pi_aloha_encode_actions(self, actions):\n        # Flip the joints.\n        for motor_idx in [1, 2, 8, 9]:\n            actions[:, :, motor_idx] *= -1\n        # Reverse the gripper transformation that is being applied by the Aloha runtime.\n        for motor_idx in [6, 13]:\n            actions[:, :, motor_idx] = aloha_gripper_from_angular(actions[:, :, motor_idx])\n        return actions\n\n    def _pi_aloha_encode_actions_inv(self, actions):\n        # Flip the joints again.\n        for motor_idx in [1, 2, 8, 9]:\n            actions[:, :, motor_idx] *= -1\n        # Reverse the gripper transformation that is being applied by the Aloha runtime.\n        for motor_idx in [6, 13]:\n            actions[:, :, motor_idx] = aloha_gripper_from_angular_inv(actions[:, :, motor_idx])\n        return actions\n\n    def prepare_state(self, batch):\n        \"\"\"Pad state\"\"\"\n        state = batch[OBS_STATE][:, -1, :] if batch[OBS_STATE].ndim > 2 else batch[OBS_STATE]\n        state = pad_vector(state, self.config.max_state_dim)\n        return state\n\n    def prepare_action(self, batch):\n        \"\"\"Pad action\"\"\"\n        actions = pad_vector(batch[ACTION], self.config.max_action_dim)\n        return actions\n\n    def _get_default_peft_targets(self) -> dict[str, any]:\n        \"\"\"Return default PEFT target modules for SmolVLA fine-tuning.\"\"\"\n        common_projections = (\n            \"state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out\"\n        )\n        target_modules = rf\"(model\\.vlm_with_expert\\.lm_expert\\..*\\.(q|v)_proj|model\\.({common_projections}))\"\n        return {\n            \"target_modules\": target_modules,\n            \"modules_to_save\": [],\n        }\n\n    def _validate_peft_config(self, peft_config) -> None:\n        \"\"\"Validate PEFT configuration for SmolVLA.\"\"\"\n        super()._validate_peft_config(peft_config)\n        if not self.config.load_vlm_weights:\n            import logging\n\n            logging.warning(\n                \"Training SmolVLA from scratch using PEFT. This is unlikely to yield good results. \"\n                \"Set `load_vlm_weights=True` to fine-tune the existing policy.\"\n            )\n\n\ndef pad_tensor(tensor, max_len, pad_value=0):\n    \"\"\"\n    Efficiently pads a tensor along sequence dimension to match max_len.\n\n    Args:\n        tensor (torch.Tensor): Shape (B, L, ...) or (B, L).\n        max_len (int): Fixed sequence length.\n        pad_value (int/float): Value for padding.\n\n    Returns:\n        torch.Tensor: Shape (B, max_len, ...) or (B, max_len).\n    \"\"\"\n    b, d = tensor.shape[:2]\n\n    # Create a padded tensor of max_len and copy the existing values\n    padded_tensor = torch.full(\n        (b, max_len, *tensor.shape[2:]), pad_value, dtype=tensor.dtype, device=tensor.device\n    )\n    padded_tensor[:, :d] = tensor  # Efficient in-place copy\n\n    return padded_tensor\n\n\nclass VLAFlowMatching(nn.Module):\n    \"\"\"\n    SmolVLA\n\n    [Paper]()\n\n    Designed by Hugging Face.\n    ┌──────────────────────────────┐\n    │                 actions      │\n    │                    ▲         │\n    │ ┌─────────┐      ┌─|────┐    │\n    │ |         │────► │      │    │\n    │ |         │ kv   │      │    │\n    │ |         │────► │Action│    │\n    │ |   VLM   │cache │Expert│    |\n    │ │         │────► |      │    │\n    │ │         │      │      │    │\n    │ └▲──▲───▲─┘      └───▲──┘    |\n    │  │  |   |            │       |\n    │  |  |   |          noise     │\n    │  │  │ state                  │\n    │  │ language tokens           │\n    │  image(s)                    │\n    └──────────────────────────────┘\n    \"\"\"\n\n    def __init__(self, config: SmolVLAConfig, rtc_processor: RTCProcessor | None = None):\n        super().__init__()\n        self.config = config\n\n        self.vlm_with_expert = SmolVLMWithExpertModel(\n            model_id=self.config.vlm_model_name,\n            freeze_vision_encoder=self.config.freeze_vision_encoder,\n            train_expert_only=self.config.train_expert_only,\n            load_vlm_weights=self.config.load_vlm_weights,\n            attention_mode=self.config.attention_mode,\n            num_expert_layers=self.config.num_expert_layers,\n            num_vlm_layers=self.config.num_vlm_layers,\n            self_attn_every_n_layers=self.config.self_attn_every_n_layers,\n            expert_width_multiplier=self.config.expert_width_multiplier,\n            device=self.config.device if self.config.device is not None else \"auto\",\n        )\n        self.state_proj = nn.Linear(\n            self.config.max_state_dim, self.vlm_with_expert.config.text_config.hidden_size\n        )\n        self.action_in_proj = nn.Linear(self.config.max_action_dim, self.vlm_with_expert.expert_hidden_size)\n        self.action_out_proj = nn.Linear(self.vlm_with_expert.expert_hidden_size, self.config.max_action_dim)\n\n        self.action_time_mlp_in = nn.Linear(\n            self.vlm_with_expert.expert_hidden_size * 2, self.vlm_with_expert.expert_hidden_size\n        )\n        self.action_time_mlp_out = nn.Linear(\n            self.vlm_with_expert.expert_hidden_size, self.vlm_with_expert.expert_hidden_size\n        )\n\n        self.set_requires_grad()\n        self.fake_image_token = self.vlm_with_expert.processor.tokenizer.fake_image_token_id\n        self.global_image_token = self.vlm_with_expert.processor.tokenizer.global_image_token_id\n        self.global_image_start_token = torch.tensor(\n            [self.fake_image_token, self.global_image_token], dtype=torch.long\n        )\n\n        self.add_image_special_tokens = self.config.add_image_special_tokens\n        self.image_end_token = torch.tensor([self.fake_image_token], dtype=torch.long)\n        self.prefix_length = self.config.prefix_length\n        self.rtc_processor = rtc_processor\n\n        # Compile model if requested\n        if config.compile_model:\n            torch.set_float32_matmul_precision(\"high\")\n            self.sample_actions = torch.compile(self.sample_actions, mode=config.compile_mode)\n            self.forward = torch.compile(self.forward, mode=config.compile_mode)\n\n    def _rtc_enabled(self):\n        return self.config.rtc_config is not None and self.config.rtc_config.enabled\n\n    def set_requires_grad(self):\n        for params in self.state_proj.parameters():\n            params.requires_grad = self.config.train_state_proj\n\n    def sample_noise(self, shape, device):\n        noise = torch.normal(\n            mean=0.0,\n            std=1.0,\n            size=shape,\n            dtype=torch.float32,\n            device=device,\n        )\n        return noise\n\n    def sample_time(self, bsize, device):\n        beta_dist = torch.distributions.Beta(concentration1=1.5, concentration0=1.0)\n        time_beta = beta_dist.sample((bsize,)).to(device=device, dtype=torch.float32)\n        time = time_beta * 0.999 + 0.001\n        return time\n\n    def embed_prefix(\n        self, images, img_masks, lang_tokens, lang_masks, state: torch.Tensor = None\n    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:\n        \"\"\"Embed images with SigLIP and language tokens with embedding layer to prepare\n        for SmolVLM transformer processing.\n        \"\"\"\n        embs = []\n        pad_masks = []\n        att_masks = []\n        for _img_idx, (\n            img,\n            img_mask,\n        ) in enumerate(zip(images, img_masks, strict=False)):\n            if self.add_image_special_tokens:\n                image_start_token = (\n                    self.vlm_with_expert.embed_language_tokens(\n                        self.global_image_start_token.to(device=self.vlm_with_expert.vlm.device)\n                    )\n                    .unsqueeze(0)\n                    .expand(img.shape[0], -1, -1)\n                )\n                image_start_mask = torch.ones_like(\n                    image_start_token[:, :, 0], dtype=torch.bool, device=image_start_token.device\n                )\n                att_masks += [0] * (image_start_mask.shape[-1])\n                embs.append(image_start_token)\n                pad_masks.append(image_start_mask)\n\n            img_emb = self.vlm_with_expert.embed_image(img)\n            img_emb = img_emb\n\n            # Normalize image embeddings\n            img_emb_dim = img_emb.shape[-1]\n            img_emb = img_emb * torch.tensor(img_emb_dim**0.5, dtype=img_emb.dtype, device=img_emb.device)\n\n            bsize, num_img_embs = img_emb.shape[:2]\n            img_mask = img_mask[:, None].expand(bsize, num_img_embs)\n\n            embs.append(img_emb)\n            pad_masks.append(img_mask)\n\n            att_masks += [0] * (num_img_embs)\n            if self.add_image_special_tokens:\n                image_end_token = (\n                    self.vlm_with_expert.embed_language_tokens(\n                        self.image_end_token.to(device=self.vlm_with_expert.vlm.device)\n                    )\n                    .unsqueeze(0)\n                    .expand(img.shape[0], -1, -1)\n                )\n                image_end_mask = torch.ones_like(\n                    image_end_token[:, :, 0], dtype=torch.bool, device=image_end_token.device\n                )\n                embs.append(image_end_token)\n                pad_masks.append(image_end_mask)\n                att_masks += [0] * (image_end_mask.shape[1])\n        lang_emb = self.vlm_with_expert.embed_language_tokens(lang_tokens)\n        # Normalize language embeddings\n        lang_emb_dim = lang_emb.shape[-1]\n        lang_emb = lang_emb * math.sqrt(lang_emb_dim)\n\n        embs.append(lang_emb)\n        pad_masks.append(lang_masks)\n\n        num_lang_embs = lang_emb.shape[1]\n        att_masks += [0] * num_lang_embs\n\n        state_emb = self.state_proj(state)\n        state_emb = state_emb[:, None, :] if state_emb.ndim == 2 else state_emb\n        embs.append(state_emb)\n        bsize = state_emb.shape[0]\n        device = state_emb.device\n\n        states_seq_len = state_emb.shape[1]\n        state_mask = torch.ones(bsize, states_seq_len, dtype=torch.bool, device=device)\n        pad_masks.append(state_mask)\n\n        # Set attention masks so that image and language inputs do not attend to state or actions\n        att_masks += [1] * (states_seq_len)\n        embs = torch.cat(embs, dim=1)\n        pad_masks = torch.cat(pad_masks, dim=1)\n        att_masks = torch.tensor(att_masks, dtype=torch.bool, device=pad_masks.device)\n        att_masks = att_masks[None, :]\n\n        seq_len = pad_masks.shape[1]\n        if seq_len < self.prefix_length:\n            embs = pad_tensor(embs, self.prefix_length, pad_value=0)\n            pad_masks = pad_tensor(pad_masks, self.prefix_length, pad_value=0)\n            att_masks = pad_tensor(att_masks, self.prefix_length, pad_value=0)\n\n        att_masks = att_masks.expand(bsize, -1)\n\n        return embs, pad_masks, att_masks\n\n    def embed_suffix(self, noisy_actions, timestep):\n        \"\"\"Embed state, noisy_actions, timestep to prepare for Expert Gemma processing.\"\"\"\n        embs = []\n        pad_masks = []\n        att_masks = []\n\n        # Fuse timestep + action information using an MLP\n        action_emb = self.action_in_proj(noisy_actions)\n        device = action_emb.device\n        bsize = action_emb.shape[0]\n        dtype = action_emb.dtype\n        # Embed timestep using sine-cosine positional encoding with sensitivity in the range [0, 1]\n        time_emb = create_sinusoidal_pos_embedding(\n            timestep,\n            self.vlm_with_expert.expert_hidden_size,\n            self.config.min_period,\n            self.config.max_period,\n            device=device,\n        )\n        time_emb = time_emb.type(dtype=dtype)\n\n        time_emb = time_emb[:, None, :].expand_as(action_emb)\n        action_time_emb = torch.cat([action_emb, time_emb], dim=2)\n\n        action_time_emb = self.action_time_mlp_in(action_time_emb)\n        action_time_emb = F.silu(action_time_emb)  # swish == silu\n        action_time_emb = self.action_time_mlp_out(action_time_emb)\n\n        # Add to input tokens\n        embs.append(action_time_emb)\n\n        bsize, action_time_dim = action_time_emb.shape[:2]\n        action_time_mask = torch.ones(bsize, action_time_dim, dtype=torch.bool, device=device)\n        pad_masks.append(action_time_mask)\n\n        # Set attention masks so that image, language and state inputs do not attend to action tokens\n        att_masks += [1] * self.config.chunk_size\n        embs = torch.cat(embs, dim=1)\n        pad_masks = torch.cat(pad_masks, dim=1)\n        att_masks = torch.tensor(att_masks, dtype=embs.dtype, device=embs.device)\n        att_masks = att_masks[None, :].expand(bsize, len(att_masks))\n        return embs, pad_masks, att_masks\n\n    def forward(\n        self, images, img_masks, lang_tokens, lang_masks, state, actions, noise=None, time=None\n    ) -> Tensor:\n        \"\"\"Do a full training forward pass and compute the loss (batch_size x num_steps x num_motors)\"\"\"\n        if noise is None:\n            noise = self.sample_noise(actions.shape, actions.device)\n\n        if time is None:\n            time = self.sample_time(actions.shape[0], actions.device)\n\n        time_expanded = time[:, None, None]\n        x_t = time_expanded * noise + (1 - time_expanded) * actions\n        u_t = noise - actions\n        prefix_embs, prefix_pad_masks, prefix_att_masks = self.embed_prefix(\n            images, img_masks, lang_tokens, lang_masks, state=state\n        )\n        suffix_embs, suffix_pad_masks, suffix_att_masks = self.embed_suffix(x_t, time)\n\n        pad_masks = torch.cat([prefix_pad_masks, suffix_pad_masks], dim=1)\n        att_masks = torch.cat([prefix_att_masks, suffix_att_masks], dim=1)\n\n        att_2d_masks = make_att_2d_masks(pad_masks, att_masks)\n        position_ids = torch.cumsum(pad_masks, dim=1) - 1\n        (_, suffix_out), _ = self.vlm_with_expert.forward(\n            attention_mask=att_2d_masks,\n            position_ids=position_ids,\n            past_key_values=None,\n            inputs_embeds=[prefix_embs, suffix_embs],\n            use_cache=False,\n            fill_kv_cache=False,\n        )\n        suffix_out = suffix_out[:, -self.config.chunk_size :]\n        # Original openpi code, upcast attention output\n        suffix_out = suffix_out.to(dtype=torch.float32)\n        v_t = self.action_out_proj(suffix_out)\n        losses = F.mse_loss(u_t, v_t, reduction=\"none\")\n        return losses\n\n    def sample_actions(\n        self,\n        images,\n        img_masks,\n        lang_tokens,\n        lang_masks,\n        state,\n        noise=None,\n        **kwargs: Unpack[ActionSelectKwargs],\n    ) -> Tensor:\n        \"\"\"Do a full inference forward and compute the action (batch_size x num_steps x num_motors)\"\"\"\n        bsize = state.shape[0]\n        device = state.device\n\n        if noise is None:\n            actions_shape = (bsize, self.config.chunk_size, self.config.max_action_dim)\n            noise = self.sample_noise(actions_shape, device)\n\n        prefix_embs, prefix_pad_masks, prefix_att_masks = self.embed_prefix(\n            images, img_masks, lang_tokens, lang_masks, state=state\n        )\n        prefix_att_2d_masks = make_att_2d_masks(prefix_pad_masks, prefix_att_masks)\n        prefix_position_ids = torch.cumsum(prefix_pad_masks, dim=1) - 1\n        # Compute image and language key value cache\n        _, past_key_values = self.vlm_with_expert.forward(\n            attention_mask=prefix_att_2d_masks,\n            position_ids=prefix_position_ids,\n            past_key_values=None,\n            inputs_embeds=[prefix_embs, None],\n            use_cache=self.config.use_cache,\n            fill_kv_cache=True,\n        )\n        num_steps = self.config.num_steps\n        dt = -1.0 / num_steps\n\n        x_t = noise\n        for step in range(num_steps):\n            time = 1.0 + step * dt\n            time_tensor = torch.tensor(time, dtype=torch.float32, device=device).expand(bsize)\n\n            def denoise_step_partial_call(input_x_t, current_timestep=time_tensor):\n                return self.denoise_step(\n                    x_t=input_x_t,\n                    prefix_pad_masks=prefix_pad_masks,\n                    past_key_values=past_key_values,\n                    timestep=current_timestep,\n                )\n\n            if self._rtc_enabled():\n                inference_delay = kwargs.get(\"inference_delay\")\n                prev_chunk_left_over = kwargs.get(\"prev_chunk_left_over\")\n                execution_horizon = kwargs.get(\"execution_horizon\")\n\n                v_t = self.rtc_processor.denoise_step(\n                    x_t=x_t,\n                    prev_chunk_left_over=prev_chunk_left_over,\n                    inference_delay=inference_delay,\n                    time=time,\n                    original_denoise_step_partial=denoise_step_partial_call,\n                    execution_horizon=execution_horizon,\n                )\n            else:\n                v_t = denoise_step_partial_call(x_t)\n\n            x_t = x_t + dt * v_t\n\n            if self.rtc_processor is not None and self.rtc_processor.is_debug_enabled():\n                self.rtc_processor.track(time=time, x_t=x_t, v_t=v_t)\n\n        return x_t\n\n    def denoise_step(\n        self,\n        prefix_pad_masks,\n        past_key_values,\n        x_t,\n        timestep,\n    ):\n        \"\"\"Apply one denoising step of the noise `x_t` at a given timestep.\"\"\"\n        suffix_embs, suffix_pad_masks, suffix_att_masks = self.embed_suffix(x_t, timestep)\n\n        suffix_len = suffix_pad_masks.shape[1]\n        batch_size = prefix_pad_masks.shape[0]\n        prefix_len = prefix_pad_masks.shape[1]\n        prefix_pad_2d_masks = prefix_pad_masks[:, None, :].expand(batch_size, suffix_len, prefix_len)\n\n        suffix_att_2d_masks = make_att_2d_masks(suffix_pad_masks, suffix_att_masks)\n\n        full_att_2d_masks = torch.cat([prefix_pad_2d_masks, suffix_att_2d_masks], dim=2)\n        prefix_offsets = torch.sum(prefix_pad_masks, dim=-1)[:, None]\n        position_ids = prefix_offsets + torch.cumsum(suffix_pad_masks, dim=1) - 1\n\n        outputs_embeds, _ = self.vlm_with_expert.forward(\n            attention_mask=full_att_2d_masks,\n            position_ids=position_ids,\n            past_key_values=past_key_values,\n            inputs_embeds=[None, suffix_embs],\n            use_cache=self.config.use_cache,\n            fill_kv_cache=False,\n        )\n        suffix_out = outputs_embeds[1]\n        suffix_out = suffix_out[:, -self.config.chunk_size :]\n        suffix_out = suffix_out.to(dtype=torch.float32)\n        v_t = self.action_out_proj(suffix_out)\n        return v_t\n",
      "numLines": 917,
      "startLine": 1,
      "totalLines": 917
    }
  }
}
````

</details>

---
