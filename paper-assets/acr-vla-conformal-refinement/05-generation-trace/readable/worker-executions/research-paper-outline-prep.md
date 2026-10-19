# research paper outline prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_research_paper-outline-prep_20260515T044605.log`
- **Structured JSON:** [`074936167641958c6e55.json`](../../sessions/07/074936167641958c6e55.json)

## Before a recorded user message

23 recorded events

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
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
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
  "uuid": "fdded427-fb6d-489b-a947-cf7a3341db15",
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
    "resetsAt": 1778837400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "781ad303-1a82-4cd9-b55e-da06f41cc35c",
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the three source files mentioned in the task steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "14e31415-fa47-4633-9a70-949ec59cf0b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXvDtRxE4F2kgdZRtefjRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11441,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11441
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LDGMiFKpnVMXMbYBYgweub`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "ba46b6b4-3238-4a73-ba8c-79a7a5b01d7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXvDtRxE4F2kgdZRtefjRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11441,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11441
      },
      "output_tokens": 23,
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

_source line 6 · 2026-05-15T04:46:16.216Z_

<details><summary>↩ Tool result · `toolu_01LDGMiFKpnVMXMbYBYgweub`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "85b61985-08b3-4e82-9879-be5ead82b0e7",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

读取三个源文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "198fe282-bfd4-48a5-8ab9-c9d86953ea3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWmRckJaa51NeyW8vXdMFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 23282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1342
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PBuFJNeyDTRtngzee7cELc`</summary>

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
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "133fb6f9-e45f-4baa-92af-bc2001d66b51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWmRckJaa51NeyW8vXdMFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 23282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1342
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

_source line 9 · 2026-05-15T04:46:19.962Z_

