# research correction magnitude analysis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_research_correction-magnitude-analysis_20260515T013100.log`
- **Structured JSON:** [`4856f5e4c3d8a1285d99.json`](../../sessions/48/4856f5e4c3d8a1285d99.json)

## Before a recorded user message

36 recorded events

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
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
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
  "uuid": "eae92615-2aca-4081-9710-3e6933042fcb",
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
    "resetsAt": 1778816400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8830596f-39f6-4caa-8622-8f85c7ca6c1e",
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing project files to understand what's already known, then do literature search, and finally produce the analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "7175078c-ed52-4174-91a4-64172ae8bb33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C49HdEYHnBzQCuKHf3hdQp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11462,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11462
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

### Assistant

_source line 5_

先读取现有项目文件，了解已有知识基础。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "4abcabce-e704-41f3-9006-feb47a49c210",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C49HdEYHnBzQCuKHf3hdQp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11462,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11462
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017LxYCXgw2bzm62iLosyFz9`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__append_idea,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,WebSearch",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "0632b402-5750-47c3-83b7-f9983dba22e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C49HdEYHnBzQCuKHf3hdQp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11462,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11462
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

_source line 7 · 2026-05-15T01:31:15.401Z_

<details><summary>↩ Tool result · `toolu_017LxYCXgw2bzm62iLosyFz9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "fbb30fdd-5e64-4d72-a0d9-29a15bfc7a24",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact",
      "WebSearch"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__append_idea,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,WebSearch",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Gdutz6vsM9tQM9Z1zM4JtY`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "e3308b41-2949-48fa-8dc4-9643153d673a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FkgDVh8pJDF8aWaKFvqYj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 23303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2071
      },
      "output_tokens": 42,
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

_source line 9 · 2026-05-15T01:31:21.211Z_

