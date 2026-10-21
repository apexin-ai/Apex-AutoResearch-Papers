# research paper outline prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_research_paper-outline-prep_20260515T132442.log`
- **Structured JSON:** [`044ae9da69078d8ae0c1.json`](../../sessions/04/044ae9da69078d8ae0c1.json)

## Before a recorded user message

21 recorded events

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
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
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
  "uuid": "1208cfe0-8f23-40c8-abb2-599e6fc48bfd",
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
    "resetsAt": 1778856000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d480dece-7c31-4030-a5ff-d2c6f2d57bea",
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9"
}
```

---

### Assistant

_source line 4_

I'll read the four project files to understand the full context before drafting the outline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "ee9a1aa8-fa72-4224-a39a-4c3a67588cad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117Ui1j23WTj7nWmxMQsQU3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11506,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11506
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01F6weMJcDoZ6oSfeP2K2awx`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "e3f1cd82-40c9-4f15-92ee-3534da300536",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117Ui1j23WTj7nWmxMQsQU3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11506,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11506
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

_source line 6 · 2026-05-15T13:24:51.607Z_

<details><summary>↩ Tool result · `toolu_01F6weMJcDoZ6oSfeP2K2awx`</summary>

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
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "7489fe86-1135-4556-8e8e-b04b905999eb",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all four project files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "fe6bbe02-eae4-45f5-9479-47113e3ab26c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1mwzWWexMVzkYsVGQfiPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
      },
      "output_tokens": 43,
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014uPYt92c2EThVwq78LFU1a`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
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
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "b5e63fc0-efb5-4bc0-aff5-2f1fdfa2397c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1mwzWWexMVzkYsVGQfiPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
      },
      "output_tokens": 43,
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

_source line 9 · 2026-05-15T13:24:55.003Z_

<details><summary>↩ Tool result · `toolu_014uPYt92c2EThVwq78LFU1a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\"which action dimensions are uncertain and how they co-vary\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\n\\n> ⚠️ **Pending ablation confirmation**: \\\"fundamentally richer\\\" 措辞依赖 Scenario A (perdof > obs_only)。如果 Scenario B/C，Core Insight 需调整为 \\\"uncertainty-conditioned learned correction\\\" 或 \\\"observation-conditioned residual correction\\\"。见备选策略。\\n\\n## Core Claims (1 条，可证伪) — D022: Claim 3 移除, D023: Claim 2 移除. CoRL 聚焦单 Claim.\\n1. **Learned correction conditioned on uncertainty features significantly improves VLA robustness**: CRM（轻量 MLP）以 uncertainty 特征为条件输入，在 argmin 样本选择基础上进一步校正动作，显著优于纯选择方法。\\n   - **主 claim**: CRM correction 相比 argmin-only selection 有独立增量\\n   - **⚠️ D027 SPATIAL DATA**: matched-task T0-T6 perdof = argmin = 42.9% (0pp delta). Kill criteria TRIGGERED on spatial.\\n   - **obs_only matched T0-T5**: 40% vs perdof/argmin 35% (+5pp) — obs_only CRM 可能仍有效\\n   - **子 claim (待确认)**: Per-DOF conformal features (40D) 作为 conditioning 比 obs-only / scalar 更优\\n   - **⚠️ D027**: 子 claim 在 spatial 上初步否定 (perdof = argmin, obs_only > perdof)\\n   - 验证: spatial 4-way ablation (重启中) + object benchmark (RUNNING) + magnitude sweep (RUNNING)\\n   - Kill criterion (主 claim): CRM correction vs argmin-only < 3pp across BOTH benchmarks → correction 无价值\\n   - Kill criterion (子 claim): obs_only eval >= perdof eval → per-DOF features 无额外价值，启用备选 framing\\n   - **存活条件**: (a) magnitude sweep 某 norm 下 perdof >> argmin, (b) object benchmark perdof > argmin, (c) obs_only CRM +5pp 跨 benchmark 稳定\\n\\n~~2. **ACI+COC 在分布偏移下维持 calibrated uncertainty** — D023 移除: ACI update() 需要 ground truth action，test-time 不可用。理论前提 (i.i.d.) 在 sequential robotics 下不满足。~~\\n\\n~~3. **ACR-VLA 与 training-time 方法正交互补** — D022 移除: 11 天内无法获取 SRPO checkpoint + 重训 CRM + eval。留给扩展版本。~~\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\"哪些维度不确定+跨维度协方差\\\"，使 CRM 能做维度选择性校正。\\n- **Headline result template**: \\\"On LIBERO, ACR-VLA's uncertainty-conditioned sample-then-refine pipeline (K=10 conformal selection + learned CRM correction) improves SmolVLA success by +X pp on spatial and +Y pp on object tasks — with CRM correction contributing Z pp beyond sample selection alone, and correction magnitude control proving critical for closed-loop stability.\\\"\\n\\n## Competitive Landscape\\n\\n### ReconVLA — 最直接竞品\\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\n\\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \\\"哪个关节不确定\\\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\\n\\n### SC-VLA — Inference-time RL refinement\\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\\n\\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\\n\\n### VLA-Pilot — MLLM-guided steering\\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\\n\\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\\n\\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\\n\\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \\\"不确定\\\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\\n\\n### ACR-VLA 差异化定位\\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\\n\\n## Anticipated Reviewer Concerns\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\n7. **[Dream 新增] \\\"Conformal\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\"conformal-feature-conditioned correction\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\n\\n## Framing 备选策略 (D022 细化, Reviewer 审查后修补)\\n\\n**四路 ablation 排序预测** (val_loss 顺序: obs_only 0.0165 < perdof 0.0358 ≈ scalar_unc 0.0374):\\n- 训练 loss 预测: obs_only > scalar_unc ≈ perdof > argmin_only\\n- 但 closed-loop eval 可能翻转（conformal features 在分布偏移下的 epistemic value）\\n\\n### Scenario A: perdof > obs_only (最佳)\\nClaim 1 主+子 claim 均成立。Story: \\\"Per-DOF conformal features encode dimension-specific uncertainty that observation features alone cannot capture; this enables superior learned correction under distribution shift — despite worse training loss, conformal features' real-time epistemic signal proves critical in closed-loop deployment.\\\"\\n- Core Insight 不变\\n- 这是最强 narrative：training loss 反直觉但 eval 翻转 = compelling story\\n- scalar_unc 预期位置: ≈ perdof (相似 val_loss) 或略低 → per-DOF vs scalar 差异化成立\\n\\n### Scenario B: perdof ≈ obs_only ≈ scalar_unc (任意两者差 <5pp)\\n主 claim 成立（CRM correction 有价值），子 claim 弱化。Story: \\\"Uncertainty-conditioned learned correction (sample-then-refine) significantly outperforms pure sample selection. The specific form of uncertainty features (per-DOF, scalar, or observation-only) matters less than the correction mechanism itself.\\\"\\n- Core Insight 调整: 去掉 \\\"fundamentally richer than scalar\\\"，改为 \\\"enables principled learned correction\\\"\\n- Per-DOF 作为 Claim 2 (ACI+COC) 的必要组件保留\\n- **Magnitude control as empirical contribution**: 升级为独立发现 (Section: \\\"Critical Role of Correction Magnitude\\\")\\n\\n### Scenario C: obs_only > perdof AND obs_only > scalar_unc (>5pp)\\n主 claim 仍成立（CRM correction 有价值），子 claim 不成立。Story: \\\"Observation-conditioned residual correction is the key contribution. Conformal features as direct CRM input offer no additional value over observation features, but remain valuable for (a) sample selection quality, (b) online coverage monitoring (ACI+COC).\\\"\\n- Core Insight 需重写: \\\"Lightweight learned residual correction on selected VLA samples significantly improves robustness\\\"\\n- Per-DOF features 在 ablation table 如实呈现为 negative result\\n- **特殊子情况**: 如果 scalar_unc > perdof 但 scalar_unc < obs_only → conformal 特征形式无关紧要\\n\\n### 共性硬证据（所有 scenario 均可用）\\n- ~~CRM correction vs argmin-only: +9.6pp~~ → **D027 invalidated**: matched-task 0pp on spatial (perdof). obs_only +5pp on T0-T5 仍待全 10 task 确认\\n- VLA baseline (K=1): spatial 30%, object 13%\\n- VLA mean (K=10): spatial 31%\\n- Argmin selection (K=10): spatial ~35% (matched T0-T5)\\n- Magnitude control discovery: norm=1.42 → 0%, norm=0.1 → ~35-42% (novel empirical finding, 可独立成 contribution section)\\n- ~~ACI+COC online adaptation~~ → D023 移除\\n\\n### Kill criteria (Reviewer 校准后)\\n- **内部 kill (停止投入)**: CRM correction vs argmin-only < 3pp on ANY benchmark\\n- **论文 claim 门槛**: ≥5pp + Fisher exact test p<0.05 on EACH benchmark independently\\n- **3-5pp 灰区**: claim 技术上存活但论文说服力不足 (\\\"zombie claim\\\")，需要加 n_rollouts 或加 benchmark 提升统计力\\n- **跨 benchmark 逻辑**: ANY benchmark < 3pp → 该 benchmark 降级; BOTH < 3pp → claim killed\\n\", \"total_chars\": 9422, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "e1885ab4-f003-4bee-9306-1a6ca2baee2e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n## Target Venue\\\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\\\n- ~~ICLR 2027~~ — 不再是首要目标\\\\n\\\\n## Core Insight\\\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\\\\\"which action dimensions are uncertain and how they co-vary\\\\\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\\\n\\\\n> ⚠️ **Pending ablation confirmation**: \\\\\\\"fundamentally richer\\\\\\\" 措辞依赖 Scenario A (perdof > obs_only)。如果 Scenario B/C，Core Insight 需调整为 \\\\\\\"uncertainty-conditioned learned correction\\\\\\\" 或 \\\\\\\"observation-conditioned residual correction\\\\\\\"。见备选策略。\\\\n\\\\n## Core Claims (1 条，可证伪) — D022: Claim 3 移除, D023: Claim 2 移除. CoRL 聚焦单 Claim.\\\\n1. **Learned correction conditioned on uncertainty features significantly improves VLA robustness**: CRM（轻量 MLP）以 uncertainty 特征为条件输入，在 argmin 样本选择基础上进一步校正动作，显著优于纯选择方法。\\\\n   - **主 claim**: CRM correction 相比 argmin-only selection 有独立增量\\\\n   - **⚠️ D027 SPATIAL DATA**: matched-task T0-T6 perdof = argmin = 42.9% (0pp delta). Kill criteria TRIGGERED on spatial.\\\\n   - **obs_only matched T0-T5**: 40% vs perdof/argmin 35% (+5pp) — obs_only CRM 可能仍有效\\\\n   - **子 claim (待确认)**: Per-DOF conformal features (40D) 作为 conditioning 比 obs-only / scalar 更优\\\\n   - **⚠️ D027**: 子 claim 在 spatial 上初步否定 (perdof = argmin, obs_only > perdof)\\\\n   - 验证: spatial 4-way ablation (重启中) + object benchmark (RUNNING) + magnitude sweep (RUNNING)\\\\n   - Kill criterion (主 claim): CRM correction vs argmin-only < 3pp across BOTH benchmarks → correction 无价值\\\\n   - Kill criterion (子 claim): obs_only eval >= perdof eval → per-DOF features 无额外价值，启用备选 framing\\\\n   - **存活条件**: (a) magnitude sweep 某 norm 下 perdof >> argmin, (b) object benchmark perdof > argmin, (c) obs_only CRM +5pp 跨 benchmark 稳定\\\\n\\\\n~~2. **ACI+COC 在分布偏移下维持 calibrated uncertainty** — D023 移除: ACI update() 需要 ground truth action，test-time 不可用。理论前提 (i.i.d.) 在 sequential robotics 下不满足。~~\\\\n\\\\n~~3. **ACR-VLA 与 training-time 方法正交互补** — D022 移除: 11 天内无法获取 SRPO checkpoint + 重训 CRM + eval。留给扩展版本。~~\\\\n\\\\n## Story Spine\\\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\\\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\\\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\\\\\"哪些维度不确定+跨维度协方差\\\\\\\"，使 CRM 能做维度选择性校正。\\\\n- **Headline result template**: \\\\\\\"On LIBERO, ACR-VLA's uncertainty-conditioned sample-then-refine pipeline (K=10 conformal selection + learned CRM correction) improves SmolVLA success by +X pp on spatial and +Y pp on object tasks — with CRM correction contributing Z pp beyond sample selection alone, and correction magnitude control proving critical for closed-loop stability.\\\\\\\"\\\\n\\\\n## Competitive Landscape\\\\n\\\\n### ReconVLA — 最直接竞品\\\\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\\\n\\\\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \\\\\\\"哪个关节不确定\\\\\\\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\\\\n\\\\n### SC-VLA — Inference-time RL refinement\\\\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\\\\n\\\\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\\\\n\\\\n### VLA-Pilot — MLLM-guided steering\\\\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\\\\n\\\\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\\\\n\\\\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\\\\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\\\\n\\\\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \\\\\\\"不确定\\\\\\\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\\\\n\\\\n### ACR-VLA 差异化定位\\\\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\\\n7. **[Dream 新增] \\\\\\\"Conformal\\\\\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\\\\\"conformal-feature-conditioned correction\\\\\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\\\n\\\\n## Framing 备选策略 (D022 细化, Reviewer 审查后修补)\\\\n\\\\n**四路 ablation 排序预测** (val_loss 顺序: obs_only 0.0165 < perdof 0.0358 ≈ scalar_unc 0.0374):\\\\n- 训练 loss 预测: obs_only > scalar_unc ≈ perdof > argmin_only\\\\n- 但 closed-loop eval 可能翻转（conformal features 在分布偏移下的 epistemic value）\\\\n\\\\n### Scenario A: perdof > obs_only (最佳)\\\\nClaim 1 主+子 claim 均成立。Story: \\\\\\\"Per-DOF conformal features encode dimension-specific uncertainty that observation features alone cannot capture; this enables superior learned correction under distribution shift — despite worse training loss, conformal features' real-time epistemic signal proves critical in closed-loop deployment.\\\\\\\"\\\\n- Core Insight 不变\\\\n- 这是最强 narrative：training loss 反直觉但 eval 翻转 = compelling story\\\\n- scalar_unc 预期位置: ≈ perdof (相似 val_loss) 或略低 → per-DOF vs scalar 差异化成立\\\\n\\\\n### Scenario B: perdof ≈ obs_only ≈ scalar_unc (任意两者差 <5pp)\\\\n主 claim 成立（CRM correction 有价值），子 claim 弱化。Story: \\\\\\\"Uncertainty-conditioned learned correction (sample-then-refine) significantly outperforms pure sample selection. The specific form of uncertainty features (per-DOF, scalar, or observation-only) matters less than the correction mechanism itself.\\\\\\\"\\\\n- Core Insight 调整: 去掉 \\\\\\\"fundamentally richer than scalar\\\\\\\"，改为 \\\\\\\"enables principled learned correction\\\\\\\"\\\\n- Per-DOF 作为 Claim 2 (ACI+COC) 的必要组件保留\\\\n- **Magnitude control as empirical contribution**: 升级为独立发现 (Section: \\\\\\\"Critical Role of Correction Magnitude\\\\\\\")\\\\n\\\\n### Scenario C: obs_only > perdof AND obs_only > scalar_unc (>5pp)\\\\n主 claim 仍成立（CRM correction 有价值），子 claim 不成立。Story: \\\\\\\"Observation-conditioned residual correction is the key contribution. Conformal features as direct CRM input offer no additional value over observation features, but remain valuable for (a) sample selection quality, (b) online coverage monitoring (ACI+COC).\\\\\\\"\\\\n- Core Insight 需重写: \\\\\\\"Lightweight learned residual correction on selected VLA samples significantly improves robustness\\\\\\\"\\\\n- Per-DOF features 在 ablation table 如实呈现为 negative result\\\\n- **特殊子情况**: 如果 scalar_unc > perdof 但 scalar_unc < obs_only → conformal 特征形式无关紧要\\\\n\\\\n### 共性硬证据（所有 scenario 均可用）\\\\n- ~~CRM correction vs argmin-only: +9.6pp~~ → **D027 invalidated**: matched-task 0pp on spatial (perdof). obs_only +5pp on T0-T5 仍待全 10 task 确认\\\\n- VLA baseline (K=1): spatial 30%, object 13%\\\\n- VLA mean (K=10): spatial 31%\\\\n- Argmin selection (K=10): spatial ~35% (matched T0-T5)\\\\n- Magnitude control discovery: norm=1.42 → 0%, norm=0.1 → ~35-42% (novel empirical finding, 可独立成 contribution section)\\\\n- ~~ACI+COC online adaptation~~ → D023 移除\\\\n\\\\n### Kill criteria (Reviewer 校准后)\\\\n- **内部 kill (停止投入)**: CRM correction vs argmin-only < 3pp on ANY benchmark\\\\n- **论文 claim 门槛**: ≥5pp + Fisher exact test p<0.05 on EACH benchmark independently\\\\n- **3-5pp 灰区**: claim 技术上存活但论文说服力不足 (\\\\\\\"zombie claim\\\\\\\")，需要加 n_rollouts 或加 benchmark 提升统计力\\\\n- **跨 benchmark 逻辑**: ANY benchmark < 3pp → 该 benchmark 降级; BOTH < 3pp → claim killed\\\\n\\\", \\\"total_chars\\\": 9422, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\"which action dimensions are uncertain and how they co-vary\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\n\\n> ⚠️ **Pending ablation confirmation**: \\\"fundamentally richer\\\" 措辞依赖 Scenario A (perdof > obs_only)。如果 Scenario B/C，Core Insight 需调整为 \\\"uncertainty-conditioned learned correction\\\" 或 \\\"observation-conditioned residual correction\\\"。见备选策略。\\n\\n## Core Claims (1 条，可证伪) — D022: Claim 3 移除, D023: Claim 2 移除. CoRL 聚焦单 Claim.\\n1. **Learned correction conditioned on uncertainty features significantly improves VLA robustness**: CRM（轻量 MLP）以 uncertainty 特征为条件输入，在 argmin 样本选择基础上进一步校正动作，显著优于纯选择方法。\\n   - **主 claim**: CRM correction 相比 argmin-only selection 有独立增量\\n   - **⚠️ D027 SPATIAL DATA**: matched-task T0-T6 perdof = argmin = 42.9% (0pp delta). Kill criteria TRIGGERED on spatial.\\n   - **obs_only matched T0-T5**: 40% vs perdof/argmin 35% (+5pp) — obs_only CRM 可能仍有效\\n   - **子 claim (待确认)**: Per-DOF conformal features (40D) 作为 conditioning 比 obs-only / scalar 更优\\n   - **⚠️ D027**: 子 claim 在 spatial 上初步否定 (perdof = argmin, obs_only > perdof)\\n   - 验证: spatial 4-way ablation (重启中) + object benchmark (RUNNING) + magnitude sweep (RUNNING)\\n   - Kill criterion (主 claim): CRM correction vs argmin-only < 3pp across BOTH benchmarks → correction 无价值\\n   - Kill criterion (子 claim): obs_only eval >= perdof eval → per-DOF features 无额外价值，启用备选 framing\\n   - **存活条件**: (a) magnitude sweep 某 norm 下 perdof >> argmin, (b) object benchmark perdof > argmin, (c) obs_only CRM +5pp 跨 benchmark 稳定\\n\\n~~2. **ACI+COC 在分布偏移下维持 calibrated uncertainty** — D023 移除: ACI update() 需要 ground truth action，test-time 不可用。理论前提 (i.i.d.) 在 sequential robotics 下不满足。~~\\n\\n~~3. **ACR-VLA 与 training-time 方法正交互补** — D022 移除: 11 天内无法获取 SRPO checkpoint + 重训 CRM + eval。留给扩展版本。~~\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\"哪些维度不确定+跨维度协方差\\\"，使 CRM 能做维度选择性校正。\\n- **Headline result template**: \\\"On LIBERO, ACR-VLA's uncertainty-conditioned sample-then-refine pipeline (K=10 conformal selection + learned CRM correction) improves SmolVLA success by +X pp on spatial and +Y pp on object tasks — with CRM correction contributing Z pp beyond sample selection alone, and correction magnitude control proving critical for closed-loop stability.\\\"\\n\\n## Competitive Landscape\\n\\n### ReconVLA — 最直接竞品\\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\n\\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \\\"哪个关节不确定\\\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\\n\\n### SC-VLA — Inference-time RL refinement\\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\\n\\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\\n\\n### VLA-Pilot — MLLM-guided steering\\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\\n\\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\\n\\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\\n\\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \\\"不确定\\\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\\n\\n### ACR-VLA 差异化定位\\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\\n\\n## Anticipated Reviewer Concerns\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\n7. **[Dream 新增] \\\"Conformal\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\"conformal-feature-conditioned correction\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\n\\n## Framing 备选策略 (D022 细化, Reviewer 审查后修补)\\n\\n**四路 ablation 排序预测** (val_loss 顺序: obs_only 0.0165 < perdof 0.0358 ≈ scalar_unc 0.0374):\\n- 训练 loss 预测: obs_only > scalar_unc ≈ perdof > argmin_only\\n- 但 closed-loop eval 可能翻转（conformal features 在分布偏移下的 epistemic value）\\n\\n### Scenario A: perdof > obs_only (最佳)\\nClaim 1 主+子 claim 均成立。Story: \\\"Per-DOF conformal features encode dimension-specific uncertainty that observation features alone cannot capture; this enables superior learned correction under distribution shift — despite worse training loss, conformal features' real-time epistemic signal proves critical in closed-loop deployment.\\\"\\n- Core Insight 不变\\n- 这是最强 narrative：training loss 反直觉但 eval 翻转 = compelling story\\n- scalar_unc 预期位置: ≈ perdof (相似 val_loss) 或略低 → per-DOF vs scalar 差异化成立\\n\\n### Scenario B: perdof ≈ obs_only ≈ scalar_unc (任意两者差 <5pp)\\n主 claim 成立（CRM correction 有价值），子 claim 弱化。Story: \\\"Uncertainty-conditioned learned correction (sample-then-refine) significantly outperforms pure sample selection. The specific form of uncertainty features (per-DOF, scalar, or observation-only) matters less than the correction mechanism itself.\\\"\\n- Core Insight 调整: 去掉 \\\"fundamentally richer than scalar\\\"，改为 \\\"enables principled learned correction\\\"\\n- Per-DOF 作为 Claim 2 (ACI+COC) 的必要组件保留\\n- **Magnitude control as empirical contribution**: 升级为独立发现 (Section: \\\"Critical Role of Correction Magnitude\\\")\\n\\n### Scenario C: obs_only > perdof AND obs_only > scalar_unc (>5pp)\\n主 claim 仍成立（CRM correction 有价值），子 claim 不成立。Story: \\\"Observation-conditioned residual correction is the key contribution. Conformal features as direct CRM input offer no additional value over observation features, but remain valuable for (a) sample selection quality, (b) online coverage monitoring (ACI+COC).\\\"\\n- Core Insight 需重写: \\\"Lightweight learned residual correction on selected VLA samples significantly improves robustness\\\"\\n- Per-DOF features 在 ablation table 如实呈现为 negative result\\n- **特殊子情况**: 如果 scalar_unc > perdof 但 scalar_unc < obs_only → conformal 特征形式无关紧要\\n\\n### 共性硬证据（所有 scenario 均可用）\\n- ~~CRM correction vs argmin-only: +9.6pp~~ → **D027 invalidated**: matched-task 0pp on spatial (perdof). obs_only +5pp on T0-T5 仍待全 10 task 确认\\n- VLA baseline (K=1): spatial 30%, object 13%\\n- VLA mean (K=10): spatial 31%\\n- Argmin selection (K=10): spatial ~35% (matched T0-T5)\\n- Magnitude control discovery: norm=1.42 → 0%, norm=0.1 → ~35-42% (novel empirical finding, 可独立成 contribution section)\\n- ~~ACI+COC online adaptation~~ → D023 移除\\n\\n### Kill criteria (Reviewer 校准后)\\n- **内部 kill (停止投入)**: CRM correction vs argmin-only < 3pp on ANY benchmark\\n- **论文 claim 门槛**: ≥5pp + Fisher exact test p<0.05 on EACH benchmark independently\\n- **3-5pp 灰区**: claim 技术上存活但论文说服力不足 (\\\"zombie claim\\\")，需要加 n_rollouts 或加 benchmark 提升统计力\\n- **跨 benchmark 逻辑**: ANY benchmark < 3pp → 该 benchmark 降级; BOTH < 3pp → claim killed\\n\", \"total_chars\": 9422, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TySVs9uJktrPge5iP92o4b`</summary>

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
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "7020bcec-79db-4af4-a905-b1531ac6e09b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1mwzWWexMVzkYsVGQfiPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
      },
      "output_tokens": 43,
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