<details><summary>↩ Tool result · `toolu_01PBuFJNeyDTRtngzee7cELc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\"which action dimensions are uncertain and how they co-vary\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\n\\n> ⚠️ **Pending ablation confirmation**: \\\"fundamentally richer\\\" 措辞依赖 Scenario A (perdof > obs_only)。如果 Scenario B/C，Core Insight 需调整为 \\\"uncertainty-conditioned learned correction\\\" 或 \\\"observation-conditioned residual correction\\\"。见备选策略。\\n\\n## Core Claims (2 条，均可证伪) — D022: Claim 3 SRPO stacking 因 CoRL 时间限制移除\\n1. **Learned correction conditioned on uncertainty features significantly improves VLA robustness**: CRM（轻量 MLP）以 uncertainty 特征为条件输入，在 argmin 样本选择基础上进一步校正动作，显著优于纯选择方法。\\n   - **主 claim (硬证据)**: CRM correction 相比 argmin-only selection 有独立增量 (+9.6pp interim)\\n   - **子 claim (待确认)**: Per-DOF conformal features (40D) 作为 conditioning 比 obs-only / scalar 更优\\n   - 验证: MVP (✅ done) + spatial 4-way ablation (perdof vs obs_only vs scalar_unc vs argmin_only, RUNNING) + object benchmark\\n   - Kill criterion (主 claim): CRM correction vs argmin-only < 3pp across both benchmarks → correction 无价值\\n   - Kill criterion (子 claim): obs_only eval >= perdof eval → per-DOF features 无额外价值，启用备选 framing\\n\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\\n\\n~~3. **ACR-VLA 与 training-time 方法正交互补** — D022 移除: 11 天内无法获取 SRPO checkpoint + 重训 CRM + eval。留给扩展版本。~~\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\"哪些维度不确定+跨维度协方差\\\"，使 CRM 能做维度选择性校正。\\n- **Headline result template**: \\\"On LIBERO, ACR-VLA's uncertainty-conditioned sample-then-refine pipeline (K=10 conformal selection + learned CRM correction) improves SmolVLA success by +X pp on spatial and +Y pp on object tasks — with CRM correction contributing Z pp beyond sample selection alone, and correction magnitude control proving critical for closed-loop stability.\\\"\\n\\n## Competitive Landscape\\n\\n### ReconVLA — 最直接竞品\\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\n\\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \\\"哪个关节不确定\\\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\\n\\n### SC-VLA — Inference-time RL refinement\\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\\n\\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\\n\\n### VLA-Pilot — MLLM-guided steering\\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\\n\\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\\n\\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\\n\\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \\\"不确定\\\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\\n\\n### ACR-VLA 差异化定位\\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\\n\\n## Anticipated Reviewer Concerns\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\n7. **[Dream 新增] \\\"Conformal\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\"conformal-feature-conditioned correction\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\n\\n## Framing 备选策略 (D022 细化, Reviewer 审查后修补)\\n\\n**四路 ablation 排序预测** (val_loss 顺序: obs_only 0.0165 < perdof 0.0358 ≈ scalar_unc 0.0374):\\n- 训练 loss 预测: obs_only > scalar_unc ≈ perdof > argmin_only\\n- 但 closed-loop eval 可能翻转（conformal features 在分布偏移下的 epistemic value）\\n\\n### Scenario A: perdof > obs_only (最佳)\\nClaim 1 主+子 claim 均成立。Story: \\\"Per-DOF conformal features encode dimension-specific uncertainty that observation features alone cannot capture; this enables superior learned correction under distribution shift — despite worse training loss, conformal features' real-time epistemic signal proves critical in closed-loop deployment.\\\"\\n- Core Insight 不变\\n- 这是最强 narrative：training loss 反直觉但 eval 翻转 = compelling story\\n- scalar_unc 预期位置: ≈ perdof (相似 val_loss) 或略低 → per-DOF vs scalar 差异化成立\\n\\n### Scenario B: perdof ≈ obs_only ≈ scalar_unc (任意两者差 <5pp)\\n主 claim 成立（CRM correction 有价值），子 claim 弱化。Story: \\\"Uncertainty-conditioned learned correction (sample-then-refine) significantly outperforms pure sample selection. The specific form of uncertainty features (per-DOF, scalar, or observation-only) matters less than the correction mechanism itself.\\\"\\n- Core Insight 调整: 去掉 \\\"fundamentally richer than scalar\\\"，改为 \\\"enables principled learned correction\\\"\\n- Per-DOF 作为 Claim 2 (ACI+COC) 的必要组件保留\\n- **Magnitude control as empirical contribution**: 升级为独立发现 (Section: \\\"Critical Role of Correction Magnitude\\\")\\n\\n### Scenario C: obs_only > perdof AND obs_only > scalar_unc (>5pp)\\n主 claim 仍成立（CRM correction 有价值），子 claim 不成立。Story: \\\"Observation-conditioned residual correction is the key contribution. Conformal features as direct CRM input offer no additional value over observation features, but remain valuable for (a) sample selection quality, (b) online coverage monitoring (ACI+COC).\\\"\\n- Core Insight 需重写: \\\"Lightweight learned residual correction on selected VLA samples significantly improves robustness\\\"\\n- Per-DOF features 在 ablation table 如实呈现为 negative result\\n- **特殊子情况**: 如果 scalar_unc > perdof 但 scalar_unc < obs_only → conformal 特征形式无关紧要\\n\\n### 共性硬证据（所有 scenario 均可用）\\n- CRM correction vs argmin-only: +9.6pp (interim, if holds)\\n- Selection + Correction vs baseline: +20.5pp (interim)\\n- Magnitude control discovery: norm=1.42 → 0%, norm=0.1 → 52.5% (novel empirical finding, 可独立成 contribution section)\\n- ACI+COC online adaptation (Claim 2, independent of Claim 1 outcome)\\n\\n### Kill criteria (Reviewer 校准后)\\n- **内部 kill (停止投入)**: CRM correction vs argmin-only < 3pp on ANY benchmark\\n- **论文 claim 门槛**: ≥5pp + Fisher exact test p<0.05 on EACH benchmark independently\\n- **3-5pp 灰区**: claim 技术上存活但论文说服力不足 (\\\"zombie claim\\\")，需要加 n_rollouts 或加 benchmark 提升统计力\\n- **跨 benchmark 逻辑**: ANY benchmark < 3pp → 该 benchmark 降级; BOTH < 3pp → claim killed\\n\", \"total_chars\": 9063, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "d18c73fb-3a90-4ef3-bca3-3ac08df736dd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n## Target Venue\\\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\\\n- ~~ICLR 2027~~ — 不再是首要目标\\\\n\\\\n## Core Insight\\\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\\\\\"which action dimensions are uncertain and how they co-vary\\\\\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\\\n\\\\n> ⚠️ **Pending ablation confirmation**: \\\\\\\"fundamentally richer\\\\\\\" 措辞依赖 Scenario A (perdof > obs_only)。如果 Scenario B/C，Core Insight 需调整为 \\\\\\\"uncertainty-conditioned learned correction\\\\\\\" 或 \\\\\\\"observation-conditioned residual correction\\\\\\\"。见备选策略。\\\\n\\\\n## Core Claims (2 条，均可证伪) — D022: Claim 3 SRPO stacking 因 CoRL 时间限制移除\\\\n1. **Learned correction conditioned on uncertainty features significantly improves VLA robustness**: CRM（轻量 MLP）以 uncertainty 特征为条件输入，在 argmin 样本选择基础上进一步校正动作，显著优于纯选择方法。\\\\n   - **主 claim (硬证据)**: CRM correction 相比 argmin-only selection 有独立增量 (+9.6pp interim)\\\\n   - **子 claim (待确认)**: Per-DOF conformal features (40D) 作为 conditioning 比 obs-only / scalar 更优\\\\n   - 验证: MVP (✅ done) + spatial 4-way ablation (perdof vs obs_only vs scalar_unc vs argmin_only, RUNNING) + object benchmark\\\\n   - Kill criterion (主 claim): CRM correction vs argmin-only < 3pp across both benchmarks → correction 无价值\\\\n   - Kill criterion (子 claim): obs_only eval >= perdof eval → per-DOF features 无额外价值，启用备选 framing\\\\n\\\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\\\\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\\\\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\\\\n\\\\n~~3. **ACR-VLA 与 training-time 方法正交互补** — D022 移除: 11 天内无法获取 SRPO checkpoint + 重训 CRM + eval。留给扩展版本。~~\\\\n\\\\n## Story Spine\\\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\\\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\\\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\\\\\"哪些维度不确定+跨维度协方差\\\\\\\"，使 CRM 能做维度选择性校正。\\\\n- **Headline result template**: \\\\\\\"On LIBERO, ACR-VLA's uncertainty-conditioned sample-then-refine pipeline (K=10 conformal selection + learned CRM correction) improves SmolVLA success by +X pp on spatial and +Y pp on object tasks — with CRM correction contributing Z pp beyond sample selection alone, and correction magnitude control proving critical for closed-loop stability.\\\\\\\"\\\\n\\\\n## Competitive Landscape\\\\n\\\\n### ReconVLA — 最直接竞品\\\\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\\\n\\\\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \\\\\\\"哪个关节不确定\\\\\\\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\\\\n\\\\n### SC-VLA — Inference-time RL refinement\\\\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\\\\n\\\\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\\\\n\\\\n### VLA-Pilot — MLLM-guided steering\\\\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\\\\n\\\\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\\\\n\\\\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\\\\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\\\\n\\\\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \\\\\\\"不确定\\\\\\\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\\\\n\\\\n### ACR-VLA 差异化定位\\\\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\\\n7. **[Dream 新增] \\\\\\\"Conformal\\\\\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\\\\\"conformal-feature-conditioned correction\\\\\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\\\n\\\\n## Framing 备选策略 (D022 细化, Reviewer 审查后修补)\\\\n\\\\n**四路 ablation 排序预测** (val_loss 顺序: obs_only 0.0165 < perdof 0.0358 ≈ scalar_unc 0.0374):\\\\n- 训练 loss 预测: obs_only > scalar_unc ≈ perdof > argmin_only\\\\n- 但 closed-loop eval 可能翻转（conformal features 在分布偏移下的 epistemic value）\\\\n\\\\n### Scenario A: perdof > obs_only (最佳)\\\\nClaim 1 主+子 claim 均成立。Story: \\\\\\\"Per-DOF conformal features encode dimension-specific uncertainty that observation features alone cannot capture; this enables superior learned correction under distribution shift — despite worse training loss, conformal features' real-time epistemic signal proves critical in closed-loop deployment.\\\\\\\"\\\\n- Core Insight 不变\\\\n- 这是最强 narrative：training loss 反直觉但 eval 翻转 = compelling story\\\\n- scalar_unc 预期位置: ≈ perdof (相似 val_loss) 或略低 → per-DOF vs scalar 差异化成立\\\\n\\\\n### Scenario B: perdof ≈ obs_only ≈ scalar_unc (任意两者差 <5pp)\\\\n主 claim 成立（CRM correction 有价值），子 claim 弱化。Story: \\\\\\\"Uncertainty-conditioned learned correction (sample-then-refine) significantly outperforms pure sample selection. The specific form of uncertainty features (per-DOF, scalar, or observation-only) matters less than the correction mechanism itself.\\\\\\\"\\\\n- Core Insight 调整: 去掉 \\\\\\\"fundamentally richer than scalar\\\\\\\"，改为 \\\\\\\"enables principled learned correction\\\\\\\"\\\\n- Per-DOF 作为 Claim 2 (ACI+COC) 的必要组件保留\\\\n- **Magnitude control as empirical contribution**: 升级为独立发现 (Section: \\\\\\\"Critical Role of Correction Magnitude\\\\\\\")\\\\n\\\\n### Scenario C: obs_only > perdof AND obs_only > scalar_unc (>5pp)\\\\n主 claim 仍成立（CRM correction 有价值），子 claim 不成立。Story: \\\\\\\"Observation-conditioned residual correction is the key contribution. Conformal features as direct CRM input offer no additional value over observation features, but remain valuable for (a) sample selection quality, (b) online coverage monitoring (ACI+COC).\\\\\\\"\\\\n- Core Insight 需重写: \\\\\\\"Lightweight learned residual correction on selected VLA samples significantly improves robustness\\\\\\\"\\\\n- Per-DOF features 在 ablation table 如实呈现为 negative result\\\\n- **特殊子情况**: 如果 scalar_unc > perdof 但 scalar_unc < obs_only → conformal 特征形式无关紧要\\\\n\\\\n### 共性硬证据（所有 scenario 均可用）\\\\n- CRM correction vs argmin-only: +9.6pp (interim, if holds)\\\\n- Selection + Correction vs baseline: +20.5pp (interim)\\\\n- Magnitude control discovery: norm=1.42 → 0%, norm=0.1 → 52.5% (novel empirical finding, 可独立成 contribution section)\\\\n- ACI+COC online adaptation (Claim 2, independent of Claim 1 outcome)\\\\n\\\\n### Kill criteria (Reviewer 校准后)\\\\n- **内部 kill (停止投入)**: CRM correction vs argmin-only < 3pp on ANY benchmark\\\\n- **论文 claim 门槛**: ≥5pp + Fisher exact test p<0.05 on EACH benchmark independently\\\\n- **3-5pp 灰区**: claim 技术上存活但论文说服力不足 (\\\\\\\"zombie claim\\\\\\\")，需要加 n_rollouts 或加 benchmark 提升统计力\\\\n- **跨 benchmark 逻辑**: ANY benchmark < 3pp → 该 benchmark 降级; BOTH < 3pp → claim killed\\\\n\\\", \\\"total_chars\\\": 9063, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\"which action dimensions are uncertain and how they co-vary\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\n\\n> ⚠️ **Pending ablation confirmation**: \\\"fundamentally richer\\\" 措辞依赖 Scenario A (perdof > obs_only)。如果 Scenario B/C，Core Insight 需调整为 \\\"uncertainty-conditioned learned correction\\\" 或 \\\"observation-conditioned residual correction\\\"。见备选策略。\\n\\n## Core Claims (2 条，均可证伪) — D022: Claim 3 SRPO stacking 因 CoRL 时间限制移除\\n1. **Learned correction conditioned on uncertainty features significantly improves VLA robustness**: CRM（轻量 MLP）以 uncertainty 特征为条件输入，在 argmin 样本选择基础上进一步校正动作，显著优于纯选择方法。\\n   - **主 claim (硬证据)**: CRM correction 相比 argmin-only selection 有独立增量 (+9.6pp interim)\\n   - **子 claim (待确认)**: Per-DOF conformal features (40D) 作为 conditioning 比 obs-only / scalar 更优\\n   - 验证: MVP (✅ done) + spatial 4-way ablation (perdof vs obs_only vs scalar_unc vs argmin_only, RUNNING) + object benchmark\\n   - Kill criterion (主 claim): CRM correction vs argmin-only < 3pp across both benchmarks → correction 无价值\\n   - Kill criterion (子 claim): obs_only eval >= perdof eval → per-DOF features 无额外价值，启用备选 framing\\n\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。\\n   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static\\n   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI\\n\\n~~3. **ACR-VLA 与 training-time 方法正交互补** — D022 移除: 11 天内无法获取 SRPO checkpoint + 重训 CRM + eval。留给扩展版本。~~\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。\\n- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃跨维度协方差结构，且无法合成优于任何单个样本的动作；SC-VLA 通过 sparse world imagination + residual RL 在线纠正，但需要任务级 RL 训练且无统计保证，纠正作用在全局 action vector 上无维度选择性；VLA-Pilot 用 MLLM 做开放世界 action scoring + evolutionary search，推理延迟 2.41s/step 且依赖启发式评分无 calibrated confidence。Training-time 方面，ACoT-VLA 通过 action chain-of-thought 达到 LIBERO-Plus 84.1% SOTA，但属于静态训练方法，部署后无法在线适应分布偏移。所有现有方法均未将 per-DOF conformal statistics 作为 learned correction 的输入特征。\\n- **Our angle**: 第一个将多元 conformal 统计量作为学习型校正模块直接输入特征的方法。关键 insight 是 per-DOF conformal 特征编码\\\"哪些维度不确定+跨维度协方差\\\"，使 CRM 能做维度选择性校正。\\n- **Headline result template**: \\\"On LIBERO, ACR-VLA's uncertainty-conditioned sample-then-refine pipeline (K=10 conformal selection + learned CRM correction) improves SmolVLA success by +X pp on spatial and +Y pp on object tasks — with CRM correction contributing Z pp beyond sample selection alone, and correction magnitude control proving critical for closed-loop stability.\\\"\\n\\n## Competitive Landscape\\n\\n### ReconVLA — 最直接竞品\\nPost-hoc conformal prediction on frozen VLA（理念最接近 ACR-VLA）。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\n\\n**关键差异**：(1) Scalar CQR aggregation 丢失维度信息，无法区分 \\\"哪个关节不确定\\\"；(2) Sample selection 而非 learned correction——当 K 个样本都不好时 selection 失效；(3) Static calibration set 不做在线适应，distribution shift 下 coverage 退化。ACR-VLA 在 UQ 粒度（40D vs scalar）、纠正策略（CRM synthesis vs selection）、在线适应（ACI+COC vs static）三个维度均更进一步。\\n\\n### SC-VLA — Inference-time RL refinement\\nSparse World Imagination (SPI) + Online Action Refinement (OAR)。在 VLA backbone 上附加辅助预测头预测任务进度和未来轨迹趋势，构建 endogenous reward 驱动 residual RL 在线调整动作。ManiSkill 平均 86%，+9% SR。\\n\\n**关键差异**：(1) 需要任务级 RL 训练（residual policy + auxiliary heads），非 plug-and-play；(2) 无统计保证和不确定性量化；(3) Residual 作用在整个 action vector 上，无维度选择性；(4) 未在 LIBERO-Plus 评估。ACR-VLA 的 SampleConsensus baseline 近似模拟此方法的 sample consensus 思路。\\n\\n### VLA-Pilot — MLLM-guided steering\\nMLLM verifier + evolutionary diffusion optimizer，三阶段 inference-time steering。利用 VLM 开放世界推理能力做 action scoring。OOD 场景成功率 0.50 vs baseline 0.12-0.19。\\n\\n**关键差异**：(1) 推理延迟 2.41s/step，不适合实时控制；(2) 依赖 MLLM 质量，scoring 为启发式方法无 calibrated confidence；(3) 无统计保证；(4) 未在 LIBERO 标准 benchmark 评估。优势在 zero-shot OOD 泛化（靠 MLLM 开放世界知识）。\\n\\n### ACoT-VLA — Training-time SOTA (CVPR 2026)\\nAction Chain-of-Thought：EAR (Explicit Action Reasoner) 生成粗粒度参考轨迹 + IAR (Implicit Action Reasoner) 提取 latent action priors，联合训练引导 action head。LIBERO 98.5%，LIBERO-Plus 84.1%（当前 SOTA 之一）。\\n\\n**关键差异**：(1) Training-time 方法，需在目标任务上训练 EAR+IAR；(2) 无不确定性量化，无法识别何时 \\\"不确定\\\"；(3) 静态模型，部署后不在线适应。**与 ACR-VLA 正交互补**——ACoT 增强 VLA 基础能力，ACR-VLA 在其之上提供 inference-time statistical safety net。\\n\\n### ACR-VLA 差异化定位\\n唯一将 multivariate conformal statistics（per-DOF intervals + ellipsoid volume + cross-DOF covariance structure）作为 learned correction module (CRM) 直接输入特征的方法。核心差异化组合：**Per-DOF statistical guarantees + Learned dimension-selective correction + Online coverage adaptation**——三者缺一不可，现有方法均未同时具备。\\n\\n## Anticipated Reviewer Concerns\\n1. **K=10 covariance 估计可靠性** (p/n=0.6): Ledoit-Wolf shrinkage 是标准方案，MVP 已验证 K=10 estimated 仍有效（衰减 ~15pp 但仍显著）。K sensitivity sweep (K=5,10,15,20) 作为 P1 实验。\\n2. **CRM ~250K 参数表达力**: 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。\\n3. **Synthetic augmentation 覆盖不全** (layout/language 不可覆盖): Honest limitation。ACI 在线适应部分弥补。per-perturbation breakdown 透明呈现。held-out perturbation test (P1) 隔离 conformal features vs augmentation memorization。\\n4. **仿真 only**: CoRL 接受 sim-only，LIBERO-Plus 是 recognized benchmark。\\n5. **DiU 的 single-pass uncertainty 更高效**: DiU 捕获 aleatoric，CGS 捕获 epistemic（分布偏移时升高）。A7 ablation 验证区分。\\n6. **[Dream 新增] 缺外部 baseline 对比**: 必须加 ReconVLA (scalar CP + sample selection) 作为实验 baseline。A3 ablation 近似 A2C2 但需明确说明区别。\\n7. **[Dream 新增] \\\"Conformal\\\" 标签可能误导**: CRM 输出无 formal coverage guarantee。论文需明确说明 CP 用作 feature extractor 而非输出保证。\\n8. **[Dream 新增] per-DOF 优势可能modest**: median dream 显示 per-DOF vs scalar 仅 +2.1%。若真实实验确认此趋势，需 reframe：强调 \\\"conformal-feature-conditioned correction\\\" 整体优势（residual + uncertainty 共同贡献），而非仅 per-DOF vs scalar。\\n\\n## Framing 备选策略 (D022 细化, Reviewer 审查后修补)\\n\\n**四路 ablation 排序预测** (val_loss 顺序: obs_only 0.0165 < perdof 0.0358 ≈ scalar_unc 0.0374):\\n- 训练 loss 预测: obs_only > scalar_unc ≈ perdof > argmin_only\\n- 但 closed-loop eval 可能翻转（conformal features 在分布偏移下的 epistemic value）\\n\\n### Scenario A: perdof > obs_only (最佳)\\nClaim 1 主+子 claim 均成立。Story: \\\"Per-DOF conformal features encode dimension-specific uncertainty that observation features alone cannot capture; this enables superior learned correction under distribution shift — despite worse training loss, conformal features' real-time epistemic signal proves critical in closed-loop deployment.\\\"\\n- Core Insight 不变\\n- 这是最强 narrative：training loss 反直觉但 eval 翻转 = compelling story\\n- scalar_unc 预期位置: ≈ perdof (相似 val_loss) 或略低 → per-DOF vs scalar 差异化成立\\n\\n### Scenario B: perdof ≈ obs_only ≈ scalar_unc (任意两者差 <5pp)\\n主 claim 成立（CRM correction 有价值），子 claim 弱化。Story: \\\"Uncertainty-conditioned learned correction (sample-then-refine) significantly outperforms pure sample selection. The specific form of uncertainty features (per-DOF, scalar, or observation-only) matters less than the correction mechanism itself.\\\"\\n- Core Insight 调整: 去掉 \\\"fundamentally richer than scalar\\\"，改为 \\\"enables principled learned correction\\\"\\n- Per-DOF 作为 Claim 2 (ACI+COC) 的必要组件保留\\n- **Magnitude control as empirical contribution**: 升级为独立发现 (Section: \\\"Critical Role of Correction Magnitude\\\")\\n\\n### Scenario C: obs_only > perdof AND obs_only > scalar_unc (>5pp)\\n主 claim 仍成立（CRM correction 有价值），子 claim 不成立。Story: \\\"Observation-conditioned residual correction is the key contribution. Conformal features as direct CRM input offer no additional value over observation features, but remain valuable for (a) sample selection quality, (b) online coverage monitoring (ACI+COC).\\\"\\n- Core Insight 需重写: \\\"Lightweight learned residual correction on selected VLA samples significantly improves robustness\\\"\\n- Per-DOF features 在 ablation table 如实呈现为 negative result\\n- **特殊子情况**: 如果 scalar_unc > perdof 但 scalar_unc < obs_only → conformal 特征形式无关紧要\\n\\n### 共性硬证据（所有 scenario 均可用）\\n- CRM correction vs argmin-only: +9.6pp (interim, if holds)\\n- Selection + Correction vs baseline: +20.5pp (interim)\\n- Magnitude control discovery: norm=1.42 → 0%, norm=0.1 → 52.5% (novel empirical finding, 可独立成 contribution section)\\n- ACI+COC online adaptation (Claim 2, independent of Claim 1 outcome)\\n\\n### Kill criteria (Reviewer 校准后)\\n- **内部 kill (停止投入)**: CRM correction vs argmin-only < 3pp on ANY benchmark\\n- **论文 claim 门槛**: ≥5pp + Fisher exact test p<0.05 on EACH benchmark independently\\n- **3-5pp 灰区**: claim 技术上存活但论文说服力不足 (\\\"zombie claim\\\")，需要加 n_rollouts 或加 benchmark 提升统计力\\n- **跨 benchmark 逻辑**: ANY benchmark < 3pp → 该 benchmark 降级; BOTH < 3pp → claim killed\\n\", \"total_chars\": 9063, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017zTx48DTMeMk4otDv3XGD2`</summary>

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
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "3884f1c1-a01d-4526-8ce7-9c6cd52d0695",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWmRckJaa51NeyW8vXdMFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 23282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1342
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