<details><summary>↩ Tool result · `toolu_01Gdutz6vsM9tQM9Z1zM4JtY`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Memory — acr-vla-conformal-refinement\\n\\n## VLA-mean Baseline 定稿：多采样平均无收益（2026-05-15）\\n\\n### 发现\\neval-vla-mean-spatial: K=10 平均 ≈ 31%（9/10 tasks），与 K=1 baseline 30% 无显著差异（+1pp，噪声范围）。\\n\\n### 含义\\n- **多采样平均不是 ACR-VLA 改善的来源**。flow-matching VLA 的 K 个样本虽然不同，但 averaging 消除的噪声对 task success 无帮助\\n- ACR-VLA 的任何改善必须来自 intelligent selection（argmin）或 CRM correction\\n- argmin-only 早期信号 53.3%（3/10 tasks）>> VLA-mean 31% → **sample selection 本身就有强贡献**\\n- Narrative 可分层：(1) sample selection > averaging (2) CRM correction adds calibrated precision\\n\\n### 论文定位\\n这证实了 Section 1 (Intro) 的动机：naive aggregation 不够，需要 structured uncertainty-guided selection。\\n\\n## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）\\n\\n### 发现\\neval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。\\n\\n### 含义\\n- correction clipping / gating 是正确的补救方向\\n- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）\\n- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval\\n- **不改变目标 venue（ICLR 2027）**，narrative 可从 \\\"per-DOF correction always helps\\\" 调整为 \\\"per-DOF correction with magnitude control\\\"\\n\\n### ⚠️ 注意\\n这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。\\n\\n## Correction Magnitude 文献支撑（2026-05-14 18:37）\\n\\n### 核心竞品/支撑论文\\n1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现\\n2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致\\n3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude\\n4. **DRC (2025)**: temporal decay of correction\\n5. **DAWN (2026)**: scale mismatch → residual 学不好\\n\\n### 独特贡献角度\\n**没有现有方法提供 per-DOF, per-timestep, calibrated magnitude bounds。** ACR-VLA 的 conformal intervals 天然提供 calibrated bounds on expected action range。\\n\\n### 推荐 Framing 调整方向\\n\\\"Conformally-Calibrated Correction Magnitude\\\" — CP intervals 作为 correction 幅度的自然上界，不依赖固定超参数（α, ξ）或 binary gate。\\n\\n### 对比表（可用于论文 Table 1）\\n| Method | Bound Type | Per-DOF | Per-Timestep | Calibrated |\\n|--------|-----------|---------|-------------|------------|\\n| Silver 2018 | Action space | ✗ | ✗ | ✗ |\\n| Johannink 2019 | Fixed tube | ✗ | ✗ | ✗ |\\n| TRANSIC 2024 | Binary gate | ✗ | ✓ | ✗ |\\n| PLD 2026 | Scheduled ξ | ✗ | ~ | ✗ |\\n| **ACR-VLA** | **CP intervals** | **✓** | **✓** | **✓** |\\n\\n## CRM v3-norm 训练结果（2026-05-14 20:06）\\n\\n### 结果\\n- best_val_loss=0.03578 (epoch 47/50)，收敛稳定\\n- normalization stats 嵌入 checkpoint: mean [-26.94, 5.54], std [0.004, 2.22]\\n- 训练数据: crm_cache_v5/spatial, 12167 samples\\n\\n### 与 v2 不可比\\nv2 perdof val_loss=0.009 是在 buggy cache（D016 state dim mismatch）上训练的。v3-norm 是首个 all-bugs-fixed + normalized 的 CRM。训练 loss 数值比较无意义，只有 eval 结果才能判断 normalization 是否真正解决了 correction degradation。\\n\\n### 决策\\n核心悬念：v3-norm eval 是否避免 40%→3% 退化。如果仍退化，问题在 correction magnitude 而非 normalization，需走 \\\"Conformally-Calibrated Correction Magnitude\\\" framing。\\n\\n## CRM Feature Scale 失衡与 Normalization 缺失（2026-05-14 18:00，代码审查确认）\\n\\n### 发现\\nCRM 1030D 输入无 normalization，feature scale 严重失衡：\\n- base_action [0:30]: mean abs ~0.264\\n- uncertainty [30:70]: mean abs ~2.448（log_volume ≈ -25 vs per_dof_std ≈ 0.017，差 1500x）\\n- obs_features [70:1030]: mean abs ~0.467\\n\\n### 影响\\n- CRM 在训练集上只帮助 49% 样本（等于随机），improvement ratio = -0.16\\n- 闭环 eval 中 40% baseline → 3% ACR-VLA（compounding error 雪崩）\\n- 不是 train/eval 不匹配 bug，是模型训练效果差\\n\\n### 修复\\nCRM v3: 在 CRM buffer 中嵌入 per-feature mean/std，forward 时 standardize。eval 加载 checkpoint 自动生效。\\n\\n### 教训\\n**MLP 处理高维异构输入时必须做 input normalization**。1030D 输入中混合了 action space (~0.3)、对数空间 (~-25)、标准差 (~0.02)、VLM hidden states (~0.5)，量级差 3 个数量级。未来类似模型第一步就加 normalization。\\n\\n## SmolVLA Wrapper 正确预处理规范（2026-05-13 16:00，7 个 bug 修复后验证通过）\\n\\n### 教训\\n初次 eval 0% 成功率，**7 个 wrapper bug 全部是预处理/后处理不匹配**。必须完全对齐 lerobot 官方推理管线。\\n\\n### 正确预处理（已验证 55.6% success）\\n| 步骤 | 正确做法 | 之前的 bug |\\n|------|----------|-----------|\\n| 图像翻转 | `torch.flip(dims=[2,3])` 翻转 H+W | 无翻转 |\\n| 图像尺寸 | `resize_with_pad(512, 512)` | `Resize(256,256)` |\\n| 图像值域 | `img * 2.0 - 1.0` → [-1,1] | `ToTensor()` → [0,1] |\\n| State 维度 | **8D**: eef_pos(3) + eef_axisangle(3) + gripper_qpos(2) | 6D（缺 gripper） |\\n| State 归一化 | `(s - mean) / (std + ε)` MEAN_STD | 原始值直接传入 |\\n| Action 反归一化 | `a * std + mean` MEAN_STD | 模型原始输出 |\\n| Camera names | env_args 指定 `[\\\"agentview\\\", \\\"robot0_eye_in_hand\\\"]` | 只有 agentview |\\n\\n### Normalizer 文件\\n- State: `policy_preprocessor_step_5_normalizer_processor.safetensors` (8D mean/std)\\n- Action: `policy_postprocessor_step_0_unnormalizer_processor.safetensors` (7D mean/std)\\n- 路径: 模型目录下\\n\\n### ⚠️ Precompute 数据需重做\\n之前 3-shard precompute（spatial + object）用的是 buggy wrapper → K-samples 和 obs_features 全部错误。**必须用修复后的 wrapper 重新 precompute 才能训练 CRM。**\\n\\n## evaluate.py rollout_single 正确初始化顺序（2026-05-13 23:35，两轮修复后确认）\\n\\n**正确顺序**：\\n```python\\nenv.reset()                           # 1. 清除 terminated flag\\nobs = env.set_init_state(init_state)  # 2. 设目标初始状态（覆盖 reset 的随机状态）\\nfor _ in range(5):\\n    obs, _, _, _ = env.step(np.zeros(7))  # 3. 物理稳定\\n```\\n\\n**两个 bug 历史**：\\n1. 原始 bug: `env.reset()` 在 `set_init_state()` **之后**调用 → 覆盖了 demo 初始状态\\n2. 过度修复: 完全删除 `env.reset()` → 前一个 rollout terminated 后 env.step() 抛 ValueError\\n\\n**教训**: env.reset() 必须存在（清 terminated flag），但必须在 set_init_state 之前。两台服务器代码必须同步验证。eval 脚本修改后做 init_state 保持验证。\\n\\n## vla_only 模式 K=1 修复（2026-05-14 00:00）\\n\\n**问题**: evaluate.py 默认 K=10 多采样，即使 vla_only 模式（不需要 uncertainty 统计）也会每步推理 10 次。导致 eval 时长从 2-3h 膨胀到 40-80h。\\n**修复**: main() 中添加 `if args.mode == \\\"vla_only\\\": args.K = 1`，强制单次推理。\\n**教训**: 新增 eval 模式时必须检查 K 采样是否需要，避免不必要的 10x 计算开销。\\n\\n## SmolVLA LIBERO Spatial Baseline（2026-05-14 01:40，eval-spatial-v7-full）\\n\\n- **Overall: 30% (30/100)**，10 tasks × 10 rollouts，K=1，seed=42\\n- 模式清晰：\\\"next_to\\\" 类简单任务 90-100%（next_to_ramekin 100%, next_to_cookie_box 90%）\\n- 需要精确空间理解的任务（on/in/from）几乎全部 0%\\n- **ACR-VLA 改进空间主要在后者**——如果 CRM 能帮助这些精确任务，提升空间大\\n\\n## smolvla_libero checkpoint 信息\\n\\n- `lerobot/smolvla_libero`：25K 步全参数微调 on libero_spatial, action_dim=7\\n- 验证结果：spatial 前 3 tasks **55.6% (5/9)** with K=1\\n- smolvla_base (6D, 无 gripper) 只是预训练基座，不能直接用于 LIBERO\\n- 需要同时下载 VLM backbone `SmolVLM2-500M-Video-Instruct` 到本地\\n\\n## 评估崩溃根因（2026-05-13 11:00）\\n\\n- **根因：HuggingFace AutoProcessor.from_pretrained 联网失败**（AutoDL 网络不通）\\n- `tee` 掩盖退出码 → 看似\\\"无声崩溃\\\"\\n- **修复**：HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 + try/except + SIGSEGV handler\\n\\n## MVP 实验关键洞察 (2026-05-13)\\n\\n### Per-DOF vs 标量 uncertainty\\n- Per-DOF (B) 在所有轴上都优于标量 (A)，说明 per-DOF 特征的价值是\\\"信息增益\\\"而非仅\\\"选择性校正\\\"\\n- 即使 1.5:1 低各向异性比率，per-DOF 仍显著优于标量\\n- K=10 估计 vs Oracle 差距 ~15pp，后续需关注复杂场景下估计质量\\n\\n## SmolVLA 架构\\n\\n- smolvla_libero: 450M params, 7D action, chunk_size=50, H_eff=5, flow matching 10 steps\\n- VLM hidden size = 960, CRM input = 1030D (960 + 30 + 40), CRM ~337K params\\n- K=10 with KV cache: 3.2s (vs 7.9s no cache)\\n\\n### 踩坑记录\\n- `attention_mask` 必须是 `bool` 类型\\n- Key 格式 `observation.language.tokens`（点号分隔）\\n- `HF_HUB_OFFLINE=1` 必须在 AutoDL 上\\n- ACI 更新符号：`alpha + gamma*(alpha_target - err)`\\n- LIBERO assets 需从 GitHub 源码安装\\n- BDDL 路径用 `benchmark_instance.get_task_bddl_file_path(task_idx)`\\n- **EXIT_CODE=129 不一定是训练失败**：tmux session 的 SIGHUP trap 可能在训练完成后触发 exit 129。确认训练是否完成应看 log 最后输出，而非仅 exit code（crm-train-v1 教训，50/50 epoch 实际完成）\\n\\n## Precompute Pipeline 规范（2026-05-13）\\n\\n- `precompute_crm_cache.py`: 按 task 遍历 demo，每步跑 K 次 VLA 推理\\n- 输出: `{benchmark}_train.pt` / `{benchmark}_val.pt`（list of dicts）\\n- 每条包含: `base_action`, `K_samples`, `expert_action`, `obs_features`, `task_id`, `demo_id`, `step_id`\\n- 按 80/20 split by demo（同一 demo 不跨 train/val）\\n\", \"total_chars\": 7450, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "b488510b-253a-43a3-a596-fae45d1b9d8d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\\\", \\\"content\\\": \\\"# Memory — acr-vla-conformal-refinement\\\\n\\\\n## VLA-mean Baseline 定稿：多采样平均无收益（2026-05-15）\\\\n\\\\n### 发现\\\\neval-vla-mean-spatial: K=10 平均 ≈ 31%（9/10 tasks），与 K=1 baseline 30% 无显著差异（+1pp，噪声范围）。\\\\n\\\\n### 含义\\\\n- **多采样平均不是 ACR-VLA 改善的来源**。flow-matching VLA 的 K 个样本虽然不同，但 averaging 消除的噪声对 task success 无帮助\\\\n- ACR-VLA 的任何改善必须来自 intelligent selection（argmin）或 CRM correction\\\\n- argmin-only 早期信号 53.3%（3/10 tasks）>> VLA-mean 31% → **sample selection 本身就有强贡献**\\\\n- Narrative 可分层：(1) sample selection > averaging (2) CRM correction adds calibrated precision\\\\n\\\\n### 论文定位\\\\n这证实了 Section 1 (Intro) 的动机：naive aggregation 不够，需要 structured uncertainty-guided selection。\\\\n\\\\n## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）\\\\n\\\\n### 发现\\\\neval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。\\\\n\\\\n### 含义\\\\n- correction clipping / gating 是正确的补救方向\\\\n- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）\\\\n- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval\\\\n- **不改变目标 venue（ICLR 2027）**，narrative 可从 \\\\\\\"per-DOF correction always helps\\\\\\\" 调整为 \\\\\\\"per-DOF correction with magnitude control\\\\\\\"\\\\n\\\\n### ⚠️ 注意\\\\n这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。\\\\n\\\\n## Correction Magnitude 文献支撑（2026-05-14 18:37）\\\\n\\\\n### 核心竞品/支撑论文\\\\n1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现\\\\n2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致\\\\n3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude\\\\n4. **DRC (2025)**: temporal decay of correction\\\\n5. **DAWN (2026)**: scale mismatch → residual 学不好\\\\n\\\\n### 独特贡献角度\\\\n**没有现有方法提供 per-DOF, per-timestep, calibrated magnitude bounds。** ACR-VLA 的 conformal intervals 天然提供 calibrated bounds on expected action range。\\\\n\\\\n### 推荐 Framing 调整方向\\\\n\\\\\\\"Conformally-Calibrated Correction Magnitude\\\\\\\" — CP intervals 作为 correction 幅度的自然上界，不依赖固定超参数（α, ξ）或 binary gate。\\\\n\\\\n### 对比表（可用于论文 Table 1）\\\\n| Method | Bound Type | Per-DOF | Per-Timestep | Calibrated |\\\\n|--------|-----------|---------|-------------|------------|\\\\n| Silver 2018 | Action space | ✗ | ✗ | ✗ |\\\\n| Johannink 2019 | Fixed tube | ✗ | ✗ | ✗ |\\\\n| TRANSIC 2024 | Binary gate | ✗ | ✓ | ✗ |\\\\n| PLD 2026 | Scheduled ξ | ✗ | ~ | ✗ |\\\\n| **ACR-VLA** | **CP intervals** | **✓** | **✓** | **✓** |\\\\n\\\\n## CRM v3-norm 训练结果（2026-05-14 20:06）\\\\n\\\\n### 结果\\\\n- best_val_loss=0.03578 (epoch 47/50)，收敛稳定\\\\n- normalization stats 嵌入 checkpoint: mean [-26.94, 5.54], std [0.004, 2.22]\\\\n- 训练数据: crm_cache_v5/spatial, 12167 samples\\\\n\\\\n### 与 v2 不可比\\\\nv2 perdof val_loss=0.009 是在 buggy cache（D016 state dim mismatch）上训练的。v3-norm 是首个 all-bugs-fixed + normalized 的 CRM。训练 loss 数值比较无意义，只有 eval 结果才能判断 normalization 是否真正解决了 correction degradation。\\\\n\\\\n### 决策\\\\n核心悬念：v3-norm eval 是否避免 40%→3% 退化。如果仍退化，问题在 correction magnitude 而非 normalization，需走 \\\\\\\"Conformally-Calibrated Correction Magnitude\\\\\\\" framing。\\\\n\\\\n## CRM Feature Scale 失衡与 Normalization 缺失（2026-05-14 18:00，代码审查确认）\\\\n\\\\n### 发现\\\\nCRM 1030D 输入无 normalization，feature scale 严重失衡：\\\\n- base_action [0:30]: mean abs ~0.264\\\\n- uncertainty [30:70]: mean abs ~2.448（log_volume ≈ -25 vs per_dof_std ≈ 0.017，差 1500x）\\\\n- obs_features [70:1030]: mean abs ~0.467\\\\n\\\\n### 影响\\\\n- CRM 在训练集上只帮助 49% 样本（等于随机），improvement ratio = -0.16\\\\n- 闭环 eval 中 40% baseline → 3% ACR-VLA（compounding error 雪崩）\\\\n- 不是 train/eval 不匹配 bug，是模型训练效果差\\\\n\\\\n### 修复\\\\nCRM v3: 在 CRM buffer 中嵌入 per-feature mean/std，forward 时 standardize。eval 加载 checkpoint 自动生效。\\\\n\\\\n### 教训\\\\n**MLP 处理高维异构输入时必须做 input normalization**。1030D 输入中混合了 action space (~0.3)、对数空间 (~-25)、标准差 (~0.02)、VLM hidden states (~0.5)，量级差 3 个数量级。未来类似模型第一步就加 normalization。\\\\n\\\\n## SmolVLA Wrapper 正确预处理规范（2026-05-13 16:00，7 个 bug 修复后验证通过）\\\\n\\\\n### 教训\\\\n初次 eval 0% 成功率，**7 个 wrapper bug 全部是预处理/后处理不匹配**。必须完全对齐 lerobot 官方推理管线。\\\\n\\\\n### 正确预处理（已验证 55.6% success）\\\\n| 步骤 | 正确做法 | 之前的 bug |\\\\n|------|----------|-----------|\\\\n| 图像翻转 | `torch.flip(dims=[2,3])` 翻转 H+W | 无翻转 |\\\\n| 图像尺寸 | `resize_with_pad(512, 512)` | `Resize(256,256)` |\\\\n| 图像值域 | `img * 2.0 - 1.0` → [-1,1] | `ToTensor()` → [0,1] |\\\\n| State 维度 | **8D**: eef_pos(3) + eef_axisangle(3) + gripper_qpos(2) | 6D（缺 gripper） |\\\\n| State 归一化 | `(s - mean) / (std + ε)` MEAN_STD | 原始值直接传入 |\\\\n| Action 反归一化 | `a * std + mean` MEAN_STD | 模型原始输出 |\\\\n| Camera names | env_args 指定 `[\\\\\\\"agentview\\\\\\\", \\\\\\\"robot0_eye_in_hand\\\\\\\"]` | 只有 agentview |\\\\n\\\\n### Normalizer 文件\\\\n- State: `policy_preprocessor_step_5_normalizer_processor.safetensors` (8D mean/std)\\\\n- Action: `policy_postprocessor_step_0_unnormalizer_processor.safetensors` (7D mean/std)\\\\n- 路径: 模型目录下\\\\n\\\\n### ⚠️ Precompute 数据需重做\\\\n之前 3-shard precompute（spatial + object）用的是 buggy wrapper → K-samples 和 obs_features 全部错误。**必须用修复后的 wrapper 重新 precompute 才能训练 CRM。**\\\\n\\\\n## evaluate.py rollout_single 正确初始化顺序（2026-05-13 23:35，两轮修复后确认）\\\\n\\\\n**正确顺序**：\\\\n```python\\\\nenv.reset()                           # 1. 清除 terminated flag\\\\nobs = env.set_init_state(init_state)  # 2. 设目标初始状态（覆盖 reset 的随机状态）\\\\nfor _ in range(5):\\\\n    obs, _, _, _ = env.step(np.zeros(7))  # 3. 物理稳定\\\\n```\\\\n\\\\n**两个 bug 历史**：\\\\n1. 原始 bug: `env.reset()` 在 `set_init_state()` **之后**调用 → 覆盖了 demo 初始状态\\\\n2. 过度修复: 完全删除 `env.reset()` → 前一个 rollout terminated 后 env.step() 抛 ValueError\\\\n\\\\n**教训**: env.reset() 必须存在（清 terminated flag），但必须在 set_init_state 之前。两台服务器代码必须同步验证。eval 脚本修改后做 init_state 保持验证。\\\\n\\\\n## vla_only 模式 K=1 修复（2026-05-14 00:00）\\\\n\\\\n**问题**: evaluate.py 默认 K=10 多采样，即使 vla_only 模式（不需要 uncertainty 统计）也会每步推理 10 次。导致 eval 时长从 2-3h 膨胀到 40-80h。\\\\n**修复**: main() 中添加 `if args.mode == \\\\\\\"vla_only\\\\\\\": args.K = 1`，强制单次推理。\\\\n**教训**: 新增 eval 模式时必须检查 K 采样是否需要，避免不必要的 10x 计算开销。\\\\n\\\\n## SmolVLA LIBERO Spatial Baseline（2026-05-14 01:40，eval-spatial-v7-full）\\\\n\\\\n- **Overall: 30% (30/100)**，10 tasks × 10 rollouts，K=1，seed=42\\\\n- 模式清晰：\\\\\\\"next_to\\\\\\\" 类简单任务 90-100%（next_to_ramekin 100%, next_to_cookie_box 90%）\\\\n- 需要精确空间理解的任务（on/in/from）几乎全部 0%\\\\n- **ACR-VLA 改进空间主要在后者**——如果 CRM 能帮助这些精确任务，提升空间大\\\\n\\\\n## smolvla_libero checkpoint 信息\\\\n\\\\n- `lerobot/smolvla_libero`：25K 步全参数微调 on libero_spatial, action_dim=7\\\\n- 验证结果：spatial 前 3 tasks **55.6% (5/9)** with K=1\\\\n- smolvla_base (6D, 无 gripper) 只是预训练基座，不能直接用于 LIBERO\\\\n- 需要同时下载 VLM backbone `SmolVLM2-500M-Video-Instruct` 到本地\\\\n\\\\n## 评估崩溃根因（2026-05-13 11:00）\\\\n\\\\n- **根因：HuggingFace AutoProcessor.from_pretrained 联网失败**（AutoDL 网络不通）\\\\n- `tee` 掩盖退出码 → 看似\\\\\\\"无声崩溃\\\\\\\"\\\\n- **修复**：HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 + try/except + SIGSEGV handler\\\\n\\\\n## MVP 实验关键洞察 (2026-05-13)\\\\n\\\\n### Per-DOF vs 标量 uncertainty\\\\n- Per-DOF (B) 在所有轴上都优于标量 (A)，说明 per-DOF 特征的价值是\\\\\\\"信息增益\\\\\\\"而非仅\\\\\\\"选择性校正\\\\\\\"\\\\n- 即使 1.5:1 低各向异性比率，per-DOF 仍显著优于标量\\\\n- K=10 估计 vs Oracle 差距 ~15pp，后续需关注复杂场景下估计质量\\\\n\\\\n## SmolVLA 架构\\\\n\\\\n- smolvla_libero: 450M params, 7D action, chunk_size=50, H_eff=5, flow matching 10 steps\\\\n- VLM hidden size = 960, CRM input = 1030D (960 + 30 + 40), CRM ~337K params\\\\n- K=10 with KV cache: 3.2s (vs 7.9s no cache)\\\\n\\\\n### 踩坑记录\\\\n- `attention_mask` 必须是 `bool` 类型\\\\n- Key 格式 `observation.language.tokens`（点号分隔）\\\\n- `HF_HUB_OFFLINE=1` 必须在 AutoDL 上\\\\n- ACI 更新符号：`alpha + gamma*(alpha_target - err)`\\\\n- LIBERO assets 需从 GitHub 源码安装\\\\n- BDDL 路径用 `benchmark_instance.get_task_bddl_file_path(task_idx)`\\\\n- **EXIT_CODE=129 不一定是训练失败**：tmux session 的 SIGHUP trap 可能在训练完成后触发 exit 129。确认训练是否完成应看 log 最后输出，而非仅 exit code（crm-train-v1 教训，50/50 epoch 实际完成）\\\\n\\\\n## Precompute Pipeline 规范（2026-05-13）\\\\n\\\\n- `precompute_crm_cache.py`: 按 task 遍历 demo，每步跑 K 次 VLA 推理\\\\n- 输出: `{benchmark}_train.pt` / `{benchmark}_val.pt`（list of dicts）\\\\n- 每条包含: `base_action`, `K_samples`, `expert_action`, `obs_features`, `task_id`, `demo_id`, `step_id`\\\\n- 按 80/20 split by demo（同一 demo 不跨 train/val）\\\\n\\\", \\\"total_chars\\\": 7450, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Memory — acr-vla-conformal-refinement\\n\\n## VLA-mean Baseline 定稿：多采样平均无收益（2026-05-15）\\n\\n### 发现\\neval-vla-mean-spatial: K=10 平均 ≈ 31%（9/10 tasks），与 K=1 baseline 30% 无显著差异（+1pp，噪声范围）。\\n\\n### 含义\\n- **多采样平均不是 ACR-VLA 改善的来源**。flow-matching VLA 的 K 个样本虽然不同，但 averaging 消除的噪声对 task success 无帮助\\n- ACR-VLA 的任何改善必须来自 intelligent selection（argmin）或 CRM correction\\n- argmin-only 早期信号 53.3%（3/10 tasks）>> VLA-mean 31% → **sample selection 本身就有强贡献**\\n- Narrative 可分层：(1) sample selection > averaging (2) CRM correction adds calibrated precision\\n\\n### 论文定位\\n这证实了 Section 1 (Intro) 的动机：naive aggregation 不够，需要 structured uncertainty-guided selection。\\n\\n## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）\\n\\n### 发现\\neval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。\\n\\n### 含义\\n- correction clipping / gating 是正确的补救方向\\n- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）\\n- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval\\n- **不改变目标 venue（ICLR 2027）**，narrative 可从 \\\"per-DOF correction always helps\\\" 调整为 \\\"per-DOF correction with magnitude control\\\"\\n\\n### ⚠️ 注意\\n这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。\\n\\n## Correction Magnitude 文献支撑（2026-05-14 18:37）\\n\\n### 核心竞品/支撑论文\\n1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现\\n2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致\\n3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude\\n4. **DRC (2025)**: temporal decay of correction\\n5. **DAWN (2026)**: scale mismatch → residual 学不好\\n\\n### 独特贡献角度\\n**没有现有方法提供 per-DOF, per-timestep, calibrated magnitude bounds。** ACR-VLA 的 conformal intervals 天然提供 calibrated bounds on expected action range。\\n\\n### 推荐 Framing 调整方向\\n\\\"Conformally-Calibrated Correction Magnitude\\\" — CP intervals 作为 correction 幅度的自然上界，不依赖固定超参数（α, ξ）或 binary gate。\\n\\n### 对比表（可用于论文 Table 1）\\n| Method | Bound Type | Per-DOF | Per-Timestep | Calibrated |\\n|--------|-----------|---------|-------------|------------|\\n| Silver 2018 | Action space | ✗ | ✗ | ✗ |\\n| Johannink 2019 | Fixed tube | ✗ | ✗ | ✗ |\\n| TRANSIC 2024 | Binary gate | ✗ | ✓ | ✗ |\\n| PLD 2026 | Scheduled ξ | ✗ | ~ | ✗ |\\n| **ACR-VLA** | **CP intervals** | **✓** | **✓** | **✓** |\\n\\n## CRM v3-norm 训练结果（2026-05-14 20:06）\\n\\n### 结果\\n- best_val_loss=0.03578 (epoch 47/50)，收敛稳定\\n- normalization stats 嵌入 checkpoint: mean [-26.94, 5.54], std [0.004, 2.22]\\n- 训练数据: crm_cache_v5/spatial, 12167 samples\\n\\n### 与 v2 不可比\\nv2 perdof val_loss=0.009 是在 buggy cache（D016 state dim mismatch）上训练的。v3-norm 是首个 all-bugs-fixed + normalized 的 CRM。训练 loss 数值比较无意义，只有 eval 结果才能判断 normalization 是否真正解决了 correction degradation。\\n\\n### 决策\\n核心悬念：v3-norm eval 是否避免 40%→3% 退化。如果仍退化，问题在 correction magnitude 而非 normalization，需走 \\\"Conformally-Calibrated Correction Magnitude\\\" framing。\\n\\n## CRM Feature Scale 失衡与 Normalization 缺失（2026-05-14 18:00，代码审查确认）\\n\\n### 发现\\nCRM 1030D 输入无 normalization，feature scale 严重失衡：\\n- base_action [0:30]: mean abs ~0.264\\n- uncertainty [30:70]: mean abs ~2.448（log_volume ≈ -25 vs per_dof_std ≈ 0.017，差 1500x）\\n- obs_features [70:1030]: mean abs ~0.467\\n\\n### 影响\\n- CRM 在训练集上只帮助 49% 样本（等于随机），improvement ratio = -0.16\\n- 闭环 eval 中 40% baseline → 3% ACR-VLA（compounding error 雪崩）\\n- 不是 train/eval 不匹配 bug，是模型训练效果差\\n\\n### 修复\\nCRM v3: 在 CRM buffer 中嵌入 per-feature mean/std，forward 时 standardize。eval 加载 checkpoint 自动生效。\\n\\n### 教训\\n**MLP 处理高维异构输入时必须做 input normalization**。1030D 输入中混合了 action space (~0.3)、对数空间 (~-25)、标准差 (~0.02)、VLM hidden states (~0.5)，量级差 3 个数量级。未来类似模型第一步就加 normalization。\\n\\n## SmolVLA Wrapper 正确预处理规范（2026-05-13 16:00，7 个 bug 修复后验证通过）\\n\\n### 教训\\n初次 eval 0% 成功率，**7 个 wrapper bug 全部是预处理/后处理不匹配**。必须完全对齐 lerobot 官方推理管线。\\n\\n### 正确预处理（已验证 55.6% success）\\n| 步骤 | 正确做法 | 之前的 bug |\\n|------|----------|-----------|\\n| 图像翻转 | `torch.flip(dims=[2,3])` 翻转 H+W | 无翻转 |\\n| 图像尺寸 | `resize_with_pad(512, 512)` | `Resize(256,256)` |\\n| 图像值域 | `img * 2.0 - 1.0` → [-1,1] | `ToTensor()` → [0,1] |\\n| State 维度 | **8D**: eef_pos(3) + eef_axisangle(3) + gripper_qpos(2) | 6D（缺 gripper） |\\n| State 归一化 | `(s - mean) / (std + ε)` MEAN_STD | 原始值直接传入 |\\n| Action 反归一化 | `a * std + mean` MEAN_STD | 模型原始输出 |\\n| Camera names | env_args 指定 `[\\\"agentview\\\", \\\"robot0_eye_in_hand\\\"]` | 只有 agentview |\\n\\n### Normalizer 文件\\n- State: `policy_preprocessor_step_5_normalizer_processor.safetensors` (8D mean/std)\\n- Action: `policy_postprocessor_step_0_unnormalizer_processor.safetensors` (7D mean/std)\\n- 路径: 模型目录下\\n\\n### ⚠️ Precompute 数据需重做\\n之前 3-shard precompute（spatial + object）用的是 buggy wrapper → K-samples 和 obs_features 全部错误。**必须用修复后的 wrapper 重新 precompute 才能训练 CRM。**\\n\\n## evaluate.py rollout_single 正确初始化顺序（2026-05-13 23:35，两轮修复后确认）\\n\\n**正确顺序**：\\n```python\\nenv.reset()                           # 1. 清除 terminated flag\\nobs = env.set_init_state(init_state)  # 2. 设目标初始状态（覆盖 reset 的随机状态）\\nfor _ in range(5):\\n    obs, _, _, _ = env.step(np.zeros(7))  # 3. 物理稳定\\n```\\n\\n**两个 bug 历史**：\\n1. 原始 bug: `env.reset()` 在 `set_init_state()` **之后**调用 → 覆盖了 demo 初始状态\\n2. 过度修复: 完全删除 `env.reset()` → 前一个 rollout terminated 后 env.step() 抛 ValueError\\n\\n**教训**: env.reset() 必须存在（清 terminated flag），但必须在 set_init_state 之前。两台服务器代码必须同步验证。eval 脚本修改后做 init_state 保持验证。\\n\\n## vla_only 模式 K=1 修复（2026-05-14 00:00）\\n\\n**问题**: evaluate.py 默认 K=10 多采样，即使 vla_only 模式（不需要 uncertainty 统计）也会每步推理 10 次。导致 eval 时长从 2-3h 膨胀到 40-80h。\\n**修复**: main() 中添加 `if args.mode == \\\"vla_only\\\": args.K = 1`，强制单次推理。\\n**教训**: 新增 eval 模式时必须检查 K 采样是否需要，避免不必要的 10x 计算开销。\\n\\n## SmolVLA LIBERO Spatial Baseline（2026-05-14 01:40，eval-spatial-v7-full）\\n\\n- **Overall: 30% (30/100)**，10 tasks × 10 rollouts，K=1，seed=42\\n- 模式清晰：\\\"next_to\\\" 类简单任务 90-100%（next_to_ramekin 100%, next_to_cookie_box 90%）\\n- 需要精确空间理解的任务（on/in/from）几乎全部 0%\\n- **ACR-VLA 改进空间主要在后者**——如果 CRM 能帮助这些精确任务，提升空间大\\n\\n## smolvla_libero checkpoint 信息\\n\\n- `lerobot/smolvla_libero`：25K 步全参数微调 on libero_spatial, action_dim=7\\n- 验证结果：spatial 前 3 tasks **55.6% (5/9)** with K=1\\n- smolvla_base (6D, 无 gripper) 只是预训练基座，不能直接用于 LIBERO\\n- 需要同时下载 VLM backbone `SmolVLM2-500M-Video-Instruct` 到本地\\n\\n## 评估崩溃根因（2026-05-13 11:00）\\n\\n- **根因：HuggingFace AutoProcessor.from_pretrained 联网失败**（AutoDL 网络不通）\\n- `tee` 掩盖退出码 → 看似\\\"无声崩溃\\\"\\n- **修复**：HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 + try/except + SIGSEGV handler\\n\\n## MVP 实验关键洞察 (2026-05-13)\\n\\n### Per-DOF vs 标量 uncertainty\\n- Per-DOF (B) 在所有轴上都优于标量 (A)，说明 per-DOF 特征的价值是\\\"信息增益\\\"而非仅\\\"选择性校正\\\"\\n- 即使 1.5:1 低各向异性比率，per-DOF 仍显著优于标量\\n- K=10 估计 vs Oracle 差距 ~15pp，后续需关注复杂场景下估计质量\\n\\n## SmolVLA 架构\\n\\n- smolvla_libero: 450M params, 7D action, chunk_size=50, H_eff=5, flow matching 10 steps\\n- VLM hidden size = 960, CRM input = 1030D (960 + 30 + 40), CRM ~337K params\\n- K=10 with KV cache: 3.2s (vs 7.9s no cache)\\n\\n### 踩坑记录\\n- `attention_mask` 必须是 `bool` 类型\\n- Key 格式 `observation.language.tokens`（点号分隔）\\n- `HF_HUB_OFFLINE=1` 必须在 AutoDL 上\\n- ACI 更新符号：`alpha + gamma*(alpha_target - err)`\\n- LIBERO assets 需从 GitHub 源码安装\\n- BDDL 路径用 `benchmark_instance.get_task_bddl_file_path(task_idx)`\\n- **EXIT_CODE=129 不一定是训练失败**：tmux session 的 SIGHUP trap 可能在训练完成后触发 exit 129。确认训练是否完成应看 log 最后输出，而非仅 exit code（crm-train-v1 教训，50/50 epoch 实际完成）\\n\\n## Precompute Pipeline 规范（2026-05-13）\\n\\n- `precompute_crm_cache.py`: 按 task 遍历 demo，每步跑 K 次 VLA 推理\\n- 输出: `{benchmark}_train.pt` / `{benchmark}_val.pt`（list of dicts）\\n- 每条包含: `base_action`, `K_samples`, `expert_action`, `obs_features`, `task_id`, `demo_id`, `step_id`\\n- 按 80/20 split by demo（同一 demo 不跨 train/val）\\n\", \"total_chars\": 7450, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
````

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DdezK9UKBs1KaaAeGAKuYH`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "c65ffd4b-81d9-4d7b-8b65-828a408eae29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FkgDVh8pJDF8aWaKFvqYj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 23303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2071
      },
      "output_tokens": 42,
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

_source line 11 · 2026-05-15T01:31:22.259Z_

<details><summary>↩ Tool result · `toolu_01DdezK9UKBs1KaaAeGAKuYH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\\n  # ===== New entries added 2026-05-14 =====\\n\\n  - bibtex_key: \\\"fan2025interpretable_mcp\\\"\\n    title: \\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\"\\n    authors: \\\"Fan & Sesia\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.15383\\\"\\n    url: \\\"https://arxiv.org/abs/2512.15383\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"klein2025otcp\\\"\\n    title: \\\"Multivariate Conformal Prediction using Optimal Transport\\\"\\n    authors: \\\"Klein, Bethune, Ndiaye & Cuturi\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.03609\\\"\\n    url: \\\"https://arxiv.org/abs/2502.03609\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"zollo2025vla_calibration\\\"\\n    title: \\\"Confidence Calibration in Vision-Language-Action Models\\\"\\n    authors: \\\"Zollo & Zemel\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17383\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17383\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\"\\n    must_cite: true\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"tang2026shifting_uncertainty\\\"\\n    title: \\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\"\\n    authors: \\\"Tang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2603.18342\\\"\\n    url: \\\"https://arxiv.org/abs/2603.18342\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lcp2025\\\"\\n    title: \\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.21955\\\"\\n    url: \\\"https://arxiv.org/abs/2509.21955\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"claps2025\\\"\\n    title: \\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.10294\\\"\\n    url: \\\"https://arxiv.org/abs/2512.10294\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lucca2024\\\"\\n    title: \\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\"\\n    authors: \\\"Marques et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2409.08249\\\"\\n    url: \\\"https://arxiv.org/abs/2409.08249\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"sc_vla_2026\\\"\\n    title: \\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.21633\\\"\\n    url: \\\"https://arxiv.org/abs/2602.21633\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"vla_pilot_2025\\\"\\n    title: \\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.14178\\\"\\n    url: \\\"https://arxiv.org/abs/2511.14178\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"acot_vla_2026\\\"\\n    title: \\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\"\\n    authors: \\\"AgibotTech\\\"\\n    year: 2026\\n    venue: \\\"CVPR 2026, arXiv:2601.11404\\\"\\n    url: \\\"https://arxiv.org/abs/2601.11404\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"gonzales2026crc_cbf\\\"\\n    title: \\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\"\\n    authors: \\\"Gonzales et al.\\\"\\n    year: 2026\\n    venue: \\\"IROS 2025, arXiv:2603.10392\\\"\\n    url: \\\"https://arxiv.org/abs/2603.10392\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"safediffcon2025\\\"\\n    title: \\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025, arXiv:2502.02205\\\"\\n    url: \\\"https://arxiv.org/abs/2502.02205\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"afil2026\\\"\\n    title: \\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.08434\\\"\\n    url: \\\"https://arxiv.org/abs/2605.08434\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"valle2025vla_uq_metrics\\\"\\n    title: \\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\"\\n    authors: \\\"Valle et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17049\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17049\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"diffusionvla2024\\\"\\n    title: \\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\"\\n    authors: \\\"Wen et al.\\\"\\n    year: 2024\\n    venue: \\\"ICML 2025, arXiv:2412.03293\\\"\\n    url: \\\"https://arxiv.org/abs/2412.03293\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\\n\\n  - bibtex_key: \\\"silver2018residual\\\"\\n    title: \\\"Residual Policy Learning\\\"\\n    authors: \\\"Silver et al.\\\"\\n    year: 2018\\n    venue: \\\"RSS 2018\\\"\\n    url: \\\"https://arxiv.org/abs/1812.06298\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\\\"\\n    must_cite: true\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"johannink2019residual\\\"\\n    title: \\\"Residual Reinforcement Learning for Robot Manipulator Control\\\"\\n    authors: \\\"Johannink et al.\\\"\\n    year: 2019\\n    venue: \\\"ICRA 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1812.03201\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"jiang2024transic\\\"\\n    title: \\\"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2405.10315\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"ankile2024resip\\\"\\n    title: \\\"ResiP: Residual Reinforcement Learning for Precise Assembly\\\"\\n    authors: \\\"Ankile et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL Workshop 2024\\\"\\n    url: \\\"\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: false\\n    verification_note: \\\"Workshop paper, no arXiv ID provided\\\"\\n    relevance: \\\"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"xiao2026pld\\\"\\n    title: \\\"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\\\"\\n    authors: \\\"Xiao et al.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2511.00091\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"pan2025drc\\\"\\n    title: \\\"DRC: Decaying Relative Correction for Policy Refinement\\\"\\n    authors: \\\"Pan et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2503.15368\\\"\\n    url: \\\"https://arxiv.org/abs/2503.15368\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"ma2026dawn\\\"\\n    title: \\\"DAWN: Value Learning in Residual Reinforcement Learning\\\"\\n    authors: \\\"Ma et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.10539\\\"\\n    url: \\\"https://arxiv.org/abs/2602.10539\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"vla_in_the_loop_2025\\\"\\n    title: \\\"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: false\\n    verification_note: \\\"No arXiv ID provided, needs verification\\\"\\n    relevance: \\\"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"zhou2025acp_cbf\\\"\\n    title: \\\"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\\\"\\n    authors: \\\"Zhou et al.\\\"\\n    year: 2025\\n    venue: \\\"ICRA 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.17678\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"method-component\\\"\\n\", \"total_chars\": 29225, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "206c21eb-98fc-4595-b7d3-d45d519e192f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  - bibtex_key: \\\\\\\"a2c2_2025\\\\\\\"\\\\n    title: \\\\\\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\\\\\"\\\\n    authors: \\\\\\\"Sendai et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.23224\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.23224\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"angelopoulos2023gentle\\\\\\\"\\\\n    title: \\\\\\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\\\\\"\\\\n    authors: \\\\\\\"Angelopoulos & Bates\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Foundations and Trends in Machine Learning\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2107.07511\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"barber2023conformal\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction Beyond Exchangeability\\\\\\\"\\\\n    authors: \\\\\\\"Barber et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Annals of Statistics, 51(2):816-845\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2202.13415\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"black2024pi0\\\\\\\"\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Black et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2410.24164\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.24164\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"braun2025cgs\\\\\\\"\\\\n    title: \\\\\\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\\\\\"\\\\n    authors: \\\\\\\"Braun et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.20941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.20941\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"brohan2023rt2\\\\\\\"\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Brohan et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv:2307.15818\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2307.15818\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chen2026reconvla\\\\\\\"\\\\n    title: \\\\\\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Chen et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.16677\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.16677\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"digflow2025\\\\\\\"\\\\n    title: \\\\\\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.01715\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.01715\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"fei2025liberoplus\\\\\\\"\\\\n    title: \\\\\\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.13626\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.13626\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"ghosh2024octo\\\\\\\"\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Ghosh et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2405.12213\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2405.12213\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gibbs2021aci\\\\\\\"\\\\n    title: \\\\\\\"Adaptive Conformal Inference Under Distribution Shift\\\\\\\"\\\\n    authors: \\\\\\\"Gibbs & Candès\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"NeurIPS 2021\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2106.00170\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"gu2025safe\\\\\\\"\\\\n    title: \\\\\\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Gu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.09937\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"kim2024openvla\\\\\\\"\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2406.09246\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.09246\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"ledoit2004well\\\\\\\"\\\\n    title: \\\\\\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\\\\\"\\\\n    authors: \\\\\\\"Ledoit & Wolf\\\\\\\"\\\\n    year: 2004\\\\n    venue: \\\\\\\"Journal of Multivariate Analysis, 88(2):365-411\\\\\\\"\\\\n    url: \\\\\\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lipman2023flow\\\\\\\"\\\\n    title: \\\\\\\"Flow Matching for Generative Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Lipman et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICLR 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2210.02747\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2023libero\\\\\\\"\\\\n    title: \\\\\\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2306.03310\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2026ttvla\\\\\\\"\\\\n    title: \\\\\\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.06748\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.06748\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"luan2026snapflow\\\\\\\"\\\\n    title: \\\\\\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\\\\\"\\\\n    authors: \\\\\\\"Luan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.05656\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.05656\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"robustvla2025\\\\\\\"\\\\n    title: \\\\\\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.01331\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.01331\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"romano2019cqr\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Quantile Regression\\\\\\\"\\\\n    authors: \\\\\\\"Romano et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"NeurIPS 2019\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1905.03222\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shafer2008tutorial\\\\\\\"\\\\n    title: \\\\\\\"A Tutorial on Conformal Prediction\\\\\\\"\\\\n    authors: \\\\\\\"Shafer & Vovk\\\\\\\"\\\\n    year: 2008\\\\n    venue: \\\\\\\"Journal of Machine Learning Research, 9:371-421\\\\\\\"\\\\n    url: \\\\\\\"https://jmlr.org/papers/v9/shafer08a.html\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shukor2025smolvla\\\\\\\"\\\\n    title: \\\\\\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\\\\\"\\\\n    authors: \\\\\\\"Shukor et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2506.01844\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.01844\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"srpo2025\\\\\\\"\\\\n    title: \\\\\\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.15605\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.15605\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"wang2025cploop\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Wang & Ning\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.16376\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.16376\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"xing2026diu\\\\\\\"\\\\n    title: \\\\\\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\\\\\"\\\\n    authors: \\\\\\\"Xing et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.00941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.00941\\\\\\\"\\\\n    category: \\\\\\\"uq_flow_matching\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"yuan2026ups\\\\\\\"\\\\n    title: \\\\\\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\\\\\"\\\\n    authors: \\\\\\\"Yuan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.22474\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.22474\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"zhao2024conformalized\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\\\\\"\\\\n    authors: \\\\\\\"Zhao et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"RSS 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.07767\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"cosmos_policy_2026\\\\\\\"\\\\n    title: \\\\\\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.16163\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.16163\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_gse_2026\\\\\\\"\\\\n    title: \\\\\\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\\\\\"\\\\n    authors: \\\\\\\"Jiang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.06175\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.06175\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lakshminarayanan2017ensembles\\\\\\\"\\\\n    title: \\\\\\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\\\\\"\\\\n    authors: \\\\\\\"Lakshminarayanan et al.\\\\\\\"\\\\n    year: 2017\\\\n    venue: \\\\\\\"NeurIPS 2017\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1612.01474\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gal2016dropout\\\\\\\"\\\\n    title: \\\\\\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\\\\\"\\\\n    authors: \\\\\\\"Gal & Ghahramani\\\\\\\"\\\\n    year: 2016\\\\n    venue: \\\\\\\"ICML 2016\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1506.02142\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chi2023diffusion_policy\\\\\\\"\\\\n    title: \\\\\\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Chi et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"RSS 2023 / IJRR 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2303.04137\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"Well-known paper, needs URL reachability confirmation\\\\\\\"\\\\n    relevance: \\\\\\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  # ===== New entries added 2026-05-14 =====\\\\n\\\\n  - bibtex_key: \\\\\\\"fan2025interpretable_mcp\\\\\\\"\\\\n    title: \\\\\\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\\\\\"\\\\n    authors: \\\\\\\"Fan & Sesia\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.15383\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.15383\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"klein2025otcp\\\\\\\"\\\\n    title: \\\\\\\"Multivariate Conformal Prediction using Optimal Transport\\\\\\\"\\\\n    authors: \\\\\\\"Klein, Bethune, Ndiaye & Cuturi\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2502.03609\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.03609\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"zollo2025vla_calibration\\\\\\\"\\\\n    title: \\\\\\\"Confidence Calibration in Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Zollo & Zemel\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.17383\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.17383\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"tang2026shifting_uncertainty\\\\\\\"\\\\n    title: \\\\\\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\\\\\"\\\\n    authors: \\\\\\\"Tang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2603.18342\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.18342\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"lcp2025\\\\\\\"\\\\n    title: \\\\\\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.21955\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.21955\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"claps2025\\\\\\\"\\\\n    title: \\\\\\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.10294\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.10294\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"lucca2024\\\\\\\"\\\\n    title: \\\\\\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\\\\\"\\\\n    authors: \\\\\\\"Marques et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2409.08249\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2409.08249\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"sc_vla_2026\\\\\\\"\\\\n    title: \\\\\\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.21633\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.21633\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_pilot_2025\\\\\\\"\\\\n    title: \\\\\\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.14178\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.14178\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"acot_vla_2026\\\\\\\"\\\\n    title: \\\\\\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"AgibotTech\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"CVPR 2026, arXiv:2601.11404\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.11404\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"gonzales2026crc_cbf\\\\\\\"\\\\n    title: \\\\\\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\\\\\"\\\\n    authors: \\\\\\\"Gonzales et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"IROS 2025, arXiv:2603.10392\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.10392\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"safediffcon2025\\\\\\\"\\\\n    title: \\\\\\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025, arXiv:2502.02205\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.02205\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"afil2026\\\\\\\"\\\\n    title: \\\\\\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.08434\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.08434\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"valle2025vla_uq_metrics\\\\\\\"\\\\n    title: \\\\\\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\\\\\"\\\\n    authors: \\\\\\\"Valle et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.17049\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.17049\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"diffusionvla2024\\\\\\\"\\\\n    title: \\\\\\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Wen et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICML 2025, arXiv:2412.03293\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2412.03293\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\\\\n\\\\n  - bibtex_key: \\\\\\\"silver2018residual\\\\\\\"\\\\n    title: \\\\\\\"Residual Policy Learning\\\\\\\"\\\\n    authors: \\\\\\\"Silver et al.\\\\\\\"\\\\n    year: 2018\\\\n    venue: \\\\\\\"RSS 2018\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1812.06298\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"johannink2019residual\\\\\\\"\\\\n    title: \\\\\\\"Residual Reinforcement Learning for Robot Manipulator Control\\\\\\\"\\\\n    authors: \\\\\\\"Johannink et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"ICRA 2019\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1812.03201\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"jiang2024transic\\\\\\\"\\\\n    title: \\\\\\\"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\\\\\\\"\\\\n    authors: \\\\\\\"Jiang et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"CoRL 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2405.10315\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"direct-competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"ankile2024resip\\\\\\\"\\\\n    title: \\\\\\\"ResiP: Residual Reinforcement Learning for Precise Assembly\\\\\\\"\\\\n    authors: \\\\\\\"Ankile et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"CoRL Workshop 2024\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"Workshop paper, no arXiv ID provided\\\\\\\"\\\\n    relevance: \\\\\\\"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"xiao2026pld\\\\\\\"\\\\n    title: \\\\\\\"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Xiao et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.00091\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"direct-competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"pan2025drc\\\\\\\"\\\\n    title: \\\\\\\"DRC: Decaying Relative Correction for Policy Refinement\\\\\\\"\\\\n    authors: \\\\\\\"Pan et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2503.15368\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.15368\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"ma2026dawn\\\\\\\"\\\\n    title: \\\\\\\"DAWN: Value Learning in Residual Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Ma et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.10539\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.10539\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_in_the_loop_2025\\\\\\\"\\\\n    title: \\\\\\\"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2025\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"No arXiv ID provided, needs verification\\\\\\\"\\\\n    relevance: \\\\\\\"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"zhou2025acp_cbf\\\\\\\"\\\\n    title: \\\\\\\"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Zhou et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICRA 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.17678\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 29225, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\\n  # ===== New entries added 2026-05-14 =====\\n\\n  - bibtex_key: \\\"fan2025interpretable_mcp\\\"\\n    title: \\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\"\\n    authors: \\\"Fan & Sesia\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.15383\\\"\\n    url: \\\"https://arxiv.org/abs/2512.15383\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"klein2025otcp\\\"\\n    title: \\\"Multivariate Conformal Prediction using Optimal Transport\\\"\\n    authors: \\\"Klein, Bethune, Ndiaye & Cuturi\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.03609\\\"\\n    url: \\\"https://arxiv.org/abs/2502.03609\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"zollo2025vla_calibration\\\"\\n    title: \\\"Confidence Calibration in Vision-Language-Action Models\\\"\\n    authors: \\\"Zollo & Zemel\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17383\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17383\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\"\\n    must_cite: true\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"tang2026shifting_uncertainty\\\"\\n    title: \\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\"\\n    authors: \\\"Tang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2603.18342\\\"\\n    url: \\\"https://arxiv.org/abs/2603.18342\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lcp2025\\\"\\n    title: \\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.21955\\\"\\n    url: \\\"https://arxiv.org/abs/2509.21955\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"claps2025\\\"\\n    title: \\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.10294\\\"\\n    url: \\\"https://arxiv.org/abs/2512.10294\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lucca2024\\\"\\n    title: \\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\"\\n    authors: \\\"Marques et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2409.08249\\\"\\n    url: \\\"https://arxiv.org/abs/2409.08249\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"sc_vla_2026\\\"\\n    title: \\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.21633\\\"\\n    url: \\\"https://arxiv.org/abs/2602.21633\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"vla_pilot_2025\\\"\\n    title: \\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.14178\\\"\\n    url: \\\"https://arxiv.org/abs/2511.14178\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"acot_vla_2026\\\"\\n    title: \\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\"\\n    authors: \\\"AgibotTech\\\"\\n    year: 2026\\n    venue: \\\"CVPR 2026, arXiv:2601.11404\\\"\\n    url: \\\"https://arxiv.org/abs/2601.11404\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"gonzales2026crc_cbf\\\"\\n    title: \\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\"\\n    authors: \\\"Gonzales et al.\\\"\\n    year: 2026\\n    venue: \\\"IROS 2025, arXiv:2603.10392\\\"\\n    url: \\\"https://arxiv.org/abs/2603.10392\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"safediffcon2025\\\"\\n    title: \\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025, arXiv:2502.02205\\\"\\n    url: \\\"https://arxiv.org/abs/2502.02205\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"afil2026\\\"\\n    title: \\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.08434\\\"\\n    url: \\\"https://arxiv.org/abs/2605.08434\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"valle2025vla_uq_metrics\\\"\\n    title: \\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\"\\n    authors: \\\"Valle et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17049\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17049\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"diffusionvla2024\\\"\\n    title: \\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\"\\n    authors: \\\"Wen et al.\\\"\\n    year: 2024\\n    venue: \\\"ICML 2025, arXiv:2412.03293\\\"\\n    url: \\\"https://arxiv.org/abs/2412.03293\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\\n\\n  - bibtex_key: \\\"silver2018residual\\\"\\n    title: \\\"Residual Policy Learning\\\"\\n    authors: \\\"Silver et al.\\\"\\n    year: 2018\\n    venue: \\\"RSS 2018\\\"\\n    url: \\\"https://arxiv.org/abs/1812.06298\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\\\"\\n    must_cite: true\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"johannink2019residual\\\"\\n    title: \\\"Residual Reinforcement Learning for Robot Manipulator Control\\\"\\n    authors: \\\"Johannink et al.\\\"\\n    year: 2019\\n    venue: \\\"ICRA 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1812.03201\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"jiang2024transic\\\"\\n    title: \\\"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2405.10315\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"ankile2024resip\\\"\\n    title: \\\"ResiP: Residual Reinforcement Learning for Precise Assembly\\\"\\n    authors: \\\"Ankile et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL Workshop 2024\\\"\\n    url: \\\"\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: false\\n    verification_note: \\\"Workshop paper, no arXiv ID provided\\\"\\n    relevance: \\\"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"xiao2026pld\\\"\\n    title: \\\"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\\\"\\n    authors: \\\"Xiao et al.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2511.00091\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"pan2025drc\\\"\\n    title: \\\"DRC: Decaying Relative Correction for Policy Refinement\\\"\\n    authors: \\\"Pan et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2503.15368\\\"\\n    url: \\\"https://arxiv.org/abs/2503.15368\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"ma2026dawn\\\"\\n    title: \\\"DAWN: Value Learning in Residual Reinforcement Learning\\\"\\n    authors: \\\"Ma et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.10539\\\"\\n    url: \\\"https://arxiv.org/abs/2602.10539\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"vla_in_the_loop_2025\\\"\\n    title: \\\"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: false\\n    verification_note: \\\"No arXiv ID provided, needs verification\\\"\\n    relevance: \\\"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"zhou2025acp_cbf\\\"\\n    title: \\\"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\\\"\\n    authors: \\\"Zhou et al.\\\"\\n    year: 2025\\n    venue: \\\"ICRA 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.17678\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"method-component\\\"\\n\", \"total_chars\": 29225, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Rj1zpsdwcvqqgLcmXr4iGH`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "491572d2-0928-4e96-a47e-a9b152281ae1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FkgDVh8pJDF8aWaKFvqYj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 23303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2071
      },
      "output_tokens": 42,
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