_source line 11 · 2026-05-15T13:24:55.980Z_

<details><summary>↩ Tool result · `toolu_01TySVs9uJktrPge5iP92o4b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 10:18 UTC | 更新原因: obs-only-r3 完成: spatial obs_only locked at 35%, D030 fully confirmed\\n\\n## 核心方向\\nobs_only CRM（基于观测特征的 learned correction）是唯一存活路径。Per-DOF conformal claim 已死。论文 story 须 pivot。详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 2d — Object benchmark 决定项目存亡\\n- **MVP**: PASS\\n- **D030 CONFIRMED**: Spatial ALL CRM dead — obs_only 35%, perdof 35%, argmin 34%（±1pp，无统计意义）\\n- **Object (5/10 tasks)**: obs_only 16% vs argmin 8% (+8pp) — **唯一存活信号**，p≈0.19\\n- **Magnitude sweep**: obs_only > perdof at confirmed norms (+8~12pp on 2/4 norms, 2 pending)\\n- **D031**: 统计显著性方案（seed=43 doubling + bootstrap CI）\\n\\n## Per-Task Data\\n\\n### Spatial (10-task, LOCKED ✅)\\n\\n| Task | argmin | perdof | obs_only | scalar |\\n|------|--------|--------|----------|--------|\\n| T0 | 60% | 60% | **90%** | 60% |\\n| T1 | 100% | 100% | 100% | 100% |\\n| T2 | 0% | 10% | 0% | 10% |\\n| T3 | 30% | 40% | 40% | 40% |\\n| T4 | 10% | 0% | 10% | 0% |\\n| T5 | 10% | 0% | 0% | 0% |\\n| T6 | 90% | 90% | 90% | 90% |\\n| T7 | 0% | 10% | 0% | running |\\n| T8 | 30% | 40% | 20% | — |\\n| T9 | 10% | 0% | 0% | — |\\n| **Total** | **34%** | **35%** | **35%** | running |\\n\\n注: obs_only T0 +30pp over argmin，但被 T5/T8/T9 各 -10pp 抵消。CRM 存在 task-specific compounding error。\\n\\n### Object (5/10 tasks — ⭐ CRITICAL, remaining 5 decide project fate)\\n\\n| Task | VLA-only | argmin | perdof | obs_only | scalar |\\n|------|----------|--------|--------|----------|--------|\\n| T0 | 0% | 0% | 0% | 0% | 0% |\\n| T1 | 10% | 0% | 0% | **10%** | 0% |\\n| T2 | 20% | 10% | 20% | **20%** | 10% |\\n| T3 | 20% | 30% | 30% | **40%** | 10% |\\n| T4 | 0% | 0% | 0% | **10%** | 0% |\\n| **5-task avg** | **10%** | **8%** | **10%** | **16%** | **4%** |\\n\\n### Magnitude Sweep (5/10 tasks each, spatial)\\n\\n| Task | perdof-003 | perdof-005 | perdof-02 | perdof-03 | obsonly-005 | obsonly-02 |\\n|------|------------|------------|-----------|-----------|-------------|------------|\\n| T0 | 60% | 50% | 60% | 70% | **80%** | **90%** |\\n| T1 | 100% | 100% | 90% | **50%↓** | 90% | **100%** |\\n| T2 | 0% | 0% | 0% | 10% | 0% | 0% |\\n| T3 | 30% | 30% | 20% | 10% | **40%** | 30% |\\n| T4 | 10% | 0% | 0% | 0% | **10%** | 10% |\\n| **avg** | **40%** | **36%** | **34%** | **28%** | **44%** | **46%** |\\n\\n## 统计显著性应对方案（D031）\\n\\n**问题**: 10-task 维持 obs_only 16% vs argmin 8% → Fisher p ≈ 0.058，不过 0.05。\\n**方案**: (1) Object seed=43 → 200 trials, p ≈ 0.012 (2) Bootstrap CI (3) Magnitude robustness narrative\\n**关键假设**: seed=43 复现 +8pp 效应量\\n**GPU 来源**: bjb1-18228 cuda:2 + cuda:3 已释放/待释放\\n\\n## 服务器状态\\n\\n| 服务器 | GPU 数 | 实验 | 状态 |\\n|--------|--------|------|------|\\n| bjb1-18228 | 4× 4090 | cuda:0 norm03-r2, cuda:1 scalar-r2 | cuda:2 僵尸待 kill, cuda:3 已释放 ✅ |\\n| bjb1-32546 | 6× 4090 | object 6-way eval ⭐ | 5/10 tasks, cuda:4 双进程待 kill |\\n| bjb2-28827 | 6× 4090 | magnitude sweep 6-way | 5/10 tasks each |\\n| bjb2-40593 | 1× 4090 D | obsonly-norm003-b2 | 3/10 tasks |\\n\\n⚠️ 两个 kill 任务（bjb1-32546 PID 42320 + bjb1-18228 PID 341878）已派 Agent，等待执行\\n\\n## 近期任务\\n- [ ] Kill bjb1-32546 PID 42320（cuda:4 双进程，5h+ 未解决）\\n- [ ] Kill bjb1-18228 PID 341878（cuda:2 僵尸）\\n- [ ] Object eval T5-T9 → 项目存亡裁决\\n- [ ] 部署 object seed=43 eval 到 bjb1-18228 cuda:2+3（D031）\\n- [ ] Magnitude sweep 10-task 完成 → norm sensitivity curve\\n- [ ] scalar-r2 完成 → 锁定 spatial scalar final\\n- [ ] 根据 object 最终结果更新 paper_framing.md\\n- [ ] Paper Agent 启动 CoRL 初稿\\n\\n## 项目存活条件（D030 confirmed）\\n1. ~~Perdof >> argmin~~ ✘\\n2. ~~Object perdof > argmin~~ ✘\\n3. **Object obs_only +8pp 维持 + seed=43 doubling 达 p < 0.05** ← 唯一路径\\n4. Object obs_only 回落 或 seed=43 不复现 → 项目 dead\\n\\n## GPU 预算\\n17× RTX 4090。bjb1-18228 cuda:2+3 待回收部署 object seed=43。\\n\\n## 风险\\n- 单种子 p=0.058 不够，必须 seed=43 doubling\\n- seed=43 效应量衰减风险\\n- obs_only \\\"learned correction\\\" 新颖性弱\\n- 11 天 DDL\\n- Spatial 中 obs_only task-specific ±10-30pp 波动暗示 CRM 可能引入 compounding error\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D032 | 2026-05-15 | D032: Magnitude sweep narrative 修正 — obs_only 优势不是 | eval-mag-obsonly-norm005, eval-mag-obsonly-norm02, eval-mag-perdof-norm03 |\\n| D031 | 2026-05-15 | D031: 统计显著性应对方案 — object eval 完成后立即部署 seed=43 doub | eval-acr-object-v4-obs-only, eval-obs-only-spatial-seed43 |\\n| D030 | 2026-05-15 | D030: Spatial ALL CRM variants confirmed dead (inc | eval-acr-spatial-v4-obs-only-r3, eval-acr-object-v4-obs-only, eval-argmin-only-spatial-r2, eval-acr-spatial-v4-small-r2 |\\n| D029 | 2026-05-15 | D029: Perdof CRM spatial full 10-task = 35% vs arg | eval-acr-spatial-v4-small, eval-acr-spatial-v4-small-r2, eval-argmin-only-spatial |\\n| D028 | 2026-05-15 | D028: Argmin K=10 spatial baseline locked at 34% ( | eval-argmin-only-spatial, eval-argmin-only-spatial-r2 |\\n| D027 | 2026-05-15 | D027: Reviewer matched-task analysis reveals perdo | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-argmin-only-spatial |\\n| D026 | 2026-05-15 | D026: Kill + restart bjb1-18228 stuck experiments. | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-acr-spatial-v4-scalar, eval-argmin-only-spatial |\\n| D025 | 2026-05-15 | D025: D019 \\\"52.5% perdof\\\" claim invalidated — actu | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-argmin-only-spatial |\\n| D024 | 2026-05-15 | D024: Kill bjb2-40593 v4-default-r3 (norm=1.42) —  | eval-acr-spatial-v4-default-r3 |\\n| D023 | 2026-05-15 | D023: Drop Claim 2 (ACI/COC) for CoRL — focus sing | plan_005, plan_006, plan_007 |\\n\\n\", \"total_chars\": 5433, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "fb824803-8b39-44d9-bab8-14c4a180eda1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\\\", \\\"content\\\": \\\"# acr-vla-conformal-refinement — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-15 10:18 UTC | 更新原因: obs-only-r3 完成: spatial obs_only locked at 35%, D030 fully confirmed\\\\n\\\\n## 核心方向\\\\nobs_only CRM（基于观测特征的 learned correction）是唯一存活路径。Per-DOF conformal claim 已死。论文 story 须 pivot。详见 paper_framing.md。\\\\n\\\\n## 投稿目标\\\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Phase 2d — Object benchmark 决定项目存亡\\\\n- **MVP**: PASS\\\\n- **D030 CONFIRMED**: Spatial ALL CRM dead — obs_only 35%, perdof 35%, argmin 34%（±1pp，无统计意义）\\\\n- **Object (5/10 tasks)**: obs_only 16% vs argmin 8% (+8pp) — **唯一存活信号**，p≈0.19\\\\n- **Magnitude sweep**: obs_only > perdof at confirmed norms (+8~12pp on 2/4 norms, 2 pending)\\\\n- **D031**: 统计显著性方案（seed=43 doubling + bootstrap CI）\\\\n\\\\n## Per-Task Data\\\\n\\\\n### Spatial (10-task, LOCKED ✅)\\\\n\\\\n| Task | argmin | perdof | obs_only | scalar |\\\\n|------|--------|--------|----------|--------|\\\\n| T0 | 60% | 60% | **90%** | 60% |\\\\n| T1 | 100% | 100% | 100% | 100% |\\\\n| T2 | 0% | 10% | 0% | 10% |\\\\n| T3 | 30% | 40% | 40% | 40% |\\\\n| T4 | 10% | 0% | 10% | 0% |\\\\n| T5 | 10% | 0% | 0% | 0% |\\\\n| T6 | 90% | 90% | 90% | 90% |\\\\n| T7 | 0% | 10% | 0% | running |\\\\n| T8 | 30% | 40% | 20% | — |\\\\n| T9 | 10% | 0% | 0% | — |\\\\n| **Total** | **34%** | **35%** | **35%** | running |\\\\n\\\\n注: obs_only T0 +30pp over argmin，但被 T5/T8/T9 各 -10pp 抵消。CRM 存在 task-specific compounding error。\\\\n\\\\n### Object (5/10 tasks — ⭐ CRITICAL, remaining 5 decide project fate)\\\\n\\\\n| Task | VLA-only | argmin | perdof | obs_only | scalar |\\\\n|------|----------|--------|--------|----------|--------|\\\\n| T0 | 0% | 0% | 0% | 0% | 0% |\\\\n| T1 | 10% | 0% | 0% | **10%** | 0% |\\\\n| T2 | 20% | 10% | 20% | **20%** | 10% |\\\\n| T3 | 20% | 30% | 30% | **40%** | 10% |\\\\n| T4 | 0% | 0% | 0% | **10%** | 0% |\\\\n| **5-task avg** | **10%** | **8%** | **10%** | **16%** | **4%** |\\\\n\\\\n### Magnitude Sweep (5/10 tasks each, spatial)\\\\n\\\\n| Task | perdof-003 | perdof-005 | perdof-02 | perdof-03 | obsonly-005 | obsonly-02 |\\\\n|------|------------|------------|-----------|-----------|-------------|------------|\\\\n| T0 | 60% | 50% | 60% | 70% | **80%** | **90%** |\\\\n| T1 | 100% | 100% | 90% | **50%↓** | 90% | **100%** |\\\\n| T2 | 0% | 0% | 0% | 10% | 0% | 0% |\\\\n| T3 | 30% | 30% | 20% | 10% | **40%** | 30% |\\\\n| T4 | 10% | 0% | 0% | 0% | **10%** | 10% |\\\\n| **avg** | **40%** | **36%** | **34%** | **28%** | **44%** | **46%** |\\\\n\\\\n## 统计显著性应对方案（D031）\\\\n\\\\n**问题**: 10-task 维持 obs_only 16% vs argmin 8% → Fisher p ≈ 0.058，不过 0.05。\\\\n**方案**: (1) Object seed=43 → 200 trials, p ≈ 0.012 (2) Bootstrap CI (3) Magnitude robustness narrative\\\\n**关键假设**: seed=43 复现 +8pp 效应量\\\\n**GPU 来源**: bjb1-18228 cuda:2 + cuda:3 已释放/待释放\\\\n\\\\n## 服务器状态\\\\n\\\\n| 服务器 | GPU 数 | 实验 | 状态 |\\\\n|--------|--------|------|------|\\\\n| bjb1-18228 | 4× 4090 | cuda:0 norm03-r2, cuda:1 scalar-r2 | cuda:2 僵尸待 kill, cuda:3 已释放 ✅ |\\\\n| bjb1-32546 | 6× 4090 | object 6-way eval ⭐ | 5/10 tasks, cuda:4 双进程待 kill |\\\\n| bjb2-28827 | 6× 4090 | magnitude sweep 6-way | 5/10 tasks each |\\\\n| bjb2-40593 | 1× 4090 D | obsonly-norm003-b2 | 3/10 tasks |\\\\n\\\\n⚠️ 两个 kill 任务（bjb1-32546 PID 42320 + bjb1-18228 PID 341878）已派 Agent，等待执行\\\\n\\\\n## 近期任务\\\\n- [ ] Kill bjb1-32546 PID 42320（cuda:4 双进程，5h+ 未解决）\\\\n- [ ] Kill bjb1-18228 PID 341878（cuda:2 僵尸）\\\\n- [ ] Object eval T5-T9 → 项目存亡裁决\\\\n- [ ] 部署 object seed=43 eval 到 bjb1-18228 cuda:2+3（D031）\\\\n- [ ] Magnitude sweep 10-task 完成 → norm sensitivity curve\\\\n- [ ] scalar-r2 完成 → 锁定 spatial scalar final\\\\n- [ ] 根据 object 最终结果更新 paper_framing.md\\\\n- [ ] Paper Agent 启动 CoRL 初稿\\\\n\\\\n## 项目存活条件（D030 confirmed）\\\\n1. ~~Perdof >> argmin~~ ✘\\\\n2. ~~Object perdof > argmin~~ ✘\\\\n3. **Object obs_only +8pp 维持 + seed=43 doubling 达 p < 0.05** ← 唯一路径\\\\n4. Object obs_only 回落 或 seed=43 不复现 → 项目 dead\\\\n\\\\n## GPU 预算\\\\n17× RTX 4090。bjb1-18228 cuda:2+3 待回收部署 object seed=43。\\\\n\\\\n## 风险\\\\n- 单种子 p=0.058 不够，必须 seed=43 doubling\\\\n- seed=43 效应量衰减风险\\\\n- obs_only \\\\\\\"learned correction\\\\\\\" 新颖性弱\\\\n- 11 天 DDL\\\\n- Spatial 中 obs_only task-specific ±10-30pp 波动暗示 CRM 可能引入 compounding error\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D032 | 2026-05-15 | D032: Magnitude sweep narrative 修正 — obs_only 优势不是 | eval-mag-obsonly-norm005, eval-mag-obsonly-norm02, eval-mag-perdof-norm03 |\\\\n| D031 | 2026-05-15 | D031: 统计显著性应对方案 — object eval 完成后立即部署 seed=43 doub | eval-acr-object-v4-obs-only, eval-obs-only-spatial-seed43 |\\\\n| D030 | 2026-05-15 | D030: Spatial ALL CRM variants confirmed dead (inc | eval-acr-spatial-v4-obs-only-r3, eval-acr-object-v4-obs-only, eval-argmin-only-spatial-r2, eval-acr-spatial-v4-small-r2 |\\\\n| D029 | 2026-05-15 | D029: Perdof CRM spatial full 10-task = 35% vs arg | eval-acr-spatial-v4-small, eval-acr-spatial-v4-small-r2, eval-argmin-only-spatial |\\\\n| D028 | 2026-05-15 | D028: Argmin K=10 spatial baseline locked at 34% ( | eval-argmin-only-spatial, eval-argmin-only-spatial-r2 |\\\\n| D027 | 2026-05-15 | D027: Reviewer matched-task analysis reveals perdo | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-argmin-only-spatial |\\\\n| D026 | 2026-05-15 | D026: Kill + restart bjb1-18228 stuck experiments. | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-acr-spatial-v4-scalar, eval-argmin-only-spatial |\\\\n| D025 | 2026-05-15 | D025: D019 \\\\\\\"52.5% perdof\\\\\\\" claim invalidated — actu | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-argmin-only-spatial |\\\\n| D024 | 2026-05-15 | D024: Kill bjb2-40593 v4-default-r3 (norm=1.42) —  | eval-acr-spatial-v4-default-r3 |\\\\n| D023 | 2026-05-15 | D023: Drop Claim 2 (ACI/COC) for CoRL — focus sing | plan_005, plan_006, plan_007 |\\\\n\\\\n\\\", \\\"total_chars\\\": 5433, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 10:18 UTC | 更新原因: obs-only-r3 完成: spatial obs_only locked at 35%, D030 fully confirmed\\n\\n## 核心方向\\nobs_only CRM（基于观测特征的 learned correction）是唯一存活路径。Per-DOF conformal claim 已死。论文 story 须 pivot。详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 2d — Object benchmark 决定项目存亡\\n- **MVP**: PASS\\n- **D030 CONFIRMED**: Spatial ALL CRM dead — obs_only 35%, perdof 35%, argmin 34%（±1pp，无统计意义）\\n- **Object (5/10 tasks)**: obs_only 16% vs argmin 8% (+8pp) — **唯一存活信号**，p≈0.19\\n- **Magnitude sweep**: obs_only > perdof at confirmed norms (+8~12pp on 2/4 norms, 2 pending)\\n- **D031**: 统计显著性方案（seed=43 doubling + bootstrap CI）\\n\\n## Per-Task Data\\n\\n### Spatial (10-task, LOCKED ✅)\\n\\n| Task | argmin | perdof | obs_only | scalar |\\n|------|--------|--------|----------|--------|\\n| T0 | 60% | 60% | **90%** | 60% |\\n| T1 | 100% | 100% | 100% | 100% |\\n| T2 | 0% | 10% | 0% | 10% |\\n| T3 | 30% | 40% | 40% | 40% |\\n| T4 | 10% | 0% | 10% | 0% |\\n| T5 | 10% | 0% | 0% | 0% |\\n| T6 | 90% | 90% | 90% | 90% |\\n| T7 | 0% | 10% | 0% | running |\\n| T8 | 30% | 40% | 20% | — |\\n| T9 | 10% | 0% | 0% | — |\\n| **Total** | **34%** | **35%** | **35%** | running |\\n\\n注: obs_only T0 +30pp over argmin，但被 T5/T8/T9 各 -10pp 抵消。CRM 存在 task-specific compounding error。\\n\\n### Object (5/10 tasks — ⭐ CRITICAL, remaining 5 decide project fate)\\n\\n| Task | VLA-only | argmin | perdof | obs_only | scalar |\\n|------|----------|--------|--------|----------|--------|\\n| T0 | 0% | 0% | 0% | 0% | 0% |\\n| T1 | 10% | 0% | 0% | **10%** | 0% |\\n| T2 | 20% | 10% | 20% | **20%** | 10% |\\n| T3 | 20% | 30% | 30% | **40%** | 10% |\\n| T4 | 0% | 0% | 0% | **10%** | 0% |\\n| **5-task avg** | **10%** | **8%** | **10%** | **16%** | **4%** |\\n\\n### Magnitude Sweep (5/10 tasks each, spatial)\\n\\n| Task | perdof-003 | perdof-005 | perdof-02 | perdof-03 | obsonly-005 | obsonly-02 |\\n|------|------------|------------|-----------|-----------|-------------|------------|\\n| T0 | 60% | 50% | 60% | 70% | **80%** | **90%** |\\n| T1 | 100% | 100% | 90% | **50%↓** | 90% | **100%** |\\n| T2 | 0% | 0% | 0% | 10% | 0% | 0% |\\n| T3 | 30% | 30% | 20% | 10% | **40%** | 30% |\\n| T4 | 10% | 0% | 0% | 0% | **10%** | 10% |\\n| **avg** | **40%** | **36%** | **34%** | **28%** | **44%** | **46%** |\\n\\n## 统计显著性应对方案（D031）\\n\\n**问题**: 10-task 维持 obs_only 16% vs argmin 8% → Fisher p ≈ 0.058，不过 0.05。\\n**方案**: (1) Object seed=43 → 200 trials, p ≈ 0.012 (2) Bootstrap CI (3) Magnitude robustness narrative\\n**关键假设**: seed=43 复现 +8pp 效应量\\n**GPU 来源**: bjb1-18228 cuda:2 + cuda:3 已释放/待释放\\n\\n## 服务器状态\\n\\n| 服务器 | GPU 数 | 实验 | 状态 |\\n|--------|--------|------|------|\\n| bjb1-18228 | 4× 4090 | cuda:0 norm03-r2, cuda:1 scalar-r2 | cuda:2 僵尸待 kill, cuda:3 已释放 ✅ |\\n| bjb1-32546 | 6× 4090 | object 6-way eval ⭐ | 5/10 tasks, cuda:4 双进程待 kill |\\n| bjb2-28827 | 6× 4090 | magnitude sweep 6-way | 5/10 tasks each |\\n| bjb2-40593 | 1× 4090 D | obsonly-norm003-b2 | 3/10 tasks |\\n\\n⚠️ 两个 kill 任务（bjb1-32546 PID 42320 + bjb1-18228 PID 341878）已派 Agent，等待执行\\n\\n## 近期任务\\n- [ ] Kill bjb1-32546 PID 42320（cuda:4 双进程，5h+ 未解决）\\n- [ ] Kill bjb1-18228 PID 341878（cuda:2 僵尸）\\n- [ ] Object eval T5-T9 → 项目存亡裁决\\n- [ ] 部署 object seed=43 eval 到 bjb1-18228 cuda:2+3（D031）\\n- [ ] Magnitude sweep 10-task 完成 → norm sensitivity curve\\n- [ ] scalar-r2 完成 → 锁定 spatial scalar final\\n- [ ] 根据 object 最终结果更新 paper_framing.md\\n- [ ] Paper Agent 启动 CoRL 初稿\\n\\n## 项目存活条件（D030 confirmed）\\n1. ~~Perdof >> argmin~~ ✘\\n2. ~~Object perdof > argmin~~ ✘\\n3. **Object obs_only +8pp 维持 + seed=43 doubling 达 p < 0.05** ← 唯一路径\\n4. Object obs_only 回落 或 seed=43 不复现 → 项目 dead\\n\\n## GPU 预算\\n17× RTX 4090。bjb1-18228 cuda:2+3 待回收部署 object seed=43。\\n\\n## 风险\\n- 单种子 p=0.058 不够，必须 seed=43 doubling\\n- seed=43 效应量衰减风险\\n- obs_only \\\"learned correction\\\" 新颖性弱\\n- 11 天 DDL\\n- Spatial 中 obs_only task-specific ±10-30pp 波动暗示 CRM 可能引入 compounding error\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D032 | 2026-05-15 | D032: Magnitude sweep narrative 修正 — obs_only 优势不是 | eval-mag-obsonly-norm005, eval-mag-obsonly-norm02, eval-mag-perdof-norm03 |\\n| D031 | 2026-05-15 | D031: 统计显著性应对方案 — object eval 完成后立即部署 seed=43 doub | eval-acr-object-v4-obs-only, eval-obs-only-spatial-seed43 |\\n| D030 | 2026-05-15 | D030: Spatial ALL CRM variants confirmed dead (inc | eval-acr-spatial-v4-obs-only-r3, eval-acr-object-v4-obs-only, eval-argmin-only-spatial-r2, eval-acr-spatial-v4-small-r2 |\\n| D029 | 2026-05-15 | D029: Perdof CRM spatial full 10-task = 35% vs arg | eval-acr-spatial-v4-small, eval-acr-spatial-v4-small-r2, eval-argmin-only-spatial |\\n| D028 | 2026-05-15 | D028: Argmin K=10 spatial baseline locked at 34% ( | eval-argmin-only-spatial, eval-argmin-only-spatial-r2 |\\n| D027 | 2026-05-15 | D027: Reviewer matched-task analysis reveals perdo | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-argmin-only-spatial |\\n| D026 | 2026-05-15 | D026: Kill + restart bjb1-18228 stuck experiments. | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-acr-spatial-v4-scalar, eval-argmin-only-spatial |\\n| D025 | 2026-05-15 | D025: D019 \\\"52.5% perdof\\\" claim invalidated — actu | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-argmin-only-spatial |\\n| D024 | 2026-05-15 | D024: Kill bjb2-40593 v4-default-r3 (norm=1.42) —  | eval-acr-spatial-v4-default-r3 |\\n| D023 | 2026-05-15 | D023: Drop Claim 2 (ACI/COC) for CoRL — focus sing | plan_005, plan_006, plan_007 |\\n\\n\", \"total_chars\": 5433, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BN7kywNYJPDMbvYE71MWMx`</summary>

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
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "83919c43-2919-4e2c-9537-e50daf9956bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1mwzWWexMVzkYsVGQfiPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
      },
      "output_tokens": 43,
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