_source line 11 · 2026-05-15T04:46:20.885Z_

<details><summary>↩ Tool result · `toolu_017zTx48DTMeMk4otDv3XGD2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 03:08 UTC | 更新原因: D023 drop Claim 2, D024 kill v4-default-r3, D025 suspend D019 conclusion, spatial mid-results update\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 2c — Spatial 4-way Ablation (等全 10 task) + Object 4-way 并行铺开\\n- **MVP**: PASS\\n- **Claim 2 (ACI/COC) 已放弃 (D023)**: ACI 需 expert_action，test-time 不可用，11 天内重设计风险过高。CoRL 论文聚焦单 Claim (CRM correction)\\n- **D019 \\\"52.5%\\\" 已失效 (D025)**: perdof 实际 42%@5/10 tasks，仅 +4.5pp over argmin (噪声水平)。obs_only 57.5%@4 tasks 暂时领先。**必须等全 10 task 完成再做 framing 裁决**\\n- **Baselines 锁定**: spatial 30% (K=1), VLA-mean 31% (K=10), object 13% (K=1)\\n\\n## Spatial Eval 进行中（bjb1-18228）\\n\\n| 实验 | Mode | Tasks | 当前 SR | ETA |\\n|------|------|-------|---------|-----|\\n| obs-only-r2 | crm_obs_only, norm=0.1 | 4/10 | **57.5%** | ~7h |\\n| v4-small (perdof) | acr_vla, norm=0.1 | 5/10 | 42.0% | ~6h |\\n| argmin-only | reconvla | 8/10 | 37.5% | ~2h |\\n| v4-scalar | crm_scalar, norm=0.1 | 2/10 | 80%* (easy tasks only) | ~6h |\\n\\n## Object Eval 进行中（bjb1-32546, 6/6 GPU 满载）\\n\\n| GPU | 实验 | Mode | 状态 |\\n|-----|------|------|------|\\n| cuda:0 | reconvla-object | reconvla, K=10 | RUNNING (no results yet) |\\n| cuda:1 | acr-object-v4-perdof | crm_perdof, norm=0.1 | RUNNING |\\n| cuda:2 | acr-object-v4-obs-only | crm_obs_only, norm=0.1 | RUNNING |\\n| cuda:3 | acr-object-v4-scalar | crm_scalar, norm=0.1 | RUNNING |\\n| cuda:4 | vla-only-object | vla_only, K=1 | RUNNING (unregistered) |\\n| cuda:5 | vla-mean-object | vla_only mean, K=10 | RUNNING (unregistered) |\\n\\n## 其他服务器\\n\\n| 服务器 | GPU | 状态 |\\n|--------|-----|------|\\n| bjb2-40593 (1×4090D) | cuda:0 | reconvla-object n=20 (v4-default-r3 待 kill, D024) |\\n| bjb2-28827 (6×4090) | 全空闲 | SmolVLM2+CRM+code 已就绪，config 已修复，待重新提交实验 |\\n\\n## 近期任务\\n- [ ] 等 bjb1-18228 spatial 全 10 task 完成 → Claim 1 framing 裁决\\n- [ ] Kill bjb2-40593 v4-default-r3 (D024)\\n- [ ] bjb2-28827 重新提交实验（config 已修复）\\n- [ ] 注册 bjb1-32546 上两个未注册实验 (vla-only, vla-mean)\\n- [ ] 确认 crm_perdof vs acr_vla mode 等价性\\n- [ ] Object benchmark 全 10 task 完成后汇总\\n- [ ] Magnitude sweep: norm ∈ {0.03, 0.05, 0.2, 0.3}\\n- [ ] Paper Agent 启动 CoRL 初稿（等 spatial 结果出来后）\\n\\n## GPU 资源\\n- **bjb1-18228** (4× RTX 4090): 全部在跑 spatial eval\\n- **bjb2-40593** (1× RTX 4090 D): reconvla-object n=20 + 待 kill 实验\\n- **bjb1-32546** (6× RTX 4090): 全满载 object eval\\n- **bjb2-28827** (6× RTX 4090): 空闲，环境就绪待部署\\n- **总计**: 17 张 4090\\n\\n## 关键路径\\n1. Spatial eval 完成 → Claim 1 framing 裁决 (预计 6-9h)\\n2. Object eval 完成 → cross-benchmark validation (预计 ~2h after spatial)\\n3. bjb2-28827 部署 → magnitude sweep / 额外 ablation\\n4. Paper Agent 初稿 (spatial+object 结果出来后启动)\\n5. Abstract 提交 (May 26)\\n\\n## 风险\\n- obs_only ≥ perdof 趋势持续 → Claim 1 需 Scenario B framing（\\\"correction helps, per-DOF is one valid feature set\\\"）\\n- perdof ≈ argmin → CRM correction 增益可能统计不显著\\n- 11 天 DDL 紧张，单 claim 论文需要极强的实验证据\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D025 | 2026-05-15 | D025: D019 \\\"52.5% perdof\\\" claim invalidated — actu | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-argmin-only-spatial |\\n| D024 | 2026-05-15 | D024: Kill bjb2-40593 v4-default-r3 (norm=1.42) —  | eval-acr-spatial-v4-default-r3 |\\n| D023 | 2026-05-15 | D023: Drop Claim 2 (ACI/COC) for CoRL — focus sing | plan_005, plan_006, plan_007 |\\n| D022 | 2026-05-15 | D022: CoRL 论文降为 2 Claims (drop Claim 3 SRPO stacki | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2 |\\n| D021 | 2026-05-15 | D021: 撤销 D011，重新瞄准 CoRL 2026（abstract DDL ~May 26） | — |\\n| D020 | 2026-05-14 | D020: obs_only val_loss (0.0165) 54% better than p | crm-train-v3-norm-obs-only, crm-train-v3-norm-scalar-unc, crm-train-v3-norm, eval-acr-spatial-v4-default |\\n| D019 | 2026-05-14 | D019: Normalization alone insufficient — magnitude | eval-acr-spatial-v4-default, eval-acr-spatial-v4-small, eval-argmin-only-spatial, eval-tiny-correction-spatial, eval-vla-mean-spatial |\\n| D018 | 2026-05-14 | D018: CRM 失败根因确认为输入未归一化（1500x scale 差异），批准 normali | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3 |\\n| D017 | 2026-05-14 | D017: CRM correction 全面拖累 baseline — kill 两路 ablat | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3, eval-vla-mean-spatial |\\n| D016 | 2026-05-14 | D016: CRM 训练/评估 state 维度不匹配 bug 确认，批准四项修复 + 重跑 pip | eval-acr-spatial-v2, eval-k5-spatial, eval-scalar-unc-spatial |\\n\\n\\n\", \"total_chars\": 4538, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "d2f75f73-e554-478c-9edb-5179d27326f7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\\\", \\\"content\\\": \\\"# acr-vla-conformal-refinement — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-15 03:08 UTC | 更新原因: D023 drop Claim 2, D024 kill v4-default-r3, D025 suspend D019 conclusion, spatial mid-results update\\\\n\\\\n## 核心方向\\\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\\\n\\\\n## 投稿目标\\\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Phase 2c — Spatial 4-way Ablation (等全 10 task) + Object 4-way 并行铺开\\\\n- **MVP**: PASS\\\\n- **Claim 2 (ACI/COC) 已放弃 (D023)**: ACI 需 expert_action，test-time 不可用，11 天内重设计风险过高。CoRL 论文聚焦单 Claim (CRM correction)\\\\n- **D019 \\\\\\\"52.5%\\\\\\\" 已失效 (D025)**: perdof 实际 42%@5/10 tasks，仅 +4.5pp over argmin (噪声水平)。obs_only 57.5%@4 tasks 暂时领先。**必须等全 10 task 完成再做 framing 裁决**\\\\n- **Baselines 锁定**: spatial 30% (K=1), VLA-mean 31% (K=10), object 13% (K=1)\\\\n\\\\n## Spatial Eval 进行中（bjb1-18228）\\\\n\\\\n| 实验 | Mode | Tasks | 当前 SR | ETA |\\\\n|------|------|-------|---------|-----|\\\\n| obs-only-r2 | crm_obs_only, norm=0.1 | 4/10 | **57.5%** | ~7h |\\\\n| v4-small (perdof) | acr_vla, norm=0.1 | 5/10 | 42.0% | ~6h |\\\\n| argmin-only | reconvla | 8/10 | 37.5% | ~2h |\\\\n| v4-scalar | crm_scalar, norm=0.1 | 2/10 | 80%* (easy tasks only) | ~6h |\\\\n\\\\n## Object Eval 进行中（bjb1-32546, 6/6 GPU 满载）\\\\n\\\\n| GPU | 实验 | Mode | 状态 |\\\\n|-----|------|------|------|\\\\n| cuda:0 | reconvla-object | reconvla, K=10 | RUNNING (no results yet) |\\\\n| cuda:1 | acr-object-v4-perdof | crm_perdof, norm=0.1 | RUNNING |\\\\n| cuda:2 | acr-object-v4-obs-only | crm_obs_only, norm=0.1 | RUNNING |\\\\n| cuda:3 | acr-object-v4-scalar | crm_scalar, norm=0.1 | RUNNING |\\\\n| cuda:4 | vla-only-object | vla_only, K=1 | RUNNING (unregistered) |\\\\n| cuda:5 | vla-mean-object | vla_only mean, K=10 | RUNNING (unregistered) |\\\\n\\\\n## 其他服务器\\\\n\\\\n| 服务器 | GPU | 状态 |\\\\n|--------|-----|------|\\\\n| bjb2-40593 (1×4090D) | cuda:0 | reconvla-object n=20 (v4-default-r3 待 kill, D024) |\\\\n| bjb2-28827 (6×4090) | 全空闲 | SmolVLM2+CRM+code 已就绪，config 已修复，待重新提交实验 |\\\\n\\\\n## 近期任务\\\\n- [ ] 等 bjb1-18228 spatial 全 10 task 完成 → Claim 1 framing 裁决\\\\n- [ ] Kill bjb2-40593 v4-default-r3 (D024)\\\\n- [ ] bjb2-28827 重新提交实验（config 已修复）\\\\n- [ ] 注册 bjb1-32546 上两个未注册实验 (vla-only, vla-mean)\\\\n- [ ] 确认 crm_perdof vs acr_vla mode 等价性\\\\n- [ ] Object benchmark 全 10 task 完成后汇总\\\\n- [ ] Magnitude sweep: norm ∈ {0.03, 0.05, 0.2, 0.3}\\\\n- [ ] Paper Agent 启动 CoRL 初稿（等 spatial 结果出来后）\\\\n\\\\n## GPU 资源\\\\n- **bjb1-18228** (4× RTX 4090): 全部在跑 spatial eval\\\\n- **bjb2-40593** (1× RTX 4090 D): reconvla-object n=20 + 待 kill 实验\\\\n- **bjb1-32546** (6× RTX 4090): 全满载 object eval\\\\n- **bjb2-28827** (6× RTX 4090): 空闲，环境就绪待部署\\\\n- **总计**: 17 张 4090\\\\n\\\\n## 关键路径\\\\n1. Spatial eval 完成 → Claim 1 framing 裁决 (预计 6-9h)\\\\n2. Object eval 完成 → cross-benchmark validation (预计 ~2h after spatial)\\\\n3. bjb2-28827 部署 → magnitude sweep / 额外 ablation\\\\n4. Paper Agent 初稿 (spatial+object 结果出来后启动)\\\\n5. Abstract 提交 (May 26)\\\\n\\\\n## 风险\\\\n- obs_only ≥ perdof 趋势持续 → Claim 1 需 Scenario B framing（\\\\\\\"correction helps, per-DOF is one valid feature set\\\\\\\"）\\\\n- perdof ≈ argmin → CRM correction 增益可能统计不显著\\\\n- 11 天 DDL 紧张，单 claim 论文需要极强的实验证据\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D025 | 2026-05-15 | D025: D019 \\\\\\\"52.5% perdof\\\\\\\" claim invalidated — actu | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-argmin-only-spatial |\\\\n| D024 | 2026-05-15 | D024: Kill bjb2-40593 v4-default-r3 (norm=1.42) —  | eval-acr-spatial-v4-default-r3 |\\\\n| D023 | 2026-05-15 | D023: Drop Claim 2 (ACI/COC) for CoRL — focus sing | plan_005, plan_006, plan_007 |\\\\n| D022 | 2026-05-15 | D022: CoRL 论文降为 2 Claims (drop Claim 3 SRPO stacki | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2 |\\\\n| D021 | 2026-05-15 | D021: 撤销 D011，重新瞄准 CoRL 2026（abstract DDL ~May 26） | — |\\\\n| D020 | 2026-05-14 | D020: obs_only val_loss (0.0165) 54% better than p | crm-train-v3-norm-obs-only, crm-train-v3-norm-scalar-unc, crm-train-v3-norm, eval-acr-spatial-v4-default |\\\\n| D019 | 2026-05-14 | D019: Normalization alone insufficient — magnitude | eval-acr-spatial-v4-default, eval-acr-spatial-v4-small, eval-argmin-only-spatial, eval-tiny-correction-spatial, eval-vla-mean-spatial |\\\\n| D018 | 2026-05-14 | D018: CRM 失败根因确认为输入未归一化（1500x scale 差异），批准 normali | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3 |\\\\n| D017 | 2026-05-14 | D017: CRM correction 全面拖累 baseline — kill 两路 ablat | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3, eval-vla-mean-spatial |\\\\n| D016 | 2026-05-14 | D016: CRM 训练/评估 state 维度不匹配 bug 确认，批准四项修复 + 重跑 pip | eval-acr-spatial-v2, eval-k5-spatial, eval-scalar-unc-spatial |\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 4538, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 03:08 UTC | 更新原因: D023 drop Claim 2, D024 kill v4-default-r3, D025 suspend D019 conclusion, spatial mid-results update\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 2c — Spatial 4-way Ablation (等全 10 task) + Object 4-way 并行铺开\\n- **MVP**: PASS\\n- **Claim 2 (ACI/COC) 已放弃 (D023)**: ACI 需 expert_action，test-time 不可用，11 天内重设计风险过高。CoRL 论文聚焦单 Claim (CRM correction)\\n- **D019 \\\"52.5%\\\" 已失效 (D025)**: perdof 实际 42%@5/10 tasks，仅 +4.5pp over argmin (噪声水平)。obs_only 57.5%@4 tasks 暂时领先。**必须等全 10 task 完成再做 framing 裁决**\\n- **Baselines 锁定**: spatial 30% (K=1), VLA-mean 31% (K=10), object 13% (K=1)\\n\\n## Spatial Eval 进行中（bjb1-18228）\\n\\n| 实验 | Mode | Tasks | 当前 SR | ETA |\\n|------|------|-------|---------|-----|\\n| obs-only-r2 | crm_obs_only, norm=0.1 | 4/10 | **57.5%** | ~7h |\\n| v4-small (perdof) | acr_vla, norm=0.1 | 5/10 | 42.0% | ~6h |\\n| argmin-only | reconvla | 8/10 | 37.5% | ~2h |\\n| v4-scalar | crm_scalar, norm=0.1 | 2/10 | 80%* (easy tasks only) | ~6h |\\n\\n## Object Eval 进行中（bjb1-32546, 6/6 GPU 满载）\\n\\n| GPU | 实验 | Mode | 状态 |\\n|-----|------|------|------|\\n| cuda:0 | reconvla-object | reconvla, K=10 | RUNNING (no results yet) |\\n| cuda:1 | acr-object-v4-perdof | crm_perdof, norm=0.1 | RUNNING |\\n| cuda:2 | acr-object-v4-obs-only | crm_obs_only, norm=0.1 | RUNNING |\\n| cuda:3 | acr-object-v4-scalar | crm_scalar, norm=0.1 | RUNNING |\\n| cuda:4 | vla-only-object | vla_only, K=1 | RUNNING (unregistered) |\\n| cuda:5 | vla-mean-object | vla_only mean, K=10 | RUNNING (unregistered) |\\n\\n## 其他服务器\\n\\n| 服务器 | GPU | 状态 |\\n|--------|-----|------|\\n| bjb2-40593 (1×4090D) | cuda:0 | reconvla-object n=20 (v4-default-r3 待 kill, D024) |\\n| bjb2-28827 (6×4090) | 全空闲 | SmolVLM2+CRM+code 已就绪，config 已修复，待重新提交实验 |\\n\\n## 近期任务\\n- [ ] 等 bjb1-18228 spatial 全 10 task 完成 → Claim 1 framing 裁决\\n- [ ] Kill bjb2-40593 v4-default-r3 (D024)\\n- [ ] bjb2-28827 重新提交实验（config 已修复）\\n- [ ] 注册 bjb1-32546 上两个未注册实验 (vla-only, vla-mean)\\n- [ ] 确认 crm_perdof vs acr_vla mode 等价性\\n- [ ] Object benchmark 全 10 task 完成后汇总\\n- [ ] Magnitude sweep: norm ∈ {0.03, 0.05, 0.2, 0.3}\\n- [ ] Paper Agent 启动 CoRL 初稿（等 spatial 结果出来后）\\n\\n## GPU 资源\\n- **bjb1-18228** (4× RTX 4090): 全部在跑 spatial eval\\n- **bjb2-40593** (1× RTX 4090 D): reconvla-object n=20 + 待 kill 实验\\n- **bjb1-32546** (6× RTX 4090): 全满载 object eval\\n- **bjb2-28827** (6× RTX 4090): 空闲，环境就绪待部署\\n- **总计**: 17 张 4090\\n\\n## 关键路径\\n1. Spatial eval 完成 → Claim 1 framing 裁决 (预计 6-9h)\\n2. Object eval 完成 → cross-benchmark validation (预计 ~2h after spatial)\\n3. bjb2-28827 部署 → magnitude sweep / 额外 ablation\\n4. Paper Agent 初稿 (spatial+object 结果出来后启动)\\n5. Abstract 提交 (May 26)\\n\\n## 风险\\n- obs_only ≥ perdof 趋势持续 → Claim 1 需 Scenario B framing（\\\"correction helps, per-DOF is one valid feature set\\\"）\\n- perdof ≈ argmin → CRM correction 增益可能统计不显著\\n- 11 天 DDL 紧张，单 claim 论文需要极强的实验证据\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D025 | 2026-05-15 | D025: D019 \\\"52.5% perdof\\\" claim invalidated — actu | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2, eval-argmin-only-spatial |\\n| D024 | 2026-05-15 | D024: Kill bjb2-40593 v4-default-r3 (norm=1.42) —  | eval-acr-spatial-v4-default-r3 |\\n| D023 | 2026-05-15 | D023: Drop Claim 2 (ACI/COC) for CoRL — focus sing | plan_005, plan_006, plan_007 |\\n| D022 | 2026-05-15 | D022: CoRL 论文降为 2 Claims (drop Claim 3 SRPO stacki | eval-acr-spatial-v4-small, eval-acr-spatial-v4-obs-only-r2 |\\n| D021 | 2026-05-15 | D021: 撤销 D011，重新瞄准 CoRL 2026（abstract DDL ~May 26） | — |\\n| D020 | 2026-05-14 | D020: obs_only val_loss (0.0165) 54% better than p | crm-train-v3-norm-obs-only, crm-train-v3-norm-scalar-unc, crm-train-v3-norm, eval-acr-spatial-v4-default |\\n| D019 | 2026-05-14 | D019: Normalization alone insufficient — magnitude | eval-acr-spatial-v4-default, eval-acr-spatial-v4-small, eval-argmin-only-spatial, eval-tiny-correction-spatial, eval-vla-mean-spatial |\\n| D018 | 2026-05-14 | D018: CRM 失败根因确认为输入未归一化（1500x scale 差异），批准 normali | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3 |\\n| D017 | 2026-05-14 | D017: CRM correction 全面拖累 baseline — kill 两路 ablat | eval-acr-spatial-v3, eval-scalar-unc-spatial-v2, eval-obs-only-spatial-v3, eval-vla-mean-spatial |\\n| D016 | 2026-05-14 | D016: CRM 训练/评估 state 维度不匹配 bug 确认，批准四项修复 + 重跑 pip | eval-acr-spatial-v2, eval-k5-spatial, eval-scalar-unc-spatial |\\n\\n\\n\", \"total_chars\": 4538, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TEYiLs3qmaRVLwJDWJ8Tnu`</summary>

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
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "40778749-bf2c-454b-a603-274f07e73197",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWmRckJaa51NeyW8vXdMFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 23282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1342
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