_source line 13 · 2026-05-15T01:31:22.614Z_

<details><summary>↩ Tool result · `toolu_01Rj1zpsdwcvqqgLcmXr4iGH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 01:30 UTC | 更新原因: Loop #6 session-start, D021 CoRL 2026 目标恢复, 5路eval进行中\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, D021 撤销 D011）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 2b — CRM Correction Magnitude Sweep + Ablation（D018-D020 诊断闭环后）\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\n- **SFT Gate**: 30% baseline，决定继续（D015）\\n- **CRM v3-norm 训练完成**: perdof val_loss=0.0358, scalar_unc=0.0374, obs_only=0.0165（obs_only 最优）\\n- **Baselines 锁定**: spatial 30% (K=1), VLA-mean 31% (K=10, ≈K=1), object 13% (K=1)\\n- **CRM 失败根因确认（D018）**: 输入 normalization 缺失（1500x scale 差异）+ correction magnitude 过大\\n- **关键发现**: argmin-only（纯样本选择、无 CRM correction）40% @ 5 tasks >> baseline 30%\\n- **最强信号**: tiny-correction（max_norm=0.05）53.3% @ 3 tasks（但样本量不足，不能下结论）\\n- **核心悬念**: CRM correction 是否有正向贡献，还是所有收益来自 argmin 样本选择\\n\\n## 近期任务\\n- [ ] eval-argmin-only-spatial 完成 → 10 task 结果，确认 argmin-only 真实水平\\n- [ ] eval-tiny-correction-spatial 完成 → 与 argmin-only 逐 task 对比，判断 CRM correction 贡献\\n- [ ] eval-acr-spatial-v4-small 完成 → max_norm=0.1 vs 0.05 最佳点\\n- [ ] eval-acr-spatial-v4-obs-only-r2 完成 → obs_only vs perdof, Claim 1 裁决\\n- [ ] eval-vla-mean-spatial-t10 完成 → VLA-mean T10 补全\\n- [ ] eval-acr-spatial-v4-scalar → GPU 空出后启动（三路 ablation 的 scalar_unc 部分）\\n- [ ] 上述全完成 → 组装 spatial 完整对比表 → 向 Director 汇报 + framing 建议\\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\\n\\n## SFT Gate\\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\\n\\n## GPU 预算\\n- bjb1-18228 (4× RTX 4090): eval-acr-spatial-v4-obs-only-r2(cuda:0) + eval-argmin-only-spatial(cuda:1) + eval-tiny-correction-spatial(cuda:2) + eval-acr-spatial-v4-small(cuda:3)\\n- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial-t10(cuda:0)\\n- 总预算 ~200 GPU·h, 已用 ~100h, 剩余 ~100h\\n\\n## 关键路径\\n**当前**: 5 路 eval 全部在跑 → 完整对比表 → framing 决策 → 论文写作（CoRL DDL ~May 26）\\n**核心悬念**: CRM correction 本身有贡献 vs 全靠 argmin 样本选择\\n**风险**: 11 天内需要完成 eval + 分析 + 写论文，时间极紧\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D021 | 2026-05-15 | D021: 撤销 D011，重新瞄准 CoRL 2026（abstract DDL ~May 26） | — |\\n| D020 | 2026-05-14 | D020: obs_only val_loss (0.0165) 54% better than p | crm-train-v3-norm-obs-only, crm-train-v3-norm-scalar-unc, crm-train-v3-norm, eval-acr-spatial-v4-default |\\n| D019 | 2026-05-14 | D019: Normalization alone insufficient — magnitude | eval-acr-spatial-v4-default, eval-acr-spatial-v4-small, eval-argmin-only-spatial, eval-tiny-correction-spatial, eval-vla-mean-spatial |\\n| D018 | 2026-05-14 | D018: CRM 失败根因确认为输入未归一化（1500x scale 差异），批准 normali | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3 |\\n| D017 | 2026-05-14 | D017: CRM correction 全面拖累 baseline — kill 两路 ablat | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3, eval-vla-mean-spatial |\\n| D016 | 2026-05-14 | D016: CRM 训练/评估 state 维度不匹配 bug 确认，批准四项修复 + 重跑 pip | eval-acr-spatial-v2, eval-k5-spatial, eval-scalar-unc-spatial |\\n| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |\\n| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |\\n| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |\\n| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |\\n\\n\", \"total_chars\": 3518, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "8dbef9fb-67a4-4103-985f-aed211ece20b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\\\", \\\"content\\\": \\\"# acr-vla-conformal-refinement — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-15 01:30 UTC | 更新原因: Loop #6 session-start, D021 CoRL 2026 目标恢复, 5路eval进行中\\\\n\\\\n## 核心方向\\\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\\\n\\\\n## 投稿目标\\\\n**CoRL 2026**（abstract DDL ~May 26, D021 撤销 D011）。剩余 ~11 天。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Phase 2b — CRM Correction Magnitude Sweep + Ablation（D018-D020 诊断闭环后）\\\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\\\n- **SFT Gate**: 30% baseline，决定继续（D015）\\\\n- **CRM v3-norm 训练完成**: perdof val_loss=0.0358, scalar_unc=0.0374, obs_only=0.0165（obs_only 最优）\\\\n- **Baselines 锁定**: spatial 30% (K=1), VLA-mean 31% (K=10, ≈K=1), object 13% (K=1)\\\\n- **CRM 失败根因确认（D018）**: 输入 normalization 缺失（1500x scale 差异）+ correction magnitude 过大\\\\n- **关键发现**: argmin-only（纯样本选择、无 CRM correction）40% @ 5 tasks >> baseline 30%\\\\n- **最强信号**: tiny-correction（max_norm=0.05）53.3% @ 3 tasks（但样本量不足，不能下结论）\\\\n- **核心悬念**: CRM correction 是否有正向贡献，还是所有收益来自 argmin 样本选择\\\\n\\\\n## 近期任务\\\\n- [ ] eval-argmin-only-spatial 完成 → 10 task 结果，确认 argmin-only 真实水平\\\\n- [ ] eval-tiny-correction-spatial 完成 → 与 argmin-only 逐 task 对比，判断 CRM correction 贡献\\\\n- [ ] eval-acr-spatial-v4-small 完成 → max_norm=0.1 vs 0.05 最佳点\\\\n- [ ] eval-acr-spatial-v4-obs-only-r2 完成 → obs_only vs perdof, Claim 1 裁决\\\\n- [ ] eval-vla-mean-spatial-t10 完成 → VLA-mean T10 补全\\\\n- [ ] eval-acr-spatial-v4-scalar → GPU 空出后启动（三路 ablation 的 scalar_unc 部分）\\\\n- [ ] 上述全完成 → 组装 spatial 完整对比表 → 向 Director 汇报 + framing 建议\\\\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\\\\n\\\\n## SFT Gate\\\\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\\\\n\\\\n## GPU 预算\\\\n- bjb1-18228 (4× RTX 4090): eval-acr-spatial-v4-obs-only-r2(cuda:0) + eval-argmin-only-spatial(cuda:1) + eval-tiny-correction-spatial(cuda:2) + eval-acr-spatial-v4-small(cuda:3)\\\\n- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial-t10(cuda:0)\\\\n- 总预算 ~200 GPU·h, 已用 ~100h, 剩余 ~100h\\\\n\\\\n## 关键路径\\\\n**当前**: 5 路 eval 全部在跑 → 完整对比表 → framing 决策 → 论文写作（CoRL DDL ~May 26）\\\\n**核心悬念**: CRM correction 本身有贡献 vs 全靠 argmin 样本选择\\\\n**风险**: 11 天内需要完成 eval + 分析 + 写论文，时间极紧\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D021 | 2026-05-15 | D021: 撤销 D011，重新瞄准 CoRL 2026（abstract DDL ~May 26） | — |\\\\n| D020 | 2026-05-14 | D020: obs_only val_loss (0.0165) 54% better than p | crm-train-v3-norm-obs-only, crm-train-v3-norm-scalar-unc, crm-train-v3-norm, eval-acr-spatial-v4-default |\\\\n| D019 | 2026-05-14 | D019: Normalization alone insufficient — magnitude | eval-acr-spatial-v4-default, eval-acr-spatial-v4-small, eval-argmin-only-spatial, eval-tiny-correction-spatial, eval-vla-mean-spatial |\\\\n| D018 | 2026-05-14 | D018: CRM 失败根因确认为输入未归一化（1500x scale 差异），批准 normali | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3 |\\\\n| D017 | 2026-05-14 | D017: CRM correction 全面拖累 baseline — kill 两路 ablat | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3, eval-vla-mean-spatial |\\\\n| D016 | 2026-05-14 | D016: CRM 训练/评估 state 维度不匹配 bug 确认，批准四项修复 + 重跑 pip | eval-acr-spatial-v2, eval-k5-spatial, eval-scalar-unc-spatial |\\\\n| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |\\\\n| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |\\\\n| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |\\\\n| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |\\\\n\\\\n\\\", \\\"total_chars\\\": 3518, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 01:30 UTC | 更新原因: Loop #6 session-start, D021 CoRL 2026 目标恢复, 5路eval进行中\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, D021 撤销 D011）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 2b — CRM Correction Magnitude Sweep + Ablation（D018-D020 诊断闭环后）\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\n- **SFT Gate**: 30% baseline，决定继续（D015）\\n- **CRM v3-norm 训练完成**: perdof val_loss=0.0358, scalar_unc=0.0374, obs_only=0.0165（obs_only 最优）\\n- **Baselines 锁定**: spatial 30% (K=1), VLA-mean 31% (K=10, ≈K=1), object 13% (K=1)\\n- **CRM 失败根因确认（D018）**: 输入 normalization 缺失（1500x scale 差异）+ correction magnitude 过大\\n- **关键发现**: argmin-only（纯样本选择、无 CRM correction）40% @ 5 tasks >> baseline 30%\\n- **最强信号**: tiny-correction（max_norm=0.05）53.3% @ 3 tasks（但样本量不足，不能下结论）\\n- **核心悬念**: CRM correction 是否有正向贡献，还是所有收益来自 argmin 样本选择\\n\\n## 近期任务\\n- [ ] eval-argmin-only-spatial 完成 → 10 task 结果，确认 argmin-only 真实水平\\n- [ ] eval-tiny-correction-spatial 完成 → 与 argmin-only 逐 task 对比，判断 CRM correction 贡献\\n- [ ] eval-acr-spatial-v4-small 完成 → max_norm=0.1 vs 0.05 最佳点\\n- [ ] eval-acr-spatial-v4-obs-only-r2 完成 → obs_only vs perdof, Claim 1 裁决\\n- [ ] eval-vla-mean-spatial-t10 完成 → VLA-mean T10 补全\\n- [ ] eval-acr-spatial-v4-scalar → GPU 空出后启动（三路 ablation 的 scalar_unc 部分）\\n- [ ] 上述全完成 → 组装 spatial 完整对比表 → 向 Director 汇报 + framing 建议\\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\\n\\n## SFT Gate\\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\\n\\n## GPU 预算\\n- bjb1-18228 (4× RTX 4090): eval-acr-spatial-v4-obs-only-r2(cuda:0) + eval-argmin-only-spatial(cuda:1) + eval-tiny-correction-spatial(cuda:2) + eval-acr-spatial-v4-small(cuda:3)\\n- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial-t10(cuda:0)\\n- 总预算 ~200 GPU·h, 已用 ~100h, 剩余 ~100h\\n\\n## 关键路径\\n**当前**: 5 路 eval 全部在跑 → 完整对比表 → framing 决策 → 论文写作（CoRL DDL ~May 26）\\n**核心悬念**: CRM correction 本身有贡献 vs 全靠 argmin 样本选择\\n**风险**: 11 天内需要完成 eval + 分析 + 写论文，时间极紧\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D021 | 2026-05-15 | D021: 撤销 D011，重新瞄准 CoRL 2026（abstract DDL ~May 26） | — |\\n| D020 | 2026-05-14 | D020: obs_only val_loss (0.0165) 54% better than p | crm-train-v3-norm-obs-only, crm-train-v3-norm-scalar-unc, crm-train-v3-norm, eval-acr-spatial-v4-default |\\n| D019 | 2026-05-14 | D019: Normalization alone insufficient — magnitude | eval-acr-spatial-v4-default, eval-acr-spatial-v4-small, eval-argmin-only-spatial, eval-tiny-correction-spatial, eval-vla-mean-spatial |\\n| D018 | 2026-05-14 | D018: CRM 失败根因确认为输入未归一化（1500x scale 差异），批准 normali | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3 |\\n| D017 | 2026-05-14 | D017: CRM correction 全面拖累 baseline — kill 两路 ablat | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3, eval-vla-mean-spatial |\\n| D016 | 2026-05-14 | D016: CRM 训练/评估 state 维度不匹配 bug 确认，批准四项修复 + 重跑 pip | eval-acr-spatial-v2, eval-k5-spatial, eval-scalar-unc-spatial |\\n| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |\\n| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |\\n| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |\\n| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |\\n\\n\", \"total_chars\": 3518, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the project state. The memory.md already has a "Correction Magnitude 文献支撑" section from 2026-05-14 with some initial literature. I need to:

1. Do more targeted literature search on correction magnitude control methods
2. Analyze the argmin vs tiny-correction gap
3. Produce a comprehensive analysis document

Let me search for more specific literature on the topics mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "7d74ee3a-6a43-4e79-90da-d4c8f2674e88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQReTrwmYL8uPJvkTfx1UN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18441,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18441
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

_source line 15_

已有的 memory.md 包含初步文献支撑（PLD, TRANSIC, ResiP, DRC, DAWN）。现在做更深入的文献调研，聚焦 conformal-calibrated correction magnitude 方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "c08b6c0d-f43d-4a97-819c-1ee48ea27ad0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQReTrwmYL8uPJvkTfx1UN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18441,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18441
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HAaaGkatTYZBu23fMKnDwW`</summary>

