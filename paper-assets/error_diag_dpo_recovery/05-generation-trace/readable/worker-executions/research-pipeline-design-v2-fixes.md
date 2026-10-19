# research pipeline design v2 fixes

**error diag dpo recovery** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_research_pipeline-design-v2-fixes_20260512T105951.log`
- **Structured JSON:** [`1cf7c2a8b069d16c5b8c.json`](../../sessions/1c/1cf7c2a8b069d16c5b8c.json)

## Before a recorded user message

44 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
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
  "uuid": "c47d2130-a5c3-434f-b391-10b6056c159a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-rl-active-probe-fl/memory/"
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
    "resetsAt": 1778597400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "206c0cc1-3ddb-4c9d-bb2d-0991391f3a57",
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7"
}
```

---

### Assistant

_source line 4_

我先读取文件内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "bb4880b3-4208-45fd-8621-7ea5646c8a0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJ2MTaA8HQAqzAEy3zngke",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12267,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12267
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01QSEZeEpjuWyoNcYW6DnmAm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "981aa1e7-9e61-451d-8210-e6389c245422",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJ2MTaA8HQAqzAEy3zngke",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12267,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12267
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T11:00:04.307Z_

<details><summary>↩ Tool result · `toolu_01QSEZeEpjuWyoNcYW6DnmAm`</summary>

````text
1	# DMPO + ETADN 训练 Pipeline 设计（v2）
2	
3	## 0. 术语与背景
4	
5	**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。
6	
7	**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。
8	
9	**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。
10	
11	---
12	
13	## 1. DMPO Loss 实现方案
14	
15	### 1.1 完整 DMPO Loss 公式
16	
17	标准 DPO loss（单轮）：
18	
19	```
20	L_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]
21	```
22	
23	DMPO loss（多轮，论文 Eq.16）：
24	
25	```
26	L_DMPO = -E[ log σ(
27	    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]
28	  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]
29	)]
30	```
31	
32	其中时间折扣函数：
33	
34	```
35	φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
36	```
37	
38	- t = turn index (0-indexed)
39	- T = 总 turn 数
40	- γ ∈ (0, 1) = 时间折扣因子
41	- φ(t, T) 单调递减：早期 turn 权重更高
42	
43	**特殊情况**：
44	- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO
45	- γ = 1: φ(t,T) = (T-t)/T → 线性衰减
46	
47	### 1.2 在 trl DPOTrainer 上实现 DMPO
48	
49	**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。
50	
51	**需要修改的核心逻辑**（在 `_compute_loss` 内）：
52	
53	| 原始 trl 行为 | DMPO 修改 |
54	|---|---|
55	| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |
56	| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |
57	| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |
58	
59	**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。
60	
61	### 1.3 Per-turn log probability 计算
62	
63	ALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。
64	
65	**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：
66	
67	```
68	token:    [&lt;prompt> | Think... Act... | Think... Act... | Think... Act... ]
69	turn_ids: [   -1    |       0        |        1        |        2        ]
70	```
71	
72	**加权聚合伪代码**：
73	
74	```python
75	def dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):
76	    """
77	    per_token_logps: [batch, seq_len]
78	    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)
79	    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)
80	    gamma:           [batch]           (per-sample γ)
81	    num_turns:       [batch]           (per-sample T)
82	    Returns:         [batch]           (weighted log probability per sample)
83	    """
84	    # 构建 per-token φ 权重
85	    token_weights = torch.zeros_like(per_token_logps)
86	    for t in range(turn_ids.max() + 1):
87	        mask_t = (turn_ids == t)  # [batch, seq_len]
88	        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
89	        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)
90	        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]
91	
92	    return (per_token_logps * completion_mask * token_weights).sum(dim=1)
93	```
94	
95	**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：
96	
97	```python
98	def compute_phi_weights(turn_ids, gamma, num_turns, max_turns):
99	    """全向量化 φ 权重计算"""
100	    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]
101	    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]
102	    T = num_turns.unsqueeze(1).float()                            # [batch, 1]
103	
104	    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)
105	    # phi: [batch, max_turns]
106	
107	    # 用 turn_ids gather 到 per-token 权重
108	    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零
109	    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]
110	    return token_phi
111	```
112	
113	### 1.4 φ(t,T) 权重应用到 per-turn loss
114	
115	在 `_compute_loss` 中，替换聚合步骤：
116	
117	```python
118	# === 原始 trl ===
119	# logps = per_token_logps.sum(dim=1)
120	
121	# === DMPO 修改 ===
122	token_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)
123	logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)
124	
125	chosen_logps, rejected_logps = logps.chunk(2, dim=0)
126	# 后续 log ratio、sigmoid loss 与标准 DPO 相同
127	```
128	
129	---
130	
131	## 2. γ_e 注入方案
132	
133	### 2.1 Error Type → γ_e 映射
134	
135	```yaml
136	# config.yaml
137	gamma_e_mapping:
138	  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步
139	  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列
140	  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹
141	  default: 0.90   # 未分类 fallback
142	```
143	
144	**直觉**：
145	- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）
146	- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）
147	
148	### 2.2 注入流程
149	
150	```
151	数据加载 → 每个样本有 error_type 字段
152	       ↓
153	DataCollator → 查表得到 gamma_per_sample: [batch_size]
154	       ↓
155	_compute_loss → gamma_per_sample 传入 compute_phi_weights()
156	       ↓
157	per-token 权重 → 加权聚合 → 标准 sigmoid loss
158	```
159	
160	**Collator 中的 γ 注入**：
161	
162	```python
163	class DMPODataCollator(DataCollatorForPreference):
164	    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):
165	        super().__init__(**kwargs)
166	        self.gamma_map = gamma_map
167	        self.mode = mode
168	        self.global_gamma = global_gamma
169	
170	    def __call__(self, features):
171	        batch = super().__call__(features)
172	
173	        # 收集 error_type → gamma
174	        gammas = []
175	        for f in features:
176	            if self.mode == "etadn":
177	                et = f.get("error_type", "default")
178	                gammas.append(self.gamma_map.get(et, self.gamma_map["default"]))
179	            elif self.mode == "dmpo":
180	                gammas.append(self.global_gamma)
181	            else:  # dpo
182	                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权
183	
184	        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）
185	        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)
186	        gamma_rejected = gamma_chosen.clone()
187	        batch["gamma"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)
188	
189	        return batch
190	```
191	
192	### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e
193	
194	| 维度 | DMPO | ETADN |
195	|---|---|---|
196	| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |
197	| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |
198	| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |
199	| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |
200	
201	---
202	
203	## 3. 数据 Pipeline
204	
205	### 3.1 DPO 数据格式
206	
207	每个样本包含：
208	
209	```json
210	{
211	  "id": "alfworld_task_42_pair_0",
212	  "error_type": "action",
213	  "prompt": "You are in a kitchen. Your task is to ...",
214	  "chosen": [
215	    {"role": "assistant", "content": "Think: I need to find a tomato. Act: go to fridge 1"},
216	    {"role": "user", "content": "Obs: The fridge is closed."},
217	    {"role": "assistant", "content": "Think: I should open it. Act: open fridge 1"},
218	    {"role": "user", "content": "Obs: You open the fridge. You see a tomato 1."},
219	    {"role": "assistant", "content": "Think: Found it. Act: take tomato 1 from fridge 1"},
220	    {"role": "user", "content": "Obs: You pick up the tomato 1."}
221	  ],
222	  "rejected": [
223	    {"role": "assistant", "content": "Think: I need to find a tomato. Act: go to countertop 1"},
224	    {"role": "user", "content": "Obs: On the countertop you see a bread 1."},
225	    {"role": "assistant", "content": "Think: Not here. Act: go to countertop 2"},
226	    {"role": "user", "content": "Obs: On the countertop you see a cup 1."},
227	    {"role": "assistant", "content": "Think: Maybe in the cabinet. Act: go to cabinet 1"},
228	    {"role": "user", "content": "Obs: The cabinet is closed."}
229	  ],
230	  "chosen_turns": 3,
231	  "rejected_turns": 3
232	}
233	```
234	
235	### 3.2 多轮对话处理：Turn 定义
236	
237	ALFWorld 轨迹中每个 turn 的结构：
238	
239	```
240	Turn t:
241	  Assistant: "Think: &lt;reasoning>. Act: &lt;action>"    ← agent 生成
242	  User:      "Obs: &lt;environment_observation>"        ← 环境返回
243	```
244	
245	**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。
246	
247	Turn 数 T = assistant 回复的数量。
248	
249	### 3.3 Tokenization 与 Turn 标记
250	
251	```python
252	def tokenize_multiturn(example, tokenizer, max_length):
253	    """将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids"""
254	    # 1. 构建完整对话（chat template）
255	    messages = [{"role": "system", "content": example["prompt"]}]
256	    messages += example["chosen"]  # 或 rejected
257	
258	    # 2. 分步 tokenize 以获取 turn 边界
259	    prompt_ids = tokenizer.apply_chat_template(
260	        [messages[0]], tokenize=True, add_generation_prompt=True
261	    )
262	
263	    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1
264	    completion_mask = [0] * len(prompt_ids)
265	    all_ids = list(prompt_ids)
266	    current_turn = 0
267	
268	    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs
269	        # assistant 部分
270	        asst_msg = messages[i]
271	        asst_ids = tokenizer.encode(asst_msg["content"], add_special_tokens=False)
272	        # + chat template 的 role tokens
273	        role_ids = tokenizer.encode("<|im_start|>assistant\n", add_special_tokens=False)
274	        end_ids = tokenizer.encode("<|im_end|>\n", add_special_tokens=False)
275	
276	        all_ids += role_ids
277	        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss
278	        completion_mask += [0] * len(role_ids)
279	
280	        all_ids += asst_ids
281	        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t
282	        completion_mask += [1] * len(asst_ids)
283	
284	        all_ids += end_ids
285	        turn_ids += [current_turn] * len(end_ids)
286	        completion_mask += [1] * len(end_ids)
287	
288	        # user/observation 部分
289	        if i + 1 < len(messages):
290	            user_msg = messages[i + 1]
291	            user_ids = tokenizer.encode(
292	                f"<|im_start|>user\n{user_msg['content']}<|im_end|>\n",
293	                add_special_tokens=False
294	            )
295	            all_ids += user_ids
296	            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss
297	            completion_mask += [0] * len(user_ids)
298	
299	        current_turn += 1
300	
301	    # 3. 截断
302	    all_ids = all_ids[:max_length]
303	    turn_ids = turn_ids[:max_length]
304	    completion_mask = completion_mask[:max_length]
305	
306	    return {
307	        "input_ids": all_ids,
308	        "turn_ids": turn_ids,
309	        "completion_mask": completion_mask,
310	        "num_turns": current_turn,
311	    }
312	```
313	
314	**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。
315	
316	### 3.4 数据集统计预估
317	
318	| 维度 | 估计值 |
319	|---|---|
320	| ALFWorld 任务数 | ~3,500 (train split) |
321	| 每任务轨迹数 | 5-10（采样多条） |
322	| 有效 preference pairs | ~2,000-5,000（过滤后） |
323	| 平均 turn 数 T | 5-15 |
324	| 平均序列长度 | 1,500-3,000 tokens |
325	
326	---
327	
328	## 4. 模型配置
329	
330	### 4.1 Qwen3-8B QLoRA 配置
331	
332	```python
333	from transformers import AutoModelForCausalLM, BitsAndBytesConfig
334	from peft import LoraConfig
335	
336	bnb_config = BitsAndBytesConfig(
337	    load_in_4bit=True,
338	    bnb_4bit_quant_type="nf4",
339	    bnb_4bit_compute_dtype=torch.bfloat16,
340	    bnb_4bit_use_double_quant=True,
341	)
342	
343	model = AutoModelForCausalLM.from_pretrained(
344	    "Qwen/Qwen3-8B",
345	    quantization_config=bnb_config,
346	    torch_dtype=torch.bfloat16,
347	    attn_implementation="flash_attention_2",
348	    device_map={"": device_id},  # 单卡绑定
349	)
350	
351	lora_config = LoraConfig(
352	    r=64,
353	    lora_alpha=128,
354	    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
355	                     "gate_proj", "up_proj", "down_proj"],
356	    lora_dropout=0.05,
357	    task_type="CAUSAL_LM",
358	    bias="none",
359	)
360	```
361	
362	### 4.2 Ref Model 处理
363	
364	QLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。
365	
366	trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：
367	1. 创建 "ref" adapter 副本（复制 default adapter 权重）
368	2. 前向传播时通过 `use_adapter(model, "ref")` 切换到冻结的初始权重
369	3. 或者直接 `model.disable_adapter()` → base model = ref model
370	
371	**推荐方式**：`precompute_ref_log_probs=True`。训练前一次性计算所有样本的 ref logps 并缓存为 `.npz`，训练时从 dataset 直接读取。优势：
372	- 训练时无需 ref model 前向传播，节省 ~30% VRAM
373	- 训练速度提升 ~40%
374	
375	### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）
376	
377	| 组件 | 估计 VRAM |
378	|---|---|
379	| Qwen3-8B 4-bit weights | ~4.5 GB |
380	| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |
381	| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |
382	| Gradients (bf16) | ~0.4 GB |
383	| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |
384	| PyTorch + CUDA overhead | ~2 GB |
385	| **总计** | **~15-17 GB** |
386	
387	剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。
388	
389	**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。
390	
391	### 4.4 训练超参
392	
393	```yaml
394	# config.yaml
395	training:
396	  mode: "etadn"            # "dpo" | "dmpo" | "etadn"
397	  beta: 0.1                # DPO β
398	  global_gamma: 0.90       # DMPO 模式下的全局 γ
399	  learning_rate: 1.0e-6
400	  lr_scheduler_type: "constant_with_warmup"
401	  warmup_ratio: 0.1
402	  num_train_epochs: 3
403	  per_device_train_batch_size: 1
404	  gradient_accumulation_steps: 16
405	  gradient_checkpointing: true
406	  bf16: true
407	  max_length: 3072
408	  max_prompt_length: 512
409	  logging_steps: 5
410	  save_steps: 100
411	  eval_steps: 50
412	  precompute_ref_log_probs: true
413	  label_smoothing: 0.0
414	  loss_type: "sigmoid"
415	
416	lora:
417	  r: 64
418	  lora_alpha: 128
419	  target_modules: ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
420	  lora_dropout: 0.05
421	
422	gamma_e_mapping:
423	  action: 0.85
424	  verify: 0.92
425	  plan: 0.97
426	  default: 0.90
427	```
428	
429	---
430	
431	## 5. 推理 Pipeline
432	
433	### 5.1 轨迹收集
434	
435	```python
436	# collect_trajectories.py
437	# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互
438	# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）
439	
440	from vllm import LLM, SamplingParams  # 或 transformers.generate
441	
442	model = LLM(
443	    model="path/to/qwen3-8b-merged",  # LoRA merge 后的 checkpoint
444	    tensor_parallel_size=1,
445	    gpu_memory_utilization=0.85,
446	    max_model_len=4096,
447	)
448	
449	params = SamplingParams(
450	    temperature=0.7,
451	    top_p=0.9,
452	    max_tokens=256,      # 每步生成上限
453	    stop=["Obs:"],       # ALFWorld 环境会返回 Obs
454	)
455	
456	# 循环：generate → parse action → env.step → append obs → repeat
457	```
458	
459	**输出格式**：
460	
461	```json
462	{
463	  "task_id": "pick_clean_then_place-Tomato-...",
464	  "trajectory": [
465	    {"role": "assistant", "content": "Think: ... Act: go to fridge 1"},
466	    {"role": "user", "content": "Obs: The fridge is closed."},
467	    ...
468	  ],
469	  "reward": 1,           # ALFWorld: 1=成功, 0=失败
470	  "num_steps": 8,
471	  "task_type": "pick_clean_then_place"
472	}
473	```
474	
475	### 5.2 错误分类
476	
477	```python
478	# classify_errors.py
479	# 用 Qwen3-14B-AWQ 做 zero-shot 分类
480	
481	CLASSIFY_PROMPT = """Analyze the following failed trajectory in ALFWorld.
482	The agent attempted a task but failed. Identify the PRIMARY error type:
483	
484	- action: Wrong physical action (e.g., went to wrong location, used wrong object)
485	- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)
486	- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)
487	
488	Task: {task_description}
489	Successful trajectory: {chosen_trajectory}
490	Failed trajectory: {rejected_trajectory}
491	
492	Respond with ONLY one word: action, verify, or plan"""
493	
494	# 输出: error_type ∈ {"action", "verify", "plan"}
495	```
496	
497	### 5.3 Preference Pair 构建
498	
499	```python
500	# construct_preference.py
501	
502	def construct_pairs(trajectories, error_classifications):
503	    """
504	    策略：
505	    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected
506	    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs
507	    3. 附加 error_type 标签（来自 classify_errors.py 的输出）
508	    """
509	    pairs = []
510	    for task_id, task_trajs in group_by_task(trajectories):
511	        chosen_trajs = [t for t in task_trajs if t["reward"] == 1]
512	        rejected_trajs = [t for t in task_trajs if t["reward"] == 0]
513	
514	        if not chosen_trajs or not rejected_trajs:
515	            continue
516	
517	        best_chosen = min(chosen_trajs, key=lambda t: t["num_steps"])
518	
519	        for rej in rejected_trajs:
520	            error_type = error_classifications.get(
521	                f"{task_id}_{rej['traj_id']}", "default"
522	            )
523	            pairs.append({
524	                "id": f"{task_id}_pair_{len(pairs)}",
525	                "error_type": error_type,
526	                "prompt": task_description(task_id),
527	                "chosen": best_chosen["trajectory"],
528	                "rejected": rej["trajectory"],
529	                "chosen_turns": count_assistant_turns(best_chosen["trajectory"]),
530	                "rejected_turns": count_assistant_turns(rej["trajectory"]),
531	            })
532	
533	    return pairs
534	```
535	
536	---
537	
538	## 6. 完整文件结构
539	
540	```
541	rl-active-probe-fl/
542	├── train_etadn.py              # 主训练入口
543	│   - 解析 config.yaml
544	│   - 加载模型 + LoRA + BnB 量化
545	│   - 构建 dataset + collator
546	│   - 初始化 ETADNTrainer
547	│   - trainer.train()
548	│
549	├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）
550	│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted
551	│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns
552	│   - DMPODataCollator: 注入 gamma、pad turn_ids
553	│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)
554	│
555	├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合
556	│   - compute_phi(t, T, gamma): 单值 φ 计算
557	│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重
558	│   - dmpo_weighted_logps(): per_token_logps → weighted scalar
559	│
560	├── data_utils.py               # 数据加载与预处理
561	│   - load_preference_data(path): 加载 JSON pairs
562	│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization
563	│   - build_dataset(): HF Dataset 构建
564	│
565	├── config.yaml                 # 超参配置（见 §4.4）
566	│
567	├── collect_trajectories.py     # 轨迹收集（§5.1）
568	│   - ALFWorld 环境交互
569	│   - vLLM / transformers 推理
570	│   - 输出 trajectories.jsonl
571	│
572	├── classify_errors.py          # 错误分类（§5.2）
573	│   - Qwen3-14B-AWQ zero-shot
574	│   - 输出 error_classifications.json
575	│
576	├── construct_preference.py     # Preference pair 构建（§5.3）
577	│   - 输入: trajectories + error_classifications
578	│   - 输出: preference_pairs.json
579	│
580	├── evaluate.py                 # ALFWorld 评估
581	│   - 标准 eval protocol: 134 unseen tasks
582	│   - 指标: success rate, average steps
583	│   - 按 task type 分组报告
584	│
585	├── scripts/
586	│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)
587	│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)
588	│
589	└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）
590	    ├── env_wrapper.py
591	    └── task_configs/
592	```
593	
594	### 6.1 关键模块依赖关系
595	
596	```
597	config.yaml
598	    ↓
599	train_etadn.py
600	    ├── data_utils.py → tokenize_multiturn()
601	    ├── dmpo_trainer.py → ETADNTrainer
602	    │       ├── dmpo_loss.py → compute_phi_weights()
603	    │       └── DMPODataCollator → gamma injection
604	    └── evaluate.py (训练结束后调用)
605	
606	collect_trajectories.py → trajectories.jsonl
607	    ↓
608	classify_errors.py → error_classifications.json
609	    ↓
610	construct_preference.py → preference_pairs.json
611	    ↓
612	train_etadn.py (读取 preference_pairs.json)
613	```
614	
615	---
616	
617	## 7. Ablation 设计
618	
619	### 7.1 三种模式切换
620	
621	通过 `config.yaml` 中 `training.mode` 字段切换：
622	
623	| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |
624	|---|---|---|---|
625	| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |
626	| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |
627	| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |
628	
629	### 7.2 代码中的模式分支
630	
631	在 `ETADNTrainer._compute_loss` 中：
632	
633	```python
634	if self.mode == "dpo":
635	    # 标准 DPO: 直接 sum
636	    logps = (per_token_logps * shift_completion_mask).sum(dim=1)
637	else:
638	    # dmpo 或 etadn: φ-weighted sum
639	    # gamma 已由 collator 注入到 batch["gamma"]
640	    token_phi = compute_phi_weights(
641	        turn_ids=batch["turn_ids"][:, 1:],  # shift 对齐
642	        gamma=batch["gamma"],
643	        num_turns=batch["num_turns"],
644	        max_turns=batch["turn_ids"].max().item() + 1,
645	    )
646	    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)
647	```
648	
649	### 7.3 实验矩阵
650	
651	| Run | Mode | γ / γ_e | GPU | Seed | 目的 |
652	|---|---|---|---|---|---|
653	| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |
654	| A2 | dpo | — | 1 | 42 | Baseline 复现 |
655	| B1 | dmpo | 0.90 | 0 | 42 | Baseline: DMPO 全局 γ |
656	| B2 | dmpo | 0.85 | 1 | 42 | DMPO γ 敏感性 |
657	| C1 | etadn | per-sample | 0 | 42 | **Ours**: ETADN |
658	| C2 | etadn | per-sample | 1 | 123 | Ours 不同 seed |
659	
660	**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run。6 个 run 分 3 轮完成。
661	
662	### 7.4 评估指标
663	
664	| 指标 | 说明 |
665	|---|---|
666	| ALFWorld success rate (overall) | 主指标，134 unseen tasks |
667	| Success rate per task type | 6 种 task type 的分项成功率 |
668	| Average steps to success | 效率指标 |
669	| Error type distribution shift | 训练前后的错误类型分布变化 |
670	| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |
671	| Training loss curve | 收敛性对比 |
672	
673	---
674	
675	## 8. ETADNTrainer 核心代码骨架
676	
677	```python
678	# dmpo_trainer.py
679	
680	from trl import DPOTrainer, DPOConfig
681	from dmpo_loss import compute_phi_weights
682	
683	class ETADNConfig(DPOConfig):
684	    mode: str = "etadn"          # "dpo" | "dmpo" | "etadn"
685	    global_gamma: float = 0.90
686	    gamma_e_mapping: dict = None  # {"action": 0.85, "verify": 0.92, "plan": 0.97}
687	
688	
689	class ETADNTrainer(DPOTrainer):
690	
691	    def __init__(self, *args, mode="etadn", global_gamma=0.9, gamma_e_mapping=None, **kwargs):
692	        super().__init__(*args, **kwargs)
693	        self.mode = mode
694	        self.global_gamma = global_gamma
695	        self.gamma_e_mapping = gamma_e_mapping or {}
696	
697	    def _compute_loss(self, model, inputs, return_outputs=False):
698	        """Override: DMPO φ-weighted log probability aggregation."""
699	        # --- 1. 提取额外字段 ---
700	        turn_ids = inputs.pop("turn_ids", None)
701	        num_turns = inputs.pop("num_turns", None)
702	        gamma = inputs.pop("gamma", None)
703	        completion_mask = inputs["completion_mask"]
704	        input_ids = inputs["input_ids"]
705	
706	        # --- 2. Policy forward ---
707	        model_kwargs = {k: v for k, v in inputs.items()
708	                        if k not in ("completion_mask", "ref_chosen_logps", "ref_rejected_logps")}
709	        outputs = model(**model_kwargs)
710	
711	        # --- 3. Per-token logps ---
712	        from trl.trainer.utils import selective_log_softmax
713	        shift_logits = outputs.logits[..., :-1, :].contiguous()
714	        shift_labels = input_ids[..., 1:].contiguous()
715	        shift_completion_mask = completion_mask[..., 1:].contiguous()
716	        per_token_logps = selective_log_softmax(shift_logits, shift_labels)
717	        per_token_logps[shift_completion_mask == 0] = 0.0
718	
719	        # --- 4. 聚合（核心修改点） ---
720	        if self.mode == "dpo" or turn_ids is None:
721	            logps = per_token_logps.sum(dim=1)
722	        else:
723	            shift_turn_ids = turn_ids[..., 1:].contiguous()
724	            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,
725	                                            max_turns=shift_turn_ids.max().item() + 1)
726	            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)
727	
728	        chosen_logps, rejected_logps = logps.chunk(2, dim=0)
729	
730	        # --- 5. Reference logps ---
731	        if "ref_chosen_logps" in inputs:
732	            ref_chosen_logps = inputs["ref_chosen_logps"]
733	            ref_rejected_logps = inputs["ref_rejected_logps"]
734	        else:
735	            with torch.no_grad():
736	                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(
737	                    model, inputs, shift_completion_mask,
738	                    turn_ids=shift_turn_ids if self.mode != "dpo" else None,
739	                    gamma=gamma, num_turns=num_turns,
740	                )
741	
742	        # --- 6. Loss (sigmoid, same as standard DPO) ---
743	        chosen_logratios = chosen_logps - ref_chosen_logps
744	        rejected_logratios = rejected_logps - ref_rejected_logps
745	        logits = chosen_logratios - rejected_logratios
746	
747	        loss = -F.logsigmoid(self.beta * logits).mean()
748	
749	        # --- 7. Metrics ---
750	        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()
751	        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()
752	        reward_margin = (chosen_rewards - rejected_rewards).mean()
753	
754	        metrics = {
755	            "loss": loss.detach().item(),
756	            "rewards/chosen": chosen_rewards.mean().item(),
757	            "rewards/rejected": rejected_rewards.mean().item(),
758	            "rewards/margin": reward_margin.item(),
759	        }
760	        self.store_metrics(metrics, train_eval="train")
761	
762	        if return_outputs:
763	            return loss, {"logits": logits}
764	        return loss
765	```
766	
767	---
768	
769	## 9. 风险与注意事项
770	
771	| 风险 | 缓解 |
772	|---|---|
773	| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |
774	| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |
775	| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |
776	| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |
777	| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |
778	
779	---
780	
781	## 10. 实施优先级
782	
783	| Phase | 内容 | 估计时间 |
784	|---|---|---|
785	| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |
786	| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |
787	| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |
788	| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |
789	| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |
790	| P6 | 完整训练 + 评估 | 2-3 天 |
791	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "9dacdbe1-af14-46d4-9747-23e5ab31ded7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
      "content": "# DMPO + ETADN 训练 Pipeline 设计（v2）\n\n## 0. 术语与背景\n\n**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。\n\n**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。\n\n**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。\n\n---\n\n## 1. DMPO Loss 实现方案\n\n### 1.1 完整 DMPO Loss 公式\n\n标准 DPO loss（单轮）：\n\n```\nL_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]\n```\n\nDMPO loss（多轮，论文 Eq.16）：\n\n```\nL_DMPO = -E[ log σ(\n    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]\n  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]\n)]\n```\n\n其中时间折扣函数：\n\n```\nφ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n```\n\n- t = turn index (0-indexed)\n- T = 总 turn 数\n- γ ∈ (0, 1) = 时间折扣因子\n- φ(t, T) 单调递减：早期 turn 权重更高\n\n**特殊情况**：\n- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO\n- γ = 1: φ(t,T) = (T-t)/T → 线性衰减\n\n### 1.2 在 trl DPOTrainer 上实现 DMPO\n\n**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。\n\n**需要修改的核心逻辑**（在 `_compute_loss` 内）：\n\n| 原始 trl 行为 | DMPO 修改 |\n|---|---|\n| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |\n| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |\n| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |\n\n**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。\n\n### 1.3 Per-turn log probability 计算\n\nALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。\n\n**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：\n\n```\ntoken:    [&lt;prompt> | Think... Act... | Think... Act... | Think... Act... ]\nturn_ids: [   -1    |       0        |        1        |        2        ]\n```\n\n**加权聚合伪代码**：\n\n```python\ndef dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):\n    \"\"\"\n    per_token_logps: [batch, seq_len]\n    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)\n    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)\n    gamma:           [batch]           (per-sample γ)\n    num_turns:       [batch]           (per-sample T)\n    Returns:         [batch]           (weighted log probability per sample)\n    \"\"\"\n    # 构建 per-token φ 权重\n    token_weights = torch.zeros_like(per_token_logps)\n    for t in range(turn_ids.max() + 1):\n        mask_t = (turn_ids == t)  # [batch, seq_len]\n        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)\n        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]\n\n    return (per_token_logps * completion_mask * token_weights).sum(dim=1)\n```\n\n**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：\n\n```python\ndef compute_phi_weights(turn_ids, gamma, num_turns, max_turns):\n    \"\"\"全向量化 φ 权重计算\"\"\"\n    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]\n    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]\n    T = num_turns.unsqueeze(1).float()                            # [batch, 1]\n\n    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)\n    # phi: [batch, max_turns]\n\n    # 用 turn_ids gather 到 per-token 权重\n    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零\n    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]\n    return token_phi\n```\n\n### 1.4 φ(t,T) 权重应用到 per-turn loss\n\n在 `_compute_loss` 中，替换聚合步骤：\n\n```python\n# === 原始 trl ===\n# logps = per_token_logps.sum(dim=1)\n\n# === DMPO 修改 ===\ntoken_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)\nlogps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\nchosen_logps, rejected_logps = logps.chunk(2, dim=0)\n# 后续 log ratio、sigmoid loss 与标准 DPO 相同\n```\n\n---\n\n## 2. γ_e 注入方案\n\n### 2.1 Error Type → γ_e 映射\n\n```yaml\n# config.yaml\ngamma_e_mapping:\n  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步\n  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列\n  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹\n  default: 0.90   # 未分类 fallback\n```\n\n**直觉**：\n- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）\n- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）\n\n### 2.2 注入流程\n\n```\n数据加载 → 每个样本有 error_type 字段\n       ↓\nDataCollator → 查表得到 gamma_per_sample: [batch_size]\n       ↓\n_compute_loss → gamma_per_sample 传入 compute_phi_weights()\n       ↓\nper-token 权重 → 加权聚合 → 标准 sigmoid loss\n```\n\n**Collator 中的 γ 注入**：\n\n```python\nclass DMPODataCollator(DataCollatorForPreference):\n    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):\n        super().__init__(**kwargs)\n        self.gamma_map = gamma_map\n        self.mode = mode\n        self.global_gamma = global_gamma\n\n    def __call__(self, features):\n        batch = super().__call__(features)\n\n        # 收集 error_type → gamma\n        gammas = []\n        for f in features:\n            if self.mode == \"etadn\":\n                et = f.get(\"error_type\", \"default\")\n                gammas.append(self.gamma_map.get(et, self.gamma_map[\"default\"]))\n            elif self.mode == \"dmpo\":\n                gammas.append(self.global_gamma)\n            else:  # dpo\n                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权\n\n        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）\n        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)\n        gamma_rejected = gamma_chosen.clone()\n        batch[\"gamma\"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)\n\n        return batch\n```\n\n### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e\n\n| 维度 | DMPO | ETADN |\n|---|---|---|\n| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |\n| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |\n| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |\n| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |\n\n---\n\n## 3. 数据 Pipeline\n\n### 3.1 DPO 数据格式\n\n每个样本包含：\n\n```json\n{\n  \"id\": \"alfworld_task_42_pair_0\",\n  \"error_type\": \"action\",\n  \"prompt\": \"You are in a kitchen. Your task is to ...\",\n  \"chosen\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: I should open it. Act: open fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You open the fridge. You see a tomato 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Found it. Act: take tomato 1 from fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You pick up the tomato 1.\"}\n  ],\n  \"rejected\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to countertop 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a bread 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Not here. Act: go to countertop 2\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a cup 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Maybe in the cabinet. Act: go to cabinet 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The cabinet is closed.\"}\n  ],\n  \"chosen_turns\": 3,\n  \"rejected_turns\": 3\n}\n```\n\n### 3.2 多轮对话处理：Turn 定义\n\nALFWorld 轨迹中每个 turn 的结构：\n\n```\nTurn t:\n  Assistant: \"Think: &lt;reasoning>. Act: &lt;action>\"    ← agent 生成\n  User:      \"Obs: &lt;environment_observation>\"        ← 环境返回\n```\n\n**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。\n\nTurn 数 T = assistant 回复的数量。\n\n### 3.3 Tokenization 与 Turn 标记\n\n```python\ndef tokenize_multiturn(example, tokenizer, max_length):\n    \"\"\"将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids\"\"\"\n    # 1. 构建完整对话（chat template）\n    messages = [{\"role\": \"system\", \"content\": example[\"prompt\"]}]\n    messages += example[\"chosen\"]  # 或 rejected\n\n    # 2. 分步 tokenize 以获取 turn 边界\n    prompt_ids = tokenizer.apply_chat_template(\n        [messages[0]], tokenize=True, add_generation_prompt=True\n    )\n\n    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1\n    completion_mask = [0] * len(prompt_ids)\n    all_ids = list(prompt_ids)\n    current_turn = 0\n\n    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs\n        # assistant 部分\n        asst_msg = messages[i]\n        asst_ids = tokenizer.encode(asst_msg[\"content\"], add_special_tokens=False)\n        # + chat template 的 role tokens\n        role_ids = tokenizer.encode(\"<|im_start|>assistant\\n\", add_special_tokens=False)\n        end_ids = tokenizer.encode(\"<|im_end|>\\n\", add_special_tokens=False)\n\n        all_ids += role_ids\n        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss\n        completion_mask += [0] * len(role_ids)\n\n        all_ids += asst_ids\n        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t\n        completion_mask += [1] * len(asst_ids)\n\n        all_ids += end_ids\n        turn_ids += [current_turn] * len(end_ids)\n        completion_mask += [1] * len(end_ids)\n\n        # user/observation 部分\n        if i + 1 < len(messages):\n            user_msg = messages[i + 1]\n            user_ids = tokenizer.encode(\n                f\"<|im_start|>user\\n{user_msg['content']}<|im_end|>\\n\",\n                add_special_tokens=False\n            )\n            all_ids += user_ids\n            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss\n            completion_mask += [0] * len(user_ids)\n\n        current_turn += 1\n\n    # 3. 截断\n    all_ids = all_ids[:max_length]\n    turn_ids = turn_ids[:max_length]\n    completion_mask = completion_mask[:max_length]\n\n    return {\n        \"input_ids\": all_ids,\n        \"turn_ids\": turn_ids,\n        \"completion_mask\": completion_mask,\n        \"num_turns\": current_turn,\n    }\n```\n\n**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。\n\n### 3.4 数据集统计预估\n\n| 维度 | 估计值 |\n|---|---|\n| ALFWorld 任务数 | ~3,500 (train split) |\n| 每任务轨迹数 | 5-10（采样多条） |\n| 有效 preference pairs | ~2,000-5,000（过滤后） |\n| 平均 turn 数 T | 5-15 |\n| 平均序列长度 | 1,500-3,000 tokens |\n\n---\n\n## 4. 模型配置\n\n### 4.1 Qwen3-8B QLoRA 配置\n\n```python\nfrom transformers import AutoModelForCausalLM, BitsAndBytesConfig\nfrom peft import LoraConfig\n\nbnb_config = BitsAndBytesConfig(\n    load_in_4bit=True,\n    bnb_4bit_quant_type=\"nf4\",\n    bnb_4bit_compute_dtype=torch.bfloat16,\n    bnb_4bit_use_double_quant=True,\n)\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    \"Qwen/Qwen3-8B\",\n    quantization_config=bnb_config,\n    torch_dtype=torch.bfloat16,\n    attn_implementation=\"flash_attention_2\",\n    device_map={\"\": device_id},  # 单卡绑定\n)\n\nlora_config = LoraConfig(\n    r=64,\n    lora_alpha=128,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                     \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_dropout=0.05,\n    task_type=\"CAUSAL_LM\",\n    bias=\"none\",\n)\n```\n\n### 4.2 Ref Model 处理\n\nQLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。\n\ntrl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`。训练前一次性计算所有样本的 ref logps 并缓存为 `.npz`，训练时从 dataset 直接读取。优势：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n\n### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）\n\n| 组件 | 估计 VRAM |\n|---|---|\n| Qwen3-8B 4-bit weights | ~4.5 GB |\n| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |\n| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |\n| Gradients (bf16) | ~0.4 GB |\n| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |\n| PyTorch + CUDA overhead | ~2 GB |\n| **总计** | **~15-17 GB** |\n\n剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。\n\n**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。\n\n### 4.4 训练超参\n\n```yaml\n# config.yaml\ntraining:\n  mode: \"etadn\"            # \"dpo\" | \"dmpo\" | \"etadn\"\n  beta: 0.1                # DPO β\n  global_gamma: 0.90       # DMPO 模式下的全局 γ\n  learning_rate: 1.0e-6\n  lr_scheduler_type: \"constant_with_warmup\"\n  warmup_ratio: 0.1\n  num_train_epochs: 3\n  per_device_train_batch_size: 1\n  gradient_accumulation_steps: 16\n  gradient_checkpointing: true\n  bf16: true\n  max_length: 3072\n  max_prompt_length: 512\n  logging_steps: 5\n  save_steps: 100\n  eval_steps: 50\n  precompute_ref_log_probs: true\n  label_smoothing: 0.0\n  loss_type: \"sigmoid\"\n\nlora:\n  r: 64\n  lora_alpha: 128\n  target_modules: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n  lora_dropout: 0.05\n\ngamma_e_mapping:\n  action: 0.85\n  verify: 0.92\n  plan: 0.97\n  default: 0.90\n```\n\n---\n\n## 5. 推理 Pipeline\n\n### 5.1 轨迹收集\n\n```python\n# collect_trajectories.py\n# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互\n# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）\n\nfrom vllm import LLM, SamplingParams  # 或 transformers.generate\n\nmodel = LLM(\n    model=\"path/to/qwen3-8b-merged\",  # LoRA merge 后的 checkpoint\n    tensor_parallel_size=1,\n    gpu_memory_utilization=0.85,\n    max_model_len=4096,\n)\n\nparams = SamplingParams(\n    temperature=0.7,\n    top_p=0.9,\n    max_tokens=256,      # 每步生成上限\n    stop=[\"Obs:\"],       # ALFWorld 环境会返回 Obs\n)\n\n# 循环：generate → parse action → env.step → append obs → repeat\n```\n\n**输出格式**：\n\n```json\n{\n  \"task_id\": \"pick_clean_then_place-Tomato-...\",\n  \"trajectory\": [\n    {\"role\": \"assistant\", \"content\": \"Think: ... Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    ...\n  ],\n  \"reward\": 1,           # ALFWorld: 1=成功, 0=失败\n  \"num_steps\": 8,\n  \"task_type\": \"pick_clean_then_place\"\n}\n```\n\n### 5.2 错误分类\n\n```python\n# classify_errors.py\n# 用 Qwen3-14B-AWQ 做 zero-shot 分类\n\nCLASSIFY_PROMPT = \"\"\"Analyze the following failed trajectory in ALFWorld.\nThe agent attempted a task but failed. Identify the PRIMARY error type:\n\n- action: Wrong physical action (e.g., went to wrong location, used wrong object)\n- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)\n- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)\n\nTask: {task_description}\nSuccessful trajectory: {chosen_trajectory}\nFailed trajectory: {rejected_trajectory}\n\nRespond with ONLY one word: action, verify, or plan\"\"\"\n\n# 输出: error_type ∈ {\"action\", \"verify\", \"plan\"}\n```\n\n### 5.3 Preference Pair 构建\n\n```python\n# construct_preference.py\n\ndef construct_pairs(trajectories, error_classifications):\n    \"\"\"\n    策略：\n    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected\n    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs\n    3. 附加 error_type 标签（来自 classify_errors.py 的输出）\n    \"\"\"\n    pairs = []\n    for task_id, task_trajs in group_by_task(trajectories):\n        chosen_trajs = [t for t in task_trajs if t[\"reward\"] == 1]\n        rejected_trajs = [t for t in task_trajs if t[\"reward\"] == 0]\n\n        if not chosen_trajs or not rejected_trajs:\n            continue\n\n        best_chosen = min(chosen_trajs, key=lambda t: t[\"num_steps\"])\n\n        for rej in rejected_trajs:\n            error_type = error_classifications.get(\n                f\"{task_id}_{rej['traj_id']}\", \"default\"\n            )\n            pairs.append({\n                \"id\": f\"{task_id}_pair_{len(pairs)}\",\n                \"error_type\": error_type,\n                \"prompt\": task_description(task_id),\n                \"chosen\": best_chosen[\"trajectory\"],\n                \"rejected\": rej[\"trajectory\"],\n                \"chosen_turns\": count_assistant_turns(best_chosen[\"trajectory\"]),\n                \"rejected_turns\": count_assistant_turns(rej[\"trajectory\"]),\n            })\n\n    return pairs\n```\n\n---\n\n## 6. 完整文件结构\n\n```\nrl-active-probe-fl/\n├── train_etadn.py              # 主训练入口\n│   - 解析 config.yaml\n│   - 加载模型 + LoRA + BnB 量化\n│   - 构建 dataset + collator\n│   - 初始化 ETADNTrainer\n│   - trainer.train()\n│\n├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）\n│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted\n│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns\n│   - DMPODataCollator: 注入 gamma、pad turn_ids\n│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)\n│\n├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合\n│   - compute_phi(t, T, gamma): 单值 φ 计算\n│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重\n│   - dmpo_weighted_logps(): per_token_logps → weighted scalar\n│\n├── data_utils.py               # 数据加载与预处理\n│   - load_preference_data(path): 加载 JSON pairs\n│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization\n│   - build_dataset(): HF Dataset 构建\n│\n├── config.yaml                 # 超参配置（见 §4.4）\n│\n├── collect_trajectories.py     # 轨迹收集（§5.1）\n│   - ALFWorld 环境交互\n│   - vLLM / transformers 推理\n│   - 输出 trajectories.jsonl\n│\n├── classify_errors.py          # 错误分类（§5.2）\n│   - Qwen3-14B-AWQ zero-shot\n│   - 输出 error_classifications.json\n│\n├── construct_preference.py     # Preference pair 构建（§5.3）\n│   - 输入: trajectories + error_classifications\n│   - 输出: preference_pairs.json\n│\n├── evaluate.py                 # ALFWorld 评估\n│   - 标准 eval protocol: 134 unseen tasks\n│   - 指标: success rate, average steps\n│   - 按 task type 分组报告\n│\n├── scripts/\n│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)\n│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)\n│\n└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）\n    ├── env_wrapper.py\n    └── task_configs/\n```\n\n### 6.1 关键模块依赖关系\n\n```\nconfig.yaml\n    ↓\ntrain_etadn.py\n    ├── data_utils.py → tokenize_multiturn()\n    ├── dmpo_trainer.py → ETADNTrainer\n    │       ├── dmpo_loss.py → compute_phi_weights()\n    │       └── DMPODataCollator → gamma injection\n    └── evaluate.py (训练结束后调用)\n\ncollect_trajectories.py → trajectories.jsonl\n    ↓\nclassify_errors.py → error_classifications.json\n    ↓\nconstruct_preference.py → preference_pairs.json\n    ↓\ntrain_etadn.py (读取 preference_pairs.json)\n```\n\n---\n\n## 7. Ablation 设计\n\n### 7.1 三种模式切换\n\n通过 `config.yaml` 中 `training.mode` 字段切换：\n\n| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |\n|---|---|---|---|\n| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |\n| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |\n| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |\n\n### 7.2 代码中的模式分支\n\n在 `ETADNTrainer._compute_loss` 中：\n\n```python\nif self.mode == \"dpo\":\n    # 标准 DPO: 直接 sum\n    logps = (per_token_logps * shift_completion_mask).sum(dim=1)\nelse:\n    # dmpo 或 etadn: φ-weighted sum\n    # gamma 已由 collator 注入到 batch[\"gamma\"]\n    token_phi = compute_phi_weights(\n        turn_ids=batch[\"turn_ids\"][:, 1:],  # shift 对齐\n        gamma=batch[\"gamma\"],\n        num_turns=batch[\"num_turns\"],\n        max_turns=batch[\"turn_ids\"].max().item() + 1,\n    )\n    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n```\n\n### 7.3 实验矩阵\n\n| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| A2 | dpo | — | 1 | 42 | Baseline 复现 |\n| B1 | dmpo | 0.90 | 0 | 42 | Baseline: DMPO 全局 γ |\n| B2 | dmpo | 0.85 | 1 | 42 | DMPO γ 敏感性 |\n| C1 | etadn | per-sample | 0 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 1 | 123 | Ours 不同 seed |\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run。6 个 run 分 3 轮完成。\n\n### 7.4 评估指标\n\n| 指标 | 说明 |\n|---|---|\n| ALFWorld success rate (overall) | 主指标，134 unseen tasks |\n| Success rate per task type | 6 种 task type 的分项成功率 |\n| Average steps to success | 效率指标 |\n| Error type distribution shift | 训练前后的错误类型分布变化 |\n| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |\n| Training loss curve | 收敛性对比 |\n\n---\n\n## 8. ETADNTrainer 核心代码骨架\n\n```python\n# dmpo_trainer.py\n\nfrom trl import DPOTrainer, DPOConfig\nfrom dmpo_loss import compute_phi_weights\n\nclass ETADNConfig(DPOConfig):\n    mode: str = \"etadn\"          # \"dpo\" | \"dmpo\" | \"etadn\"\n    global_gamma: float = 0.90\n    gamma_e_mapping: dict = None  # {\"action\": 0.85, \"verify\": 0.92, \"plan\": 0.97}\n\n\nclass ETADNTrainer(DPOTrainer):\n\n    def __init__(self, *args, mode=\"etadn\", global_gamma=0.9, gamma_e_mapping=None, **kwargs):\n        super().__init__(*args, **kwargs)\n        self.mode = mode\n        self.global_gamma = global_gamma\n        self.gamma_e_mapping = gamma_e_mapping or {}\n\n    def _compute_loss(self, model, inputs, return_outputs=False):\n        \"\"\"Override: DMPO φ-weighted log probability aggregation.\"\"\"\n        # --- 1. 提取额外字段 ---\n        turn_ids = inputs.pop(\"turn_ids\", None)\n        num_turns = inputs.pop(\"num_turns\", None)\n        gamma = inputs.pop(\"gamma\", None)\n        completion_mask = inputs[\"completion_mask\"]\n        input_ids = inputs[\"input_ids\"]\n\n        # --- 2. Policy forward ---\n        model_kwargs = {k: v for k, v in inputs.items()\n                        if k not in (\"completion_mask\", \"ref_chosen_logps\", \"ref_rejected_logps\")}\n        outputs = model(**model_kwargs)\n\n        # --- 3. Per-token logps ---\n        from trl.trainer.utils import selective_log_softmax\n        shift_logits = outputs.logits[..., :-1, :].contiguous()\n        shift_labels = input_ids[..., 1:].contiguous()\n        shift_completion_mask = completion_mask[..., 1:].contiguous()\n        per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n        per_token_logps[shift_completion_mask == 0] = 0.0\n\n        # --- 4. 聚合（核心修改点） ---\n        if self.mode == \"dpo\" or turn_ids is None:\n            logps = per_token_logps.sum(dim=1)\n        else:\n            shift_turn_ids = turn_ids[..., 1:].contiguous()\n            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,\n                                            max_turns=shift_turn_ids.max().item() + 1)\n            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\n        chosen_logps, rejected_logps = logps.chunk(2, dim=0)\n\n        # --- 5. Reference logps ---\n        if \"ref_chosen_logps\" in inputs:\n            ref_chosen_logps = inputs[\"ref_chosen_logps\"]\n            ref_rejected_logps = inputs[\"ref_rejected_logps\"]\n        else:\n            with torch.no_grad():\n                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(\n                    model, inputs, shift_completion_mask,\n                    turn_ids=shift_turn_ids if self.mode != \"dpo\" else None,\n                    gamma=gamma, num_turns=num_turns,\n                )\n\n        # --- 6. Loss (sigmoid, same as standard DPO) ---\n        chosen_logratios = chosen_logps - ref_chosen_logps\n        rejected_logratios = rejected_logps - ref_rejected_logps\n        logits = chosen_logratios - rejected_logratios\n\n        loss = -F.logsigmoid(self.beta * logits).mean()\n\n        # --- 7. Metrics ---\n        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()\n        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()\n        reward_margin = (chosen_rewards - rejected_rewards).mean()\n\n        metrics = {\n            \"loss\": loss.detach().item(),\n            \"rewards/chosen\": chosen_rewards.mean().item(),\n            \"rewards/rejected\": rejected_rewards.mean().item(),\n            \"rewards/margin\": reward_margin.item(),\n        }\n        self.store_metrics(metrics, train_eval=\"train\")\n\n        if return_outputs:\n            return loss, {\"logits\": logits}\n        return loss\n```\n\n---\n\n## 9. 风险与注意事项\n\n| 风险 | 缓解 |\n|---|---|\n| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |\n| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |\n| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |\n| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |\n| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |\n\n---\n\n## 10. 实施优先级\n\n| Phase | 内容 | 估计时间 |\n|---|---|---|\n| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |\n| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |\n| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |\n| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |\n| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |\n| P6 | 完整训练 + 评估 | 2-3 天 |\n",
      "numLines": 791,
      "startLine": 1,
      "totalLines": 791
    }
  }
}
````

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file content. Let me plan the edits:

1. **修 1**: precompute_ref_log_probs 与 φ-weighted 聚合兼容性
   - Section 4.2 (Ref Model 处理) mentions precompute_ref_log_probs
   - Section 9 (风险与注意事项) also mentions this
   - Need to update Section 4.2 to clarify the precompute must use φ-weighted aggregation and add pseudocode

2. **修 2**: 实验矩阵 seed 数
   - Section 7.3 has the experiment matrix - need to update it

3. **修 3**: trl 版本
   - Need to find dependency/version mentions and update
   - Section 1.2 mentions trl v1.4.0
   - Section 9 mentions trl version locking

4. **额外**: φ(t,T) 归一化验证 - add new subsection

Now I'm working through the specific edits. In Section 4.2, I need to clarify that precompute_ref_log_probs must use φ-weighted aggregation and add the corresponding pseudocode to make this requirement explicit.

For Section 7.3, I'll replace the experiment matrix with updated values. Then I need to consolidate the trl version references scattered throughout the document - there's mention at line 49 and line 774 - so I should create a dedicated environment dependencies section. Finally, I'll add a new subsection to verify φ normalization.

Now looking at the DPOTrainer section: when a PeftModel is detected without an explicit ref_model, trl creates a "ref" adapter by copying the default adapter weights, then switches between them during forward passes using adapter management. The recommended approach is precomputing all reference log probabilities before training with `precompute_ref_log_probs=True`, caching them as `.npz` files so the dataset can load them directly during training rather than computing them on the fly. Now I'm working through the specific edits needed for the document. I need to revise section 4.2 to clarify how the φ-weighted precompute mechanism works, update the risk assessment table in section 9 to reflect the fix that was already mentioned in the first entry, and then implement all these changes systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "2ec04a7a-dfa7-49e3-976d-6e03cd309c90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJynHHJRuVjY8rjtmF8Nkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12731,
      "cache_read_input_tokens": 24108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12731
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 8_

文件已读取，开始执行 4 项修改。

**修 1**：更新 Section 4.2 precompute 流程 + Section 9 风险表
**修 2**：更新 Section 7.3 实验矩阵
**修 3**：添加环境依赖小节
**额外**：添加 φ 归一化验证小节

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "7e9261a8-b726-4a7f-9ada-6835d547b936",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJynHHJRuVjY8rjtmF8Nkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12731,
      "cache_read_input_tokens": 24108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12731
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01Vhfbkk7YLBsLoZSDRUh1jV`</summary>

````json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`。训练前一次性计算所有样本的 ref logps 并缓存为 `.npz`，训练时从 dataset 直接读取。优势：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%",
  "new_string": "trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "d12009f4-a2c5-45b7-9ccd-e94b36b1c46e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJynHHJRuVjY8rjtmF8Nkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12731,
      "cache_read_input_tokens": 24108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12731
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T11:00:48.933Z_