_source line 13 · 2026-05-15T04:46:21.239Z_

<details><summary>↩ Tool result · `toolu_01TEYiLs3qmaRVLwJDWJ8Tnu`</summary>

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
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "2cc31927-f679-4a2e-b22f-e0a1a60b8b84",
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

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have all three source files. Let me synthesize the information and write the analysis memo. Let me organize the key facts:

**Current data (from task description + ROADMAP):**
- VLA baselines: ~30-31% (K=1: 30%, VLA-mean K=10: 31%)
- argmin-only (no CRM): ~36.7% → updated to 37.5% @8/10 tasks
- perdof CRM: ~42.0% @5/10 tasks (was 42.9% in task, but ROADMAP says 42.0%)


- obs_only CRM: 57.5% @4/10 tasks (was 40.0% in task, but ROADMAP says 57.5%)
- scalar CRM: 80%* @2/10 tasks (easy tasks only, unreliable)

I notice the ROADMAP has more recent numbers than the task description, so I'll prioritize those values for accuracy.

Now I'm cross-referencing the baseline metrics from the paper framing document to see how these CRM variants compare against the foundational approaches.

The core claim is that CRM correction strengthens VLA robustness, with per-DOF features outperforming both observation-only and scalar approaches across three defined scenarios. I've already dropped the ACI/COC and SRPO stacking claims, so I'm focusing on this single direction. The ROADMAP data shows obs-only actually leading at 57.5% right now, which contradicts the per-DOF superiority assumption—this aligns with Scenario C, though I need results from all 10 tasks to confirm. For positioning against related work, ReconVLA with its scalar correction and sample selection strategy is the closest competitor, along with SC-VLA's residual RL approach and VLA-Pilot's MLLM-guided steering.