```json
{
  "query": "conformal prediction action correction magnitude robotics manipulation 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "d941339b-002c-4e2d-9420-e607f044df55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQReTrwmYL8uPJvkTfx1UN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18441,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18441
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RZrnY4x3xfyDMjHTcq4Nb4`</summary>

```json
{
  "query": "residual policy learning magnitude constraint bounded correction robot 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "31bdfc87-c922-4c8e-800a-8395e4fa7a8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQReTrwmYL8uPJvkTfx1UN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18441,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18441
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

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014GNrn3bs4PQXjC3Wyob4mv`</summary>

```json
{
  "query": "conformal prediction calibrated intervention control safety constraint reinforcement learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "9a212d86-1fc4-44b1-b0f7-035e1b998e21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQReTrwmYL8uPJvkTfx1UN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18441,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18441
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

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GTXjwypn1sqYpc6kuwzXc9`</summary>

```json
{
  "query": "action correction scaling vision language action model VLA inference time 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "c269f5e0-0c1e-4aea-a1f4-46fa1fab699f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQReTrwmYL8uPJvkTfx1UN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18441,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18441
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

_source line 20 · 2026-05-15T01:31:39.322Z_

<details><summary>↩ Tool result · `toolu_01HAaaGkatTYZBu23fMKnDwW`</summary>

```text
Web search results for query: "conformal prediction action correction magnitude robotics manipulation 2024 2025 2026"