<details><summary>↩ Tool result · `toolu_01Vhfbkk7YLBsLoZSDRUh1jV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "6539cab7-df21-4de9-b928-0a026d4f7a3b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "oldString": "trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`。训练前一次性计算所有样本的 ref logps 并缓存为 `.npz`，训练时从 dataset 直接读取。优势：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%",
    "newString": "trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确",
    "originalFile": "# DMPO + ETADN 训练 Pipeline 设计（v2）\n\n## 0. 术语与背景\n\n**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。\n\n**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。\n\n**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。\n\n---\n\n## 1. DMPO Loss 实现方案\n\n### 1.1 完整 DMPO Loss 公式\n\n标准 DPO loss（单轮）：\n\n```\nL_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]\n```\n\nDMPO loss（多轮，论文 Eq.16）：\n\n```\nL_DMPO = -E[ log σ(\n    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]\n  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]\n)]\n```\n\n其中时间折扣函数：\n\n```\nφ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n```\n\n- t = turn index (0-indexed)\n- T = 总 turn 数\n- γ ∈ (0, 1) = 时间折扣因子\n- φ(t, T) 单调递减：早期 turn 权重更高\n\n**特殊情况**：\n- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO\n- γ = 1: φ(t,T) = (T-t)/T → 线性衰减\n\n### 1.2 在 trl DPOTrainer 上实现 DMPO\n\n**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。\n\n**需要修改的核心逻辑**（在 `_compute_loss` 内）：\n\n| 原始 trl 行为 | DMPO 修改 |\n|---|---|\n| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |\n| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |\n| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |\n\n**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。\n\n### 1.3 Per-turn log probability 计算\n\nALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。\n\n**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：\n\n```\ntoken:    [&lt;prompt> | Think... Act... | Think... Act... | Think... Act... ]\nturn_ids: [   -1    |       0        |        1        |        2        ]\n```\n\n**加权聚合伪代码**：\n\n```python\ndef dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):\n    \"\"\"\n    per_token_logps: [batch, seq_len]\n    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)\n    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)\n    gamma:           [batch]           (per-sample γ)\n    num_turns:       [batch]           (per-sample T)\n    Returns:         [batch]           (weighted log probability per sample)\n    \"\"\"\n    # 构建 per-token φ 权重\n    token_weights = torch.zeros_like(per_token_logps)\n    for t in range(turn_ids.max() + 1):\n        mask_t = (turn_ids == t)  # [batch, seq_len]\n        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)\n        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]\n\n    return (per_token_logps * completion_mask * token_weights).sum(dim=1)\n```\n\n**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：\n\n```python\ndef compute_phi_weights(turn_ids, gamma, num_turns, max_turns):\n    \"\"\"全向量化 φ 权重计算\"\"\"\n    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]\n    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]\n    T = num_turns.unsqueeze(1).float()                            # [batch, 1]\n\n    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)\n    # phi: [batch, max_turns]\n\n    # 用 turn_ids gather 到 per-token 权重\n    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零\n    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]\n    return token_phi\n```\n\n### 1.4 φ(t,T) 权重应用到 per-turn loss\n\n在 `_compute_loss` 中，替换聚合步骤：\n\n```python\n# === 原始 trl ===\n# logps = per_token_logps.sum(dim=1)\n\n# === DMPO 修改 ===\ntoken_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)\nlogps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\nchosen_logps, rejected_logps = logps.chunk(2, dim=0)\n# 后续 log ratio、sigmoid loss 与标准 DPO 相同\n```\n\n---\n\n## 2. γ_e 注入方案\n\n### 2.1 Error Type → γ_e 映射\n\n```yaml\n# config.yaml\ngamma_e_mapping:\n  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步\n  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列\n  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹\n  default: 0.90   # 未分类 fallback\n```\n\n**直觉**：\n- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）\n- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）\n\n### 2.2 注入流程\n\n```\n数据加载 → 每个样本有 error_type 字段\n       ↓\nDataCollator → 查表得到 gamma_per_sample: [batch_size]\n       ↓\n_compute_loss → gamma_per_sample 传入 compute_phi_weights()\n       ↓\nper-token 权重 → 加权聚合 → 标准 sigmoid loss\n```\n\n**Collator 中的 γ 注入**：\n\n```python\nclass DMPODataCollator(DataCollatorForPreference):\n    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):\n        super().__init__(**kwargs)\n        self.gamma_map = gamma_map\n        self.mode = mode\n        self.global_gamma = global_gamma\n\n    def __call__(self, features):\n        batch = super().__call__(features)\n\n        # 收集 error_type → gamma\n        gammas = []\n        for f in features:\n            if self.mode == \"etadn\":\n                et = f.get(\"error_type\", \"default\")\n                gammas.append(self.gamma_map.get(et, self.gamma_map[\"default\"]))\n            elif self.mode == \"dmpo\":\n                gammas.append(self.global_gamma)\n            else:  # dpo\n                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权\n\n        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）\n        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)\n        gamma_rejected = gamma_chosen.clone()\n        batch[\"gamma\"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)\n\n        return batch\n```\n\n### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e\n\n| 维度 | DMPO | ETADN |\n|---|---|---|\n| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |\n| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |\n| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |\n| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |\n\n---\n\n## 3. 数据 Pipeline\n\n### 3.1 DPO 数据格式\n\n每个样本包含：\n\n```json\n{\n  \"id\": \"alfworld_task_42_pair_0\",\n  \"error_type\": \"action\",\n  \"prompt\": \"You are in a kitchen. Your task is to ...\",\n  \"chosen\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: I should open it. Act: open fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You open the fridge. You see a tomato 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Found it. Act: take tomato 1 from fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You pick up the tomato 1.\"}\n  ],\n  \"rejected\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to countertop 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a bread 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Not here. Act: go to countertop 2\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a cup 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Maybe in the cabinet. Act: go to cabinet 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The cabinet is closed.\"}\n  ],\n  \"chosen_turns\": 3,\n  \"rejected_turns\": 3\n}\n```\n\n### 3.2 多轮对话处理：Turn 定义\n\nALFWorld 轨迹中每个 turn 的结构：\n\n```\nTurn t:\n  Assistant: \"Think: &lt;reasoning>. Act: &lt;action>\"    ← agent 生成\n  User:      \"Obs: &lt;environment_observation>\"        ← 环境返回\n```\n\n**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。\n\nTurn 数 T = assistant 回复的数量。\n\n### 3.3 Tokenization 与 Turn 标记\n\n```python\ndef tokenize_multiturn(example, tokenizer, max_length):\n    \"\"\"将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids\"\"\"\n    # 1. 构建完整对话（chat template）\n    messages = [{\"role\": \"system\", \"content\": example[\"prompt\"]}]\n    messages += example[\"chosen\"]  # 或 rejected\n\n    # 2. 分步 tokenize 以获取 turn 边界\n    prompt_ids = tokenizer.apply_chat_template(\n        [messages[0]], tokenize=True, add_generation_prompt=True\n    )\n\n    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1\n    completion_mask = [0] * len(prompt_ids)\n    all_ids = list(prompt_ids)\n    current_turn = 0\n\n    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs\n        # assistant 部分\n        asst_msg = messages[i]\n        asst_ids = tokenizer.encode(asst_msg[\"content\"], add_special_tokens=False)\n        # + chat template 的 role tokens\n        role_ids = tokenizer.encode(\"<|im_start|>assistant\\n\", add_special_tokens=False)\n        end_ids = tokenizer.encode(\"<|im_end|>\\n\", add_special_tokens=False)\n\n        all_ids += role_ids\n        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss\n        completion_mask += [0] * len(role_ids)\n\n        all_ids += asst_ids\n        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t\n        completion_mask += [1] * len(asst_ids)\n\n        all_ids += end_ids\n        turn_ids += [current_turn] * len(end_ids)\n        completion_mask += [1] * len(end_ids)\n\n        # user/observation 部分\n        if i + 1 < len(messages):\n            user_msg = messages[i + 1]\n            user_ids = tokenizer.encode(\n                f\"<|im_start|>user\\n{user_msg['content']}<|im_end|>\\n\",\n                add_special_tokens=False\n            )\n            all_ids += user_ids\n            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss\n            completion_mask += [0] * len(user_ids)\n\n        current_turn += 1\n\n    # 3. 截断\n    all_ids = all_ids[:max_length]\n    turn_ids = turn_ids[:max_length]\n    completion_mask = completion_mask[:max_length]\n\n    return {\n        \"input_ids\": all_ids,\n        \"turn_ids\": turn_ids,\n        \"completion_mask\": completion_mask,\n        \"num_turns\": current_turn,\n    }\n```\n\n**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。\n\n### 3.4 数据集统计预估\n\n| 维度 | 估计值 |\n|---|---|\n| ALFWorld 任务数 | ~3,500 (train split) |\n| 每任务轨迹数 | 5-10（采样多条） |\n| 有效 preference pairs | ~2,000-5,000（过滤后） |\n| 平均 turn 数 T | 5-15 |\n| 平均序列长度 | 1,500-3,000 tokens |\n\n---\n\n## 4. 模型配置\n\n### 4.1 Qwen3-8B QLoRA 配置\n\n```python\nfrom transformers import AutoModelForCausalLM, BitsAndBytesConfig\nfrom peft import LoraConfig\n\nbnb_config = BitsAndBytesConfig(\n    load_in_4bit=True,\n    bnb_4bit_quant_type=\"nf4\",\n    bnb_4bit_compute_dtype=torch.bfloat16,\n    bnb_4bit_use_double_quant=True,\n)\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    \"Qwen/Qwen3-8B\",\n    quantization_config=bnb_config,\n    torch_dtype=torch.bfloat16,\n    attn_implementation=\"flash_attention_2\",\n    device_map={\"\": device_id},  # 单卡绑定\n)\n\nlora_config = LoraConfig(\n    r=64,\n    lora_alpha=128,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                     \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_dropout=0.05,\n    task_type=\"CAUSAL_LM\",\n    bias=\"none\",\n)\n```\n\n### 4.2 Ref Model 处理\n\nQLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。\n\ntrl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`。训练前一次性计算所有样本的 ref logps 并缓存为 `.npz`，训练时从 dataset 直接读取。优势：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n\n### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）\n\n| 组件 | 估计 VRAM |\n|---|---|\n| Qwen3-8B 4-bit weights | ~4.5 GB |\n| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |\n| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |\n| Gradients (bf16) | ~0.4 GB |\n| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |\n| PyTorch + CUDA overhead | ~2 GB |\n| **总计** | **~15-17 GB** |\n\n剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。\n\n**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。\n\n### 4.4 训练超参\n\n```yaml\n# config.yaml\ntraining:\n  mode: \"etadn\"            # \"dpo\" | \"dmpo\" | \"etadn\"\n  beta: 0.1                # DPO β\n  global_gamma: 0.90       # DMPO 模式下的全局 γ\n  learning_rate: 1.0e-6\n  lr_scheduler_type: \"constant_with_warmup\"\n  warmup_ratio: 0.1\n  num_train_epochs: 3\n  per_device_train_batch_size: 1\n  gradient_accumulation_steps: 16\n  gradient_checkpointing: true\n  bf16: true\n  max_length: 3072\n  max_prompt_length: 512\n  logging_steps: 5\n  save_steps: 100\n  eval_steps: 50\n  precompute_ref_log_probs: true\n  label_smoothing: 0.0\n  loss_type: \"sigmoid\"\n\nlora:\n  r: 64\n  lora_alpha: 128\n  target_modules: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n  lora_dropout: 0.05\n\ngamma_e_mapping:\n  action: 0.85\n  verify: 0.92\n  plan: 0.97\n  default: 0.90\n```\n\n---\n\n## 5. 推理 Pipeline\n\n### 5.1 轨迹收集\n\n```python\n# collect_trajectories.py\n# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互\n# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）\n\nfrom vllm import LLM, SamplingParams  # 或 transformers.generate\n\nmodel = LLM(\n    model=\"path/to/qwen3-8b-merged\",  # LoRA merge 后的 checkpoint\n    tensor_parallel_size=1,\n    gpu_memory_utilization=0.85,\n    max_model_len=4096,\n)\n\nparams = SamplingParams(\n    temperature=0.7,\n    top_p=0.9,\n    max_tokens=256,      # 每步生成上限\n    stop=[\"Obs:\"],       # ALFWorld 环境会返回 Obs\n)\n\n# 循环：generate → parse action → env.step → append obs → repeat\n```\n\n**输出格式**：\n\n```json\n{\n  \"task_id\": \"pick_clean_then_place-Tomato-...\",\n  \"trajectory\": [\n    {\"role\": \"assistant\", \"content\": \"Think: ... Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    ...\n  ],\n  \"reward\": 1,           # ALFWorld: 1=成功, 0=失败\n  \"num_steps\": 8,\n  \"task_type\": \"pick_clean_then_place\"\n}\n```\n\n### 5.2 错误分类\n\n```python\n# classify_errors.py\n# 用 Qwen3-14B-AWQ 做 zero-shot 分类\n\nCLASSIFY_PROMPT = \"\"\"Analyze the following failed trajectory in ALFWorld.\nThe agent attempted a task but failed. Identify the PRIMARY error type:\n\n- action: Wrong physical action (e.g., went to wrong location, used wrong object)\n- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)\n- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)\n\nTask: {task_description}\nSuccessful trajectory: {chosen_trajectory}\nFailed trajectory: {rejected_trajectory}\n\nRespond with ONLY one word: action, verify, or plan\"\"\"\n\n# 输出: error_type ∈ {\"action\", \"verify\", \"plan\"}\n```\n\n### 5.3 Preference Pair 构建\n\n```python\n# construct_preference.py\n\ndef construct_pairs(trajectories, error_classifications):\n    \"\"\"\n    策略：\n    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected\n    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs\n    3. 附加 error_type 标签（来自 classify_errors.py 的输出）\n    \"\"\"\n    pairs = []\n    for task_id, task_trajs in group_by_task(trajectories):\n        chosen_trajs = [t for t in task_trajs if t[\"reward\"] == 1]\n        rejected_trajs = [t for t in task_trajs if t[\"reward\"] == 0]\n\n        if not chosen_trajs or not rejected_trajs:\n            continue\n\n        best_chosen = min(chosen_trajs, key=lambda t: t[\"num_steps\"])\n\n        for rej in rejected_trajs:\n            error_type = error_classifications.get(\n                f\"{task_id}_{rej['traj_id']}\", \"default\"\n            )\n            pairs.append({\n                \"id\": f\"{task_id}_pair_{len(pairs)}\",\n                \"error_type\": error_type,\n                \"prompt\": task_description(task_id),\n                \"chosen\": best_chosen[\"trajectory\"],\n                \"rejected\": rej[\"trajectory\"],\n                \"chosen_turns\": count_assistant_turns(best_chosen[\"trajectory\"]),\n                \"rejected_turns\": count_assistant_turns(rej[\"trajectory\"]),\n            })\n\n    return pairs\n```\n\n---\n\n## 6. 完整文件结构\n\n```\nrl-active-probe-fl/\n├── train_etadn.py              # 主训练入口\n│   - 解析 config.yaml\n│   - 加载模型 + LoRA + BnB 量化\n│   - 构建 dataset + collator\n│   - 初始化 ETADNTrainer\n│   - trainer.train()\n│\n├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）\n│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted\n│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns\n│   - DMPODataCollator: 注入 gamma、pad turn_ids\n│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)\n│\n├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合\n│   - compute_phi(t, T, gamma): 单值 φ 计算\n│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重\n│   - dmpo_weighted_logps(): per_token_logps → weighted scalar\n│\n├── data_utils.py               # 数据加载与预处理\n│   - load_preference_data(path): 加载 JSON pairs\n│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization\n│   - build_dataset(): HF Dataset 构建\n│\n├── config.yaml                 # 超参配置（见 §4.4）\n│\n├── collect_trajectories.py     # 轨迹收集（§5.1）\n│   - ALFWorld 环境交互\n│   - vLLM / transformers 推理\n│   - 输出 trajectories.jsonl\n│\n├── classify_errors.py          # 错误分类（§5.2）\n│   - Qwen3-14B-AWQ zero-shot\n│   - 输出 error_classifications.json\n│\n├── construct_preference.py     # Preference pair 构建（§5.3）\n│   - 输入: trajectories + error_classifications\n│   - 输出: preference_pairs.json\n│\n├── evaluate.py                 # ALFWorld 评估\n│   - 标准 eval protocol: 134 unseen tasks\n│   - 指标: success rate, average steps\n│   - 按 task type 分组报告\n│\n├── scripts/\n│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)\n│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)\n│\n└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）\n    ├── env_wrapper.py\n    └── task_configs/\n```\n\n### 6.1 关键模块依赖关系\n\n```\nconfig.yaml\n    ↓\ntrain_etadn.py\n    ├── data_utils.py → tokenize_multiturn()\n    ├── dmpo_trainer.py → ETADNTrainer\n    │       ├── dmpo_loss.py → compute_phi_weights()\n    │       └── DMPODataCollator → gamma injection\n    └── evaluate.py (训练结束后调用)\n\ncollect_trajectories.py → trajectories.jsonl\n    ↓\nclassify_errors.py → error_classifications.json\n    ↓\nconstruct_preference.py → preference_pairs.json\n    ↓\ntrain_etadn.py (读取 preference_pairs.json)\n```\n\n---\n\n## 7. Ablation 设计\n\n### 7.1 三种模式切换\n\n通过 `config.yaml` 中 `training.mode` 字段切换：\n\n| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |\n|---|---|---|---|\n| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |\n| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |\n| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |\n\n### 7.2 代码中的模式分支\n\n在 `ETADNTrainer._compute_loss` 中：\n\n```python\nif self.mode == \"dpo\":\n    # 标准 DPO: 直接 sum\n    logps = (per_token_logps * shift_completion_mask).sum(dim=1)\nelse:\n    # dmpo 或 etadn: φ-weighted sum\n    # gamma 已由 collator 注入到 batch[\"gamma\"]\n    token_phi = compute_phi_weights(\n        turn_ids=batch[\"turn_ids\"][:, 1:],  # shift 对齐\n        gamma=batch[\"gamma\"],\n        num_turns=batch[\"num_turns\"],\n        max_turns=batch[\"turn_ids\"].max().item() + 1,\n    )\n    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n```\n\n### 7.3 实验矩阵\n\n| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| A2 | dpo | — | 1 | 42 | Baseline 复现 |\n| B1 | dmpo | 0.90 | 0 | 42 | Baseline: DMPO 全局 γ |\n| B2 | dmpo | 0.85 | 1 | 42 | DMPO γ 敏感性 |\n| C1 | etadn | per-sample | 0 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 1 | 123 | Ours 不同 seed |\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run。6 个 run 分 3 轮完成。\n\n### 7.4 评估指标\n\n| 指标 | 说明 |\n|---|---|\n| ALFWorld success rate (overall) | 主指标，134 unseen tasks |\n| Success rate per task type | 6 种 task type 的分项成功率 |\n| Average steps to success | 效率指标 |\n| Error type distribution shift | 训练前后的错误类型分布变化 |\n| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |\n| Training loss curve | 收敛性对比 |\n\n---\n\n## 8. ETADNTrainer 核心代码骨架\n\n```python\n# dmpo_trainer.py\n\nfrom trl import DPOTrainer, DPOConfig\nfrom dmpo_loss import compute_phi_weights\n\nclass ETADNConfig(DPOConfig):\n    mode: str = \"etadn\"          # \"dpo\" | \"dmpo\" | \"etadn\"\n    global_gamma: float = 0.90\n    gamma_e_mapping: dict = None  # {\"action\": 0.85, \"verify\": 0.92, \"plan\": 0.97}\n\n\nclass ETADNTrainer(DPOTrainer):\n\n    def __init__(self, *args, mode=\"etadn\", global_gamma=0.9, gamma_e_mapping=None, **kwargs):\n        super().__init__(*args, **kwargs)\n        self.mode = mode\n        self.global_gamma = global_gamma\n        self.gamma_e_mapping = gamma_e_mapping or {}\n\n    def _compute_loss(self, model, inputs, return_outputs=False):\n        \"\"\"Override: DMPO φ-weighted log probability aggregation.\"\"\"\n        # --- 1. 提取额外字段 ---\n        turn_ids = inputs.pop(\"turn_ids\", None)\n        num_turns = inputs.pop(\"num_turns\", None)\n        gamma = inputs.pop(\"gamma\", None)\n        completion_mask = inputs[\"completion_mask\"]\n        input_ids = inputs[\"input_ids\"]\n\n        # --- 2. Policy forward ---\n        model_kwargs = {k: v for k, v in inputs.items()\n                        if k not in (\"completion_mask\", \"ref_chosen_logps\", \"ref_rejected_logps\")}\n        outputs = model(**model_kwargs)\n\n        # --- 3. Per-token logps ---\n        from trl.trainer.utils import selective_log_softmax\n        shift_logits = outputs.logits[..., :-1, :].contiguous()\n        shift_labels = input_ids[..., 1:].contiguous()\n        shift_completion_mask = completion_mask[..., 1:].contiguous()\n        per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n        per_token_logps[shift_completion_mask == 0] = 0.0\n\n        # --- 4. 聚合（核心修改点） ---\n        if self.mode == \"dpo\" or turn_ids is None:\n            logps = per_token_logps.sum(dim=1)\n        else:\n            shift_turn_ids = turn_ids[..., 1:].contiguous()\n            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,\n                                            max_turns=shift_turn_ids.max().item() + 1)\n            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\n        chosen_logps, rejected_logps = logps.chunk(2, dim=0)\n\n        # --- 5. Reference logps ---\n        if \"ref_chosen_logps\" in inputs:\n            ref_chosen_logps = inputs[\"ref_chosen_logps\"]\n            ref_rejected_logps = inputs[\"ref_rejected_logps\"]\n        else:\n            with torch.no_grad():\n                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(\n                    model, inputs, shift_completion_mask,\n                    turn_ids=shift_turn_ids if self.mode != \"dpo\" else None,\n                    gamma=gamma, num_turns=num_turns,\n                )\n\n        # --- 6. Loss (sigmoid, same as standard DPO) ---\n        chosen_logratios = chosen_logps - ref_chosen_logps\n        rejected_logratios = rejected_logps - ref_rejected_logps\n        logits = chosen_logratios - rejected_logratios\n\n        loss = -F.logsigmoid(self.beta * logits).mean()\n\n        # --- 7. Metrics ---\n        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()\n        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()\n        reward_margin = (chosen_rewards - rejected_rewards).mean()\n\n        metrics = {\n            \"loss\": loss.detach().item(),\n            \"rewards/chosen\": chosen_rewards.mean().item(),\n            \"rewards/rejected\": rejected_rewards.mean().item(),\n            \"rewards/margin\": reward_margin.item(),\n        }\n        self.store_metrics(metrics, train_eval=\"train\")\n\n        if return_outputs:\n            return loss, {\"logits\": logits}\n        return loss\n```\n\n---\n\n## 9. 风险与注意事项\n\n| 风险 | 缓解 |\n|---|---|\n| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |\n| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |\n| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |\n| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |\n| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |\n\n---\n\n## 10. 实施优先级\n\n| Phase | 内容 | 估计时间 |\n|---|---|---|\n| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |\n| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |\n| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |\n| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |\n| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |\n| P6 | 完整训练 + 评估 | 2-3 天 |\n",
    "structuredPatch": [
      {
        "oldStart": 368,
        "oldLines": 9,
        "newStart": 368,
        "newLines": 68,
        "lines": [
          " 2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重",
          " 3. 或者直接 `model.disable_adapter()` → base model = ref model",
          " ",
          "-**推荐方式**：`precompute_ref_log_probs=True`。训练前一次性计算所有样本的 ref logps 并缓存为 `.npz`，训练时从 dataset 直接读取。优势：",
          "+**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。",
          "+",
          "+> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**",
          "+>",
          "+> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。",
          "+>",
          "+> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。",
          "+",
          "+**预计算流程**：",
          "+",
          "+```python",
          "+def precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):",
          "+    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"",
          "+    ref_model.eval()",
          "+    ref_model.disable_adapter()  # base model = ref model",
          "+",
          "+    ref_chosen_logps_list = []",
          "+    ref_rejected_logps_list = []",
          "+",
          "+    with torch.no_grad():",
          "+        for sample in dataset:",
          "+            for key in (\"chosen\", \"rejected\"):",
          "+                input_ids = sample[f\"{key}_input_ids\"]",
          "+                completion_mask = sample[f\"{key}_completion_mask\"]",
          "+                turn_ids = sample[f\"{key}_turn_ids\"]",
          "+                num_turns = sample[f\"{key}_num_turns\"]",
          "+",
          "+                # 1. Per-token logps",
          "+                outputs = ref_model(input_ids=input_ids.unsqueeze(0))",
          "+                shift_logits = outputs.logits[..., :-1, :].contiguous()",
          "+                shift_labels = input_ids[1:].unsqueeze(0)",
          "+                per_token_logps = selective_log_softmax(shift_logits, shift_labels)",
          "+                shift_mask = completion_mask[1:]",
          "+",
          "+                # 2. φ-weighted 聚合（与训练一致）",
          "+                if mode == \"dpo\":",
          "+                    logps = (per_token_logps * shift_mask).sum(dim=1)",
          "+                else:",
          "+                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])",
          "+                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)",
          "+                    T = torch.tensor([num_turns], device=input_ids.device)",
          "+                    shift_turn_ids = turn_ids[1:].unsqueeze(0)",
          "+                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,",
          "+                                                    max_turns=shift_turn_ids.max().item() + 1)",
          "+                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)",
          "+",
          "+                if key == \"chosen\":",
          "+                    ref_chosen_logps_list.append(logps.item())",
          "+                else:",
          "+                    ref_rejected_logps_list.append(logps.item())",
          "+",
          "+    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）",
          "+    del ref_model",
          "+    torch.cuda.empty_cache()",
          "+",
          "+    return ref_chosen_logps_list, ref_rejected_logps_list",
          "+```",
          "+",
          "+**优势**：",
          " - 训练时无需 ref model 前向传播，节省 ~30% VRAM",
          " - 训练速度提升 ~40%",
          "+- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确",
          " ",
          " ### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）",
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01GpaAXRd8aovA9GnDjXidmM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| A2 | dpo | — | 1 | 42 | Baseline 复现 |\n| B1 | dmpo | 0.90 | 0 | 42 | Baseline: DMPO 全局 γ |\n| B2 | dmpo | 0.85 | 1 | 42 | DMPO γ 敏感性 |\n| C1 | etadn | per-sample | 0 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 1 | 123 | Ours 不同 seed |\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run。6 个 run 分 3 轮完成。",
  "new_string": "| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "ebe204ce-a585-4f93-adf3-a14a245b0bb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM4fvoGjqTikj8V8Re8tu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2703,
      "cache_read_input_tokens": 36839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2703
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T11:01:04.042Z_

<details><summary>↩ Tool result · `toolu_01GpaAXRd8aovA9GnDjXidmM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "ecf6f9a9-fd60-4897-a79b-fbd3f9b5259c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "oldString": "| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| A2 | dpo | — | 1 | 42 | Baseline 复现 |\n| B1 | dmpo | 0.90 | 0 | 42 | Baseline: DMPO 全局 γ |\n| B2 | dmpo | 0.85 | 1 | 42 | DMPO γ 敏感性 |\n| C1 | etadn | per-sample | 0 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 1 | 123 | Ours 不同 seed |\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run。6 个 run 分 3 轮完成。",
    "newString": "| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)",
    "originalFile": "# DMPO + ETADN 训练 Pipeline 设计（v2）\n\n## 0. 术语与背景\n\n**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。\n\n**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。\n\n**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。\n\n---\n\n## 1. DMPO Loss 实现方案\n\n### 1.1 完整 DMPO Loss 公式\n\n标准 DPO loss（单轮）：\n\n```\nL_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]\n```\n\nDMPO loss（多轮，论文 Eq.16）：\n\n```\nL_DMPO = -E[ log σ(\n    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]\n  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]\n)]\n```\n\n其中时间折扣函数：\n\n```\nφ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n```\n\n- t = turn index (0-indexed)\n- T = 总 turn 数\n- γ ∈ (0, 1) = 时间折扣因子\n- φ(t, T) 单调递减：早期 turn 权重更高\n\n**特殊情况**：\n- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO\n- γ = 1: φ(t,T) = (T-t)/T → 线性衰减\n\n### 1.2 在 trl DPOTrainer 上实现 DMPO\n\n**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。\n\n**需要修改的核心逻辑**（在 `_compute_loss` 内）：\n\n| 原始 trl 行为 | DMPO 修改 |\n|---|---|\n| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |\n| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |\n| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |\n\n**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。\n\n### 1.3 Per-turn log probability 计算\n\nALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。\n\n**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：\n\n```\ntoken:    [&lt;prompt> | Think... Act... | Think... Act... | Think... Act... ]\nturn_ids: [   -1    |       0        |        1        |        2        ]\n```\n\n**加权聚合伪代码**：\n\n```python\ndef dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):\n    \"\"\"\n    per_token_logps: [batch, seq_len]\n    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)\n    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)\n    gamma:           [batch]           (per-sample γ)\n    num_turns:       [batch]           (per-sample T)\n    Returns:         [batch]           (weighted log probability per sample)\n    \"\"\"\n    # 构建 per-token φ 权重\n    token_weights = torch.zeros_like(per_token_logps)\n    for t in range(turn_ids.max() + 1):\n        mask_t = (turn_ids == t)  # [batch, seq_len]\n        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)\n        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]\n\n    return (per_token_logps * completion_mask * token_weights).sum(dim=1)\n```\n\n**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：\n\n```python\ndef compute_phi_weights(turn_ids, gamma, num_turns, max_turns):\n    \"\"\"全向量化 φ 权重计算\"\"\"\n    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]\n    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]\n    T = num_turns.unsqueeze(1).float()                            # [batch, 1]\n\n    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)\n    # phi: [batch, max_turns]\n\n    # 用 turn_ids gather 到 per-token 权重\n    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零\n    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]\n    return token_phi\n```\n\n### 1.4 φ(t,T) 权重应用到 per-turn loss\n\n在 `_compute_loss` 中，替换聚合步骤：\n\n```python\n# === 原始 trl ===\n# logps = per_token_logps.sum(dim=1)\n\n# === DMPO 修改 ===\ntoken_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)\nlogps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\nchosen_logps, rejected_logps = logps.chunk(2, dim=0)\n# 后续 log ratio、sigmoid loss 与标准 DPO 相同\n```\n\n---\n\n## 2. γ_e 注入方案\n\n### 2.1 Error Type → γ_e 映射\n\n```yaml\n# config.yaml\ngamma_e_mapping:\n  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步\n  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列\n  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹\n  default: 0.90   # 未分类 fallback\n```\n\n**直觉**：\n- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）\n- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）\n\n### 2.2 注入流程\n\n```\n数据加载 → 每个样本有 error_type 字段\n       ↓\nDataCollator → 查表得到 gamma_per_sample: [batch_size]\n       ↓\n_compute_loss → gamma_per_sample 传入 compute_phi_weights()\n       ↓\nper-token 权重 → 加权聚合 → 标准 sigmoid loss\n```\n\n**Collator 中的 γ 注入**：\n\n```python\nclass DMPODataCollator(DataCollatorForPreference):\n    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):\n        super().__init__(**kwargs)\n        self.gamma_map = gamma_map\n        self.mode = mode\n        self.global_gamma = global_gamma\n\n    def __call__(self, features):\n        batch = super().__call__(features)\n\n        # 收集 error_type → gamma\n        gammas = []\n        for f in features:\n            if self.mode == \"etadn\":\n                et = f.get(\"error_type\", \"default\")\n                gammas.append(self.gamma_map.get(et, self.gamma_map[\"default\"]))\n            elif self.mode == \"dmpo\":\n                gammas.append(self.global_gamma)\n            else:  # dpo\n                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权\n\n        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）\n        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)\n        gamma_rejected = gamma_chosen.clone()\n        batch[\"gamma\"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)\n\n        return batch\n```\n\n### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e\n\n| 维度 | DMPO | ETADN |\n|---|---|---|\n| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |\n| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |\n| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |\n| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |\n\n---\n\n## 3. 数据 Pipeline\n\n### 3.1 DPO 数据格式\n\n每个样本包含：\n\n```json\n{\n  \"id\": \"alfworld_task_42_pair_0\",\n  \"error_type\": \"action\",\n  \"prompt\": \"You are in a kitchen. Your task is to ...\",\n  \"chosen\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: I should open it. Act: open fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You open the fridge. You see a tomato 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Found it. Act: take tomato 1 from fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You pick up the tomato 1.\"}\n  ],\n  \"rejected\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to countertop 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a bread 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Not here. Act: go to countertop 2\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a cup 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Maybe in the cabinet. Act: go to cabinet 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The cabinet is closed.\"}\n  ],\n  \"chosen_turns\": 3,\n  \"rejected_turns\": 3\n}\n```\n\n### 3.2 多轮对话处理：Turn 定义\n\nALFWorld 轨迹中每个 turn 的结构：\n\n```\nTurn t:\n  Assistant: \"Think: &lt;reasoning>. Act: &lt;action>\"    ← agent 生成\n  User:      \"Obs: &lt;environment_observation>\"        ← 环境返回\n```\n\n**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。\n\nTurn 数 T = assistant 回复的数量。\n\n### 3.3 Tokenization 与 Turn 标记\n\n```python\ndef tokenize_multiturn(example, tokenizer, max_length):\n    \"\"\"将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids\"\"\"\n    # 1. 构建完整对话（chat template）\n    messages = [{\"role\": \"system\", \"content\": example[\"prompt\"]}]\n    messages += example[\"chosen\"]  # 或 rejected\n\n    # 2. 分步 tokenize 以获取 turn 边界\n    prompt_ids = tokenizer.apply_chat_template(\n        [messages[0]], tokenize=True, add_generation_prompt=True\n    )\n\n    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1\n    completion_mask = [0] * len(prompt_ids)\n    all_ids = list(prompt_ids)\n    current_turn = 0\n\n    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs\n        # assistant 部分\n        asst_msg = messages[i]\n        asst_ids = tokenizer.encode(asst_msg[\"content\"], add_special_tokens=False)\n        # + chat template 的 role tokens\n        role_ids = tokenizer.encode(\"<|im_start|>assistant\\n\", add_special_tokens=False)\n        end_ids = tokenizer.encode(\"<|im_end|>\\n\", add_special_tokens=False)\n\n        all_ids += role_ids\n        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss\n        completion_mask += [0] * len(role_ids)\n\n        all_ids += asst_ids\n        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t\n        completion_mask += [1] * len(asst_ids)\n\n        all_ids += end_ids\n        turn_ids += [current_turn] * len(end_ids)\n        completion_mask += [1] * len(end_ids)\n\n        # user/observation 部分\n        if i + 1 < len(messages):\n            user_msg = messages[i + 1]\n            user_ids = tokenizer.encode(\n                f\"<|im_start|>user\\n{user_msg['content']}<|im_end|>\\n\",\n                add_special_tokens=False\n            )\n            all_ids += user_ids\n            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss\n            completion_mask += [0] * len(user_ids)\n\n        current_turn += 1\n\n    # 3. 截断\n    all_ids = all_ids[:max_length]\n    turn_ids = turn_ids[:max_length]\n    completion_mask = completion_mask[:max_length]\n\n    return {\n        \"input_ids\": all_ids,\n        \"turn_ids\": turn_ids,\n        \"completion_mask\": completion_mask,\n        \"num_turns\": current_turn,\n    }\n```\n\n**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。\n\n### 3.4 数据集统计预估\n\n| 维度 | 估计值 |\n|---|---|\n| ALFWorld 任务数 | ~3,500 (train split) |\n| 每任务轨迹数 | 5-10（采样多条） |\n| 有效 preference pairs | ~2,000-5,000（过滤后） |\n| 平均 turn 数 T | 5-15 |\n| 平均序列长度 | 1,500-3,000 tokens |\n\n---\n\n## 4. 模型配置\n\n### 4.1 Qwen3-8B QLoRA 配置\n\n```python\nfrom transformers import AutoModelForCausalLM, BitsAndBytesConfig\nfrom peft import LoraConfig\n\nbnb_config = BitsAndBytesConfig(\n    load_in_4bit=True,\n    bnb_4bit_quant_type=\"nf4\",\n    bnb_4bit_compute_dtype=torch.bfloat16,\n    bnb_4bit_use_double_quant=True,\n)\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    \"Qwen/Qwen3-8B\",\n    quantization_config=bnb_config,\n    torch_dtype=torch.bfloat16,\n    attn_implementation=\"flash_attention_2\",\n    device_map={\"\": device_id},  # 单卡绑定\n)\n\nlora_config = LoraConfig(\n    r=64,\n    lora_alpha=128,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                     \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_dropout=0.05,\n    task_type=\"CAUSAL_LM\",\n    bias=\"none\",\n)\n```\n\n### 4.2 Ref Model 处理\n\nQLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。\n\ntrl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确\n\n### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）\n\n| 组件 | 估计 VRAM |\n|---|---|\n| Qwen3-8B 4-bit weights | ~4.5 GB |\n| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |\n| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |\n| Gradients (bf16) | ~0.4 GB |\n| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |\n| PyTorch + CUDA overhead | ~2 GB |\n| **总计** | **~15-17 GB** |\n\n剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。\n\n**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。\n\n### 4.4 训练超参\n\n```yaml\n# config.yaml\ntraining:\n  mode: \"etadn\"            # \"dpo\" | \"dmpo\" | \"etadn\"\n  beta: 0.1                # DPO β\n  global_gamma: 0.90       # DMPO 模式下的全局 γ\n  learning_rate: 1.0e-6\n  lr_scheduler_type: \"constant_with_warmup\"\n  warmup_ratio: 0.1\n  num_train_epochs: 3\n  per_device_train_batch_size: 1\n  gradient_accumulation_steps: 16\n  gradient_checkpointing: true\n  bf16: true\n  max_length: 3072\n  max_prompt_length: 512\n  logging_steps: 5\n  save_steps: 100\n  eval_steps: 50\n  precompute_ref_log_probs: true\n  label_smoothing: 0.0\n  loss_type: \"sigmoid\"\n\nlora:\n  r: 64\n  lora_alpha: 128\n  target_modules: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n  lora_dropout: 0.05\n\ngamma_e_mapping:\n  action: 0.85\n  verify: 0.92\n  plan: 0.97\n  default: 0.90\n```\n\n---\n\n## 5. 推理 Pipeline\n\n### 5.1 轨迹收集\n\n```python\n# collect_trajectories.py\n# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互\n# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）\n\nfrom vllm import LLM, SamplingParams  # 或 transformers.generate\n\nmodel = LLM(\n    model=\"path/to/qwen3-8b-merged\",  # LoRA merge 后的 checkpoint\n    tensor_parallel_size=1,\n    gpu_memory_utilization=0.85,\n    max_model_len=4096,\n)\n\nparams = SamplingParams(\n    temperature=0.7,\n    top_p=0.9,\n    max_tokens=256,      # 每步生成上限\n    stop=[\"Obs:\"],       # ALFWorld 环境会返回 Obs\n)\n\n# 循环：generate → parse action → env.step → append obs → repeat\n```\n\n**输出格式**：\n\n```json\n{\n  \"task_id\": \"pick_clean_then_place-Tomato-...\",\n  \"trajectory\": [\n    {\"role\": \"assistant\", \"content\": \"Think: ... Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    ...\n  ],\n  \"reward\": 1,           # ALFWorld: 1=成功, 0=失败\n  \"num_steps\": 8,\n  \"task_type\": \"pick_clean_then_place\"\n}\n```\n\n### 5.2 错误分类\n\n```python\n# classify_errors.py\n# 用 Qwen3-14B-AWQ 做 zero-shot 分类\n\nCLASSIFY_PROMPT = \"\"\"Analyze the following failed trajectory in ALFWorld.\nThe agent attempted a task but failed. Identify the PRIMARY error type:\n\n- action: Wrong physical action (e.g., went to wrong location, used wrong object)\n- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)\n- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)\n\nTask: {task_description}\nSuccessful trajectory: {chosen_trajectory}\nFailed trajectory: {rejected_trajectory}\n\nRespond with ONLY one word: action, verify, or plan\"\"\"\n\n# 输出: error_type ∈ {\"action\", \"verify\", \"plan\"}\n```\n\n### 5.3 Preference Pair 构建\n\n```python\n# construct_preference.py\n\ndef construct_pairs(trajectories, error_classifications):\n    \"\"\"\n    策略：\n    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected\n    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs\n    3. 附加 error_type 标签（来自 classify_errors.py 的输出）\n    \"\"\"\n    pairs = []\n    for task_id, task_trajs in group_by_task(trajectories):\n        chosen_trajs = [t for t in task_trajs if t[\"reward\"] == 1]\n        rejected_trajs = [t for t in task_trajs if t[\"reward\"] == 0]\n\n        if not chosen_trajs or not rejected_trajs:\n            continue\n\n        best_chosen = min(chosen_trajs, key=lambda t: t[\"num_steps\"])\n\n        for rej in rejected_trajs:\n            error_type = error_classifications.get(\n                f\"{task_id}_{rej['traj_id']}\", \"default\"\n            )\n            pairs.append({\n                \"id\": f\"{task_id}_pair_{len(pairs)}\",\n                \"error_type\": error_type,\n                \"prompt\": task_description(task_id),\n                \"chosen\": best_chosen[\"trajectory\"],\n                \"rejected\": rej[\"trajectory\"],\n                \"chosen_turns\": count_assistant_turns(best_chosen[\"trajectory\"]),\n                \"rejected_turns\": count_assistant_turns(rej[\"trajectory\"]),\n            })\n\n    return pairs\n```\n\n---\n\n## 6. 完整文件结构\n\n```\nrl-active-probe-fl/\n├── train_etadn.py              # 主训练入口\n│   - 解析 config.yaml\n│   - 加载模型 + LoRA + BnB 量化\n│   - 构建 dataset + collator\n│   - 初始化 ETADNTrainer\n│   - trainer.train()\n│\n├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）\n│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted\n│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns\n│   - DMPODataCollator: 注入 gamma、pad turn_ids\n│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)\n│\n├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合\n│   - compute_phi(t, T, gamma): 单值 φ 计算\n│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重\n│   - dmpo_weighted_logps(): per_token_logps → weighted scalar\n│\n├── data_utils.py               # 数据加载与预处理\n│   - load_preference_data(path): 加载 JSON pairs\n│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization\n│   - build_dataset(): HF Dataset 构建\n│\n├── config.yaml                 # 超参配置（见 §4.4）\n│\n├── collect_trajectories.py     # 轨迹收集（§5.1）\n│   - ALFWorld 环境交互\n│   - vLLM / transformers 推理\n│   - 输出 trajectories.jsonl\n│\n├── classify_errors.py          # 错误分类（§5.2）\n│   - Qwen3-14B-AWQ zero-shot\n│   - 输出 error_classifications.json\n│\n├── construct_preference.py     # Preference pair 构建（§5.3）\n│   - 输入: trajectories + error_classifications\n│   - 输出: preference_pairs.json\n│\n├── evaluate.py                 # ALFWorld 评估\n│   - 标准 eval protocol: 134 unseen tasks\n│   - 指标: success rate, average steps\n│   - 按 task type 分组报告\n│\n├── scripts/\n│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)\n│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)\n│\n└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）\n    ├── env_wrapper.py\n    └── task_configs/\n```\n\n### 6.1 关键模块依赖关系\n\n```\nconfig.yaml\n    ↓\ntrain_etadn.py\n    ├── data_utils.py → tokenize_multiturn()\n    ├── dmpo_trainer.py → ETADNTrainer\n    │       ├── dmpo_loss.py → compute_phi_weights()\n    │       └── DMPODataCollator → gamma injection\n    └── evaluate.py (训练结束后调用)\n\ncollect_trajectories.py → trajectories.jsonl\n    ↓\nclassify_errors.py → error_classifications.json\n    ↓\nconstruct_preference.py → preference_pairs.json\n    ↓\ntrain_etadn.py (读取 preference_pairs.json)\n```\n\n---\n\n## 7. Ablation 设计\n\n### 7.1 三种模式切换\n\n通过 `config.yaml` 中 `training.mode` 字段切换：\n\n| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |\n|---|---|---|---|\n| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |\n| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |\n| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |\n\n### 7.2 代码中的模式分支\n\n在 `ETADNTrainer._compute_loss` 中：\n\n```python\nif self.mode == \"dpo\":\n    # 标准 DPO: 直接 sum\n    logps = (per_token_logps * shift_completion_mask).sum(dim=1)\nelse:\n    # dmpo 或 etadn: φ-weighted sum\n    # gamma 已由 collator 注入到 batch[\"gamma\"]\n    token_phi = compute_phi_weights(\n        turn_ids=batch[\"turn_ids\"][:, 1:],  # shift 对齐\n        gamma=batch[\"gamma\"],\n        num_turns=batch[\"num_turns\"],\n        max_turns=batch[\"turn_ids\"].max().item() + 1,\n    )\n    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n```\n\n### 7.3 实验矩阵\n\n| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| A2 | dpo | — | 1 | 42 | Baseline 复现 |\n| B1 | dmpo | 0.90 | 0 | 42 | Baseline: DMPO 全局 γ |\n| B2 | dmpo | 0.85 | 1 | 42 | DMPO γ 敏感性 |\n| C1 | etadn | per-sample | 0 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 1 | 123 | Ours 不同 seed |\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run。6 个 run 分 3 轮完成。\n\n### 7.4 评估指标\n\n| 指标 | 说明 |\n|---|---|\n| ALFWorld success rate (overall) | 主指标，134 unseen tasks |\n| Success rate per task type | 6 种 task type 的分项成功率 |\n| Average steps to success | 效率指标 |\n| Error type distribution shift | 训练前后的错误类型分布变化 |\n| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |\n| Training loss curve | 收敛性对比 |\n\n---\n\n## 8. ETADNTrainer 核心代码骨架\n\n```python\n# dmpo_trainer.py\n\nfrom trl import DPOTrainer, DPOConfig\nfrom dmpo_loss import compute_phi_weights\n\nclass ETADNConfig(DPOConfig):\n    mode: str = \"etadn\"          # \"dpo\" | \"dmpo\" | \"etadn\"\n    global_gamma: float = 0.90\n    gamma_e_mapping: dict = None  # {\"action\": 0.85, \"verify\": 0.92, \"plan\": 0.97}\n\n\nclass ETADNTrainer(DPOTrainer):\n\n    def __init__(self, *args, mode=\"etadn\", global_gamma=0.9, gamma_e_mapping=None, **kwargs):\n        super().__init__(*args, **kwargs)\n        self.mode = mode\n        self.global_gamma = global_gamma\n        self.gamma_e_mapping = gamma_e_mapping or {}\n\n    def _compute_loss(self, model, inputs, return_outputs=False):\n        \"\"\"Override: DMPO φ-weighted log probability aggregation.\"\"\"\n        # --- 1. 提取额外字段 ---\n        turn_ids = inputs.pop(\"turn_ids\", None)\n        num_turns = inputs.pop(\"num_turns\", None)\n        gamma = inputs.pop(\"gamma\", None)\n        completion_mask = inputs[\"completion_mask\"]\n        input_ids = inputs[\"input_ids\"]\n\n        # --- 2. Policy forward ---\n        model_kwargs = {k: v for k, v in inputs.items()\n                        if k not in (\"completion_mask\", \"ref_chosen_logps\", \"ref_rejected_logps\")}\n        outputs = model(**model_kwargs)\n\n        # --- 3. Per-token logps ---\n        from trl.trainer.utils import selective_log_softmax\n        shift_logits = outputs.logits[..., :-1, :].contiguous()\n        shift_labels = input_ids[..., 1:].contiguous()\n        shift_completion_mask = completion_mask[..., 1:].contiguous()\n        per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n        per_token_logps[shift_completion_mask == 0] = 0.0\n\n        # --- 4. 聚合（核心修改点） ---\n        if self.mode == \"dpo\" or turn_ids is None:\n            logps = per_token_logps.sum(dim=1)\n        else:\n            shift_turn_ids = turn_ids[..., 1:].contiguous()\n            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,\n                                            max_turns=shift_turn_ids.max().item() + 1)\n            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\n        chosen_logps, rejected_logps = logps.chunk(2, dim=0)\n\n        # --- 5. Reference logps ---\n        if \"ref_chosen_logps\" in inputs:\n            ref_chosen_logps = inputs[\"ref_chosen_logps\"]\n            ref_rejected_logps = inputs[\"ref_rejected_logps\"]\n        else:\n            with torch.no_grad():\n                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(\n                    model, inputs, shift_completion_mask,\n                    turn_ids=shift_turn_ids if self.mode != \"dpo\" else None,\n                    gamma=gamma, num_turns=num_turns,\n                )\n\n        # --- 6. Loss (sigmoid, same as standard DPO) ---\n        chosen_logratios = chosen_logps - ref_chosen_logps\n        rejected_logratios = rejected_logps - ref_rejected_logps\n        logits = chosen_logratios - rejected_logratios\n\n        loss = -F.logsigmoid(self.beta * logits).mean()\n\n        # --- 7. Metrics ---\n        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()\n        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()\n        reward_margin = (chosen_rewards - rejected_rewards).mean()\n\n        metrics = {\n            \"loss\": loss.detach().item(),\n            \"rewards/chosen\": chosen_rewards.mean().item(),\n            \"rewards/rejected\": rejected_rewards.mean().item(),\n            \"rewards/margin\": reward_margin.item(),\n        }\n        self.store_metrics(metrics, train_eval=\"train\")\n\n        if return_outputs:\n            return loss, {\"logits\": logits}\n        return loss\n```\n\n---\n\n## 9. 风险与注意事项\n\n| 风险 | 缓解 |\n|---|---|\n| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |\n| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |\n| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |\n| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |\n| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |\n\n---\n\n## 10. 实施优先级\n\n| Phase | 内容 | 估计时间 |\n|---|---|---|\n| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |\n| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |\n| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |\n| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |\n| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |\n| P6 | 完整训练 + 评估 | 2-3 天 |\n",
    "structuredPatch": [
      {
        "oldStart": 710,
        "oldLines": 14,
        "newStart": 710,
        "newLines": 23,
        "lines": [
          " | Run | Mode | γ / γ_e | GPU | Seed | 目的 |",
          " |---|---|---|---|---|---|",
          " | A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |",
          "-| A2 | dpo | — | 1 | 42 | Baseline 复现 |",
          "-| B1 | dmpo | 0.90 | 0 | 42 | Baseline: DMPO 全局 γ |",
          "-| B2 | dmpo | 0.85 | 1 | 42 | DMPO γ 敏感性 |",
          "-| C1 | etadn | per-sample | 0 | 42 | **Ours**: ETADN |",
          "-| C2 | etadn | per-sample | 1 | 123 | Ours 不同 seed |",
          "+| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |",
          "+| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |",
          "+| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |",
          "+| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |",
          "+| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |",
          "+| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |",
          " ",
          "-**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run。6 个 run 分 3 轮完成。",
          "+**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。",
          " ",
          "+**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。",
          "+",
          "+**调度顺序**：",
          "+1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号",
          "+2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)",
          "+3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)",
          "+4. 轮 4: A1 (DPO baseline seed=42, GPU0)",
          "+",
          " ### 7.4 评估指标",
          " ",
          " | 指标 | 说明 |"
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_017jJc2R22tQtAfkDsLvRYdk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |",
  "new_string": "| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "26d68a2a-19c1-495c-9b09-d41facee3c80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJobkBoyaC9HnVWdKPaUBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 39542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1019
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T11:01:10.086Z_

<details><summary>↩ Tool result · `toolu_017jJc2R22tQtAfkDsLvRYdk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "ad8b2420-3441-40fa-b162-ead8b27d144b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "oldString": "| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |",
    "newString": "| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |",
    "originalFile": "# DMPO + ETADN 训练 Pipeline 设计（v2）\n\n## 0. 术语与背景\n\n**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。\n\n**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。\n\n**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。\n\n---\n\n## 1. DMPO Loss 实现方案\n\n### 1.1 完整 DMPO Loss 公式\n\n标准 DPO loss（单轮）：\n\n```\nL_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]\n```\n\nDMPO loss（多轮，论文 Eq.16）：\n\n```\nL_DMPO = -E[ log σ(\n    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]\n  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]\n)]\n```\n\n其中时间折扣函数：\n\n```\nφ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n```\n\n- t = turn index (0-indexed)\n- T = 总 turn 数\n- γ ∈ (0, 1) = 时间折扣因子\n- φ(t, T) 单调递减：早期 turn 权重更高\n\n**特殊情况**：\n- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO\n- γ = 1: φ(t,T) = (T-t)/T → 线性衰减\n\n### 1.2 在 trl DPOTrainer 上实现 DMPO\n\n**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。\n\n**需要修改的核心逻辑**（在 `_compute_loss` 内）：\n\n| 原始 trl 行为 | DMPO 修改 |\n|---|---|\n| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |\n| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |\n| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |\n\n**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。\n\n### 1.3 Per-turn log probability 计算\n\nALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。\n\n**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：\n\n```\ntoken:    [&lt;prompt> | Think... Act... | Think... Act... | Think... Act... ]\nturn_ids: [   -1    |       0        |        1        |        2        ]\n```\n\n**加权聚合伪代码**：\n\n```python\ndef dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):\n    \"\"\"\n    per_token_logps: [batch, seq_len]\n    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)\n    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)\n    gamma:           [batch]           (per-sample γ)\n    num_turns:       [batch]           (per-sample T)\n    Returns:         [batch]           (weighted log probability per sample)\n    \"\"\"\n    # 构建 per-token φ 权重\n    token_weights = torch.zeros_like(per_token_logps)\n    for t in range(turn_ids.max() + 1):\n        mask_t = (turn_ids == t)  # [batch, seq_len]\n        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)\n        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]\n\n    return (per_token_logps * completion_mask * token_weights).sum(dim=1)\n```\n\n**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：\n\n```python\ndef compute_phi_weights(turn_ids, gamma, num_turns, max_turns):\n    \"\"\"全向量化 φ 权重计算\"\"\"\n    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]\n    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]\n    T = num_turns.unsqueeze(1).float()                            # [batch, 1]\n\n    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)\n    # phi: [batch, max_turns]\n\n    # 用 turn_ids gather 到 per-token 权重\n    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零\n    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]\n    return token_phi\n```\n\n### 1.4 φ(t,T) 权重应用到 per-turn loss\n\n在 `_compute_loss` 中，替换聚合步骤：\n\n```python\n# === 原始 trl ===\n# logps = per_token_logps.sum(dim=1)\n\n# === DMPO 修改 ===\ntoken_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)\nlogps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\nchosen_logps, rejected_logps = logps.chunk(2, dim=0)\n# 后续 log ratio、sigmoid loss 与标准 DPO 相同\n```\n\n---\n\n## 2. γ_e 注入方案\n\n### 2.1 Error Type → γ_e 映射\n\n```yaml\n# config.yaml\ngamma_e_mapping:\n  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步\n  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列\n  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹\n  default: 0.90   # 未分类 fallback\n```\n\n**直觉**：\n- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）\n- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）\n\n### 2.2 注入流程\n\n```\n数据加载 → 每个样本有 error_type 字段\n       ↓\nDataCollator → 查表得到 gamma_per_sample: [batch_size]\n       ↓\n_compute_loss → gamma_per_sample 传入 compute_phi_weights()\n       ↓\nper-token 权重 → 加权聚合 → 标准 sigmoid loss\n```\n\n**Collator 中的 γ 注入**：\n\n```python\nclass DMPODataCollator(DataCollatorForPreference):\n    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):\n        super().__init__(**kwargs)\n        self.gamma_map = gamma_map\n        self.mode = mode\n        self.global_gamma = global_gamma\n\n    def __call__(self, features):\n        batch = super().__call__(features)\n\n        # 收集 error_type → gamma\n        gammas = []\n        for f in features:\n            if self.mode == \"etadn\":\n                et = f.get(\"error_type\", \"default\")\n                gammas.append(self.gamma_map.get(et, self.gamma_map[\"default\"]))\n            elif self.mode == \"dmpo\":\n                gammas.append(self.global_gamma)\n            else:  # dpo\n                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权\n\n        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）\n        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)\n        gamma_rejected = gamma_chosen.clone()\n        batch[\"gamma\"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)\n\n        return batch\n```\n\n### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e\n\n| 维度 | DMPO | ETADN |\n|---|---|---|\n| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |\n| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |\n| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |\n| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |\n\n---\n\n## 3. 数据 Pipeline\n\n### 3.1 DPO 数据格式\n\n每个样本包含：\n\n```json\n{\n  \"id\": \"alfworld_task_42_pair_0\",\n  \"error_type\": \"action\",\n  \"prompt\": \"You are in a kitchen. Your task is to ...\",\n  \"chosen\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: I should open it. Act: open fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You open the fridge. You see a tomato 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Found it. Act: take tomato 1 from fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You pick up the tomato 1.\"}\n  ],\n  \"rejected\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to countertop 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a bread 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Not here. Act: go to countertop 2\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a cup 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Maybe in the cabinet. Act: go to cabinet 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The cabinet is closed.\"}\n  ],\n  \"chosen_turns\": 3,\n  \"rejected_turns\": 3\n}\n```\n\n### 3.2 多轮对话处理：Turn 定义\n\nALFWorld 轨迹中每个 turn 的结构：\n\n```\nTurn t:\n  Assistant: \"Think: &lt;reasoning>. Act: &lt;action>\"    ← agent 生成\n  User:      \"Obs: &lt;environment_observation>\"        ← 环境返回\n```\n\n**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。\n\nTurn 数 T = assistant 回复的数量。\n\n### 3.3 Tokenization 与 Turn 标记\n\n```python\ndef tokenize_multiturn(example, tokenizer, max_length):\n    \"\"\"将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids\"\"\"\n    # 1. 构建完整对话（chat template）\n    messages = [{\"role\": \"system\", \"content\": example[\"prompt\"]}]\n    messages += example[\"chosen\"]  # 或 rejected\n\n    # 2. 分步 tokenize 以获取 turn 边界\n    prompt_ids = tokenizer.apply_chat_template(\n        [messages[0]], tokenize=True, add_generation_prompt=True\n    )\n\n    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1\n    completion_mask = [0] * len(prompt_ids)\n    all_ids = list(prompt_ids)\n    current_turn = 0\n\n    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs\n        # assistant 部分\n        asst_msg = messages[i]\n        asst_ids = tokenizer.encode(asst_msg[\"content\"], add_special_tokens=False)\n        # + chat template 的 role tokens\n        role_ids = tokenizer.encode(\"<|im_start|>assistant\\n\", add_special_tokens=False)\n        end_ids = tokenizer.encode(\"<|im_end|>\\n\", add_special_tokens=False)\n\n        all_ids += role_ids\n        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss\n        completion_mask += [0] * len(role_ids)\n\n        all_ids += asst_ids\n        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t\n        completion_mask += [1] * len(asst_ids)\n\n        all_ids += end_ids\n        turn_ids += [current_turn] * len(end_ids)\n        completion_mask += [1] * len(end_ids)\n\n        # user/observation 部分\n        if i + 1 < len(messages):\n            user_msg = messages[i + 1]\n            user_ids = tokenizer.encode(\n                f\"<|im_start|>user\\n{user_msg['content']}<|im_end|>\\n\",\n                add_special_tokens=False\n            )\n            all_ids += user_ids\n            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss\n            completion_mask += [0] * len(user_ids)\n\n        current_turn += 1\n\n    # 3. 截断\n    all_ids = all_ids[:max_length]\n    turn_ids = turn_ids[:max_length]\n    completion_mask = completion_mask[:max_length]\n\n    return {\n        \"input_ids\": all_ids,\n        \"turn_ids\": turn_ids,\n        \"completion_mask\": completion_mask,\n        \"num_turns\": current_turn,\n    }\n```\n\n**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。\n\n### 3.4 数据集统计预估\n\n| 维度 | 估计值 |\n|---|---|\n| ALFWorld 任务数 | ~3,500 (train split) |\n| 每任务轨迹数 | 5-10（采样多条） |\n| 有效 preference pairs | ~2,000-5,000（过滤后） |\n| 平均 turn 数 T | 5-15 |\n| 平均序列长度 | 1,500-3,000 tokens |\n\n---\n\n## 4. 模型配置\n\n### 4.1 Qwen3-8B QLoRA 配置\n\n```python\nfrom transformers import AutoModelForCausalLM, BitsAndBytesConfig\nfrom peft import LoraConfig\n\nbnb_config = BitsAndBytesConfig(\n    load_in_4bit=True,\n    bnb_4bit_quant_type=\"nf4\",\n    bnb_4bit_compute_dtype=torch.bfloat16,\n    bnb_4bit_use_double_quant=True,\n)\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    \"Qwen/Qwen3-8B\",\n    quantization_config=bnb_config,\n    torch_dtype=torch.bfloat16,\n    attn_implementation=\"flash_attention_2\",\n    device_map={\"\": device_id},  # 单卡绑定\n)\n\nlora_config = LoraConfig(\n    r=64,\n    lora_alpha=128,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                     \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_dropout=0.05,\n    task_type=\"CAUSAL_LM\",\n    bias=\"none\",\n)\n```\n\n### 4.2 Ref Model 处理\n\nQLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。\n\ntrl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确\n\n### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）\n\n| 组件 | 估计 VRAM |\n|---|---|\n| Qwen3-8B 4-bit weights | ~4.5 GB |\n| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |\n| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |\n| Gradients (bf16) | ~0.4 GB |\n| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |\n| PyTorch + CUDA overhead | ~2 GB |\n| **总计** | **~15-17 GB** |\n\n剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。\n\n**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。\n\n### 4.4 训练超参\n\n```yaml\n# config.yaml\ntraining:\n  mode: \"etadn\"            # \"dpo\" | \"dmpo\" | \"etadn\"\n  beta: 0.1                # DPO β\n  global_gamma: 0.90       # DMPO 模式下的全局 γ\n  learning_rate: 1.0e-6\n  lr_scheduler_type: \"constant_with_warmup\"\n  warmup_ratio: 0.1\n  num_train_epochs: 3\n  per_device_train_batch_size: 1\n  gradient_accumulation_steps: 16\n  gradient_checkpointing: true\n  bf16: true\n  max_length: 3072\n  max_prompt_length: 512\n  logging_steps: 5\n  save_steps: 100\n  eval_steps: 50\n  precompute_ref_log_probs: true\n  label_smoothing: 0.0\n  loss_type: \"sigmoid\"\n\nlora:\n  r: 64\n  lora_alpha: 128\n  target_modules: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n  lora_dropout: 0.05\n\ngamma_e_mapping:\n  action: 0.85\n  verify: 0.92\n  plan: 0.97\n  default: 0.90\n```\n\n---\n\n## 5. 推理 Pipeline\n\n### 5.1 轨迹收集\n\n```python\n# collect_trajectories.py\n# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互\n# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）\n\nfrom vllm import LLM, SamplingParams  # 或 transformers.generate\n\nmodel = LLM(\n    model=\"path/to/qwen3-8b-merged\",  # LoRA merge 后的 checkpoint\n    tensor_parallel_size=1,\n    gpu_memory_utilization=0.85,\n    max_model_len=4096,\n)\n\nparams = SamplingParams(\n    temperature=0.7,\n    top_p=0.9,\n    max_tokens=256,      # 每步生成上限\n    stop=[\"Obs:\"],       # ALFWorld 环境会返回 Obs\n)\n\n# 循环：generate → parse action → env.step → append obs → repeat\n```\n\n**输出格式**：\n\n```json\n{\n  \"task_id\": \"pick_clean_then_place-Tomato-...\",\n  \"trajectory\": [\n    {\"role\": \"assistant\", \"content\": \"Think: ... Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    ...\n  ],\n  \"reward\": 1,           # ALFWorld: 1=成功, 0=失败\n  \"num_steps\": 8,\n  \"task_type\": \"pick_clean_then_place\"\n}\n```\n\n### 5.2 错误分类\n\n```python\n# classify_errors.py\n# 用 Qwen3-14B-AWQ 做 zero-shot 分类\n\nCLASSIFY_PROMPT = \"\"\"Analyze the following failed trajectory in ALFWorld.\nThe agent attempted a task but failed. Identify the PRIMARY error type:\n\n- action: Wrong physical action (e.g., went to wrong location, used wrong object)\n- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)\n- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)\n\nTask: {task_description}\nSuccessful trajectory: {chosen_trajectory}\nFailed trajectory: {rejected_trajectory}\n\nRespond with ONLY one word: action, verify, or plan\"\"\"\n\n# 输出: error_type ∈ {\"action\", \"verify\", \"plan\"}\n```\n\n### 5.3 Preference Pair 构建\n\n```python\n# construct_preference.py\n\ndef construct_pairs(trajectories, error_classifications):\n    \"\"\"\n    策略：\n    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected\n    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs\n    3. 附加 error_type 标签（来自 classify_errors.py 的输出）\n    \"\"\"\n    pairs = []\n    for task_id, task_trajs in group_by_task(trajectories):\n        chosen_trajs = [t for t in task_trajs if t[\"reward\"] == 1]\n        rejected_trajs = [t for t in task_trajs if t[\"reward\"] == 0]\n\n        if not chosen_trajs or not rejected_trajs:\n            continue\n\n        best_chosen = min(chosen_trajs, key=lambda t: t[\"num_steps\"])\n\n        for rej in rejected_trajs:\n            error_type = error_classifications.get(\n                f\"{task_id}_{rej['traj_id']}\", \"default\"\n            )\n            pairs.append({\n                \"id\": f\"{task_id}_pair_{len(pairs)}\",\n                \"error_type\": error_type,\n                \"prompt\": task_description(task_id),\n                \"chosen\": best_chosen[\"trajectory\"],\n                \"rejected\": rej[\"trajectory\"],\n                \"chosen_turns\": count_assistant_turns(best_chosen[\"trajectory\"]),\n                \"rejected_turns\": count_assistant_turns(rej[\"trajectory\"]),\n            })\n\n    return pairs\n```\n\n---\n\n## 6. 完整文件结构\n\n```\nrl-active-probe-fl/\n├── train_etadn.py              # 主训练入口\n│   - 解析 config.yaml\n│   - 加载模型 + LoRA + BnB 量化\n│   - 构建 dataset + collator\n│   - 初始化 ETADNTrainer\n│   - trainer.train()\n│\n├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）\n│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted\n│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns\n│   - DMPODataCollator: 注入 gamma、pad turn_ids\n│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)\n│\n├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合\n│   - compute_phi(t, T, gamma): 单值 φ 计算\n│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重\n│   - dmpo_weighted_logps(): per_token_logps → weighted scalar\n│\n├── data_utils.py               # 数据加载与预处理\n│   - load_preference_data(path): 加载 JSON pairs\n│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization\n│   - build_dataset(): HF Dataset 构建\n│\n├── config.yaml                 # 超参配置（见 §4.4）\n│\n├── collect_trajectories.py     # 轨迹收集（§5.1）\n│   - ALFWorld 环境交互\n│   - vLLM / transformers 推理\n│   - 输出 trajectories.jsonl\n│\n├── classify_errors.py          # 错误分类（§5.2）\n│   - Qwen3-14B-AWQ zero-shot\n│   - 输出 error_classifications.json\n│\n├── construct_preference.py     # Preference pair 构建（§5.3）\n│   - 输入: trajectories + error_classifications\n│   - 输出: preference_pairs.json\n│\n├── evaluate.py                 # ALFWorld 评估\n│   - 标准 eval protocol: 134 unseen tasks\n│   - 指标: success rate, average steps\n│   - 按 task type 分组报告\n│\n├── scripts/\n│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)\n│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)\n│\n└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）\n    ├── env_wrapper.py\n    └── task_configs/\n```\n\n### 6.1 关键模块依赖关系\n\n```\nconfig.yaml\n    ↓\ntrain_etadn.py\n    ├── data_utils.py → tokenize_multiturn()\n    ├── dmpo_trainer.py → ETADNTrainer\n    │       ├── dmpo_loss.py → compute_phi_weights()\n    │       └── DMPODataCollator → gamma injection\n    └── evaluate.py (训练结束后调用)\n\ncollect_trajectories.py → trajectories.jsonl\n    ↓\nclassify_errors.py → error_classifications.json\n    ↓\nconstruct_preference.py → preference_pairs.json\n    ↓\ntrain_etadn.py (读取 preference_pairs.json)\n```\n\n---\n\n## 7. Ablation 设计\n\n### 7.1 三种模式切换\n\n通过 `config.yaml` 中 `training.mode` 字段切换：\n\n| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |\n|---|---|---|---|\n| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |\n| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |\n| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |\n\n### 7.2 代码中的模式分支\n\n在 `ETADNTrainer._compute_loss` 中：\n\n```python\nif self.mode == \"dpo\":\n    # 标准 DPO: 直接 sum\n    logps = (per_token_logps * shift_completion_mask).sum(dim=1)\nelse:\n    # dmpo 或 etadn: φ-weighted sum\n    # gamma 已由 collator 注入到 batch[\"gamma\"]\n    token_phi = compute_phi_weights(\n        turn_ids=batch[\"turn_ids\"][:, 1:],  # shift 对齐\n        gamma=batch[\"gamma\"],\n        num_turns=batch[\"num_turns\"],\n        max_turns=batch[\"turn_ids\"].max().item() + 1,\n    )\n    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n```\n\n### 7.3 实验矩阵\n\n| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)\n\n### 7.4 评估指标\n\n| 指标 | 说明 |\n|---|---|\n| ALFWorld success rate (overall) | 主指标，134 unseen tasks |\n| Success rate per task type | 6 种 task type 的分项成功率 |\n| Average steps to success | 效率指标 |\n| Error type distribution shift | 训练前后的错误类型分布变化 |\n| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |\n| Training loss curve | 收敛性对比 |\n\n---\n\n## 8. ETADNTrainer 核心代码骨架\n\n```python\n# dmpo_trainer.py\n\nfrom trl import DPOTrainer, DPOConfig\nfrom dmpo_loss import compute_phi_weights\n\nclass ETADNConfig(DPOConfig):\n    mode: str = \"etadn\"          # \"dpo\" | \"dmpo\" | \"etadn\"\n    global_gamma: float = 0.90\n    gamma_e_mapping: dict = None  # {\"action\": 0.85, \"verify\": 0.92, \"plan\": 0.97}\n\n\nclass ETADNTrainer(DPOTrainer):\n\n    def __init__(self, *args, mode=\"etadn\", global_gamma=0.9, gamma_e_mapping=None, **kwargs):\n        super().__init__(*args, **kwargs)\n        self.mode = mode\n        self.global_gamma = global_gamma\n        self.gamma_e_mapping = gamma_e_mapping or {}\n\n    def _compute_loss(self, model, inputs, return_outputs=False):\n        \"\"\"Override: DMPO φ-weighted log probability aggregation.\"\"\"\n        # --- 1. 提取额外字段 ---\n        turn_ids = inputs.pop(\"turn_ids\", None)\n        num_turns = inputs.pop(\"num_turns\", None)\n        gamma = inputs.pop(\"gamma\", None)\n        completion_mask = inputs[\"completion_mask\"]\n        input_ids = inputs[\"input_ids\"]\n\n        # --- 2. Policy forward ---\n        model_kwargs = {k: v for k, v in inputs.items()\n                        if k not in (\"completion_mask\", \"ref_chosen_logps\", \"ref_rejected_logps\")}\n        outputs = model(**model_kwargs)\n\n        # --- 3. Per-token logps ---\n        from trl.trainer.utils import selective_log_softmax\n        shift_logits = outputs.logits[..., :-1, :].contiguous()\n        shift_labels = input_ids[..., 1:].contiguous()\n        shift_completion_mask = completion_mask[..., 1:].contiguous()\n        per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n        per_token_logps[shift_completion_mask == 0] = 0.0\n\n        # --- 4. 聚合（核心修改点） ---\n        if self.mode == \"dpo\" or turn_ids is None:\n            logps = per_token_logps.sum(dim=1)\n        else:\n            shift_turn_ids = turn_ids[..., 1:].contiguous()\n            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,\n                                            max_turns=shift_turn_ids.max().item() + 1)\n            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\n        chosen_logps, rejected_logps = logps.chunk(2, dim=0)\n\n        # --- 5. Reference logps ---\n        if \"ref_chosen_logps\" in inputs:\n            ref_chosen_logps = inputs[\"ref_chosen_logps\"]\n            ref_rejected_logps = inputs[\"ref_rejected_logps\"]\n        else:\n            with torch.no_grad():\n                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(\n                    model, inputs, shift_completion_mask,\n                    turn_ids=shift_turn_ids if self.mode != \"dpo\" else None,\n                    gamma=gamma, num_turns=num_turns,\n                )\n\n        # --- 6. Loss (sigmoid, same as standard DPO) ---\n        chosen_logratios = chosen_logps - ref_chosen_logps\n        rejected_logratios = rejected_logps - ref_rejected_logps\n        logits = chosen_logratios - rejected_logratios\n\n        loss = -F.logsigmoid(self.beta * logits).mean()\n\n        # --- 7. Metrics ---\n        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()\n        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()\n        reward_margin = (chosen_rewards - rejected_rewards).mean()\n\n        metrics = {\n            \"loss\": loss.detach().item(),\n            \"rewards/chosen\": chosen_rewards.mean().item(),\n            \"rewards/rejected\": rejected_rewards.mean().item(),\n            \"rewards/margin\": reward_margin.item(),\n        }\n        self.store_metrics(metrics, train_eval=\"train\")\n\n        if return_outputs:\n            return loss, {\"logits\": logits}\n        return loss\n```\n\n---\n\n## 9. 风险与注意事项\n\n| 风险 | 缓解 |\n|---|---|\n| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |\n| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |\n| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |\n| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |\n| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |\n\n---\n\n## 10. 实施优先级\n\n| Phase | 内容 | 估计时间 |\n|---|---|---|\n| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |\n| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |\n| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |\n| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |\n| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |\n| P6 | 完整训练 + 评估 | 2-3 天 |\n",
    "structuredPatch": [
      {
        "oldStart": 838,
        "oldLines": 7,
        "newStart": 838,
        "newLines": 7,
        "lines": [
          " ",
          " | 风险 | 缓解 |",
          " |---|---|",
          "-| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |",
          "+| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |",
          " | trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |",
          " | Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |",
          " | φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |"
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

_source line 15_

Now add the trl version section and φ normalization verification section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "1f1cc4b7-e566-45de-8768-e680b942c8aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ83xoS7J5Zbg4bNeYPzUx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 40561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 408
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01XBwVSSanw4KV8RY6CCkfv7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |",
  "new_string": "| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "0c2ee0e6-df00-4bb6-acf5-456cbdaeda3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ83xoS7J5Zbg4bNeYPzUx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 40561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 408
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T11:01:15.898Z_

<details><summary>↩ Tool result · `toolu_01XBwVSSanw4KV8RY6CCkfv7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "b4609b2a-1c0c-4f1c-9c39-a49dcce05995",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "oldString": "| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |",
    "newString": "| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |",
    "originalFile": "# DMPO + ETADN 训练 Pipeline 设计（v2）\n\n## 0. 术语与背景\n\n**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。\n\n**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。\n\n**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。\n\n---\n\n## 1. DMPO Loss 实现方案\n\n### 1.1 完整 DMPO Loss 公式\n\n标准 DPO loss（单轮）：\n\n```\nL_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]\n```\n\nDMPO loss（多轮，论文 Eq.16）：\n\n```\nL_DMPO = -E[ log σ(\n    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]\n  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]\n)]\n```\n\n其中时间折扣函数：\n\n```\nφ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n```\n\n- t = turn index (0-indexed)\n- T = 总 turn 数\n- γ ∈ (0, 1) = 时间折扣因子\n- φ(t, T) 单调递减：早期 turn 权重更高\n\n**特殊情况**：\n- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO\n- γ = 1: φ(t,T) = (T-t)/T → 线性衰减\n\n### 1.2 在 trl DPOTrainer 上实现 DMPO\n\n**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。\n\n**需要修改的核心逻辑**（在 `_compute_loss` 内）：\n\n| 原始 trl 行为 | DMPO 修改 |\n|---|---|\n| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |\n| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |\n| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |\n\n**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。\n\n### 1.3 Per-turn log probability 计算\n\nALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。\n\n**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：\n\n```\ntoken:    [&lt;prompt> | Think... Act... | Think... Act... | Think... Act... ]\nturn_ids: [   -1    |       0        |        1        |        2        ]\n```\n\n**加权聚合伪代码**：\n\n```python\ndef dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):\n    \"\"\"\n    per_token_logps: [batch, seq_len]\n    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)\n    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)\n    gamma:           [batch]           (per-sample γ)\n    num_turns:       [batch]           (per-sample T)\n    Returns:         [batch]           (weighted log probability per sample)\n    \"\"\"\n    # 构建 per-token φ 权重\n    token_weights = torch.zeros_like(per_token_logps)\n    for t in range(turn_ids.max() + 1):\n        mask_t = (turn_ids == t)  # [batch, seq_len]\n        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)\n        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]\n\n    return (per_token_logps * completion_mask * token_weights).sum(dim=1)\n```\n\n**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：\n\n```python\ndef compute_phi_weights(turn_ids, gamma, num_turns, max_turns):\n    \"\"\"全向量化 φ 权重计算\"\"\"\n    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]\n    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]\n    T = num_turns.unsqueeze(1).float()                            # [batch, 1]\n\n    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)\n    # phi: [batch, max_turns]\n\n    # 用 turn_ids gather 到 per-token 权重\n    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零\n    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]\n    return token_phi\n```\n\n### 1.4 φ(t,T) 权重应用到 per-turn loss\n\n在 `_compute_loss` 中，替换聚合步骤：\n\n```python\n# === 原始 trl ===\n# logps = per_token_logps.sum(dim=1)\n\n# === DMPO 修改 ===\ntoken_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)\nlogps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\nchosen_logps, rejected_logps = logps.chunk(2, dim=0)\n# 后续 log ratio、sigmoid loss 与标准 DPO 相同\n```\n\n---\n\n## 2. γ_e 注入方案\n\n### 2.1 Error Type → γ_e 映射\n\n```yaml\n# config.yaml\ngamma_e_mapping:\n  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步\n  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列\n  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹\n  default: 0.90   # 未分类 fallback\n```\n\n**直觉**：\n- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）\n- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）\n\n### 2.2 注入流程\n\n```\n数据加载 → 每个样本有 error_type 字段\n       ↓\nDataCollator → 查表得到 gamma_per_sample: [batch_size]\n       ↓\n_compute_loss → gamma_per_sample 传入 compute_phi_weights()\n       ↓\nper-token 权重 → 加权聚合 → 标准 sigmoid loss\n```\n\n**Collator 中的 γ 注入**：\n\n```python\nclass DMPODataCollator(DataCollatorForPreference):\n    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):\n        super().__init__(**kwargs)\n        self.gamma_map = gamma_map\n        self.mode = mode\n        self.global_gamma = global_gamma\n\n    def __call__(self, features):\n        batch = super().__call__(features)\n\n        # 收集 error_type → gamma\n        gammas = []\n        for f in features:\n            if self.mode == \"etadn\":\n                et = f.get(\"error_type\", \"default\")\n                gammas.append(self.gamma_map.get(et, self.gamma_map[\"default\"]))\n            elif self.mode == \"dmpo\":\n                gammas.append(self.global_gamma)\n            else:  # dpo\n                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权\n\n        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）\n        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)\n        gamma_rejected = gamma_chosen.clone()\n        batch[\"gamma\"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)\n\n        return batch\n```\n\n### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e\n\n| 维度 | DMPO | ETADN |\n|---|---|---|\n| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |\n| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |\n| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |\n| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |\n\n---\n\n## 3. 数据 Pipeline\n\n### 3.1 DPO 数据格式\n\n每个样本包含：\n\n```json\n{\n  \"id\": \"alfworld_task_42_pair_0\",\n  \"error_type\": \"action\",\n  \"prompt\": \"You are in a kitchen. Your task is to ...\",\n  \"chosen\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: I should open it. Act: open fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You open the fridge. You see a tomato 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Found it. Act: take tomato 1 from fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You pick up the tomato 1.\"}\n  ],\n  \"rejected\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to countertop 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a bread 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Not here. Act: go to countertop 2\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a cup 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Maybe in the cabinet. Act: go to cabinet 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The cabinet is closed.\"}\n  ],\n  \"chosen_turns\": 3,\n  \"rejected_turns\": 3\n}\n```\n\n### 3.2 多轮对话处理：Turn 定义\n\nALFWorld 轨迹中每个 turn 的结构：\n\n```\nTurn t:\n  Assistant: \"Think: &lt;reasoning>. Act: &lt;action>\"    ← agent 生成\n  User:      \"Obs: &lt;environment_observation>\"        ← 环境返回\n```\n\n**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。\n\nTurn 数 T = assistant 回复的数量。\n\n### 3.3 Tokenization 与 Turn 标记\n\n```python\ndef tokenize_multiturn(example, tokenizer, max_length):\n    \"\"\"将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids\"\"\"\n    # 1. 构建完整对话（chat template）\n    messages = [{\"role\": \"system\", \"content\": example[\"prompt\"]}]\n    messages += example[\"chosen\"]  # 或 rejected\n\n    # 2. 分步 tokenize 以获取 turn 边界\n    prompt_ids = tokenizer.apply_chat_template(\n        [messages[0]], tokenize=True, add_generation_prompt=True\n    )\n\n    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1\n    completion_mask = [0] * len(prompt_ids)\n    all_ids = list(prompt_ids)\n    current_turn = 0\n\n    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs\n        # assistant 部分\n        asst_msg = messages[i]\n        asst_ids = tokenizer.encode(asst_msg[\"content\"], add_special_tokens=False)\n        # + chat template 的 role tokens\n        role_ids = tokenizer.encode(\"<|im_start|>assistant\\n\", add_special_tokens=False)\n        end_ids = tokenizer.encode(\"<|im_end|>\\n\", add_special_tokens=False)\n\n        all_ids += role_ids\n        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss\n        completion_mask += [0] * len(role_ids)\n\n        all_ids += asst_ids\n        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t\n        completion_mask += [1] * len(asst_ids)\n\n        all_ids += end_ids\n        turn_ids += [current_turn] * len(end_ids)\n        completion_mask += [1] * len(end_ids)\n\n        # user/observation 部分\n        if i + 1 < len(messages):\n            user_msg = messages[i + 1]\n            user_ids = tokenizer.encode(\n                f\"<|im_start|>user\\n{user_msg['content']}<|im_end|>\\n\",\n                add_special_tokens=False\n            )\n            all_ids += user_ids\n            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss\n            completion_mask += [0] * len(user_ids)\n\n        current_turn += 1\n\n    # 3. 截断\n    all_ids = all_ids[:max_length]\n    turn_ids = turn_ids[:max_length]\n    completion_mask = completion_mask[:max_length]\n\n    return {\n        \"input_ids\": all_ids,\n        \"turn_ids\": turn_ids,\n        \"completion_mask\": completion_mask,\n        \"num_turns\": current_turn,\n    }\n```\n\n**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。\n\n### 3.4 数据集统计预估\n\n| 维度 | 估计值 |\n|---|---|\n| ALFWorld 任务数 | ~3,500 (train split) |\n| 每任务轨迹数 | 5-10（采样多条） |\n| 有效 preference pairs | ~2,000-5,000（过滤后） |\n| 平均 turn 数 T | 5-15 |\n| 平均序列长度 | 1,500-3,000 tokens |\n\n---\n\n## 4. 模型配置\n\n### 4.1 Qwen3-8B QLoRA 配置\n\n```python\nfrom transformers import AutoModelForCausalLM, BitsAndBytesConfig\nfrom peft import LoraConfig\n\nbnb_config = BitsAndBytesConfig(\n    load_in_4bit=True,\n    bnb_4bit_quant_type=\"nf4\",\n    bnb_4bit_compute_dtype=torch.bfloat16,\n    bnb_4bit_use_double_quant=True,\n)\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    \"Qwen/Qwen3-8B\",\n    quantization_config=bnb_config,\n    torch_dtype=torch.bfloat16,\n    attn_implementation=\"flash_attention_2\",\n    device_map={\"\": device_id},  # 单卡绑定\n)\n\nlora_config = LoraConfig(\n    r=64,\n    lora_alpha=128,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                     \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_dropout=0.05,\n    task_type=\"CAUSAL_LM\",\n    bias=\"none\",\n)\n```\n\n### 4.2 Ref Model 处理\n\nQLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。\n\ntrl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确\n\n### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）\n\n| 组件 | 估计 VRAM |\n|---|---|\n| Qwen3-8B 4-bit weights | ~4.5 GB |\n| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |\n| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |\n| Gradients (bf16) | ~0.4 GB |\n| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |\n| PyTorch + CUDA overhead | ~2 GB |\n| **总计** | **~15-17 GB** |\n\n剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。\n\n**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。\n\n### 4.4 训练超参\n\n```yaml\n# config.yaml\ntraining:\n  mode: \"etadn\"            # \"dpo\" | \"dmpo\" | \"etadn\"\n  beta: 0.1                # DPO β\n  global_gamma: 0.90       # DMPO 模式下的全局 γ\n  learning_rate: 1.0e-6\n  lr_scheduler_type: \"constant_with_warmup\"\n  warmup_ratio: 0.1\n  num_train_epochs: 3\n  per_device_train_batch_size: 1\n  gradient_accumulation_steps: 16\n  gradient_checkpointing: true\n  bf16: true\n  max_length: 3072\n  max_prompt_length: 512\n  logging_steps: 5\n  save_steps: 100\n  eval_steps: 50\n  precompute_ref_log_probs: true\n  label_smoothing: 0.0\n  loss_type: \"sigmoid\"\n\nlora:\n  r: 64\n  lora_alpha: 128\n  target_modules: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n  lora_dropout: 0.05\n\ngamma_e_mapping:\n  action: 0.85\n  verify: 0.92\n  plan: 0.97\n  default: 0.90\n```\n\n---\n\n## 5. 推理 Pipeline\n\n### 5.1 轨迹收集\n\n```python\n# collect_trajectories.py\n# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互\n# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）\n\nfrom vllm import LLM, SamplingParams  # 或 transformers.generate\n\nmodel = LLM(\n    model=\"path/to/qwen3-8b-merged\",  # LoRA merge 后的 checkpoint\n    tensor_parallel_size=1,\n    gpu_memory_utilization=0.85,\n    max_model_len=4096,\n)\n\nparams = SamplingParams(\n    temperature=0.7,\n    top_p=0.9,\n    max_tokens=256,      # 每步生成上限\n    stop=[\"Obs:\"],       # ALFWorld 环境会返回 Obs\n)\n\n# 循环：generate → parse action → env.step → append obs → repeat\n```\n\n**输出格式**：\n\n```json\n{\n  \"task_id\": \"pick_clean_then_place-Tomato-...\",\n  \"trajectory\": [\n    {\"role\": \"assistant\", \"content\": \"Think: ... Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    ...\n  ],\n  \"reward\": 1,           # ALFWorld: 1=成功, 0=失败\n  \"num_steps\": 8,\n  \"task_type\": \"pick_clean_then_place\"\n}\n```\n\n### 5.2 错误分类\n\n```python\n# classify_errors.py\n# 用 Qwen3-14B-AWQ 做 zero-shot 分类\n\nCLASSIFY_PROMPT = \"\"\"Analyze the following failed trajectory in ALFWorld.\nThe agent attempted a task but failed. Identify the PRIMARY error type:\n\n- action: Wrong physical action (e.g., went to wrong location, used wrong object)\n- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)\n- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)\n\nTask: {task_description}\nSuccessful trajectory: {chosen_trajectory}\nFailed trajectory: {rejected_trajectory}\n\nRespond with ONLY one word: action, verify, or plan\"\"\"\n\n# 输出: error_type ∈ {\"action\", \"verify\", \"plan\"}\n```\n\n### 5.3 Preference Pair 构建\n\n```python\n# construct_preference.py\n\ndef construct_pairs(trajectories, error_classifications):\n    \"\"\"\n    策略：\n    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected\n    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs\n    3. 附加 error_type 标签（来自 classify_errors.py 的输出）\n    \"\"\"\n    pairs = []\n    for task_id, task_trajs in group_by_task(trajectories):\n        chosen_trajs = [t for t in task_trajs if t[\"reward\"] == 1]\n        rejected_trajs = [t for t in task_trajs if t[\"reward\"] == 0]\n\n        if not chosen_trajs or not rejected_trajs:\n            continue\n\n        best_chosen = min(chosen_trajs, key=lambda t: t[\"num_steps\"])\n\n        for rej in rejected_trajs:\n            error_type = error_classifications.get(\n                f\"{task_id}_{rej['traj_id']}\", \"default\"\n            )\n            pairs.append({\n                \"id\": f\"{task_id}_pair_{len(pairs)}\",\n                \"error_type\": error_type,\n                \"prompt\": task_description(task_id),\n                \"chosen\": best_chosen[\"trajectory\"],\n                \"rejected\": rej[\"trajectory\"],\n                \"chosen_turns\": count_assistant_turns(best_chosen[\"trajectory\"]),\n                \"rejected_turns\": count_assistant_turns(rej[\"trajectory\"]),\n            })\n\n    return pairs\n```\n\n---\n\n## 6. 完整文件结构\n\n```\nrl-active-probe-fl/\n├── train_etadn.py              # 主训练入口\n│   - 解析 config.yaml\n│   - 加载模型 + LoRA + BnB 量化\n│   - 构建 dataset + collator\n│   - 初始化 ETADNTrainer\n│   - trainer.train()\n│\n├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）\n│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted\n│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns\n│   - DMPODataCollator: 注入 gamma、pad turn_ids\n│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)\n│\n├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合\n│   - compute_phi(t, T, gamma): 单值 φ 计算\n│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重\n│   - dmpo_weighted_logps(): per_token_logps → weighted scalar\n│\n├── data_utils.py               # 数据加载与预处理\n│   - load_preference_data(path): 加载 JSON pairs\n│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization\n│   - build_dataset(): HF Dataset 构建\n│\n├── config.yaml                 # 超参配置（见 §4.4）\n│\n├── collect_trajectories.py     # 轨迹收集（§5.1）\n│   - ALFWorld 环境交互\n│   - vLLM / transformers 推理\n│   - 输出 trajectories.jsonl\n│\n├── classify_errors.py          # 错误分类（§5.2）\n│   - Qwen3-14B-AWQ zero-shot\n│   - 输出 error_classifications.json\n│\n├── construct_preference.py     # Preference pair 构建（§5.3）\n│   - 输入: trajectories + error_classifications\n│   - 输出: preference_pairs.json\n│\n├── evaluate.py                 # ALFWorld 评估\n│   - 标准 eval protocol: 134 unseen tasks\n│   - 指标: success rate, average steps\n│   - 按 task type 分组报告\n│\n├── scripts/\n│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)\n│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)\n│\n└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）\n    ├── env_wrapper.py\n    └── task_configs/\n```\n\n### 6.1 关键模块依赖关系\n\n```\nconfig.yaml\n    ↓\ntrain_etadn.py\n    ├── data_utils.py → tokenize_multiturn()\n    ├── dmpo_trainer.py → ETADNTrainer\n    │       ├── dmpo_loss.py → compute_phi_weights()\n    │       └── DMPODataCollator → gamma injection\n    └── evaluate.py (训练结束后调用)\n\ncollect_trajectories.py → trajectories.jsonl\n    ↓\nclassify_errors.py → error_classifications.json\n    ↓\nconstruct_preference.py → preference_pairs.json\n    ↓\ntrain_etadn.py (读取 preference_pairs.json)\n```\n\n---\n\n## 7. Ablation 设计\n\n### 7.1 三种模式切换\n\n通过 `config.yaml` 中 `training.mode` 字段切换：\n\n| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |\n|---|---|---|---|\n| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |\n| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |\n| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |\n\n### 7.2 代码中的模式分支\n\n在 `ETADNTrainer._compute_loss` 中：\n\n```python\nif self.mode == \"dpo\":\n    # 标准 DPO: 直接 sum\n    logps = (per_token_logps * shift_completion_mask).sum(dim=1)\nelse:\n    # dmpo 或 etadn: φ-weighted sum\n    # gamma 已由 collator 注入到 batch[\"gamma\"]\n    token_phi = compute_phi_weights(\n        turn_ids=batch[\"turn_ids\"][:, 1:],  # shift 对齐\n        gamma=batch[\"gamma\"],\n        num_turns=batch[\"num_turns\"],\n        max_turns=batch[\"turn_ids\"].max().item() + 1,\n    )\n    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n```\n\n### 7.3 实验矩阵\n\n| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)\n\n### 7.4 评估指标\n\n| 指标 | 说明 |\n|---|---|\n| ALFWorld success rate (overall) | 主指标，134 unseen tasks |\n| Success rate per task type | 6 种 task type 的分项成功率 |\n| Average steps to success | 效率指标 |\n| Error type distribution shift | 训练前后的错误类型分布变化 |\n| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |\n| Training loss curve | 收敛性对比 |\n\n---\n\n## 8. ETADNTrainer 核心代码骨架\n\n```python\n# dmpo_trainer.py\n\nfrom trl import DPOTrainer, DPOConfig\nfrom dmpo_loss import compute_phi_weights\n\nclass ETADNConfig(DPOConfig):\n    mode: str = \"etadn\"          # \"dpo\" | \"dmpo\" | \"etadn\"\n    global_gamma: float = 0.90\n    gamma_e_mapping: dict = None  # {\"action\": 0.85, \"verify\": 0.92, \"plan\": 0.97}\n\n\nclass ETADNTrainer(DPOTrainer):\n\n    def __init__(self, *args, mode=\"etadn\", global_gamma=0.9, gamma_e_mapping=None, **kwargs):\n        super().__init__(*args, **kwargs)\n        self.mode = mode\n        self.global_gamma = global_gamma\n        self.gamma_e_mapping = gamma_e_mapping or {}\n\n    def _compute_loss(self, model, inputs, return_outputs=False):\n        \"\"\"Override: DMPO φ-weighted log probability aggregation.\"\"\"\n        # --- 1. 提取额外字段 ---\n        turn_ids = inputs.pop(\"turn_ids\", None)\n        num_turns = inputs.pop(\"num_turns\", None)\n        gamma = inputs.pop(\"gamma\", None)\n        completion_mask = inputs[\"completion_mask\"]\n        input_ids = inputs[\"input_ids\"]\n\n        # --- 2. Policy forward ---\n        model_kwargs = {k: v for k, v in inputs.items()\n                        if k not in (\"completion_mask\", \"ref_chosen_logps\", \"ref_rejected_logps\")}\n        outputs = model(**model_kwargs)\n\n        # --- 3. Per-token logps ---\n        from trl.trainer.utils import selective_log_softmax\n        shift_logits = outputs.logits[..., :-1, :].contiguous()\n        shift_labels = input_ids[..., 1:].contiguous()\n        shift_completion_mask = completion_mask[..., 1:].contiguous()\n        per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n        per_token_logps[shift_completion_mask == 0] = 0.0\n\n        # --- 4. 聚合（核心修改点） ---\n        if self.mode == \"dpo\" or turn_ids is None:\n            logps = per_token_logps.sum(dim=1)\n        else:\n            shift_turn_ids = turn_ids[..., 1:].contiguous()\n            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,\n                                            max_turns=shift_turn_ids.max().item() + 1)\n            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\n        chosen_logps, rejected_logps = logps.chunk(2, dim=0)\n\n        # --- 5. Reference logps ---\n        if \"ref_chosen_logps\" in inputs:\n            ref_chosen_logps = inputs[\"ref_chosen_logps\"]\n            ref_rejected_logps = inputs[\"ref_rejected_logps\"]\n        else:\n            with torch.no_grad():\n                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(\n                    model, inputs, shift_completion_mask,\n                    turn_ids=shift_turn_ids if self.mode != \"dpo\" else None,\n                    gamma=gamma, num_turns=num_turns,\n                )\n\n        # --- 6. Loss (sigmoid, same as standard DPO) ---\n        chosen_logratios = chosen_logps - ref_chosen_logps\n        rejected_logratios = rejected_logps - ref_rejected_logps\n        logits = chosen_logratios - rejected_logratios\n\n        loss = -F.logsigmoid(self.beta * logits).mean()\n\n        # --- 7. Metrics ---\n        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()\n        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()\n        reward_margin = (chosen_rewards - rejected_rewards).mean()\n\n        metrics = {\n            \"loss\": loss.detach().item(),\n            \"rewards/chosen\": chosen_rewards.mean().item(),\n            \"rewards/rejected\": rejected_rewards.mean().item(),\n            \"rewards/margin\": reward_margin.item(),\n        }\n        self.store_metrics(metrics, train_eval=\"train\")\n\n        if return_outputs:\n            return loss, {\"logits\": logits}\n        return loss\n```\n\n---\n\n## 9. 风险与注意事项\n\n| 风险 | 缓解 |\n|---|---|\n| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |\n| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |\n| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |\n| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |\n| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |\n\n---\n\n## 10. 实施优先级\n\n| Phase | 内容 | 估计时间 |\n|---|---|---|\n| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |\n| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |\n| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |\n| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |\n| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |\n| P6 | 完整训练 + 评估 | 2-3 天 |\n",
    "structuredPatch": [
      {
        "oldStart": 839,
        "oldLines": 7,
        "newStart": 839,
        "newLines": 7,
        "lines": [
          " | 风险 | 缓解 |",
          " |---|---|",
          " | `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |",
          "-| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |",
          "+| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |",
          " | Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |",
          " | φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |",
          " | γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |"
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01YN924EUCf2eRSDqkzXSJLP`</summary>

````json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "---\n\n## 5. 推理 Pipeline",
  "new_string": "### 4.5 环境依赖\n\n| 包 | 要求版本 | 说明 |\n|---|---|---|\n| `trl` | **`==1.4.0`** | 必须使用此版本。1.4.0 将旧版 `get_batch_loss_metrics` / `concatenated_forward` / `get_batch_logps` 合并为 `_compute_loss`，本设计基于此 API 结构。服务器现有 1.1.0 需升级。 |\n| `transformers` | `>=4.40.0` | Qwen3 支持 |\n| `peft` | `>=0.10.0` | LoRA + BnB 集成 |\n| `bitsandbytes` | `>=0.43.0` | nf4 量化 |\n| `torch` | `>=2.1` | bf16 + flash_attention_2 |\n| `flash-attn` | `>=2.5.0` | Flash Attention 2 |\n\n**trl 1.4.0 中本设计依赖的关键 API**：\n- `DPOTrainer._compute_loss(model, inputs, return_outputs)` — 唯一的 loss 扩展点\n- `trl.trainer.utils.selective_log_softmax(logits, labels)` — per-token log prob 计算\n- `DPOConfig` — 训练配置基类\n\n**升级命令**：\n```bash\npip install trl==1.4.0\n```\n\n---\n\n## 5. 推理 Pipeline"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "ed1a0fb7-df0e-4198-8442-c0bdaa606565",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7sSnmkz2geipSmEhJHYp3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 380,
      "cache_read_input_tokens": 40969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 380
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T11:01:26.622Z_

<details><summary>↩ Tool result · `toolu_01YN924EUCf2eRSDqkzXSJLP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "8cb5e218-843e-4073-a029-72314e8c1e97",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "oldString": "---\n\n## 5. 推理 Pipeline",
    "newString": "### 4.5 环境依赖\n\n| 包 | 要求版本 | 说明 |\n|---|---|---|\n| `trl` | **`==1.4.0`** | 必须使用此版本。1.4.0 将旧版 `get_batch_loss_metrics` / `concatenated_forward` / `get_batch_logps` 合并为 `_compute_loss`，本设计基于此 API 结构。服务器现有 1.1.0 需升级。 |\n| `transformers` | `>=4.40.0` | Qwen3 支持 |\n| `peft` | `>=0.10.0` | LoRA + BnB 集成 |\n| `bitsandbytes` | `>=0.43.0` | nf4 量化 |\n| `torch` | `>=2.1` | bf16 + flash_attention_2 |\n| `flash-attn` | `>=2.5.0` | Flash Attention 2 |\n\n**trl 1.4.0 中本设计依赖的关键 API**：\n- `DPOTrainer._compute_loss(model, inputs, return_outputs)` — 唯一的 loss 扩展点\n- `trl.trainer.utils.selective_log_softmax(logits, labels)` — per-token log prob 计算\n- `DPOConfig` — 训练配置基类\n\n**升级命令**：\n```bash\npip install trl==1.4.0\n```\n\n---\n\n## 5. 推理 Pipeline",
    "originalFile": "# DMPO + ETADN 训练 Pipeline 设计（v2）\n\n## 0. 术语与背景\n\n**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。\n\n**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。\n\n**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。\n\n---\n\n## 1. DMPO Loss 实现方案\n\n### 1.1 完整 DMPO Loss 公式\n\n标准 DPO loss（单轮）：\n\n```\nL_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]\n```\n\nDMPO loss（多轮，论文 Eq.16）：\n\n```\nL_DMPO = -E[ log σ(\n    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]\n  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]\n)]\n```\n\n其中时间折扣函数：\n\n```\nφ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n```\n\n- t = turn index (0-indexed)\n- T = 总 turn 数\n- γ ∈ (0, 1) = 时间折扣因子\n- φ(t, T) 单调递减：早期 turn 权重更高\n\n**特殊情况**：\n- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO\n- γ = 1: φ(t,T) = (T-t)/T → 线性衰减\n\n### 1.2 在 trl DPOTrainer 上实现 DMPO\n\n**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。\n\n**需要修改的核心逻辑**（在 `_compute_loss` 内）：\n\n| 原始 trl 行为 | DMPO 修改 |\n|---|---|\n| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |\n| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |\n| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |\n\n**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。\n\n### 1.3 Per-turn log probability 计算\n\nALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。\n\n**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：\n\n```\ntoken:    [&lt;prompt> | Think... Act... | Think... Act... | Think... Act... ]\nturn_ids: [   -1    |       0        |        1        |        2        ]\n```\n\n**加权聚合伪代码**：\n\n```python\ndef dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):\n    \"\"\"\n    per_token_logps: [batch, seq_len]\n    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)\n    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)\n    gamma:           [batch]           (per-sample γ)\n    num_turns:       [batch]           (per-sample T)\n    Returns:         [batch]           (weighted log probability per sample)\n    \"\"\"\n    # 构建 per-token φ 权重\n    token_weights = torch.zeros_like(per_token_logps)\n    for t in range(turn_ids.max() + 1):\n        mask_t = (turn_ids == t)  # [batch, seq_len]\n        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)\n        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]\n\n    return (per_token_logps * completion_mask * token_weights).sum(dim=1)\n```\n\n**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：\n\n```python\ndef compute_phi_weights(turn_ids, gamma, num_turns, max_turns):\n    \"\"\"全向量化 φ 权重计算\"\"\"\n    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]\n    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]\n    T = num_turns.unsqueeze(1).float()                            # [batch, 1]\n\n    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)\n    # phi: [batch, max_turns]\n\n    # 用 turn_ids gather 到 per-token 权重\n    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零\n    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]\n    return token_phi\n```\n\n### 1.4 φ(t,T) 权重应用到 per-turn loss\n\n在 `_compute_loss` 中，替换聚合步骤：\n\n```python\n# === 原始 trl ===\n# logps = per_token_logps.sum(dim=1)\n\n# === DMPO 修改 ===\ntoken_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)\nlogps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\nchosen_logps, rejected_logps = logps.chunk(2, dim=0)\n# 后续 log ratio、sigmoid loss 与标准 DPO 相同\n```\n\n---\n\n## 2. γ_e 注入方案\n\n### 2.1 Error Type → γ_e 映射\n\n```yaml\n# config.yaml\ngamma_e_mapping:\n  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步\n  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列\n  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹\n  default: 0.90   # 未分类 fallback\n```\n\n**直觉**：\n- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）\n- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）\n\n### 2.2 注入流程\n\n```\n数据加载 → 每个样本有 error_type 字段\n       ↓\nDataCollator → 查表得到 gamma_per_sample: [batch_size]\n       ↓\n_compute_loss → gamma_per_sample 传入 compute_phi_weights()\n       ↓\nper-token 权重 → 加权聚合 → 标准 sigmoid loss\n```\n\n**Collator 中的 γ 注入**：\n\n```python\nclass DMPODataCollator(DataCollatorForPreference):\n    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):\n        super().__init__(**kwargs)\n        self.gamma_map = gamma_map\n        self.mode = mode\n        self.global_gamma = global_gamma\n\n    def __call__(self, features):\n        batch = super().__call__(features)\n\n        # 收集 error_type → gamma\n        gammas = []\n        for f in features:\n            if self.mode == \"etadn\":\n                et = f.get(\"error_type\", \"default\")\n                gammas.append(self.gamma_map.get(et, self.gamma_map[\"default\"]))\n            elif self.mode == \"dmpo\":\n                gammas.append(self.global_gamma)\n            else:  # dpo\n                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权\n\n        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）\n        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)\n        gamma_rejected = gamma_chosen.clone()\n        batch[\"gamma\"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)\n\n        return batch\n```\n\n### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e\n\n| 维度 | DMPO | ETADN |\n|---|---|---|\n| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |\n| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |\n| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |\n| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |\n\n---\n\n## 3. 数据 Pipeline\n\n### 3.1 DPO 数据格式\n\n每个样本包含：\n\n```json\n{\n  \"id\": \"alfworld_task_42_pair_0\",\n  \"error_type\": \"action\",\n  \"prompt\": \"You are in a kitchen. Your task is to ...\",\n  \"chosen\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: I should open it. Act: open fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You open the fridge. You see a tomato 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Found it. Act: take tomato 1 from fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You pick up the tomato 1.\"}\n  ],\n  \"rejected\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to countertop 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a bread 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Not here. Act: go to countertop 2\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a cup 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Maybe in the cabinet. Act: go to cabinet 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The cabinet is closed.\"}\n  ],\n  \"chosen_turns\": 3,\n  \"rejected_turns\": 3\n}\n```\n\n### 3.2 多轮对话处理：Turn 定义\n\nALFWorld 轨迹中每个 turn 的结构：\n\n```\nTurn t:\n  Assistant: \"Think: &lt;reasoning>. Act: &lt;action>\"    ← agent 生成\n  User:      \"Obs: &lt;environment_observation>\"        ← 环境返回\n```\n\n**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。\n\nTurn 数 T = assistant 回复的数量。\n\n### 3.3 Tokenization 与 Turn 标记\n\n```python\ndef tokenize_multiturn(example, tokenizer, max_length):\n    \"\"\"将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids\"\"\"\n    # 1. 构建完整对话（chat template）\n    messages = [{\"role\": \"system\", \"content\": example[\"prompt\"]}]\n    messages += example[\"chosen\"]  # 或 rejected\n\n    # 2. 分步 tokenize 以获取 turn 边界\n    prompt_ids = tokenizer.apply_chat_template(\n        [messages[0]], tokenize=True, add_generation_prompt=True\n    )\n\n    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1\n    completion_mask = [0] * len(prompt_ids)\n    all_ids = list(prompt_ids)\n    current_turn = 0\n\n    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs\n        # assistant 部分\n        asst_msg = messages[i]\n        asst_ids = tokenizer.encode(asst_msg[\"content\"], add_special_tokens=False)\n        # + chat template 的 role tokens\n        role_ids = tokenizer.encode(\"<|im_start|>assistant\\n\", add_special_tokens=False)\n        end_ids = tokenizer.encode(\"<|im_end|>\\n\", add_special_tokens=False)\n\n        all_ids += role_ids\n        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss\n        completion_mask += [0] * len(role_ids)\n\n        all_ids += asst_ids\n        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t\n        completion_mask += [1] * len(asst_ids)\n\n        all_ids += end_ids\n        turn_ids += [current_turn] * len(end_ids)\n        completion_mask += [1] * len(end_ids)\n\n        # user/observation 部分\n        if i + 1 < len(messages):\n            user_msg = messages[i + 1]\n            user_ids = tokenizer.encode(\n                f\"<|im_start|>user\\n{user_msg['content']}<|im_end|>\\n\",\n                add_special_tokens=False\n            )\n            all_ids += user_ids\n            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss\n            completion_mask += [0] * len(user_ids)\n\n        current_turn += 1\n\n    # 3. 截断\n    all_ids = all_ids[:max_length]\n    turn_ids = turn_ids[:max_length]\n    completion_mask = completion_mask[:max_length]\n\n    return {\n        \"input_ids\": all_ids,\n        \"turn_ids\": turn_ids,\n        \"completion_mask\": completion_mask,\n        \"num_turns\": current_turn,\n    }\n```\n\n**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。\n\n### 3.4 数据集统计预估\n\n| 维度 | 估计值 |\n|---|---|\n| ALFWorld 任务数 | ~3,500 (train split) |\n| 每任务轨迹数 | 5-10（采样多条） |\n| 有效 preference pairs | ~2,000-5,000（过滤后） |\n| 平均 turn 数 T | 5-15 |\n| 平均序列长度 | 1,500-3,000 tokens |\n\n---\n\n## 4. 模型配置\n\n### 4.1 Qwen3-8B QLoRA 配置\n\n```python\nfrom transformers import AutoModelForCausalLM, BitsAndBytesConfig\nfrom peft import LoraConfig\n\nbnb_config = BitsAndBytesConfig(\n    load_in_4bit=True,\n    bnb_4bit_quant_type=\"nf4\",\n    bnb_4bit_compute_dtype=torch.bfloat16,\n    bnb_4bit_use_double_quant=True,\n)\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    \"Qwen/Qwen3-8B\",\n    quantization_config=bnb_config,\n    torch_dtype=torch.bfloat16,\n    attn_implementation=\"flash_attention_2\",\n    device_map={\"\": device_id},  # 单卡绑定\n)\n\nlora_config = LoraConfig(\n    r=64,\n    lora_alpha=128,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                     \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_dropout=0.05,\n    task_type=\"CAUSAL_LM\",\n    bias=\"none\",\n)\n```\n\n### 4.2 Ref Model 处理\n\nQLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。\n\ntrl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确\n\n### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）\n\n| 组件 | 估计 VRAM |\n|---|---|\n| Qwen3-8B 4-bit weights | ~4.5 GB |\n| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |\n| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |\n| Gradients (bf16) | ~0.4 GB |\n| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |\n| PyTorch + CUDA overhead | ~2 GB |\n| **总计** | **~15-17 GB** |\n\n剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。\n\n**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。\n\n### 4.4 训练超参\n\n```yaml\n# config.yaml\ntraining:\n  mode: \"etadn\"            # \"dpo\" | \"dmpo\" | \"etadn\"\n  beta: 0.1                # DPO β\n  global_gamma: 0.90       # DMPO 模式下的全局 γ\n  learning_rate: 1.0e-6\n  lr_scheduler_type: \"constant_with_warmup\"\n  warmup_ratio: 0.1\n  num_train_epochs: 3\n  per_device_train_batch_size: 1\n  gradient_accumulation_steps: 16\n  gradient_checkpointing: true\n  bf16: true\n  max_length: 3072\n  max_prompt_length: 512\n  logging_steps: 5\n  save_steps: 100\n  eval_steps: 50\n  precompute_ref_log_probs: true\n  label_smoothing: 0.0\n  loss_type: \"sigmoid\"\n\nlora:\n  r: 64\n  lora_alpha: 128\n  target_modules: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n  lora_dropout: 0.05\n\ngamma_e_mapping:\n  action: 0.85\n  verify: 0.92\n  plan: 0.97\n  default: 0.90\n```\n\n---\n\n## 5. 推理 Pipeline\n\n### 5.1 轨迹收集\n\n```python\n# collect_trajectories.py\n# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互\n# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）\n\nfrom vllm import LLM, SamplingParams  # 或 transformers.generate\n\nmodel = LLM(\n    model=\"path/to/qwen3-8b-merged\",  # LoRA merge 后的 checkpoint\n    tensor_parallel_size=1,\n    gpu_memory_utilization=0.85,\n    max_model_len=4096,\n)\n\nparams = SamplingParams(\n    temperature=0.7,\n    top_p=0.9,\n    max_tokens=256,      # 每步生成上限\n    stop=[\"Obs:\"],       # ALFWorld 环境会返回 Obs\n)\n\n# 循环：generate → parse action → env.step → append obs → repeat\n```\n\n**输出格式**：\n\n```json\n{\n  \"task_id\": \"pick_clean_then_place-Tomato-...\",\n  \"trajectory\": [\n    {\"role\": \"assistant\", \"content\": \"Think: ... Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    ...\n  ],\n  \"reward\": 1,           # ALFWorld: 1=成功, 0=失败\n  \"num_steps\": 8,\n  \"task_type\": \"pick_clean_then_place\"\n}\n```\n\n### 5.2 错误分类\n\n```python\n# classify_errors.py\n# 用 Qwen3-14B-AWQ 做 zero-shot 分类\n\nCLASSIFY_PROMPT = \"\"\"Analyze the following failed trajectory in ALFWorld.\nThe agent attempted a task but failed. Identify the PRIMARY error type:\n\n- action: Wrong physical action (e.g., went to wrong location, used wrong object)\n- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)\n- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)\n\nTask: {task_description}\nSuccessful trajectory: {chosen_trajectory}\nFailed trajectory: {rejected_trajectory}\n\nRespond with ONLY one word: action, verify, or plan\"\"\"\n\n# 输出: error_type ∈ {\"action\", \"verify\", \"plan\"}\n```\n\n### 5.3 Preference Pair 构建\n\n```python\n# construct_preference.py\n\ndef construct_pairs(trajectories, error_classifications):\n    \"\"\"\n    策略：\n    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected\n    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs\n    3. 附加 error_type 标签（来自 classify_errors.py 的输出）\n    \"\"\"\n    pairs = []\n    for task_id, task_trajs in group_by_task(trajectories):\n        chosen_trajs = [t for t in task_trajs if t[\"reward\"] == 1]\n        rejected_trajs = [t for t in task_trajs if t[\"reward\"] == 0]\n\n        if not chosen_trajs or not rejected_trajs:\n            continue\n\n        best_chosen = min(chosen_trajs, key=lambda t: t[\"num_steps\"])\n\n        for rej in rejected_trajs:\n            error_type = error_classifications.get(\n                f\"{task_id}_{rej['traj_id']}\", \"default\"\n            )\n            pairs.append({\n                \"id\": f\"{task_id}_pair_{len(pairs)}\",\n                \"error_type\": error_type,\n                \"prompt\": task_description(task_id),\n                \"chosen\": best_chosen[\"trajectory\"],\n                \"rejected\": rej[\"trajectory\"],\n                \"chosen_turns\": count_assistant_turns(best_chosen[\"trajectory\"]),\n                \"rejected_turns\": count_assistant_turns(rej[\"trajectory\"]),\n            })\n\n    return pairs\n```\n\n---\n\n## 6. 完整文件结构\n\n```\nrl-active-probe-fl/\n├── train_etadn.py              # 主训练入口\n│   - 解析 config.yaml\n│   - 加载模型 + LoRA + BnB 量化\n│   - 构建 dataset + collator\n│   - 初始化 ETADNTrainer\n│   - trainer.train()\n│\n├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）\n│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted\n│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns\n│   - DMPODataCollator: 注入 gamma、pad turn_ids\n│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)\n│\n├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合\n│   - compute_phi(t, T, gamma): 单值 φ 计算\n│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重\n│   - dmpo_weighted_logps(): per_token_logps → weighted scalar\n│\n├── data_utils.py               # 数据加载与预处理\n│   - load_preference_data(path): 加载 JSON pairs\n│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization\n│   - build_dataset(): HF Dataset 构建\n│\n├── config.yaml                 # 超参配置（见 §4.4）\n│\n├── collect_trajectories.py     # 轨迹收集（§5.1）\n│   - ALFWorld 环境交互\n│   - vLLM / transformers 推理\n│   - 输出 trajectories.jsonl\n│\n├── classify_errors.py          # 错误分类（§5.2）\n│   - Qwen3-14B-AWQ zero-shot\n│   - 输出 error_classifications.json\n│\n├── construct_preference.py     # Preference pair 构建（§5.3）\n│   - 输入: trajectories + error_classifications\n│   - 输出: preference_pairs.json\n│\n├── evaluate.py                 # ALFWorld 评估\n│   - 标准 eval protocol: 134 unseen tasks\n│   - 指标: success rate, average steps\n│   - 按 task type 分组报告\n│\n├── scripts/\n│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)\n│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)\n│\n└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）\n    ├── env_wrapper.py\n    └── task_configs/\n```\n\n### 6.1 关键模块依赖关系\n\n```\nconfig.yaml\n    ↓\ntrain_etadn.py\n    ├── data_utils.py → tokenize_multiturn()\n    ├── dmpo_trainer.py → ETADNTrainer\n    │       ├── dmpo_loss.py → compute_phi_weights()\n    │       └── DMPODataCollator → gamma injection\n    └── evaluate.py (训练结束后调用)\n\ncollect_trajectories.py → trajectories.jsonl\n    ↓\nclassify_errors.py → error_classifications.json\n    ↓\nconstruct_preference.py → preference_pairs.json\n    ↓\ntrain_etadn.py (读取 preference_pairs.json)\n```\n\n---\n\n## 7. Ablation 设计\n\n### 7.1 三种模式切换\n\n通过 `config.yaml` 中 `training.mode` 字段切换：\n\n| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |\n|---|---|---|---|\n| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |\n| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |\n| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |\n\n### 7.2 代码中的模式分支\n\n在 `ETADNTrainer._compute_loss` 中：\n\n```python\nif self.mode == \"dpo\":\n    # 标准 DPO: 直接 sum\n    logps = (per_token_logps * shift_completion_mask).sum(dim=1)\nelse:\n    # dmpo 或 etadn: φ-weighted sum\n    # gamma 已由 collator 注入到 batch[\"gamma\"]\n    token_phi = compute_phi_weights(\n        turn_ids=batch[\"turn_ids\"][:, 1:],  # shift 对齐\n        gamma=batch[\"gamma\"],\n        num_turns=batch[\"num_turns\"],\n        max_turns=batch[\"turn_ids\"].max().item() + 1,\n    )\n    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n```\n\n### 7.3 实验矩阵\n\n| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)\n\n### 7.4 评估指标\n\n| 指标 | 说明 |\n|---|---|\n| ALFWorld success rate (overall) | 主指标，134 unseen tasks |\n| Success rate per task type | 6 种 task type 的分项成功率 |\n| Average steps to success | 效率指标 |\n| Error type distribution shift | 训练前后的错误类型分布变化 |\n| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |\n| Training loss curve | 收敛性对比 |\n\n---\n\n## 8. ETADNTrainer 核心代码骨架\n\n```python\n# dmpo_trainer.py\n\nfrom trl import DPOTrainer, DPOConfig\nfrom dmpo_loss import compute_phi_weights\n\nclass ETADNConfig(DPOConfig):\n    mode: str = \"etadn\"          # \"dpo\" | \"dmpo\" | \"etadn\"\n    global_gamma: float = 0.90\n    gamma_e_mapping: dict = None  # {\"action\": 0.85, \"verify\": 0.92, \"plan\": 0.97}\n\n\nclass ETADNTrainer(DPOTrainer):\n\n    def __init__(self, *args, mode=\"etadn\", global_gamma=0.9, gamma_e_mapping=None, **kwargs):\n        super().__init__(*args, **kwargs)\n        self.mode = mode\n        self.global_gamma = global_gamma\n        self.gamma_e_mapping = gamma_e_mapping or {}\n\n    def _compute_loss(self, model, inputs, return_outputs=False):\n        \"\"\"Override: DMPO φ-weighted log probability aggregation.\"\"\"\n        # --- 1. 提取额外字段 ---\n        turn_ids = inputs.pop(\"turn_ids\", None)\n        num_turns = inputs.pop(\"num_turns\", None)\n        gamma = inputs.pop(\"gamma\", None)\n        completion_mask = inputs[\"completion_mask\"]\n        input_ids = inputs[\"input_ids\"]\n\n        # --- 2. Policy forward ---\n        model_kwargs = {k: v for k, v in inputs.items()\n                        if k not in (\"completion_mask\", \"ref_chosen_logps\", \"ref_rejected_logps\")}\n        outputs = model(**model_kwargs)\n\n        # --- 3. Per-token logps ---\n        from trl.trainer.utils import selective_log_softmax\n        shift_logits = outputs.logits[..., :-1, :].contiguous()\n        shift_labels = input_ids[..., 1:].contiguous()\n        shift_completion_mask = completion_mask[..., 1:].contiguous()\n        per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n        per_token_logps[shift_completion_mask == 0] = 0.0\n\n        # --- 4. 聚合（核心修改点） ---\n        if self.mode == \"dpo\" or turn_ids is None:\n            logps = per_token_logps.sum(dim=1)\n        else:\n            shift_turn_ids = turn_ids[..., 1:].contiguous()\n            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,\n                                            max_turns=shift_turn_ids.max().item() + 1)\n            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\n        chosen_logps, rejected_logps = logps.chunk(2, dim=0)\n\n        # --- 5. Reference logps ---\n        if \"ref_chosen_logps\" in inputs:\n            ref_chosen_logps = inputs[\"ref_chosen_logps\"]\n            ref_rejected_logps = inputs[\"ref_rejected_logps\"]\n        else:\n            with torch.no_grad():\n                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(\n                    model, inputs, shift_completion_mask,\n                    turn_ids=shift_turn_ids if self.mode != \"dpo\" else None,\n                    gamma=gamma, num_turns=num_turns,\n                )\n\n        # --- 6. Loss (sigmoid, same as standard DPO) ---\n        chosen_logratios = chosen_logps - ref_chosen_logps\n        rejected_logratios = rejected_logps - ref_rejected_logps\n        logits = chosen_logratios - rejected_logratios\n\n        loss = -F.logsigmoid(self.beta * logits).mean()\n\n        # --- 7. Metrics ---\n        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()\n        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()\n        reward_margin = (chosen_rewards - rejected_rewards).mean()\n\n        metrics = {\n            \"loss\": loss.detach().item(),\n            \"rewards/chosen\": chosen_rewards.mean().item(),\n            \"rewards/rejected\": rejected_rewards.mean().item(),\n            \"rewards/margin\": reward_margin.item(),\n        }\n        self.store_metrics(metrics, train_eval=\"train\")\n\n        if return_outputs:\n            return loss, {\"logits\": logits}\n        return loss\n```\n\n---\n\n## 9. 风险与注意事项\n\n| 风险 | 缓解 |\n|---|---|\n| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |\n| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |\n| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |\n| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |\n| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |\n\n---\n\n## 10. 实施优先级\n\n| Phase | 内容 | 估计时间 |\n|---|---|---|\n| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |\n| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |\n| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |\n| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |\n| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |\n| P6 | 完整训练 + 评估 | 2-3 天 |\n",
    "structuredPatch": [
      {
        "oldStart": 485,
        "oldLines": 6,
        "newStart": 485,
        "newLines": 27,
        "lines": [
          "   default: 0.90",
          " ```",
          " ",
          "+### 4.5 环境依赖",
          "+",
          "+| 包 | 要求版本 | 说明 |",
          "+|---|---|---|",
          "+| `trl` | **`==1.4.0`** | 必须使用此版本。1.4.0 将旧版 `get_batch_loss_metrics` / `concatenated_forward` / `get_batch_logps` 合并为 `_compute_loss`，本设计基于此 API 结构。服务器现有 1.1.0 需升级。 |",
          "+| `transformers` | `>=4.40.0` | Qwen3 支持 |",
          "+| `peft` | `>=0.10.0` | LoRA + BnB 集成 |",
          "+| `bitsandbytes` | `>=0.43.0` | nf4 量化 |",
          "+| `torch` | `>=2.1` | bf16 + flash_attention_2 |",
          "+| `flash-attn` | `>=2.5.0` | Flash Attention 2 |",
          "+",
          "+**trl 1.4.0 中本设计依赖的关键 API**：",
          "+- `DPOTrainer._compute_loss(model, inputs, return_outputs)` — 唯一的 loss 扩展点",
          "+- `trl.trainer.utils.selective_log_softmax(logits, labels)` — per-token log prob 计算",
          "+- `DPOConfig` — 训练配置基类",
          "+",
          "+**升级命令**：",
          "+```bash",
          "+pip install trl==1.4.0",
          "+```",
          "+",
          " ---",
          " ",
          " ## 5. 推理 Pipeline"
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

Now add the φ normalization verification section. I'll add it after section 1.3 (per-turn log probability) since it's closely related to the φ function.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "2031d25c-8534-4ba2-8dfd-a13677432e6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkA9592FYp5Aodq688eBRK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 41349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 660
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_016Ly9oXJbgPoq5brFwREnZT`</summary>

````json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "### 1.4 φ(t,T) 权重应用到 per-turn loss",
  "new_string": "### 1.4 φ(t,T) 归一化验证\n\n在实现前需验证 Σ_{t=0}^{T-1} φ(t,T,γ) 在不同 γ 和 T 下的值，确认 φ 是否归一化（即是否 Σφ = 1）。如果 Σφ ≠ 1，需检查 DMPO 论文原始设计意图——可能有意不归一化，利用非归一化引入 length bias（较长轨迹整体权重更大）。\n\n**单元测试**：\n\n```python\nimport math\n\ndef phi(t, T, gamma):\n    \"\"\"DMPO 时间折扣函数\"\"\"\n    return gamma**t * (1 - gamma**(T - t)) / (1 - gamma**T)\n\ndef test_phi_normalization():\n    print(\"=== φ(t,T) 归一化验证 ===\")\n    for gamma in [0.85, 0.92, 0.97]:\n        for T in [5, 10, 20, 40]:\n            phi_sum = sum(phi(t, T, gamma) for t in range(T))\n            normalized = \"✓\" if abs(phi_sum - 1.0) < 1e-6 else \"✗\"\n            print(f\"γ={gamma}, T={T:2d}: Σφ={phi_sum:.6f}  {normalized}\")\n    print()\n    print(\"如果 Σφ ≠ 1:\")\n    print(\"  1. 检查 DMPO 论文 Eq.16 是否有意不归一化\")\n    print(\"  2. 若有意：长轨迹获得更大总权重 → implicit length bias\")\n    print(\"  3. 若需归一化：可在 compute_phi_weights 中除以 Σφ\")\n    print(\"  4. 非归一化时可能需要调整 β 以补偿尺度变化\")\n\nif __name__ == \"__main__\":\n    test_phi_normalization()\n```\n\n此测试应在 P1 阶段（`dmpo_loss.py` 单元测试）中执行。若 Σφ 显著偏离 1，需在 §9 风险表中记录应对方案，并决定是否在 `compute_phi_weights` 中添加归一化选项。\n\n### 1.5 φ(t,T) 权重应用到 per-turn loss"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "a38e654e-a603-48e8-9f2c-8cf9b0c772da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkA9592FYp5Aodq688eBRK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 41349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 660
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T11:01:42.457Z_

<details><summary>↩ Tool result · `toolu_016Ly9oXJbgPoq5brFwREnZT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "97af31b6-48c8-4fa2-817a-522476387d4c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "oldString": "### 1.4 φ(t,T) 权重应用到 per-turn loss",
    "newString": "### 1.4 φ(t,T) 归一化验证\n\n在实现前需验证 Σ_{t=0}^{T-1} φ(t,T,γ) 在不同 γ 和 T 下的值，确认 φ 是否归一化（即是否 Σφ = 1）。如果 Σφ ≠ 1，需检查 DMPO 论文原始设计意图——可能有意不归一化，利用非归一化引入 length bias（较长轨迹整体权重更大）。\n\n**单元测试**：\n\n```python\nimport math\n\ndef phi(t, T, gamma):\n    \"\"\"DMPO 时间折扣函数\"\"\"\n    return gamma**t * (1 - gamma**(T - t)) / (1 - gamma**T)\n\ndef test_phi_normalization():\n    print(\"=== φ(t,T) 归一化验证 ===\")\n    for gamma in [0.85, 0.92, 0.97]:\n        for T in [5, 10, 20, 40]:\n            phi_sum = sum(phi(t, T, gamma) for t in range(T))\n            normalized = \"✓\" if abs(phi_sum - 1.0) < 1e-6 else \"✗\"\n            print(f\"γ={gamma}, T={T:2d}: Σφ={phi_sum:.6f}  {normalized}\")\n    print()\n    print(\"如果 Σφ ≠ 1:\")\n    print(\"  1. 检查 DMPO 论文 Eq.16 是否有意不归一化\")\n    print(\"  2. 若有意：长轨迹获得更大总权重 → implicit length bias\")\n    print(\"  3. 若需归一化：可在 compute_phi_weights 中除以 Σφ\")\n    print(\"  4. 非归一化时可能需要调整 β 以补偿尺度变化\")\n\nif __name__ == \"__main__\":\n    test_phi_normalization()\n```\n\n此测试应在 P1 阶段（`dmpo_loss.py` 单元测试）中执行。若 Σφ 显著偏离 1，需在 §9 风险表中记录应对方案，并决定是否在 `compute_phi_weights` 中添加归一化选项。\n\n### 1.5 φ(t,T) 权重应用到 per-turn loss",
    "originalFile": "# DMPO + ETADN 训练 Pipeline 设计（v2）\n\n## 0. 术语与背景\n\n**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。\n\n**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。\n\n**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。\n\n---\n\n## 1. DMPO Loss 实现方案\n\n### 1.1 完整 DMPO Loss 公式\n\n标准 DPO loss（单轮）：\n\n```\nL_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]\n```\n\nDMPO loss（多轮，论文 Eq.16）：\n\n```\nL_DMPO = -E[ log σ(\n    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]\n  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]\n)]\n```\n\n其中时间折扣函数：\n\n```\nφ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n```\n\n- t = turn index (0-indexed)\n- T = 总 turn 数\n- γ ∈ (0, 1) = 时间折扣因子\n- φ(t, T) 单调递减：早期 turn 权重更高\n\n**特殊情况**：\n- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO\n- γ = 1: φ(t,T) = (T-t)/T → 线性衰减\n\n### 1.2 在 trl DPOTrainer 上实现 DMPO\n\n**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。\n\n**需要修改的核心逻辑**（在 `_compute_loss` 内）：\n\n| 原始 trl 行为 | DMPO 修改 |\n|---|---|\n| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |\n| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |\n| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |\n\n**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。\n\n### 1.3 Per-turn log probability 计算\n\nALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。\n\n**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：\n\n```\ntoken:    [&lt;prompt> | Think... Act... | Think... Act... | Think... Act... ]\nturn_ids: [   -1    |       0        |        1        |        2        ]\n```\n\n**加权聚合伪代码**：\n\n```python\ndef dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):\n    \"\"\"\n    per_token_logps: [batch, seq_len]\n    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)\n    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)\n    gamma:           [batch]           (per-sample γ)\n    num_turns:       [batch]           (per-sample T)\n    Returns:         [batch]           (weighted log probability per sample)\n    \"\"\"\n    # 构建 per-token φ 权重\n    token_weights = torch.zeros_like(per_token_logps)\n    for t in range(turn_ids.max() + 1):\n        mask_t = (turn_ids == t)  # [batch, seq_len]\n        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)\n        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]\n\n    return (per_token_logps * completion_mask * token_weights).sum(dim=1)\n```\n\n**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：\n\n```python\ndef compute_phi_weights(turn_ids, gamma, num_turns, max_turns):\n    \"\"\"全向量化 φ 权重计算\"\"\"\n    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]\n    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]\n    T = num_turns.unsqueeze(1).float()                            # [batch, 1]\n\n    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)\n    # phi: [batch, max_turns]\n\n    # 用 turn_ids gather 到 per-token 权重\n    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零\n    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]\n    return token_phi\n```\n\n### 1.4 φ(t,T) 权重应用到 per-turn loss\n\n在 `_compute_loss` 中，替换聚合步骤：\n\n```python\n# === 原始 trl ===\n# logps = per_token_logps.sum(dim=1)\n\n# === DMPO 修改 ===\ntoken_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)\nlogps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\nchosen_logps, rejected_logps = logps.chunk(2, dim=0)\n# 后续 log ratio、sigmoid loss 与标准 DPO 相同\n```\n\n---\n\n## 2. γ_e 注入方案\n\n### 2.1 Error Type → γ_e 映射\n\n```yaml\n# config.yaml\ngamma_e_mapping:\n  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步\n  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列\n  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹\n  default: 0.90   # 未分类 fallback\n```\n\n**直觉**：\n- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）\n- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）\n\n### 2.2 注入流程\n\n```\n数据加载 → 每个样本有 error_type 字段\n       ↓\nDataCollator → 查表得到 gamma_per_sample: [batch_size]\n       ↓\n_compute_loss → gamma_per_sample 传入 compute_phi_weights()\n       ↓\nper-token 权重 → 加权聚合 → 标准 sigmoid loss\n```\n\n**Collator 中的 γ 注入**：\n\n```python\nclass DMPODataCollator(DataCollatorForPreference):\n    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):\n        super().__init__(**kwargs)\n        self.gamma_map = gamma_map\n        self.mode = mode\n        self.global_gamma = global_gamma\n\n    def __call__(self, features):\n        batch = super().__call__(features)\n\n        # 收集 error_type → gamma\n        gammas = []\n        for f in features:\n            if self.mode == \"etadn\":\n                et = f.get(\"error_type\", \"default\")\n                gammas.append(self.gamma_map.get(et, self.gamma_map[\"default\"]))\n            elif self.mode == \"dmpo\":\n                gammas.append(self.global_gamma)\n            else:  # dpo\n                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权\n\n        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）\n        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)\n        gamma_rejected = gamma_chosen.clone()\n        batch[\"gamma\"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)\n\n        return batch\n```\n\n### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e\n\n| 维度 | DMPO | ETADN |\n|---|---|---|\n| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |\n| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |\n| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |\n| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |\n\n---\n\n## 3. 数据 Pipeline\n\n### 3.1 DPO 数据格式\n\n每个样本包含：\n\n```json\n{\n  \"id\": \"alfworld_task_42_pair_0\",\n  \"error_type\": \"action\",\n  \"prompt\": \"You are in a kitchen. Your task is to ...\",\n  \"chosen\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: I should open it. Act: open fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You open the fridge. You see a tomato 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Found it. Act: take tomato 1 from fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You pick up the tomato 1.\"}\n  ],\n  \"rejected\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to countertop 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a bread 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Not here. Act: go to countertop 2\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a cup 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Maybe in the cabinet. Act: go to cabinet 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The cabinet is closed.\"}\n  ],\n  \"chosen_turns\": 3,\n  \"rejected_turns\": 3\n}\n```\n\n### 3.2 多轮对话处理：Turn 定义\n\nALFWorld 轨迹中每个 turn 的结构：\n\n```\nTurn t:\n  Assistant: \"Think: &lt;reasoning>. Act: &lt;action>\"    ← agent 生成\n  User:      \"Obs: &lt;environment_observation>\"        ← 环境返回\n```\n\n**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。\n\nTurn 数 T = assistant 回复的数量。\n\n### 3.3 Tokenization 与 Turn 标记\n\n```python\ndef tokenize_multiturn(example, tokenizer, max_length):\n    \"\"\"将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids\"\"\"\n    # 1. 构建完整对话（chat template）\n    messages = [{\"role\": \"system\", \"content\": example[\"prompt\"]}]\n    messages += example[\"chosen\"]  # 或 rejected\n\n    # 2. 分步 tokenize 以获取 turn 边界\n    prompt_ids = tokenizer.apply_chat_template(\n        [messages[0]], tokenize=True, add_generation_prompt=True\n    )\n\n    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1\n    completion_mask = [0] * len(prompt_ids)\n    all_ids = list(prompt_ids)\n    current_turn = 0\n\n    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs\n        # assistant 部分\n        asst_msg = messages[i]\n        asst_ids = tokenizer.encode(asst_msg[\"content\"], add_special_tokens=False)\n        # + chat template 的 role tokens\n        role_ids = tokenizer.encode(\"<|im_start|>assistant\\n\", add_special_tokens=False)\n        end_ids = tokenizer.encode(\"<|im_end|>\\n\", add_special_tokens=False)\n\n        all_ids += role_ids\n        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss\n        completion_mask += [0] * len(role_ids)\n\n        all_ids += asst_ids\n        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t\n        completion_mask += [1] * len(asst_ids)\n\n        all_ids += end_ids\n        turn_ids += [current_turn] * len(end_ids)\n        completion_mask += [1] * len(end_ids)\n\n        # user/observation 部分\n        if i + 1 < len(messages):\n            user_msg = messages[i + 1]\n            user_ids = tokenizer.encode(\n                f\"<|im_start|>user\\n{user_msg['content']}<|im_end|>\\n\",\n                add_special_tokens=False\n            )\n            all_ids += user_ids\n            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss\n            completion_mask += [0] * len(user_ids)\n\n        current_turn += 1\n\n    # 3. 截断\n    all_ids = all_ids[:max_length]\n    turn_ids = turn_ids[:max_length]\n    completion_mask = completion_mask[:max_length]\n\n    return {\n        \"input_ids\": all_ids,\n        \"turn_ids\": turn_ids,\n        \"completion_mask\": completion_mask,\n        \"num_turns\": current_turn,\n    }\n```\n\n**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。\n\n### 3.4 数据集统计预估\n\n| 维度 | 估计值 |\n|---|---|\n| ALFWorld 任务数 | ~3,500 (train split) |\n| 每任务轨迹数 | 5-10（采样多条） |\n| 有效 preference pairs | ~2,000-5,000（过滤后） |\n| 平均 turn 数 T | 5-15 |\n| 平均序列长度 | 1,500-3,000 tokens |\n\n---\n\n## 4. 模型配置\n\n### 4.1 Qwen3-8B QLoRA 配置\n\n```python\nfrom transformers import AutoModelForCausalLM, BitsAndBytesConfig\nfrom peft import LoraConfig\n\nbnb_config = BitsAndBytesConfig(\n    load_in_4bit=True,\n    bnb_4bit_quant_type=\"nf4\",\n    bnb_4bit_compute_dtype=torch.bfloat16,\n    bnb_4bit_use_double_quant=True,\n)\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    \"Qwen/Qwen3-8B\",\n    quantization_config=bnb_config,\n    torch_dtype=torch.bfloat16,\n    attn_implementation=\"flash_attention_2\",\n    device_map={\"\": device_id},  # 单卡绑定\n)\n\nlora_config = LoraConfig(\n    r=64,\n    lora_alpha=128,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                     \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_dropout=0.05,\n    task_type=\"CAUSAL_LM\",\n    bias=\"none\",\n)\n```\n\n### 4.2 Ref Model 处理\n\nQLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。\n\ntrl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确\n\n### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）\n\n| 组件 | 估计 VRAM |\n|---|---|\n| Qwen3-8B 4-bit weights | ~4.5 GB |\n| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |\n| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |\n| Gradients (bf16) | ~0.4 GB |\n| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |\n| PyTorch + CUDA overhead | ~2 GB |\n| **总计** | **~15-17 GB** |\n\n剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。\n\n**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。\n\n### 4.4 训练超参\n\n```yaml\n# config.yaml\ntraining:\n  mode: \"etadn\"            # \"dpo\" | \"dmpo\" | \"etadn\"\n  beta: 0.1                # DPO β\n  global_gamma: 0.90       # DMPO 模式下的全局 γ\n  learning_rate: 1.0e-6\n  lr_scheduler_type: \"constant_with_warmup\"\n  warmup_ratio: 0.1\n  num_train_epochs: 3\n  per_device_train_batch_size: 1\n  gradient_accumulation_steps: 16\n  gradient_checkpointing: true\n  bf16: true\n  max_length: 3072\n  max_prompt_length: 512\n  logging_steps: 5\n  save_steps: 100\n  eval_steps: 50\n  precompute_ref_log_probs: true\n  label_smoothing: 0.0\n  loss_type: \"sigmoid\"\n\nlora:\n  r: 64\n  lora_alpha: 128\n  target_modules: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n  lora_dropout: 0.05\n\ngamma_e_mapping:\n  action: 0.85\n  verify: 0.92\n  plan: 0.97\n  default: 0.90\n```\n\n### 4.5 环境依赖\n\n| 包 | 要求版本 | 说明 |\n|---|---|---|\n| `trl` | **`==1.4.0`** | 必须使用此版本。1.4.0 将旧版 `get_batch_loss_metrics` / `concatenated_forward` / `get_batch_logps` 合并为 `_compute_loss`，本设计基于此 API 结构。服务器现有 1.1.0 需升级。 |\n| `transformers` | `>=4.40.0` | Qwen3 支持 |\n| `peft` | `>=0.10.0` | LoRA + BnB 集成 |\n| `bitsandbytes` | `>=0.43.0` | nf4 量化 |\n| `torch` | `>=2.1` | bf16 + flash_attention_2 |\n| `flash-attn` | `>=2.5.0` | Flash Attention 2 |\n\n**trl 1.4.0 中本设计依赖的关键 API**：\n- `DPOTrainer._compute_loss(model, inputs, return_outputs)` — 唯一的 loss 扩展点\n- `trl.trainer.utils.selective_log_softmax(logits, labels)` — per-token log prob 计算\n- `DPOConfig` — 训练配置基类\n\n**升级命令**：\n```bash\npip install trl==1.4.0\n```\n\n---\n\n## 5. 推理 Pipeline\n\n### 5.1 轨迹收集\n\n```python\n# collect_trajectories.py\n# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互\n# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）\n\nfrom vllm import LLM, SamplingParams  # 或 transformers.generate\n\nmodel = LLM(\n    model=\"path/to/qwen3-8b-merged\",  # LoRA merge 后的 checkpoint\n    tensor_parallel_size=1,\n    gpu_memory_utilization=0.85,\n    max_model_len=4096,\n)\n\nparams = SamplingParams(\n    temperature=0.7,\n    top_p=0.9,\n    max_tokens=256,      # 每步生成上限\n    stop=[\"Obs:\"],       # ALFWorld 环境会返回 Obs\n)\n\n# 循环：generate → parse action → env.step → append obs → repeat\n```\n\n**输出格式**：\n\n```json\n{\n  \"task_id\": \"pick_clean_then_place-Tomato-...\",\n  \"trajectory\": [\n    {\"role\": \"assistant\", \"content\": \"Think: ... Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    ...\n  ],\n  \"reward\": 1,           # ALFWorld: 1=成功, 0=失败\n  \"num_steps\": 8,\n  \"task_type\": \"pick_clean_then_place\"\n}\n```\n\n### 5.2 错误分类\n\n```python\n# classify_errors.py\n# 用 Qwen3-14B-AWQ 做 zero-shot 分类\n\nCLASSIFY_PROMPT = \"\"\"Analyze the following failed trajectory in ALFWorld.\nThe agent attempted a task but failed. Identify the PRIMARY error type:\n\n- action: Wrong physical action (e.g., went to wrong location, used wrong object)\n- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)\n- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)\n\nTask: {task_description}\nSuccessful trajectory: {chosen_trajectory}\nFailed trajectory: {rejected_trajectory}\n\nRespond with ONLY one word: action, verify, or plan\"\"\"\n\n# 输出: error_type ∈ {\"action\", \"verify\", \"plan\"}\n```\n\n### 5.3 Preference Pair 构建\n\n```python\n# construct_preference.py\n\ndef construct_pairs(trajectories, error_classifications):\n    \"\"\"\n    策略：\n    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected\n    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs\n    3. 附加 error_type 标签（来自 classify_errors.py 的输出）\n    \"\"\"\n    pairs = []\n    for task_id, task_trajs in group_by_task(trajectories):\n        chosen_trajs = [t for t in task_trajs if t[\"reward\"] == 1]\n        rejected_trajs = [t for t in task_trajs if t[\"reward\"] == 0]\n\n        if not chosen_trajs or not rejected_trajs:\n            continue\n\n        best_chosen = min(chosen_trajs, key=lambda t: t[\"num_steps\"])\n\n        for rej in rejected_trajs:\n            error_type = error_classifications.get(\n                f\"{task_id}_{rej['traj_id']}\", \"default\"\n            )\n            pairs.append({\n                \"id\": f\"{task_id}_pair_{len(pairs)}\",\n                \"error_type\": error_type,\n                \"prompt\": task_description(task_id),\n                \"chosen\": best_chosen[\"trajectory\"],\n                \"rejected\": rej[\"trajectory\"],\n                \"chosen_turns\": count_assistant_turns(best_chosen[\"trajectory\"]),\n                \"rejected_turns\": count_assistant_turns(rej[\"trajectory\"]),\n            })\n\n    return pairs\n```\n\n---\n\n## 6. 完整文件结构\n\n```\nrl-active-probe-fl/\n├── train_etadn.py              # 主训练入口\n│   - 解析 config.yaml\n│   - 加载模型 + LoRA + BnB 量化\n│   - 构建 dataset + collator\n│   - 初始化 ETADNTrainer\n│   - trainer.train()\n│\n├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）\n│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted\n│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns\n│   - DMPODataCollator: 注入 gamma、pad turn_ids\n│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)\n│\n├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合\n│   - compute_phi(t, T, gamma): 单值 φ 计算\n│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重\n│   - dmpo_weighted_logps(): per_token_logps → weighted scalar\n│\n├── data_utils.py               # 数据加载与预处理\n│   - load_preference_data(path): 加载 JSON pairs\n│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization\n│   - build_dataset(): HF Dataset 构建\n│\n├── config.yaml                 # 超参配置（见 §4.4）\n│\n├── collect_trajectories.py     # 轨迹收集（§5.1）\n│   - ALFWorld 环境交互\n│   - vLLM / transformers 推理\n│   - 输出 trajectories.jsonl\n│\n├── classify_errors.py          # 错误分类（§5.2）\n│   - Qwen3-14B-AWQ zero-shot\n│   - 输出 error_classifications.json\n│\n├── construct_preference.py     # Preference pair 构建（§5.3）\n│   - 输入: trajectories + error_classifications\n│   - 输出: preference_pairs.json\n│\n├── evaluate.py                 # ALFWorld 评估\n│   - 标准 eval protocol: 134 unseen tasks\n│   - 指标: success rate, average steps\n│   - 按 task type 分组报告\n│\n├── scripts/\n│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)\n│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)\n│\n└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）\n    ├── env_wrapper.py\n    └── task_configs/\n```\n\n### 6.1 关键模块依赖关系\n\n```\nconfig.yaml\n    ↓\ntrain_etadn.py\n    ├── data_utils.py → tokenize_multiturn()\n    ├── dmpo_trainer.py → ETADNTrainer\n    │       ├── dmpo_loss.py → compute_phi_weights()\n    │       └── DMPODataCollator → gamma injection\n    └── evaluate.py (训练结束后调用)\n\ncollect_trajectories.py → trajectories.jsonl\n    ↓\nclassify_errors.py → error_classifications.json\n    ↓\nconstruct_preference.py → preference_pairs.json\n    ↓\ntrain_etadn.py (读取 preference_pairs.json)\n```\n\n---\n\n## 7. Ablation 设计\n\n### 7.1 三种模式切换\n\n通过 `config.yaml` 中 `training.mode` 字段切换：\n\n| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |\n|---|---|---|---|\n| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |\n| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |\n| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |\n\n### 7.2 代码中的模式分支\n\n在 `ETADNTrainer._compute_loss` 中：\n\n```python\nif self.mode == \"dpo\":\n    # 标准 DPO: 直接 sum\n    logps = (per_token_logps * shift_completion_mask).sum(dim=1)\nelse:\n    # dmpo 或 etadn: φ-weighted sum\n    # gamma 已由 collator 注入到 batch[\"gamma\"]\n    token_phi = compute_phi_weights(\n        turn_ids=batch[\"turn_ids\"][:, 1:],  # shift 对齐\n        gamma=batch[\"gamma\"],\n        num_turns=batch[\"num_turns\"],\n        max_turns=batch[\"turn_ids\"].max().item() + 1,\n    )\n    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n```\n\n### 7.3 实验矩阵\n\n| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)\n\n### 7.4 评估指标\n\n| 指标 | 说明 |\n|---|---|\n| ALFWorld success rate (overall) | 主指标，134 unseen tasks |\n| Success rate per task type | 6 种 task type 的分项成功率 |\n| Average steps to success | 效率指标 |\n| Error type distribution shift | 训练前后的错误类型分布变化 |\n| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |\n| Training loss curve | 收敛性对比 |\n\n---\n\n## 8. ETADNTrainer 核心代码骨架\n\n```python\n# dmpo_trainer.py\n\nfrom trl import DPOTrainer, DPOConfig\nfrom dmpo_loss import compute_phi_weights\n\nclass ETADNConfig(DPOConfig):\n    mode: str = \"etadn\"          # \"dpo\" | \"dmpo\" | \"etadn\"\n    global_gamma: float = 0.90\n    gamma_e_mapping: dict = None  # {\"action\": 0.85, \"verify\": 0.92, \"plan\": 0.97}\n\n\nclass ETADNTrainer(DPOTrainer):\n\n    def __init__(self, *args, mode=\"etadn\", global_gamma=0.9, gamma_e_mapping=None, **kwargs):\n        super().__init__(*args, **kwargs)\n        self.mode = mode\n        self.global_gamma = global_gamma\n        self.gamma_e_mapping = gamma_e_mapping or {}\n\n    def _compute_loss(self, model, inputs, return_outputs=False):\n        \"\"\"Override: DMPO φ-weighted log probability aggregation.\"\"\"\n        # --- 1. 提取额外字段 ---\n        turn_ids = inputs.pop(\"turn_ids\", None)\n        num_turns = inputs.pop(\"num_turns\", None)\n        gamma = inputs.pop(\"gamma\", None)\n        completion_mask = inputs[\"completion_mask\"]\n        input_ids = inputs[\"input_ids\"]\n\n        # --- 2. Policy forward ---\n        model_kwargs = {k: v for k, v in inputs.items()\n                        if k not in (\"completion_mask\", \"ref_chosen_logps\", \"ref_rejected_logps\")}\n        outputs = model(**model_kwargs)\n\n        # --- 3. Per-token logps ---\n        from trl.trainer.utils import selective_log_softmax\n        shift_logits = outputs.logits[..., :-1, :].contiguous()\n        shift_labels = input_ids[..., 1:].contiguous()\n        shift_completion_mask = completion_mask[..., 1:].contiguous()\n        per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n        per_token_logps[shift_completion_mask == 0] = 0.0\n\n        # --- 4. 聚合（核心修改点） ---\n        if self.mode == \"dpo\" or turn_ids is None:\n            logps = per_token_logps.sum(dim=1)\n        else:\n            shift_turn_ids = turn_ids[..., 1:].contiguous()\n            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,\n                                            max_turns=shift_turn_ids.max().item() + 1)\n            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\n        chosen_logps, rejected_logps = logps.chunk(2, dim=0)\n\n        # --- 5. Reference logps ---\n        if \"ref_chosen_logps\" in inputs:\n            ref_chosen_logps = inputs[\"ref_chosen_logps\"]\n            ref_rejected_logps = inputs[\"ref_rejected_logps\"]\n        else:\n            with torch.no_grad():\n                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(\n                    model, inputs, shift_completion_mask,\n                    turn_ids=shift_turn_ids if self.mode != \"dpo\" else None,\n                    gamma=gamma, num_turns=num_turns,\n                )\n\n        # --- 6. Loss (sigmoid, same as standard DPO) ---\n        chosen_logratios = chosen_logps - ref_chosen_logps\n        rejected_logratios = rejected_logps - ref_rejected_logps\n        logits = chosen_logratios - rejected_logratios\n\n        loss = -F.logsigmoid(self.beta * logits).mean()\n\n        # --- 7. Metrics ---\n        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()\n        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()\n        reward_margin = (chosen_rewards - rejected_rewards).mean()\n\n        metrics = {\n            \"loss\": loss.detach().item(),\n            \"rewards/chosen\": chosen_rewards.mean().item(),\n            \"rewards/rejected\": rejected_rewards.mean().item(),\n            \"rewards/margin\": reward_margin.item(),\n        }\n        self.store_metrics(metrics, train_eval=\"train\")\n\n        if return_outputs:\n            return loss, {\"logits\": logits}\n        return loss\n```\n\n---\n\n## 9. 风险与注意事项\n\n| 风险 | 缓解 |\n|---|---|\n| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |\n| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |\n| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |\n| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |\n| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |\n\n---\n\n## 10. 实施优先级\n\n| Phase | 内容 | 估计时间 |\n|---|---|---|\n| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |\n| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |\n| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |\n| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |\n| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |\n| P6 | 完整训练 + 评估 | 2-3 天 |\n",
    "structuredPatch": [
      {
        "oldStart": 110,
        "oldLines": 8,
        "newStart": 110,
        "newLines": 41,
        "lines": [
          "     return token_phi",
          " ```",
          " ",
          "-### 1.4 φ(t,T) 权重应用到 per-turn loss",
          "+### 1.4 φ(t,T) 归一化验证",
          " ",
          "+在实现前需验证 Σ_{t=0}^{T-1} φ(t,T,γ) 在不同 γ 和 T 下的值，确认 φ 是否归一化（即是否 Σφ = 1）。如果 Σφ ≠ 1，需检查 DMPO 论文原始设计意图——可能有意不归一化，利用非归一化引入 length bias（较长轨迹整体权重更大）。",
          "+",
          "+**单元测试**：",
          "+",
          "+```python",
          "+import math",
          "+",
          "+def phi(t, T, gamma):",
          "+    \"\"\"DMPO 时间折扣函数\"\"\"",
          "+    return gamma**t * (1 - gamma**(T - t)) / (1 - gamma**T)",
          "+",
          "+def test_phi_normalization():",
          "+    print(\"=== φ(t,T) 归一化验证 ===\")",
          "+    for gamma in [0.85, 0.92, 0.97]:",
          "+        for T in [5, 10, 20, 40]:",
          "+            phi_sum = sum(phi(t, T, gamma) for t in range(T))",
          "+            normalized = \"✓\" if abs(phi_sum - 1.0) < 1e-6 else \"✗\"",
          "+            print(f\"γ={gamma}, T={T:2d}: Σφ={phi_sum:.6f}  {normalized}\")",
          "+    print()",
          "+    print(\"如果 Σφ ≠ 1:\")",
          "+    print(\"  1. 检查 DMPO 论文 Eq.16 是否有意不归一化\")",
          "+    print(\"  2. 若有意：长轨迹获得更大总权重 → implicit length bias\")",
          "+    print(\"  3. 若需归一化：可在 compute_phi_weights 中除以 Σφ\")",
          "+    print(\"  4. 非归一化时可能需要调整 β 以补偿尺度变化\")",
          "+",
          "+if __name__ == \"__main__\":",
          "+    test_phi_normalization()",
          "+```",
          "+",
          "+此测试应在 P1 阶段（`dmpo_loss.py` 单元测试）中执行。若 Σφ 显著偏离 1，需在 §9 风险表中记录应对方案，并决定是否在 `compute_phi_weights` 中添加归一化选项。",
          "+",
          "+### 1.5 φ(t,T) 权重应用到 per-turn loss",
          "+",
          " 在 `_compute_loss` 中，替换聚合步骤：",
          " ",
          " ```python"
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

Now update the section reference in section 7 since 1.4 became 1.5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "42a7eca7-1c55-42f7-9fb6-91c8bdced713",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3GWWR9kTGK9ojvvuHGadb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 42009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1070
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01NmrSLmHbpG4ez7sLShk75q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |",
  "new_string": "| φ 权重导致梯度尺度变化 | 需通过 §1.4 归一化验证确认 Σφ 的实际值。若 Σφ ≠ 1 且偏差显著，可在 `compute_phi_weights` 中添加归一化选项，或调整 β 补偿尺度 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "e8d8574f-cfad-4d57-9137-cb5ff7d10aa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3GWWR9kTGK9ojvvuHGadb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 42009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1070
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-12T11:01:50.770Z_

<details><summary>↩ Tool result · `toolu_01NmrSLmHbpG4ez7sLShk75q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "05bad9f0-fd13-48fd-a174-4f6e1981ed79",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "oldString": "| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |",
    "newString": "| φ 权重导致梯度尺度变化 | 需通过 §1.4 归一化验证确认 Σφ 的实际值。若 Σφ ≠ 1 且偏差显著，可在 `compute_phi_weights` 中添加归一化选项，或调整 β 补偿尺度 |",
    "originalFile": "# DMPO + ETADN 训练 Pipeline 设计（v2）\n\n## 0. 术语与背景\n\n**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。\n\n**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。\n\n**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。\n\n---\n\n## 1. DMPO Loss 实现方案\n\n### 1.1 完整 DMPO Loss 公式\n\n标准 DPO loss（单轮）：\n\n```\nL_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]\n```\n\nDMPO loss（多轮，论文 Eq.16）：\n\n```\nL_DMPO = -E[ log σ(\n    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]\n  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]\n)]\n```\n\n其中时间折扣函数：\n\n```\nφ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n```\n\n- t = turn index (0-indexed)\n- T = 总 turn 数\n- γ ∈ (0, 1) = 时间折扣因子\n- φ(t, T) 单调递减：早期 turn 权重更高\n\n**特殊情况**：\n- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO\n- γ = 1: φ(t,T) = (T-t)/T → 线性衰减\n\n### 1.2 在 trl DPOTrainer 上实现 DMPO\n\n**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。\n\n**需要修改的核心逻辑**（在 `_compute_loss` 内）：\n\n| 原始 trl 行为 | DMPO 修改 |\n|---|---|\n| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |\n| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |\n| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |\n\n**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。\n\n### 1.3 Per-turn log probability 计算\n\nALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。\n\n**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：\n\n```\ntoken:    [&lt;prompt> | Think... Act... | Think... Act... | Think... Act... ]\nturn_ids: [   -1    |       0        |        1        |        2        ]\n```\n\n**加权聚合伪代码**：\n\n```python\ndef dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):\n    \"\"\"\n    per_token_logps: [batch, seq_len]\n    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)\n    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)\n    gamma:           [batch]           (per-sample γ)\n    num_turns:       [batch]           (per-sample T)\n    Returns:         [batch]           (weighted log probability per sample)\n    \"\"\"\n    # 构建 per-token φ 权重\n    token_weights = torch.zeros_like(per_token_logps)\n    for t in range(turn_ids.max() + 1):\n        mask_t = (turn_ids == t)  # [batch, seq_len]\n        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)\n        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)\n        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]\n\n    return (per_token_logps * completion_mask * token_weights).sum(dim=1)\n```\n\n**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：\n\n```python\ndef compute_phi_weights(turn_ids, gamma, num_turns, max_turns):\n    \"\"\"全向量化 φ 权重计算\"\"\"\n    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]\n    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]\n    T = num_turns.unsqueeze(1).float()                            # [batch, 1]\n\n    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)\n    # phi: [batch, max_turns]\n\n    # 用 turn_ids gather 到 per-token 权重\n    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零\n    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]\n    return token_phi\n```\n\n### 1.4 φ(t,T) 归一化验证\n\n在实现前需验证 Σ_{t=0}^{T-1} φ(t,T,γ) 在不同 γ 和 T 下的值，确认 φ 是否归一化（即是否 Σφ = 1）。如果 Σφ ≠ 1，需检查 DMPO 论文原始设计意图——可能有意不归一化，利用非归一化引入 length bias（较长轨迹整体权重更大）。\n\n**单元测试**：\n\n```python\nimport math\n\ndef phi(t, T, gamma):\n    \"\"\"DMPO 时间折扣函数\"\"\"\n    return gamma**t * (1 - gamma**(T - t)) / (1 - gamma**T)\n\ndef test_phi_normalization():\n    print(\"=== φ(t,T) 归一化验证 ===\")\n    for gamma in [0.85, 0.92, 0.97]:\n        for T in [5, 10, 20, 40]:\n            phi_sum = sum(phi(t, T, gamma) for t in range(T))\n            normalized = \"✓\" if abs(phi_sum - 1.0) < 1e-6 else \"✗\"\n            print(f\"γ={gamma}, T={T:2d}: Σφ={phi_sum:.6f}  {normalized}\")\n    print()\n    print(\"如果 Σφ ≠ 1:\")\n    print(\"  1. 检查 DMPO 论文 Eq.16 是否有意不归一化\")\n    print(\"  2. 若有意：长轨迹获得更大总权重 → implicit length bias\")\n    print(\"  3. 若需归一化：可在 compute_phi_weights 中除以 Σφ\")\n    print(\"  4. 非归一化时可能需要调整 β 以补偿尺度变化\")\n\nif __name__ == \"__main__\":\n    test_phi_normalization()\n```\n\n此测试应在 P1 阶段（`dmpo_loss.py` 单元测试）中执行。若 Σφ 显著偏离 1，需在 §9 风险表中记录应对方案，并决定是否在 `compute_phi_weights` 中添加归一化选项。\n\n### 1.5 φ(t,T) 权重应用到 per-turn loss\n\n在 `_compute_loss` 中，替换聚合步骤：\n\n```python\n# === 原始 trl ===\n# logps = per_token_logps.sum(dim=1)\n\n# === DMPO 修改 ===\ntoken_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)\nlogps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\nchosen_logps, rejected_logps = logps.chunk(2, dim=0)\n# 后续 log ratio、sigmoid loss 与标准 DPO 相同\n```\n\n---\n\n## 2. γ_e 注入方案\n\n### 2.1 Error Type → γ_e 映射\n\n```yaml\n# config.yaml\ngamma_e_mapping:\n  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步\n  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列\n  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹\n  default: 0.90   # 未分类 fallback\n```\n\n**直觉**：\n- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）\n- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）\n\n### 2.2 注入流程\n\n```\n数据加载 → 每个样本有 error_type 字段\n       ↓\nDataCollator → 查表得到 gamma_per_sample: [batch_size]\n       ↓\n_compute_loss → gamma_per_sample 传入 compute_phi_weights()\n       ↓\nper-token 权重 → 加权聚合 → 标准 sigmoid loss\n```\n\n**Collator 中的 γ 注入**：\n\n```python\nclass DMPODataCollator(DataCollatorForPreference):\n    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):\n        super().__init__(**kwargs)\n        self.gamma_map = gamma_map\n        self.mode = mode\n        self.global_gamma = global_gamma\n\n    def __call__(self, features):\n        batch = super().__call__(features)\n\n        # 收集 error_type → gamma\n        gammas = []\n        for f in features:\n            if self.mode == \"etadn\":\n                et = f.get(\"error_type\", \"default\")\n                gammas.append(self.gamma_map.get(et, self.gamma_map[\"default\"]))\n            elif self.mode == \"dmpo\":\n                gammas.append(self.global_gamma)\n            else:  # dpo\n                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权\n\n        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）\n        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)\n        gamma_rejected = gamma_chosen.clone()\n        batch[\"gamma\"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)\n\n        return batch\n```\n\n### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e\n\n| 维度 | DMPO | ETADN |\n|---|---|---|\n| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |\n| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |\n| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |\n| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |\n\n---\n\n## 3. 数据 Pipeline\n\n### 3.1 DPO 数据格式\n\n每个样本包含：\n\n```json\n{\n  \"id\": \"alfworld_task_42_pair_0\",\n  \"error_type\": \"action\",\n  \"prompt\": \"You are in a kitchen. Your task is to ...\",\n  \"chosen\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: I should open it. Act: open fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You open the fridge. You see a tomato 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Found it. Act: take tomato 1 from fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: You pick up the tomato 1.\"}\n  ],\n  \"rejected\": [\n    {\"role\": \"assistant\", \"content\": \"Think: I need to find a tomato. Act: go to countertop 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a bread 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Not here. Act: go to countertop 2\"},\n    {\"role\": \"user\", \"content\": \"Obs: On the countertop you see a cup 1.\"},\n    {\"role\": \"assistant\", \"content\": \"Think: Maybe in the cabinet. Act: go to cabinet 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The cabinet is closed.\"}\n  ],\n  \"chosen_turns\": 3,\n  \"rejected_turns\": 3\n}\n```\n\n### 3.2 多轮对话处理：Turn 定义\n\nALFWorld 轨迹中每个 turn 的结构：\n\n```\nTurn t:\n  Assistant: \"Think: &lt;reasoning>. Act: &lt;action>\"    ← agent 生成\n  User:      \"Obs: &lt;environment_observation>\"        ← 环境返回\n```\n\n**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。\n\nTurn 数 T = assistant 回复的数量。\n\n### 3.3 Tokenization 与 Turn 标记\n\n```python\ndef tokenize_multiturn(example, tokenizer, max_length):\n    \"\"\"将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids\"\"\"\n    # 1. 构建完整对话（chat template）\n    messages = [{\"role\": \"system\", \"content\": example[\"prompt\"]}]\n    messages += example[\"chosen\"]  # 或 rejected\n\n    # 2. 分步 tokenize 以获取 turn 边界\n    prompt_ids = tokenizer.apply_chat_template(\n        [messages[0]], tokenize=True, add_generation_prompt=True\n    )\n\n    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1\n    completion_mask = [0] * len(prompt_ids)\n    all_ids = list(prompt_ids)\n    current_turn = 0\n\n    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs\n        # assistant 部分\n        asst_msg = messages[i]\n        asst_ids = tokenizer.encode(asst_msg[\"content\"], add_special_tokens=False)\n        # + chat template 的 role tokens\n        role_ids = tokenizer.encode(\"<|im_start|>assistant\\n\", add_special_tokens=False)\n        end_ids = tokenizer.encode(\"<|im_end|>\\n\", add_special_tokens=False)\n\n        all_ids += role_ids\n        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss\n        completion_mask += [0] * len(role_ids)\n\n        all_ids += asst_ids\n        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t\n        completion_mask += [1] * len(asst_ids)\n\n        all_ids += end_ids\n        turn_ids += [current_turn] * len(end_ids)\n        completion_mask += [1] * len(end_ids)\n\n        # user/observation 部分\n        if i + 1 < len(messages):\n            user_msg = messages[i + 1]\n            user_ids = tokenizer.encode(\n                f\"<|im_start|>user\\n{user_msg['content']}<|im_end|>\\n\",\n                add_special_tokens=False\n            )\n            all_ids += user_ids\n            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss\n            completion_mask += [0] * len(user_ids)\n\n        current_turn += 1\n\n    # 3. 截断\n    all_ids = all_ids[:max_length]\n    turn_ids = turn_ids[:max_length]\n    completion_mask = completion_mask[:max_length]\n\n    return {\n        \"input_ids\": all_ids,\n        \"turn_ids\": turn_ids,\n        \"completion_mask\": completion_mask,\n        \"num_turns\": current_turn,\n    }\n```\n\n**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。\n\n### 3.4 数据集统计预估\n\n| 维度 | 估计值 |\n|---|---|\n| ALFWorld 任务数 | ~3,500 (train split) |\n| 每任务轨迹数 | 5-10（采样多条） |\n| 有效 preference pairs | ~2,000-5,000（过滤后） |\n| 平均 turn 数 T | 5-15 |\n| 平均序列长度 | 1,500-3,000 tokens |\n\n---\n\n## 4. 模型配置\n\n### 4.1 Qwen3-8B QLoRA 配置\n\n```python\nfrom transformers import AutoModelForCausalLM, BitsAndBytesConfig\nfrom peft import LoraConfig\n\nbnb_config = BitsAndBytesConfig(\n    load_in_4bit=True,\n    bnb_4bit_quant_type=\"nf4\",\n    bnb_4bit_compute_dtype=torch.bfloat16,\n    bnb_4bit_use_double_quant=True,\n)\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    \"Qwen/Qwen3-8B\",\n    quantization_config=bnb_config,\n    torch_dtype=torch.bfloat16,\n    attn_implementation=\"flash_attention_2\",\n    device_map={\"\": device_id},  # 单卡绑定\n)\n\nlora_config = LoraConfig(\n    r=64,\n    lora_alpha=128,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                     \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_dropout=0.05,\n    task_type=\"CAUSAL_LM\",\n    bias=\"none\",\n)\n```\n\n### 4.2 Ref Model 处理\n\nQLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。\n\ntrl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确\n\n### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）\n\n| 组件 | 估计 VRAM |\n|---|---|\n| Qwen3-8B 4-bit weights | ~4.5 GB |\n| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |\n| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |\n| Gradients (bf16) | ~0.4 GB |\n| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |\n| PyTorch + CUDA overhead | ~2 GB |\n| **总计** | **~15-17 GB** |\n\n剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。\n\n**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。\n\n### 4.4 训练超参\n\n```yaml\n# config.yaml\ntraining:\n  mode: \"etadn\"            # \"dpo\" | \"dmpo\" | \"etadn\"\n  beta: 0.1                # DPO β\n  global_gamma: 0.90       # DMPO 模式下的全局 γ\n  learning_rate: 1.0e-6\n  lr_scheduler_type: \"constant_with_warmup\"\n  warmup_ratio: 0.1\n  num_train_epochs: 3\n  per_device_train_batch_size: 1\n  gradient_accumulation_steps: 16\n  gradient_checkpointing: true\n  bf16: true\n  max_length: 3072\n  max_prompt_length: 512\n  logging_steps: 5\n  save_steps: 100\n  eval_steps: 50\n  precompute_ref_log_probs: true\n  label_smoothing: 0.0\n  loss_type: \"sigmoid\"\n\nlora:\n  r: 64\n  lora_alpha: 128\n  target_modules: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"]\n  lora_dropout: 0.05\n\ngamma_e_mapping:\n  action: 0.85\n  verify: 0.92\n  plan: 0.97\n  default: 0.90\n```\n\n### 4.5 环境依赖\n\n| 包 | 要求版本 | 说明 |\n|---|---|---|\n| `trl` | **`==1.4.0`** | 必须使用此版本。1.4.0 将旧版 `get_batch_loss_metrics` / `concatenated_forward` / `get_batch_logps` 合并为 `_compute_loss`，本设计基于此 API 结构。服务器现有 1.1.0 需升级。 |\n| `transformers` | `>=4.40.0` | Qwen3 支持 |\n| `peft` | `>=0.10.0` | LoRA + BnB 集成 |\n| `bitsandbytes` | `>=0.43.0` | nf4 量化 |\n| `torch` | `>=2.1` | bf16 + flash_attention_2 |\n| `flash-attn` | `>=2.5.0` | Flash Attention 2 |\n\n**trl 1.4.0 中本设计依赖的关键 API**：\n- `DPOTrainer._compute_loss(model, inputs, return_outputs)` — 唯一的 loss 扩展点\n- `trl.trainer.utils.selective_log_softmax(logits, labels)` — per-token log prob 计算\n- `DPOConfig` — 训练配置基类\n\n**升级命令**：\n```bash\npip install trl==1.4.0\n```\n\n---\n\n## 5. 推理 Pipeline\n\n### 5.1 轨迹收集\n\n```python\n# collect_trajectories.py\n# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互\n# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）\n\nfrom vllm import LLM, SamplingParams  # 或 transformers.generate\n\nmodel = LLM(\n    model=\"path/to/qwen3-8b-merged\",  # LoRA merge 后的 checkpoint\n    tensor_parallel_size=1,\n    gpu_memory_utilization=0.85,\n    max_model_len=4096,\n)\n\nparams = SamplingParams(\n    temperature=0.7,\n    top_p=0.9,\n    max_tokens=256,      # 每步生成上限\n    stop=[\"Obs:\"],       # ALFWorld 环境会返回 Obs\n)\n\n# 循环：generate → parse action → env.step → append obs → repeat\n```\n\n**输出格式**：\n\n```json\n{\n  \"task_id\": \"pick_clean_then_place-Tomato-...\",\n  \"trajectory\": [\n    {\"role\": \"assistant\", \"content\": \"Think: ... Act: go to fridge 1\"},\n    {\"role\": \"user\", \"content\": \"Obs: The fridge is closed.\"},\n    ...\n  ],\n  \"reward\": 1,           # ALFWorld: 1=成功, 0=失败\n  \"num_steps\": 8,\n  \"task_type\": \"pick_clean_then_place\"\n}\n```\n\n### 5.2 错误分类\n\n```python\n# classify_errors.py\n# 用 Qwen3-14B-AWQ 做 zero-shot 分类\n\nCLASSIFY_PROMPT = \"\"\"Analyze the following failed trajectory in ALFWorld.\nThe agent attempted a task but failed. Identify the PRIMARY error type:\n\n- action: Wrong physical action (e.g., went to wrong location, used wrong object)\n- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)\n- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)\n\nTask: {task_description}\nSuccessful trajectory: {chosen_trajectory}\nFailed trajectory: {rejected_trajectory}\n\nRespond with ONLY one word: action, verify, or plan\"\"\"\n\n# 输出: error_type ∈ {\"action\", \"verify\", \"plan\"}\n```\n\n### 5.3 Preference Pair 构建\n\n```python\n# construct_preference.py\n\ndef construct_pairs(trajectories, error_classifications):\n    \"\"\"\n    策略：\n    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected\n    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs\n    3. 附加 error_type 标签（来自 classify_errors.py 的输出）\n    \"\"\"\n    pairs = []\n    for task_id, task_trajs in group_by_task(trajectories):\n        chosen_trajs = [t for t in task_trajs if t[\"reward\"] == 1]\n        rejected_trajs = [t for t in task_trajs if t[\"reward\"] == 0]\n\n        if not chosen_trajs or not rejected_trajs:\n            continue\n\n        best_chosen = min(chosen_trajs, key=lambda t: t[\"num_steps\"])\n\n        for rej in rejected_trajs:\n            error_type = error_classifications.get(\n                f\"{task_id}_{rej['traj_id']}\", \"default\"\n            )\n            pairs.append({\n                \"id\": f\"{task_id}_pair_{len(pairs)}\",\n                \"error_type\": error_type,\n                \"prompt\": task_description(task_id),\n                \"chosen\": best_chosen[\"trajectory\"],\n                \"rejected\": rej[\"trajectory\"],\n                \"chosen_turns\": count_assistant_turns(best_chosen[\"trajectory\"]),\n                \"rejected_turns\": count_assistant_turns(rej[\"trajectory\"]),\n            })\n\n    return pairs\n```\n\n---\n\n## 6. 完整文件结构\n\n```\nrl-active-probe-fl/\n├── train_etadn.py              # 主训练入口\n│   - 解析 config.yaml\n│   - 加载模型 + LoRA + BnB 量化\n│   - 构建 dataset + collator\n│   - 初始化 ETADNTrainer\n│   - trainer.train()\n│\n├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）\n│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted\n│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns\n│   - DMPODataCollator: 注入 gamma、pad turn_ids\n│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)\n│\n├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合\n│   - compute_phi(t, T, gamma): 单值 φ 计算\n│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重\n│   - dmpo_weighted_logps(): per_token_logps → weighted scalar\n│\n├── data_utils.py               # 数据加载与预处理\n│   - load_preference_data(path): 加载 JSON pairs\n│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization\n│   - build_dataset(): HF Dataset 构建\n│\n├── config.yaml                 # 超参配置（见 §4.4）\n│\n├── collect_trajectories.py     # 轨迹收集（§5.1）\n│   - ALFWorld 环境交互\n│   - vLLM / transformers 推理\n│   - 输出 trajectories.jsonl\n│\n├── classify_errors.py          # 错误分类（§5.2）\n│   - Qwen3-14B-AWQ zero-shot\n│   - 输出 error_classifications.json\n│\n├── construct_preference.py     # Preference pair 构建（§5.3）\n│   - 输入: trajectories + error_classifications\n│   - 输出: preference_pairs.json\n│\n├── evaluate.py                 # ALFWorld 评估\n│   - 标准 eval protocol: 134 unseen tasks\n│   - 指标: success rate, average steps\n│   - 按 task type 分组报告\n│\n├── scripts/\n│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)\n│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)\n│\n└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）\n    ├── env_wrapper.py\n    └── task_configs/\n```\n\n### 6.1 关键模块依赖关系\n\n```\nconfig.yaml\n    ↓\ntrain_etadn.py\n    ├── data_utils.py → tokenize_multiturn()\n    ├── dmpo_trainer.py → ETADNTrainer\n    │       ├── dmpo_loss.py → compute_phi_weights()\n    │       └── DMPODataCollator → gamma injection\n    └── evaluate.py (训练结束后调用)\n\ncollect_trajectories.py → trajectories.jsonl\n    ↓\nclassify_errors.py → error_classifications.json\n    ↓\nconstruct_preference.py → preference_pairs.json\n    ↓\ntrain_etadn.py (读取 preference_pairs.json)\n```\n\n---\n\n## 7. Ablation 设计\n\n### 7.1 三种模式切换\n\n通过 `config.yaml` 中 `training.mode` 字段切换：\n\n| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |\n|---|---|---|---|\n| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |\n| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |\n| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |\n\n### 7.2 代码中的模式分支\n\n在 `ETADNTrainer._compute_loss` 中：\n\n```python\nif self.mode == \"dpo\":\n    # 标准 DPO: 直接 sum\n    logps = (per_token_logps * shift_completion_mask).sum(dim=1)\nelse:\n    # dmpo 或 etadn: φ-weighted sum\n    # gamma 已由 collator 注入到 batch[\"gamma\"]\n    token_phi = compute_phi_weights(\n        turn_ids=batch[\"turn_ids\"][:, 1:],  # shift 对齐\n        gamma=batch[\"gamma\"],\n        num_turns=batch[\"num_turns\"],\n        max_turns=batch[\"turn_ids\"].max().item() + 1,\n    )\n    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n```\n\n### 7.3 实验矩阵\n\n| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)\n\n### 7.4 评估指标\n\n| 指标 | 说明 |\n|---|---|\n| ALFWorld success rate (overall) | 主指标，134 unseen tasks |\n| Success rate per task type | 6 种 task type 的分项成功率 |\n| Average steps to success | 效率指标 |\n| Error type distribution shift | 训练前后的错误类型分布变化 |\n| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |\n| Training loss curve | 收敛性对比 |\n\n---\n\n## 8. ETADNTrainer 核心代码骨架\n\n```python\n# dmpo_trainer.py\n\nfrom trl import DPOTrainer, DPOConfig\nfrom dmpo_loss import compute_phi_weights\n\nclass ETADNConfig(DPOConfig):\n    mode: str = \"etadn\"          # \"dpo\" | \"dmpo\" | \"etadn\"\n    global_gamma: float = 0.90\n    gamma_e_mapping: dict = None  # {\"action\": 0.85, \"verify\": 0.92, \"plan\": 0.97}\n\n\nclass ETADNTrainer(DPOTrainer):\n\n    def __init__(self, *args, mode=\"etadn\", global_gamma=0.9, gamma_e_mapping=None, **kwargs):\n        super().__init__(*args, **kwargs)\n        self.mode = mode\n        self.global_gamma = global_gamma\n        self.gamma_e_mapping = gamma_e_mapping or {}\n\n    def _compute_loss(self, model, inputs, return_outputs=False):\n        \"\"\"Override: DMPO φ-weighted log probability aggregation.\"\"\"\n        # --- 1. 提取额外字段 ---\n        turn_ids = inputs.pop(\"turn_ids\", None)\n        num_turns = inputs.pop(\"num_turns\", None)\n        gamma = inputs.pop(\"gamma\", None)\n        completion_mask = inputs[\"completion_mask\"]\n        input_ids = inputs[\"input_ids\"]\n\n        # --- 2. Policy forward ---\n        model_kwargs = {k: v for k, v in inputs.items()\n                        if k not in (\"completion_mask\", \"ref_chosen_logps\", \"ref_rejected_logps\")}\n        outputs = model(**model_kwargs)\n\n        # --- 3. Per-token logps ---\n        from trl.trainer.utils import selective_log_softmax\n        shift_logits = outputs.logits[..., :-1, :].contiguous()\n        shift_labels = input_ids[..., 1:].contiguous()\n        shift_completion_mask = completion_mask[..., 1:].contiguous()\n        per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n        per_token_logps[shift_completion_mask == 0] = 0.0\n\n        # --- 4. 聚合（核心修改点） ---\n        if self.mode == \"dpo\" or turn_ids is None:\n            logps = per_token_logps.sum(dim=1)\n        else:\n            shift_turn_ids = turn_ids[..., 1:].contiguous()\n            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,\n                                            max_turns=shift_turn_ids.max().item() + 1)\n            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\n        chosen_logps, rejected_logps = logps.chunk(2, dim=0)\n\n        # --- 5. Reference logps ---\n        if \"ref_chosen_logps\" in inputs:\n            ref_chosen_logps = inputs[\"ref_chosen_logps\"]\n            ref_rejected_logps = inputs[\"ref_rejected_logps\"]\n        else:\n            with torch.no_grad():\n                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(\n                    model, inputs, shift_completion_mask,\n                    turn_ids=shift_turn_ids if self.mode != \"dpo\" else None,\n                    gamma=gamma, num_turns=num_turns,\n                )\n\n        # --- 6. Loss (sigmoid, same as standard DPO) ---\n        chosen_logratios = chosen_logps - ref_chosen_logps\n        rejected_logratios = rejected_logps - ref_rejected_logps\n        logits = chosen_logratios - rejected_logratios\n\n        loss = -F.logsigmoid(self.beta * logits).mean()\n\n        # --- 7. Metrics ---\n        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()\n        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()\n        reward_margin = (chosen_rewards - rejected_rewards).mean()\n\n        metrics = {\n            \"loss\": loss.detach().item(),\n            \"rewards/chosen\": chosen_rewards.mean().item(),\n            \"rewards/rejected\": rejected_rewards.mean().item(),\n            \"rewards/margin\": reward_margin.item(),\n        }\n        self.store_metrics(metrics, train_eval=\"train\")\n\n        if return_outputs:\n            return loss, {\"logits\": logits}\n        return loss\n```\n\n---\n\n## 9. 风险与注意事项\n\n| 风险 | 缓解 |\n|---|---|\n| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |\n| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |\n| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |\n| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |\n| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |\n\n---\n\n## 10. 实施优先级\n\n| Phase | 内容 | 估计时间 |\n|---|---|---|\n| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |\n| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |\n| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |\n| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |\n| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |\n| P6 | 完整训练 + 评估 | 2-3 天 |\n",
    "structuredPatch": [
      {
        "oldStart": 895,
        "oldLines": 7,
        "newStart": 895,
        "newLines": 7,
        "lines": [
          " | `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |",
          " | trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |",
          " | Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |",
          "-| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |",
          "+| φ 权重导致梯度尺度变化 | 需通过 §1.4 归一化验证确认 Σφ 的实际值。若 Σφ ≠ 1 且偏差显著，可在 `compute_phi_weights` 中添加归一化选项，或调整 β 补偿尺度 |",
          " | γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |",
          " ",
          " ---"
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

Now copy the changes to the unregistered duplicate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "b82dc472-61df-4a71-8ff9-7627d54a2525",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6JXpTWuzwgy6woAkw3CHY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 43079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 460
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_019ktnpWaEkxHpumcdduS4d8`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2.md",
  "description": "Copy updated file to unregistered duplicate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "ae323a02-db8a-4671-87d2-836ffe020be9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6JXpTWuzwgy6woAkw3CHY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 43079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 460
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T11:01:54.714Z_

<details><summary>↩ Tool result · `toolu_019ktnpWaEkxHpumcdduS4d8`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "8484080f-b690-4f6c-9b31-9f946d21acf2",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Assistant

_source line 29_

验证修改结果，读取关键部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "0d167a63-9f6b-49e0-a009-3a16c2994a71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ9ZKVdnZWD3yCuqHPeZBX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 43539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01KBCiDbwnghkHqe3b7r2RHx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": 113,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "5e40940f-1648-4e0f-8cf7-f339cf9d76db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ9ZKVdnZWD3yCuqHPeZBX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 43539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-12T11:01:58.758Z_

<details><summary>↩ Tool result · `toolu_01KBCiDbwnghkHqe3b7r2RHx`</summary>

````text
113	### 1.4 φ(t,T) 归一化验证
114	
115	在实现前需验证 Σ_{t=0}^{T-1} φ(t,T,γ) 在不同 γ 和 T 下的值，确认 φ 是否归一化（即是否 Σφ = 1）。如果 Σφ ≠ 1，需检查 DMPO 论文原始设计意图——可能有意不归一化，利用非归一化引入 length bias（较长轨迹整体权重更大）。
116	
117	**单元测试**：
118	
119	```python
120	import math
121	
122	def phi(t, T, gamma):
123	    """DMPO 时间折扣函数"""
124	    return gamma**t * (1 - gamma**(T - t)) / (1 - gamma**T)
125	
126	def test_phi_normalization():
127	    print("=== φ(t,T) 归一化验证 ===")
128	    for gamma in [0.85, 0.92, 0.97]:
129	        for T in [5, 10, 20, 40]:
130	            phi_sum = sum(phi(t, T, gamma) for t in range(T))
131	            normalized = "✓" if abs(phi_sum - 1.0) < 1e-6 else "✗"
132	            print(f"γ={gamma}, T={T:2d}: Σφ={phi_sum:.6f}  {normalized}")
133	    print()
134	    print("如果 Σφ ≠ 1:")
135	    print("  1. 检查 DMPO 论文 Eq.16 是否有意不归一化")
136	    print("  2. 若有意：长轨迹获得更大总权重 → implicit length bias")
137	    print("  3. 若需归一化：可在 compute_phi_weights 中除以 Σφ")
138	    print("  4. 非归一化时可能需要调整 β 以补偿尺度变化")
139	
140	if __name__ == "__main__":
141	    test_phi_normalization()
142	```
143	
144	此测试应在 P1 阶段（`dmpo_loss.py` 单元测试）中执行。若 Σφ 显著偏离 1，需在 §9 风险表中记录应对方案，并决定是否在 `compute_phi_weights` 中添加归一化选项。
145	
146	### 1.5 φ(t,T) 权重应用到 per-turn loss
147	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "a7a6163d-f45b-4d8b-85ad-25dcc1288400",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
      "content": "### 1.4 φ(t,T) 归一化验证\n\n在实现前需验证 Σ_{t=0}^{T-1} φ(t,T,γ) 在不同 γ 和 T 下的值，确认 φ 是否归一化（即是否 Σφ = 1）。如果 Σφ ≠ 1，需检查 DMPO 论文原始设计意图——可能有意不归一化，利用非归一化引入 length bias（较长轨迹整体权重更大）。\n\n**单元测试**：\n\n```python\nimport math\n\ndef phi(t, T, gamma):\n    \"\"\"DMPO 时间折扣函数\"\"\"\n    return gamma**t * (1 - gamma**(T - t)) / (1 - gamma**T)\n\ndef test_phi_normalization():\n    print(\"=== φ(t,T) 归一化验证 ===\")\n    for gamma in [0.85, 0.92, 0.97]:\n        for T in [5, 10, 20, 40]:\n            phi_sum = sum(phi(t, T, gamma) for t in range(T))\n            normalized = \"✓\" if abs(phi_sum - 1.0) < 1e-6 else \"✗\"\n            print(f\"γ={gamma}, T={T:2d}: Σφ={phi_sum:.6f}  {normalized}\")\n    print()\n    print(\"如果 Σφ ≠ 1:\")\n    print(\"  1. 检查 DMPO 论文 Eq.16 是否有意不归一化\")\n    print(\"  2. 若有意：长轨迹获得更大总权重 → implicit length bias\")\n    print(\"  3. 若需归一化：可在 compute_phi_weights 中除以 Σφ\")\n    print(\"  4. 非归一化时可能需要调整 β 以补偿尺度变化\")\n\nif __name__ == \"__main__\":\n    test_phi_normalization()\n```\n\n此测试应在 P1 阶段（`dmpo_loss.py` 单元测试）中执行。若 Σφ 显著偏离 1，需在 §9 风险表中记录应对方案，并决定是否在 `compute_phi_weights` 中添加归一化选项。\n\n### 1.5 φ(t,T) 权重应用到 per-turn loss\n",
      "numLines": 35,
      "startLine": 113,
      "totalLines": 913
    }
  }
}
````

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01SbWAuv2AUMvDdJ6gxXV2vt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": 364,
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
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "cfb90e23-8c47-42b0-b636-d630033ca1cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ9ZKVdnZWD3yCuqHPeZBX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 43539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T11:01:59.657Z_

<details><summary>↩ Tool result · `toolu_01SbWAuv2AUMvDdJ6gxXV2vt`</summary>

````text
364	
365	```python
366	from transformers import AutoModelForCausalLM, BitsAndBytesConfig
367	from peft import LoraConfig
368	
369	bnb_config = BitsAndBytesConfig(
370	    load_in_4bit=True,
371	    bnb_4bit_quant_type="nf4",
372	    bnb_4bit_compute_dtype=torch.bfloat16,
373	    bnb_4bit_use_double_quant=True,
374	)
375	
376	model = AutoModelForCausalLM.from_pretrained(
377	    "Qwen/Qwen3-8B",
378	    quantization_config=bnb_config,
379	    torch_dtype=torch.bfloat16,
380	    attn_implementation="flash_attention_2",
381	    device_map={"": device_id},  # 单卡绑定
382	)
383	
384	lora_config = LoraConfig(
385	    r=64,
386	    lora_alpha=128,
387	    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
388	                     "gate_proj", "up_proj", "down_proj"],
389	    lora_dropout=0.05,
390	    task_type="CAUSAL_LM",
391	    bias="none",
392	)
393	```
394	
395	### 4.2 Ref Model 处理
396	
397	QLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。
398	
399	trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：
400	1. 创建 "ref" adapter 副本（复制 default adapter 权重）
401	2. 前向传播时通过 `use_adapter(model, "ref")` 切换到冻结的初始权重
402	3. 或者直接 `model.disable_adapter()` → base model = ref model
403	
404	**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。
405	
406	> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**
407	>
408	> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。
409	>
410	> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。
411	
412	**预计算流程**：
413	
414	```python
415	def precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):
416	    """预计算 ref model 的 φ-weighted log probs"""
417	    ref_model.eval()
418	    ref_model.disable_adapter()  # base model = ref model
419	
420	    ref_chosen_logps_list = []
421	    ref_rejected_logps_list = []
422	
423	    with torch.no_grad():
424	        for sample in dataset:
425	            for key in ("chosen", "rejected"):
426	                input_ids = sample[f"{key}_input_ids"]
427	                completion_mask = sample[f"{key}_completion_mask"]
428	                turn_ids = sample[f"{key}_turn_ids"]
429	                num_turns = sample[f"{key}_num_turns"]
430	
431	                # 1. Per-token logps
432	                outputs = ref_model(input_ids=input_ids.unsqueeze(0))
433	                shift_logits = outputs.logits[..., :-1, :].contiguous()
434	                shift_labels = input_ids[1:].unsqueeze(0)
435	                per_token_logps = selective_log_softmax(shift_logits, shift_labels)
436	                shift_mask = completion_mask[1:]
437	
438	                # 2. φ-weighted 聚合（与训练一致）
439	                if mode == "dpo":
440	                    logps = (per_token_logps * shift_mask).sum(dim=1)
441	                else:
442	                    gamma_e = gamma_e_mapping.get(sample["error_type"], gamma_e_mapping["default"])
443	                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "730dada2-69d7-43d6-a4df-fe039c2ec821",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
      "content": "\n```python\nfrom transformers import AutoModelForCausalLM, BitsAndBytesConfig\nfrom peft import LoraConfig\n\nbnb_config = BitsAndBytesConfig(\n    load_in_4bit=True,\n    bnb_4bit_quant_type=\"nf4\",\n    bnb_4bit_compute_dtype=torch.bfloat16,\n    bnb_4bit_use_double_quant=True,\n)\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    \"Qwen/Qwen3-8B\",\n    quantization_config=bnb_config,\n    torch_dtype=torch.bfloat16,\n    attn_implementation=\"flash_attention_2\",\n    device_map={\"\": device_id},  # 单卡绑定\n)\n\nlora_config = LoraConfig(\n    r=64,\n    lora_alpha=128,\n    target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                     \"gate_proj\", \"up_proj\", \"down_proj\"],\n    lora_dropout=0.05,\n    task_type=\"CAUSAL_LM\",\n    bias=\"none\",\n)\n```\n\n### 4.2 Ref Model 处理\n\nQLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。\n\ntrl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)",
      "numLines": 80,
      "startLine": 364,
      "totalLines": 913
    }
  }
}
````

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01TGSEzKQ8dtCd9dDwuiDZTT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": 454,
  "limit": 45
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "1c9adf5d-86b4-4787-8681-8c9d28e624e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ9ZKVdnZWD3yCuqHPeZBX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 43539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-12T11:02:00.597Z_

<details><summary>↩ Tool result · `toolu_01TGSEzKQ8dtCd9dDwuiDZTT`</summary>

````text
454	
455	    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）
456	    del ref_model
457	    torch.cuda.empty_cache()
458	
459	    return ref_chosen_logps_list, ref_rejected_logps_list
460	```
461	
462	**优势**：
463	- 训练时无需 ref model 前向传播，节省 ~30% VRAM
464	- 训练速度提升 ~40%
465	- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确
466	
467	### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）
468	
469	| 组件 | 估计 VRAM |
470	|---|---|
471	| Qwen3-8B 4-bit weights | ~4.5 GB |
472	| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |
473	| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |
474	| Gradients (bf16) | ~0.4 GB |
475	| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |
476	| PyTorch + CUDA overhead | ~2 GB |
477	| **总计** | **~15-17 GB** |
478	
479	剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。
480	
481	**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。
482	
483	### 4.4 训练超参
484	
485	```yaml
486	# config.yaml
487	training:
488	  mode: "etadn"            # "dpo" | "dmpo" | "etadn"
489	  beta: 0.1                # DPO β
490	  global_gamma: 0.90       # DMPO 模式下的全局 γ
491	  learning_rate: 1.0e-6
492	  lr_scheduler_type: "constant_with_warmup"
493	  warmup_ratio: 0.1
494	  num_train_epochs: 3
495	  per_device_train_batch_size: 1
496	  gradient_accumulation_steps: 16
497	  gradient_checkpointing: true
498	  bf16: true
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "58951ba2-9468-4ac2-b12b-9eeff5be92e3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
      "content": "\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确\n\n### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）\n\n| 组件 | 估计 VRAM |\n|---|---|\n| Qwen3-8B 4-bit weights | ~4.5 GB |\n| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |\n| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |\n| Gradients (bf16) | ~0.4 GB |\n| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |\n| PyTorch + CUDA overhead | ~2 GB |\n| **总计** | **~15-17 GB** |\n\n剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。\n\n**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。\n\n### 4.4 训练超参\n\n```yaml\n# config.yaml\ntraining:\n  mode: \"etadn\"            # \"dpo\" | \"dmpo\" | \"etadn\"\n  beta: 0.1                # DPO β\n  global_gamma: 0.90       # DMPO 模式下的全局 γ\n  learning_rate: 1.0e-6\n  lr_scheduler_type: \"constant_with_warmup\"\n  warmup_ratio: 0.1\n  num_train_epochs: 3\n  per_device_train_batch_size: 1\n  gradient_accumulation_steps: 16\n  gradient_checkpointing: true\n  bf16: true",
      "numLines": 45,
      "startLine": 454,
      "totalLines": 913
    }
  }
}
````

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01RiDjpj1M5P2guAvUzZXnBK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": 720,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "c8fd459c-9e7a-4874-902c-c98e95042b30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ9ZKVdnZWD3yCuqHPeZBX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 43539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-12T11:02:01.655Z_