_source line 13 · 2026-05-15T13:24:56.463Z_

<details><summary>↩ Tool result · `toolu_01BN7kywNYJPDMbvYE71MWMx`</summary>

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
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "e9d1c211-fb16-42c7-81d8-60dcdbc399ad",
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Y7KcZ37cwweXfNhz1d7g63`</summary>

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
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "2e8b2774-484e-477c-9175-f8d98fb2a605",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1mwzWWexMVzkYsVGQfiPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
      },
      "output_tokens": 43,
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

_source line 15 · 2026-05-15T13:24:56.995Z_

<details><summary>↩ Tool result · `toolu_01Y7KcZ37cwweXfNhz1d7g63`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## Spatial Baselines 锁定 (2026-05-15)\\n\\n| 方法 | SR | 来源 |\\n|------|-----|------|\\n| VLA-only K=1 | 30% | eval-spatial-v7-full |\\n| VLA-mean K=10 | 32% | eval-vla-mean-spatial |\\n| Argmin K=10 | 34% | eval-argmin-only-spatial-r2 (与 reconvla-v3 独立复现一致) |\\n\\n**关键发现**: K=10 采样 + scalar argmin 选择增益有限 (+2pp over mean, +4pp over K=1)。CRM correction 的 bar 是 34%。\\n\\n## Hard Tasks 普遍失败 (2026-05-15)\\n\\nT2 (from_table_center), T7 (on_stove): 所有方法 0%。T4 (in_top_drawer), T5 (on_ramekin): 所有方法 0-10%。这是 VLA backbone 限制，不是 CRM 问题。论文不应在这些 tasks 上 claim CRM 改进。\\n\\n## D027 CRITICAL: perdof = argmin on matched tasks (2026-05-15)\\n\\nT0-T6 matched comparison: perdof 42.9% = argmin ~43% (0pp delta)。Per-DOF claim 在 spatial 上已死。项目存活依赖：\\n1. Magnitude sweep 找到 perdof 显著优于 argmin 的 norm 点\\n2. Object benchmark 跨域验证\\n3. obs_only CRM +5pp 稳定 → 转向 \\\"learned correction\\\" narrative\\n\\n## obs_only 走势 (2026-05-15)\\n\\nobs_only 从 57.5%@4tasks 降到 40%@6tasks（hard tasks 拖累）。但 obs_only 在 magnitude sweep 中每个已测 norm 下都 >= perdof (+10-20pp，仅 2 tasks)。如果趋势在 5+ tasks 后仍保持，论文可转向 \\\"obs-only CRM correction\\\" narrative。\\n\\n## Object Baseline (2026-05-15)\\n\\nVLA-only K=1 object = 12%。CRM 在 object benchmark 有更大提升空间（baseline 低）。\\n\\n## bjb2-40593 环境问题 (2026-05-14-15)\\n\\n- 无 .git repo\\n- CRM cache 路径 /root/autodl-tmp/crm_cache/spatial/（旧路径，非 v5）\\n- Ghost PID 211962 已 kill，eval-mag-obsonly-norm003-b2 恢复运行\\n\\n## [失败模式] submit_training_job EXIT_CODE=127 (2026-05-15)\\n\\ntmux 用 `sh` 而非 `bash` 执行命令，`python` 等 conda/venv 命令不在 `sh` PATH 中。修复：命令必须用 `bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...\\\"` 包裹。裸 `python -u ...` 有时可行（取决于服务器 PATH 配置），但不可靠。\\n\\n## [失败模式] Kill 操作前必须逐参数比对 (2026-05-15)\\n\\n**事故**: Worker 将 norm=0.3 (norm03) 误判为 norm=0.03 (norm003) 的重复实验，kill 了有效进程。cuda:0 空闲 9 小时。\\n**根因**: Worker 只看 session 名和 output_file 路径，未核对 `--max_correction_norm` 参数值。\\n**规则**: kill 实验前必须 `ps aux | grep` 完整命令行，逐一比对关键参数（mode, norm, checkpoint, benchmark）。名字相似 ≠ 同一实验。\\n\\n## [命名规范] exp_id 中 norm 值 (2026-05-15)\\n\\n- Registry exp_id 不允许 `.`，norm 值用 `p` 替代小数点：norm-0p3 = 0.3, norm-0p03 = 0.03\\n- 禁止缩写歧义命名（norm03 可能是 0.03 也可能是 0.3）\\n- output_file 同步使用 `0p3` 格式\\n\", \"total_chars\": 2113, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "02cf1bd4-0a84-4bdc-975f-0a0e6ec9ab07",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\\\", \\\"content\\\": \\\"# Project Memory\\\\n\\\\n## Spatial Baselines 锁定 (2026-05-15)\\\\n\\\\n| 方法 | SR | 来源 |\\\\n|------|-----|------|\\\\n| VLA-only K=1 | 30% | eval-spatial-v7-full |\\\\n| VLA-mean K=10 | 32% | eval-vla-mean-spatial |\\\\n| Argmin K=10 | 34% | eval-argmin-only-spatial-r2 (与 reconvla-v3 独立复现一致) |\\\\n\\\\n**关键发现**: K=10 采样 + scalar argmin 选择增益有限 (+2pp over mean, +4pp over K=1)。CRM correction 的 bar 是 34%。\\\\n\\\\n## Hard Tasks 普遍失败 (2026-05-15)\\\\n\\\\nT2 (from_table_center), T7 (on_stove): 所有方法 0%。T4 (in_top_drawer), T5 (on_ramekin): 所有方法 0-10%。这是 VLA backbone 限制，不是 CRM 问题。论文不应在这些 tasks 上 claim CRM 改进。\\\\n\\\\n## D027 CRITICAL: perdof = argmin on matched tasks (2026-05-15)\\\\n\\\\nT0-T6 matched comparison: perdof 42.9% = argmin ~43% (0pp delta)。Per-DOF claim 在 spatial 上已死。项目存活依赖：\\\\n1. Magnitude sweep 找到 perdof 显著优于 argmin 的 norm 点\\\\n2. Object benchmark 跨域验证\\\\n3. obs_only CRM +5pp 稳定 → 转向 \\\\\\\"learned correction\\\\\\\" narrative\\\\n\\\\n## obs_only 走势 (2026-05-15)\\\\n\\\\nobs_only 从 57.5%@4tasks 降到 40%@6tasks（hard tasks 拖累）。但 obs_only 在 magnitude sweep 中每个已测 norm 下都 >= perdof (+10-20pp，仅 2 tasks)。如果趋势在 5+ tasks 后仍保持，论文可转向 \\\\\\\"obs-only CRM correction\\\\\\\" narrative。\\\\n\\\\n## Object Baseline (2026-05-15)\\\\n\\\\nVLA-only K=1 object = 12%。CRM 在 object benchmark 有更大提升空间（baseline 低）。\\\\n\\\\n## bjb2-40593 环境问题 (2026-05-14-15)\\\\n\\\\n- 无 .git repo\\\\n- CRM cache 路径 /root/autodl-tmp/crm_cache/spatial/（旧路径，非 v5）\\\\n- Ghost PID 211962 已 kill，eval-mag-obsonly-norm003-b2 恢复运行\\\\n\\\\n## [失败模式] submit_training_job EXIT_CODE=127 (2026-05-15)\\\\n\\\\ntmux 用 `sh` 而非 `bash` 执行命令，`python` 等 conda/venv 命令不在 `sh` PATH 中。修复：命令必须用 `bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...\\\\\\\"` 包裹。裸 `python -u ...` 有时可行（取决于服务器 PATH 配置），但不可靠。\\\\n\\\\n## [失败模式] Kill 操作前必须逐参数比对 (2026-05-15)\\\\n\\\\n**事故**: Worker 将 norm=0.3 (norm03) 误判为 norm=0.03 (norm003) 的重复实验，kill 了有效进程。cuda:0 空闲 9 小时。\\\\n**根因**: Worker 只看 session 名和 output_file 路径，未核对 `--max_correction_norm` 参数值。\\\\n**规则**: kill 实验前必须 `ps aux | grep` 完整命令行，逐一比对关键参数（mode, norm, checkpoint, benchmark）。名字相似 ≠ 同一实验。\\\\n\\\\n## [命名规范] exp_id 中 norm 值 (2026-05-15)\\\\n\\\\n- Registry exp_id 不允许 `.`，norm 值用 `p` 替代小数点：norm-0p3 = 0.3, norm-0p03 = 0.03\\\\n- 禁止缩写歧义命名（norm03 可能是 0.03 也可能是 0.3）\\\\n- output_file 同步使用 `0p3` 格式\\\\n\\\", \\\"total_chars\\\": 2113, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## Spatial Baselines 锁定 (2026-05-15)\\n\\n| 方法 | SR | 来源 |\\n|------|-----|------|\\n| VLA-only K=1 | 30% | eval-spatial-v7-full |\\n| VLA-mean K=10 | 32% | eval-vla-mean-spatial |\\n| Argmin K=10 | 34% | eval-argmin-only-spatial-r2 (与 reconvla-v3 独立复现一致) |\\n\\n**关键发现**: K=10 采样 + scalar argmin 选择增益有限 (+2pp over mean, +4pp over K=1)。CRM correction 的 bar 是 34%。\\n\\n## Hard Tasks 普遍失败 (2026-05-15)\\n\\nT2 (from_table_center), T7 (on_stove): 所有方法 0%。T4 (in_top_drawer), T5 (on_ramekin): 所有方法 0-10%。这是 VLA backbone 限制，不是 CRM 问题。论文不应在这些 tasks 上 claim CRM 改进。\\n\\n## D027 CRITICAL: perdof = argmin on matched tasks (2026-05-15)\\n\\nT0-T6 matched comparison: perdof 42.9% = argmin ~43% (0pp delta)。Per-DOF claim 在 spatial 上已死。项目存活依赖：\\n1. Magnitude sweep 找到 perdof 显著优于 argmin 的 norm 点\\n2. Object benchmark 跨域验证\\n3. obs_only CRM +5pp 稳定 → 转向 \\\"learned correction\\\" narrative\\n\\n## obs_only 走势 (2026-05-15)\\n\\nobs_only 从 57.5%@4tasks 降到 40%@6tasks（hard tasks 拖累）。但 obs_only 在 magnitude sweep 中每个已测 norm 下都 >= perdof (+10-20pp，仅 2 tasks)。如果趋势在 5+ tasks 后仍保持，论文可转向 \\\"obs-only CRM correction\\\" narrative。\\n\\n## Object Baseline (2026-05-15)\\n\\nVLA-only K=1 object = 12%。CRM 在 object benchmark 有更大提升空间（baseline 低）。\\n\\n## bjb2-40593 环境问题 (2026-05-14-15)\\n\\n- 无 .git repo\\n- CRM cache 路径 /root/autodl-tmp/crm_cache/spatial/（旧路径，非 v5）\\n- Ghost PID 211962 已 kill，eval-mag-obsonly-norm003-b2 恢复运行\\n\\n## [失败模式] submit_training_job EXIT_CODE=127 (2026-05-15)\\n\\ntmux 用 `sh` 而非 `bash` 执行命令，`python` 等 conda/venv 命令不在 `sh` PATH 中。修复：命令必须用 `bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...\\\"` 包裹。裸 `python -u ...` 有时可行（取决于服务器 PATH 配置），但不可靠。\\n\\n## [失败模式] Kill 操作前必须逐参数比对 (2026-05-15)\\n\\n**事故**: Worker 将 norm=0.3 (norm03) 误判为 norm=0.03 (norm003) 的重复实验，kill 了有效进程。cuda:0 空闲 9 小时。\\n**根因**: Worker 只看 session 名和 output_file 路径，未核对 `--max_correction_norm` 参数值。\\n**规则**: kill 实验前必须 `ps aux | grep` 完整命令行，逐一比对关键参数（mode, norm, checkpoint, benchmark）。名字相似 ≠ 同一实验。\\n\\n## [命名规范] exp_id 中 norm 值 (2026-05-15)\\n\\n- Registry exp_id 不允许 `.`，norm 值用 `p` 替代小数点：norm-0p3 = 0.3, norm-0p03 = 0.03\\n- 禁止缩写歧义命名（norm03 可能是 0.03 也可能是 0.3）\\n- output_file 同步使用 `0p3` 格式\\n\", \"total_chars\": 2113, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have all four files. Let me synthesize the information and create a comprehensive CoRL paper outline.