Now I'm ready to draft the analysis memo.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "f0f33c24-41eb-4615-b5b5-9d1473129cad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DsubASpBaZaQJh4oQTXQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18816,
      "cache_read_input_tokens": 24624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18816
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

ROADMAP 数据比任务描述更新（2026-05-15 03:08 UTC），存在差异。以 ROADMAP 数据为准撰写分析备忘录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "7ef0950b-5a93-4377-a82b-76e5c351afc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DsubASpBaZaQJh4oQTXQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18816,
      "cache_read_input_tokens": 24624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18816
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Tnco3EMBwBn929UNCvVSEd`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/",
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
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "b8ef4af1-a32f-4d5f-8a0b-3f5c38f09fce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DsubASpBaZaQJh4oQTXQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18816,
      "cache_read_input_tokens": 24624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18816
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

_source line 17 · 2026-05-15T04:46:46.584Z_

<details><summary>↩ Tool result · `toolu_01Tnco3EMBwBn929UNCvVSEd`</summary>

```text
_project
ablation_eval_commands.md
competitive_analysis_20260515.md
competitor_analysis.md
correction_degradation_literature.md
crm-train-v2-k5
crm_bug_audit.md
diag-eval-v6-batch-failure.md
dream_reports
eval-reconvla-spatial-v1-diag.md
fix_plan_code_sketch.md
lerobot-pipeline-alignment.md
libero-smolvla-env-report.md
manifest.yaml
method_section_draft.tex
mvp-point-reaching
object_eval_commands.md
pipeline-dimension-verification.md
precompute-k5
precompute-k5-analysis.md
reconvla-comparison-report.md
report_eval_progress.md
report_running_status.md
smolvla-libero-finetune-survey.md
smolvla_wrapper_fixed.py
spatial_comparison_template.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "49ef55d8-6932-454d-87ee-3af4b97c666b",
  "tool_use_result": {
    "stdout": "_project\nablation_eval_commands.md\ncompetitive_analysis_20260515.md\ncompetitor_analysis.md\ncorrection_degradation_literature.md\ncrm-train-v2-k5\ncrm_bug_audit.md\ndiag-eval-v6-batch-failure.md\ndream_reports\neval-reconvla-spatial-v1-diag.md\nfix_plan_code_sketch.md\nlerobot-pipeline-alignment.md\nlibero-smolvla-env-report.md\nmanifest.yaml\nmethod_section_draft.tex\nmvp-point-reaching\nobject_eval_commands.md\npipeline-dimension-verification.md\nprecompute-k5\nprecompute-k5-analysis.md\nreconvla-comparison-report.md\nreport_eval_progress.md\nreport_running_status.md\nsmolvla-libero-finetune-survey.md\nsmolvla_wrapper_fixed.py\nspatial_comparison_template.md",
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

_source line 18_

<details open><summary>🔧 Tool call — Write · `toolu_01Jw3MhTTBBXKcG1GQQ1YRnF`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_analysis_prep.md",
  "content": "# Spatial Ablation Analysis & Paper Narrative Preparation\n\n> 生成时间: 2026-05-15 | 状态: 分析备忘录（等待全 10 task 完成后裁决）\n\n## 1. 当前数据快照\n\n### Spatial Benchmark（ROADMAP 2026-05-15 03:08 UTC）\n\n| 实验 | Mode | Tasks 完成 | 当前 SR | 来源 |\n|------|------|-----------|---------|------|\n| VLA baseline (K=1) | vla_only | locked | **30%** | ROADMAP baselines |\n| VLA-mean (K=10) | vla_only mean | locked | **31%** | ROADMAP baselines |\n| argmin-only | reconvla | 8/10 | **37.5%** | ROADMAP spatial eval |\n| perdof CRM | acr_vla, norm=0.1 | 5/10 | **42.0%** | ROADMAP spatial eval (v4-small) |\n| obs_only CRM | crm_obs_only, norm=0.1 | 4/10 | **57.5%** | ROADMAP spatial eval (obs-only-r2) |\n| scalar CRM | crm_scalar, norm=0.1 | 2/10 | **80%*** | ROADMAP spatial eval (*easy tasks only) |\n\n**注意**: 任务描述中的数字（perdof 42.9%, obs_only 40.0%, scalar 56.7%@3 tasks）与 ROADMAP 不一致。以 ROADMAP 为准，但两者均为中间结果，任何中间排序均可能在剩余 tasks 翻转。\n\n### 关键增量\n\n| 对比 | 增量 | 统计可信度 |\n|------|------|-----------|\n| CRM (any) vs argmin-only | +4.5pp (perdof) 至 +20pp (obs_only) | 低: 4-5/10 tasks |\n| argmin-only vs VLA baseline | +7.5pp | 中: 8/10 tasks |\n| 全 pipeline vs VLA baseline | +12pp (perdof) 至 +27.5pp (obs_only) | 低: 不同 task counts |\n\n### 数据可靠性警告\n- **obs_only** 仅 4/10 tasks，当前领先可能因 task selection bias 翻转\n- **scalar** 仅 2/10 tasks 且均为 easy tasks，80% 完全不可信\n- **perdof** 5/10 tasks，D025 已将 D019 \"52.5%\" claim 标记为失效\n- 所有 CRM variant 排序必须等全 10 tasks 完成\n\n---\n\n## 2. 三种 Narrative 分析\n\n### Scenario A: perdof > obs_only（per-DOF story）\n\n**触发条件**: 全 10 task 后 perdof SR > obs_only SR 且差 ≥5pp\n\n**可能性评估**: **低**。当前 obs_only (57.5%@4) 大幅领先 perdof (42.0%@5)。需要剩余 tasks 中 obs_only 大幅下滑且 perdof 追上。训练 loss 也支持 obs_only（val_loss 0.0165 vs perdof 0.0358，见 D020）。\n\n**Narrative**: \"Per-DOF conformal features encode dimension-specific uncertainty that observation features cannot capture. Despite worse training loss, conformal features' epistemic signal proves critical under distribution shift in closed-loop deployment.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | 开门见山：scalar UQ 丢失维度信息 → per-DOF conformal features 是解决方案。Problem 聚焦 \"information loss in scalar aggregation\" |\n| **Method** | CGS multivariate CP + per-DOF interval extraction 是核心技术贡献。CRM 架构强调 40D conformal feature vector 的设计。Magnitude control 作为工程发现 |\n| **Results** | 主表: 4-way ablation 展示 perdof > obs_only > scalar ≈ argmin。亮点故事: \"training loss 预测翻转\" (obs_only lower loss but worse eval) = compelling evidence for epistemic value |\n| **Discussion** | 强调 conformal features 在 distribution shift 下的 epistemic value 与 in-distribution training loss 的 divergence。与 ReconVLA scalar CP 对比突出信息增益 |\n\n**风险**: 如果 perdof 仅略优于 obs_only (3-5pp)，统计显著性不足，narrative 说服力弱。\n\n---\n\n### Scenario B: perdof ≈ obs_only ≈ scalar（correction-is-key story）\n\n**触发条件**: 全 10 task 后三种 CRM variant 两两差 <5pp\n\n**可能性评估**: **中**。如果 obs_only 在剩余 tasks 下滑，三者可能收敛到 40-50% 区间。\n\n**Narrative**: \"Learned uncertainty-conditioned correction (sample-then-refine) significantly outperforms pure sample selection. The correction mechanism is the contribution, not the specific feature representation.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | Problem: 现有方法止步于 sample selection (ReconVLA) 或需 RL 训练 (SC-VLA)。Gap: 缺少 lightweight learned correction。Our angle: CRM 作为 plug-and-play correction module |\n| **Method** | CRM 架构设计 + magnitude control 是核心贡献。Per-DOF features 作为 \"one valid feature set\" 呈现，不强调其必要性。重点放在 correction mechanism 设计原则（bounded residual, norm control） |\n| **Results** | 主表: CRM (any variant) vs argmin-only 的增量。Feature ablation 作为次要表 \"CRM is robust to feature choice\"。Magnitude control study (norm sensitivity) 升级为独立 contribution |\n| **Discussion** | \"Correction > selection\" 作为主要 takeaway。与 residual policy learning 文献 (Silver 2018, PLD, TRANSIC) 建立联系。Per-DOF 保留用于 online monitoring (future work) |\n\n**优势**: 这是最稳健的 narrative——只要 CRM vs argmin-only ≥5pp 即可成立。不依赖特定 feature variant 排序。\n**风险**: Contribution novelty 降低——\"learned correction helps\" 不够新颖。需要用 magnitude control discovery 和 CoRL 实验规模补偿。\n\n---\n\n### Scenario C: obs_only > perdof（simpler-is-better / observation-conditioned story）\n\n**触发条件**: 全 10 task 后 obs_only SR > perdof SR 且差 ≥5pp\n\n**可能性评估**: **较高**。当前数据 (57.5% vs 42.0%) + 训练 loss (0.0165 vs 0.0358) 均支持此方向。D025 已预警此趋势。\n\n**Narrative**: \"Observation-conditioned learned residual correction is the key contribution. Conformal features provide no additional value as CRM input over observation features, but remain valuable for sample selection quality and coverage monitoring.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | Problem 保持不变（VLA robustness gap）。Gap: 缺少 inference-time learned correction。Our angle: lightweight observation-conditioned residual correction，不需要额外 UQ features |\n| **Method** | CRM 架构 + magnitude control 是核心。CGS/conformal 降为 \"sample selection module\" 的理论基础，不再是 CRM feature。需要解释 per-DOF features 的 negative result |\n| **Results** | 主表: obs_only CRM vs argmin-only vs baselines。Feature ablation 如实呈现——conformal features 不优于 observation features 作为 honest negative result。Per-DOF 在 sample selection 中的角色仍可报告 |\n| **Discussion** | 解释可能原因: (1) 观测特征已隐含编码 uncertainty 信息 (2) conformal 特征在小 K 下噪声大 (3) CRM 容量足以从观测中学到校正方向。将 per-DOF 定位为 \"future direction: larger K + better calibration\" |\n\n**Core Insight 需重写**: \"Lightweight learned residual correction on selected VLA samples significantly improves robustness. The correction module only needs observation features; structured uncertainty features are not required.\"\n\n**优势**: 实际上简化了 method 和 story——不需要解释复杂的 multivariate CP 管线作为 CRM 输入。\n**风险**: (1) 论文标题 \"ACR-VLA\" 中 \"conformal\" 角色弱化；(2) 与 A2C2 (Sendai 2025) 的差异化缩小——都变成了 \"observation-conditioned residual correction\"；(3) Reviewer 可能质疑 \"你们做了这么复杂的 CP pipeline 结果没用？\"\n\n**子情况 C1**: scalar > perdof 但 scalar < obs_only → conformal feature 形式无关紧要，进一步支持 \"correction mechanism is key\" narrative（hybrid of B+C）\n\n---\n\n## 3. 待完成实验及其对 Narrative 选择的影响\n\n| 实验 | 当前状态 | ETA | 对 narrative 的影响 |\n|------|---------|-----|-------------------|\n| **Spatial 全 10 task** (bjb1-18228) | 4-8/10 tasks | ~6-9h | **决定性**: 全部排序确认后才能选择 A/B/C |\n| **Object benchmark 全 10 task** (bjb1-32546) | 刚开始 | ~数小时 after spatial | **验证性**: cross-benchmark consistency。如果 spatial B 但 object A → narrative 困难 |\n| **Magnitude sweep** (norm ∈ {0.03, 0.05, 0.2, 0.3}) | 未开始 | 待 bjb2-28827 部署 | **补充性**: 强化 magnitude control contribution (所有 scenario 均可用) |\n| **K sensitivity sweep** (K=5,10,15,20) | 未开始 | 待 GPU 释放 | **补充性**: 回应 Reviewer Q1 (K=10 covariance reliability) |\n| **Fisher exact test** | 需全 10 task 数据 | post-eval | **统计性**: 判断增量是否 p<0.05 |\n\n**裁决所需最低数据**: Spatial 全 10 task + Object 全 10 task。两个 benchmark 均显示 CRM vs argmin ≥5pp (p<0.05) 才能安全 claim。\n\n---\n\n## 4. CoRL 8 页单 Claim 论文结构建议\n\n### 推荐结构（CoRL 2026, 8 pages + references）\n\n| 章节 | 页数 | 内容 |\n|------|------|------|\n| **Abstract** | — | 一句 problem, 一句 method (sample-then-refine + CRM), 一句 headline result |\n| **1. Introduction** | 1.0 | Problem (VLA robustness gap) → Existing approaches (selection/RL/MLLM) → Gap (no lightweight learned correction with statistical grounding) → Contribution (CRM + magnitude control + empirical findings) |\n| **2. Related Work** | 0.75 | (a) VLA robustness: training-time (RobustVLA, DiG-Flow, SRPO, ACoT) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2) (b) CP in robotics (c) Residual policy learning |\n| **3. Method** | 2.0 | 3.1 Multi-sample inference + CGS (0.5p) → 3.2 Conformal sample selection (0.5p) → 3.3 CRM architecture + feature variants (0.5p) → 3.4 Magnitude control (0.5p) |\n| **4. Experiments** | 2.5 | 4.1 Setup: LIBERO-Plus spatial+object, SmolVLA backbone, baselines (0.5p) → 4.2 Main results: headline table (0.5p) → 4.3 Feature ablation: 4-way comparison (0.5p) → 4.4 Magnitude sensitivity study (0.5p) → 4.5 Analysis: per-task breakdown, failure modes (0.5p) |\n| **5. Discussion & Limitations** | 0.75 | Sim-only, K=10 overhead, feature choice insights, future directions |\n| **6. Conclusion** | 0.25 | 2-3 sentences |\n| **References** | ~1.5 (不计入) | ~30-35 refs |\n\n### 单 Claim 论文的关键策略\n\n1. **Claim 必须够强**: \"CRM correction ≥5pp over argmin-only on BOTH benchmarks\" 是最低门槛。单 claim 论文缺乏 \"至少有一个 claim 成立\" 的安全网。\n\n2. **Ablation 表做得像 multi-claim**: 4-way feature ablation + magnitude sweep + K sensitivity = 3 个独立分析维度。即使只有一个 claim，实验深度可以补偿。\n\n3. **Magnitude control 升级为独立 contribution**: norm=1.42 → 0% vs norm=0.1 → 42-57.5% 的发现是 novel empirical insight（来源: D019）。这在所有 scenario 下都成立，可作为论文的 \"second punch\"。\n\n4. **Negative result 如实呈现**: 如果 per-DOF 不优于 obs_only (Scenario B/C)，Table 中如实展示比隐藏更好——Reviewer 会欣赏 thorough ablation。\n\n5. **与 ReconVLA 的对比是必须的** (paper_framing.md Reviewer Q6)。argmin-only baseline 已经是 ReconVLA 的近似（conformal selection without correction），但需要在论文中明确声明这一对应关系。\n\n### 各 Scenario 下的标题候选\n\n| Scenario | 标题方向 |\n|----------|---------|\n| A (perdof wins) | \"ACR-VLA: Dimension-Selective Action Correction via Per-DOF Conformal Features\" |\n| B (all similar) | \"Sample-then-Refine: Uncertainty-Conditioned Learned Correction for Robust VLA Deployment\" |\n| C (obs_only wins) | \"Learned Residual Correction Improves VLA Robustness: A Conformal Selection + Observation-Conditioned Refinement Pipeline\" |\n\n---\n\n## 5. 决策依赖与时间线\n\n```\nMay 15 (NOW)\n  ├── Spatial eval running (ETA ~6-9h)\n  ├── Object eval running (ETA ~hours after spatial)\n  └── This memo prepared\n\nMay 16 (Day 2)\n  ├── Spatial 全 10 task 完成 → 初步排序\n  ├── Object 初步结果\n  └── ★ Narrative 初步选择 (A/B/C)\n\nMay 17-19 (Day 3-5)\n  ├── Object 全 10 task 完成\n  ├── Fisher exact test on both benchmarks\n  ├── Magnitude sweep (if GPU available)\n  └── ★ Narrative 最终锁定 + paper_framing.md 更新\n\nMay 20-24 (Day 6-10)\n  ├── Paper writing (8 pages)\n  ├── Figures: main results table, ablation, magnitude curve\n  └── Per-task breakdown analysis\n\nMay 25-26 (Day 11-12)\n  ├── Abstract 提交 (May 26 DDL)\n  └── Continue full paper for Jun 2 DDL\n```\n\n---\n\n## 6. Scenario-Specific 风险矩阵\n\n| 风险 | Scenario A | Scenario B | Scenario C |\n|------|-----------|-----------|-----------|\n| Novelty 挑战 | 低 (per-DOF is novel) | 中 (correction alone less novel) | 中-高 (需与 A2C2 差异化) |\n| Statistical power | 需 perdof-obs_only ≥5pp | 只需 CRM-argmin ≥5pp | 需 obs_only-argmin ≥5pp |\n| Reviewer \"so what?\" | 低 | 中 (加 magnitude control) | 中 (conformal pipeline \"wasted\"?) |\n| 论文完成复杂度 | 高 (需解释 loss-eval 反直觉) | 低 (最直白) | 中 (需优雅处理 negative result) |\n| Title/branding 一致性 | 最佳 (ACR = conformal features) | 可接受 | 差 (ACR 中 conformal 角色弱化) |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "2bdfd036-db77-4700-9368-3f7484a0af2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLj78f3QunkziNYXhaHXhC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1168,
      "cache_read_input_tokens": 43440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1168
      },
      "output_tokens": 53,
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

