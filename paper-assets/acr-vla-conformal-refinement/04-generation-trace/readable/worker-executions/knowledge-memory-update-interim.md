# knowledge memory update interim

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_knowledge_memory-update-interim_20260514T073343.log`
- **Structured JSON:** [`3775e24583cd8a684c9c.json`](../../sessions/37/3775e24583cd8a684c9c.json)

## Before a recorded user message

10 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "f17ed634-23bb-42fc-857f-04c2de13a371",
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
  "uuid": "90752779-faa0-4d97-a3f2-4774bb84618f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778760600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3be03da0-6103-440e-86a2-1726dadcc977",
  "session_id": "f17ed634-23bb-42fc-857f-04c2de13a371"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to update memory.md with specific findings. Let me first read the current content of the file, then append the new section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f17ed634-23bb-42fc-857f-04c2de13a371",
  "uuid": "2e4601db-6f0a-40f1-b014-01ab08472e87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGHkqWvSpbqXYJXC6z9fWy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11635,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11635
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — Read · `toolu_011di4bDd8NYzA6VPPfzf5M9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f17ed634-23bb-42fc-857f-04c2de13a371",
  "uuid": "5877c23f-713d-41f3-bd5a-161ca3e020fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGHkqWvSpbqXYJXC6z9fWy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11635,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11635
      },
      "output_tokens": 24,
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

_source line 6 · 2026-05-14T07:33:55.869Z_

<details><summary>↩ Tool result · `toolu_011di4bDd8NYzA6VPPfzf5M9`</summary>