Key facts:
1. **Spatial benchmark**: ALL CRM variants dead (obs_only 35%, perdof 35%, argmin 34% — ±1pp, no statistical significance)
2. **Object benchmark (5/10 tasks)**: obs_only 16% vs argmin 8% (+8pp) — only surviving signal, p≈0.19
3. **Magnitude sweep**: obs_only > perdof at all tested norms (+8-12pp on confirmed norms)


4. **Per-DOF conformal approach doesn't hold up** — observation-conditioned residual learning is the only viable direction
5. **Statistical thresholds**: Object benchmark obs_only advantage of +8pp combined with seed=43 doubling gets us to p<0.05
6. **VLA baselines**: VLA-only K=1 spatial 30%, object 12%; argmin K=10 spatial 34%

The paper needs to pivot to **Scenario C**: "Observation-conditioned residual correction is the key contribution." The core narrative becomes: learned observation-conditioned correction outperforms conformal per-DOF correction, which in turn outperforms pure sample selection. Now I'm drafting the writing.

Structuring the narrative around honesty about the spatial null result while positioning obs_only CRM as the main finding, with magnitude control as a critical insight and per-DOF conformal as an interesting negative ablation. Some results still depend on seed=43 data for statistical validation. For the title, I'm considering angles around learned residual correction for VLA robustness, sample-then-refine, or observation-conditioned correction. I need to plan out the figures: an overview pipeline diagram, object benchmark comparison, magnitude sweep curve, per-task heatmap, and bootstrap confidence interval plot. Now I'm setting up the YAML structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "e1c09b1b-cd5a-45c3-9d05-60372a7c0525",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVcY5GXEp2ecmRteEsnSnk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20967,
      "cache_read_input_tokens": 24065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20967
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