_source line 19 · 2026-05-15T04:48:35.547Z_

<details><summary>↩ Tool result · `toolu_01Jw3MhTTBBXKcG1GQQ1YRnF`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_analysis_prep.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "c07cafb2-bc91-4b86-8824-9a1fb3fa62d9",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_analysis_prep.md",
    "content": "# Spatial Ablation Analysis & Paper Narrative Preparation\n\n> 生成时间: 2026-05-15 | 状态: 分析备忘录（等待全 10 task 完成后裁决）\n\n## 1. 当前数据快照\n\n### Spatial Benchmark（ROADMAP 2026-05-15 03:08 UTC）\n\n| 实验 | Mode | Tasks 完成 | 当前 SR | 来源 |\n|------|------|-----------|---------|------|\n| VLA baseline (K=1) | vla_only | locked | **30%** | ROADMAP baselines |\n| VLA-mean (K=10) | vla_only mean | locked | **31%** | ROADMAP baselines |\n| argmin-only | reconvla | 8/10 | **37.5%** | ROADMAP spatial eval |\n| perdof CRM | acr_vla, norm=0.1 | 5/10 | **42.0%** | ROADMAP spatial eval (v4-small) |\n| obs_only CRM | crm_obs_only, norm=0.1 | 4/10 | **57.5%** | ROADMAP spatial eval (obs-only-r2) |\n| scalar CRM | crm_scalar, norm=0.1 | 2/10 | **80%*** | ROADMAP spatial eval (*easy tasks only) |\n\n**注意**: 任务描述中的数字（perdof 42.9%, obs_only 40.0%, scalar 56.7%@3 tasks）与 ROADMAP 不一致。以 ROADMAP 为准，但两者均为中间结果，任何中间排序均可能在剩余 tasks 翻转。\n\n### 关键增量\n\n| 对比 | 增量 | 统计可信度 |\n|------|------|-----------|\n| CRM (any) vs argmin-only | +4.5pp (perdof) 至 +20pp (obs_only) | 低: 4-5/10 tasks |\n| argmin-only vs VLA baseline | +7.5pp | 中: 8/10 tasks |\n| 全 pipeline vs VLA baseline | +12pp (perdof) 至 +27.5pp (obs_only) | 低: 不同 task counts |\n\n### 数据可靠性警告\n- **obs_only** 仅 4/10 tasks，当前领先可能因 task selection bias 翻转\n- **scalar** 仅 2/10 tasks 且均为 easy tasks，80% 完全不可信\n- **perdof** 5/10 tasks，D025 已将 D019 \"52.5%\" claim 标记为失效\n- 所有 CRM variant 排序必须等全 10 tasks 完成\n\n---\n\n## 2. 三种 Narrative 分析\n\n### Scenario A: perdof > obs_only（per-DOF story）\n\n**触发条件**: 全 10 task 后 perdof SR > obs_only SR 且差 ≥5pp\n\n**可能性评估**: **低**。当前 obs_only (57.5%@4) 大幅领先 perdof (42.0%@5)。需要剩余 tasks 中 obs_only 大幅下滑且 perdof 追上。训练 loss 也支持 obs_only（val_loss 0.0165 vs perdof 0.0358，见 D020）。\n\n**Narrative**: \"Per-DOF conformal features encode dimension-specific uncertainty that observation features cannot capture. Despite worse training loss, conformal features' epistemic signal proves critical under distribution shift in closed-loop deployment.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | 开门见山：scalar UQ 丢失维度信息 → per-DOF conformal features 是解决方案。Problem 聚焦 \"information loss in scalar aggregation\" |\n| **Method** | CGS multivariate CP + per-DOF interval extraction 是核心技术贡献。CRM 架构强调 40D conformal feature vector 的设计。Magnitude control 作为工程发现 |\n| **Results** | 主表: 4-way ablation 展示 perdof > obs_only > scalar ≈ argmin。亮点故事: \"training loss 预测翻转\" (obs_only lower loss but worse eval) = compelling evidence for epistemic value |\n| **Discussion** | 强调 conformal features 在 distribution shift 下的 epistemic value 与 in-distribution training loss 的 divergence。与 ReconVLA scalar CP 对比突出信息增益 |\n\n**风险**: 如果 perdof 仅略优于 obs_only (3-5pp)，统计显著性不足，narrative 说服力弱。\n\n---\n\n### Scenario B: perdof ≈ obs_only ≈ scalar（correction-is-key story）\n\n**触发条件**: 全 10 task 后三种 CRM variant 两两差 <5pp\n\n**可能性评估**: **中**。如果 obs_only 在剩余 tasks 下滑，三者可能收敛到 40-50% 区间。\n\n**Narrative**: \"Learned uncertainty-conditioned correction (sample-then-refine) significantly outperforms pure sample selection. The correction mechanism is the contribution, not the specific feature representation.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | Problem: 现有方法止步于 sample selection (ReconVLA) 或需 RL 训练 (SC-VLA)。Gap: 缺少 lightweight learned correction。Our angle: CRM 作为 plug-and-play correction module |\n| **Method** | CRM 架构设计 + magnitude control 是核心贡献。Per-DOF features 作为 \"one valid feature set\" 呈现，不强调其必要性。重点放在 correction mechanism 设计原则（bounded residual, norm control） |\n| **Results** | 主表: CRM (any variant) vs argmin-only 的增量。Feature ablation 作为次要表 \"CRM is robust to feature choice\"。Magnitude control study (norm sensitivity) 升级为独立 contribution |\n| **Discussion** | \"Correction > selection\" 作为主要 takeaway。与 residual policy learning 文献 (Silver 2018, PLD, TRANSIC) 建立联系。Per-DOF 保留用于 online monitoring (future work) |\n\n**优势**: 这是最稳健的 narrative——只要 CRM vs argmin-only ≥5pp 即可成立。不依赖特定 feature variant 排序。\n**风险**: Contribution novelty 降低——\"learned correction helps\" 不够新颖。需要用 magnitude control discovery 和 CoRL 实验规模补偿。\n\n---\n\n### Scenario C: obs_only > perdof（simpler-is-better / observation-conditioned story）\n\n**触发条件**: 全 10 task 后 obs_only SR > perdof SR 且差 ≥5pp\n\n**可能性评估**: **较高**。当前数据 (57.5% vs 42.0%) + 训练 loss (0.0165 vs 0.0358) 均支持此方向。D025 已预警此趋势。\n\n**Narrative**: \"Observation-conditioned learned residual correction is the key contribution. Conformal features provide no additional value as CRM input over observation features, but remain valuable for sample selection quality and coverage monitoring.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | Problem 保持不变（VLA robustness gap）。Gap: 缺少 inference-time learned correction。Our angle: lightweight observation-conditioned residual correction，不需要额外 UQ features |\n| **Method** | CRM 架构 + magnitude control 是核心。CGS/conformal 降为 \"sample selection module\" 的理论基础，不再是 CRM feature。需要解释 per-DOF features 的 negative result |\n| **Results** | 主表: obs_only CRM vs argmin-only vs baselines。Feature ablation 如实呈现——conformal features 不优于 observation features 作为 honest negative result。Per-DOF 在 sample selection 中的角色仍可报告 |\n| **Discussion** | 解释可能原因: (1) 观测特征已隐含编码 uncertainty 信息 (2) conformal 特征在小 K 下噪声大 (3) CRM 容量足以从观测中学到校正方向。将 per-DOF 定位为 \"future direction: larger K + better calibration\" |\n\n**Core Insight 需重写**: \"Lightweight learned residual correction on selected VLA samples significantly improves robustness. The correction module only needs observation features; structured uncertainty features are not required.\"\n\n**优势**: 实际上简化了 method 和 story——不需要解释复杂的 multivariate CP 管线作为 CRM 输入。\n**风险**: (1) 论文标题 \"ACR-VLA\" 中 \"conformal\" 角色弱化；(2) 与 A2C2 (Sendai 2025) 的差异化缩小——都变成了 \"observation-conditioned residual correction\"；(3) Reviewer 可能质疑 \"你们做了这么复杂的 CP pipeline 结果没用？\"\n\n**子情况 C1**: scalar > perdof 但 scalar < obs_only → conformal feature 形式无关紧要，进一步支持 \"correction mechanism is key\" narrative（hybrid of B+C）\n\n---\n\n## 3. 待完成实验及其对 Narrative 选择的影响\n\n| 实验 | 当前状态 | ETA | 对 narrative 的影响 |\n|------|---------|-----|-------------------|\n| **Spatial 全 10 task** (bjb1-18228) | 4-8/10 tasks | ~6-9h | **决定性**: 全部排序确认后才能选择 A/B/C |\n| **Object benchmark 全 10 task** (bjb1-32546) | 刚开始 | ~数小时 after spatial | **验证性**: cross-benchmark consistency。如果 spatial B 但 object A → narrative 困难 |\n| **Magnitude sweep** (norm ∈ {0.03, 0.05, 0.2, 0.3}) | 未开始 | 待 bjb2-28827 部署 | **补充性**: 强化 magnitude control contribution (所有 scenario 均可用) |\n| **K sensitivity sweep** (K=5,10,15,20) | 未开始 | 待 GPU 释放 | **补充性**: 回应 Reviewer Q1 (K=10 covariance reliability) |\n| **Fisher exact test** | 需全 10 task 数据 | post-eval | **统计性**: 判断增量是否 p<0.05 |\n\n**裁决所需最低数据**: Spatial 全 10 task + Object 全 10 task。两个 benchmark 均显示 CRM vs argmin ≥5pp (p<0.05) 才能安全 claim。\n\n---\n\n## 4. CoRL 8 页单 Claim 论文结构建议\n\n### 推荐结构（CoRL 2026, 8 pages + references）\n\n| 章节 | 页数 | 内容 |\n|------|------|------|\n| **Abstract** | — | 一句 problem, 一句 method (sample-then-refine + CRM), 一句 headline result |\n| **1. Introduction** | 1.0 | Problem (VLA robustness gap) → Existing approaches (selection/RL/MLLM) → Gap (no lightweight learned correction with statistical grounding) → Contribution (CRM + magnitude control + empirical findings) |\n| **2. Related Work** | 0.75 | (a) VLA robustness: training-time (RobustVLA, DiG-Flow, SRPO, ACoT) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2) (b) CP in robotics (c) Residual policy learning |\n| **3. Method** | 2.0 | 3.1 Multi-sample inference + CGS (0.5p) → 3.2 Conformal sample selection (0.5p) → 3.3 CRM architecture + feature variants (0.5p) → 3.4 Magnitude control (0.5p) |\n| **4. Experiments** | 2.5 | 4.1 Setup: LIBERO-Plus spatial+object, SmolVLA backbone, baselines (0.5p) → 4.2 Main results: headline table (0.5p) → 4.3 Feature ablation: 4-way comparison (0.5p) → 4.4 Magnitude sensitivity study (0.5p) → 4.5 Analysis: per-task breakdown, failure modes (0.5p) |\n| **5. Discussion & Limitations** | 0.75 | Sim-only, K=10 overhead, feature choice insights, future directions |\n| **6. Conclusion** | 0.25 | 2-3 sentences |\n| **References** | ~1.5 (不计入) | ~30-35 refs |\n\n### 单 Claim 论文的关键策略\n\n1. **Claim 必须够强**: \"CRM correction ≥5pp over argmin-only on BOTH benchmarks\" 是最低门槛。单 claim 论文缺乏 \"至少有一个 claim 成立\" 的安全网。\n\n2. **Ablation 表做得像 multi-claim**: 4-way feature ablation + magnitude sweep + K sensitivity = 3 个独立分析维度。即使只有一个 claim，实验深度可以补偿。\n\n3. **Magnitude control 升级为独立 contribution**: norm=1.42 → 0% vs norm=0.1 → 42-57.5% 的发现是 novel empirical insight（来源: D019）。这在所有 scenario 下都成立，可作为论文的 \"second punch\"。\n\n4. **Negative result 如实呈现**: 如果 per-DOF 不优于 obs_only (Scenario B/C)，Table 中如实展示比隐藏更好——Reviewer 会欣赏 thorough ablation。\n\n5. **与 ReconVLA 的对比是必须的** (paper_framing.md Reviewer Q6)。argmin-only baseline 已经是 ReconVLA 的近似（conformal selection without correction），但需要在论文中明确声明这一对应关系。\n\n### 各 Scenario 下的标题候选\n\n| Scenario | 标题方向 |\n|----------|---------|\n| A (perdof wins) | \"ACR-VLA: Dimension-Selective Action Correction via Per-DOF Conformal Features\" |\n| B (all similar) | \"Sample-then-Refine: Uncertainty-Conditioned Learned Correction for Robust VLA Deployment\" |\n| C (obs_only wins) | \"Learned Residual Correction Improves VLA Robustness: A Conformal Selection + Observation-Conditioned Refinement Pipeline\" |\n\n---\n\n## 5. 决策依赖与时间线\n\n```\nMay 15 (NOW)\n  ├── Spatial eval running (ETA ~6-9h)\n  ├── Object eval running (ETA ~hours after spatial)\n  └── This memo prepared\n\nMay 16 (Day 2)\n  ├── Spatial 全 10 task 完成 → 初步排序\n  ├── Object 初步结果\n  └── ★ Narrative 初步选择 (A/B/C)\n\nMay 17-19 (Day 3-5)\n  ├── Object 全 10 task 完成\n  ├── Fisher exact test on both benchmarks\n  ├── Magnitude sweep (if GPU available)\n  └── ★ Narrative 最终锁定 + paper_framing.md 更新\n\nMay 20-24 (Day 6-10)\n  ├── Paper writing (8 pages)\n  ├── Figures: main results table, ablation, magnitude curve\n  └── Per-task breakdown analysis\n\nMay 25-26 (Day 11-12)\n  ├── Abstract 提交 (May 26 DDL)\n  └── Continue full paper for Jun 2 DDL\n```\n\n---\n\n## 6. Scenario-Specific 风险矩阵\n\n| 风险 | Scenario A | Scenario B | Scenario C |\n|------|-----------|-----------|-----------|\n| Novelty 挑战 | 低 (per-DOF is novel) | 中 (correction alone less novel) | 中-高 (需与 A2C2 差异化) |\n| Statistical power | 需 perdof-obs_only ≥5pp | 只需 CRM-argmin ≥5pp | 需 obs_only-argmin ≥5pp |\n| Reviewer \"so what?\" | 低 | 中 (加 magnitude control) | 中 (conformal pipeline \"wasted\"?) |\n| 论文完成复杂度 | 高 (需解释 loss-eval 反直觉) | 低 (最直白) | 中 (需优雅处理 negative result) |\n| Title/branding 一致性 | 最佳 (ACR = conformal features) | 可接受 | 差 (ACR 中 conformal 角色弱化) |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01625QesBEBmkZhrzt3BWdQn`</summary>