Links: [{"title":"Formal Verification and Control With Conformal Prediction: Practical Safety Guarantees For Autonomous Systems | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/5488303/11274416/11274485.pdf"},{"title":"160 IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 10, NO. 1, JANUARY 2025","url":"https://par.nsf.gov/servlets/purl/10574146"},{"title":"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://arxiv.org/html/2603.10392v1"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 8th Conference on Robot Learning Held in Munich, Germany on 06-09 November 2024 Published as Volume 270 by the Proceedings of Machine Learning Research on 12 January 2025. Volume Edited by: Pulkit Agrawal Oliver Kroemer Wolfram Burgard Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v270/"},{"title":"dblp: Robotics: Science and Systems 2024","url":"https://dblp.org/db/conf/rss/rss2024.html"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"5116 IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 8, NO. 8, AUGUST 2023","url":"https://www.georgejpappas.org/wp-content/uploads/2023/08/Safe_Planning_in_Dynamic_Environments_Using_Conformal_Prediction.pdf"},{"title":"What foundation models can bring for robot learning in manipulation: A survey - Dingzhe Li, Yixiang Jin, YuHao Sun, Yong A, Hongze Yu, Jun Shi, Xiaoshuai Hao, Peng Hao, Huaping Liu, Xiang Li, Xinde Li, Fuchun Sun, Jianwei Zhang, Bin Fang, 2025","url":"https://journals.sagepub.com/doi/10.1177/02783649251390579"},{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/full/10.1145/3736575"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"}]

I've performed the web search for your query on conformal prediction, action correction, magnitude, robotics manipulation from 2024-2026. Here are the key findings:

## Recent Research on Conformal Prediction in Robotics and Manipulation

The search results reveal several important developments in this area:

### Conformal Prediction Applications in Robotics

Recent work includes probabilistically correct language-based multi-robot planning using conformal prediction, published in January 2025.

A novel probabilistic safe control framework for human-robot interaction combines control barrier functions with conformal risk control to provide formal safety guarantees while considering complex human behavior, using conformal risk control to quantify and control prediction errors.

There is also recent work on conformalized teleoperation for confidently mapping human inputs to high-dimensional robot actions, presented at Robotics: Science and Systems 2024.

### Safe Planning with Conformal Prediction

An algorithm dynamically adjusts safety margins produced by conformal risk control based on the current interaction context.

### Broader Context

Conformal prediction is a distribution-free uncertainty quantification framework that reliably provides valid predictive inference for black-box models.

The research demonstrates that conformal prediction is being actively applied to robotics and manipulation tasks to provide formal safety guarantees and uncertainty quantification for robot control and planning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "989753bd-b4bd-4f71-a956-898454d62174",
  "tool_use_result": {
    "query": "conformal prediction action correction magnitude robotics manipulation 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U8g5ChV2n7PFZaZ3yCsfAL",
        "content": [
          {
            "title": "Formal Verification and Control With Conformal Prediction: Practical Safety Guarantees For Autonomous Systems | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/iel8/5488303/11274416/11274485.pdf"
          },
          {
            "title": "160 IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 10, NO. 1, JANUARY 2025",
            "url": "https://par.nsf.gov/servlets/purl/10574146"
          },
          {
            "title": "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://arxiv.org/html/2603.10392v1"
          },
          {
            "title": "Proceedings of Machine Learning Research | Proceedings of The 8th Conference on Robot Learning Held in Munich, Germany on 06-09 November 2024 Published as Volume 270 by the Proceedings of Machine Learning Research on 12 January 2025. Volume Edited by: Pulkit Agrawal Oliver Kroemer Wolfram Burgard Series Editors: Neil D. Lawrence",
            "url": "https://proceedings.mlr.press/v270/"
          },
          {
            "title": "dblp: Robotics: Science and Systems 2024",
            "url": "https://dblp.org/db/conf/rss/rss2024.html"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "5116 IEEE ROBOTICS AND AUTOMATION LETTERS, VOL. 8, NO. 8, AUGUST 2023",
            "url": "https://www.georgejpappas.org/wp-content/uploads/2023/08/Safe_Planning_in_Dynamic_Environments_Using_Conformal_Prediction.pdf"
          },
          {
            "title": "What foundation models can bring for robot learning in manipulation: A survey - Dingzhe Li, Yixiang Jin, YuHao Sun, Yong A, Hongze Yu, Jun Shi, Xiaoshuai Hao, Peng Hao, Huaping Liu, Xiang Li, Xinde Li, Fuchun Sun, Jianwei Zhang, Bin Fang, 2025",
            "url": "https://journals.sagepub.com/doi/10.1177/02783649251390579"
          },
          {
            "title": "Conformal Prediction: A Data Perspective | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/full/10.1145/3736575"
          },
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0031320325007113"
          }
        ]
      },
      "I've performed the web search for your query on conformal prediction, action correction, magnitude, robotics manipulation from 2024-2026. Here are the key findings:\n\n## Recent Research on Conformal Prediction in Robotics and Manipulation\n\nThe search results reveal several important developments in this area:\n\n### Conformal Prediction Applications in Robotics\n\nRecent work includes probabilistically correct language-based multi-robot planning using conformal prediction, published in January 2025.\n\nA novel probabilistic safe control framework for human-robot interaction combines control barrier functions with conformal risk control to provide formal safety guarantees while considering complex human behavior, using conformal risk control to quantify and control prediction errors.\n\nThere is also recent work on conformalized teleoperation for confidently mapping human inputs to high-dimensional robot actions, presented at Robotics: Science and Systems 2024.\n\n### Safe Planning with Conformal Prediction\n\nAn algorithm dynamically adjusts safety margins produced by conformal risk control based on the current interaction context.\n\n### Broader Context\n\nConformal prediction is a distribution-free uncertainty quantification framework that reliably provides valid predictive inference for black-box models.\n\nThe research demonstrates that conformal prediction is being actively applied to robotics and manipulation tasks to provide formal safety guarantees and uncertainty quantification for robot control and planning systems."
    ],
    "durationSeconds": 5.778388620999999
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T01:31:42.152Z_