````text
1	# Memory — acr-vla-conformal-refinement
2	
3	## SmolVLA Wrapper 正确预处理规范（2026-05-13 16:00，7 个 bug 修复后验证通过）
4	
5	### 教训
6	初次 eval 0% 成功率，**7 个 wrapper bug 全部是预处理/后处理不匹配**。必须完全对齐 lerobot 官方推理管线。
7	
8	### 正确预处理（已验证 55.6% success）
9	| 步骤 | 正确做法 | 之前的 bug |
10	|------|----------|-----------|
11	| 图像翻转 | `torch.flip(dims=[2,3])` 翻转 H+W | 无翻转 |
12	| 图像尺寸 | `resize_with_pad(512, 512)` | `Resize(256,256)` |
13	| 图像值域 | `img * 2.0 - 1.0` → [-1,1] | `ToTensor()` → [0,1] |
14	| State 维度 | **8D**: eef_pos(3) + eef_axisangle(3) + gripper_qpos(2) | 6D（缺 gripper） |
15	| State 归一化 | `(s - mean) / (std + ε)` MEAN_STD | 原始值直接传入 |
16	| Action 反归一化 | `a * std + mean` MEAN_STD | 模型原始输出 |
17	| Camera names | env_args 指定 `["agentview", "robot0_eye_in_hand"]` | 只有 agentview |
18	
19	### Normalizer 文件
20	- State: `policy_preprocessor_step_5_normalizer_processor.safetensors` (8D mean/std)
21	- Action: `policy_postprocessor_step_0_unnormalizer_processor.safetensors` (7D mean/std)
22	- 路径: 模型目录下
23	
24	### ⚠️ Precompute 数据需重做
25	之前 3-shard precompute（spatial + object）用的是 buggy wrapper → K-samples 和 obs_features 全部错误。**必须用修复后的 wrapper 重新 precompute 才能训练 CRM。**
26	
27	## evaluate.py rollout_single 正确初始化顺序（2026-05-13 23:35，两轮修复后确认）
28	
29	**正确顺序**：
30	```python
31	env.reset()                           # 1. 清除 terminated flag
32	obs = env.set_init_state(init_state)  # 2. 设目标初始状态（覆盖 reset 的随机状态）
33	for _ in range(5):
34	    obs, _, _, _ = env.step(np.zeros(7))  # 3. 物理稳定
35	```
36	
37	**两个 bug 历史**：
38	1. 原始 bug: `env.reset()` 在 `set_init_state()` **之后**调用 → 覆盖了 demo 初始状态
39	2. 过度修复: 完全删除 `env.reset()` → 前一个 rollout terminated 后 env.step() 抛 ValueError
40	
41	**教训**: env.reset() 必须存在（清 terminated flag），但必须在 set_init_state 之前。两台服务器代码必须同步验证。eval 脚本修改后做 init_state 保持验证。
42	
43	## vla_only 模式 K=1 修复（2026-05-14 00:00）
44	
45	**问题**: evaluate.py 默认 K=10 多采样，即使 vla_only 模式（不需要 uncertainty 统计）也会每步推理 10 次。导致 eval 时长从 2-3h 膨胀到 40-80h。
46	**修复**: main() 中添加 `if args.mode == "vla_only": args.K = 1`，强制单次推理。
47	**教训**: 新增 eval 模式时必须检查 K 采样是否需要，避免不必要的 10x 计算开销。
48	
49	## SmolVLA LIBERO Spatial Baseline（2026-05-14 01:40，eval-spatial-v7-full）
50	
51	- **Overall: 30% (30/100)**，10 tasks × 10 rollouts，K=1，seed=42
52	- 模式清晰："next_to" 类简单任务 90-100%（next_to_ramekin 100%, next_to_cookie_box 90%）
53	- 需要精确空间理解的任务（on/in/from）几乎全部 0%
54	- **ACR-VLA 改进空间主要在后者**——如果 CRM 能帮助这些精确任务，提升空间大
55	
56	## smolvla_libero checkpoint 信息
57	
58	- `lerobot/smolvla_libero`：25K 步全参数微调 on libero_spatial, action_dim=7
59	- 验证结果：spatial 前 3 tasks **55.6% (5/9)** with K=1
60	- smolvla_base (6D, 无 gripper) 只是预训练基座，不能直接用于 LIBERO
61	- 需要同时下载 VLM backbone `SmolVLM2-500M-Video-Instruct` 到本地
62	
63	## 评估崩溃根因（2026-05-13 11:00）
64	
65	- **根因：HuggingFace AutoProcessor.from_pretrained 联网失败**（AutoDL 网络不通）
66	- `tee` 掩盖退出码 → 看似"无声崩溃"
67	- **修复**：HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 + try/except + SIGSEGV handler
68	
69	## MVP 实验关键洞察 (2026-05-13)
70	
71	### Per-DOF vs 标量 uncertainty
72	- Per-DOF (B) 在所有轴上都优于标量 (A)，说明 per-DOF 特征的价值是"信息增益"而非仅"选择性校正"
73	- 即使 1.5:1 低各向异性比率，per-DOF 仍显著优于标量
74	- K=10 估计 vs Oracle 差距 ~15pp，后续需关注复杂场景下估计质量
75	
76	## SmolVLA 架构
77	
78	- smolvla_libero: 450M params, 7D action, chunk_size=50, H_eff=5, flow matching 10 steps
79	- VLM hidden size = 960, CRM input = 1030D (960 + 30 + 40), CRM ~337K params
80	- K=10 with KV cache: 3.2s (vs 7.9s no cache)
81	
82	### 踩坑记录
83	- `attention_mask` 必须是 `bool` 类型
84	- Key 格式 `observation.language.tokens`（点号分隔）
85	- `HF_HUB_OFFLINE=1` 必须在 AutoDL 上
86	- ACI 更新符号：`alpha + gamma*(alpha_target - err)`
87	- LIBERO assets 需从 GitHub 源码安装
88	- BDDL 路径用 `benchmark_instance.get_task_bddl_file_path(task_idx)`
89	- **EXIT_CODE=129 不一定是训练失败**：tmux session 的 SIGHUP trap 可能在训练完成后触发 exit 129。确认训练是否完成应看 log 最后输出，而非仅 exit code（crm-train-v1 教训，50/50 epoch 实际完成）
90	
91	## Precompute 性能基线
92	- 未优化 3.1s → batch 0.82s → 4090x4 0.45s/sample
93	- 增量保存每 500 samples + shard 支持
94	
95	## ReconVLA 竞品分析（2026-05-13 22:29）
96	
97	**ReconVLA (arXiv 2604.16677)** 是最直接竞争者：同样在 flow-matching VLA 上用 CP + K=10 samples。
98	
99	差异化三层：
100	1. **Scalar vs Per-DOF**：ReconVLA 将 7D error 压为 1 个标量 Euclidean；ACR-VLA 保留 40D per-DOF
101	2. **Selection vs Correction**：ReconVLA 只能从 K candidates 选最好的（argmin CQR bound）；ACR-VLA 的 CRM 合成新 action
102	3. **Static vs Online**：ReconVLA 用 offline split conformal；ACR-VLA 用 ACI+COC 在线适应
103	
104	**重要**：ReconVLA 用 CQR 分位数回归做 selection，不是简单 Euclidean argmin。我们当前的 SampleConsensus baseline（raw argmin）低估了 ReconVLA。后续可能需要 ReconVLA Medium baseline（CQR + argmin）。
105	
106	Framing 方向：从 sample selection 到 uncertainty-conditioned correction 的范式跃迁。
107	
108	## 数据增强实际 vs 论文声称（2026-05-13 22:47）
109	
110	代码实际只有 1 种增强（CGS 特征空间高斯噪声），论文声称 3 种（camera viewpoint、sensor noise、robot-state perturbation）。Camera viewpoint 和 robot-state perturbation 均未实现。论文描述需修正。
111	
112	## CRM 训练参数基线
113	
114	- crm-train-v1 (full, baseline): bs=32, lr=1e-3, 50 epochs, val_loss=0.009046, ~337K params
115	- crm-train-a3-obs-only: bs=512, lr=0.016, val_loss=0.018312 (2x worse than full, confirms conformal features critical)
116	- crm-train-a4-scalar-unc: bs=32, lr=1e-3 (running, matched to baseline)
117	- 训练 ~5-15 分钟（纯 MLP on precomputed features）
118	- **Ablation 系列（plan_002/003/006/007/009/010/011）必须用 baseline 超参 bs=32/lr=1e-3**，否则 confound ablation 比较
119	- "bs≥512" 仅限非 ablation 探索性实验
120	
121	## Object Benchmark 评估就绪验证（2026-05-14）
122	
123	### 数据验证 ✅
124	两台服务器 `libero_object/` 均有 10 个 task（hdf5 文件大小一致）：
125	alphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, ketchup, milk, orange_juice, salad_dressing, tomato_sauce
126	
127	### 脚本兼容性 ✅
128	`src/evaluate.py` 支持 `--benchmark object`（choices: object, spatial, goal, long, 90），无需修改。
129	
130	### CRM Cache ✅（仅 bjb1）
131	- bjb1 object cache: 14570 samples（K=10），spatial cache: 12167 samples，合计 26737
132	- bjb2 object cache: **空**（但 eval 不依赖 cache，cache 仅 CRM 训练用）
133	
134	### CRM Checkpoints
135	| Checkpoint | bjb1-18228 路径 | bjb2-40593 |
136	|------------|----------------|------------|
137	| per-DOF (ours) | `/root/autodl-tmp/checkpoints/crm/crm_best.pt` (337K params) | ❌ 仅有 `crm_spatial_only/crm_best.pt`（spatial-only 训练，不适合 object eval） |
138	| scalar_unc | `/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt` (328K params) | ❌ 无 |
139	| obs_only | `/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt` | ❌ 无 |
140	
141	### ⚠️ bjb2 限制
142	bjb2 只能跑不依赖 CRM checkpoint 的方法（vla_only、vla_mean、reconvla）。CRM 方法需在 bjb1 执行或先 scp checkpoints。
143	
144	### 5 套 Object Benchmark 启动命令
145	
146	**GPU 分配方案**：bjb1 跑 4 个方法（4 GPU 并行），bjb2 跑 VLA Mean（1 GPU）。
147	
148	#### 1. ACR-VLA — bjb1 GPU 0
149	```bash
150	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
151	cd /root/acr-vla-conformal-refinement && \
152	MUJOCO_GL=egl TARGET_GPU=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
153	nohup /root/miniconda3/bin/python run_eval_gpu.py \
154	  --benchmark object --mode acr_vla \
155	  --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt \
156	  --n_rollouts 10 \
157	  --output_file /root/autodl-tmp/eval_results/eval-acr-object.json \
158	  > /root/autodl-tmp/eval_results/eval-acr-object.log 2>&1 &
159	```
160	
161	#### 2. Scalar CRM — bjb1 GPU 1
162	```bash
163	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
164	cd /root/acr-vla-conformal-refinement && \
165	MUJOCO_GL=egl TARGET_GPU=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
166	nohup /root/miniconda3/bin/python run_eval_gpu.py \
167	  --benchmark object --mode crm_scalar \
168	  --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt \
169	  --n_rollouts 10 \
170	  --output_file /root/autodl-tmp/eval_results/eval-scalar-unc-object.json \
171	  > /root/autodl-tmp/eval_results/eval-scalar-unc-object.log 2>&1 &
172	```
173	
174	#### 3. ReconVLA (SampleConsensus) — bjb1 GPU 2
175	```bash
176	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
177	cd /root/acr-vla-conformal-refinement && \
178	MUJOCO_GL=egl TARGET_GPU=2 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
179	nohup /root/miniconda3/bin/python run_eval_gpu.py \
180	  --benchmark object --mode reconvla \
181	  --n_rollouts 10 \
182	  --output_file /root/autodl-tmp/eval_results/eval-reconvla-object.json \
183	  > /root/autodl-tmp/eval_results/eval-reconvla-object.log 2>&1 &
184	```
185	
186	#### 4. VLA Only (K=1) — bjb1 GPU 3
187	```bash
188	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
189	cd /root/acr-vla-conformal-refinement && \
190	MUJOCO_GL=egl TARGET_GPU=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
191	nohup /root/miniconda3/bin/python run_eval_gpu.py \
192	  --benchmark object --mode vla_only --baseline_mode single \
193	  --n_rollouts 10 \
194	  --output_file /root/autodl-tmp/eval_results/eval-vla-only-object.json \
195	  > /root/autodl-tmp/eval_results/eval-vla-only-object.log 2>&1 &
196	```
197	
198	#### 5. VLA Mean (K=10) — bjb2 GPU 0
199	```bash
200	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
201	cd /root/acr-vla-conformal-refinement && \
202	MUJOCO_GL=egl TARGET_GPU=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
203	nohup /root/miniconda3/bin/python run_eval_gpu.py \
204	  --benchmark object --mode vla_only --baseline_mode mean \
205	  --n_rollouts 10 \
206	  --output_file /root/autodl-tmp/eval_results/eval-vla-mean-object.json \
207	  > /root/autodl-tmp/eval_results/eval-vla-mean-object.log 2>&1 &
208	```
209	
210	### Object Baseline 预期
211	Spatial baseline = 30%（vla_only）。Object benchmark 整体应更低（task context 说 object baseline = 13%），因为 pick-and-place 需要精确抓取。
212	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f17ed634-23bb-42fc-857f-04c2de13a371",
  "uuid": "df45c3f2-2acd-474c-ab30-be95b464aa31",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
      "content": "# Memory — acr-vla-conformal-refinement\n\n## SmolVLA Wrapper 正确预处理规范（2026-05-13 16:00，7 个 bug 修复后验证通过）\n\n### 教训\n初次 eval 0% 成功率，**7 个 wrapper bug 全部是预处理/后处理不匹配**。必须完全对齐 lerobot 官方推理管线。\n\n### 正确预处理（已验证 55.6% success）\n| 步骤 | 正确做法 | 之前的 bug |\n|------|----------|-----------|\n| 图像翻转 | `torch.flip(dims=[2,3])` 翻转 H+W | 无翻转 |\n| 图像尺寸 | `resize_with_pad(512, 512)` | `Resize(256,256)` |\n| 图像值域 | `img * 2.0 - 1.0` → [-1,1] | `ToTensor()` → [0,1] |\n| State 维度 | **8D**: eef_pos(3) + eef_axisangle(3) + gripper_qpos(2) | 6D（缺 gripper） |\n| State 归一化 | `(s - mean) / (std + ε)` MEAN_STD | 原始值直接传入 |\n| Action 反归一化 | `a * std + mean` MEAN_STD | 模型原始输出 |\n| Camera names | env_args 指定 `[\"agentview\", \"robot0_eye_in_hand\"]` | 只有 agentview |\n\n### Normalizer 文件\n- State: `policy_preprocessor_step_5_normalizer_processor.safetensors` (8D mean/std)\n- Action: `policy_postprocessor_step_0_unnormalizer_processor.safetensors` (7D mean/std)\n- 路径: 模型目录下\n\n### ⚠️ Precompute 数据需重做\n之前 3-shard precompute（spatial + object）用的是 buggy wrapper → K-samples 和 obs_features 全部错误。**必须用修复后的 wrapper 重新 precompute 才能训练 CRM。**\n\n## evaluate.py rollout_single 正确初始化顺序（2026-05-13 23:35，两轮修复后确认）\n\n**正确顺序**：\n```python\nenv.reset()                           # 1. 清除 terminated flag\nobs = env.set_init_state(init_state)  # 2. 设目标初始状态（覆盖 reset 的随机状态）\nfor _ in range(5):\n    obs, _, _, _ = env.step(np.zeros(7))  # 3. 物理稳定\n```\n\n**两个 bug 历史**：\n1. 原始 bug: `env.reset()` 在 `set_init_state()` **之后**调用 → 覆盖了 demo 初始状态\n2. 过度修复: 完全删除 `env.reset()` → 前一个 rollout terminated 后 env.step() 抛 ValueError\n\n**教训**: env.reset() 必须存在（清 terminated flag），但必须在 set_init_state 之前。两台服务器代码必须同步验证。eval 脚本修改后做 init_state 保持验证。\n\n## vla_only 模式 K=1 修复（2026-05-14 00:00）\n\n**问题**: evaluate.py 默认 K=10 多采样，即使 vla_only 模式（不需要 uncertainty 统计）也会每步推理 10 次。导致 eval 时长从 2-3h 膨胀到 40-80h。\n**修复**: main() 中添加 `if args.mode == \"vla_only\": args.K = 1`，强制单次推理。\n**教训**: 新增 eval 模式时必须检查 K 采样是否需要，避免不必要的 10x 计算开销。\n\n## SmolVLA LIBERO Spatial Baseline（2026-05-14 01:40，eval-spatial-v7-full）\n\n- **Overall: 30% (30/100)**，10 tasks × 10 rollouts，K=1，seed=42\n- 模式清晰：\"next_to\" 类简单任务 90-100%（next_to_ramekin 100%, next_to_cookie_box 90%）\n- 需要精确空间理解的任务（on/in/from）几乎全部 0%\n- **ACR-VLA 改进空间主要在后者**——如果 CRM 能帮助这些精确任务，提升空间大\n\n## smolvla_libero checkpoint 信息\n\n- `lerobot/smolvla_libero`：25K 步全参数微调 on libero_spatial, action_dim=7\n- 验证结果：spatial 前 3 tasks **55.6% (5/9)** with K=1\n- smolvla_base (6D, 无 gripper) 只是预训练基座，不能直接用于 LIBERO\n- 需要同时下载 VLM backbone `SmolVLM2-500M-Video-Instruct` 到本地\n\n## 评估崩溃根因（2026-05-13 11:00）\n\n- **根因：HuggingFace AutoProcessor.from_pretrained 联网失败**（AutoDL 网络不通）\n- `tee` 掩盖退出码 → 看似\"无声崩溃\"\n- **修复**：HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 + try/except + SIGSEGV handler\n\n## MVP 实验关键洞察 (2026-05-13)\n\n### Per-DOF vs 标量 uncertainty\n- Per-DOF (B) 在所有轴上都优于标量 (A)，说明 per-DOF 特征的价值是\"信息增益\"而非仅\"选择性校正\"\n- 即使 1.5:1 低各向异性比率，per-DOF 仍显著优于标量\n- K=10 估计 vs Oracle 差距 ~15pp，后续需关注复杂场景下估计质量\n\n## SmolVLA 架构\n\n- smolvla_libero: 450M params, 7D action, chunk_size=50, H_eff=5, flow matching 10 steps\n- VLM hidden size = 960, CRM input = 1030D (960 + 30 + 40), CRM ~337K params\n- K=10 with KV cache: 3.2s (vs 7.9s no cache)\n\n### 踩坑记录\n- `attention_mask` 必须是 `bool` 类型\n- Key 格式 `observation.language.tokens`（点号分隔）\n- `HF_HUB_OFFLINE=1` 必须在 AutoDL 上\n- ACI 更新符号：`alpha + gamma*(alpha_target - err)`\n- LIBERO assets 需从 GitHub 源码安装\n- BDDL 路径用 `benchmark_instance.get_task_bddl_file_path(task_idx)`\n- **EXIT_CODE=129 不一定是训练失败**：tmux session 的 SIGHUP trap 可能在训练完成后触发 exit 129。确认训练是否完成应看 log 最后输出，而非仅 exit code（crm-train-v1 教训，50/50 epoch 实际完成）\n\n## Precompute 性能基线\n- 未优化 3.1s → batch 0.82s → 4090x4 0.45s/sample\n- 增量保存每 500 samples + shard 支持\n\n## ReconVLA 竞品分析（2026-05-13 22:29）\n\n**ReconVLA (arXiv 2604.16677)** 是最直接竞争者：同样在 flow-matching VLA 上用 CP + K=10 samples。\n\n差异化三层：\n1. **Scalar vs Per-DOF**：ReconVLA 将 7D error 压为 1 个标量 Euclidean；ACR-VLA 保留 40D per-DOF\n2. **Selection vs Correction**：ReconVLA 只能从 K candidates 选最好的（argmin CQR bound）；ACR-VLA 的 CRM 合成新 action\n3. **Static vs Online**：ReconVLA 用 offline split conformal；ACR-VLA 用 ACI+COC 在线适应\n\n**重要**：ReconVLA 用 CQR 分位数回归做 selection，不是简单 Euclidean argmin。我们当前的 SampleConsensus baseline（raw argmin）低估了 ReconVLA。后续可能需要 ReconVLA Medium baseline（CQR + argmin）。\n\nFraming 方向：从 sample selection 到 uncertainty-conditioned correction 的范式跃迁。\n\n## 数据增强实际 vs 论文声称（2026-05-13 22:47）\n\n代码实际只有 1 种增强（CGS 特征空间高斯噪声），论文声称 3 种（camera viewpoint、sensor noise、robot-state perturbation）。Camera viewpoint 和 robot-state perturbation 均未实现。论文描述需修正。\n\n## CRM 训练参数基线\n\n- crm-train-v1 (full, baseline): bs=32, lr=1e-3, 50 epochs, val_loss=0.009046, ~337K params\n- crm-train-a3-obs-only: bs=512, lr=0.016, val_loss=0.018312 (2x worse than full, confirms conformal features critical)\n- crm-train-a4-scalar-unc: bs=32, lr=1e-3 (running, matched to baseline)\n- 训练 ~5-15 分钟（纯 MLP on precomputed features）\n- **Ablation 系列（plan_002/003/006/007/009/010/011）必须用 baseline 超参 bs=32/lr=1e-3**，否则 confound ablation 比较\n- \"bs≥512\" 仅限非 ablation 探索性实验\n\n## Object Benchmark 评估就绪验证（2026-05-14）\n\n### 数据验证 ✅\n两台服务器 `libero_object/` 均有 10 个 task（hdf5 文件大小一致）：\nalphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, ketchup, milk, orange_juice, salad_dressing, tomato_sauce\n\n### 脚本兼容性 ✅\n`src/evaluate.py` 支持 `--benchmark object`（choices: object, spatial, goal, long, 90），无需修改。\n\n### CRM Cache ✅（仅 bjb1）\n- bjb1 object cache: 14570 samples（K=10），spatial cache: 12167 samples，合计 26737\n- bjb2 object cache: **空**（但 eval 不依赖 cache，cache 仅 CRM 训练用）\n\n### CRM Checkpoints\n| Checkpoint | bjb1-18228 路径 | bjb2-40593 |\n|------------|----------------|------------|\n| per-DOF (ours) | `/root/autodl-tmp/checkpoints/crm/crm_best.pt` (337K params) | ❌ 仅有 `crm_spatial_only/crm_best.pt`（spatial-only 训练，不适合 object eval） |\n| scalar_unc | `/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt` (328K params) | ❌ 无 |\n| obs_only | `/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt` | ❌ 无 |\n\n### ⚠️ bjb2 限制\nbjb2 只能跑不依赖 CRM checkpoint 的方法（vla_only、vla_mean、reconvla）。CRM 方法需在 bjb1 执行或先 scp checkpoints。\n\n### 5 套 Object Benchmark 启动命令\n\n**GPU 分配方案**：bjb1 跑 4 个方法（4 GPU 并行），bjb2 跑 VLA Mean（1 GPU）。\n\n#### 1. ACR-VLA — bjb1 GPU 0\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode acr_vla \\\n  --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-acr-object.json \\\n  > /root/autodl-tmp/eval_results/eval-acr-object.log 2>&1 &\n```\n\n#### 2. Scalar CRM — bjb1 GPU 1\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode crm_scalar \\\n  --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-scalar-unc-object.json \\\n  > /root/autodl-tmp/eval_results/eval-scalar-unc-object.log 2>&1 &\n```\n\n#### 3. ReconVLA (SampleConsensus) — bjb1 GPU 2\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=2 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode reconvla \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-reconvla-object.json \\\n  > /root/autodl-tmp/eval_results/eval-reconvla-object.log 2>&1 &\n```\n\n#### 4. VLA Only (K=1) — bjb1 GPU 3\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode vla_only --baseline_mode single \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-vla-only-object.json \\\n  > /root/autodl-tmp/eval_results/eval-vla-only-object.log 2>&1 &\n```\n\n#### 5. VLA Mean (K=10) — bjb2 GPU 0\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode vla_only --baseline_mode mean \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-vla-mean-object.json \\\n  > /root/autodl-tmp/eval_results/eval-vla-mean-object.log 2>&1 &\n```\n\n### Object Baseline 预期\nSpatial baseline = 30%（vla_only）。Object benchmark 整体应更低（task context 说 object baseline = 13%），因为 pick-and-place 需要精确抓取。\n",
      "numLines": 212,
      "startLine": 1,
      "totalLines": 212
    }
  }
}
````

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Edit · `toolu_015WxtuDY8A8gjt6djNEHrtk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
  "old_string": "### Object Baseline 预期\nSpatial baseline = 30%（vla_only）。Object benchmark 整体应更低（task context 说 object baseline = 13%），因为 pick-and-place 需要精确抓取。",
  "new_string": "### Object Baseline 预期\nSpatial baseline = 30%（vla_only）。Object benchmark 整体应更低（task context 说 object baseline = 13%），因为 pick-and-place 需要精确抓取。\n\n## ACR-VLA Correction 退化现象（2026-05-14 interim analysis）\n\n### 核心发现：CRM correction 低于 baseline\n- ACR-VLA per-DOF CRM (K=10: ~23%, K=5: ~26%) **低于** vla_only baseline (30%)\n- SampleConsensus (argmin selection, 42.9%) 显著优于 ACR-VLA，说明\"选好样本\"比\"学修正\"更有效\n- Scalar CRM (35%) 略优于 baseline 但远低于 SampleConsensus\n- **中间结果**（6-7/10 spatial tasks 完成），最终可能略有变动\n\n### 推测原因（来自文献调研）\n- CRM 对好样本的过度修正（已正确的 action 被不必要地 shift）\n- 训练分布与 eval 分布 mismatch\n- Correction magnitude 无界，大误差修正反而引入更大偏移\n\n## Task 难度二分性（2026-05-14）\n\n- **简单 tasks** (next_to_ramekin 70-100%, between_plate 40-70%, next_to_cookie_box 90%): ACR-VLA 在这些 task 上低于 baseline，CRM correction 损害了本已正确的 action\n- **困难 tasks** (table_center 0%, top_drawer 0-10%, on_ramekin 0-10%): 所有方法都接近 0%，CRM 也无法救\n- **结论**：CRM correction \"不该修正的地方修正了，该修正的地方修正不了\"\n\n## Eval 时间估算经验（2026-05-14）\n\n| 配置 | 每个 task 耗时 (4090) |\n|------|----------------------|\n| K=10 eval (ACR/reconvla/scalar) | ~1h |\n| K=1 eval (vla_only) | ~12min |\n| K=10 mean baseline | ~1h（需生成 K 个样本） |\n| bjb2 (4090 D) vs bjb1 (4090) | 慢约 20-30% |\n\n## 潜在补救方向（2026-05-14，来自文献调研 art_20260514_d21dd2）\n\n1. **Correction magnitude clipping**（最低成本实验）\n2. **Confidence-gated correction**（仅高 uncertainty 时修正）\n3. **Hybrid**: SampleConsensus top-K → bounded correction\n4. 需要 Director 决策后才能铺实验"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f17ed634-23bb-42fc-857f-04c2de13a371",
  "uuid": "aa6ef760-7e31-4cbb-a39c-37ca29218d94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZVTSqh68weNqXtDjhW4FE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5199,
      "cache_read_input_tokens": 23476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5199
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

_source line 8 · 2026-05-14T07:34:21.957Z_

<details><summary>↩ Tool result · `toolu_015WxtuDY8A8gjt6djNEHrtk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f17ed634-23bb-42fc-857f-04c2de13a371",
  "uuid": "d154b933-e070-4efd-b7d5-3b0c92e55e5c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
    "oldString": "### Object Baseline 预期\nSpatial baseline = 30%（vla_only）。Object benchmark 整体应更低（task context 说 object baseline = 13%），因为 pick-and-place 需要精确抓取。",
    "newString": "### Object Baseline 预期\nSpatial baseline = 30%（vla_only）。Object benchmark 整体应更低（task context 说 object baseline = 13%），因为 pick-and-place 需要精确抓取。\n\n## ACR-VLA Correction 退化现象（2026-05-14 interim analysis）\n\n### 核心发现：CRM correction 低于 baseline\n- ACR-VLA per-DOF CRM (K=10: ~23%, K=5: ~26%) **低于** vla_only baseline (30%)\n- SampleConsensus (argmin selection, 42.9%) 显著优于 ACR-VLA，说明\"选好样本\"比\"学修正\"更有效\n- Scalar CRM (35%) 略优于 baseline 但远低于 SampleConsensus\n- **中间结果**（6-7/10 spatial tasks 完成），最终可能略有变动\n\n### 推测原因（来自文献调研）\n- CRM 对好样本的过度修正（已正确的 action 被不必要地 shift）\n- 训练分布与 eval 分布 mismatch\n- Correction magnitude 无界，大误差修正反而引入更大偏移\n\n## Task 难度二分性（2026-05-14）\n\n- **简单 tasks** (next_to_ramekin 70-100%, between_plate 40-70%, next_to_cookie_box 90%): ACR-VLA 在这些 task 上低于 baseline，CRM correction 损害了本已正确的 action\n- **困难 tasks** (table_center 0%, top_drawer 0-10%, on_ramekin 0-10%): 所有方法都接近 0%，CRM 也无法救\n- **结论**：CRM correction \"不该修正的地方修正了，该修正的地方修正不了\"\n\n## Eval 时间估算经验（2026-05-14）\n\n| 配置 | 每个 task 耗时 (4090) |\n|------|----------------------|\n| K=10 eval (ACR/reconvla/scalar) | ~1h |\n| K=1 eval (vla_only) | ~12min |\n| K=10 mean baseline | ~1h（需生成 K 个样本） |\n| bjb2 (4090 D) vs bjb1 (4090) | 慢约 20-30% |\n\n## 潜在补救方向（2026-05-14，来自文献调研 art_20260514_d21dd2）\n\n1. **Correction magnitude clipping**（最低成本实验）\n2. **Confidence-gated correction**（仅高 uncertainty 时修正）\n3. **Hybrid**: SampleConsensus top-K → bounded correction\n4. 需要 Director 决策后才能铺实验",
    "originalFile": "# Memory — acr-vla-conformal-refinement\n\n## SmolVLA Wrapper 正确预处理规范（2026-05-13 16:00，7 个 bug 修复后验证通过）\n\n### 教训\n初次 eval 0% 成功率，**7 个 wrapper bug 全部是预处理/后处理不匹配**。必须完全对齐 lerobot 官方推理管线。\n\n### 正确预处理（已验证 55.6% success）\n| 步骤 | 正确做法 | 之前的 bug |\n|------|----------|-----------|\n| 图像翻转 | `torch.flip(dims=[2,3])` 翻转 H+W | 无翻转 |\n| 图像尺寸 | `resize_with_pad(512, 512)` | `Resize(256,256)` |\n| 图像值域 | `img * 2.0 - 1.0` → [-1,1] | `ToTensor()` → [0,1] |\n| State 维度 | **8D**: eef_pos(3) + eef_axisangle(3) + gripper_qpos(2) | 6D（缺 gripper） |\n| State 归一化 | `(s - mean) / (std + ε)` MEAN_STD | 原始值直接传入 |\n| Action 反归一化 | `a * std + mean` MEAN_STD | 模型原始输出 |\n| Camera names | env_args 指定 `[\"agentview\", \"robot0_eye_in_hand\"]` | 只有 agentview |\n\n### Normalizer 文件\n- State: `policy_preprocessor_step_5_normalizer_processor.safetensors` (8D mean/std)\n- Action: `policy_postprocessor_step_0_unnormalizer_processor.safetensors` (7D mean/std)\n- 路径: 模型目录下\n\n### ⚠️ Precompute 数据需重做\n之前 3-shard precompute（spatial + object）用的是 buggy wrapper → K-samples 和 obs_features 全部错误。**必须用修复后的 wrapper 重新 precompute 才能训练 CRM。**\n\n## evaluate.py rollout_single 正确初始化顺序（2026-05-13 23:35，两轮修复后确认）\n\n**正确顺序**：\n```python\nenv.reset()                           # 1. 清除 terminated flag\nobs = env.set_init_state(init_state)  # 2. 设目标初始状态（覆盖 reset 的随机状态）\nfor _ in range(5):\n    obs, _, _, _ = env.step(np.zeros(7))  # 3. 物理稳定\n```\n\n**两个 bug 历史**：\n1. 原始 bug: `env.reset()` 在 `set_init_state()` **之后**调用 → 覆盖了 demo 初始状态\n2. 过度修复: 完全删除 `env.reset()` → 前一个 rollout terminated 后 env.step() 抛 ValueError\n\n**教训**: env.reset() 必须存在（清 terminated flag），但必须在 set_init_state 之前。两台服务器代码必须同步验证。eval 脚本修改后做 init_state 保持验证。\n\n## vla_only 模式 K=1 修复（2026-05-14 00:00）\n\n**问题**: evaluate.py 默认 K=10 多采样，即使 vla_only 模式（不需要 uncertainty 统计）也会每步推理 10 次。导致 eval 时长从 2-3h 膨胀到 40-80h。\n**修复**: main() 中添加 `if args.mode == \"vla_only\": args.K = 1`，强制单次推理。\n**教训**: 新增 eval 模式时必须检查 K 采样是否需要，避免不必要的 10x 计算开销。\n\n## SmolVLA LIBERO Spatial Baseline（2026-05-14 01:40，eval-spatial-v7-full）\n\n- **Overall: 30% (30/100)**，10 tasks × 10 rollouts，K=1，seed=42\n- 模式清晰：\"next_to\" 类简单任务 90-100%（next_to_ramekin 100%, next_to_cookie_box 90%）\n- 需要精确空间理解的任务（on/in/from）几乎全部 0%\n- **ACR-VLA 改进空间主要在后者**——如果 CRM 能帮助这些精确任务，提升空间大\n\n## smolvla_libero checkpoint 信息\n\n- `lerobot/smolvla_libero`：25K 步全参数微调 on libero_spatial, action_dim=7\n- 验证结果：spatial 前 3 tasks **55.6% (5/9)** with K=1\n- smolvla_base (6D, 无 gripper) 只是预训练基座，不能直接用于 LIBERO\n- 需要同时下载 VLM backbone `SmolVLM2-500M-Video-Instruct` 到本地\n\n## 评估崩溃根因（2026-05-13 11:00）\n\n- **根因：HuggingFace AutoProcessor.from_pretrained 联网失败**（AutoDL 网络不通）\n- `tee` 掩盖退出码 → 看似\"无声崩溃\"\n- **修复**：HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 + try/except + SIGSEGV handler\n\n## MVP 实验关键洞察 (2026-05-13)\n\n### Per-DOF vs 标量 uncertainty\n- Per-DOF (B) 在所有轴上都优于标量 (A)，说明 per-DOF 特征的价值是\"信息增益\"而非仅\"选择性校正\"\n- 即使 1.5:1 低各向异性比率，per-DOF 仍显著优于标量\n- K=10 估计 vs Oracle 差距 ~15pp，后续需关注复杂场景下估计质量\n\n## SmolVLA 架构\n\n- smolvla_libero: 450M params, 7D action, chunk_size=50, H_eff=5, flow matching 10 steps\n- VLM hidden size = 960, CRM input = 1030D (960 + 30 + 40), CRM ~337K params\n- K=10 with KV cache: 3.2s (vs 7.9s no cache)\n\n### 踩坑记录\n- `attention_mask` 必须是 `bool` 类型\n- Key 格式 `observation.language.tokens`（点号分隔）\n- `HF_HUB_OFFLINE=1` 必须在 AutoDL 上\n- ACI 更新符号：`alpha + gamma*(alpha_target - err)`\n- LIBERO assets 需从 GitHub 源码安装\n- BDDL 路径用 `benchmark_instance.get_task_bddl_file_path(task_idx)`\n- **EXIT_CODE=129 不一定是训练失败**：tmux session 的 SIGHUP trap 可能在训练完成后触发 exit 129。确认训练是否完成应看 log 最后输出，而非仅 exit code（crm-train-v1 教训，50/50 epoch 实际完成）\n\n## Precompute 性能基线\n- 未优化 3.1s → batch 0.82s → 4090x4 0.45s/sample\n- 增量保存每 500 samples + shard 支持\n\n## ReconVLA 竞品分析（2026-05-13 22:29）\n\n**ReconVLA (arXiv 2604.16677)** 是最直接竞争者：同样在 flow-matching VLA 上用 CP + K=10 samples。\n\n差异化三层：\n1. **Scalar vs Per-DOF**：ReconVLA 将 7D error 压为 1 个标量 Euclidean；ACR-VLA 保留 40D per-DOF\n2. **Selection vs Correction**：ReconVLA 只能从 K candidates 选最好的（argmin CQR bound）；ACR-VLA 的 CRM 合成新 action\n3. **Static vs Online**：ReconVLA 用 offline split conformal；ACR-VLA 用 ACI+COC 在线适应\n\n**重要**：ReconVLA 用 CQR 分位数回归做 selection，不是简单 Euclidean argmin。我们当前的 SampleConsensus baseline（raw argmin）低估了 ReconVLA。后续可能需要 ReconVLA Medium baseline（CQR + argmin）。\n\nFraming 方向：从 sample selection 到 uncertainty-conditioned correction 的范式跃迁。\n\n## 数据增强实际 vs 论文声称（2026-05-13 22:47）\n\n代码实际只有 1 种增强（CGS 特征空间高斯噪声），论文声称 3 种（camera viewpoint、sensor noise、robot-state perturbation）。Camera viewpoint 和 robot-state perturbation 均未实现。论文描述需修正。\n\n## CRM 训练参数基线\n\n- crm-train-v1 (full, baseline): bs=32, lr=1e-3, 50 epochs, val_loss=0.009046, ~337K params\n- crm-train-a3-obs-only: bs=512, lr=0.016, val_loss=0.018312 (2x worse than full, confirms conformal features critical)\n- crm-train-a4-scalar-unc: bs=32, lr=1e-3 (running, matched to baseline)\n- 训练 ~5-15 分钟（纯 MLP on precomputed features）\n- **Ablation 系列（plan_002/003/006/007/009/010/011）必须用 baseline 超参 bs=32/lr=1e-3**，否则 confound ablation 比较\n- \"bs≥512\" 仅限非 ablation 探索性实验\n\n## Object Benchmark 评估就绪验证（2026-05-14）\n\n### 数据验证 ✅\n两台服务器 `libero_object/` 均有 10 个 task（hdf5 文件大小一致）：\nalphabet_soup, bbq_sauce, butter, chocolate_pudding, cream_cheese, ketchup, milk, orange_juice, salad_dressing, tomato_sauce\n\n### 脚本兼容性 ✅\n`src/evaluate.py` 支持 `--benchmark object`（choices: object, spatial, goal, long, 90），无需修改。\n\n### CRM Cache ✅（仅 bjb1）\n- bjb1 object cache: 14570 samples（K=10），spatial cache: 12167 samples，合计 26737\n- bjb2 object cache: **空**（但 eval 不依赖 cache，cache 仅 CRM 训练用）\n\n### CRM Checkpoints\n| Checkpoint | bjb1-18228 路径 | bjb2-40593 |\n|------------|----------------|------------|\n| per-DOF (ours) | `/root/autodl-tmp/checkpoints/crm/crm_best.pt` (337K params) | ❌ 仅有 `crm_spatial_only/crm_best.pt`（spatial-only 训练，不适合 object eval） |\n| scalar_unc | `/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt` (328K params) | ❌ 无 |\n| obs_only | `/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt` | ❌ 无 |\n\n### ⚠️ bjb2 限制\nbjb2 只能跑不依赖 CRM checkpoint 的方法（vla_only、vla_mean、reconvla）。CRM 方法需在 bjb1 执行或先 scp checkpoints。\n\n### 5 套 Object Benchmark 启动命令\n\n**GPU 分配方案**：bjb1 跑 4 个方法（4 GPU 并行），bjb2 跑 VLA Mean（1 GPU）。\n\n#### 1. ACR-VLA — bjb1 GPU 0\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode acr_vla \\\n  --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-acr-object.json \\\n  > /root/autodl-tmp/eval_results/eval-acr-object.log 2>&1 &\n```\n\n#### 2. Scalar CRM — bjb1 GPU 1\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode crm_scalar \\\n  --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-scalar-unc-object.json \\\n  > /root/autodl-tmp/eval_results/eval-scalar-unc-object.log 2>&1 &\n```\n\n#### 3. ReconVLA (SampleConsensus) — bjb1 GPU 2\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=2 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode reconvla \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-reconvla-object.json \\\n  > /root/autodl-tmp/eval_results/eval-reconvla-object.log 2>&1 &\n```\n\n#### 4. VLA Only (K=1) — bjb1 GPU 3\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode vla_only --baseline_mode single \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-vla-only-object.json \\\n  > /root/autodl-tmp/eval_results/eval-vla-only-object.log 2>&1 &\n```\n\n#### 5. VLA Mean (K=10) — bjb2 GPU 0\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\ncd /root/acr-vla-conformal-refinement && \\\nMUJOCO_GL=egl TARGET_GPU=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\nnohup /root/miniconda3/bin/python run_eval_gpu.py \\\n  --benchmark object --mode vla_only --baseline_mode mean \\\n  --n_rollouts 10 \\\n  --output_file /root/autodl-tmp/eval_results/eval-vla-mean-object.json \\\n  > /root/autodl-tmp/eval_results/eval-vla-mean-object.log 2>&1 &\n```\n\n### Object Baseline 预期\nSpatial baseline = 30%（vla_only）。Object benchmark 整体应更低（task context 说 object baseline = 13%），因为 pick-and-place 需要精确抓取。\n",
    "structuredPatch": [
      {
        "oldStart": 209,
        "oldLines": 3,
        "newStart": 209,
        "newLines": 38,
        "lines": [
          " ",
          " ### Object Baseline 预期",
          " Spatial baseline = 30%（vla_only）。Object benchmark 整体应更低（task context 说 object baseline = 13%），因为 pick-and-place 需要精确抓取。",
          "+",
          "+## ACR-VLA Correction 退化现象（2026-05-14 interim analysis）",
          "+",
          "+### 核心发现：CRM correction 低于 baseline",
          "+- ACR-VLA per-DOF CRM (K=10: ~23%, K=5: ~26%) **低于** vla_only baseline (30%)",
          "+- SampleConsensus (argmin selection, 42.9%) 显著优于 ACR-VLA，说明\"选好样本\"比\"学修正\"更有效",
          "+- Scalar CRM (35%) 略优于 baseline 但远低于 SampleConsensus",
          "+- **中间结果**（6-7/10 spatial tasks 完成），最终可能略有变动",
          "+",
          "+### 推测原因（来自文献调研）",
          "+- CRM 对好样本的过度修正（已正确的 action 被不必要地 shift）",
          "+- 训练分布与 eval 分布 mismatch",
          "+- Correction magnitude 无界，大误差修正反而引入更大偏移",
          "+",
          "+## Task 难度二分性（2026-05-14）",
          "+",
          "+- **简单 tasks** (next_to_ramekin 70-100%, between_plate 40-70%, next_to_cookie_box 90%): ACR-VLA 在这些 task 上低于 baseline，CRM correction 损害了本已正确的 action",
          "+- **困难 tasks** (table_center 0%, top_drawer 0-10%, on_ramekin 0-10%): 所有方法都接近 0%，CRM 也无法救",
          "+- **结论**：CRM correction \"不该修正的地方修正了，该修正的地方修正不了\"",
          "+",
          "+## Eval 时间估算经验（2026-05-14）",
          "+",
          "+| 配置 | 每个 task 耗时 (4090) |",
          "+|------|----------------------|",
          "+| K=10 eval (ACR/reconvla/scalar) | ~1h |",
          "+| K=1 eval (vla_only) | ~12min |",
          "+| K=10 mean baseline | ~1h（需生成 K 个样本） |",
          "+| bjb2 (4090 D) vs bjb1 (4090) | 慢约 20-30% |",
          "+",
          "+## 潜在补救方向（2026-05-14，来自文献调研 art_20260514_d21dd2）",
          "+",
          "+1. **Correction magnitude clipping**（最低成本实验）",
          "+2. **Confidence-gated correction**（仅高 uncertainty 时修正）",
          "+3. **Hybrid**: SampleConsensus top-K → bounded correction",
          "+4. 需要 Director 决策后才能铺实验"
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

_source line 9_

已追加 4 个 section 到 memory.md：ACR-VLA correction 退化现象、Task 难度二分性、Eval 时间估算、潜在补救方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f17ed634-23bb-42fc-857f-04c2de13a371",
  "uuid": "37e1b281-a97f-40e6-b444-af5d3df2ed36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZhrBxbRKvfVaop8QjmZNW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1016,
      "cache_read_input_tokens": 28675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1016
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

_source line 10_

已追加 4 个 section 到 memory.md：ACR-VLA correction 退化现象、Task 难度二分性、Eval 时间估算、潜在补救方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 32759,
  "duration_api_ms": 33942,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "f17ed634-23bb-42fc-857f-04c2de13a371",
  "total_cost_usd": 0.1734455,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 17850,
    "cache_read_input_tokens": 63992,
    "output_tokens": 1132,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17850,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 55,
        "cache_read_input_tokens": 28675,
        "cache_creation_input_tokens": 1016,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1016
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1467,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001562,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 1132,
      "cacheReadInputTokens": 63992,
      "cacheCreationInputTokens": 17850,
      "webSearchRequests": 0,
      "costUSD": 0.1718835,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "94eb55bc-db2d-492e-bf80-f5c79445d27a"
}
```

</details>

---
