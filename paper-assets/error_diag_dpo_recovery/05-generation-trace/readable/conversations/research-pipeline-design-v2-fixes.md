# research pipeline design v2 fixes

**error diag dpo recovery** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_research_pipeline-design-v2-fixes_20260512T105951.jsonl`
- **Structured JSON:** [`4a88c59cbf0009527e91.json`](../../sessions/4a/4a88c59cbf0009527e91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-12T11:02:15.942073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T11:02:15.942596+00:00_

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
65	**Turn 边界标记**：在数据预处理阶段，为每个 to
…[truncated 25282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T11:02:15.942934+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

````json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`。训练前一次性计算所有样本的 ref logps 并缓存为 `.npz`，训练时从 dataset 直接读取。优势：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%",
  "new_string": "trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "old_string": "trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`。训练前一次性计算所有样本的 ref logps 并缓存为 `.npz`，训练时从 dataset 直接读取。优势：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%",
    "new_string": "trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：\n1. 创建 \"ref\" adapter 副本（复制 default adapter 权重）\n2. 前向传播时通过 `use_adapter(model, \"ref\")` 切换到冻结的初始权重\n3. 或者直接 `model.disable_adapter()` → base model = ref model\n\n**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。\n\n> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**\n>\n> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。\n>\n> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。\n\n**预计算流程**：\n\n```python\ndef precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):\n    \"\"\"预计算 ref model 的 φ-weighted log probs\"\"\"\n    ref_model.eval()\n    ref_model.disable_adapter()  # base model = ref model\n\n    ref_chosen_logps_list = []\n    ref_rejected_logps_list = []\n\n    with torch.no_grad():\n        for sample in dataset:\n            for key in (\"chosen\", \"rejected\"):\n                input_ids = sample[f\"{key}_input_ids\"]\n                completion_mask = sample[f\"{key}_completion_mask\"]\n                turn_ids = sample[f\"{key}_turn_ids\"]\n                num_turns = sample[f\"{key}_num_turns\"]\n\n                # 1. Per-token logps\n                outputs = ref_model(input_ids=input_ids.unsqueeze(0))\n                shift_logits = outputs.logits[..., :-1, :].contiguous()\n                shift_labels = input_ids[1:].unsqueeze(0)\n                per_token_logps = selective_log_softmax(shift_logits, shift_labels)\n                shift_mask = completion_mask[1:]\n\n                # 2. φ-weighted 聚合（与训练一致）\n                if mode == \"dpo\":\n                    logps = (per_token_logps * shift_mask).sum(dim=1)\n                else:\n                    gamma_e = gamma_e_mapping.get(sample[\"error_type\"], gamma_e_mapping[\"default\"])\n                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)\n                    T = torch.tensor([num_turns], device=input_ids.device)\n                    shift_turn_ids = turn_ids[1:].unsqueeze(0)\n                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,\n                                                    max_turns=shift_turn_ids.max().item() + 1)\n                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)\n\n                if key == \"chosen\":\n                    ref_chosen_logps_list.append(logps.item())\n                else:\n                    ref_rejected_logps_list.append(logps.item())\n\n    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）\n    del ref_model\n    torch.cuda.empty_cache()\n\n    return ref_chosen_logps_list, ref_rejected_logps_list\n```\n\n**优势**：\n- 训练时无需 ref model 前向传播，节省 ~30% VRAM\n- 训练速度提升 ~40%\n- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确"
  }
}
````

</details>

---

### Tool result

_source line 4 · 2026-05-12T11:02:15.943254+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T11:02:15.943420+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| A2 | dpo | — | 1 | 42 | Baseline 复现 |\n| B1 | dmpo | 0.90 | 0 | 42 | Baseline: DMPO 全局 γ |\n| B2 | dmpo | 0.85 | 1 | 42 | DMPO γ 敏感性 |\n| C1 | etadn | per-sample | 0 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 1 | 123 | Ours 不同 seed |\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run。6 个 run 分 3 轮完成。",
  "new_string": "| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "old_string": "| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| A2 | dpo | — | 1 | 42 | Baseline 复现 |\n| B1 | dmpo | 0.90 | 0 | 42 | Baseline: DMPO 全局 γ |\n| B2 | dmpo | 0.85 | 1 | 42 | DMPO γ 敏感性 |\n| C1 | etadn | per-sample | 0 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 1 | 123 | Ours 不同 seed |\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run。6 个 run 分 3 轮完成。",
    "new_string": "| Run | Mode | γ / γ_e | GPU | Seed | 目的 |\n|---|---|---|---|---|---|\n| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |\n| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |\n| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |\n| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |\n| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |\n| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |\n| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |\n\n**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。\n\n**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。\n\n**调度顺序**：\n1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号\n2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)\n3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)\n4. 轮 4: A1 (DPO baseline seed=42, GPU0)"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T11:02:15.943727+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T11:02:15.943904+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |",
  "new_string": "| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "old_string": "| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | ref logps 也必须用相同 φ 加权。需确认 precompute 阶段和训练阶段使用一致的 turn_ids 和 gamma |",
    "new_string": "| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T11:02:15.944163+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T11:02:15.944331+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |",
  "new_string": "| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "old_string": "| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 trl 版本（pip install trl==1.4.0），在代码中 assert 关键接口存在 |",
    "new_string": "| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T11:02:15.944561+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T11:02:15.944734+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