<details><summary>↩ Tool result · `toolu_01RiDjpj1M5P2guAvUzZXnBK`</summary>

````text
720	    ↓
721	classify_errors.py → error_classifications.json
722	    ↓
723	construct_preference.py → preference_pairs.json
724	    ↓
725	train_etadn.py (读取 preference_pairs.json)
726	```
727	
728	---
729	
730	## 7. Ablation 设计
731	
732	### 7.1 三种模式切换
733	
734	通过 `config.yaml` 中 `training.mode` 字段切换：
735	
736	| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |
737	|---|---|---|---|
738	| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |
739	| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |
740	| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |
741	
742	### 7.2 代码中的模式分支
743	
744	在 `ETADNTrainer._compute_loss` 中：
745	
746	```python
747	if self.mode == "dpo":
748	    # 标准 DPO: 直接 sum
749	    logps = (per_token_logps * shift_completion_mask).sum(dim=1)
750	else:
751	    # dmpo 或 etadn: φ-weighted sum
752	    # gamma 已由 collator 注入到 batch["gamma"]
753	    token_phi = compute_phi_weights(
754	        turn_ids=batch["turn_ids"][:, 1:],  # shift 对齐
755	        gamma=batch["gamma"],
756	        num_turns=batch["num_turns"],
757	        max_turns=batch["turn_ids"].max().item() + 1,
758	    )
759	    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "e11698fc-b1b2-4273-87ae-91e17746308b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
      "content": "    ↓\nclassify_errors.py → error_classifications.json\n    ↓\nconstruct_preference.py → preference_pairs.json\n    ↓\ntrain_etadn.py (读取 preference_pairs.json)\n```\n\n---\n\n## 7. Ablation 设计\n\n### 7.1 三种模式切换\n\n通过 `config.yaml` 中 `training.mode` 字段切换：\n\n| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |\n|---|---|---|---|\n| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |\n| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |\n| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |\n\n### 7.2 代码中的模式分支\n\n在 `ETADNTrainer._compute_loss` 中：\n\n```python\nif self.mode == \"dpo\":\n    # 标准 DPO: 直接 sum\n    logps = (per_token_logps * shift_completion_mask).sum(dim=1)\nelse:\n    # dmpo 或 etadn: φ-weighted sum\n    # gamma 已由 collator 注入到 batch[\"gamma\"]\n    token_phi = compute_phi_weights(\n        turn_ids=batch[\"turn_ids\"][:, 1:],  # shift 对齐\n        gamma=batch[\"gamma\"],\n        num_turns=batch[\"num_turns\"],\n        max_turns=batch[\"turn_ids\"].max().item() + 1,\n    )\n    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)",
      "numLines": 40,
      "startLine": 720,
      "totalLines": 913
    }
  }
}
````

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_015g9ABY5y2t8VTXqZMZaQtV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": 845,
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
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "9137efa5-a52c-4336-a7d4-094579c2653a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ9ZKVdnZWD3yCuqHPeZBX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 43539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-12T11:02:02.409Z_

