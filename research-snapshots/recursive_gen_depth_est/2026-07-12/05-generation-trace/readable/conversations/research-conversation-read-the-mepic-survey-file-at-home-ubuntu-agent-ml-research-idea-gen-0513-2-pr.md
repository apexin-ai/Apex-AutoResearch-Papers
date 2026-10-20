# Research conversation: Read the MEPIC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/me

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac52294b4d40fe0d9.jsonl`
- **Structured JSON:** [`85d3992a7d02f6409964.json`](../../sessions/85/85d3992a7d02f6409964.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-14T05:13:50.703Z_

Read the MEPIC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md to understand the MEPIC NoPE implementation details. Report back: how NoPE KV storage works, how boundary recomputation works, monkey-patching approach, and any code snippets.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "408b9aa3-c2e6-4892-a0f1-7346e3d62a27",
  "agentId": "ac52294b4d40fe0d9",
  "type": "user",
  "uuid": "86484b8b-69f4-4fac-bbf7-63809d5ffb4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache",
  "sessionId": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-14T05:13:51.668Z_

I'll read the MEPIC survey file to understand the NoPE implementation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86484b8b-69f4-4fac-bbf7-63809d5ffb4f",
  "isSidechain": true,
  "agentId": "ac52294b4d40fe0d9",
  "requestId": "req_011Cb1ta2pEw5gY4kdffV1AR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "afa32f6f-be6b-4974-af1e-2e1f73e3bfd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache",
  "sessionId": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018CQCugwPsNP8QfA9ETFspH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 17934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 516,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 3 · 2026-05-14T05:13:51.854Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ANVRb2TCFq67VNV1U6cfn7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afa32f6f-be6b-4974-af1e-2e1f73e3bfd2",
  "isSidechain": true,
  "agentId": "ac52294b4d40fe0d9",
  "requestId": "req_011Cb1ta2pEw5gY4kdffV1AR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f38facc0-48fc-4e3d-a169-1dffdafeed2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache",
  "sessionId": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018CQCugwPsNP8QfA9ETFspH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 17934,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 516
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 17934,
          "cache_creation_input_tokens": 516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 516,
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

_source line 4 · 2026-05-14T05:13:51.860Z_

<details><summary>↩ Tool result · `toolu_01ANVRb2TCFq67VNV1U6cfn7`</summary>

````text
1	# MEPIC 技术调研报告
2	
3	## 1. 概述
4	
5	**MEPIC** (Memory-Efficient Position-Independent Caching) 是一种面向 LLM serving 的 KV cache 复用系统，核心思想是将 KV cache 以 **NoPE (No Positional Encoding)** 格式存储，在 attention 计算时通过 fused kernel 动态注入 RoPE，从而实现 chunk-level KV 在不同位置、不同请求、不同 batch 间的无损复用。
6	
7	- **论文**: [arXiv:2512.16822](https://arxiv.org/abs/2512.16822) (2025.12)
8	- **作者**: Qian Wang, Zahra Yousefijamarani, Morgan Lindsay Heisler, Rongzhi Gu 等
9	- **代码**: **未开源**。论文基于 vLLM + LMCache 实现，但无公开仓库。
10	- **前身**: [EPIC](https://arxiv.org/abs/2410.15332) (ICML 2025)，代码开源于 [GitHub](https://github.com/DerekHJH/epic)（vLLM 0.7.0 fork）
11	
12	### 1.1 相关工作谱系
13	
14	| 系统 | 核心策略 | RoPE 处理 | 复用粒度 | 代码 |
15	|------|---------|-----------|---------|------|
16	| **CacheBlend** (EuroSys'25) | 比较 ΔK 选 15% token 重算 | 标准 post-RoPE 存储 | Token-level | ✗ |
17	| **EPIC** (ICML'25) | LegoLink: 重算每 chunk 前 k 个 token | 标准 post-RoPE 存储 | Token-level | [✓](https://github.com/DerekHJH/epic) |
18	| **MEPIC** (2025.12) | NoPE 存储 + fused RoPE attention | **NoPE: 去除 RoPE** | Block-level | ✗ |
19	| **KV Packet** (2026.04) | Soft-token adapter 包裹 chunk | 无需修改 RoPE | Chunk-level | ✗ |
20	
21	---
22	
23	## 2. 核心技术机制
24	
25	### 2.1 NoPE KV 存储
26	
27	**标准流程** (HuggingFace transformers / vLLM):
28	```
29	Q, K, V = proj(hidden_states)
30	Q_rope, K_rope = apply_rotary_pos_emb(Q, K, cos, sin)  # RoPE 嵌入位置信息
31	cache.update(K_rope, V)  # 存储 post-RoPE 的 K
32	attn = softmax(Q_rope @ K_rope^T / sqrt(d)) @ V
33	```
34	
35	**MEPIC NoPE 流程**:
36	```
37	Q, K, V = proj(hidden_states)
38	Q_rope = apply_rotary_pos_emb(Q, cos, sin)  # 仅 Q 应用 RoPE
39	cache.update(K, V)  # 存储 pre-RoPE 的 K（NoPE 格式）
40	# attention 计算时在 fused kernel 中动态对 K 应用 RoPE
41	attn = fused_rope_attention(Q_rope, K_nope, V, position_offsets)
42	```
43	
44	**关键差异**: KV cache 中的 key 不包含位置信息，因此同一 chunk 的 KV 可在任意位置复用。
45	
46	### 2.2 RoPE 数学基础
47	
48	RoPE 对 d 维向量按 d/2 对逐对旋转：
49	
50	**正向 (apply)**:
51	```
52	θ_i = 10000^(-2(i-1)/d),  i ∈ [1, d/2]
53	
54	RoPE(x, m) = [x_1·cos(mθ_1) - x_{d/2+1}·sin(mθ_1),
55	               x_2·cos(mθ_2) - x_{d/2+2}·sin(mθ_2),
56	               ...,
57	               x_{d/2+1}·cos(mθ_1) + x_1·sin(mθ_1),
58	               ...]
59	```
60	
61	HuggingFace 实现:
62	```python
63	def rotate_half(x):
64	    x1 = x[..., :x.shape[-1] // 2]
65	    x2 = x[..., x.shape[-1] // 2:]
66	    return torch.cat((-x2, x1), dim=-1)
67	
68	def apply_rotary_pos_emb(q, k, cos, sin):
69	    q_embed = (q * cos) + (rotate_half(q) * sin)
70	    k_embed = (k * cos) + (rotate_half(k) * sin)
71	    return q_embed, k_embed
72	```
73	
74	**逆向 (remove/undo)**:
75	旋转矩阵的逆就是转置（等价于用 -θ 旋转）：
76	```python
77	def remove_rotary_pos_emb(k_rope, cos, sin):
78	    """从 post-RoPE key 恢复 pre-RoPE key"""
79	    k_nope = (k_rope * cos) + (rotate_half(k_rope) * (-sin))
80	    return k_nope
81	    # 等价于: k_nope = (k_rope * cos) - (rotate_half(k_rope) * sin)
82	```
83	
84	**Attention score 不变性**:
85	```
86	⟨RoPE(q, m), RoPE(k, n)⟩ = ⟨RoPE(q, m-n), k⟩
87	```
88	即：如果 key 未应用 RoPE，只需在 query 上应用相对位置 (m-n) 的旋转即可得到正确的 attention score。这是 MEPIC NoPE 方案的数学基础。
89	
90	### 2.3 Fused RoPE-Attention Kernel
91	
92	MEPIC 将 RoPE 应用融合到 attention kernel 中：
93	
94	```
95	// Pseudocode for fused kernel
96	for each query token at position m:
97	    for each key block at position range [n_start, n_end]:
98	        // 从 HBM 加载 NoPE key block
99	        K_nope = load_from_hbm(block_id)
100	        // 在 SRAM 中动态应用 RoPE offset
101	        for each key at position n in [n_start, n_end]:
102	            K_rope[n] = apply_rope(K_nope[n], cos[n], sin[n])
103	        // 计算 attention score
104	        score = Q_rope[m] @ K_rope^T / sqrt(d)
105	```
106	
107	vLLM 已有 `rope_kvcache_fusion` 编译 pass，将 RoPE 和 KV cache 写入操作融合为单一 kernel。MEPIC 在此基础上进一步将 RoPE 推迟到 attention 计算阶段。
108	
109	### 2.4 Block 对齐与 Padding
110	
111	MEPIC 使用 **非对称 padding** 确保每个 chunk 的起始对齐到 KV page boundary：
112	
113	| 段类型 | Padding 方式 | 原因 |
114	|--------|-------------|------|
115	| Chunk 段 | **前导 padding** (leading) | 确保 chunk 起始对齐到 block 边界 |
116	| Prompt 段 | **尾部 padding** (trailing) | 填充到 block 边界 |
117	| 最后一个 Prompt 段 | 无 padding | 避免浪费 |
118	
119	Padding pattern 还隐式编码了段类型，计算路径无需额外 metadata 即可区分 chunk 和 prompt。
120	
121	**示例**: Block size = 16 tokens
122	```
123	[pad pad pad chunk_token_1 ... chunk_token_16] [chunk_token_17 ... chunk_token_32] ...
124	     leading padding           block 1 (first block)        block 2 (canonical, shareable)
125	```
126	
127	### 2.5 First-Block Recomputation
128	
129	这是 MEPIC 最关键的设计之一：
130	
131	**规则**: 对于每个 cached chunk，仅重新计算其**第一个 KV block**，其余 block 直接复用 canonical KV。
132	
133	**原因**:
134	1. Chunk 第一个 block 包含与前文（其他 chunk 或 prompt）的 cross-attention 边界效应
135	2. 后续 block 的 KV 主要取决于 chunk 内部上下文，位置无关
136	3. 重算一个 block（通常 16 tokens）的开销远小于重算整个 chunk
137	
138	**实现**:
139	- 第一个 block: 通过 vLLM prefix cache 分配和重算（request-specific）
140	- 后续 block: 通过 chunk cache 管理（canonical, shared across requests）
141	
142	**与 EPIC LegoLink 的对比**:
143	| | EPIC LegoLink | MEPIC First-Block |
144	|---|---|---|
145	| 重算粒度 | Token-level (前 k 个 token) | Block-level (第一个 block) |
146	| 选择策略 | 静态: k ≤ 32 | 固定: 1 个 block |
147	| 复杂度 | O(kN) | O(B) where B = block_size |
148	| 存储格式 | Post-RoPE | NoPE |
149	
150	### 2.6 Scheduling Path (Algorithm 1)
151	
152	```
153	Input:  Request tokens T with segment markers
154	Output: Padded tokens T_align + paged KV block mapping, or Reject
155	
156	1. Segmentation: 根据 markers 将 T 分为 {S_1, ..., S_m}
157	2. Canonicalization: 
158	   - 确定每段类型 (chunk / prompt)
159	   - 对每段应用 padding 实现 block 对齐
160	   - 构造 T_align
161	3. Residency Resolution:
162	   - 对每段检查 HBM 驻留状态
163	   - Hash chunk 的 padded token 序列确定身份
164	4. Admission Check:
165	   - 估算非驻留段需要的 KV blocks
166	   - 若不够且无法通过 LRU 回收 → Reject
167	5. KV Block Allocation:
168	   - 按驻留/类型分配 paged KV blocks
169	   - Return T_align + block mapping
170	```
171	
172	### 2.7 系统架构
173	
174	MEPIC 扩展 vLLM 的 paged KV 管理：
175	
176	```
177	┌─ Scheduling Path ─────────────────────────────────┐
178	│  Chunk Processor → Chunk Matcher → Hybrid KV Mgr  │
179	│  (segmentation/    (residency     (prefix/chunk    │
180	│   canonicalization) resolution)    coordination)   │
181	│                                  + Chunk LRU Mgr   │
182	└────────────────────────────────────────────────────┘
183	                          │
184	                          ▼
185	┌─ Computation Path ────────────────────────────────┐
186	│  Selective Recomputation → Fused-RoPE Attention    │
187	│  (first block only)       (NoPE → RoPE on-the-fly) │
188	└────────────────────────────────────────────────────┘
189	```
190	
191	---
192	
193	## 3. 性能评估
194	
195	### 3.1 HBM 节省
196	
197	| 对比基线 | HBM 节省倍数 | 条件 |
198	|---------|-------------|------|
199	| CacheBlend | 2× | 常规场景 |
200	| EPIC | 2× | 常规场景 |
201	| CacheBlend | 5.74× | 高 QPS |
202	| EPIC | 5.25× | 高 QPS |
203	| 长 prompt | 5× | 长上下文 |
204	
205	### 3.2 延迟
206	
207	- 比 EPIC 低 9.1%
208	- 比 CacheBlend 低 11.48%
209	
210	### 3.3 精度
211	
212	在 SQuAD, NewsQA, NarrativeQA, emrQA 上 F1/Rouge-L 与 baseline 持平或略优。
213	
214	### 3.4 Recomputation 开销
215	
216	各数据集平均每个 request 需重算 29-521 tokens。
217	
218	---
219	
220	## 4. EPIC 代码分析（可参考实现）
221	
222	EPIC 是 MEPIC 的前身，有开源代码 ([GitHub](https://github.com/DerekHJH/epic))，基于 vLLM 0.7.0 fork，约 2K 行 Python。
223	
224	### 4.1 核心模块
225	
226	| 模块 | 功能 |
227	|------|------|
228	| **KVGen** | 为静态 chunk 预生成 KV cache |
229	| **KVStore** | 管理 KV cache 存储 (HBM/DRAM/filesystem) |
230	| **KVLink** | 检索、拼接 KV cache，执行 LegoLink 选择性重算 |
231	| **KVSplit** | 可选的语义切分模块 |
232	
233	### 4.2 关键修改点
234	
235	1. **Attention backend**: 支持 masked attention across scattered positions
236	2. **Memory management**: 扩展至 DRAM/filesystem
237	3. **Scheduler**: 管理 cache 生命周期 (create/expire)
238	
239	### 4.3 LegoLink 重算流程
240	
241	```python
242	# Pseudocode
243	for each chunk (except first):
244	    # 取前 k 个 token 的 embedding
245	    embeds = get_embeddings(chunk[:k])
246	    Q, K, V = project(embeds)
247	    # 拼接已缓存的 KV
248	    K_expanded = concat(cached_KV, K)
249	    # 带 mask 的 attention (causal + chunk boundary)
250	    attn = masked_attention(Q, K_expanded, mask)
251	    # 更新这 k 个 token 的 KV cache
252	    update_cache(chunk[:k], new_KV)
253	```
254	
255	---
256	
257	## 5. 为 CompressLink 实现 MEPIC 的设计方案
258	
259	### 5.1 实现策略选择
260	
261	鉴于 MEPIC 没有开源代码，且其实现依赖 vLLM 的 paged attention 和自定义 CUDA kernel，**不建议直接复刻 MEPIC 的 serving 系统**。
262	
263	对于 CompressLink，我们需要的是 MEPIC 的**核心算法组件**（NoPE KV + RoPE-on-query），而非其 serving 框架。建议基于 HuggingFace transformers 实现 functional MEPIC。
264	
265	### 5.2 需要 Hook/修改的模块
266	
267	#### (1) `apply_rotary_pos_emb` — 分离 Q/K 的 RoPE
268	
269	**文件**: `transformers/models/llama/modeling_llama.py` (或目标模型)
270	
271	**当前代码** (~L95):
272	```python
273	cos, sin = position_embeddings
274	query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
275	```
276	
277	**修改方案**: 仅对 query 应用 RoPE，key 保持 NoPE
278	```python
279	cos, sin = position_embeddings
280	if use_nope_kv:
281	    query_states = apply_rotary_pos_emb_query_only(query_states, cos, sin)
282	    # key_states 保持原样 (NoPE)
283	else:
284	    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
285	```
286	
287	#### (2) KV Cache 更新 — 存储 NoPE keys
288	
289	**当前代码**:
290	```python
291	# RoPE 已应用后才存入 cache
292	key_states, value_states = past_key_values.update(key_states, value_states, self.layer_idx)
293	```
294	
295	**修改**: NoPE 模式下，存入 cache 的 key 不含 RoPE。无需修改 cache.update 本身，因为 key_states 已经是 NoPE 的。
296	
297	#### (3) Attention 计算 — 动态 RoPE
298	
299	**修改方案**: 从 cache 取出 NoPE keys 后，在 attention 前动态施加 RoPE
300	
301	```python
302	def nope_attention(query_states, key_states, value_states, cos_full, sin_full):
303	    """
304	    query_states: 已应用 RoPE 的 Q [B, H, L_q, D]
305	    key_states:   NoPE 格式的 K [B, H, L_kv, D]  (从 cache 取出)
306	    cos_full/sin_full: 所有 key 位置对应的 cos/sin
307	    """
308	    # 对 NoPE keys 动态施加 RoPE
309	    key_states_rope = apply_rotary_pos_emb_key_only(key_states, cos_full, sin_full)
310	    # 标准 attention
311	    attn_weights = torch.matmul(query_states, key_states_rope.transpose(-2, -1)) / math.sqrt(d)
312	    attn_weights = F.softmax(attn_weights, dim=-1)
313	    attn_output = torch.matmul(attn_weights, value_states)
314	    return attn_output
315	```
316	
317	#### (4) 辅助函数
318	
319	```python
320	def apply_rotary_pos_emb_query_only(q, cos, sin):
321	    """仅对 query 应用 RoPE"""
322	    return (q * cos) + (rotate_half(q) * sin)
323	
324	def apply_rotary_pos_emb_key_only(k, cos, sin):
325	    """对 NoPE key 施加指定位置的 RoPE"""
326	    return (k * cos) + (rotate_half(k) * sin)
327	
328	def remove_rotary_pos_emb(k_rope, cos, sin):
329	    """从 post-RoPE key 恢复 NoPE key (用于转换已有 cache)"""
330	    return (k_rope * cos) - (rotate_half(k_rope) * sin)
331	```
332	
333	### 5.3 Boundary Recomputation 实现
334	
335	```python
336	class BoundaryRecomputer:
337	    def __init__(self, model, block_size=16):
338	        self.model = model
339	        self.block_size = block_size
340	    
341	    def recompute_first_block(self, chunk_kv, prefix_hidden_states, chunk_tokens):
342	        """
343	        重算 chunk 第一个 block 的 KV。
344	        
345	        Args:
346	            chunk_kv: cached NoPE KV for the full chunk
347	            prefix_hidden_states: 前文的 hidden states (用于 cross attention)
348	            chunk_tokens: chunk 的 token ids
349	        
350	        Returns:
351	            updated chunk_kv with recomputed first block
352	        """
353	        first_block_tokens = chunk_tokens[:self.block_size]
354	        # 将前文 + 第一个 block 一起前向传播
355	        combined_input = concat(prefix_hidden_states, first_block_tokens)
356	        new_kv = self.model.forward_partial(combined_input)
357	        # 替换第一个 block 的 KV
358	        chunk_kv[:, :, :self.block_size, :] = new_kv[:, :, -self.block_size:, :]
359	        return chunk_kv
360	```
361	
362	### 5.4 预估代码量与难度
363	
364	| 组件 | 代码量 | 难度 | 说明 |
365	|------|--------|------|------|
366	| NoPE KV 存储 (Q-only RoPE) | ~50 行 | 低 | 修改 attention forward |
367	| 动态 RoPE attention | ~80 行 | 中 | 需处理 position_ids mapping |
368	| Boundary recomputation | ~150 行 | 中 | 需 partial forward 支持 |
369	| RoPE remove/restore 工具函数 | ~30 行 | 低 | 纯数学操作 |
370	| Chunk 管理 (segmentation/padding) | ~200 行 | 中 | 对齐逻辑 |
371	| 测试与验证 | ~200 行 | 低 | 正确性验证 |
372	| **总计** | **~710 行** | **中** | |
373	
374	---
375	
376	## 6. 与 KVTC 的兼容性分析
377	
378	### 6.1 共同基础: RoPE-Free Keys
379	
380	**KVTC** 和 **MEPIC** 都依赖 RoPE-free keys：
381	
382	| | KVTC | MEPIC |
383	|---|---|---|
384	| 为何去除 RoPE | RoPE 掩盖了 key 的低秩结构，影响 PCA 压缩率 | 使 KV 位置无关，支持 chunk 复用 |
385	| 去除时机 | 压缩前 remove，解压后 re-apply | 存储时不 apply，attention 时 apply |
386	| 数学操作 | `k_nope = (k_rope * cos) - (rotate_half(k_rope) * sin)` | 直接不应用 RoPE |
387	
388	**兼容性结论**: 两者天然互补。
389	- MEPIC 生成的 NoPE KV 可以直接送入 KVTC 的 PCA 压缩流程（无需额外 remove RoPE 步骤）
390	- KVTC 解压后的 NoPE KV 可以直接用 MEPIC 的 fused RoPE attention 消费
391	
392	### 6.2 CompressLink 集成方案
393	
394	```
395	Chunk Input → NoPE KV 生成 (MEPIC) → KVTC 压缩 → 存储
396	                                                      ↓
397	Query 到达 → KVTC 解压 → First-Block Recomputation → Fused RoPE Attention → Output
398	```
399	
400	---
401	
402	## 7. 与 CEGR (Compression-Error-Guided Restoration) 的关系
403	
404	### 7.1 机制对比
405	
406	| | MEPIC First-Block Recomputation | CEGR |
407	|---|---|---|
408	| 触发条件 | 固定: 每个 cached chunk 的第一个 block | 动态: 基于压缩误差阈值 |
409	| 选择策略 | 位置固定 (block boundary) | 误差驱动 (高误差 token) |
410	| 计算开销 | 低且可预测 (1 block per chunk) | 可变 (取决于压缩质量) |
411	| 适用场景 | Chunk-level KV 复用 | KV 压缩后的质量恢复 |
412	
413	### 7.2 互补性
414	
415	- MEPIC 的 first-block recomputation 处理的是 **chunk 拼接边界** 的上下文断裂问题
416	- CEGR 处理的是 **压缩损失** 导致的 KV 精度退化问题
417	- 两者解决不同层面的问题，可以叠加使用
418	
419	**建议**: 在 CompressLink 中，先用 MEPIC 做 boundary recomputation（修复拼接误差），再用 CEGR 做 compression error restoration（修复压缩误差）。
420	
421	---
422	
423	## 8. 总结与建议
424	
425	### 8.1 关键发现
426	
427	1. **MEPIC 未开源**，但核心算法（NoPE KV + fused RoPE attention）可从论文中完整复现
428	2. **EPIC 有代码**（vLLM fork），但采用不同技术路线（post-RoPE + token-level recomputation），参考价值有限
429	3. **NoPE 格式是 KVTC 和 MEPIC 的共同基础**，CompressLink 应以 NoPE 作为核心 KV 表示
430	4. RoPE 的 apply/remove 是简单的旋转操作，实现难度低
431	5. 主要实现挑战在于 **boundary recomputation 的 partial forward** 和 **position_ids 的正确管理**
432	
433	### 8.2 实现优先级建议
434	
435	1. **P0**: NoPE KV 存储 + Q-only RoPE（基础能力，~50 行）
436	2. **P0**: RoPE remove/restore 工具函数（KVTC 集成需要，~30 行）
437	3. **P1**: 动态 RoPE attention（支持从 NoPE cache 消费 KV，~80 行）
438	4. **P1**: Boundary recomputation（chunk 复用时的精度保障，~150 行）
439	5. **P2**: Chunk 管理与 padding 对齐（production-level 特性，~200 行）
440	
441	### 8.3 风险点
442	
443	- **精度验证**: NoPE 存储在数学上等价，但浮点误差累积可能影响长序列结果，需跑 benchmark 验证
444	- **Flash Attention 兼容**: 标准 Flash Attention 不支持在 kernel 内动态 apply RoPE，可能需要退回到 eager attention 或使用自定义 kernel
445	- **Partial forward**: HuggingFace transformers 没有原生的 partial layer forward，boundary recomputation 需要额外工程
446	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f38facc0-48fc-4e3d-a169-1dffdafeed2d",
  "isSidechain": true,
  "promptId": "408b9aa3-c2e6-4892-a0f1-7346e3d62a27",
  "agentId": "ac52294b4d40fe0d9",
  "type": "user",
  "uuid": "810bc9c9-fab5-4623-b961-321daee62f89",
  "sourceToolAssistantUUID": "f38facc0-48fc-4e3d-a169-1dffdafeed2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache",
  "sessionId": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-14T05:14:10.516Z_

Perfect! I've read the MEPIC survey file. Here's a comprehensive summary of the key implementation details:

## MEPIC NoPE Implementation Details

### 1. **NoPE KV Storage**

The core innovation is storing KV cache in "NoPE" (No Positional Encoding) format:

**Standard approach:**
```python
Q, K, V = proj(hidden_states)
Q_rope, K_rope = apply_rotary_pos_emb(Q, K, cos, sin)  # RoPE applied to both
cache.update(K_rope, V)  # Stores post-RoPE keys
attn = softmax(Q_rope @ K_rope^T / sqrt(d)) @ V
```

**MEPIC NoPE approach:**
```python
Q, K, V = proj(hidden_states)
Q_rope = apply_rotary_pos_emb(Q, cos, sin)  # Only Q gets RoPE
cache.update(K, V)  # Stores pre-RoPE keys (NoPE format)
# RoPE applied dynamically in fused kernel during attention
attn = fused_rope_attention(Q_rope, K_nope, V, position_offsets)
```

**Key insight**: Since KV cache lacks position information, the same chunk can be reused at any position without loss of correctness. This is mathematically valid because: `⟨RoPE(q, m), RoPE(k, n)⟩ = ⟨RoPE(q, m-n), k⟩`

### 2. **Boundary Recomputation (First-Block Strategy)**

MEPIC uses a targeted recomputation approach:

**Rule**: For each cached chunk, **only recompute the first KV block**, reuse subsequent blocks directly.

**Why this works:**
- The first block contains cross-attention boundaries with preceding context (other chunks or prompt)
- Subsequent blocks depend mainly on internal chunk context, relatively position-independent
- Overhead is minimal (1 block ≈ 16 tokens recomputed per chunk)

**Comparison to EPIC LegoLink:**

| Aspect | EPIC LegoLink | MEPIC First-Block |
|--------|---|---|
| Granularity | Token-level (first k tokens) | Block-level (first block) |
| Strategy | Static: k ≤ 32 | Fixed: 1 block |
| Complexity | O(kN) | O(B) where B = block_size |
| Storage | Post-RoPE | NoPE |

### 3. **Monkey-Patching / Hook Points**

The implementation requires modifying 4 key locations in HuggingFace transformers:

**a) Separate Q/K RoPE application** (apply_rotary_pos_emb):
```python
if use_nope_kv:
    query_states = apply_rotary_pos_emb_query_only(query_states, cos, sin)
    # key_states stays NoPE
else:
    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
```

**b) KV Cache storage** (unchanged from user's perspective, since keys are already NoPE)

**c) Attention computation** (dynamic RoPE application):
```python
def nope_attention(query_states, key_states, value_states, cos_full, sin_full):
    # Apply RoPE to NoPE keys dynamically
    key_states_rope = apply_rotary_pos_emb_key_only(key_states, cos_full, sin_full)
    attn_weights = torch.matmul(query_states, key_states_rope.transpose(-2, -1)) / math.sqrt(d)
    attn_weights = F.softmax(attn_weights, dim=-1)
    attn_output = torch.matmul(attn_weights, value_states)
    return attn_output
```

**d) Helper functions:**
```python
def apply_rotary_pos_emb_query_only(q, cos, sin):
    return (q * cos) + (rotate_half(q) * sin)

def apply_rotary_pos_emb_key_only(k, cos, sin):
    return (k * cos) + (rotate_half(k) * sin)

def remove_rotary_pos_emb(k_rope, cos, sin):
    """Recover NoPE key from post-RoPE (for cache migration)"""
    return (k_rope * cos) - (rotate_half(k_rope) * sin)
```

### 4. **RoPE Mathematics**

**Forward application (rotation by angle mθ):**
```python
def rotate_half(x):
    x1 = x[..., :x.shape[-1] // 2]
    x2 = x[..., x.shape[-1] // 2:]
    return torch.cat((-x2, x1), dim=-1)

def apply_rotary_pos_emb(q, k, cos, sin):
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed
```

**Reverse operation (undo RoPE via inverse rotation):**
```python
def remove_rotary_pos_emb(k_rope, cos, sin):
    k_nope = (k_rope * cos) + (rotate_half(k_rope) * (-sin))
    # Equivalent to: (k_rope * cos) - (rotate_half(k_rope) * sin)
```

### 5. **Fused RoPE-Attention Kernel (Pseudocode)**

```c
for each query token at position m:
    for each key block at position range [n_start, n_end]:
        K_nope = load_from_hbm(block_id)
        for each key at position n in [n_start, n_end]:
            K_rope[n] = apply_rope(K_nope[n], cos[n], sin[n])
        score = Q_rope[m] @ K_rope^T / sqrt(d)
```

### 6. **Boundary Recomputation Implementation Pattern**

```python
class BoundaryRecomputer:
    def recompute_first_block(self, chunk_kv, prefix_hidden_states, chunk_tokens):
        first_block_tokens = chunk_tokens[:self.block_size]
        combined_input = concat(prefix_hidden_states, first_block_tokens)
        new_kv = self.model.forward_partial(combined_input)
        chunk_kv[:, :, :self.block_size, :] = new_kv[:, :, -self.block_size:, :]
        return chunk_kv
```

### 7. **Implementation Estimate**

| Component | Lines | Difficulty |
|-----------|-------|-----------|
| NoPE KV storage (Q-only RoPE) | 50 | Low |
| Dynamic RoPE attention | 80 | Medium |
| Boundary recomputation | 150 | Medium |
| RoPE remove/restore utilities | 30 | Low |
| Chunk management (segmentation/padding) | 200 | Medium |
| Testing & verification | 200 | Low |
| **Total** | **~710** | **Medium** |

### 8. **Key Compatibility with KVTC**

Both MEPIC and KVTC are built on RoPE-free keys:
- MEPIC generates NoPE KV (stores without RoPE)
- KVTC removes RoPE before PCA compression
- **Synergy**: MEPIC output can directly feed into KVTC compression without extra processing

The survey file location is: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "810bc9c9-fab5-4623-b961-321daee62f89",
  "isSidechain": true,
  "agentId": "ac52294b4d40fe0d9",
  "requestId": "req_011Cb1ta7ps4MwncVHQq4tik",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d39611af-9d51-4199-a309-1836f1d4a685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache",
  "sessionId": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LnB2SaxkEsxDTbmWJkweyD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8909,
      "cache_read_input_tokens": 18450,
      "output_tokens": 1984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1984,
          "cache_read_input_tokens": 18450,
          "cache_creation_input_tokens": 8909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8909,
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