```json
{
  "name": "spatial_analysis_prep",
  "type": "report",
  "description": "CoRL 2026 论文 narrative 分析备忘录: 基于 spatial benchmark 中间结果的三种 Scenario (A/B/C) 分析、各章节影响、待完成实验清单、8页单claim论文结构建议",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_analysis_prep.md",
  "tags": [
    "corl2026",
    "paper-framing",
    "spatial-ablation",
    "narrative-analysis"
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
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "9664f31c-7ace-495d-a15b-cfb8bc268fc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQ9uVi6kJgYT45p2Coi3LA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 44608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
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

_source line 21 · 2026-05-15T04:48:41.673Z_

<details><summary>↩ Tool result · `toolu_01625QesBEBmkZhrzt3BWdQn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_b9f79e\", \"name\": \"spatial_analysis_prep\", \"type\": \"report\", \"description\": \"CoRL 2026 论文 narrative 分析备忘录: 基于 spatial benchmark 中间结果的三种 Scenario (A/B/C) 分析、各章节影响、待完成实验清单、8页单claim论文结构建议\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/spatial_analysis_prep.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T04:48:41.627375+00:00\", \"tags\": [\"corl2026\", \"paper-framing\", \"spatial-ablation\", \"narrative-analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "e8e7dc15-3f31-4768-ac42-c68ba86b5537",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_b9f79e\\\", \\\"name\\\": \\\"spatial_analysis_prep\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"CoRL 2026 论文 narrative 分析备忘录: 基于 spatial benchmark 中间结果的三种 Scenario (A/B/C) 分析、各章节影响、待完成实验清单、8页单claim论文结构建议\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/spatial_analysis_prep.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T04:48:41.627375+00:00\\\", \\\"tags\\\": [\\\"corl2026\\\", \\\"paper-framing\\\", \\\"spatial-ablation\\\", \\\"narrative-analysis\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_b9f79e\", \"name\": \"spatial_analysis_prep\", \"type\": \"report\", \"description\": \"CoRL 2026 论文 narrative 分析备忘录: 基于 spatial benchmark 中间结果的三种 Scenario (A/B/C) 分析、各章节影响、待完成实验清单、8页单claim论文结构建议\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/spatial_analysis_prep.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T04:48:41.627375+00:00\", \"tags\": [\"corl2026\", \"paper-framing\", \"spatial-ablation\", \"narrative-analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