````json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "---\n\n## 5. 推理 Pipeline",
  "new_string": "### 4.5 环境依赖\n\n| 包 | 要求版本 | 说明 |\n|---|---|---|\n| `trl` | **`==1.4.0`** | 必须使用此版本。1.4.0 将旧版 `get_batch_loss_metrics` / `concatenated_forward` / `get_batch_logps` 合并为 `_compute_loss`，本设计基于此 API 结构。服务器现有 1.1.0 需升级。 |\n| `transformers` | `>=4.40.0` | Qwen3 支持 |\n| `peft` | `>=0.10.0` | LoRA + BnB 集成 |\n| `bitsandbytes` | `>=0.43.0` | nf4 量化 |\n| `torch` | `>=2.1` | bf16 + flash_attention_2 |\n| `flash-attn` | `>=2.5.0` | Flash Attention 2 |\n\n**trl 1.4.0 中本设计依赖的关键 API**：\n- `DPOTrainer._compute_loss(model, inputs, return_outputs)` — 唯一的 loss 扩展点\n- `trl.trainer.utils.selective_log_softmax(logits, labels)` — per-token log prob 计算\n- `DPOConfig` — 训练配置基类\n\n**升级命令**：\n```bash\npip install trl==1.4.0\n```\n\n---\n\n## 5. 推理 Pipeline"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "old_string": "---\n\n## 5. 推理 Pipeline",
    "new_string": "### 4.5 环境依赖\n\n| 包 | 要求版本 | 说明 |\n|---|---|---|\n| `trl` | **`==1.4.0`** | 必须使用此版本。1.4.0 将旧版 `get_batch_loss_metrics` / `concatenated_forward` / `get_batch_logps` 合并为 `_compute_loss`，本设计基于此 API 结构。服务器现有 1.1.0 需升级。 |\n| `transformers` | `>=4.40.0` | Qwen3 支持 |\n| `peft` | `>=0.10.0` | LoRA + BnB 集成 |\n| `bitsandbytes` | `>=0.43.0` | nf4 量化 |\n| `torch` | `>=2.1` | bf16 + flash_attention_2 |\n| `flash-attn` | `>=2.5.0` | Flash Attention 2 |\n\n**trl 1.4.0 中本设计依赖的关键 API**：\n- `DPOTrainer._compute_loss(model, inputs, return_outputs)` — 唯一的 loss 扩展点\n- `trl.trainer.utils.selective_log_softmax(logits, labels)` — per-token log prob 计算\n- `DPOConfig` — 训练配置基类\n\n**升级命令**：\n```bash\npip install trl==1.4.0\n```\n\n---\n\n## 5. 推理 Pipeline"
  }
}
````

</details>

---

### Tool result

_source line 12 · 2026-05-12T11:02:15.944981+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-12T11:02:15.945140+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