<details><summary>↩ Tool result · `toolu_015g9ABY5y2t8VTXqZMZaQtV`</summary>

```text
845	            shift_turn_ids = turn_ids[..., 1:].contiguous()
846	            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,
847	                                            max_turns=shift_turn_ids.max().item() + 1)
848	            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)
849	
850	        chosen_logps, rejected_logps = logps.chunk(2, dim=0)
851	
852	        # --- 5. Reference logps ---
853	        if "ref_chosen_logps" in inputs:
854	            ref_chosen_logps = inputs["ref_chosen_logps"]
855	            ref_rejected_logps = inputs["ref_rejected_logps"]
856	        else:
857	            with torch.no_grad():
858	                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(
859	                    model, inputs, shift_completion_mask,
860	                    turn_ids=shift_turn_ids if self.mode != "dpo" else None,
861	                    gamma=gamma, num_turns=num_turns,
862	                )
863	
864	        # --- 6. Loss (sigmoid, same as standard DPO) ---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "80f1d28f-6c22-413a-a552-2f31c1941c28",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
      "content": "            shift_turn_ids = turn_ids[..., 1:].contiguous()\n            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,\n                                            max_turns=shift_turn_ids.max().item() + 1)\n            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)\n\n        chosen_logps, rejected_logps = logps.chunk(2, dim=0)\n\n        # --- 5. Reference logps ---\n        if \"ref_chosen_logps\" in inputs:\n            ref_chosen_logps = inputs[\"ref_chosen_logps\"]\n            ref_rejected_logps = inputs[\"ref_rejected_logps\"]\n        else:\n            with torch.no_grad():\n                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(\n                    model, inputs, shift_completion_mask,\n                    turn_ids=shift_turn_ids if self.mode != \"dpo\" else None,\n                    gamma=gamma, num_turns=num_turns,\n                )\n\n        # --- 6. Loss (sigmoid, same as standard DPO) ---",
      "numLines": 20,
      "startLine": 845,
      "totalLines": 913
    }
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Let me also verify the experiment matrix section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "f97f7bee-daab-4d6a-9431-84335e663e81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6ksU3quuC7JCRarDWrPMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4662,
      "cache_read_input_tokens": 43753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4662
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01RqfFVwJbia9PWUkVybnfcT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": 762,
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
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "c00a5b1a-0411-47e2-bf1e-b4ff55507c89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6ksU3quuC7JCRarDWrPMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4662,
      "cache_read_input_tokens": 43753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4662
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T11:02:06.773Z_

<details><summary>↩ Tool result · `toolu_01RqfFVwJbia9PWUkVybnfcT`</summary>

```text
762	### 7.3 实验矩阵
763	
764	| Run | Mode | γ / γ_e | GPU | Seed | 目的 |
765	|---|---|---|---|---|---|
766	| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |
767	| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |
768	| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |
769	| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |
770	| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |
771	| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |
772	| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |
773	
774	**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。
775	
776	**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。
777	
778	**调度顺序**：
779	1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号
780	2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)
781	3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)
782	4. 轮 4: A1 (DPO baseline seed=42, GPU0)
783	
784	### 7.4 评估指标
785	
786	| 指标 | 说明 |
787	|---|---|
788	| ALFWorld success rate (overall) | 主指标，134 unseen tasks |
789	| Success rate per task type | 6 种 task type 的分项成功率 |
790	| Average steps to success | 效率指标 |
791	| Error type distribution shift | 训练前后的错误类型分布变化 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "007db8ef-cd88-4568-8499-0ed1f6225e14",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
      "content": "### 7.3 实验矩阵\n\n| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)\n\n### 7.4 评估指标\n\n| 指标 | 说明 |\n|---|---|\n| ALFWorld success rate (overall) | 主指标，134 unseen tasks |\n| Success rate per task type | 6 种 task type 的分项成功率 |\n| Average steps to success | 效率指标 |\n| Error type distribution shift | 训练前后的错误类型分布变化 |",
      "numLines": 30,
      "startLine": 762,
      "totalLines": 913
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