<details><summary>↩ Tool result · `toolu_01RZrnY4x3xfyDMjHTcq4Nb4`</summary>

```text
Web search results for query: "residual policy learning magnitude constraint bounded correction robot 2024 2025"

Links: [{"title":"Residual Reinforcement Learning","url":"https://www.emergentmind.com/topics/residual-reinforcement-learning-rl"},{"title":"[1812.03201] Residual Reinforcement Learning for Robot Control","url":"https://arxiv.org/abs/1812.03201"},{"title":"GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub","url":"https://github.com/YanjieZe/Paper-List"},{"title":"Residual Policy Learning","url":"https://www.researchgate.net/publication/329734796_Residual_Policy_Learning"},{"title":"GitHub - k-r-allen/residual-policy-learning: Residual policy learning · GitHub","url":"https://github.com/k-r-allen/residual-policy-learning"},{"title":"[1812.06298] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298"},{"title":"[PDF] Residual Policy Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Residual-Policy-Learning-Silver-Allen/8c21a1d8844e6b58fd74b2b94c512a23497029c1"},{"title":"Residual Policy Learning for Shared Autonomy","url":"https://www.roboticsproceedings.org/rss16/p072.pdf"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 8th Conference on Robot Learning Held in Munich, Germany on 06-09 November 2024 Published as Volume 270 by the Proceedings of Machine Learning Research on 12 January 2025. Volume Edited by: Pulkit Agrawal Oliver Kroemer Wolfram Burgard Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v270/"},{"title":"Residual Skill Policies: Learning an Adaptable Skill-based Action Space for Reinforcement Learning for Robotics | OpenReview","url":"https://openreview.net/forum?id=0nb97NQypbK"}]

Based on the search results, here's what I found regarding residual policy learning with magnitude constraints and bounded corrections for robotics in 2024-2025:

## Key Findings:

**Residual Constraints and Safety:**
Residuals are often clipped into a "tube" around the base action, either by magnitude or as a percentage of the base policy's output to preserve the properties of the base controller. Lyapunov-based analyses demonstrate that such constraints yield uniformly ultimately bounded error and stability for generic mechanical systems.

**Recent Applications (2024-2025):**
Off-policy actor-critic methods (e.g., TD3, DDPG, SAC) are commonly used for continuous control, with recent work from 2025 demonstrating continued adoption. On-policy methods like PPO are preferred in settings with nonstationary dynamics or where the combination policy invalidates strict off-policy assumptions.

**Advanced Architectures:**
Residuals can be composited with robust, real-time controllers such as MPC for legged robots or aerial vehicles, achieving interpretable, constraint-satisfying, yet highly adaptable control. Blended MPC-residual architectures expand the achievable command envelope and improve asymptotic reward by 20-30%.

**Safe RL with Bounded Corrections:**
The synthesis of residual learning with control-barrier functions and disturbance observers yields RL agents capable of safe exploration even under significant model-bias and process disturbances.

The search results show that magnitude-constrained bounded residual corrections are a well-established technique in contemporary robot control, with continued development through 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "0b99ab51-8e4f-460a-923c-48e9efaaa3e7",
  "tool_use_result": {
    "query": "residual policy learning magnitude constraint bounded correction robot 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ku3Jr5yLpmZ6uStWb6e7Hz",
        "content": [
          {
            "title": "Residual Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/residual-reinforcement-learning-rl"
          },
          {
            "title": "[1812.03201] Residual Reinforcement Learning for Robot Control",
            "url": "https://arxiv.org/abs/1812.03201"
          },
          {
            "title": "GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub",
            "url": "https://github.com/YanjieZe/Paper-List"
          },
          {
            "title": "Residual Policy Learning",
            "url": "https://www.researchgate.net/publication/329734796_Residual_Policy_Learning"
          },
          {
            "title": "GitHub - k-r-allen/residual-policy-learning: Residual policy learning · GitHub",
            "url": "https://github.com/k-r-allen/residual-policy-learning"
          },
          {
            "title": "[1812.06298] Residual Policy Learning",
            "url": "https://arxiv.org/abs/1812.06298"
          },
          {
            "title": "[PDF] Residual Policy Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Residual-Policy-Learning-Silver-Allen/8c21a1d8844e6b58fd74b2b94c512a23497029c1"
          },
          {
            "title": "Residual Policy Learning for Shared Autonomy",
            "url": "https://www.roboticsproceedings.org/rss16/p072.pdf"
          },
          {
            "title": "Proceedings of Machine Learning Research | Proceedings of The 8th Conference on Robot Learning Held in Munich, Germany on 06-09 November 2024 Published as Volume 270 by the Proceedings of Machine Learning Research on 12 January 2025. Volume Edited by: Pulkit Agrawal Oliver Kroemer Wolfram Burgard Series Editors: Neil D. Lawrence",
            "url": "https://proceedings.mlr.press/v270/"
          },
          {
            "title": "Residual Skill Policies: Learning an Adaptable Skill-based Action Space for Reinforcement Learning for Robotics | OpenReview",
            "url": "https://openreview.net/forum?id=0nb97NQypbK"
          }
        ]
      },
      "Based on the search results, here's what I found regarding residual policy learning with magnitude constraints and bounded corrections for robotics in 2024-2025:\n\n## Key Findings:\n\n**Residual Constraints and Safety:**\nResiduals are often clipped into a \"tube\" around the base action, either by magnitude or as a percentage of the base policy's output to preserve the properties of the base controller. Lyapunov-based analyses demonstrate that such constraints yield uniformly ultimately bounded error and stability for generic mechanical systems.\n\n**Recent Applications (2024-2025):**\nOff-policy actor-critic methods (e.g., TD3, DDPG, SAC) are commonly used for continuous control, with recent work from 2025 demonstrating continued adoption. On-policy methods like PPO are preferred in settings with nonstationary dynamics or where the combination policy invalidates strict off-policy assumptions.\n\n**Advanced Architectures:**\nResiduals can be composited with robust, real-time controllers such as MPC for legged robots or aerial vehicles, achieving interpretable, constraint-satisfying, yet highly adaptable control. Blended MPC-residual architectures expand the achievable command envelope and improve asymptotic reward by 20-30%.\n\n**Safe RL with Bounded Corrections:**\nThe synthesis of residual learning with control-barrier functions and disturbance observers yields RL agents capable of safe exploration even under significant model-bias and process disturbances.\n\nThe search results show that magnitude-constrained bounded residual corrections are a well-established technique in contemporary robot control, with continued development through 2025."
    ],
    "durationSeconds": 7.665648976999997
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T01:31:43.448Z_

<details><summary>↩ Tool result · `toolu_01GTXjwypn1sqYpc6kuwzXc9`</summary>

```text
Web search results for query: "action correction scaling vision language action model VLA inference time 2025 2026"