````json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "### 1.4 φ(t,T) 权重应用到 per-turn loss",
  "new_string": "### 1.4 φ(t,T) 归一化验证\n\n在实现前需验证 Σ_{t=0}^{T-1} φ(t,T,γ) 在不同 γ 和 T 下的值，确认 φ 是否归一化（即是否 Σφ = 1）。如果 Σφ ≠ 1，需检查 DMPO 论文原始设计意图——可能有意不归一化，利用非归一化引入 length bias（较长轨迹整体权重更大）。\n\n**单元测试**：\n\n```python\nimport math\n\ndef phi(t, T, gamma):\n    \"\"\"DMPO 时间折扣函数\"\"\"\n    return gamma**t * (1 - gamma**(T - t)) / (1 - gamma**T)\n\ndef test_phi_normalization():\n    print(\"=== φ(t,T) 归一化验证 ===\")\n    for gamma in [0.85, 0.92, 0.97]:\n        for T in [5, 10, 20, 40]:\n            phi_sum = sum(phi(t, T, gamma) for t in range(T))\n            normalized = \"✓\" if abs(phi_sum - 1.0) < 1e-6 else \"✗\"\n            print(f\"γ={gamma}, T={T:2d}: Σφ={phi_sum:.6f}  {normalized}\")\n    print()\n    print(\"如果 Σφ ≠ 1:\")\n    print(\"  1. 检查 DMPO 论文 Eq.16 是否有意不归一化\")\n    print(\"  2. 若有意：长轨迹获得更大总权重 → implicit length bias\")\n    print(\"  3. 若需归一化：可在 compute_phi_weights 中除以 Σφ\")\n    print(\"  4. 非归一化时可能需要调整 β 以补偿尺度变化\")\n\nif __name__ == \"__main__\":\n    test_phi_normalization()\n```\n\n此测试应在 P1 阶段（`dmpo_loss.py` 单元测试）中执行。若 Σφ 显著偏离 1，需在 §9 风险表中记录应对方案，并决定是否在 `compute_phi_weights` 中添加归一化选项。\n\n### 1.5 φ(t,T) 权重应用到 per-turn loss"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "old_string": "### 1.4 φ(t,T) 权重应用到 per-turn loss",
    "new_string": "### 1.4 φ(t,T) 归一化验证\n\n在实现前需验证 Σ_{t=0}^{T-1} φ(t,T,γ) 在不同 γ 和 T 下的值，确认 φ 是否归一化（即是否 Σφ = 1）。如果 Σφ ≠ 1，需检查 DMPO 论文原始设计意图——可能有意不归一化，利用非归一化引入 length bias（较长轨迹整体权重更大）。\n\n**单元测试**：\n\n```python\nimport math\n\ndef phi(t, T, gamma):\n    \"\"\"DMPO 时间折扣函数\"\"\"\n    return gamma**t * (1 - gamma**(T - t)) / (1 - gamma**T)\n\ndef test_phi_normalization():\n    print(\"=== φ(t,T) 归一化验证 ===\")\n    for gamma in [0.85, 0.92, 0.97]:\n        for T in [5, 10, 20, 40]:\n            phi_sum = sum(phi(t, T, gamma) for t in range(T))\n            normalized = \"✓\" if abs(phi_sum - 1.0) < 1e-6 else \"✗\"\n            print(f\"γ={gamma}, T={T:2d}: Σφ={phi_sum:.6f}  {normalized}\")\n    print()\n    print(\"如果 Σφ ≠ 1:\")\n    print(\"  1. 检查 DMPO 论文 Eq.16 是否有意不归一化\")\n    print(\"  2. 若有意：长轨迹获得更大总权重 → implicit length bias\")\n    print(\"  3. 若需归一化：可在 compute_phi_weights 中除以 Σφ\")\n    print(\"  4. 非归一化时可能需要调整 β 以补偿尺度变化\")\n\nif __name__ == \"__main__\":\n    test_phi_normalization()\n```\n\n此测试应在 P1 阶段（`dmpo_loss.py` 单元测试）中执行。若 Σφ 显著偏离 1，需在 §9 风险表中记录应对方案，并决定是否在 `compute_phi_weights` 中添加归一化选项。\n\n### 1.5 φ(t,T) 权重应用到 per-turn loss"
  }
}
````

</details>

---

### Tool result

_source line 14 · 2026-05-12T11:02:15.945397+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T11:02:15.945566+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "old_string": "| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |",
  "new_string": "| φ 权重导致梯度尺度变化 | 需通过 §1.4 归一化验证确认 Σφ 的实际值。若 Σφ ≠ 1 且偏差显著，可在 `compute_phi_weights` 中添加归一化选项，或调整 β 补偿尺度 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "old_string": "| φ 权重导致梯度尺度变化 | φ 归一化保证 Σ_t φ(t,T) 接近 1（实际 = (1-γ^T)/(1-γ^T) · Σ γ^t(1-γ^{T-t}) 需验证），若偏差大需调整 β |",
    "new_string": "| φ 权重导致梯度尺度变化 | 需通过 §1.4 归一化验证确认 Σφ 的实际值。若 Σφ ≠ 1 且偏差显著，可在 `compute_phi_weights` 中添加归一化选项，或调整 β 补偿尺度 |"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T11:02:15.945829+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T11:02:15.945982+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

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
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Bash",
  "tool_args": {
    "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2.md",
    "description": "Copy updated file to unregistered duplicate"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T11:02:15.946112+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T11:02:15.946248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": "113",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "offset": "113",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T11:02:15.946387+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T11:02:15.946533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": "364",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "offset": "364",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T11:02:15.946712+00:00_

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
424	        fo
…[truncated 1092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T11:02:15.946867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": "454",
  "limit": "45"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "offset": "454",
    "limit": "45"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T11:02:15.947009+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-12T11:02:15.947156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": "720",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "offset": "720",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T11:02:15.947297+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-12T11:02:15.947437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": "845",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "offset": "845",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T11:02:15.947575+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T11:02:15.947743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
  "offset": "762",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/_project/report/dmpo_etadn_pipeline_design_v2_c89733.md",
    "offset": "762",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T11:02:15.947884+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-12T11:02:15.948066+00:00_

全部 4 项修改已完成，两个文件均已更新。修改摘要：

1. **§4.2 precompute_ref_log_probs**：添加 φ-weighted 聚合约束说明 + 完整预计算伪代码（传入 turn_ids 和 gamma_e）；§9 风险表标记为已解决
2. **§7.3 实验矩阵**：ETADN 3 seeds + DMPO 3 seeds (γ=0.92) + DPO 1 seed = 7 runs；添加 4 轮调度顺序
3. **§4.5 环境依赖**：新增小节，明确 `trl==1.4.0` 及依赖的关键 API（`_compute_loss`、`selective_log_softmax`、`DPOConfig`）
4. **§1.4 φ(t,T) 归一化验证**：新增小节，包含测试代码框架和 Σφ ≠ 1 时的处理方案

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_pipeline-design-v2-fixes_20260512T105951"
}
```

</details>

---