全部 4 项修改已完成，两个文件均已更新。修改摘要：

1. **§4.2 precompute_ref_log_probs**：添加 φ-weighted 聚合约束说明 + 完整预计算伪代码（传入 turn_ids 和 gamma_e）；§9 风险表标记为已解决
2. **§7.3 实验矩阵**：ETADN 3 seeds + DMPO 3 seeds (γ=0.92) + DPO 1 seed = 7 runs；添加 4 轮调度顺序
3. **§4.5 环境依赖**：新增小节，明确 `trl==1.4.0` 及依赖的关键 API（`_compute_loss`、`selective_log_softmax`、`DPOConfig`）
4. **§1.4 φ(t,T) 归一化验证**：新增小节，包含测试代码框架和 Σφ ≠ 1 时的处理方案

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "uuid": "167e0b19-a841-41f2-bb6a-aa5f84109967",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgjPSUnJ1h2two3WLCmNuo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 48415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 879
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 44_

全部 4 项修改已完成，两个文件均已更新。修改摘要：

1. **§4.2 precompute_ref_log_probs**：添加 φ-weighted 聚合约束说明 + 完整预计算伪代码（传入 turn_ids 和 gamma_e）；§9 风险表标记为已解决
2. **§7.3 实验矩阵**：ETADN 3 seeds + DMPO 3 seeds (γ=0.92) + DPO 1 seed = 7 runs；添加 4 轮调度顺序
3. **§4.5 环境依赖**：新增小节，明确 `trl==1.4.0` 及依赖的关键 API（`_compute_loss`、`selective_log_softmax`、`DPOConfig`）
4. **§1.4 φ(t,T) 归一化验证**：新增小节，包含测试代码框架和 Σφ ≠ 1 时的处理方案

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 134322,
  "duration_api_ms": 135088,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "14e84441-53cb-4bc8-9441-31ff9df580e7",
  "total_cost_usd": 0.6517302500000002,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 37453,
    "cache_read_input_tokens": 456004,
    "output_tokens": 7495,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37453,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 296,
        "cache_read_input_tokens": 48415,
        "cache_creation_input_tokens": 879,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 879
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2122,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002202,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 7495,
      "cacheReadInputTokens": 456004,
      "cacheCreationInputTokens": 37453,
      "webSearchRequests": 0,
      "costUSD": 0.6495282500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6438e48a-b10b-4248-a519-2871b93f9fc2"
}
```

</details>

---