Links: [{"title":"[2512.02834] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://arxiv.org/abs/2512.02834"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/abs/2505.04769"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Vision-Language-Action Instruction Tuning: From Understanding to Manipulation | OpenReview","url":"https://openreview.net/forum?id=tsxwloasw5"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"}]

Based on the web search results, I found several highly relevant papers and developments related to action correction scaling in Vision-Language-Action (VLA) models with a focus on inference-time approaches from 2025-2026:

## Key Findings:

### Action Correction and Test-Time Scaling

TACO is a test-time-scaling (TTS) framework that applies a lightweight pseudo-count estimator as a high-fidelity verifier of action chunks. VLA models integrated with TACO can execute the actions with maximum pseudo-count from all sampled action chunks, thereby preventing distribution shifts while preserving the generalization ability of VLAs since the constraint is applied only during inference. This approach was published in December 2025 and addresses inference-time fragility in VLAs.

### Correction Rules and Hybrid Approaches

Another notable development from December 2025 is the 2025 BEHAVIOR Challenge winner, which uses action compression and challenge-specific correction rules during inference. The approach complements the learned policy with correction rules derived from failure analysis: simple heuristics that detect and recover from common failure modes.

### Inference-Time Scaling

InstructVLA exhibits inference-time scaling by leveraging textual reasoning to boost manipulation performance in both simulated and real-world settings.

### VLA Efficiency and Inference Optimization

More broadly, VLA systems face challenges including high inference latency and insufficient frequency, incompatible with the sub-second control cycles required for responsive manipulation. Recent work has focused on optimizing inference through various architectural and computational strategies to address these real-time control requirements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "65e8d149-bb58-4de7-96db-61646dea5c04",
  "tool_use_result": {
    "query": "action correction scaling vision language action model VLA inference time 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q4RHnPnjcXrX6p8Nh8hFgU",
        "content": [
          {
            "title": "[2512.02834] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://arxiv.org/abs/2512.02834"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.06951v1"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/abs/2505.04769"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"
          },
          {
            "title": "Vision-Language-Action Instruction Tuning: From Understanding to Manipulation | OpenReview",
            "url": "https://openreview.net/forum?id=tsxwloasw5"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v2"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v1"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant papers and developments related to action correction scaling in Vision-Language-Action (VLA) models with a focus on inference-time approaches from 2025-2026:\n\n## Key Findings:\n\n### Action Correction and Test-Time Scaling\n\nTACO is a test-time-scaling (TTS) framework that applies a lightweight pseudo-count estimator as a high-fidelity verifier of action chunks. VLA models integrated with TACO can execute the actions with maximum pseudo-count from all sampled action chunks, thereby preventing distribution shifts while preserving the generalization ability of VLAs since the constraint is applied only during inference. This approach was published in December 2025 and addresses inference-time fragility in VLAs.\n\n### Correction Rules and Hybrid Approaches\n\nAnother notable development from December 2025 is the 2025 BEHAVIOR Challenge winner, which uses action compression and challenge-specific correction rules during inference. The approach complements the learned policy with correction rules derived from failure analysis: simple heuristics that detect and recover from common failure modes.\n\n### Inference-Time Scaling\n\nInstructVLA exhibits inference-time scaling by leveraging textual reasoning to boost manipulation performance in both simulated and real-world settings.\n\n### VLA Efficiency and Inference Optimization\n\nMore broadly, VLA systems face challenges including high inference latency and insufficient frequency, incompatible with the sub-second control cycles required for responsive manipulation. Recent work has focused on optimizing inference through various architectural and computational strategies to address these real-time control requirements."
    ],
    "durationSeconds": 7.552985719999997
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T01:31:47.100Z_

<details><summary>↩ Tool result · `toolu_014GNrn3bs4PQXjC3Wyob4mv`</summary>

```text
Web search results for query: "conformal prediction calibrated intervention control safety constraint reinforcement learning 2025 2026"

Links: [{"title":"[2503.17678] Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/abs/2503.17678"},{"title":"Conformal Signal Temporal Logic for Robust Reinforcement Learning Control: A Case Study Preprint. Accepted at ICASSP 2026.","url":"https://arxiv.org/html/2602.14322"},{"title":"Statistically Assuring Safety of Control Systems using Ensembles of Safety Filters and Conformal Prediction","url":"https://arxiv.org/html/2511.07899"},{"title":"Safe Urban Traffic Control via Uncertainty-Aware Conformal Prediction and World-Model Reinforcement Learning","url":"https://arxiv.org/html/2602.04821"},{"title":"[2602.04821] Safe Urban Traffic Control via Uncertainty-Aware Conformal Prediction and World-Model Reinforcement Learning","url":"https://arxiv.org/abs/2602.04821"},{"title":"Learning to Navigate Under Imperfect Perception: Conformalised Segmentation for Safe Reinforcement Learning","url":"https://arxiv.org/html/2510.18485"},{"title":"Safe Planning in Interactive Environments via Iterative Policy Updates and Adversarially Robust Conformal Prediction","url":"https://arxiv.org/html/2511.10586"},{"title":"[2511.10586] Safe Planning in Interactive Environments via Iterative Policy Updates and Adversarially Robust Conformal Prediction","url":"https://arxiv.org/abs/2511.10586"},{"title":"Safe POMDP Online Planning Among Dynamic Agents via Adaptive Conformal Prediction | Request PDF","url":"https://www.researchgate.net/publication/384342944_Safe_POMDP_Online_Planning_Among_Dynamic_Agents_Via_Adaptive_Conformal_Prediction"},{"title":"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/html/2503.17678"}]

Based on the search results, here are several recent papers (2025-2026) that combine conformal prediction, calibrated interventions, safety constraints, and reinforcement learning:

## Key Recent Works

1. **Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction (March 2025)**
   - Uses Adaptive Conformal Prediction (ACP) to quantify uncertainty and combines it with Control Barrier Functions (CBF) to characterize uncertainty-aware safe control constraints
   - Integrates an optimism-based exploration strategy with ACP-based CBFs for safe exploration and near-optimal safe nonlinear control

2. **Conformal Signal Temporal Logic for Robust Reinforcement Learning Control (Accepted at ICASSP 2026)**
   - Proposes a safe RL framework for F–16 flight control that integrates conformal STL monitoring with a runtime shield
   - Uses a short-horizon predictor calibrated via robust conformal prediction to forecast critical states, and when worst-case robustness becomes non-positive, the shield overrides the RL action with a safe recovery maneuver

3. **Statistically Assuring Safety of Control Systems using Ensembles of Safety Filters and Conformal Prediction (November 2025)**
   - Leverages conformal prediction to provide probabilistic safety guarantees when using learned Hamilton-Jacobi value functions and policies
   - Investigates an ensemble approach where multiple HJ value functions are independently trained and calibrated, exploring different aggregation methods for safe policies

4. **Safe Urban Traffic Control via Uncertainty-Aware Conformal Prediction and World-Model Reinforcement Learning (February 2026)**
   - Introduces the first framework to propagate calibrated uncertainty from forecasting through anomaly detection to safe policy learning with end-to-end theoretical guarantees

5. **Learning to Navigate Under Imperfect Perception: Conformalised Segmentation for Safe Reinforcement Learning (October 2025)**
   - Integrates conformal prediction directly into the perception stream for safe navigation, calibrating per-pixel hazard scores into set-valued hazard maps with finite-sample guarantees

6. **Safe Planning in Interactive Environments via Iterative Policy Updates and Adversarially Robust Conformal Prediction (November 2025)**
   - Addresses safe planning in interactive environments where the agent's control policy may change the environment's behavior

These papers represent active research into combining conformal prediction's distribution-free guarantees with safe reinforcement learning and control constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "486cc759-29cc-46cf-a53e-ff39ed378f91",
  "tool_use_result": {
    "query": "conformal prediction calibrated intervention control safety constraint reinforcement learning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Go9B2yVfHmmNaEGZGoxmfK",
        "content": [
          {
            "title": "[2503.17678] Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction",
            "url": "https://arxiv.org/abs/2503.17678"
          },
          {
            "title": "Conformal Signal Temporal Logic for Robust Reinforcement Learning Control: A Case Study Preprint. Accepted at ICASSP 2026.",
            "url": "https://arxiv.org/html/2602.14322"
          },
          {
            "title": "Statistically Assuring Safety of Control Systems using Ensembles of Safety Filters and Conformal Prediction",
            "url": "https://arxiv.org/html/2511.07899"
          },
          {
            "title": "Safe Urban Traffic Control via Uncertainty-Aware Conformal Prediction and World-Model Reinforcement Learning",
            "url": "https://arxiv.org/html/2602.04821"
          },
          {
            "title": "[2602.04821] Safe Urban Traffic Control via Uncertainty-Aware Conformal Prediction and World-Model Reinforcement Learning",
            "url": "https://arxiv.org/abs/2602.04821"
          },
          {
            "title": "Learning to Navigate Under Imperfect Perception: Conformalised Segmentation for Safe Reinforcement Learning",
            "url": "https://arxiv.org/html/2510.18485"
          },
          {
            "title": "Safe Planning in Interactive Environments via Iterative Policy Updates and Adversarially Robust Conformal Prediction",
            "url": "https://arxiv.org/html/2511.10586"
          },
          {
            "title": "[2511.10586] Safe Planning in Interactive Environments via Iterative Policy Updates and Adversarially Robust Conformal Prediction",
            "url": "https://arxiv.org/abs/2511.10586"
          },
          {
            "title": "Safe POMDP Online Planning Among Dynamic Agents via Adaptive Conformal Prediction | Request PDF",
            "url": "https://www.researchgate.net/publication/384342944_Safe_POMDP_Online_Planning_Among_Dynamic_Agents_Via_Adaptive_Conformal_Prediction"
          },
          {
            "title": "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction",
            "url": "https://arxiv.org/html/2503.17678"
          }
        ]
      },
      "Based on the search results, here are several recent papers (2025-2026) that combine conformal prediction, calibrated interventions, safety constraints, and reinforcement learning:\n\n## Key Recent Works\n\n1. **Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction (March 2025)**\n   - Uses Adaptive Conformal Prediction (ACP) to quantify uncertainty and combines it with Control Barrier Functions (CBF) to characterize uncertainty-aware safe control constraints\n   - Integrates an optimism-based exploration strategy with ACP-based CBFs for safe exploration and near-optimal safe nonlinear control\n\n2. **Conformal Signal Temporal Logic for Robust Reinforcement Learning Control (Accepted at ICASSP 2026)**\n   - Proposes a safe RL framework for F–16 flight control that integrates conformal STL monitoring with a runtime shield\n   - Uses a short-horizon predictor calibrated via robust conformal prediction to forecast critical states, and when worst-case robustness becomes non-positive, the shield overrides the RL action with a safe recovery maneuver\n\n3. **Statistically Assuring Safety of Control Systems using Ensembles of Safety Filters and Conformal Prediction (November 2025)**\n   - Leverages conformal prediction to provide probabilistic safety guarantees when using learned Hamilton-Jacobi value functions and policies\n   - Investigates an ensemble approach where multiple HJ value functions are independently trained and calibrated, exploring different aggregation methods for safe policies\n\n4. **Safe Urban Traffic Control via Uncertainty-Aware Conformal Prediction and World-Model Reinforcement Learning (February 2026)**\n   - Introduces the first framework to propagate calibrated uncertainty from forecasting through anomaly detection to safe policy learning with end-to-end theoretical guarantees\n\n5. **Learning to Navigate Under Imperfect Perception: Conformalised Segmentation for Safe Reinforcement Learning (October 2025)**\n   - Integrates conformal prediction directly into the perception stream for safe navigation, calibrating per-pixel hazard scores into set-valued hazard maps with finite-sample guarantees\n\n6. **Safe Planning in Interactive Environments via Iterative Policy Updates and Adversarially Robust Conformal Prediction (November 2025)**\n   - Addresses safe planning in interactive environments where the agent's control policy may change the environment's behavior\n\nThese papers represent active research into combining conformal prediction's distribution-free guarantees with safe reinforcement learning and control constraints."
    ],
    "durationSeconds": 11.614522596999995
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have additional papers to consider. Let me search for a few more specific topics:
1. The TACO paper (test-time anti-exploration scaling for VLAs)
2. The conformal STL paper for RL
3. SafeDiffCon (already in literature_map)

Let me also search for more specific papers on adaptive/calibrated correction magnitude.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "02eb57d9-9a28-469f-beff-27cdb64307af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYo7TpJPrMqEhJ6szUsjRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 915,
      "cache_creation_input_tokens": 3698,
      "cache_read_input_tokens": 43815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3698
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

_source line 25_

找到了几个新的相关方向。进一步搜索 TACO (test-time scaling for VLA) 和 adaptive correction magnitude 的具体机制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "871a15c9-e57f-4b01-8bbf-8960c666626e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYo7TpJPrMqEhJ6szUsjRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 915,
      "cache_creation_input_tokens": 3698,
      "cache_read_input_tokens": 43815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3698
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LTrXToLbvnJKTPUsWEHdNX`</summary>

```json
{
  "query": "TACO test time anti-exploration VLA pseudo-count action correction arxiv 2512.02834"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "53c4b767-e202-4faf-8df1-3497c0d07f00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYo7TpJPrMqEhJ6szUsjRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 915,
      "cache_creation_input_tokens": 3698,
      "cache_read_input_tokens": 43815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3698
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RArrAdnVhD3Fqb1aMC3fmp`</summary>

```json
{
  "query": "\"adaptive correction\" \"prediction interval\" \"upper bound\" magnitude reinforcement learning policy 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "33cf0561-5793-4dfd-baed-ed4f5067e4e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYo7TpJPrMqEhJ6szUsjRJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 915,
      "cache_creation_input_tokens": 3698,
      "cache_read_input_tokens": 43815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3698
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

_source line 28 · 2026-05-15T01:32:21.567Z_

<details><summary>↩ Tool result · `toolu_01LTrXToLbvnJKTPUsWEHdNX`</summary>

```text
Web search results for query: "TACO test time anti-exploration VLA pseudo-count action correction arxiv 2512.02834"

Links: [{"title":"[2512.02834] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://arxiv.org/abs/2512.02834"},{"title":"Paper page - Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://huggingface.co/papers/2512.02834"},{"title":"Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://arxiv.org/html/2512.02834v1"},{"title":"TACO: Steering Vision-Language-Action Models as Anti-Exploration","url":"https://vla-anti-exploration.github.io/"},{"title":"[2512.02834v1] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://arxiv.org/abs/2512.02834v1"},{"title":"Steering Vision-Language-Action Models as","url":"https://arxiv.org/pdf/2512.02834"},{"title":"GitHub - breez3young/TACO: Official Implementation of \"Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach\"","url":"https://github.com/breez3young/TACO/"},{"title":"(PDF) Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://www.researchgate.net/publication/398269618_Steering_Vision-Language-Action_Models_as_Anti-Exploration_A_Test-Time_Scaling_Approach"},{"title":"[Literature Review] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://www.themoonlight.io/en/review/steering-vision-language-action-models-as-anti-exploration-a-test-time-scaling-approach"},{"title":"cool ai and ml papers on X: \"TACO selects the highest pseudo-count action sequence at test time to steer diffusion/flow VLA policies toward stable behavior, improving success without retraining. Useful for deploying VLAs from imperfect demos; probably not relevant for online RL or non-generative... https://t.co/UlHG1mc58U\" / X","url":"https://x.com/aimodelsfyi/status/1997380183557599242"}]

I found the research paper you were looking for. Here's a summary of the key information:

## TACO: Steering Vision-Language-Action Models as Anti-Exploration

TACO is a test-time-scaling (TTS) framework that applies a lightweight pseudo-count estimator as a high-fidelity verifier of action chunks.

**Problem Being Addressed:**
VLAs incorporate diverse data modes in the pre-training stage, and the finetuning dataset often contains demonstration data collected in a kinematically suboptimal or undesirable way, resulting in redundant action modes that are irrelevant to the success action modes of the downstream task.

**Core Approach:**
TACO addresses this instability by applying a lightweight pseudo-count estimator as a high-fidelity verifier of action chunks. The VLA models integrated with TACO can execute the actions with maximum pseudo-count from all sampled action chunks, thereby preventing distribution shifts while preserving the generalization ability of VLAs since the constraint is applied only during inference.

**Key Advantages:**
The method resembles the classical anti-exploration principle in offline reinforcement learning (RL), and being gradient-free, it incurs significant computational benefits compared to RL update, especially for flow or diffusion-based VLAs which are difficult to perform RL update due to denoising process.

**Results:**
Extensive experiments across four simulation benchmarks (RoboTwin2.0, Robotwin, LIBERO, SimplerEnv) and a dual-arm platform demonstrate that the method significantly improves the inference stability and success rates in downstream-task adaptations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "a6403d44-7ab4-482a-ab78-45b5410ad47a",
  "tool_use_result": {
    "query": "TACO test time anti-exploration VLA pseudo-count action correction arxiv 2512.02834",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Mqunh5532Pn3ZDraaF6792",
        "content": [
          {
            "title": "[2512.02834] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://arxiv.org/abs/2512.02834"
          },
          {
            "title": "Paper page - Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://huggingface.co/papers/2512.02834"
          },
          {
            "title": "Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://arxiv.org/html/2512.02834v1"
          },
          {
            "title": "TACO: Steering Vision-Language-Action Models as Anti-Exploration",
            "url": "https://vla-anti-exploration.github.io/"
          },
          {
            "title": "[2512.02834v1] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://arxiv.org/abs/2512.02834v1"
          },
          {
            "title": "Steering Vision-Language-Action Models as",
            "url": "https://arxiv.org/pdf/2512.02834"
          },
          {
            "title": "GitHub - breez3young/TACO: Official Implementation of \"Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach\"",
            "url": "https://github.com/breez3young/TACO/"
          },
          {
            "title": "(PDF) Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://www.researchgate.net/publication/398269618_Steering_Vision-Language-Action_Models_as_Anti-Exploration_A_Test-Time_Scaling_Approach"
          },
          {
            "title": "[Literature Review] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://www.themoonlight.io/en/review/steering-vision-language-action-models-as-anti-exploration-a-test-time-scaling-approach"
          },
          {
            "title": "cool ai and ml papers on X: \"TACO selects the highest pseudo-count action sequence at test time to steer diffusion/flow VLA policies toward stable behavior, improving success without retraining. Useful for deploying VLAs from imperfect demos; probably not relevant for online RL or non-generative... https://t.co/UlHG1mc58U\" / X",
            "url": "https://x.com/aimodelsfyi/status/1997380183557599242"
          }
        ]
      },
      "I found the research paper you were looking for. Here's a summary of the key information:\n\n## TACO: Steering Vision-Language-Action Models as Anti-Exploration\n\nTACO is a test-time-scaling (TTS) framework that applies a lightweight pseudo-count estimator as a high-fidelity verifier of action chunks.\n\n**Problem Being Addressed:**\nVLAs incorporate diverse data modes in the pre-training stage, and the finetuning dataset often contains demonstration data collected in a kinematically suboptimal or undesirable way, resulting in redundant action modes that are irrelevant to the success action modes of the downstream task.\n\n**Core Approach:**\nTACO addresses this instability by applying a lightweight pseudo-count estimator as a high-fidelity verifier of action chunks. The VLA models integrated with TACO can execute the actions with maximum pseudo-count from all sampled action chunks, thereby preventing distribution shifts while preserving the generalization ability of VLAs since the constraint is applied only during inference.\n\n**Key Advantages:**\nThe method resembles the classical anti-exploration principle in offline reinforcement learning (RL), and being gradient-free, it incurs significant computational benefits compared to RL update, especially for flow or diffusion-based VLAs which are difficult to perform RL update due to denoising process.\n\n**Results:**\nExtensive experiments across four simulation benchmarks (RoboTwin2.0, Robotwin, LIBERO, SimplerEnv) and a dual-arm platform demonstrate that the method significantly improves the inference stability and success rates in downstream-task adaptations."
    ],
    "durationSeconds": 7.150643112999998
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T01:32:24.585Z_

<details><summary>↩ Tool result · `toolu_01RArrAdnVhD3Fqb1aMC3fmp`</summary>

```text
Web search results for query: ""adaptive correction" "prediction interval" "upper bound" magnitude reinforcement learning policy 2024 2025"

Links: [{"title":"Reinforcement Learning with Adaptive Regularization for Safe Control of Critical Systems | OpenReview","url":"https://openreview.net/forum?id=MRO2QhydPF"},{"title":"GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub","url":"https://github.com/yingchengyang/Reinforcement-Learning-Papers"},{"title":"Adaptive Scaling of Policy Constraints for Offline Reinforcement Learning","url":"https://arxiv.org/pdf/2508.19900"},{"title":"[2405.19909] Adaptive Advantage-Guided Policy Regularization for Offline Reinforcement Learning","url":"https://arxiv.org/abs/2405.19909"},{"title":"GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-model-based-RL"},{"title":"Reinforcement Learning in Process Industries: Review and Perspective","url":"https://www.ieee-jas.net/article/doi/10.1109/JAS.2024.124227"},{"title":"Adaptive Advantage-Guided Policy Regularization for Offline Reinforcement Learning","url":"https://arxiv.org/html/2405.19909v2"},{"title":"CS 542 Stat RL: Project Topics & References","url":"https://nanjiang.cs.illinois.edu/cs598project/"},{"title":"The State of Reinforcement Learning in 2025 - DataRoot Labs","url":"https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"},{"title":"NeurIPS 2024 Papers","url":"https://nips.cc/virtual/2024/papers.html"}]

I've completed a web search for the query about adaptive correction, prediction intervals, upper bounds, magnitude in reinforcement learning policy research from 2024-2025. Here are the relevant results:

## Key Findings:

**Recent Reinforcement Learning Papers (2024-2025):**

1. **Safe RL with Adaptive Regularization**: RL with Adaptive Regularization (RL-AR) enables safe RL exploration by combining the RL policy with a policy regularizer, with a "focus module" that determines the appropriate combination depending on the state. This was published as a NeurIPS 2024 paper.

2. **Adaptive Advantage-Guided Policy Regularization**: Adaptive Advantage-guided Policy Regularization (A2PR) obtains high-advantage actions from an augmented behavior policy combined with VAE to guide the learned policy. It effectively mitigates value overestimation with a bounded performance gap.

3. **Adaptive Scaling of Policy Constraints**: Research on offline reinforcement learning includes Adaptive Scaling of Policy Constraints (ASPC) for Offline Reinforcement Learning, addressing methods for improving policy learning in offline settings.

The search results show active research in 2024-2025 on adaptive methods in reinforcement learning, particularly focusing on policy regularization, safety constraints, and bounded performance guarantees. However, the specific combination of all the terms in your query (especially "prediction interval upper bound magnitude") appears to be quite specialized, and a more targeted search might be needed to find papers using that exact terminology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "b10c6383-e204-42c9-b61d-04816e7975b7",
  "tool_use_result": {
    "query": "\"adaptive correction\" \"prediction interval\" \"upper bound\" magnitude reinforcement learning policy 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018FM2Z15MgtGArBm7KAtRnJ",
        "content": [
          {
            "title": "Reinforcement Learning with Adaptive Regularization for Safe Control of Critical Systems | OpenReview",
            "url": "https://openreview.net/forum?id=MRO2QhydPF"
          },
          {
            "title": "GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub",
            "url": "https://github.com/yingchengyang/Reinforcement-Learning-Papers"
          },
          {
            "title": "Adaptive Scaling of Policy Constraints for Offline Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2508.19900"
          },
          {
            "title": "[2405.19909] Adaptive Advantage-Guided Policy Regularization for Offline Reinforcement Learning",
            "url": "https://arxiv.org/abs/2405.19909"
          },
          {
            "title": "GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-model-based-RL"
          },
          {
            "title": "Reinforcement Learning in Process Industries: Review and Perspective",
            "url": "https://www.ieee-jas.net/article/doi/10.1109/JAS.2024.124227"
          },
          {
            "title": "Adaptive Advantage-Guided Policy Regularization for Offline Reinforcement Learning",
            "url": "https://arxiv.org/html/2405.19909v2"
          },
          {
            "title": "CS 542 Stat RL: Project Topics & References",
            "url": "https://nanjiang.cs.illinois.edu/cs598project/"
          },
          {
            "title": "The State of Reinforcement Learning in 2025 - DataRoot Labs",
            "url": "https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"
          },
          {
            "title": "NeurIPS 2024 Papers",
            "url": "https://nips.cc/virtual/2024/papers.html"
          }
        ]
      },
      "I've completed a web search for the query about adaptive correction, prediction intervals, upper bounds, magnitude in reinforcement learning policy research from 2024-2025. Here are the relevant results:\n\n## Key Findings:\n\n**Recent Reinforcement Learning Papers (2024-2025):**\n\n1. **Safe RL with Adaptive Regularization**: RL with Adaptive Regularization (RL-AR) enables safe RL exploration by combining the RL policy with a policy regularizer, with a \"focus module\" that determines the appropriate combination depending on the state. This was published as a NeurIPS 2024 paper.\n\n2. **Adaptive Advantage-Guided Policy Regularization**: Adaptive Advantage-guided Policy Regularization (A2PR) obtains high-advantage actions from an augmented behavior policy combined with VAE to guide the learned policy. It effectively mitigates value overestimation with a bounded performance gap.\n\n3. **Adaptive Scaling of Policy Constraints**: Research on offline reinforcement learning includes Adaptive Scaling of Policy Constraints (ASPC) for Offline Reinforcement Learning, addressing methods for improving policy learning in offline settings.\n\nThe search results show active research in 2024-2025 on adaptive methods in reinforcement learning, particularly focusing on policy regularization, safety constraints, and bounded performance guarantees. However, the specific combination of all the terms in your query (especially \"prediction interval upper bound magnitude\") appears to be quite specialized, and a more targeted search might be needed to find papers using that exact terminology."
    ],
    "durationSeconds": 10.070036978000005
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to compose the analysis document. Let me also search for one more specific topic - SafeDiffCon and the conformal-guided diffusion control concept which is highly relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "d437ad53-7715-4dbc-8cb7-47bd03435779",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtSFMLuYNv7FzXVs8tYTMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3104,
      "cache_read_input_tokens": 47513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3104
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

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXURjyKY67rhDj3iZ2WWa9`</summary>

```json
{
  "query": "SafeDiffCon conformal prediction diffusion model safe control uncertainty quantile 2025 ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "dff56092-5cb4-4703-b907-978cbdaceb13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtSFMLuYNv7FzXVs8tYTMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3104,
      "cache_read_input_tokens": 47513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3104
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017VARUGxKipiCKXHFfVQqtc`</summary>

```json
{
  "query": "\"correction magnitude\" \"U-shaped\" performance degradation over-correction robot policy 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "136a2c76-a900-4f3b-a98b-b7f6ce882456",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtSFMLuYNv7FzXVs8tYTMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3104,
      "cache_read_input_tokens": 47513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3104
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

_source line 33 · 2026-05-15T01:32:34.338Z_

<details><summary>↩ Tool result · `toolu_017VARUGxKipiCKXHFfVQqtc`</summary>

```text
Web search results for query: ""correction magnitude" "U-shaped" performance degradation over-correction robot policy 2024 2025"

Links: [{"title":"On-Device Diffusion Transformer Policy for Efficient Robot Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"},{"title":"arXiv:2406.15917v1 [cs.RO] 22 Jun 2024","url":"https://cicl.stanford.edu/papers/du2024robotic.pdf"},{"title":"From Mystery to Mastery: Failure Diagnosis for Improving Manipulation Policies","url":"https://arxiv.org/html/2412.02818v2"},{"title":"Data-Driven Calibration of Industrial Robots: A Comprehensive Survey","url":"https://www.ieee-jas.net/en/article/doi/10.1109/JAS.2025.125237"},{"title":"Towards Robust and Provably Generalizable Robot Learning Zhiyi “Allen” Ren","url":"https://irom-lab.princeton.edu/wp-content/uploads/2025/02/Ren_princeton_thesis.pdf"},{"title":"Safe Policy Optimization for Reinforcement Learning in ...","url":"http://staff.ustc.edu.cn/~zkan/Papers/Bood%20Chapter/2024_Safe%20Optimization.pdf"},{"title":"Towards manufacturing robotics accuracy degradation assessment","url":"https://www.semanticscholar.org/paper/Towards-manufacturing-robotics-accuracy-degradation-Izagirre-Andonegui/e8b47db9d3026a240a2bf26dd94c9c8a4f88f0c2"},{"title":"AI Model Drift: Detect & Correct Degradation","url":"https://www.qodequay.com/ai-model-drift-detecting-and-correcting-performance-degradation"},{"title":"Towards manufacturing robotics accuracy degradation assessment: A vision-based data-driven implementation | Request PDF","url":"https://www.researchgate.net/publication/343138795_Towards_manufacturing_robotics_accuracy_degradation_assessment_A_vision-based_data-driven_implementation"},{"title":"Frontiers | Versatile graceful degradation framework for bio-inspired proprioception with redundant soft sensors","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1504651/full"}]

The search results don't contain specific information about a "U-shaped" relationship between correction magnitude and performance degradation related to over-correction in robot policies from 2024-2025. The results cover various aspects of robot policy learning, failure diagnosis, and sensor degradation, but not the specific phenomenon you're asking about.

The papers found discuss robot manipulation policies, failure detection, and policy improvement, but none specifically address the concept of a U-shaped performance curve as a function of correction magnitude or the dynamics of over-correction effects.

Would you like me to:
1. Search for related concepts like "policy correction" and "over-correction" separately?
2. Look for papers specifically on "learning from corrections" or "interactive learning" in robotics?
3. Search for more recent preprints or conference proceedings that might discuss this phenomenon?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "bb575ab0-e907-40a6-b3ff-3684760860dd",
  "tool_use_result": {
    "query": "\"correction magnitude\" \"U-shaped\" performance degradation over-correction robot policy 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MXnbRgbFNJUyQJqp8j56Lq",
        "content": [
          {
            "title": "On-Device Diffusion Transformer Policy for Efficient Robot Manipulation",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf"
          },
          {
            "title": "arXiv:2406.15917v1 [cs.RO] 22 Jun 2024",
            "url": "https://cicl.stanford.edu/papers/du2024robotic.pdf"
          },
          {
            "title": "From Mystery to Mastery: Failure Diagnosis for Improving Manipulation Policies",
            "url": "https://arxiv.org/html/2412.02818v2"
          },
          {
            "title": "Data-Driven Calibration of Industrial Robots: A Comprehensive Survey",
            "url": "https://www.ieee-jas.net/en/article/doi/10.1109/JAS.2025.125237"
          },
          {
            "title": "Towards Robust and Provably Generalizable Robot Learning Zhiyi “Allen” Ren",
            "url": "https://irom-lab.princeton.edu/wp-content/uploads/2025/02/Ren_princeton_thesis.pdf"
          },
          {
            "title": "Safe Policy Optimization for Reinforcement Learning in ...",
            "url": "http://staff.ustc.edu.cn/~zkan/Papers/Bood%20Chapter/2024_Safe%20Optimization.pdf"
          },
          {
            "title": "Towards manufacturing robotics accuracy degradation assessment",
            "url": "https://www.semanticscholar.org/paper/Towards-manufacturing-robotics-accuracy-degradation-Izagirre-Andonegui/e8b47db9d3026a240a2bf26dd94c9c8a4f88f0c2"
          },
          {
            "title": "AI Model Drift: Detect & Correct Degradation",
            "url": "https://www.qodequay.com/ai-model-drift-detecting-and-correcting-performance-degradation"
          },
          {
            "title": "Towards manufacturing robotics accuracy degradation assessment: A vision-based data-driven implementation | Request PDF",
            "url": "https://www.researchgate.net/publication/343138795_Towards_manufacturing_robotics_accuracy_degradation_assessment_A_vision-based_data-driven_implementation"
          },
          {
            "title": "Frontiers | Versatile graceful degradation framework for bio-inspired proprioception with redundant soft sensors",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1504651/full"
          }
        ]
      },
      "The search results don't contain specific information about a \"U-shaped\" relationship between correction magnitude and performance degradation related to over-correction in robot policies from 2024-2025. The results cover various aspects of robot policy learning, failure diagnosis, and sensor degradation, but not the specific phenomenon you're asking about.\n\nThe papers found discuss robot manipulation policies, failure detection, and policy improvement, but none specifically address the concept of a U-shaped performance curve as a function of correction magnitude or the dynamics of over-correction effects.\n\nWould you like me to:\n1. Search for related concepts like \"policy correction\" and \"over-correction\" separately?\n2. Look for papers specifically on \"learning from corrections\" or \"interactive learning\" in robotics?\n3. Search for more recent preprints or conference proceedings that might discuss this phenomenon?"
    ],
    "durationSeconds": 4.142456418000002
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T01:32:35.338Z_

<details><summary>↩ Tool result · `toolu_01VXURjyKY67rhDj3iZ2WWa9`</summary>

```text
Web search results for query: "SafeDiffCon conformal prediction diffusion model safe control uncertainty quantile 2025 ICML"

Links: [{"title":"ICML Poster From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control","url":"https://icml.cc/virtual/2025/poster/44969"},{"title":"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control | OpenReview","url":"https://openreview.net/forum?id=XGJ33p4qwt&noteId=q2qh0U2HX9"},{"title":"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control","url":"https://arxiv.org/html/2502.02205"},{"title":"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control","url":"https://proceedings.mlr.press/v267/hu25t.html"},{"title":"From Uncertain to Safe: Conformal Adaptation of Diffusion Models","url":"https://arxiv.org/pdf/2502.02205"},{"title":"SafeDiffuser: Safe Planning with Diffusion Probabilistic Models | OpenReview","url":"https://openreview.net/forum?id=ig2wk7kK9J"},{"title":"Conformal predictions and risk control in machine learning ...","url":"https://theses.hal.science/tel-05448293v1/file/157888_BLOT_2025_archivage-3.pdf"},{"title":"ICML Poster Optimal transport-based conformal prediction","url":"https://icml.cc/virtual/2025/poster/44266"},{"title":"Conformal Prediction for Uncertainty-Aware Planning with ...","url":"https://openreview.net/pdf?id=VeO03T59Sh"},{"title":"ICML Poster Model Uncertainty Quantification by Conformal Prediction in Continual Learning","url":"https://icml.cc/virtual/2025/poster/45394"}]

I found relevant information about SafeDiffCon. Here's what I discovered:

## SafeDiffCon: Conformal Adaptation of Diffusion Models for Safe PDE Control

SafeDiffCon (Safe Diffusion Models for PDE Control) introduces the uncertainty quantile as model uncertainty quantification to achieve optimal control under safety constraints through both post-training and inference phases.

### Key Approach

The method operates in two main phases:

1. **Post-training**: The approach post-trains a pre-trained diffusion model to generate control sequences that better satisfy safety constraints while achieving improved control objectives via a reweighted diffusion loss, which incorporates the uncertainty quantile estimated using conformal prediction.

2. **Inference**: During inference, the diffusion model dynamically adjusts both its generation process and parameters through iterative guidance and fine-tuning, conditioned on control targets while simultaneously integrating the estimated uncertainty quantile.

### Performance

In tests on fluid and fusion control tasks, SafeDiffCon is the only method that always stays safe while also achieving the best control performance.

### Publication Details

This paper was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), and the code is available at https://github.com/AI4Science-WestlakeU/safediffcon.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "e1663278-3135-41a8-a827-dc873706e03e",
  "tool_use_result": {
    "query": "SafeDiffCon conformal prediction diffusion model safe control uncertainty quantile 2025 ICML",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xv9NPx1fzdxriURntK9ntv",
        "content": [
          {
            "title": "ICML Poster From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control",
            "url": "https://icml.cc/virtual/2025/poster/44969"
          },
          {
            "title": "From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control | OpenReview",
            "url": "https://openreview.net/forum?id=XGJ33p4qwt&noteId=q2qh0U2HX9"
          },
          {
            "title": "From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control",
            "url": "https://arxiv.org/html/2502.02205"
          },
          {
            "title": "From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control",
            "url": "https://proceedings.mlr.press/v267/hu25t.html"
          },
          {
            "title": "From Uncertain to Safe: Conformal Adaptation of Diffusion Models",
            "url": "https://arxiv.org/pdf/2502.02205"
          },
          {
            "title": "SafeDiffuser: Safe Planning with Diffusion Probabilistic Models | OpenReview",
            "url": "https://openreview.net/forum?id=ig2wk7kK9J"
          },
          {
            "title": "Conformal predictions and risk control in machine learning ...",
            "url": "https://theses.hal.science/tel-05448293v1/file/157888_BLOT_2025_archivage-3.pdf"
          },
          {
            "title": "ICML Poster Optimal transport-based conformal prediction",
            "url": "https://icml.cc/virtual/2025/poster/44266"
          },
          {
            "title": "Conformal Prediction for Uncertainty-Aware Planning with ...",
            "url": "https://openreview.net/pdf?id=VeO03T59Sh"
          },
          {
            "title": "ICML Poster Model Uncertainty Quantification by Conformal Prediction in Continual Learning",
            "url": "https://icml.cc/virtual/2025/poster/45394"
          }
        ]
      },
      "I found relevant information about SafeDiffCon. Here's what I discovered:\n\n## SafeDiffCon: Conformal Adaptation of Diffusion Models for Safe PDE Control\n\nSafeDiffCon (Safe Diffusion Models for PDE Control) introduces the uncertainty quantile as model uncertainty quantification to achieve optimal control under safety constraints through both post-training and inference phases.\n\n### Key Approach\n\nThe method operates in two main phases:\n\n1. **Post-training**: The approach post-trains a pre-trained diffusion model to generate control sequences that better satisfy safety constraints while achieving improved control objectives via a reweighted diffusion loss, which incorporates the uncertainty quantile estimated using conformal prediction.\n\n2. **Inference**: During inference, the diffusion model dynamically adjusts both its generation process and parameters through iterative guidance and fine-tuning, conditioned on control targets while simultaneously integrating the estimated uncertainty quantile.\n\n### Performance\n\nIn tests on fluid and fusion control tasks, SafeDiffCon is the only method that always stays safe while also achieving the best control performance.\n\n### Publication Details\n\nThis paper was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), and the code is available at https://github.com/AI4Science-WestlakeU/safediffcon."
    ],
    "durationSeconds": 6.064539520999999
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to compose a comprehensive analysis. Let me put together the analysis document. The key new papers I've found that add to what's already in the literature_map:

1. **TACO (arXiv:2512.02834)** - Test-time scaling for VLA via anti-exploration with pseudo-count. Samples multiple action chunks and selects the one with highest pseudo-count. Very related to our argmin approach but with a different selection criterion.

2. **SafeDiffCon (ICML 2025)** - Uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. The key insight is using CP uncertainty quantile as both a training signal and inference-time guidance. 

This is conceptually very similar to our "conformal interval as magnitude bound" idea. I'm also seeing several other papers that leverage conformal prediction for safety: one from ICRA 2025 combining adaptive conformal prediction with control barrier functions, another from ICASSP 2026 that uses conformal prediction to calibrate safety monitoring with a shield mechanism, and an arXiv paper on adaptive scaling of policy constraints for offline RL.

Now I'm going to write up the full analysis and save it to memory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "8bbd2870-678b-4db9-a934-98e26d0b5647",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XduA4HSuV5XNH9ahmZDEoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 50617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1033
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

_source line 36_

已收集足够信息。现在编写分析文档并追加到 memory.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aff73dec-894b-4f5a-8350-e009bf93696b",
  "uuid": "f8eedc43-907c-412c-ae1c-9dc88c09fc51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XduA4HSuV5XNH9ahmZDEoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 50617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1033
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