备忘录已写入 `artifacts/spatial_analysis_prep.md` 并注册（art_20260515_b9f79e）。

核心发现：

- **当前数据倾向 Scenario C**（obs_only 57.5% > perdof 42.0%），但 obs_only 仅 4/10 tasks，排序可能翻转
- **Scenario B 是最稳健的 fallback**——只要 CRM vs argmin-only ≥5pp 即可支撑，不依赖 variant 排序
- **Magnitude control (norm=1.42→0% vs norm=0.1→42-57.5%)** 在所有 scenario 下都是独立 contribution，建议升级为论文 "second punch"
- **裁决最低数据**: spatial + object 均完成全 10 tasks + Fisher exact test p<0.05
- 预计 May 16 spatial 完成后可初步选择 narrative，May 17-19 锁定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "uuid": "87e7d04f-4fa4-4ff6-a39a-a85cd3e95bad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qjQ92e6AR16f6S4jNYgxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 49443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
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

_source line 23_

备忘录已写入 `artifacts/spatial_analysis_prep.md` 并注册（art_20260515_b9f79e）。

核心发现：

- **当前数据倾向 Scenario C**（obs_only 57.5% > perdof 42.0%），但 obs_only 仅 4/10 tasks，排序可能翻转
- **Scenario B 是最稳健的 fallback**——只要 CRM vs argmin-only ≥5pp 即可支撑，不依赖 variant 排序
- **Magnitude control (norm=1.42→0% vs norm=0.1→42-57.5%)** 在所有 scenario 下都是独立 contribution，建议升级为论文 "second punch"
- **裁决最低数据**: spatial + object 均完成全 10 tasks + Fisher exact test p<0.05
- 预计 May 16 spatial 完成后可初步选择 narrative，May 17-19 锁定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 165539,
  "duration_api_ms": 167110,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "bdbfa29f-c4e9-41b1-aedb-a2f2582b3d13",
  "total_cost_usd": 0.50720525,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 38237,
    "cache_read_input_tokens": 197238,
    "output_tokens": 6728,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38237,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 270,
        "cache_read_input_tokens": 49443,
        "cache_creation_input_tokens": 635,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 635
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1260,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001355,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 6728,
      "cacheReadInputTokens": 197238,
      "cacheCreationInputTokens": 38237,
      "webSearchRequests": 0,
      "costUSD": 0.5058502500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3689870b-66ca-4b21-a226-5d83a2e3bcf7"
}
```

</details>

---