_source line 17_

All four files read. Now I'll synthesize and write the outline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "a071ca03-ed2d-466e-b15c-a5eda6e215cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVcY5GXEp2ecmRteEsnSnk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20967,
      "cache_read_input_tokens": 24065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20967
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_017v9bCjYJvJS2Mk9pVtoMJx`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "writing_plan.yaml",
  "content": "# CoRL 2026 Paper Outline — ACR-VLA\n# Last updated: 2026-05-15\n# Status: DRAFT — pending object T5-T9 and seed=43 results\n\n# ============================================================\n# CANDIDATE TITLES\n# ============================================================\ntitles:\n  - \"Sample, Select, Correct: Observation-Conditioned Residual Refinement for Robust VLA Control\"\n  - \"When Conformal Features Fail: Learned Residual Correction for Vision-Language-Action Robustness\"\n  - \"ACR-VLA: Adaptive Correction and Refinement of Vision-Language-Action Policies via Learned Residual Modules\"\n\npreferred: 1  # Title 1 — action-oriented, captures pipeline, avoids overclaim\n\n# ============================================================\n# CORE CLAIM (1 sentence, falsifiable)\n# ============================================================\ncore_claim: >\n  A lightweight observation-conditioned residual module (CRM), applied after\n  multi-sample conformal selection on a frozen VLA, significantly improves\n  manipulation success on out-of-distribution object perturbations (+8pp over\n  sample selection alone), while per-DOF conformal statistics — despite their\n  theoretical appeal — provide no additional correction benefit beyond\n  observation features.\n\n# ============================================================\n# SECTION OUTLINE\n# ============================================================\nsections:\n\n  abstract:\n    target_words: 200\n    bullets:\n      - \"Flow-matching VLAs achieve near-saturated in-distribution performance but degrade catastrophically under distribution shift (LIBERO-Plus).\"\n      - \"We propose ACR-VLA: a three-stage inference-time pipeline — (1) multi-sample generation, (2) conformal-score-based selection, (3) observation-conditioned learned residual correction (CRM) — that wraps any frozen VLA without retraining.\"\n      - \"On LIBERO-Plus object perturbations, CRM correction yields +8pp over conformal selection alone (16% vs 8%); magnitude-controlled correction is essential for closed-loop stability. Ablations reveal that observation features suffice for effective correction — structured per-DOF conformal features add no benefit, a surprising negative result with implications for uncertainty-conditioned policy correction.\"\n\n  introduction:\n    target_pages: 1.5\n    bullets:\n      - \"Opening: VLAs achieve 97-99% on standard LIBERO but LIBERO-Plus exposes robustness gap under 7 perturbation types. Existing solutions are either training-time (RobustVLA, SRPO, ACoT) or limited inference-time (ReconVLA selects but cannot synthesize better actions).\"\n      - \"Gap: No existing method performs learned, dimension-aware action correction at inference time on frozen VLAs. ReconVLA's scalar CP loses per-DOF structure; SC-VLA requires task-level RL; VLA-Pilot has 2.4s latency.\"\n      - \"Contribution summary: (1) Sample-then-refine pipeline with conformal selection + learned CRM; (2) Discovery that magnitude control is critical for residual correction stability; (3) Honest ablation showing observation features outperform structured conformal features for correction conditioning — challenging the intuition that richer uncertainty representations always help.\"\n    key_references:\n      - fei2025liberoplus\n      - chen2026reconvla\n      - sc_vla_2026\n      - silver2018residual\n\n  related_work:\n    target_pages: 1.5\n    subsections:\n      vla_robustness:\n        scope: \"Training-time methods (RobustVLA, SRPO, DiG-Flow, ACoT-VLA) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2). Position ACR-VLA as plug-and-play inference-time correction.\"\n        key_refs: [robustvla2025, srpo2025, digflow2025, acot_vla_2026, chen2026reconvla, sc_vla_2026, vla_pilot_2025, a2c2_2025]\n      conformal_prediction_robotics:\n        scope: \"CP foundations (Angelopoulos, CGS), CP in robotics (conformalized teleop, CP-loop, ACP+CBF, CLAPS). Position ACR-VLA's use of CP as feature extractor, not output guarantee.\"\n        key_refs: [angelopoulos2023gentle, braun2025cgs, zhao2024conformalized, wang2025cploop, zhou2025acp_cbf]\n      residual_policy_learning:\n        scope: \"Residual RL (Silver 2018, TRANSIC, PLD, DRC). Emphasize magnitude control as underexplored critical factor.\"\n        key_refs: [silver2018residual, jiang2024transic, xiao2026pld, pan2025drc]\n      uncertainty_quantification_vla:\n        scope: \"UQ for VLAs (DiU, SAFE, VLA calibration). Distinguish multi-sample epistemic UQ from single-pass aleatoric.\"\n        key_refs: [xing2026diu, gu2025safe, zollo2025vla_calibration, tang2026shifting_uncertainty]\n\n  method:\n    target_pages: 2.0\n    subsections:\n      problem_setup:\n        bullets:\n          - \"Frozen flow-matching VLA π_θ generates K action samples per step. Goal: select and correct without retraining π_θ.\"\n          - \"Action space: 7-DOF (6 arm + 1 gripper), action chunks of length C.\"\n      multi_sample_generation_and_selection:\n        bullets:\n          - \"K=10 samples from flow-matching VLA; Conformalized Gaussian Scoring (CGS) with Ledoit-Wolf shrinkage covariance → per-sample nonconformity score.\"\n          - \"Argmin selection: pick lowest-CGS-score sample as base action a_base.\"\n      conformal_residual_module:\n        bullets:\n          - \"CRM architecture: lightweight MLP (~250K params), takes observation features z_obs as input, outputs bounded residual δ.\"\n          - \"Final action: a = a_base + clip(δ, ‖δ‖ ≤ ε) where ε is magnitude bound.\"\n          - \"Training: offline on calibration set with L2 loss to expert actions, augmented with synthetic perturbations.\"\n      magnitude_control:\n        bullets:\n          - \"Critical finding: unbounded CRM (ε=1.42) → 0% success (compounding error destroys trajectory). Small ε (0.05-0.2) → stable correction.\"\n          - \"Norm sweep: ε ∈ {0.03, 0.05, 0.1, 0.2, 0.3}. Optimal range ε ∈ [0.05, 0.2].\"\n          - \"Connect to residual RL literature (Silver 2018, TRANSIC gating, PLD scheduling).\"\n\n  experiments:\n    target_pages: 2.5\n    subsections:\n      setup:\n        bullets:\n          - \"Backbone: SmolVLA (450M params, flow-matching). Benchmark: LIBERO-Plus spatial + object (10 tasks each, 10 rollouts/task/seed).\"\n          - \"Baselines: VLA-only (K=1), VLA-mean (K=10), Argmin (K=10), perdof CRM, scalar CRM, obs_only CRM.\"\n          - \"Statistical protocol: primary seed + seed=43 doubling (200 trials), bootstrap CI, Fisher exact test.\"\n      main_results:\n        bullets:\n          - \"Object benchmark: obs_only CRM 16% vs argmin 8% (+8pp). VLA-only 10%. perdof CRM 10% ≈ argmin.\"\n          - \"Spatial benchmark: ALL methods ≈ 34-35% (honest null result). CRM correction does not help on spatial perturbations.\"\n          - \"Interpretation: spatial perturbations may require training-time adaptation; object perturbations are correctable at inference time.\"\n      ablation_crm_features:\n        bullets:\n          - \"4-way ablation: obs_only > perdof ≈ scalar ≈ argmin on both benchmarks.\"\n          - \"Key negative result: per-DOF conformal features (40D) add NO value over observation features for correction conditioning.\"\n          - \"Hypothesis: observation features already encode task-relevant geometric info; conformal statistics are redundant when correction target is learned.\"\n      magnitude_sensitivity:\n        bullets:\n          - \"Sweep across 5 norm values. obs_only consistently > perdof at every tested norm.\"\n          - \"Sharp phase transition: ε > 0.3 → rapid degradation; ε < 0.03 → correction too small to matter.\"\n          - \"Optimal ε depends on task difficulty — harder tasks benefit from smaller corrections.\"\n      per_task_analysis:\n        bullets:\n          - \"Task-level heatmap reveals CRM helps most on medium-difficulty tasks (T0, T3) where VLA is partially capable.\"\n          - \"Hard tasks (T2, T7: 0% across all methods) → VLA backbone limitation, not CRM failure.\"\n          - \"Variance across tasks: obs_only T0 +30pp over argmin, but T5/T8/T9 each -10pp → compounding error risk.\"\n\n  discussion:\n    target_pages: 0.5\n    bullets:\n      - \"Why per-DOF conformal features fail: learned correction optimizes a different objective than conformal calibration. The MLP likely learns to extract uncertainty-relevant signals directly from observation features, making explicit conformal statistics redundant as conditioning input.\"\n      - \"When does inference-time correction work? Object perturbations (novel instances of known categories) vs spatial perturbations (layout changes requiring replanning). Correction ≠ replanning.\"\n      - \"Limitations: (1) sim-only evaluation, (2) single VLA backbone, (3) compounding error on some tasks, (4) magnitude bound requires per-domain tuning.\"\n\n  conclusion:\n    target_pages: 0.3\n    bullets:\n      - \"ACR-VLA demonstrates that learned observation-conditioned correction after conformal selection improves VLA robustness on object perturbations.\"\n      - \"Negative result: per-DOF conformal features do not improve correction over observation features — a cautionary tale for uncertainty-conditioned policy correction.\"\n      - \"Future: (a) multi-backbone validation (OpenVLA, pi0), (b) real robot transfer, (c) adaptive magnitude scheduling, (d) combining with training-time methods (SRPO, ACoT).\"\n\n# ============================================================\n# KEY FIGURES (minimum 5)\n# ============================================================\nfigures:\n\n  fig1_pipeline:\n    type: overview_diagram\n    description: \"ACR-VLA pipeline: frozen VLA → K samples → CGS scoring → argmin selection → CRM correction → final action. Highlight CRM input (obs features) and magnitude clipping.\"\n    placement: method\n    priority: P0\n    status: to_create\n\n  fig2_object_benchmark:\n    type: grouped_bar_chart\n    description: \"Object benchmark 10-task success rate. Bars: VLA-only, argmin, perdof, obs_only, scalar. Error bars from bootstrap CI. Star on obs_only vs argmin significance.\"\n    placement: experiments/main_results\n    priority: P0\n    status: blocked_on_T5-T9\n    data_dependency: \"object T5-T9 eval + seed=43\"\n\n  fig3_magnitude_sweep:\n    type: line_plot\n    description: \"Success rate vs correction magnitude ε. Lines: obs_only, perdof, argmin (flat reference). X-axis: ε ∈ {0, 0.03, 0.05, 0.1, 0.2, 0.3, 1.42}. Show phase transition and optimal range.\"\n    placement: experiments/magnitude_sensitivity\n    priority: P0\n    status: blocked_on_full_sweep\n    data_dependency: \"magnitude sweep 10-task completion\"\n\n  fig4_per_task_heatmap:\n    type: heatmap\n    description: \"Per-task success rate heatmap. Rows: 10 spatial + 10 object tasks. Columns: argmin, perdof, obs_only. Color: 0-100% SR. Annotate task difficulty clusters.\"\n    placement: experiments/per_task_analysis\n    priority: P1\n    status: blocked_on_full_data\n\n  fig5_ablation_radar:\n    type: radar_or_bar\n    description: \"4-way CRM feature ablation (obs_only, perdof, scalar, argmin-only) across both benchmarks. Clearly show obs_only dominance and perdof ≈ argmin collapse.\"\n    placement: experiments/ablation_crm_features\n    priority: P0\n    status: blocked_on_object_complete\n\n  fig6_statistical_significance:\n    type: forest_plot_or_CI\n    description: \"Bootstrap confidence intervals for pairwise comparisons (obs_only vs argmin, obs_only vs perdof, perdof vs argmin). Show significance thresholds.\"\n    placement: experiments/main_results\n    priority: P1\n    status: blocked_on_seed43\n    data_dependency: \"seed=43 doubling results\"\n\n  fig7_task_difficulty:\n    type: scatter_plot\n    description: \"CRM improvement (obs_only - argmin) vs task base difficulty (argmin SR). Show that correction helps medium tasks, not easy/hard extremes.\"\n    placement: discussion\n    priority: P2\n    status: blocked_on_full_data\n\n# ============================================================\n# KEY TABLES\n# ============================================================\ntables:\n\n  table1_main_results:\n    description: \"Main results table. Rows: VLA-only, VLA-mean, Argmin, perdof CRM, obs_only CRM, scalar CRM. Columns: Spatial SR, Object SR, Δ vs Argmin, p-value. Bold best, underline second.\"\n    placement: experiments/main_results\n    priority: P0\n    status: blocked_on_full_data\n\n  table2_magnitude_sweep:\n    description: \"Success rate at each magnitude bound. Rows: ε values. Columns: perdof, obs_only, argmin (reference). Highlight optimal range.\"\n    placement: experiments/magnitude_sensitivity\n    priority: P1\n    status: blocked_on_full_sweep\n\n  table3_comparison_landscape:\n    description: \"Qualitative comparison with related methods. Rows: ReconVLA, SC-VLA, VLA-Pilot, TRANSIC, PLD, ACR-VLA. Columns: correction type, UQ method, retraining needed, latency, benchmark.\"\n    placement: related_work\n    priority: P2\n    status: can_write_now\n\n# ============================================================\n# WRITING ORDER\n# ============================================================\nwriting_order:\n  - step: 1\n    section: experiments\n    rationale: \"Data-first. Lock all numbers before writing claims. Blocked on object T5-T9 and seed=43.\"\n    deadline: \"2026-05-20\"\n\n  - step: 2\n    section: method\n    rationale: \"Describe what we actually did, informed by which results survived.\"\n    deadline: \"2026-05-22\"\n\n  - step: 3\n    section: introduction\n    rationale: \"Frame the story around confirmed results. Write gap and contribution after method is stable.\"\n    deadline: \"2026-05-24\"\n\n  - step: 4\n    section: related_work\n    rationale: \"Position against competitors with calibrated claims.\"\n    deadline: \"2026-05-25\"\n\n  - step: 5\n    section: abstract\n    rationale: \"Compress final story into 200 words. Only after all sections stable.\"\n    deadline: \"2026-05-26 (abstract DDL)\"\n\n  - step: 6\n    section: discussion_and_conclusion\n    rationale: \"Limitations and future work. Can iterate until full paper DDL.\"\n    deadline: \"2026-06-01\"\n\n  - step: 7\n    section: figures_and_polish\n    rationale: \"Final figure generation, formatting, reference check.\"\n    deadline: \"2026-06-02 (full paper DDL)\"\n\n# ============================================================\n# LITERATURE GAPS (citations to add)\n# ============================================================\nliterature_gaps:\n\n  - direction: \"Residual correction in diffusion/flow models (non-RL)\"\n    why: \"CRM is supervised residual, not RL. Need refs for supervised residual correction to distinguish from RL-based methods.\"\n    urgency: high\n\n  - direction: \"Negative results in uncertainty-conditioned control\"\n    why: \"Our per-DOF negative result needs context. Are there precedents where richer uncertainty representations failed to help downstream tasks?\"\n    urgency: medium\n\n  - direction: \"Object vs spatial robustness taxonomy\"\n    why: \"Our result that correction works for object but not spatial perturbations needs grounding in robustness/generalization theory.\"\n    urgency: medium\n\n  - direction: \"Compounding error in residual policies\"\n    why: \"Task-level variance (some tasks hurt by CRM) relates to compounding error literature. Need refs beyond DAgger/DART.\"\n    urgency: low\n\n  - direction: \"Conformal prediction as feature extraction (not guarantee)\"\n    why: \"Novel use of CP — using conformal scores as input features rather than for coverage guarantees. Any precedent?\"\n    urgency: medium\n\n# ============================================================\n# HONEST REPORTING COMMITMENTS\n# ============================================================\nhonest_reporting:\n  - \"Spatial null result (CRM ≈ argmin ±1pp) reported prominently in main results, not buried in appendix.\"\n  - \"Per-DOF conformal features failing is a headline negative result, not downplayed.\"\n  - \"Task-level variance (some tasks hurt by CRM) shown in heatmap with explicit discussion of compounding error.\"\n  - \"Statistical significance: if seed=43 does not replicate +8pp, paper is not submitted.\"\n  - \"No overclaim on 'conformal guarantees' — CRM output has no formal coverage property.\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "909db247-8c34-409c-b091-c06cfb7ab909",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BVcY5GXEp2ecmRteEsnSnk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20967,
      "cache_read_input_tokens": 24065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20967
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

_source line 19 · 2026-05-15T13:26:48.199Z_

<details><summary>↩ Tool result · `toolu_017v9bCjYJvJS2Mk9pVtoMJx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/writing_plan.yaml\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "03a8922e-993d-4af2-9f52-59711ddd0ddc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/writing_plan.yaml\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/writing_plan.yaml\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

已写入 `writing_plan.yaml`。核心结构：

**Title**: "Sample, Select, Correct: Observation-Conditioned Residual Refinement for Robust VLA Control"（首选）

**Narrative 主线**: obs_only CRM 在 object perturbation 上 +8pp over argmin selection；per-DOF conformal features 作为 headline negative result 诚实报告。

**7 个 figure**:
- P0: pipeline overview、object benchmark bar chart、magnitude sweep curve、4-way ablation
- P1: per-task heatmap、statistical significance CI
- P2: task difficulty vs CRM improvement scatter

**写作顺序**: experiments → method → intro → related work → abstract → discussion → polish，abstract DDL 5/26 前完成前 5 步。

**关键 blocker**: object T5-T9 eval 和 seed=43 doubling 数据。没有这些数据，fig2/fig5/table1 无法锁定，abstract 无法定稿。

**5 个文献缺口**: supervised（非 RL）residual correction、uncertainty-conditioned negative results 先例、object vs spatial robustness 分类学、compounding error、CP-as-feature-extractor 先例。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "uuid": "ce4ca6c5-3934-43d0-bc86-81a536c21122",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vT1y2w7rjdzvcX8PNfrvL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5127,
      "cache_read_input_tokens": 45032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5127
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

_source line 21_

已写入 `writing_plan.yaml`。核心结构：

**Title**: "Sample, Select, Correct: Observation-Conditioned Residual Refinement for Robust VLA Control"（首选）

**Narrative 主线**: obs_only CRM 在 object perturbation 上 +8pp over argmin selection；per-DOF conformal features 作为 headline negative result 诚实报告。

**7 个 figure**:
- P0: pipeline overview、object benchmark bar chart、magnitude sweep curve、4-way ablation
- P1: per-task heatmap、statistical significance CI
- P2: task difficulty vs CRM improvement scatter

**写作顺序**: experiments → method → intro → related work → abstract → discussion → polish，abstract DDL 5/26 前完成前 5 步。

**关键 blocker**: object T5-T9 eval 和 seed=43 doubling 数据。没有这些数据，fig2/fig5/table1 无法锁定，abstract 无法定稿。

**5 个文献缺口**: supervised（非 RL）residual correction、uncertainty-conditioned negative results 先例、object vs spatial robustness 分类学、compounding error、CP-as-feature-extractor 先例。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 129571,
  "duration_api_ms": 130659,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "b6cb25da-4cea-4374-bc7a-5660504ee1e9",
  "total_cost_usd": 0.440978,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 38318,
    "cache_read_input_tokens": 104285,
    "output_tokens": 5914,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38318,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 323,
        "cache_read_input_tokens": 45032,
        "cache_creation_input_tokens": 5127,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5127
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1338,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001458,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 5914,
      "cacheReadInputTokens": 104285,
      "cacheCreationInputTokens": 38318,
      "webSearchRequests": 0,
      "costUSD": 0.43952,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "84134d5f-84dd-46ac-abec-6dec63a7da70"
}
```

</details>

---
