# knowledge fix paper framing gaps

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_knowledge_fix-paper-framing-gaps_20260519T050814.log`
- **Structured JSON:** [`bbd6a4c48b3b72f55da9.json`](../../sessions/bb/bbd6a4c48b3b72f55da9.json)

## Before a recorded user message

41 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "3a72f03b-682f-4a29-aabb-2c3ab43c4fab",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1779180000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c8f1dd78-f969-4135-8c21-e329b9fa3ca4",
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current paper_framing.md and the registry entry for exp_14b_c4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "6664ef08-e8b7-4016-ae67-b3b023a86fef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3p9SPjsvdcPvEnVW5NnGC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13002,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13002
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019j9nzAj6hifoUit2cPz43U`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
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
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "59d43cd2-d841-4ce8-886a-03ebaec8f154",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3p9SPjsvdcPvEnVW5NnGC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13002,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13002
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-19T05:08:27.393Z_

<details><summary>↩ Tool result · `toolu_019j9nzAj6hifoUit2cPz43U`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "96174733-0eef-4972-97a5-ce1bd1c0c926",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper_framing.md and the registry entry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "646e42fd-7cab-40d8-8843-fd9eaf4147a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVnckDcmAHtcQRkR1FP4yK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 24843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1072
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016EivmnfDhXWvW9ViWTS5Mf`</summary>

```json
{
  "project": "gen-depth-contamination",
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
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "add79de1-c852-42a6-b7ea-6a2bb1ec7fae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVnckDcmAHtcQRkR1FP4yK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 24843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1072
      },
      "output_tokens": 21,
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

_source line 9 · 2026-05-19T05:08:31.042Z_

<details><summary>↩ Tool result · `toolu_016EivmnfDhXWvW9ViWTS5Mf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, updated D049/D050)\\n\\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\\n\\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\\n- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\\n\\n**子组件：**\\n\\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\\n> **7/8 model configurations yield K*=2 on C4 web text：**\\n>\\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|-----------|---------|--------|-----------------|\\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\\n>\\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\\n>\\n> *Decoding strategy invariance (exp-003):*\\n> | Decoding | AUC 1v2 | K* |\\n> |----------|---------|-----|\\n> | greedy | 0.6893 | 2 |\\n> | nucleus p=0.9 | 0.6866 | 2 |\\n> | temp=0.7 | 0.6887 | 2 |\\n> | temp=1.2 | 0.7039 | 2 |\\n>\\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\\n> - Paper 措辞：\\\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\\\"\\n\\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \\\"domain competence prerequisite\\\" 分析放 Appendix\\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\\n> - Sample size: n=2,200 per model\\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \\\"K*=3 with boundary pair AUC of 0.62\\\" 而非 \\\"robustly K*=3\\\"\\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\\n\\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\\n\\n**(d) Cross-model transfer (scorer invariance)**\\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\\n\\n**(e) Representation dependence of K* (Neural Probe)**\\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\\n> - 论文定位：validates choice of model-free 15D features for headline characterization\\n\\n**(f) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection，不是独立 claim\\n\\n### Secondary: C3 (K*-Aware Data Curation Validation)\\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\\n\\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \\\"universally beneficial\\\"。维持 \\\"consistent advantage\\\" 措辞，以 HellaSwag 显著性为主要证据。\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\\\"one-wash laundering\\\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\\n- **Headline result template**: \\\"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"K*∈{1,2,3} 范围太小，结论是否 trivial？\\\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\\n2. **\\\"只基于小模型（≤8B），能推广到更大模型吗？\\\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\\n3. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\\n4. **\\\"arXiv K*=3 样本量够吗？\\\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\\n5. **\\\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\\\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \\\"异常\\\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\\n6. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\\n7. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\\n8. **\\\"为什么不用 learned representations\\\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\\n9. **\\\"θ=0.60 选择是否 arbitrary？\\\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\\n10. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \\\"K*=2 everywhere\\\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\\n- One-wash laundering effect 是 memorable concept 便于传播\\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\\n\", \"total_chars\": 15549, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "ddf706d4-3514-425a-b588-9c021e5fdb24",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — gen-depth-contamination\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\\\n\\\\n## Canonical Experimental Condition\\\\n\\\\n**Continuation mode 是 cross-model 结论的基础。**\\\\n\\\\n> \\\\\\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\\\\\"\\\\n\\\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\\\n|-----------|-------------|-------------|---------|\\\\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\\\n\\\\n**原则**：\\\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\\\n- mvp-001 (Qwen-rewrite) 定位为 \\\\\\\"pilot study demonstrating feasibility\\\\\\\"，后续用 continuation mode rigorously validate\\\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\\\n\\\\n## Core Claims (2+1 结构, updated D049/D050)\\\\n\\\\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\\\\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\\\\n\\\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\\\\n\\\\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\\\\n- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\\\\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\\\\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\\\\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\\\\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\\\\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\\\\n\\\\n**子组件：**\\\\n\\\\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\\\\n> **7/8 model configurations yield K*=2 on C4 web text：**\\\\n>\\\\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\\\\n> |-------|-----------|---------|--------|-----------------|\\\\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\\\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\\\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\\\\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\\\\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\\\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\\\\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\\\\n>\\\\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\\\\n>\\\\n> *Decoding strategy invariance (exp-003):*\\\\n> | Decoding | AUC 1v2 | K* |\\\\n> |----------|---------|-----|\\\\n> | greedy | 0.6893 | 2 |\\\\n> | nucleus p=0.9 | 0.6866 | 2 |\\\\n> | temp=0.7 | 0.6887 | 2 |\\\\n> | temp=1.2 | 0.7039 | 2 |\\\\n>\\\\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\\\\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\\\\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\\\\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\\\\n> - Paper 措辞：\\\\\\\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\\\\\\\"\\\\n\\\\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\\\\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\\\\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\\\\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\\\\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\\\\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\\\\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\\\\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \\\\\\\"domain competence prerequisite\\\\\\\" 分析放 Appendix\\\\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\\\\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\\\\n> - Sample size: n=2,200 per model\\\\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \\\\\\\"K*=3 with boundary pair AUC of 0.62\\\\\\\" 而非 \\\\\\\"robustly K*=3\\\\\\\"\\\\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\\\\n\\\\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\\\\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\\\\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\\\\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\\\\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\\\\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\\\\n\\\\n**(d) Cross-model transfer (scorer invariance)**\\\\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\\\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\\\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\\\\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\\\\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\\\\n\\\\n**(e) Representation dependence of K* (Neural Probe)**\\\\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\\\\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\\\\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\\\\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\\\\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\\\\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\\\\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\\\\n> - 论文定位：validates choice of model-free 15D features for headline characterization\\\\n\\\\n**(f) Generation mode analysis (§4.x Analysis subsection)**\\\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\\\n> - 论文定位：Analysis subsection，不是独立 claim\\\\n\\\\n### Secondary: C3 (K*-Aware Data Curation Validation)\\\\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\\\\n\\\\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \\\\\\\"universally beneficial\\\\\\\"。维持 \\\\\\\"consistent advantage\\\\\\\" 措辞，以 HellaSwag 显著性为主要证据。\\\\n\\\\n### Supporting Analysis: Canonical Condition Selection\\\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\\\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\\\\\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\\\\\\\"one-wash laundering\\\\\\\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\\\\n- **Headline result template**: \\\\\\\"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\\\\\\\"\\\\n\\\\n## Anticipated Reviewer Concerns & Responses\\\\n\\\\n1. **\\\\\\\"K*∈{1,2,3} 范围太小，结论是否 trivial？\\\\\\\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\\\\n2. **\\\\\\\"只基于小模型（≤8B），能推广到更大模型吗？\\\\\\\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\\\\n3. **\\\\\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\\\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\\\\n4. **\\\\\\\"arXiv K*=3 样本量够吗？\\\\\\\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\\\\n5. **\\\\\\\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\\\\\\\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \\\\\\\"异常\\\\\\\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\\\\n6. **\\\\\\\"Prompt-chain 不代表真实世界递归污染\\\\\\\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\\\\n7. **\\\\\\\"同模型做生成和 surprisal 计算有 bias\\\\\\\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\\\\n8. **\\\\\\\"为什么不用 learned representations\\\\\\\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\\\\n9. **\\\\\\\"θ=0.60 选择是否 arbitrary？\\\\\\\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\\\\n10. **\\\\\\\"Graduated filtering 没和 data selection methods 比\\\\\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\\\\n\\\\n## Venue Fit\\\\n\\\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\\\\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \\\\\\\"K*=2 everywhere\\\\\\\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\\\\n- One-wash laundering effect 是 memorable concept 便于传播\\\\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\\\\n\\\", \\\"total_chars\\\": 15549, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, updated D049/D050)\\n\\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\\n\\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\\n- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\\n\\n**子组件：**\\n\\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\\n> **7/8 model configurations yield K*=2 on C4 web text：**\\n>\\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|-----------|---------|--------|-----------------|\\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\\n>\\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\\n>\\n> *Decoding strategy invariance (exp-003):*\\n> | Decoding | AUC 1v2 | K* |\\n> |----------|---------|-----|\\n> | greedy | 0.6893 | 2 |\\n> | nucleus p=0.9 | 0.6866 | 2 |\\n> | temp=0.7 | 0.6887 | 2 |\\n> | temp=1.2 | 0.7039 | 2 |\\n>\\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\\n> - Paper 措辞：\\\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\\\"\\n\\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \\\"domain competence prerequisite\\\" 分析放 Appendix\\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\\n> - Sample size: n=2,200 per model\\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \\\"K*=3 with boundary pair AUC of 0.62\\\" 而非 \\\"robustly K*=3\\\"\\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\\n\\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\\n\\n**(d) Cross-model transfer (scorer invariance)**\\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\\n\\n**(e) Representation dependence of K* (Neural Probe)**\\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\\n> - 论文定位：validates choice of model-free 15D features for headline characterization\\n\\n**(f) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection，不是独立 claim\\n\\n### Secondary: C3 (K*-Aware Data Curation Validation)\\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\\n\\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \\\"universally beneficial\\\"。维持 \\\"consistent advantage\\\" 措辞，以 HellaSwag 显著性为主要证据。\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\\\"one-wash laundering\\\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\\n- **Headline result template**: \\\"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"K*∈{1,2,3} 范围太小，结论是否 trivial？\\\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\\n2. **\\\"只基于小模型（≤8B），能推广到更大模型吗？\\\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\\n3. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\\n4. **\\\"arXiv K*=3 样本量够吗？\\\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\\n5. **\\\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\\\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \\\"异常\\\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\\n6. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\\n7. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\\n8. **\\\"为什么不用 learned representations\\\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\\n9. **\\\"θ=0.60 选择是否 arbitrary？\\\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\\n10. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \\\"K*=2 everywhere\\\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\\n- One-wash laundering effect 是 memorable concept 便于传播\\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\\n\", \"total_chars\": 15549, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01VxTWTe1u87vC6qyStqeRpe`</summary>

```json
{
  "project": "gen-depth-contamination",
  "filters": {
    "exp_id": "exp_14b_c4"
  },
  "fields": [
    "*"
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
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "3fda7deb-5cf8-4060-96d6-9bffc74a2acd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVnckDcmAHtcQRkR1FP4yK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 24843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1072
      },
      "output_tokens": 21,
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

_source line 11 · 2026-05-19T05:08:32.137Z_

<details><summary>↩ Tool result · `toolu_01VxTWTe1u87vC6qyStqeRpe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3457}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "081f09df-19e6-41db-9746-6258e4f426d1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3457}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3457}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The registry returned no results for exp_14b_c4. Let me search with a broader filter to find the 14B experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "173bcd44-acf0-40f6-9578-d44419adc82c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HZw3NDiq3LHNcKctGNAGb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7943,
      "cache_read_input_tokens": 25915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7943
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

Registry 没有找到 exp_14b_c4，让我用更宽的过滤条件搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "37df50db-b131-4dc5-838e-6fa16c94ce29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HZw3NDiq3LHNcKctGNAGb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7943,
      "cache_read_input_tokens": 25915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7943
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DBMWtWXMgNK53KMS6U1ddP`</summary>

```json
{
  "project": "gen-depth-contamination",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "status",
    "metrics"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "cb0feaf9-6d93-4a5a-827a-cb7a5a50f024",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HZw3NDiq3LHNcKctGNAGb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7943,
      "cache_read_input_tokens": 25915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7943
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

_source line 15 · 2026-05-19T05:08:37.927Z_

<details><summary>↩ Tool result · `toolu_01DBMWtWXMgNK53KMS6U1ddP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_pythia_retrain_depth7\": {\"status\": \"DONE\", \"metrics\": {\"kstar\": 7, \"pairwise_auc\": {\"0v1\": 0.9844, \"1v2\": 0.947, \"2v3\": 0.8891, \"3v4\": 0.7999, \"4v5\": 0.6907, \"5v6\": 0.6497, \"6v7\": 0.634}, \"pairwise_auc_ci\": {\"0v1\": [0.9829, 0.9858], \"1v2\": [0.9418, 0.9522], \"2v3\": [0.8822, 0.896], \"3v4\": [0.7951, 0.8047], \"4v5\": [0.688, 0.6934], \"5v6\": [0.6429, 0.6565], \"6v7\": [0.6275, 0.6406]}, \"pairwise_jsd\": {\"0v1\": 0.1775, \"1v2\": 0.1286, \"2v3\": 0.1069, \"3v4\": 0.0643, \"4v5\": 0.0331, \"5v6\": 0.0271, \"6v7\": 0.0138}}}, \"exp_qwen_retrain_depth7\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 7, \"theta\": 0.6, \"max_depth\": 7, \"analysis_method\": \"5-fold GroupKFold CV\", \"pairwise_auc\": {\"0v1\": {\"mean\": 0.9837, \"std\": 0.0019, \"ci_95\": [0.9821, 0.9854], \"folds\": [0.9832, 0.9821, 0.9837, 0.9823, 0.9873]}, \"1v2\": {\"mean\": 0.8971, \"std\": 0.0025, \"ci_95\": [0.8949, 0.8993], \"folds\": [0.8923, 0.8988, 0.8986, 0.8991, 0.8967]}, \"2v3\": {\"mean\": 0.8098, \"std\": 0.0052, \"ci_95\": [0.8052, 0.8144], \"folds\": [0.8086, 0.8074, 0.818, 0.8024, 0.8128]}, \"3v4\": {\"mean\": 0.76, \"std\": 0.0082, \"ci_95\": [0.7528, 0.7672], \"folds\": [0.7534, 0.7617, 0.7753, 0.7566, 0.7531]}, \"4v5\": {\"mean\": 0.7459, \"std\": 0.0091, \"ci_95\": [0.7379, 0.7538], \"folds\": [0.7429, 0.7562, 0.7521, 0.73, 0.7482]}, \"5v6\": {\"mean\": 0.7017, \"std\": 0.0068, \"ci_95\": [0.6958, 0.7076], \"folds\": [0.7006, 0.7077, 0.7104, 0.6915, 0.6984]}, \"6v7\": {\"mean\": 0.641, \"std\": 0.0039, \"ci_95\": [0.6376, 0.6445], \"folds\": [0.6419, 0.6349, 0.6464, 0.639, 0.643]}}, \"jsd\": {\"0v1\": 0.23005, \"1v2\": 0.103924, \"2v3\": 0.075049, \"3v4\": 0.065398, \"4v5\": 0.060509, \"5v6\": 0.034998, \"6v7\": 0.017652}}}, \"exp_code_pythia1b4\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"theta\": 0.6, \"pairwise_auc\": {\"0v1\": {\"mean\": 0.9592, \"std\": 0.0036, \"folds\": [0.9576, 0.9576, 0.9657, 0.96, 0.9552]}, \"1v2\": {\"mean\": 0.5983, \"std\": 0.005, \"folds\": [0.601, 0.5884, 0.6, 0.5997, 0.6024]}, \"2v3\": {\"mean\": 0.5215, \"std\": 0.0128, \"folds\": [0.5236, 0.5124, 0.5311, 0.5024, 0.5381]}, \"3v4\": {\"mean\": 0.5152, \"std\": 0.012, \"folds\": [0.4981, 0.5327, 0.5092, 0.5123, 0.5238]}, \"4v5\": {\"mean\": 0.5046, \"std\": 0.0137, \"folds\": [0.4983, 0.4822, 0.5074, 0.5224, 0.5128]}}, \"jsd\": {\"0v1\": 0.070173, \"1v2\": 0.008211, \"2v3\": 0.003674, \"3v4\": 0.002902, \"4v5\": 0.002685}, \"ordinal\": {\"mae\": 1.3268, \"accuracy\": 0.3357}, \"top_features\": [\"freq_entropy\", \"surp_d1_mean\", \"surp_d2_mean\", \"surp_mean\", \"surp_d1_skew\"], \"features_csv\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4/features.csv\"}}, \"exp_028_power_curve\": {\"status\": \"DONE\", \"metrics\": {\"min_n_100pct\": 2000, \"n500_auc\": 0.5808, \"n500_rate\": 0.2, \"n1000_auc\": 0.5911, \"n1000_rate\": 0.3, \"n2000_auc\": 0.6101, \"n2000_rate\": 1, \"n3000_auc\": 0.6166, \"n3000_rate\": 1, \"n4000_auc\": 0.622, \"n4000_rate\": 1, \"n5000_auc\": 0.6288, \"n5000_rate\": 1}}, \"exp_qwen_retrain_chain\": {\"status\": \"DONE\", \"metrics\": {\"K_star_lower_bound\": 4, \"theta\": 0.6, \"auc_0v1\": 0.9838, \"auc_1v2\": 0.8969, \"auc_2v3\": 0.81, \"auc_3v4\": 0.7624, \"ci_0v1\": [0.982, 0.9855], \"ci_1v2\": [0.8937, 0.9001], \"ci_2v3\": [0.8052, 0.8147], \"ci_3v4\": [0.7543, 0.7706], \"ci_method\": \"5-fold CV\", \"jsd_0v1\": 0.2263, \"jsd_1v2\": 0.1046, \"jsd_2v3\": 0.0752, \"jsd_3v4\": 0.0654}}, \"exp_code_qwen1b5\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 2, \"theta\": 0.6, \"auc_0v1\": 0.9388, \"auc_1v2\": 0.7382, \"auc_2v3\": 0.53, \"auc_3v4\": 0.5022, \"auc_4v5\": 0.5219, \"ci_0v1\": [0.929, 0.949], \"ci_1v2\": [0.709, 0.767], \"ci_2v3\": [0.514, 0.546], \"jsd_0v1\": 0.0814, \"jsd_1v2\": 0.0443, \"jsd_2v3\": 0.0038, \"ordinal_accuracy\": 0.359, \"ordinal_mae\": 1.204}}, \"exp_olmo_retrain_chain\": {\"status\": \"DONE\"}, \"exp_028_subsampling_power\": {\"status\": \"DONE\", \"metrics\": {\"n_1000\": {\"mean_auc\": 0.608, \"std\": 0.012, \"detection_prob\": 0.9}, \"n_2500\": {\"mean_auc\": 0.618, \"std\": 0.006, \"detection_prob\": 1}, \"n_5000\": {\"mean_auc\": 0.629, \"std\": 0, \"detection_prob\": 1}, \"key_finding\": \"n>=2500 gives 100% reliable K*=2 detection. n=1000 already 90%. Signal is robust, not large-sample artifact.\"}}, \"exp_026_arxiv_filtering\": {\"status\": \"DONE\", \"metrics\": {\"runs_completed\": \"15/15\", \"strategies\": [\"no_filter\", \"binary\", \"graduated_a09\"], \"seeds\": [42, 123, 456, 789, 1024], \"mmlu\": {\"no_filter\": \"0.5899±0.0008\", \"binary\": \"0.5876±0.0004\", \"graduated_a09\": \"0.5900±0.0011\"}, \"hellaswag\": {\"no_filter\": \"0.6600±0.0002\", \"binary\": \"0.6642±0.0004\", \"graduated_a09\": \"0.6599±0.0003\"}, \"delta_vs_no_filter\": {\"binary_mmlu\": \"-0.0023\", \"binary_hellaswag\": \"+0.0042\", \"graduated_mmlu\": \"+0.0001\", \"graduated_hellaswag\": \"-0.0001\"}, \"key_finding\": \"All three strategies produce nearly identical results. Graduated ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\"}}, \"exp_027_latex_ablation\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"k_star_preserved\": true, \"pairwise_auc_original\": {\"0v1\": 0.9948, \"1v2\": 0.8581, \"2v3\": 0.6436, \"3v4\": 0.544, \"4v5\": 0.5299}, \"pairwise_auc_stripped\": {\"0v1\": 0.9948, \"1v2\": 0.8297, \"2v3\": 0.6229, \"3v4\": 0.5468, \"4v5\": 0.5476}, \"auc_delta\": {\"0v1\": 0, \"1v2\": -0.028, \"2v3\": -0.021, \"3v4\": 0.003, \"4v5\": 0.018}, \"latex_reduction_by_depth\": {\"depth_0\": \"0.6%\", \"depth_5\": \"4.4%\"}, \"key_finding\": \"K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still >θ=0.60). LaTeX format is NOT a confound.\"}}, \"exp_025_pythia_filtering\": {\"status\": \"DONE\", \"metrics\": {\"runs_completed\": \"9/9\", \"strategies\": [\"no_filter\", \"binary_ours\", \"graduated_a09\"], \"seeds\": [42, 123, 456], \"mmlu\": {\"no_filter\": \"0.2568±0.0012\", \"binary_ours\": \"0.2585±0.0004\", \"graduated_a09\": \"0.2561±0.0009\"}, \"hellaswag\": {\"no_filter\": \"0.5250±0.0008\", \"binary_ours\": \"0.5251±0.0001\", \"graduated_a09\": \"0.5253±0.0007\"}, \"delta_vs_no_filter\": {\"binary_ours_mmlu\": \"+0.0017\", \"binary_ours_hellaswag\": \"+0.0000\", \"graduated_a09_mmlu\": \"-0.0007\", \"graduated_a09_hellaswag\": \"+0.0003\"}, \"key_finding\": \"All three filtering strategies produce nearly identical results on Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering binary>graduated>no_filter NOT confirmed.\"}}, \"exp_14b_c4\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9598, \"1v2\": 0.621, \"2v3\": 0.5494, \"3v4\": 0.5243, \"4v5\": 0.5154}, \"pairwise_jsd\": {\"0v1\": 0.1097, \"1v2\": 0.0112, \"2v3\": 0.0062, \"3v4\": 0.0044, \"4v5\": 0.0036}, \"bootstrap_ci\": {\"0v1\": [0.9564, 0.963], \"1v2\": [0.6119, 0.6304], \"2v3\": [0.5392, 0.5594], \"3v4\": [0.514, 0.5346], \"4v5\": [0.5045, 0.5265]}, \"permutation_p\": {\"0v1\": \"<0.001\", \"1v2\": \"<0.001\", \"2v3\": \"<0.001\", \"3v4\": \"<0.001\", \"4v5\": \"<0.001\"}, \"k_star_statistically_confirmed\": true, \"ordinal_mae\": 1.2266, \"ordinal_accuracy\": 0.3497, \"top_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_std\", \"surp_d1_mean\", \"surp_d2_mean\"], \"key_finding\": \"K*=2 confirmed at 14B scale with bootstrap CI. 1v2 CI lower (0.6119) > theta=0.60; 2v3 CI upper (0.5594) < theta=0.60. All permutation p<0.001.\"}}, \"exp_arXiv_mistral7b_crossscorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"scorer\": \"pythia-1.4b\", \"auc_0v1\": 0.9798, \"auc_1v2\": 0.8141, \"auc_2v3\": 0.6075, \"auc_3v4\": 0.5489, \"auc_4v5\": 0.5391, \"jsd_0v1\": 0.135575, \"jsd_1v2\": 0.078, \"jsd_2v3\": 0.020452, \"jsd_3v4\": 0.010992, \"jsd_4v5\": 0.008831, \"ordinal_mae\": 0.9061, \"ordinal_accuracy\": 0.4412}}, \"exp_arXiv_llama8b_crossscorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"auc_0v1\": 0.9629, \"auc_1v2\": 0.8433, \"auc_2v3\": 0.6201, \"auc_3v4\": 0.523, \"auc_4v5\": 0.5245, \"jsd_0v1\": 0.1214, \"jsd_1v2\": 0.0815, \"jsd_2v3\": 0.0195, \"jsd_3v4\": 0.0083, \"jsd_4v5\": 0.0082, \"ordinal_mae\": 0.9025, \"ordinal_accuracy\": 0.4407, \"scorer\": \"pythia-1.4b\"}}, \"exp_arXiv_qwen7b_crossscorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"auc_0v1\": 0.9575, \"auc_1v2\": 0.8171, \"auc_2v3\": 0.5989, \"auc_3v4\": 0.5417, \"auc_4v5\": 0.5192, \"jsd_0v1\": 0.137085, \"jsd_1v2\": 0.059688, \"jsd_2v3\": 0.013508, \"jsd_3v4\": 0.009125, \"jsd_4v5\": 0.006738, \"ordinal_mae\": 0.9617, \"ordinal_accuracy\": 0.4255}}, \"exp_arXiv_qwen1b5_crossscorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"auc_0v1\": 0.9748, \"auc_1v2\": 0.8105, \"auc_2v3\": 0.6317, \"auc_3v4\": 0.5437, \"auc_4v5\": 0.5294, \"jsd_0v1\": 0.154297, \"jsd_1v2\": 0.066782, \"jsd_2v3\": 0.019268, \"jsd_3v4\": 0.008867, \"jsd_4v5\": 0.006991, \"ordinal_mae\": 0.9017, \"ordinal_accuracy\": 0.4402}}, \"exp_wiki_scorer_confound_1b5\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"confound_verdict\": \"confirmed\", \"auc_0v1\": 0.9729, \"auc_1v2\": 0.5994, \"auc_2v3\": 0.533, \"auc_3v4\": 0.5214, \"auc_4v5\": 0.5068, \"jsd_0v1\": 0.0886, \"ordinal_mae\": 1.2995, \"ordinal_accuracy\": 0.3466}}, \"exp_wiki_scorer_confound\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"confound_verdict\": \"confirmed\", \"auc_0v1\": 0.9404, \"auc_1v2\": 0.587, \"auc_2v3\": 0.5456, \"auc_3v4\": 0.525, \"auc_4v5\": 0.5172, \"critical_delta_1v2\": -0.0238}}, \"exp_wiki_qwen7b\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 2, \"auc_0v1\": 0.9673, \"auc_1v2\": 0.6108, \"auc_2v3\": 0.5562, \"auc_3v4\": 0.5297, \"auc_4v5\": 0.529, \"jsd_0v1\": 0.083514, \"jsd_1v2\": 0.010991, \"jsd_2v3\": 0.00555, \"jsd_3v4\": 0.004611, \"jsd_4v5\": 0.003894, \"ordinal_mae\": 1.2501, \"ordinal_accuracy\": 0.3532}}, \"exp_wiki_mistral7b\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"ordinal_mae\": 1.3445, \"ordinal_accuracy\": 0.3273, \"auc_0v1\": 0.9607, \"auc_1v2\": 0.5552, \"auc_2v3\": 0.5236, \"auc_3v4\": 0.5181, \"auc_4v5\": 0.5012, \"jsd_0v1\": 0.054134, \"jsd_1v2\": 0.005678, \"jsd_2v3\": 0.003698, \"jsd_3v4\": 0.003459, \"jsd_4v5\": 0.003274}}, \"exp_wiki_llama8b\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"ordinal_mae\": 1.2954, \"ordinal_accuracy\": 0.3313, \"auc_0v1\": 0.9316, \"auc_1v2\": 0.5954, \"auc_2v3\": 0.5392, \"auc_3v4\": 0.5221, \"auc_4v5\": 0.5212, \"jsd_0v1\": 0.06169, \"jsd_1v2\": 0.00931}}, \"exp_arXiv_qwen7b\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.983, \"1v2\": 0.835, \"2v3\": 0.626, \"3v4\": 0.544, \"4v5\": 0.513}, \"pairwise_jsd\": {\"0v1\": 0.1656, \"1v2\": 0.0668, \"2v3\": 0.0156, \"3v4\": 0.0089, \"4v5\": 0.0061}, \"ordinal_mae\": 0.9, \"ordinal_accuracy\": 0.446}}, \"exp_arXiv_mistral7b\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9848, \"1v2\": 0.8201, \"2v3\": 0.6275, \"3v4\": 0.5295, \"4v5\": 0.5295}, \"jsd\": {\"0v1\": 0.14249, \"1v2\": 0.076232, \"2v3\": 0.018972, \"3v4\": 0.009908, \"4v5\": 0.008877}, \"ordinal_mae\": 0.8958, \"ordinal_accuracy\": 0.4474, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_d1_skew\", \"surp_mean\", \"surp_d2_mean\"]}}, \"exp_arXiv_llama8b\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 3, \"auc_0v1\": 0.9754, \"auc_1v2\": 0.8447, \"auc_2v3\": 0.6215, \"auc_3v4\": 0.5362, \"auc_4v5\": 0.5331, \"jsd_0v1\": 0.1296, \"jsd_1v2\": 0.0785, \"jsd_2v3\": 0.0177, \"ordinal_acc\": 0.4549, \"ordinal_mae\": 0.8806}}, \"exp_wiki_pythia_v2\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.975, \"auc_1v2\": 0.5846, \"auc_2v3\": 0.5445, \"auc_3v4\": 0.5205, \"auc_4v5\": 0.5168, \"jsd_0v1\": 0.080065, \"jsd_1v2\": 0.007773, \"ordinal_acc\": 0.3503}}, \"exp_wiki_olmo_v2\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9932, \"auc_1v2\": 0.4986, \"auc_2v3\": 0.5012, \"auc_3v4\": 0.5057, \"auc_4v5\": 0.5009, \"jsd_0v1\": 0.1688, \"ordinal_acc\": 0.3227}}, \"exp_arXiv_olmo\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9958, \"auc_1v2\": 0.5034, \"auc_2v3\": 0.5069, \"auc_3v4\": 0.5021, \"auc_4v5\": 0.5037, \"jsd_0v1\": 0.329, \"ordinal_acc\": 0.33}}, \"exp_wiki_olmo\": {\"status\": \"DONE\"}, \"exp_wiki_pythia\": {\"status\": \"DONE\"}, \"exp_009_dose_response\": {\"status\": \"DONE\", \"metrics\": {\"total_runs\": 45, \"seeds\": 5, \"ratios\": [0.1, 0.3, 0.5], \"strategies\": [\"no_filter\", \"binary_ours\", \"graduated\"], \"cross_ratio_finding\": \"Binary filtering consistently best across all ratios. Graduated filtering = no_filter at every ratio. Effect size of binary advantage increases with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp). Original C3 hypothesis (graduated > binary) rejected.\", \"gpu_hours_total\": 9.9}}, \"exp_009_dose_50pct_v3\": {\"status\": \"DONE\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6063±0.0013\", \"hellaswag\": \"0.6680±0.0005\"}, \"binary_ours\": {\"mmlu\": \"0.6088±0.0011\", \"hellaswag\": \"0.6731±0.0004\"}, \"graduated\": {\"mmlu\": \"0.6062±0.0009\", \"hellaswag\": \"0.6679±0.0002\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0025, \"p_mmlu\": 0.0377, \"delta_hellaswag\": 0.0051, \"p_hellaswag\": 2e-05}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.0026, \"p_mmlu\": 0.0257, \"delta_hellaswag\": -0.0052, \"p_hellaswag\": 3e-05}, \"graduated_vs_nofilter\": {\"delta_mmlu\": -0.0001, \"p_mmlu\": 0.89, \"delta_hellaswag\": -0.0001, \"p_hellaswag\": 0.706}}, \"key_finding\": \"Binary significantly best (HellaSwag p<0.001). Graduated = no_filter exactly.\"}}, \"exp_009_dose_30pct_v3\": {\"status\": \"DONE\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6069±0.0007\", \"hellaswag\": \"0.6664±0.0020\"}, \"binary_ours\": {\"mmlu\": \"0.6082±0.0012\", \"hellaswag\": \"0.6725±0.0007\"}, \"graduated\": {\"mmlu\": \"0.6072±0.0008\", \"hellaswag\": \"0.6665±0.0014\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0013, \"p_mmlu\": 0.0739, \"delta_hellaswag\": 0.0061, \"p_hellaswag\": 0.0036}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.001, \"p_mmlu\": 0.3018, \"delta_hellaswag\": -0.006, \"p_hellaswag\": 0.0009}, \"graduated_vs_nofilter\": {\"delta_mmlu\": 0.0003, \"p_mmlu\": 0.6638, \"delta_hellaswag\": 0.0002, \"p_hellaswag\": 0.6646}}, \"key_finding\": \"Binary best on HellaSwag (p=0.004). Graduated = no_filter.\"}}, \"exp_009_dose_10pct_v3\": {\"status\": \"DONE\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6058±0.0002\", \"hellaswag\": \"0.6689±0.0007\"}, \"binary_ours\": {\"mmlu\": \"0.6079±0.0005\", \"hellaswag\": \"0.6727±0.0008\"}, \"graduated\": {\"mmlu\": \"0.6066±0.0011\", \"hellaswag\": \"0.6700±0.0015\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0021, \"p_mmlu\": 0.001, \"delta_hellaswag\": 0.0038, \"p_hellaswag\": 0.0017}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.0014, \"p_mmlu\": 0.0917, \"delta_hellaswag\": -0.0027, \"p_hellaswag\": 0.0399}, \"graduated_vs_nofilter\": {\"delta_mmlu\": 0.0008, \"p_mmlu\": 0.2706, \"delta_hellaswag\": 0.0011, \"p_hellaswag\": 0.0611}}, \"key_finding\": \"Binary best. Graduated ≈ no_filter.\"}}, \"exp_027_retrain_bootstrap\": {\"status\": \"DONE\", \"metrics\": {\"bootstrap_iterations\": 10000, \"pairs\": {\"0v1\": {\"auc_point\": 0.9847, \"ci_lower\": 0.9828, \"ci_upper\": 0.9864, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"1v2\": {\"auc_point\": 0.9482, \"ci_lower\": 0.9443, \"ci_upper\": 0.952, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"2v3\": {\"auc_point\": 0.8885, \"ci_lower\": 0.8829, \"ci_upper\": 0.894, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"3v4\": {\"auc_point\": 0.7977, \"ci_lower\": 0.7903, \"ci_upper\": 0.8051, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}}, \"key_finding\": \"All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001.\"}}, \"exp_026_feature_stability_v2\": {\"status\": \"DONE\", \"metrics\": {\"data_source\": \"exp_001_pythia prompt-chain (K*=2)\", \"results\": {\"15D\": {\"num_tested\": 1, \"num_pass\": 1, \"min_1v2_auc\": 0.6262, \"mean_1v2_auc\": 0.6262}, \"10D\": {\"num_tested\": 5, \"num_pass\": 5, \"min_1v2_auc\": 0.6153, \"mean_1v2_auc\": 0.6191}, \"8D\": {\"num_tested\": 5, \"num_pass\": 5, \"min_1v2_auc\": 0.6056, \"mean_1v2_auc\": 0.6159}, \"5D\": {\"num_tested\": 5, \"num_pass\": 2, \"min_1v2_auc\": 0.5856, \"mean_1v2_auc\": 0.5998}, \"3D_top3\": {\"num_tested\": 1, \"num_pass\": 0, \"min_1v2_auc\": 0.5871, \"mean_1v2_auc\": 0.5871}}, \"key_finding\": \"8+ features sufficient for robust K*=2 (all pass θ=0.60). 5D fragile (2/5 pass). Top-3 alone fails. Feature diversity matters at the K* boundary.\"}}, \"exp_026_feature_stability\": {\"status\": \"DONE\", \"metrics\": {\"data_source\": \"exp_016_qwen_base (prompt-chain, K*=2)\", \"results\": {\"15D\": {\"num_tested\": 1, \"num_kstar_2\": 1, \"min_1v2_auc\": 0.6262, \"mean_1v2_auc\": 0.6262}, \"10D\": {\"num_tested\": 5, \"num_kstar_2\": 5, \"min_1v2_auc\": 0.6153, \"mean_1v2_auc\": 0.6191}, \"8D\": {\"num_tested\": 5, \"num_kstar_2\": 5, \"min_1v2_auc\": 0.6056, \"mean_1v2_auc\": 0.6159}, \"5D\": {\"num_tested\": 5, \"num_kstar_2\": 2, \"min_1v2_auc\": 0.5856, \"mean_1v2_auc\": 0.5998}, \"3D_top3\": {\"num_tested\": 1, \"num_kstar_2\": 0, \"min_1v2_auc\": 0.5871, \"mean_1v2_auc\": 0.5871}}, \"all_above_theta\": false, \"key_finding\": \"Feature selection MATTERS at K*=2 boundary. 15D/10D/8D all robust (min 1v2 AUC > 0.60). 5D random subsets: only 2/5 pass θ=0.60 (min=0.5856). Top-3 features alone (0.5871) fail θ. Contrast with retrain-chain (K*=4) where all subsets trivially passed (min=0.8314).\", \"previous_run_note\": \"v1 used retrain-chain data (K*=4), where all subsets trivially passed with min 1v2 AUC=0.8314. v2 uses prompt-chain data (K*=2) to test boundary robustness.\"}}, \"exp_027\": {\"status\": \"DONE\", \"metrics\": {\"kstar_ci\": 4, \"0v1_auc\": 0.9847, \"0v1_ci\": [0.9828, 0.9864], \"0v1_perm_p\": 0.0001, \"1v2_auc\": 0.9482, \"1v2_ci\": [0.9443, 0.952], \"1v2_perm_p\": 0.0001, \"2v3_auc\": 0.8885, \"2v3_ci\": [0.8829, 0.894], \"2v3_perm_p\": 0.0001, \"3v4_auc\": 0.7977, \"3v4_ci\": [0.7903, 0.8051], \"3v4_perm_p\": 0.0001, \"all_ci_lower_above_theta\": true}}, \"exp_005_degradation\": {\"status\": \"DONE\", \"metrics\": {\"cross_model_kendall_tau_by_first_auc\": {\"Pythia_vs_OLMo\": 0.733, \"Pythia_vs_Qwen_rewrite\": 0.467, \"Pythia_vs_Qwen_cont\": 0.695, \"OLMo_vs_Qwen_rewrite\": 0.429, \"OLMo_vs_Qwen_cont\": 0.543, \"Qwen_rewrite_vs_Qwen_cont\": 0.733}, \"cross_model_kendall_tau_by_avg_auc\": {\"Pythia_vs_OLMo\": 0.8476, \"Pythia_vs_Qwen_cont\": 0.7524, \"OLMo_vs_Qwen_cont\": 0.6762}, \"cross_model_spearman_rho_single_feature_auc\": {\"Pythia_vs_OLMo\": 0.95, \"Pythia_vs_Qwen_cont\": 0.9143, \"OLMo_vs_Qwen_cont\": 0.85, \"metric_definition\": \"Spearman ρ on per-feature AUC rankings (each feature independently classifies depth pairs)\"}, \"4model_tau_mean_continuation_by_first_auc\": 0.657, \"4model_tau_mean_all_by_first_auc\": 0.6, \"generation_mode_delta\": {\"Pythia_vs_Qwen\": \"+0.228\", \"OLMo_vs_Qwen\": \"+0.114\"}, \"top3_features_ranking_by_first_auc\": {\"Pythia\": [\"surp_d1_std\", \"surp_d2_std\", \"surp_std\"], \"OLMo\": [\"surp_std\", \"surp_d1_std\", \"surp_d2_std\"], \"Qwen_rewrite\": [\"freq_entropy\", \"surp_std\", \"surp_d1_std\"], \"Qwen_cont\": [\"surp_d1_std\", \"surp_std\", \"surp_d2_std\"]}, \"shared_top_discriminators\": \"surp_d1_std, surp_std, surp_d2_std shared across all architectures (single-feature AUC ranking)\", \"degradation_ordering_consistency\": \"Strong cross-model consistency (ρ≥0.85) on single-feature AUC ranking under controlled generation mode.\", \"residual_architecture_effect\": \"Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\", \"limitation_1v2_weakness\": \"depth-pair level consistency weakest at 1v2 (τ~0.37), near-generational feature importance ordering varies more across models\"}}, \"exp_024_arxiv_domain\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9946, \"1v2\": 0.858, \"2v3\": 0.6427, \"3v4\": 0.5437, \"4v5\": 0.5294}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9946, \"ci_lower\": 0.9929, \"ci_upper\": 0.9961, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.858, \"ci_lower\": 0.848, \"ci_upper\": 0.8679, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.6427, \"ci_lower\": 0.6275, \"ci_upper\": 0.6575, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5437, \"ci_lower\": 0.5276, \"ci_upper\": 0.5598, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5294, \"ci_lower\": 0.5133, \"ci_upper\": 0.5455, \"perm_p\": 0.0006}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\"}}, \"exp_017_qwen_continuation\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9972, \"1v2\": 0.6114, \"2v3\": 0.5609, \"3v4\": 0.5408, \"4v5\": 0.5139}, \"pairwise_jsd\": {\"0v1\": 0.28627, \"1v2\": 0.005107, \"2v3\": 0.003603, \"3v4\": 0.003395, \"4v5\": 0.003085}, \"ordinal_mae\": 1.1547, \"ordinal_accuracy\": 0.3819, \"top3_features\": [\"freq_entropy\", \"surp_mean\", \"surp_std\"]}}, \"exp_012_binary_confidence\": {\"status\": \"DONE\", \"metrics\": {\"n_samples\": 500, \"generators\": [\"qwen-rewrite\", \"pythia-1.4b\", \"olmo-1b\", \"qwen-cont\"], \"6class_accuracy\": {\"qwen-rewrite\": 0.1987, \"pythia-1.4b\": 0.1303, \"olmo-1b\": 0.127, \"qwen-cont\": 0.1833, \"random_baseline\": 0.1667}, \"spearman_rho\": {\"qwen-rewrite\": {\"log_ppl_ref\": -0.1233, \"log_ppl_obs\": 0.0815, \"ppl_ratio\": 0.1185}, \"pythia-1.4b\": {\"log_ppl_ref\": -0.2972, \"log_ppl_obs\": -0.4529, \"ppl_ratio\": -0.392}, \"olmo-1b\": {\"log_ppl_ref\": -0.378, \"log_ppl_obs\": -0.4614, \"ppl_ratio\": -0.4068}, \"qwen-cont\": {\"log_ppl_ref\": -0.3887, \"log_ppl_obs\": -0.162, \"ppl_ratio\": -0.058}}, \"binary_detector_kstar\": 1, \"obd_kstar\": 2, \"auc_non_monotonic\": true, \"key_finding\": \"Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but practically weak). AUC non-monotonic — binary detectors cannot maintain depth ordering. Confirms binary confidence ≠ depth estimation.\"}}, \"exp_C_permutation_10k\": {\"status\": \"DONE\", \"metrics\": {\"resamples\": 10000, \"all_boundary_pairs_p\": \"<0.0001\", \"key_finding\": \"10K permutation confirms all boundary p-values well below 0.01. FR-11 resolved.\"}}, \"exp_002_olmo_depth\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.997, \"1v2\": 0.6146, \"2v3\": 0.5497, \"3v4\": 0.509, \"4v5\": 0.5044}, \"pairwise_auc_std\": {\"0v1\": 0.0004, \"1v2\": 0.0029, \"2v3\": 0.004, \"3v4\": 0.0084, \"4v5\": 0.0136}, \"pairwise_jsd\": {\"0v1\": 0.23941, \"1v2\": 0.012972, \"2v3\": 0.00735, \"3v4\": 0.003968, \"4v5\": 0.003851}, \"ordinal_mae\": 1.1813, \"ordinal_accuracy\": 0.3685, \"top_features\": [\"surp_d1_mean\", \"surp_d1_skew\", \"freq_kurtosis\", \"surp_d2_mean\", \"surp_mean\"]}}, \"exp_009_dose_50pct_v2\": {\"status\": \"DONE\"}, \"exp_009_dose_30pct_v2\": {\"status\": \"DONE\"}, \"exp_009_dose_10pct_v2\": {\"status\": \"DONE\"}, \"exp_009_dose_50pct\": {\"status\": \"DONE\"}, \"exp_009_dose_30pct\": {\"status\": \"DONE\"}, \"exp_009_dose_10pct\": {\"status\": \"DONE\"}, \"exp_kstar_theta\": {\"status\": \"DONE\", \"metrics\": {\"output_files\": [\"kstar_theta_curve.pdf (32KB)\", \"kstar_theta_curve.png (335KB)\"], \"models\": [\"Qwen-rewrite\", \"Pythia\", \"OLMo\", \"Qwen-cont\"], \"depth_pairs\": 5, \"key_finding\": \"All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5. θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical resolved.\"}}, \"exp_022_cross_scorer_matrix\": {\"status\": \"DONE\", \"metrics\": {\"total_combos\": 12, \"completed\": 12, \"K_star_distribution\": {\"K2\": 11, \"K1\": 1}, \"matrix\": {\"pythia_greedy×olmo\": {\"K_star\": 2, \"1v2\": 0.8811}, \"pythia_greedy×pythia\": {\"K_star\": 2, \"1v2\": 0.8838}, \"pythia_greedy×qwen_base\": {\"K_star\": 2, \"1v2\": 0.8814}, \"pythia_greedy×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.8818}, \"qwen_base×olmo\": {\"K_star\": 2, \"1v2\": 0.6047}, \"qwen_base×pythia\": {\"K_star\": 2, \"1v2\": 0.617}, \"qwen_base×qwen_base\": {\"K_star\": 2, \"1v2\": 0.6262}, \"qwen_base×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.6273}, \"qwen_cont256×olmo\": {\"K_star\": 2, \"1v2\": 0.6028}, \"qwen_cont256×pythia\": {\"K_star\": 1, \"1v2\": 0.5979}, \"qwen_cont256×qwen_base\": {\"K_star\": 2, \"1v2\": 0.6282}, \"qwen_cont256×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.6072}}, \"key_finding\": \"Scorer independence confirmed: K*=2 in 11/12 combos. Only exception: qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.\"}}, \"exp_008_retrain_chain_v2\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": \">=4\", \"pairwise_auc\": {\"0v1\": 0.9847, \"1v2\": 0.9484, \"2v3\": 0.8888, \"3v4\": 0.7982}, \"pairwise_jsd\": {\"0v1\": 0.17, \"1v2\": 0.12, \"2v3\": 0.064, \"3v4\": 0.04}, \"key_finding\": \"Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic boundary.\"}}, \"exp-008-retrain-chain\": {\"status\": \"DONE\"}, \"exp_025_pythia_arxiv\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9877, \"1v2\": 0.8047, \"2v3\": 0.6545, \"3v4\": 0.5507, \"4v5\": 0.5287}, \"pairwise_jsd\": {\"0v1\": 0.171338, \"1v2\": 0.057344, \"2v3\": 0.019524, \"3v4\": 0.009917, \"4v5\": 0.008846}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9876, \"ci_lower\": 0.9851, \"ci_upper\": 0.99, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.8047, \"ci_lower\": 0.7934, \"ci_upper\": 0.8162, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.6544, \"ci_lower\": 0.6401, \"ci_upper\": 0.6688, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.55, \"ci_lower\": 0.534, \"ci_upper\": 0.5657, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5284, \"ci_lower\": 0.5122, \"ci_upper\": 0.5443, \"perm_p\": 0.001}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"n_samples\": 2200, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_mean\", \"surp_d1_skew\", \"surp_d1_mean\"], \"ordinal\": {\"MAE\": 0.8518, \"Accuracy\": 0.4545}, \"key_finding\": \"Pythia-1.4B on arXiv yields K*=3, identical to exp-024 (Qwen on arXiv). 2v3 CI lower=0.6401 > θ=0.60. Domain saturation depth is model-invariant for arXiv.\"}}, \"exp_020_pythia_decoding\": {\"status\": \"DONE\", \"metrics\": {\"greedy\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9992, \"1v2\": 0.8838, \"2v3\": 0.5342, \"3v4\": 0.5228, \"4v5\": 0.5162}}, \"nuc09\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9948, \"1v2\": 0.677, \"2v3\": 0.5549, \"3v4\": 0.5299, \"4v5\": 0.5013}}, \"t07\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9965, \"1v2\": 0.7265, \"2v3\": 0.5941, \"3v4\": 0.5698, \"4v5\": 0.5284}}, \"t12\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9933, \"1v2\": 0.6172, \"2v3\": 0.5226, \"3v4\": 0.517, \"4v5\": 0.5051}}}}, \"exp_021_length_ablation\": {\"status\": \"DONE\", \"metrics\": {\"128tok\": {\"K_star\": 2, \"1v2_auc\": 0.6219}, \"256tok\": {\"K_star\": 2, \"1v2_auc\": 0.6282}, \"512tok\": {\"K_star\": 2, \"1v2_auc\": 0.6073}, \"all_K_star_2\": true, \"bootstrap_ci\": {\"512tok_1v2\": {\"auc\": 0.6073, \"ci_lower\": 0.5979, \"ci_upper\": 0.6166, \"perm_p\": 0.0001, \"verdict\": \"BORDERLINE\"}}}}, \"exp_018_llama8b_depth\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9225, \"1v2\": 0.6123, \"2v3\": 0.5274, \"3v4\": 0.5138, \"4v5\": 0.5097}, \"jsd\": {\"0v1\": 0.077, \"1v2\": 0.012, \"2v3\": 0.005}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9224, \"ci_lower\": 0.9174, \"ci_upper\": 0.9272, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6123, \"ci_lower\": 0.6028, \"ci_upper\": 0.6216, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5273, \"ci_lower\": 0.5169, \"ci_upper\": 0.5378, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5168, \"ci_lower\": 0.5062, \"ci_upper\": 0.5275, \"perm_p\": 0.0037}, \"4v5\": {\"auc\": 0.5159, \"ci_lower\": 0.5052, \"ci_upper\": 0.5268, \"perm_p\": 0.0035}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000}}, \"exp_023_domain_ablation\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 2, \"1v2_auc\": 0.6193, \"2v3_auc\": 0.5498, \"all_folds_above_060\": true, \"top_feature\": \"freq_entropy\", \"ordinal_accuracy\": 0.377}}, \"exp_019b_mistral_cross_scorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9209, \"1v2\": 0.5695, \"2v3\": 0.5335, \"3v4\": 0.514, \"4v5\": 0.5184}, \"bootstrap_ci\": {\"0v1\": {\"mean\": 0.9209, \"ci_lower\": 0.9189, \"ci_upper\": 0.9229, \"pass_060\": true}, \"1v2\": {\"mean\": 0.5696, \"ci_lower\": 0.5645, \"ci_upper\": 0.5746, \"pass_060\": false}, \"2v3\": {\"mean\": 0.5335, \"ci_lower\": 0.5283, \"ci_upper\": 0.5382, \"pass_060\": false}, \"3v4\": {\"mean\": 0.514, \"ci_lower\": 0.5063, \"ci_upper\": 0.5213, \"pass_060\": false}, \"4v5\": {\"mean\": 0.5183, \"ci_lower\": 0.5128, \"ci_upper\": 0.5244, \"pass_060\": false}}, \"jsd\": {\"0v1\": 0.08355, \"1v2\": 0.007642, \"2v3\": 0.004752, \"3v4\": 0.004255, \"4v5\": 0.003758}, \"ordinal_mae\": 1.3737, \"ordinal_accuracy\": 0.3179, \"top3_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_d1_mean\"], \"key_finding\": \"Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2 AUC=0.5695 (self-scorer was 0.5935) — cross-scorer LOWER, not higher. Mistral K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact.\"}}, \"exp_019_mistral7b_depth\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9843, \"1v2\": 0.5935, \"2v3\": 0.5402, \"3v4\": 0.5232, \"4v5\": 0.5181}, \"bootstrap_ci_1v2\": {\"ci_lower\": 0.5835, \"ci_upper\": 0.6032, \"p_auc_leq_060\": 0.9017}, \"jsd\": {\"0v1\": 0.124194, \"1v2\": 0.008051, \"2v3\": 0.005047, \"3v4\": 0.004516, \"4v5\": 0.004109}, \"ordinal_mae\": 1.2275, \"ordinal_accuracy\": 0.3567, \"top3_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_d1_mean\"]}}, \"exp_016_base_vs_instruct\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.987, \"1v2\": 0.6262, \"2v3\": 0.5496, \"3v4\": 0.5294, \"4v5\": 0.5182}, \"pairwise_auc_std\": {\"0v1\": 0.0015, \"1v2\": 0.0152, \"2v3\": 0.0067, \"3v4\": 0.0132, \"4v5\": 0.0139}, \"pairwise_jsd\": {\"0v1\": 0.163726, \"1v2\": 0.01081, \"2v3\": 0.005311, \"3v4\": 0.003942, \"4v5\": 0.003522}, \"ordinal_mae\": 1.1691, \"ordinal_accuracy\": 0.3719, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_d1_skew\", \"surp_d1_mean\", \"surp_mean\"], \"n_samples\": 30000, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.987, \"ci_lower\": 0.9853, \"ci_upper\": 0.9885, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.626, \"ci_lower\": 0.6168, \"ci_upper\": 0.6353, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5397, \"ci_upper\": 0.56, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5293, \"ci_lower\": 0.5188, \"ci_upper\": 0.5399, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5181, \"ci_lower\": 0.5075, \"ci_upper\": 0.5288, \"perm_p\": 0.0016}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95% CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015, 0.6213] — no significant base-vs-instruct difference.\"}}, \"exp_003_decoding_ablation\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 2, \"K_star_robust\": true, \"bootstrap_ci\": {\"config1_greedy\": {\"0v1\": {\"auc\": 0.9796, \"ci\": [0.9772, 0.982], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6892, \"ci\": [0.6802, 0.6982], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5612, \"ci\": [0.5517, 0.5705], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.5405, \"ci\": [0.5308, 0.5502], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5137, \"ci\": [0.5033, 0.5238], \"perm_p\": 0.0082}}, \"config2_nuc09\": {\"0v1\": {\"auc\": 0.9945, \"ci\": [0.9934, 0.9956], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6862, \"ci\": [0.6774, 0.6951], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5917, \"ci\": [0.5824, 0.601], \"perm_p\": 0, \"note\": \"CI upper crosses theta=0.60\"}, \"3v4\": {\"auc\": 0.5468, \"ci\": [0.5369, 0.5568], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5066, \"ci\": [0.4959, 0.5173], \"perm_p\": 0.1199}}, \"config3_t07\": {\"0v1\": {\"auc\": 0.9877, \"ci\": [0.9857, 0.9896], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6885, \"ci\": [0.6797, 0.697], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5901, \"ci\": [0.5806, 0.5996], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.539, \"ci\": [0.5288, 0.5493], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5348, \"ci\": [0.5243, 0.5454], \"perm_p\": 0}}, \"config4_t12\": {\"0v1\": {\"auc\": 0.9982, \"ci\": [0.9975, 0.9987], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.7037, \"ci\": [0.6945, 0.7126], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.582, \"ci\": [0.5722, 0.5917], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.5293, \"ci\": [0.5185, 0.5399], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5237, \"ci\": [0.5132, 0.5347], \"perm_p\": 0.0001}}, \"resamples\": 10000, \"method\": \"GroupKFold(5) OOF + doc-level bootstrap + label permutation\"}}}, \"exp_004_7b_crossscale\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9644, \"1v2\": 0.6178, \"2v3\": 0.546, \"3v4\": 0.5225, \"4v5\": 0.5091}, \"pairwise_auc_std\": {\"0v1\": 0.0034, \"1v2\": 0.0081, \"2v3\": 0.0028, \"3v4\": 0.0113, \"4v5\": 0.0052}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9638, \"ci_lower\": 0.9607, \"ci_upper\": 0.9665, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6168, \"ci_lower\": 0.6079, \"ci_upper\": 0.6261, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5492, \"ci_lower\": 0.5388, \"ci_upper\": 0.5594, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5276, \"ci_lower\": 0.517, \"ci_upper\": 0.5375, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5085, \"ci_lower\": 0.4988, \"ci_upper\": 0.5191, \"perm_p\": 0.0676}}, \"bootstrap_resamples\": 1000, \"permutation_resamples\": 10000, \"pairwise_jsd\": {\"0v1\": 0.127422, \"1v2\": 0.010114, \"2v3\": 0.004798, \"3v4\": 0.004821, \"4v5\": 0.003335}, \"ordinal_mae\": 1.2156, \"ordinal_accuracy\": 0.3523, \"top_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_std\", \"surp_d1_mean\", \"surp_mean\"], \"key_finding\": \"K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60 (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676). FR-4 Warning resolved.\"}}, \"exp_E_paired_stats\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_significant_pairs\": \"8/15\", \"hellaswag_significant_pairs\": \"9/15\", \"binary_ours_vs_all_mmlu\": \"all significant\", \"max_cohen_d_mmlu\": 10.8, \"max_cohen_d_hellaswag\": 8.98, \"graduated_a09_vs_dsir_corrected_p\": 0.0523, \"cohen_d_method\": \"d_av (Lakens 2013)\", \"key_finding\": \"binary-ours significantly outperforms all alternatives on MMLU. On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni cummax bug fixed: MMLU 10/15→8/15. Cohen's d changed to d_av.\", \"bugfix_note\": \"Holm-Bonferroni cummax variable was never updated, causing 2 MMLU pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\"}}, \"exp_D_obd_n500\": {\"status\": \"DONE\", \"metrics\": {\"obd_accuracy_final\": 0.38, \"obd_ci\": [0.34, 0.422], \"mcnemar_vs_gpt55_p\": 0.0809, \"mcnemar_vs_claude_p\": 0.0693, \"mcnemar_significant\": false, \"multi_seed_std\": 0, \"per_depth\": {\"d0\": 0.96, \"d1\": 0.39, \"d2\": 0.14, \"d3\": 0.19, \"d4\": 0.22}, \"prob_merge_accuracy\": 0.444, \"prob_merge_d4_bias\": 0.8, \"note\": \"v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant — supports discussion.tex narrative\"}}, \"exp_B_14d_ablation\": {\"status\": \"DONE\", \"metrics\": {\"result\": \"K*=2 stable across all 4 models after removing self_BLEU (14D)\", \"key_finding\": \"self_BLEU removal does not change K* boundary. FR-3 resolved.\"}}, \"exp_A_alt_scorer\": {\"status\": \"DONE\", \"metrics\": {\"pythia_qwen_rw\": {\"k_star\": 2, \"auc_0v1\": 0.9923, \"auc_1v2\": 0.7012, \"auc_2v3\": 0.587, \"mae\": 1.006, \"accuracy\": 0.417, \"spearman_rho_vs_baseline\": 0.906}, \"pythia_qwen_cont\": {\"k_star\": 1, \"auc_0v1\": 0.99, \"auc_1v2\": 0.5923, \"auc_2v3\": null, \"mae\": 1.216, \"accuracy\": 0.371, \"spearman_rho_vs_baseline\": 0.942}, \"olmo_qwen_rw\": {\"k_star\": 2, \"auc_0v1\": 0.9918, \"auc_1v2\": 0.6947, \"auc_2v3\": null, \"mae\": 1.016, \"accuracy\": 0.413, \"spearman_rho_vs_baseline\": 0.92}, \"olmo_qwen_cont\": {\"k_star\": 1, \"auc_0v1\": 0.989, \"auc_1v2\": 0.5858, \"auc_2v3\": null, \"mae\": 1.229, \"accuracy\": 0.368, \"spearman_rho_vs_baseline\": 0.902}, \"key_finding\": \"K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1 (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer independence of feature ranking.\"}}, \"exp_015_neural_probe\": {\"status\": \"DONE\", \"metrics\": {\"pythia\": {\"k_star_neural\": 2, \"k_star_lgbm\": 2, \"accuracy\": 0.3892, \"pairwise_auc\": {\"0v1\": 0.966, \"1v2\": 0.676, \"2v3\": 0.596, \"3v4\": 0.555, \"4v5\": 0.532}}, \"olmo\": {\"k_star_neural\": 2, \"k_star_lgbm\": 2, \"accuracy\": 0.3729, \"pairwise_auc\": {\"0v1\": 0.95, \"1v2\": 0.657, \"2v3\": 0.589, \"3v4\": 0.547, \"4v5\": 0.53}}, \"qwen_cont\": {\"k_star_neural\": 3, \"k_star_lgbm\": 2, \"accuracy\": 0.4368, \"pairwise_auc\": {\"0v1\": 0.988, \"1v2\": 0.702, \"2v3\": 0.616, \"3v4\": 0.59, \"4v5\": 0.566}}, \"key_finding\": \"Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3 only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\"}}, \"exp_006_graduated_filtering\": {\"status\": \"DONE\", \"metrics\": {\"total_runs\": 51, \"binary_ours\": {\"mmlu\": \"0.5941±0.0008\", \"hellaswag\": \"0.6701±0.0006\"}, \"binary_drayson\": {\"mmlu\": \"0.5913±0.0009\", \"hellaswag\": \"0.6691±0.0004\"}, \"surprisal\": {\"mmlu\": \"0.5894±0.0009\", \"hellaswag\": \"0.6641±0.0006\"}, \"graduated_a09\": {\"mmlu\": \"0.5892±0.0008\", \"hellaswag\": \"0.6701±0.0007\"}, \"graduated_a07\": {\"mmlu\": \"0.5892±0.0014\", \"hellaswag\": \"0.6695±0.0004\"}, \"graduated_a05\": {\"mmlu\": \"0.5880±0.0013\", \"hellaswag\": \"0.6687±0.0008\"}, \"graduated_a03\": {\"mmlu\": \"0.5877±0.0013\", \"hellaswag\": \"0.6669±0.0005\"}, \"graduated_a01\": {\"mmlu\": \"0.5873±0.0019\", \"hellaswag\": \"0.6640±0.0009\"}, \"dsir\": {\"mmlu\": \"0.5869±0.0003\", \"hellaswag\": \"0.6631±0.0007\"}, \"no_filter\": {\"mmlu\": \"0.5865±0.0010\", \"hellaswag\": \"0.6638±0.0008\"}, \"base_model\": {\"mmlu\": \"0.6018\", \"hellaswag\": \"0.6821\"}, \"best_strategy\": \"binary-ours\", \"key_finding\": \"binary-ours is best filtering strategy. All strategies degrade vs base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR below all other strategies except no-filter.\"}}, \"exp_007_bootstrap_ci\": {\"status\": \"DONE\", \"metrics\": {\"qwen_rewrite\": {\"0v1\": {\"auc\": 0.9956, \"ci_lower\": 0.9946, \"ci_upper\": 0.9965, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6955, \"ci_lower\": 0.6859, \"ci_upper\": 0.7041, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5893, \"ci_lower\": 0.5795, \"ci_upper\": 0.5991, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5435, \"ci_lower\": 0.5333, \"ci_upper\": 0.5551, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.534, \"ci_lower\": 0.5238, \"ci_upper\": 0.5448, \"perm_p\": 0.002}}, \"pythia_cont\": {\"0v1\": {\"auc\": 0.9932, \"ci_lower\": 0.9921, \"ci_upper\": 0.9943, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6539, \"ci_lower\": 0.6454, \"ci_upper\": 0.663, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5514, \"ci_lower\": 0.5417, \"ci_upper\": 0.5628, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5152, \"ci_lower\": 0.5041, \"ci_upper\": 0.526, \"perm_p\": 0.006}, \"4v5\": {\"auc\": 0.5136, \"ci_lower\": 0.5021, \"ci_upper\": 0.5249, \"perm_p\": 0.008}}, \"olmo_cont\": {\"0v1\": {\"auc\": 0.997, \"ci_lower\": 0.9964, \"ci_upper\": 0.9975, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6145, \"ci_lower\": 0.6045, \"ci_upper\": 0.6247, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5399, \"ci_upper\": 0.5596, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5091, \"ci_lower\": 0.4973, \"ci_upper\": 0.52, \"perm_p\": 0.064}, \"4v5\": {\"auc\": 0.5045, \"ci_lower\": 0.4932, \"ci_upper\": 0.515, \"perm_p\": 0.232}}, \"qwen_cont\": {\"0v1\": {\"auc\": 0.9971, \"ci_lower\": 0.9963, \"ci_upper\": 0.9978, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6112, \"ci_lower\": 0.6015, \"ci_upper\": 0.6213, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5609, \"ci_lower\": 0.5511, \"ci_upper\": 0.5712, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5409, \"ci_lower\": 0.5308, \"ci_upper\": 0.5508, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.5141, \"ci_lower\": 0.5035, \"ci_upper\": 0.5255, \"perm_p\": 0.006}}, \"k_star_robust\": true, \"all_1v2_ci_lower_above_060\": true, \"most_marginal\": \"Qwen-cont CI lower=0.6015, only 0.0015 above threshold\"}}, \"exp_011_llm_zeroshot\": {\"status\": \"DONE\", \"metrics\": {\"gpt55_5class_acc\": 0.332, \"gpt55_mae\": 1.102, \"gpt55_spearman\": 0.383, \"gpt55_binary_acc\": 0.878, \"claude_5class_acc\": 0.331, \"claude_mae\": 1.15, \"claude_spearman\": 0.416, \"claude_binary_acc\": 0.882, \"odb_baseline_5class_acc\": 0.386, \"odb_baseline_mae\": 1.107, \"gpt55_per_depth_acc\": {\"depth_0\": 0.77, \"depth_1\": 0.19, \"depth_2\": 0.38, \"depth_3\": 0.24, \"depth_4\": 0.08}, \"claude_per_depth_acc\": {\"depth_0\": 0.69, \"depth_1\": 0.21, \"depth_2\": 0.28, \"depth_3\": 0.101, \"depth_4\": 0.37}, \"n_samples_per_model\": 500, \"key_finding\": \"Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails.\"}}, \"exp_013_cross_transfer\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_matrix\": {\"Qwen_rw→Qwen_rw\": 0.4229, \"Qwen_rw→Pythia\": 0.259, \"Qwen_rw→OLMo\": 0.2653, \"Qwen_rw→Qwen_cont\": 0.3466, \"Pythia→Qwen_rw\": 0.2718, \"Pythia→Pythia\": 0.3856, \"Pythia→OLMo\": 0.3531, \"Pythia→Qwen_cont\": 0.3287, \"OLMo→Qwen_rw\": 0.2768, \"OLMo→Pythia\": 0.345, \"OLMo→OLMo\": 0.3822, \"OLMo→Qwen_cont\": 0.3244, \"Qwen_cont→Qwen_rw\": 0.344, \"Qwen_cont→Pythia\": 0.3284, \"Qwen_cont→OLMo\": 0.3112, \"Qwen_cont→Qwen_cont\": 0.3875}, \"transfer_retention_accuracy\": {\"Pythia↔OLMo\": \"91-92%\", \"Qwen_rw→Pythia/OLMo\": \"61-63%\", \"Qwen_cont↔Pythia\": \"83-85%\", \"Qwen_cont↔OLMo\": \"80-85%\"}, \"transfer_retention_tau\": {\"Pythia↔OLMo\": \"85-86%\", \"Qwen_rw→Pythia/OLMo\": \"45-50%\", \"Qwen_cont↔others\": \"68-83%\"}, \"mean_pw_auc_matrix\": {\"within_avg\": 0.6099, \"cross_avg\": 0.5905, \"0v1_cross_all_above\": 0.96}, \"key_finding\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better.\"}}, \"exp_010_ordinal_baseline\": {\"status\": \"DONE\", \"metrics\": {\"qwen_rewrite\": {\"obd_lgbm\": {\"accuracy\": 0.4229, \"mae\": 0.9836, \"tau_b\": 0.5518, \"mean_pw_auc\": 0.6214}, \"multiclass_lgbm\": {\"accuracy\": 0.4182, \"mae\": 1.0163, \"tau_b\": 0.5367, \"mean_pw_auc\": 0.6246}, \"ordinal_logreg\": {\"accuracy\": 0.3636, \"mae\": 0.9105, \"tau_b\": 0.563, \"mean_pw_auc\": 0.5022}}, \"pythia\": {\"obd_lgbm\": {\"accuracy\": 0.3856, \"mae\": 1.1072, \"tau_b\": 0.4745, \"mean_pw_auc\": 0.6055}, \"multiclass_lgbm\": {\"accuracy\": 0.3832, \"mae\": 1.1399, \"tau_b\": 0.4622, \"mean_pw_auc\": 0.6062}, \"ordinal_logreg\": {\"accuracy\": 0.3179, \"mae\": 1.022, \"tau_b\": 0.49, \"mean_pw_auc\": 0.4767}}, \"olmo\": {\"obd_lgbm\": {\"accuracy\": 0.3822, \"mae\": 1.1469, \"tau_b\": 0.4683, \"mean_pw_auc\": 0.6015}, \"multiclass_lgbm\": {\"accuracy\": 0.3685, \"mae\": 1.1813, \"tau_b\": 0.4497, \"mean_pw_auc\": 0.5974}, \"ordinal_logreg\": {\"accuracy\": 0.3265, \"mae\": 1.0352, \"tau_b\": 0.4656, \"mean_pw_auc\": 0.4859}}}}, \"exp_001_pythia_depth\": {\"status\": \"DONE\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9932, \"1v2\": 0.6539, \"2v3\": 0.5515, \"3v4\": 0.5153, \"4v5\": 0.5135}, \"pairwise_auc_std\": {\"0v1\": 0.0007, \"1v2\": 0.0069, \"2v3\": 0.0137, \"3v4\": 0.0084, \"4v5\": 0.0078}, \"pairwise_jsd\": {\"0v1\": 0.2142, \"1v2\": 0.014, \"2v3\": 0.0051, \"3v4\": 0.0033, \"4v5\": 0.0031}, \"k_star\": 2, \"ordinal_mae\": 1.14, \"ordinal_accuracy\": 0.383}}, \"mvp_pilot_sat_v1\": {\"status\": \"DONE\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9956, \"1v2\": 0.6957, \"2v3\": 0.5893, \"3v4\": 0.5434, \"4v5\": 0.5343}, \"pairwise_auc_std\": {\"0v1\": 0.0005, \"1v2\": 0.0072, \"2v3\": 0.012, \"3v4\": 0.0053, \"4v5\": 0.0091}, \"pairwise_jsd\": {\"0v1\": 0.2669, \"1v2\": 0.0163, \"2v3\": 0.0069, \"3v4\": 0.0047, \"4v5\": 0.0041}, \"k_star\": 2, \"ordinal_mae\": 1.0163, \"ordinal_accuracy\": 0.4182}}}, \"count\": 75, \"total\": 75, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2975}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "218cd9fe-f8b4-42d5-b6a8-2632fb774f8b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_pythia_retrain_depth7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"kstar\\\": 7, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9844, \\\"1v2\\\": 0.947, \\\"2v3\\\": 0.8891, \\\"3v4\\\": 0.7999, \\\"4v5\\\": 0.6907, \\\"5v6\\\": 0.6497, \\\"6v7\\\": 0.634}, \\\"pairwise_auc_ci\\\": {\\\"0v1\\\": [0.9829, 0.9858], \\\"1v2\\\": [0.9418, 0.9522], \\\"2v3\\\": [0.8822, 0.896], \\\"3v4\\\": [0.7951, 0.8047], \\\"4v5\\\": [0.688, 0.6934], \\\"5v6\\\": [0.6429, 0.6565], \\\"6v7\\\": [0.6275, 0.6406]}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.1775, \\\"1v2\\\": 0.1286, \\\"2v3\\\": 0.1069, \\\"3v4\\\": 0.0643, \\\"4v5\\\": 0.0331, \\\"5v6\\\": 0.0271, \\\"6v7\\\": 0.0138}}}, \\\"exp_qwen_retrain_depth7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 7, \\\"theta\\\": 0.6, \\\"max_depth\\\": 7, \\\"analysis_method\\\": \\\"5-fold GroupKFold CV\\\", \\\"pairwise_auc\\\": {\\\"0v1\\\": {\\\"mean\\\": 0.9837, \\\"std\\\": 0.0019, \\\"ci_95\\\": [0.9821, 0.9854], \\\"folds\\\": [0.9832, 0.9821, 0.9837, 0.9823, 0.9873]}, \\\"1v2\\\": {\\\"mean\\\": 0.8971, \\\"std\\\": 0.0025, \\\"ci_95\\\": [0.8949, 0.8993], \\\"folds\\\": [0.8923, 0.8988, 0.8986, 0.8991, 0.8967]}, \\\"2v3\\\": {\\\"mean\\\": 0.8098, \\\"std\\\": 0.0052, \\\"ci_95\\\": [0.8052, 0.8144], \\\"folds\\\": [0.8086, 0.8074, 0.818, 0.8024, 0.8128]}, \\\"3v4\\\": {\\\"mean\\\": 0.76, \\\"std\\\": 0.0082, \\\"ci_95\\\": [0.7528, 0.7672], \\\"folds\\\": [0.7534, 0.7617, 0.7753, 0.7566, 0.7531]}, \\\"4v5\\\": {\\\"mean\\\": 0.7459, \\\"std\\\": 0.0091, \\\"ci_95\\\": [0.7379, 0.7538], \\\"folds\\\": [0.7429, 0.7562, 0.7521, 0.73, 0.7482]}, \\\"5v6\\\": {\\\"mean\\\": 0.7017, \\\"std\\\": 0.0068, \\\"ci_95\\\": [0.6958, 0.7076], \\\"folds\\\": [0.7006, 0.7077, 0.7104, 0.6915, 0.6984]}, \\\"6v7\\\": {\\\"mean\\\": 0.641, \\\"std\\\": 0.0039, \\\"ci_95\\\": [0.6376, 0.6445], \\\"folds\\\": [0.6419, 0.6349, 0.6464, 0.639, 0.643]}}, \\\"jsd\\\": {\\\"0v1\\\": 0.23005, \\\"1v2\\\": 0.103924, \\\"2v3\\\": 0.075049, \\\"3v4\\\": 0.065398, \\\"4v5\\\": 0.060509, \\\"5v6\\\": 0.034998, \\\"6v7\\\": 0.017652}}}, \\\"exp_code_pythia1b4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 1, \\\"theta\\\": 0.6, \\\"pairwise_auc\\\": {\\\"0v1\\\": {\\\"mean\\\": 0.9592, \\\"std\\\": 0.0036, \\\"folds\\\": [0.9576, 0.9576, 0.9657, 0.96, 0.9552]}, \\\"1v2\\\": {\\\"mean\\\": 0.5983, \\\"std\\\": 0.005, \\\"folds\\\": [0.601, 0.5884, 0.6, 0.5997, 0.6024]}, \\\"2v3\\\": {\\\"mean\\\": 0.5215, \\\"std\\\": 0.0128, \\\"folds\\\": [0.5236, 0.5124, 0.5311, 0.5024, 0.5381]}, \\\"3v4\\\": {\\\"mean\\\": 0.5152, \\\"std\\\": 0.012, \\\"folds\\\": [0.4981, 0.5327, 0.5092, 0.5123, 0.5238]}, \\\"4v5\\\": {\\\"mean\\\": 0.5046, \\\"std\\\": 0.0137, \\\"folds\\\": [0.4983, 0.4822, 0.5074, 0.5224, 0.5128]}}, \\\"jsd\\\": {\\\"0v1\\\": 0.070173, \\\"1v2\\\": 0.008211, \\\"2v3\\\": 0.003674, \\\"3v4\\\": 0.002902, \\\"4v5\\\": 0.002685}, \\\"ordinal\\\": {\\\"mae\\\": 1.3268, \\\"accuracy\\\": 0.3357}, \\\"top_features\\\": [\\\"freq_entropy\\\", \\\"surp_d1_mean\\\", \\\"surp_d2_mean\\\", \\\"surp_mean\\\", \\\"surp_d1_skew\\\"], \\\"features_csv\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4/features.csv\\\"}}, \\\"exp_028_power_curve\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"min_n_100pct\\\": 2000, \\\"n500_auc\\\": 0.5808, \\\"n500_rate\\\": 0.2, \\\"n1000_auc\\\": 0.5911, \\\"n1000_rate\\\": 0.3, \\\"n2000_auc\\\": 0.6101, \\\"n2000_rate\\\": 1, \\\"n3000_auc\\\": 0.6166, \\\"n3000_rate\\\": 1, \\\"n4000_auc\\\": 0.622, \\\"n4000_rate\\\": 1, \\\"n5000_auc\\\": 0.6288, \\\"n5000_rate\\\": 1}}, \\\"exp_qwen_retrain_chain\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star_lower_bound\\\": 4, \\\"theta\\\": 0.6, \\\"auc_0v1\\\": 0.9838, \\\"auc_1v2\\\": 0.8969, \\\"auc_2v3\\\": 0.81, \\\"auc_3v4\\\": 0.7624, \\\"ci_0v1\\\": [0.982, 0.9855], \\\"ci_1v2\\\": [0.8937, 0.9001], \\\"ci_2v3\\\": [0.8052, 0.8147], \\\"ci_3v4\\\": [0.7543, 0.7706], \\\"ci_method\\\": \\\"5-fold CV\\\", \\\"jsd_0v1\\\": 0.2263, \\\"jsd_1v2\\\": 0.1046, \\\"jsd_2v3\\\": 0.0752, \\\"jsd_3v4\\\": 0.0654}}, \\\"exp_code_qwen1b5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 2, \\\"theta\\\": 0.6, \\\"auc_0v1\\\": 0.9388, \\\"auc_1v2\\\": 0.7382, \\\"auc_2v3\\\": 0.53, \\\"auc_3v4\\\": 0.5022, \\\"auc_4v5\\\": 0.5219, \\\"ci_0v1\\\": [0.929, 0.949], \\\"ci_1v2\\\": [0.709, 0.767], \\\"ci_2v3\\\": [0.514, 0.546], \\\"jsd_0v1\\\": 0.0814, \\\"jsd_1v2\\\": 0.0443, \\\"jsd_2v3\\\": 0.0038, \\\"ordinal_accuracy\\\": 0.359, \\\"ordinal_mae\\\": 1.204}}, \\\"exp_olmo_retrain_chain\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_028_subsampling_power\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_1000\\\": {\\\"mean_auc\\\": 0.608, \\\"std\\\": 0.012, \\\"detection_prob\\\": 0.9}, \\\"n_2500\\\": {\\\"mean_auc\\\": 0.618, \\\"std\\\": 0.006, \\\"detection_prob\\\": 1}, \\\"n_5000\\\": {\\\"mean_auc\\\": 0.629, \\\"std\\\": 0, \\\"detection_prob\\\": 1}, \\\"key_finding\\\": \\\"n>=2500 gives 100% reliable K*=2 detection. n=1000 already 90%. Signal is robust, not large-sample artifact.\\\"}}, \\\"exp_026_arxiv_filtering\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"runs_completed\\\": \\\"15/15\\\", \\\"strategies\\\": [\\\"no_filter\\\", \\\"binary\\\", \\\"graduated_a09\\\"], \\\"seeds\\\": [42, 123, 456, 789, 1024], \\\"mmlu\\\": {\\\"no_filter\\\": \\\"0.5899±0.0008\\\", \\\"binary\\\": \\\"0.5876±0.0004\\\", \\\"graduated_a09\\\": \\\"0.5900±0.0011\\\"}, \\\"hellaswag\\\": {\\\"no_filter\\\": \\\"0.6600±0.0002\\\", \\\"binary\\\": \\\"0.6642±0.0004\\\", \\\"graduated_a09\\\": \\\"0.6599±0.0003\\\"}, \\\"delta_vs_no_filter\\\": {\\\"binary_mmlu\\\": \\\"-0.0023\\\", \\\"binary_hellaswag\\\": \\\"+0.0042\\\", \\\"graduated_mmlu\\\": \\\"+0.0001\\\", \\\"graduated_hellaswag\\\": \\\"-0.0001\\\"}, \\\"key_finding\\\": \\\"All three strategies produce nearly identical results. Graduated ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\\\"}}, \\\"exp_027_latex_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 3, \\\"k_star_preserved\\\": true, \\\"pairwise_auc_original\\\": {\\\"0v1\\\": 0.9948, \\\"1v2\\\": 0.8581, \\\"2v3\\\": 0.6436, \\\"3v4\\\": 0.544, \\\"4v5\\\": 0.5299}, \\\"pairwise_auc_stripped\\\": {\\\"0v1\\\": 0.9948, \\\"1v2\\\": 0.8297, \\\"2v3\\\": 0.6229, \\\"3v4\\\": 0.5468, \\\"4v5\\\": 0.5476}, \\\"auc_delta\\\": {\\\"0v1\\\": 0, \\\"1v2\\\": -0.028, \\\"2v3\\\": -0.021, \\\"3v4\\\": 0.003, \\\"4v5\\\": 0.018}, \\\"latex_reduction_by_depth\\\": {\\\"depth_0\\\": \\\"0.6%\\\", \\\"depth_5\\\": \\\"4.4%\\\"}, \\\"key_finding\\\": \\\"K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still >θ=0.60). LaTeX format is NOT a confound.\\\"}}, \\\"exp_025_pythia_filtering\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"runs_completed\\\": \\\"9/9\\\", \\\"strategies\\\": [\\\"no_filter\\\", \\\"binary_ours\\\", \\\"graduated_a09\\\"], \\\"seeds\\\": [42, 123, 456], \\\"mmlu\\\": {\\\"no_filter\\\": \\\"0.2568±0.0012\\\", \\\"binary_ours\\\": \\\"0.2585±0.0004\\\", \\\"graduated_a09\\\": \\\"0.2561±0.0009\\\"}, \\\"hellaswag\\\": {\\\"no_filter\\\": \\\"0.5250±0.0008\\\", \\\"binary_ours\\\": \\\"0.5251±0.0001\\\", \\\"graduated_a09\\\": \\\"0.5253±0.0007\\\"}, \\\"delta_vs_no_filter\\\": {\\\"binary_ours_mmlu\\\": \\\"+0.0017\\\", \\\"binary_ours_hellaswag\\\": \\\"+0.0000\\\", \\\"graduated_a09_mmlu\\\": \\\"-0.0007\\\", \\\"graduated_a09_hellaswag\\\": \\\"+0.0003\\\"}, \\\"key_finding\\\": \\\"All three filtering strategies produce nearly identical results on Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering binary>graduated>no_filter NOT confirmed.\\\"}}, \\\"exp_14b_c4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9598, \\\"1v2\\\": 0.621, \\\"2v3\\\": 0.5494, \\\"3v4\\\": 0.5243, \\\"4v5\\\": 0.5154}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.1097, \\\"1v2\\\": 0.0112, \\\"2v3\\\": 0.0062, \\\"3v4\\\": 0.0044, \\\"4v5\\\": 0.0036}, \\\"bootstrap_ci\\\": {\\\"0v1\\\": [0.9564, 0.963], \\\"1v2\\\": [0.6119, 0.6304], \\\"2v3\\\": [0.5392, 0.5594], \\\"3v4\\\": [0.514, 0.5346], \\\"4v5\\\": [0.5045, 0.5265]}, \\\"permutation_p\\\": {\\\"0v1\\\": \\\"<0.001\\\", \\\"1v2\\\": \\\"<0.001\\\", \\\"2v3\\\": \\\"<0.001\\\", \\\"3v4\\\": \\\"<0.001\\\", \\\"4v5\\\": \\\"<0.001\\\"}, \\\"k_star_statistically_confirmed\\\": true, \\\"ordinal_mae\\\": 1.2266, \\\"ordinal_accuracy\\\": 0.3497, \\\"top_features\\\": [\\\"freq_entropy\\\", \\\"surp_d1_skew\\\", \\\"surp_std\\\", \\\"surp_d1_mean\\\", \\\"surp_d2_mean\\\"], \\\"key_finding\\\": \\\"K*=2 confirmed at 14B scale with bootstrap CI. 1v2 CI lower (0.6119) > theta=0.60; 2v3 CI upper (0.5594) < theta=0.60. All permutation p<0.001.\\\"}}, \\\"exp_arXiv_mistral7b_crossscorer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 3, \\\"scorer\\\": \\\"pythia-1.4b\\\", \\\"auc_0v1\\\": 0.9798, \\\"auc_1v2\\\": 0.8141, \\\"auc_2v3\\\": 0.6075, \\\"auc_3v4\\\": 0.5489, \\\"auc_4v5\\\": 0.5391, \\\"jsd_0v1\\\": 0.135575, \\\"jsd_1v2\\\": 0.078, \\\"jsd_2v3\\\": 0.020452, \\\"jsd_3v4\\\": 0.010992, \\\"jsd_4v5\\\": 0.008831, \\\"ordinal_mae\\\": 0.9061, \\\"ordinal_accuracy\\\": 0.4412}}, \\\"exp_arXiv_llama8b_crossscorer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 3, \\\"auc_0v1\\\": 0.9629, \\\"auc_1v2\\\": 0.8433, \\\"auc_2v3\\\": 0.6201, \\\"auc_3v4\\\": 0.523, \\\"auc_4v5\\\": 0.5245, \\\"jsd_0v1\\\": 0.1214, \\\"jsd_1v2\\\": 0.0815, \\\"jsd_2v3\\\": 0.0195, \\\"jsd_3v4\\\": 0.0083, \\\"jsd_4v5\\\": 0.0082, \\\"ordinal_mae\\\": 0.9025, \\\"ordinal_accuracy\\\": 0.4407, \\\"scorer\\\": \\\"pythia-1.4b\\\"}}, \\\"exp_arXiv_qwen7b_crossscorer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 2, \\\"auc_0v1\\\": 0.9575, \\\"auc_1v2\\\": 0.8171, \\\"auc_2v3\\\": 0.5989, \\\"auc_3v4\\\": 0.5417, \\\"auc_4v5\\\": 0.5192, \\\"jsd_0v1\\\": 0.137085, \\\"jsd_1v2\\\": 0.059688, \\\"jsd_2v3\\\": 0.013508, \\\"jsd_3v4\\\": 0.009125, \\\"jsd_4v5\\\": 0.006738, \\\"ordinal_mae\\\": 0.9617, \\\"ordinal_accuracy\\\": 0.4255}}, \\\"exp_arXiv_qwen1b5_crossscorer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 3, \\\"auc_0v1\\\": 0.9748, \\\"auc_1v2\\\": 0.8105, \\\"auc_2v3\\\": 0.6317, \\\"auc_3v4\\\": 0.5437, \\\"auc_4v5\\\": 0.5294, \\\"jsd_0v1\\\": 0.154297, \\\"jsd_1v2\\\": 0.066782, \\\"jsd_2v3\\\": 0.019268, \\\"jsd_3v4\\\": 0.008867, \\\"jsd_4v5\\\": 0.006991, \\\"ordinal_mae\\\": 0.9017, \\\"ordinal_accuracy\\\": 0.4402}}, \\\"exp_wiki_scorer_confound_1b5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 1, \\\"confound_verdict\\\": \\\"confirmed\\\", \\\"auc_0v1\\\": 0.9729, \\\"auc_1v2\\\": 0.5994, \\\"auc_2v3\\\": 0.533, \\\"auc_3v4\\\": 0.5214, \\\"auc_4v5\\\": 0.5068, \\\"jsd_0v1\\\": 0.0886, \\\"ordinal_mae\\\": 1.2995, \\\"ordinal_accuracy\\\": 0.3466}}, \\\"exp_wiki_scorer_confound\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 1, \\\"confound_verdict\\\": \\\"confirmed\\\", \\\"auc_0v1\\\": 0.9404, \\\"auc_1v2\\\": 0.587, \\\"auc_2v3\\\": 0.5456, \\\"auc_3v4\\\": 0.525, \\\"auc_4v5\\\": 0.5172, \\\"critical_delta_1v2\\\": -0.0238}}, \\\"exp_wiki_qwen7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 2, \\\"auc_0v1\\\": 0.9673, \\\"auc_1v2\\\": 0.6108, \\\"auc_2v3\\\": 0.5562, \\\"auc_3v4\\\": 0.5297, \\\"auc_4v5\\\": 0.529, \\\"jsd_0v1\\\": 0.083514, \\\"jsd_1v2\\\": 0.010991, \\\"jsd_2v3\\\": 0.00555, \\\"jsd_3v4\\\": 0.004611, \\\"jsd_4v5\\\": 0.003894, \\\"ordinal_mae\\\": 1.2501, \\\"ordinal_accuracy\\\": 0.3532}}, \\\"exp_wiki_mistral7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 1, \\\"ordinal_mae\\\": 1.3445, \\\"ordinal_accuracy\\\": 0.3273, \\\"auc_0v1\\\": 0.9607, \\\"auc_1v2\\\": 0.5552, \\\"auc_2v3\\\": 0.5236, \\\"auc_3v4\\\": 0.5181, \\\"auc_4v5\\\": 0.5012, \\\"jsd_0v1\\\": 0.054134, \\\"jsd_1v2\\\": 0.005678, \\\"jsd_2v3\\\": 0.003698, \\\"jsd_3v4\\\": 0.003459, \\\"jsd_4v5\\\": 0.003274}}, \\\"exp_wiki_llama8b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 1, \\\"ordinal_mae\\\": 1.2954, \\\"ordinal_accuracy\\\": 0.3313, \\\"auc_0v1\\\": 0.9316, \\\"auc_1v2\\\": 0.5954, \\\"auc_2v3\\\": 0.5392, \\\"auc_3v4\\\": 0.5221, \\\"auc_4v5\\\": 0.5212, \\\"jsd_0v1\\\": 0.06169, \\\"jsd_1v2\\\": 0.00931}}, \\\"exp_arXiv_qwen7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 3, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.983, \\\"1v2\\\": 0.835, \\\"2v3\\\": 0.626, \\\"3v4\\\": 0.544, \\\"4v5\\\": 0.513}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.1656, \\\"1v2\\\": 0.0668, \\\"2v3\\\": 0.0156, \\\"3v4\\\": 0.0089, \\\"4v5\\\": 0.0061}, \\\"ordinal_mae\\\": 0.9, \\\"ordinal_accuracy\\\": 0.446}}, \\\"exp_arXiv_mistral7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 3, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9848, \\\"1v2\\\": 0.8201, \\\"2v3\\\": 0.6275, \\\"3v4\\\": 0.5295, \\\"4v5\\\": 0.5295}, \\\"jsd\\\": {\\\"0v1\\\": 0.14249, \\\"1v2\\\": 0.076232, \\\"2v3\\\": 0.018972, \\\"3v4\\\": 0.009908, \\\"4v5\\\": 0.008877}, \\\"ordinal_mae\\\": 0.8958, \\\"ordinal_accuracy\\\": 0.4474, \\\"top_features\\\": [\\\"freq_entropy\\\", \\\"surp_std\\\", \\\"surp_d1_skew\\\", \\\"surp_mean\\\", \\\"surp_d2_mean\\\"]}}, \\\"exp_arXiv_llama8b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 3, \\\"auc_0v1\\\": 0.9754, \\\"auc_1v2\\\": 0.8447, \\\"auc_2v3\\\": 0.6215, \\\"auc_3v4\\\": 0.5362, \\\"auc_4v5\\\": 0.5331, \\\"jsd_0v1\\\": 0.1296, \\\"jsd_1v2\\\": 0.0785, \\\"jsd_2v3\\\": 0.0177, \\\"ordinal_acc\\\": 0.4549, \\\"ordinal_mae\\\": 0.8806}}, \\\"exp_wiki_pythia_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 1, \\\"auc_0v1\\\": 0.975, \\\"auc_1v2\\\": 0.5846, \\\"auc_2v3\\\": 0.5445, \\\"auc_3v4\\\": 0.5205, \\\"auc_4v5\\\": 0.5168, \\\"jsd_0v1\\\": 0.080065, \\\"jsd_1v2\\\": 0.007773, \\\"ordinal_acc\\\": 0.3503}}, \\\"exp_wiki_olmo_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 1, \\\"auc_0v1\\\": 0.9932, \\\"auc_1v2\\\": 0.4986, \\\"auc_2v3\\\": 0.5012, \\\"auc_3v4\\\": 0.5057, \\\"auc_4v5\\\": 0.5009, \\\"jsd_0v1\\\": 0.1688, \\\"ordinal_acc\\\": 0.3227}}, \\\"exp_arXiv_olmo\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 1, \\\"auc_0v1\\\": 0.9958, \\\"auc_1v2\\\": 0.5034, \\\"auc_2v3\\\": 0.5069, \\\"auc_3v4\\\": 0.5021, \\\"auc_4v5\\\": 0.5037, \\\"jsd_0v1\\\": 0.329, \\\"ordinal_acc\\\": 0.33}}, \\\"exp_wiki_olmo\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_wiki_pythia\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_009_dose_response\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_runs\\\": 45, \\\"seeds\\\": 5, \\\"ratios\\\": [0.1, 0.3, 0.5], \\\"strategies\\\": [\\\"no_filter\\\", \\\"binary_ours\\\", \\\"graduated\\\"], \\\"cross_ratio_finding\\\": \\\"Binary filtering consistently best across all ratios. Graduated filtering = no_filter at every ratio. Effect size of binary advantage increases with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp). Original C3 hypothesis (graduated > binary) rejected.\\\", \\\"gpu_hours_total\\\": 9.9}}, \\\"exp_009_dose_50pct_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seeds\\\": 5, \\\"strategies\\\": 3, \\\"total_runs\\\": 15, \\\"mean_std\\\": {\\\"no_filter\\\": {\\\"mmlu\\\": \\\"0.6063±0.0013\\\", \\\"hellaswag\\\": \\\"0.6680±0.0005\\\"}, \\\"binary_ours\\\": {\\\"mmlu\\\": \\\"0.6088±0.0011\\\", \\\"hellaswag\\\": \\\"0.6731±0.0004\\\"}, \\\"graduated\\\": {\\\"mmlu\\\": \\\"0.6062±0.0009\\\", \\\"hellaswag\\\": \\\"0.6679±0.0002\\\"}}, \\\"paired_ttest\\\": {\\\"binary_vs_nofilter\\\": {\\\"delta_mmlu\\\": 0.0025, \\\"p_mmlu\\\": 0.0377, \\\"delta_hellaswag\\\": 0.0051, \\\"p_hellaswag\\\": 2e-05}, \\\"graduated_vs_binary\\\": {\\\"delta_mmlu\\\": -0.0026, \\\"p_mmlu\\\": 0.0257, \\\"delta_hellaswag\\\": -0.0052, \\\"p_hellaswag\\\": 3e-05}, \\\"graduated_vs_nofilter\\\": {\\\"delta_mmlu\\\": -0.0001, \\\"p_mmlu\\\": 0.89, \\\"delta_hellaswag\\\": -0.0001, \\\"p_hellaswag\\\": 0.706}}, \\\"key_finding\\\": \\\"Binary significantly best (HellaSwag p<0.001). Graduated = no_filter exactly.\\\"}}, \\\"exp_009_dose_30pct_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seeds\\\": 5, \\\"strategies\\\": 3, \\\"total_runs\\\": 15, \\\"mean_std\\\": {\\\"no_filter\\\": {\\\"mmlu\\\": \\\"0.6069±0.0007\\\", \\\"hellaswag\\\": \\\"0.6664±0.0020\\\"}, \\\"binary_ours\\\": {\\\"mmlu\\\": \\\"0.6082±0.0012\\\", \\\"hellaswag\\\": \\\"0.6725±0.0007\\\"}, \\\"graduated\\\": {\\\"mmlu\\\": \\\"0.6072±0.0008\\\", \\\"hellaswag\\\": \\\"0.6665±0.0014\\\"}}, \\\"paired_ttest\\\": {\\\"binary_vs_nofilter\\\": {\\\"delta_mmlu\\\": 0.0013, \\\"p_mmlu\\\": 0.0739, \\\"delta_hellaswag\\\": 0.0061, \\\"p_hellaswag\\\": 0.0036}, \\\"graduated_vs_binary\\\": {\\\"delta_mmlu\\\": -0.001, \\\"p_mmlu\\\": 0.3018, \\\"delta_hellaswag\\\": -0.006, \\\"p_hellaswag\\\": 0.0009}, \\\"graduated_vs_nofilter\\\": {\\\"delta_mmlu\\\": 0.0003, \\\"p_mmlu\\\": 0.6638, \\\"delta_hellaswag\\\": 0.0002, \\\"p_hellaswag\\\": 0.6646}}, \\\"key_finding\\\": \\\"Binary best on HellaSwag (p=0.004). Graduated = no_filter.\\\"}}, \\\"exp_009_dose_10pct_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seeds\\\": 5, \\\"strategies\\\": 3, \\\"total_runs\\\": 15, \\\"mean_std\\\": {\\\"no_filter\\\": {\\\"mmlu\\\": \\\"0.6058±0.0002\\\", \\\"hellaswag\\\": \\\"0.6689±0.0007\\\"}, \\\"binary_ours\\\": {\\\"mmlu\\\": \\\"0.6079±0.0005\\\", \\\"hellaswag\\\": \\\"0.6727±0.0008\\\"}, \\\"graduated\\\": {\\\"mmlu\\\": \\\"0.6066±0.0011\\\", \\\"hellaswag\\\": \\\"0.6700±0.0015\\\"}}, \\\"paired_ttest\\\": {\\\"binary_vs_nofilter\\\": {\\\"delta_mmlu\\\": 0.0021, \\\"p_mmlu\\\": 0.001, \\\"delta_hellaswag\\\": 0.0038, \\\"p_hellaswag\\\": 0.0017}, \\\"graduated_vs_binary\\\": {\\\"delta_mmlu\\\": -0.0014, \\\"p_mmlu\\\": 0.0917, \\\"delta_hellaswag\\\": -0.0027, \\\"p_hellaswag\\\": 0.0399}, \\\"graduated_vs_nofilter\\\": {\\\"delta_mmlu\\\": 0.0008, \\\"p_mmlu\\\": 0.2706, \\\"delta_hellaswag\\\": 0.0011, \\\"p_hellaswag\\\": 0.0611}}, \\\"key_finding\\\": \\\"Binary best. Graduated ≈ no_filter.\\\"}}, \\\"exp_027_retrain_bootstrap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"bootstrap_iterations\\\": 10000, \\\"pairs\\\": {\\\"0v1\\\": {\\\"auc_point\\\": 0.9847, \\\"ci_lower\\\": 0.9828, \\\"ci_upper\\\": 0.9864, \\\"perm_p\\\": 0.0001, \\\"ci_lower_gt_theta\\\": true}, \\\"1v2\\\": {\\\"auc_point\\\": 0.9482, \\\"ci_lower\\\": 0.9443, \\\"ci_upper\\\": 0.952, \\\"perm_p\\\": 0.0001, \\\"ci_lower_gt_theta\\\": true}, \\\"2v3\\\": {\\\"auc_point\\\": 0.8885, \\\"ci_lower\\\": 0.8829, \\\"ci_upper\\\": 0.894, \\\"perm_p\\\": 0.0001, \\\"ci_lower_gt_theta\\\": true}, \\\"3v4\\\": {\\\"auc_point\\\": 0.7977, \\\"ci_lower\\\": 0.7903, \\\"ci_upper\\\": 0.8051, \\\"perm_p\\\": 0.0001, \\\"ci_lower_gt_theta\\\": true}}, \\\"key_finding\\\": \\\"All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001.\\\"}}, \\\"exp_026_feature_stability_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"data_source\\\": \\\"exp_001_pythia prompt-chain (K*=2)\\\", \\\"results\\\": {\\\"15D\\\": {\\\"num_tested\\\": 1, \\\"num_pass\\\": 1, \\\"min_1v2_auc\\\": 0.6262, \\\"mean_1v2_auc\\\": 0.6262}, \\\"10D\\\": {\\\"num_tested\\\": 5, \\\"num_pass\\\": 5, \\\"min_1v2_auc\\\": 0.6153, \\\"mean_1v2_auc\\\": 0.6191}, \\\"8D\\\": {\\\"num_tested\\\": 5, \\\"num_pass\\\": 5, \\\"min_1v2_auc\\\": 0.6056, \\\"mean_1v2_auc\\\": 0.6159}, \\\"5D\\\": {\\\"num_tested\\\": 5, \\\"num_pass\\\": 2, \\\"min_1v2_auc\\\": 0.5856, \\\"mean_1v2_auc\\\": 0.5998}, \\\"3D_top3\\\": {\\\"num_tested\\\": 1, \\\"num_pass\\\": 0, \\\"min_1v2_auc\\\": 0.5871, \\\"mean_1v2_auc\\\": 0.5871}}, \\\"key_finding\\\": \\\"8+ features sufficient for robust K*=2 (all pass θ=0.60). 5D fragile (2/5 pass). Top-3 alone fails. Feature diversity matters at the K* boundary.\\\"}}, \\\"exp_026_feature_stability\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"data_source\\\": \\\"exp_016_qwen_base (prompt-chain, K*=2)\\\", \\\"results\\\": {\\\"15D\\\": {\\\"num_tested\\\": 1, \\\"num_kstar_2\\\": 1, \\\"min_1v2_auc\\\": 0.6262, \\\"mean_1v2_auc\\\": 0.6262}, \\\"10D\\\": {\\\"num_tested\\\": 5, \\\"num_kstar_2\\\": 5, \\\"min_1v2_auc\\\": 0.6153, \\\"mean_1v2_auc\\\": 0.6191}, \\\"8D\\\": {\\\"num_tested\\\": 5, \\\"num_kstar_2\\\": 5, \\\"min_1v2_auc\\\": 0.6056, \\\"mean_1v2_auc\\\": 0.6159}, \\\"5D\\\": {\\\"num_tested\\\": 5, \\\"num_kstar_2\\\": 2, \\\"min_1v2_auc\\\": 0.5856, \\\"mean_1v2_auc\\\": 0.5998}, \\\"3D_top3\\\": {\\\"num_tested\\\": 1, \\\"num_kstar_2\\\": 0, \\\"min_1v2_auc\\\": 0.5871, \\\"mean_1v2_auc\\\": 0.5871}}, \\\"all_above_theta\\\": false, \\\"key_finding\\\": \\\"Feature selection MATTERS at K*=2 boundary. 15D/10D/8D all robust (min 1v2 AUC > 0.60). 5D random subsets: only 2/5 pass θ=0.60 (min=0.5856). Top-3 features alone (0.5871) fail θ. Contrast with retrain-chain (K*=4) where all subsets trivially passed (min=0.8314).\\\", \\\"previous_run_note\\\": \\\"v1 used retrain-chain data (K*=4), where all subsets trivially passed with min 1v2 AUC=0.8314. v2 uses prompt-chain data (K*=2) to test boundary robustness.\\\"}}, \\\"exp_027\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"kstar_ci\\\": 4, \\\"0v1_auc\\\": 0.9847, \\\"0v1_ci\\\": [0.9828, 0.9864], \\\"0v1_perm_p\\\": 0.0001, \\\"1v2_auc\\\": 0.9482, \\\"1v2_ci\\\": [0.9443, 0.952], \\\"1v2_perm_p\\\": 0.0001, \\\"2v3_auc\\\": 0.8885, \\\"2v3_ci\\\": [0.8829, 0.894], \\\"2v3_perm_p\\\": 0.0001, \\\"3v4_auc\\\": 0.7977, \\\"3v4_ci\\\": [0.7903, 0.8051], \\\"3v4_perm_p\\\": 0.0001, \\\"all_ci_lower_above_theta\\\": true}}, \\\"exp_005_degradation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"cross_model_kendall_tau_by_first_auc\\\": {\\\"Pythia_vs_OLMo\\\": 0.733, \\\"Pythia_vs_Qwen_rewrite\\\": 0.467, \\\"Pythia_vs_Qwen_cont\\\": 0.695, \\\"OLMo_vs_Qwen_rewrite\\\": 0.429, \\\"OLMo_vs_Qwen_cont\\\": 0.543, \\\"Qwen_rewrite_vs_Qwen_cont\\\": 0.733}, \\\"cross_model_kendall_tau_by_avg_auc\\\": {\\\"Pythia_vs_OLMo\\\": 0.8476, \\\"Pythia_vs_Qwen_cont\\\": 0.7524, \\\"OLMo_vs_Qwen_cont\\\": 0.6762}, \\\"cross_model_spearman_rho_single_feature_auc\\\": {\\\"Pythia_vs_OLMo\\\": 0.95, \\\"Pythia_vs_Qwen_cont\\\": 0.9143, \\\"OLMo_vs_Qwen_cont\\\": 0.85, \\\"metric_definition\\\": \\\"Spearman ρ on per-feature AUC rankings (each feature independently classifies depth pairs)\\\"}, \\\"4model_tau_mean_continuation_by_first_auc\\\": 0.657, \\\"4model_tau_mean_all_by_first_auc\\\": 0.6, \\\"generation_mode_delta\\\": {\\\"Pythia_vs_Qwen\\\": \\\"+0.228\\\", \\\"OLMo_vs_Qwen\\\": \\\"+0.114\\\"}, \\\"top3_features_ranking_by_first_auc\\\": {\\\"Pythia\\\": [\\\"surp_d1_std\\\", \\\"surp_d2_std\\\", \\\"surp_std\\\"], \\\"OLMo\\\": [\\\"surp_std\\\", \\\"surp_d1_std\\\", \\\"surp_d2_std\\\"], \\\"Qwen_rewrite\\\": [\\\"freq_entropy\\\", \\\"surp_std\\\", \\\"surp_d1_std\\\"], \\\"Qwen_cont\\\": [\\\"surp_d1_std\\\", \\\"surp_std\\\", \\\"surp_d2_std\\\"]}, \\\"shared_top_discriminators\\\": \\\"surp_d1_std, surp_std, surp_d2_std shared across all architectures (single-feature AUC ranking)\\\", \\\"degradation_ordering_consistency\\\": \\\"Strong cross-model consistency (ρ≥0.85) on single-feature AUC ranking under controlled generation mode.\\\", \\\"residual_architecture_effect\\\": \\\"Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\\\", \\\"limitation_1v2_weakness\\\": \\\"depth-pair level consistency weakest at 1v2 (τ~0.37), near-generational feature importance ordering varies more across models\\\"}}, \\\"exp_024_arxiv_domain\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 3, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9946, \\\"1v2\\\": 0.858, \\\"2v3\\\": 0.6427, \\\"3v4\\\": 0.5437, \\\"4v5\\\": 0.5294}, \\\"bootstrap_ci\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9946, \\\"ci_lower\\\": 0.9929, \\\"ci_upper\\\": 0.9961, \\\"perm_p\\\": 0.0001}, \\\"1v2\\\": {\\\"auc\\\": 0.858, \\\"ci_lower\\\": 0.848, \\\"ci_upper\\\": 0.8679, \\\"perm_p\\\": 0.0001}, \\\"2v3\\\": {\\\"auc\\\": 0.6427, \\\"ci_lower\\\": 0.6275, \\\"ci_upper\\\": 0.6575, \\\"perm_p\\\": 0.0001}, \\\"3v4\\\": {\\\"auc\\\": 0.5437, \\\"ci_lower\\\": 0.5276, \\\"ci_upper\\\": 0.5598, \\\"perm_p\\\": 0.0001}, \\\"4v5\\\": {\\\"auc\\\": 0.5294, \\\"ci_lower\\\": 0.5133, \\\"ci_upper\\\": 0.5455, \\\"perm_p\\\": 0.0006}}, \\\"bootstrap_resamples\\\": 10000, \\\"permutation_resamples\\\": 10000, \\\"key_finding\\\": \\\"arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\\\"}}, \\\"exp_017_qwen_continuation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9972, \\\"1v2\\\": 0.6114, \\\"2v3\\\": 0.5609, \\\"3v4\\\": 0.5408, \\\"4v5\\\": 0.5139}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.28627, \\\"1v2\\\": 0.005107, \\\"2v3\\\": 0.003603, \\\"3v4\\\": 0.003395, \\\"4v5\\\": 0.003085}, \\\"ordinal_mae\\\": 1.1547, \\\"ordinal_accuracy\\\": 0.3819, \\\"top3_features\\\": [\\\"freq_entropy\\\", \\\"surp_mean\\\", \\\"surp_std\\\"]}}, \\\"exp_012_binary_confidence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_samples\\\": 500, \\\"generators\\\": [\\\"qwen-rewrite\\\", \\\"pythia-1.4b\\\", \\\"olmo-1b\\\", \\\"qwen-cont\\\"], \\\"6class_accuracy\\\": {\\\"qwen-rewrite\\\": 0.1987, \\\"pythia-1.4b\\\": 0.1303, \\\"olmo-1b\\\": 0.127, \\\"qwen-cont\\\": 0.1833, \\\"random_baseline\\\": 0.1667}, \\\"spearman_rho\\\": {\\\"qwen-rewrite\\\": {\\\"log_ppl_ref\\\": -0.1233, \\\"log_ppl_obs\\\": 0.0815, \\\"ppl_ratio\\\": 0.1185}, \\\"pythia-1.4b\\\": {\\\"log_ppl_ref\\\": -0.2972, \\\"log_ppl_obs\\\": -0.4529, \\\"ppl_ratio\\\": -0.392}, \\\"olmo-1b\\\": {\\\"log_ppl_ref\\\": -0.378, \\\"log_ppl_obs\\\": -0.4614, \\\"ppl_ratio\\\": -0.4068}, \\\"qwen-cont\\\": {\\\"log_ppl_ref\\\": -0.3887, \\\"log_ppl_obs\\\": -0.162, \\\"ppl_ratio\\\": -0.058}}, \\\"binary_detector_kstar\\\": 1, \\\"obd_kstar\\\": 2, \\\"auc_non_monotonic\\\": true, \\\"key_finding\\\": \\\"Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but practically weak). AUC non-monotonic — binary detectors cannot maintain depth ordering. Confirms binary confidence ≠ depth estimation.\\\"}}, \\\"exp_C_permutation_10k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"resamples\\\": 10000, \\\"all_boundary_pairs_p\\\": \\\"<0.0001\\\", \\\"key_finding\\\": \\\"10K permutation confirms all boundary p-values well below 0.01. FR-11 resolved.\\\"}}, \\\"exp_002_olmo_depth\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.997, \\\"1v2\\\": 0.6146, \\\"2v3\\\": 0.5497, \\\"3v4\\\": 0.509, \\\"4v5\\\": 0.5044}, \\\"pairwise_auc_std\\\": {\\\"0v1\\\": 0.0004, \\\"1v2\\\": 0.0029, \\\"2v3\\\": 0.004, \\\"3v4\\\": 0.0084, \\\"4v5\\\": 0.0136}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.23941, \\\"1v2\\\": 0.012972, \\\"2v3\\\": 0.00735, \\\"3v4\\\": 0.003968, \\\"4v5\\\": 0.003851}, \\\"ordinal_mae\\\": 1.1813, \\\"ordinal_accuracy\\\": 0.3685, \\\"top_features\\\": [\\\"surp_d1_mean\\\", \\\"surp_d1_skew\\\", \\\"freq_kurtosis\\\", \\\"surp_d2_mean\\\", \\\"surp_mean\\\"]}}, \\\"exp_009_dose_50pct_v2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_009_dose_30pct_v2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_009_dose_10pct_v2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_009_dose_50pct\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_009_dose_30pct\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_009_dose_10pct\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_kstar_theta\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"output_files\\\": [\\\"kstar_theta_curve.pdf (32KB)\\\", \\\"kstar_theta_curve.png (335KB)\\\"], \\\"models\\\": [\\\"Qwen-rewrite\\\", \\\"Pythia\\\", \\\"OLMo\\\", \\\"Qwen-cont\\\"], \\\"depth_pairs\\\": 5, \\\"key_finding\\\": \\\"All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5. θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical resolved.\\\"}}, \\\"exp_022_cross_scorer_matrix\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_combos\\\": 12, \\\"completed\\\": 12, \\\"K_star_distribution\\\": {\\\"K2\\\": 11, \\\"K1\\\": 1}, \\\"matrix\\\": {\\\"pythia_greedy×olmo\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.8811}, \\\"pythia_greedy×pythia\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.8838}, \\\"pythia_greedy×qwen_base\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.8814}, \\\"pythia_greedy×qwen_instruct\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.8818}, \\\"qwen_base×olmo\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.6047}, \\\"qwen_base×pythia\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.617}, \\\"qwen_base×qwen_base\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.6262}, \\\"qwen_base×qwen_instruct\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.6273}, \\\"qwen_cont256×olmo\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.6028}, \\\"qwen_cont256×pythia\\\": {\\\"K_star\\\": 1, \\\"1v2\\\": 0.5979}, \\\"qwen_cont256×qwen_base\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.6282}, \\\"qwen_cont256×qwen_instruct\\\": {\\\"K_star\\\": 2, \\\"1v2\\\": 0.6072}}, \\\"key_finding\\\": \\\"Scorer independence confirmed: K*=2 in 11/12 combos. Only exception: qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.\\\"}}, \\\"exp_008_retrain_chain_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": \\\">=4\\\", \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9847, \\\"1v2\\\": 0.9484, \\\"2v3\\\": 0.8888, \\\"3v4\\\": 0.7982}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.17, \\\"1v2\\\": 0.12, \\\"2v3\\\": 0.064, \\\"3v4\\\": 0.04}, \\\"key_finding\\\": \\\"Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic boundary.\\\"}}, \\\"exp-008-retrain-chain\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp_025_pythia_arxiv\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 3, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9877, \\\"1v2\\\": 0.8047, \\\"2v3\\\": 0.6545, \\\"3v4\\\": 0.5507, \\\"4v5\\\": 0.5287}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.171338, \\\"1v2\\\": 0.057344, \\\"2v3\\\": 0.019524, \\\"3v4\\\": 0.009917, \\\"4v5\\\": 0.008846}, \\\"bootstrap_ci\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9876, \\\"ci_lower\\\": 0.9851, \\\"ci_upper\\\": 0.99, \\\"perm_p\\\": 0.0001}, \\\"1v2\\\": {\\\"auc\\\": 0.8047, \\\"ci_lower\\\": 0.7934, \\\"ci_upper\\\": 0.8162, \\\"perm_p\\\": 0.0001}, \\\"2v3\\\": {\\\"auc\\\": 0.6544, \\\"ci_lower\\\": 0.6401, \\\"ci_upper\\\": 0.6688, \\\"perm_p\\\": 0.0001}, \\\"3v4\\\": {\\\"auc\\\": 0.55, \\\"ci_lower\\\": 0.534, \\\"ci_upper\\\": 0.5657, \\\"perm_p\\\": 0.0001}, \\\"4v5\\\": {\\\"auc\\\": 0.5284, \\\"ci_lower\\\": 0.5122, \\\"ci_upper\\\": 0.5443, \\\"perm_p\\\": 0.001}}, \\\"bootstrap_resamples\\\": 10000, \\\"permutation_resamples\\\": 10000, \\\"n_samples\\\": 2200, \\\"top_features\\\": [\\\"freq_entropy\\\", \\\"surp_std\\\", \\\"surp_mean\\\", \\\"surp_d1_skew\\\", \\\"surp_d1_mean\\\"], \\\"ordinal\\\": {\\\"MAE\\\": 0.8518, \\\"Accuracy\\\": 0.4545}, \\\"key_finding\\\": \\\"Pythia-1.4B on arXiv yields K*=3, identical to exp-024 (Qwen on arXiv). 2v3 CI lower=0.6401 > θ=0.60. Domain saturation depth is model-invariant for arXiv.\\\"}}, \\\"exp_020_pythia_decoding\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"greedy\\\": {\\\"K_star\\\": 2, \\\"auc\\\": {\\\"0v1\\\": 0.9992, \\\"1v2\\\": 0.8838, \\\"2v3\\\": 0.5342, \\\"3v4\\\": 0.5228, \\\"4v5\\\": 0.5162}}, \\\"nuc09\\\": {\\\"K_star\\\": 2, \\\"auc\\\": {\\\"0v1\\\": 0.9948, \\\"1v2\\\": 0.677, \\\"2v3\\\": 0.5549, \\\"3v4\\\": 0.5299, \\\"4v5\\\": 0.5013}}, \\\"t07\\\": {\\\"K_star\\\": 2, \\\"auc\\\": {\\\"0v1\\\": 0.9965, \\\"1v2\\\": 0.7265, \\\"2v3\\\": 0.5941, \\\"3v4\\\": 0.5698, \\\"4v5\\\": 0.5284}}, \\\"t12\\\": {\\\"K_star\\\": 2, \\\"auc\\\": {\\\"0v1\\\": 0.9933, \\\"1v2\\\": 0.6172, \\\"2v3\\\": 0.5226, \\\"3v4\\\": 0.517, \\\"4v5\\\": 0.5051}}}}, \\\"exp_021_length_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"128tok\\\": {\\\"K_star\\\": 2, \\\"1v2_auc\\\": 0.6219}, \\\"256tok\\\": {\\\"K_star\\\": 2, \\\"1v2_auc\\\": 0.6282}, \\\"512tok\\\": {\\\"K_star\\\": 2, \\\"1v2_auc\\\": 0.6073}, \\\"all_K_star_2\\\": true, \\\"bootstrap_ci\\\": {\\\"512tok_1v2\\\": {\\\"auc\\\": 0.6073, \\\"ci_lower\\\": 0.5979, \\\"ci_upper\\\": 0.6166, \\\"perm_p\\\": 0.0001, \\\"verdict\\\": \\\"BORDERLINE\\\"}}}}, \\\"exp_018_llama8b_depth\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9225, \\\"1v2\\\": 0.6123, \\\"2v3\\\": 0.5274, \\\"3v4\\\": 0.5138, \\\"4v5\\\": 0.5097}, \\\"jsd\\\": {\\\"0v1\\\": 0.077, \\\"1v2\\\": 0.012, \\\"2v3\\\": 0.005}, \\\"bootstrap_ci\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9224, \\\"ci_lower\\\": 0.9174, \\\"ci_upper\\\": 0.9272, \\\"perm_p\\\": 0.0001}, \\\"1v2\\\": {\\\"auc\\\": 0.6123, \\\"ci_lower\\\": 0.6028, \\\"ci_upper\\\": 0.6216, \\\"perm_p\\\": 0.0001}, \\\"2v3\\\": {\\\"auc\\\": 0.5273, \\\"ci_lower\\\": 0.5169, \\\"ci_upper\\\": 0.5378, \\\"perm_p\\\": 0.0001}, \\\"3v4\\\": {\\\"auc\\\": 0.5168, \\\"ci_lower\\\": 0.5062, \\\"ci_upper\\\": 0.5275, \\\"perm_p\\\": 0.0037}, \\\"4v5\\\": {\\\"auc\\\": 0.5159, \\\"ci_lower\\\": 0.5052, \\\"ci_upper\\\": 0.5268, \\\"perm_p\\\": 0.0035}}, \\\"bootstrap_resamples\\\": 10000, \\\"permutation_resamples\\\": 10000}}, \\\"exp_023_domain_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 2, \\\"1v2_auc\\\": 0.6193, \\\"2v3_auc\\\": 0.5498, \\\"all_folds_above_060\\\": true, \\\"top_feature\\\": \\\"freq_entropy\\\", \\\"ordinal_accuracy\\\": 0.377}}, \\\"exp_019b_mistral_cross_scorer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 1, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9209, \\\"1v2\\\": 0.5695, \\\"2v3\\\": 0.5335, \\\"3v4\\\": 0.514, \\\"4v5\\\": 0.5184}, \\\"bootstrap_ci\\\": {\\\"0v1\\\": {\\\"mean\\\": 0.9209, \\\"ci_lower\\\": 0.9189, \\\"ci_upper\\\": 0.9229, \\\"pass_060\\\": true}, \\\"1v2\\\": {\\\"mean\\\": 0.5696, \\\"ci_lower\\\": 0.5645, \\\"ci_upper\\\": 0.5746, \\\"pass_060\\\": false}, \\\"2v3\\\": {\\\"mean\\\": 0.5335, \\\"ci_lower\\\": 0.5283, \\\"ci_upper\\\": 0.5382, \\\"pass_060\\\": false}, \\\"3v4\\\": {\\\"mean\\\": 0.514, \\\"ci_lower\\\": 0.5063, \\\"ci_upper\\\": 0.5213, \\\"pass_060\\\": false}, \\\"4v5\\\": {\\\"mean\\\": 0.5183, \\\"ci_lower\\\": 0.5128, \\\"ci_upper\\\": 0.5244, \\\"pass_060\\\": false}}, \\\"jsd\\\": {\\\"0v1\\\": 0.08355, \\\"1v2\\\": 0.007642, \\\"2v3\\\": 0.004752, \\\"3v4\\\": 0.004255, \\\"4v5\\\": 0.003758}, \\\"ordinal_mae\\\": 1.3737, \\\"ordinal_accuracy\\\": 0.3179, \\\"top3_features\\\": [\\\"freq_entropy\\\", \\\"surp_d1_skew\\\", \\\"surp_d1_mean\\\"], \\\"key_finding\\\": \\\"Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2 AUC=0.5695 (self-scorer was 0.5935) — cross-scorer LOWER, not higher. Mistral K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact.\\\"}}, \\\"exp_019_mistral7b_depth\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 1, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9843, \\\"1v2\\\": 0.5935, \\\"2v3\\\": 0.5402, \\\"3v4\\\": 0.5232, \\\"4v5\\\": 0.5181}, \\\"bootstrap_ci_1v2\\\": {\\\"ci_lower\\\": 0.5835, \\\"ci_upper\\\": 0.6032, \\\"p_auc_leq_060\\\": 0.9017}, \\\"jsd\\\": {\\\"0v1\\\": 0.124194, \\\"1v2\\\": 0.008051, \\\"2v3\\\": 0.005047, \\\"3v4\\\": 0.004516, \\\"4v5\\\": 0.004109}, \\\"ordinal_mae\\\": 1.2275, \\\"ordinal_accuracy\\\": 0.3567, \\\"top3_features\\\": [\\\"freq_entropy\\\", \\\"surp_d1_skew\\\", \\\"surp_d1_mean\\\"]}}, \\\"exp_016_base_vs_instruct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.987, \\\"1v2\\\": 0.6262, \\\"2v3\\\": 0.5496, \\\"3v4\\\": 0.5294, \\\"4v5\\\": 0.5182}, \\\"pairwise_auc_std\\\": {\\\"0v1\\\": 0.0015, \\\"1v2\\\": 0.0152, \\\"2v3\\\": 0.0067, \\\"3v4\\\": 0.0132, \\\"4v5\\\": 0.0139}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.163726, \\\"1v2\\\": 0.01081, \\\"2v3\\\": 0.005311, \\\"3v4\\\": 0.003942, \\\"4v5\\\": 0.003522}, \\\"ordinal_mae\\\": 1.1691, \\\"ordinal_accuracy\\\": 0.3719, \\\"top_features\\\": [\\\"freq_entropy\\\", \\\"surp_std\\\", \\\"surp_d1_skew\\\", \\\"surp_d1_mean\\\", \\\"surp_mean\\\"], \\\"n_samples\\\": 30000, \\\"bootstrap_ci\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.987, \\\"ci_lower\\\": 0.9853, \\\"ci_upper\\\": 0.9885, \\\"perm_p\\\": 0.0001}, \\\"1v2\\\": {\\\"auc\\\": 0.626, \\\"ci_lower\\\": 0.6168, \\\"ci_upper\\\": 0.6353, \\\"perm_p\\\": 0.0001}, \\\"2v3\\\": {\\\"auc\\\": 0.5496, \\\"ci_lower\\\": 0.5397, \\\"ci_upper\\\": 0.56, \\\"perm_p\\\": 0.0001}, \\\"3v4\\\": {\\\"auc\\\": 0.5293, \\\"ci_lower\\\": 0.5188, \\\"ci_upper\\\": 0.5399, \\\"perm_p\\\": 0.0001}, \\\"4v5\\\": {\\\"auc\\\": 0.5181, \\\"ci_lower\\\": 0.5075, \\\"ci_upper\\\": 0.5288, \\\"perm_p\\\": 0.0016}}, \\\"bootstrap_resamples\\\": 10000, \\\"permutation_resamples\\\": 10000, \\\"key_finding\\\": \\\"K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95% CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015, 0.6213] — no significant base-vs-instruct difference.\\\"}}, \\\"exp_003_decoding_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"K_star\\\": 2, \\\"K_star_robust\\\": true, \\\"bootstrap_ci\\\": {\\\"config1_greedy\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9796, \\\"ci\\\": [0.9772, 0.982], \\\"perm_p\\\": 0}, \\\"1v2\\\": {\\\"auc\\\": 0.6892, \\\"ci\\\": [0.6802, 0.6982], \\\"perm_p\\\": 0}, \\\"2v3\\\": {\\\"auc\\\": 0.5612, \\\"ci\\\": [0.5517, 0.5705], \\\"perm_p\\\": 0}, \\\"3v4\\\": {\\\"auc\\\": 0.5405, \\\"ci\\\": [0.5308, 0.5502], \\\"perm_p\\\": 0}, \\\"4v5\\\": {\\\"auc\\\": 0.5137, \\\"ci\\\": [0.5033, 0.5238], \\\"perm_p\\\": 0.0082}}, \\\"config2_nuc09\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9945, \\\"ci\\\": [0.9934, 0.9956], \\\"perm_p\\\": 0}, \\\"1v2\\\": {\\\"auc\\\": 0.6862, \\\"ci\\\": [0.6774, 0.6951], \\\"perm_p\\\": 0}, \\\"2v3\\\": {\\\"auc\\\": 0.5917, \\\"ci\\\": [0.5824, 0.601], \\\"perm_p\\\": 0, \\\"note\\\": \\\"CI upper crosses theta=0.60\\\"}, \\\"3v4\\\": {\\\"auc\\\": 0.5468, \\\"ci\\\": [0.5369, 0.5568], \\\"perm_p\\\": 0}, \\\"4v5\\\": {\\\"auc\\\": 0.5066, \\\"ci\\\": [0.4959, 0.5173], \\\"perm_p\\\": 0.1199}}, \\\"config3_t07\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9877, \\\"ci\\\": [0.9857, 0.9896], \\\"perm_p\\\": 0}, \\\"1v2\\\": {\\\"auc\\\": 0.6885, \\\"ci\\\": [0.6797, 0.697], \\\"perm_p\\\": 0}, \\\"2v3\\\": {\\\"auc\\\": 0.5901, \\\"ci\\\": [0.5806, 0.5996], \\\"perm_p\\\": 0}, \\\"3v4\\\": {\\\"auc\\\": 0.539, \\\"ci\\\": [0.5288, 0.5493], \\\"perm_p\\\": 0}, \\\"4v5\\\": {\\\"auc\\\": 0.5348, \\\"ci\\\": [0.5243, 0.5454], \\\"perm_p\\\": 0}}, \\\"config4_t12\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9982, \\\"ci\\\": [0.9975, 0.9987], \\\"perm_p\\\": 0}, \\\"1v2\\\": {\\\"auc\\\": 0.7037, \\\"ci\\\": [0.6945, 0.7126], \\\"perm_p\\\": 0}, \\\"2v3\\\": {\\\"auc\\\": 0.582, \\\"ci\\\": [0.5722, 0.5917], \\\"perm_p\\\": 0}, \\\"3v4\\\": {\\\"auc\\\": 0.5293, \\\"ci\\\": [0.5185, 0.5399], \\\"perm_p\\\": 0}, \\\"4v5\\\": {\\\"auc\\\": 0.5237, \\\"ci\\\": [0.5132, 0.5347], \\\"perm_p\\\": 0.0001}}, \\\"resamples\\\": 10000, \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\"}}}, \\\"exp_004_7b_crossscale\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9644, \\\"1v2\\\": 0.6178, \\\"2v3\\\": 0.546, \\\"3v4\\\": 0.5225, \\\"4v5\\\": 0.5091}, \\\"pairwise_auc_std\\\": {\\\"0v1\\\": 0.0034, \\\"1v2\\\": 0.0081, \\\"2v3\\\": 0.0028, \\\"3v4\\\": 0.0113, \\\"4v5\\\": 0.0052}, \\\"bootstrap_ci\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9638, \\\"ci_lower\\\": 0.9607, \\\"ci_upper\\\": 0.9665, \\\"perm_p\\\": 0.0001}, \\\"1v2\\\": {\\\"auc\\\": 0.6168, \\\"ci_lower\\\": 0.6079, \\\"ci_upper\\\": 0.6261, \\\"perm_p\\\": 0.0001}, \\\"2v3\\\": {\\\"auc\\\": 0.5492, \\\"ci_lower\\\": 0.5388, \\\"ci_upper\\\": 0.5594, \\\"perm_p\\\": 0.0001}, \\\"3v4\\\": {\\\"auc\\\": 0.5276, \\\"ci_lower\\\": 0.517, \\\"ci_upper\\\": 0.5375, \\\"perm_p\\\": 0.0001}, \\\"4v5\\\": {\\\"auc\\\": 0.5085, \\\"ci_lower\\\": 0.4988, \\\"ci_upper\\\": 0.5191, \\\"perm_p\\\": 0.0676}}, \\\"bootstrap_resamples\\\": 1000, \\\"permutation_resamples\\\": 10000, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.127422, \\\"1v2\\\": 0.010114, \\\"2v3\\\": 0.004798, \\\"3v4\\\": 0.004821, \\\"4v5\\\": 0.003335}, \\\"ordinal_mae\\\": 1.2156, \\\"ordinal_accuracy\\\": 0.3523, \\\"top_features\\\": [\\\"freq_entropy\\\", \\\"surp_d1_skew\\\", \\\"surp_std\\\", \\\"surp_d1_mean\\\", \\\"surp_mean\\\"], \\\"key_finding\\\": \\\"K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60 (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676). FR-4 Warning resolved.\\\"}}, \\\"exp_E_paired_stats\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"mmlu_significant_pairs\\\": \\\"8/15\\\", \\\"hellaswag_significant_pairs\\\": \\\"9/15\\\", \\\"binary_ours_vs_all_mmlu\\\": \\\"all significant\\\", \\\"max_cohen_d_mmlu\\\": 10.8, \\\"max_cohen_d_hellaswag\\\": 8.98, \\\"graduated_a09_vs_dsir_corrected_p\\\": 0.0523, \\\"cohen_d_method\\\": \\\"d_av (Lakens 2013)\\\", \\\"key_finding\\\": \\\"binary-ours significantly outperforms all alternatives on MMLU. On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni cummax bug fixed: MMLU 10/15→8/15. Cohen's d changed to d_av.\\\", \\\"bugfix_note\\\": \\\"Holm-Bonferroni cummax variable was never updated, causing 2 MMLU pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\\\"}}, \\\"exp_D_obd_n500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"obd_accuracy_final\\\": 0.38, \\\"obd_ci\\\": [0.34, 0.422], \\\"mcnemar_vs_gpt55_p\\\": 0.0809, \\\"mcnemar_vs_claude_p\\\": 0.0693, \\\"mcnemar_significant\\\": false, \\\"multi_seed_std\\\": 0, \\\"per_depth\\\": {\\\"d0\\\": 0.96, \\\"d1\\\": 0.39, \\\"d2\\\": 0.14, \\\"d3\\\": 0.19, \\\"d4\\\": 0.22}, \\\"prob_merge_accuracy\\\": 0.444, \\\"prob_merge_d4_bias\\\": 0.8, \\\"note\\\": \\\"v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant — supports discussion.tex narrative\\\"}}, \\\"exp_B_14d_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"result\\\": \\\"K*=2 stable across all 4 models after removing self_BLEU (14D)\\\", \\\"key_finding\\\": \\\"self_BLEU removal does not change K* boundary. FR-3 resolved.\\\"}}, \\\"exp_A_alt_scorer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"pythia_qwen_rw\\\": {\\\"k_star\\\": 2, \\\"auc_0v1\\\": 0.9923, \\\"auc_1v2\\\": 0.7012, \\\"auc_2v3\\\": 0.587, \\\"mae\\\": 1.006, \\\"accuracy\\\": 0.417, \\\"spearman_rho_vs_baseline\\\": 0.906}, \\\"pythia_qwen_cont\\\": {\\\"k_star\\\": 1, \\\"auc_0v1\\\": 0.99, \\\"auc_1v2\\\": 0.5923, \\\"auc_2v3\\\": null, \\\"mae\\\": 1.216, \\\"accuracy\\\": 0.371, \\\"spearman_rho_vs_baseline\\\": 0.942}, \\\"olmo_qwen_rw\\\": {\\\"k_star\\\": 2, \\\"auc_0v1\\\": 0.9918, \\\"auc_1v2\\\": 0.6947, \\\"auc_2v3\\\": null, \\\"mae\\\": 1.016, \\\"accuracy\\\": 0.413, \\\"spearman_rho_vs_baseline\\\": 0.92}, \\\"olmo_qwen_cont\\\": {\\\"k_star\\\": 1, \\\"auc_0v1\\\": 0.989, \\\"auc_1v2\\\": 0.5858, \\\"auc_2v3\\\": null, \\\"mae\\\": 1.229, \\\"accuracy\\\": 0.368, \\\"spearman_rho_vs_baseline\\\": 0.902}, \\\"key_finding\\\": \\\"K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1 (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer independence of feature ranking.\\\"}}, \\\"exp_015_neural_probe\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"pythia\\\": {\\\"k_star_neural\\\": 2, \\\"k_star_lgbm\\\": 2, \\\"accuracy\\\": 0.3892, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.966, \\\"1v2\\\": 0.676, \\\"2v3\\\": 0.596, \\\"3v4\\\": 0.555, \\\"4v5\\\": 0.532}}, \\\"olmo\\\": {\\\"k_star_neural\\\": 2, \\\"k_star_lgbm\\\": 2, \\\"accuracy\\\": 0.3729, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.95, \\\"1v2\\\": 0.657, \\\"2v3\\\": 0.589, \\\"3v4\\\": 0.547, \\\"4v5\\\": 0.53}}, \\\"qwen_cont\\\": {\\\"k_star_neural\\\": 3, \\\"k_star_lgbm\\\": 2, \\\"accuracy\\\": 0.4368, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.988, \\\"1v2\\\": 0.702, \\\"2v3\\\": 0.616, \\\"3v4\\\": 0.59, \\\"4v5\\\": 0.566}}, \\\"key_finding\\\": \\\"Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3 only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\\\"}}, \\\"exp_006_graduated_filtering\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_runs\\\": 51, \\\"binary_ours\\\": {\\\"mmlu\\\": \\\"0.5941±0.0008\\\", \\\"hellaswag\\\": \\\"0.6701±0.0006\\\"}, \\\"binary_drayson\\\": {\\\"mmlu\\\": \\\"0.5913±0.0009\\\", \\\"hellaswag\\\": \\\"0.6691±0.0004\\\"}, \\\"surprisal\\\": {\\\"mmlu\\\": \\\"0.5894±0.0009\\\", \\\"hellaswag\\\": \\\"0.6641±0.0006\\\"}, \\\"graduated_a09\\\": {\\\"mmlu\\\": \\\"0.5892±0.0008\\\", \\\"hellaswag\\\": \\\"0.6701±0.0007\\\"}, \\\"graduated_a07\\\": {\\\"mmlu\\\": \\\"0.5892±0.0014\\\", \\\"hellaswag\\\": \\\"0.6695±0.0004\\\"}, \\\"graduated_a05\\\": {\\\"mmlu\\\": \\\"0.5880±0.0013\\\", \\\"hellaswag\\\": \\\"0.6687±0.0008\\\"}, \\\"graduated_a03\\\": {\\\"mmlu\\\": \\\"0.5877±0.0013\\\", \\\"hellaswag\\\": \\\"0.6669±0.0005\\\"}, \\\"graduated_a01\\\": {\\\"mmlu\\\": \\\"0.5873±0.0019\\\", \\\"hellaswag\\\": \\\"0.6640±0.0009\\\"}, \\\"dsir\\\": {\\\"mmlu\\\": \\\"0.5869±0.0003\\\", \\\"hellaswag\\\": \\\"0.6631±0.0007\\\"}, \\\"no_filter\\\": {\\\"mmlu\\\": \\\"0.5865±0.0010\\\", \\\"hellaswag\\\": \\\"0.6638±0.0008\\\"}, \\\"base_model\\\": {\\\"mmlu\\\": \\\"0.6018\\\", \\\"hellaswag\\\": \\\"0.6821\\\"}, \\\"best_strategy\\\": \\\"binary-ours\\\", \\\"key_finding\\\": \\\"binary-ours is best filtering strategy. All strategies degrade vs base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR below all other strategies except no-filter.\\\"}}, \\\"exp_007_bootstrap_ci\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"qwen_rewrite\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9956, \\\"ci_lower\\\": 0.9946, \\\"ci_upper\\\": 0.9965, \\\"perm_p\\\": 0.002}, \\\"1v2\\\": {\\\"auc\\\": 0.6955, \\\"ci_lower\\\": 0.6859, \\\"ci_upper\\\": 0.7041, \\\"perm_p\\\": 0.002}, \\\"2v3\\\": {\\\"auc\\\": 0.5893, \\\"ci_lower\\\": 0.5795, \\\"ci_upper\\\": 0.5991, \\\"perm_p\\\": 0.002}, \\\"3v4\\\": {\\\"auc\\\": 0.5435, \\\"ci_lower\\\": 0.5333, \\\"ci_upper\\\": 0.5551, \\\"perm_p\\\": 0.002}, \\\"4v5\\\": {\\\"auc\\\": 0.534, \\\"ci_lower\\\": 0.5238, \\\"ci_upper\\\": 0.5448, \\\"perm_p\\\": 0.002}}, \\\"pythia_cont\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9932, \\\"ci_lower\\\": 0.9921, \\\"ci_upper\\\": 0.9943, \\\"perm_p\\\": 0.002}, \\\"1v2\\\": {\\\"auc\\\": 0.6539, \\\"ci_lower\\\": 0.6454, \\\"ci_upper\\\": 0.663, \\\"perm_p\\\": 0.002}, \\\"2v3\\\": {\\\"auc\\\": 0.5514, \\\"ci_lower\\\": 0.5417, \\\"ci_upper\\\": 0.5628, \\\"perm_p\\\": 0.002}, \\\"3v4\\\": {\\\"auc\\\": 0.5152, \\\"ci_lower\\\": 0.5041, \\\"ci_upper\\\": 0.526, \\\"perm_p\\\": 0.006}, \\\"4v5\\\": {\\\"auc\\\": 0.5136, \\\"ci_lower\\\": 0.5021, \\\"ci_upper\\\": 0.5249, \\\"perm_p\\\": 0.008}}, \\\"olmo_cont\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.997, \\\"ci_lower\\\": 0.9964, \\\"ci_upper\\\": 0.9975, \\\"perm_p\\\": 0.002}, \\\"1v2\\\": {\\\"auc\\\": 0.6145, \\\"ci_lower\\\": 0.6045, \\\"ci_upper\\\": 0.6247, \\\"perm_p\\\": 0.002}, \\\"2v3\\\": {\\\"auc\\\": 0.5496, \\\"ci_lower\\\": 0.5399, \\\"ci_upper\\\": 0.5596, \\\"perm_p\\\": 0.002}, \\\"3v4\\\": {\\\"auc\\\": 0.5091, \\\"ci_lower\\\": 0.4973, \\\"ci_upper\\\": 0.52, \\\"perm_p\\\": 0.064}, \\\"4v5\\\": {\\\"auc\\\": 0.5045, \\\"ci_lower\\\": 0.4932, \\\"ci_upper\\\": 0.515, \\\"perm_p\\\": 0.232}}, \\\"qwen_cont\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9971, \\\"ci_lower\\\": 0.9963, \\\"ci_upper\\\": 0.9978, \\\"perm_p\\\": 0.002}, \\\"1v2\\\": {\\\"auc\\\": 0.6112, \\\"ci_lower\\\": 0.6015, \\\"ci_upper\\\": 0.6213, \\\"perm_p\\\": 0.002}, \\\"2v3\\\": {\\\"auc\\\": 0.5609, \\\"ci_lower\\\": 0.5511, \\\"ci_upper\\\": 0.5712, \\\"perm_p\\\": 0.002}, \\\"3v4\\\": {\\\"auc\\\": 0.5409, \\\"ci_lower\\\": 0.5308, \\\"ci_upper\\\": 0.5508, \\\"perm_p\\\": 0.002}, \\\"4v5\\\": {\\\"auc\\\": 0.5141, \\\"ci_lower\\\": 0.5035, \\\"ci_upper\\\": 0.5255, \\\"perm_p\\\": 0.006}}, \\\"k_star_robust\\\": true, \\\"all_1v2_ci_lower_above_060\\\": true, \\\"most_marginal\\\": \\\"Qwen-cont CI lower=0.6015, only 0.0015 above threshold\\\"}}, \\\"exp_011_llm_zeroshot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"gpt55_5class_acc\\\": 0.332, \\\"gpt55_mae\\\": 1.102, \\\"gpt55_spearman\\\": 0.383, \\\"gpt55_binary_acc\\\": 0.878, \\\"claude_5class_acc\\\": 0.331, \\\"claude_mae\\\": 1.15, \\\"claude_spearman\\\": 0.416, \\\"claude_binary_acc\\\": 0.882, \\\"odb_baseline_5class_acc\\\": 0.386, \\\"odb_baseline_mae\\\": 1.107, \\\"gpt55_per_depth_acc\\\": {\\\"depth_0\\\": 0.77, \\\"depth_1\\\": 0.19, \\\"depth_2\\\": 0.38, \\\"depth_3\\\": 0.24, \\\"depth_4\\\": 0.08}, \\\"claude_per_depth_acc\\\": {\\\"depth_0\\\": 0.69, \\\"depth_1\\\": 0.21, \\\"depth_2\\\": 0.28, \\\"depth_3\\\": 0.101, \\\"depth_4\\\": 0.37}, \\\"n_samples_per_model\\\": 500, \\\"key_finding\\\": \\\"Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails.\\\"}}, \\\"exp_013_cross_transfer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_matrix\\\": {\\\"Qwen_rw→Qwen_rw\\\": 0.4229, \\\"Qwen_rw→Pythia\\\": 0.259, \\\"Qwen_rw→OLMo\\\": 0.2653, \\\"Qwen_rw→Qwen_cont\\\": 0.3466, \\\"Pythia→Qwen_rw\\\": 0.2718, \\\"Pythia→Pythia\\\": 0.3856, \\\"Pythia→OLMo\\\": 0.3531, \\\"Pythia→Qwen_cont\\\": 0.3287, \\\"OLMo→Qwen_rw\\\": 0.2768, \\\"OLMo→Pythia\\\": 0.345, \\\"OLMo→OLMo\\\": 0.3822, \\\"OLMo→Qwen_cont\\\": 0.3244, \\\"Qwen_cont→Qwen_rw\\\": 0.344, \\\"Qwen_cont→Pythia\\\": 0.3284, \\\"Qwen_cont→OLMo\\\": 0.3112, \\\"Qwen_cont→Qwen_cont\\\": 0.3875}, \\\"transfer_retention_accuracy\\\": {\\\"Pythia↔OLMo\\\": \\\"91-92%\\\", \\\"Qwen_rw→Pythia/OLMo\\\": \\\"61-63%\\\", \\\"Qwen_cont↔Pythia\\\": \\\"83-85%\\\", \\\"Qwen_cont↔OLMo\\\": \\\"80-85%\\\"}, \\\"transfer_retention_tau\\\": {\\\"Pythia↔OLMo\\\": \\\"85-86%\\\", \\\"Qwen_rw→Pythia/OLMo\\\": \\\"45-50%\\\", \\\"Qwen_cont↔others\\\": \\\"68-83%\\\"}, \\\"mean_pw_auc_matrix\\\": {\\\"within_avg\\\": 0.6099, \\\"cross_avg\\\": 0.5905, \\\"0v1_cross_all_above\\\": 0.96}, \\\"key_finding\\\": \\\"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better.\\\"}}, \\\"exp_010_ordinal_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"qwen_rewrite\\\": {\\\"obd_lgbm\\\": {\\\"accuracy\\\": 0.4229, \\\"mae\\\": 0.9836, \\\"tau_b\\\": 0.5518, \\\"mean_pw_auc\\\": 0.6214}, \\\"multiclass_lgbm\\\": {\\\"accuracy\\\": 0.4182, \\\"mae\\\": 1.0163, \\\"tau_b\\\": 0.5367, \\\"mean_pw_auc\\\": 0.6246}, \\\"ordinal_logreg\\\": {\\\"accuracy\\\": 0.3636, \\\"mae\\\": 0.9105, \\\"tau_b\\\": 0.563, \\\"mean_pw_auc\\\": 0.5022}}, \\\"pythia\\\": {\\\"obd_lgbm\\\": {\\\"accuracy\\\": 0.3856, \\\"mae\\\": 1.1072, \\\"tau_b\\\": 0.4745, \\\"mean_pw_auc\\\": 0.6055}, \\\"multiclass_lgbm\\\": {\\\"accuracy\\\": 0.3832, \\\"mae\\\": 1.1399, \\\"tau_b\\\": 0.4622, \\\"mean_pw_auc\\\": 0.6062}, \\\"ordinal_logreg\\\": {\\\"accuracy\\\": 0.3179, \\\"mae\\\": 1.022, \\\"tau_b\\\": 0.49, \\\"mean_pw_auc\\\": 0.4767}}, \\\"olmo\\\": {\\\"obd_lgbm\\\": {\\\"accuracy\\\": 0.3822, \\\"mae\\\": 1.1469, \\\"tau_b\\\": 0.4683, \\\"mean_pw_auc\\\": 0.6015}, \\\"multiclass_lgbm\\\": {\\\"accuracy\\\": 0.3685, \\\"mae\\\": 1.1813, \\\"tau_b\\\": 0.4497, \\\"mean_pw_auc\\\": 0.5974}, \\\"ordinal_logreg\\\": {\\\"accuracy\\\": 0.3265, \\\"mae\\\": 1.0352, \\\"tau_b\\\": 0.4656, \\\"mean_pw_auc\\\": 0.4859}}}}, \\\"exp_001_pythia_depth\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9932, \\\"1v2\\\": 0.6539, \\\"2v3\\\": 0.5515, \\\"3v4\\\": 0.5153, \\\"4v5\\\": 0.5135}, \\\"pairwise_auc_std\\\": {\\\"0v1\\\": 0.0007, \\\"1v2\\\": 0.0069, \\\"2v3\\\": 0.0137, \\\"3v4\\\": 0.0084, \\\"4v5\\\": 0.0078}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.2142, \\\"1v2\\\": 0.014, \\\"2v3\\\": 0.0051, \\\"3v4\\\": 0.0033, \\\"4v5\\\": 0.0031}, \\\"k_star\\\": 2, \\\"ordinal_mae\\\": 1.14, \\\"ordinal_accuracy\\\": 0.383}}, \\\"mvp_pilot_sat_v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9956, \\\"1v2\\\": 0.6957, \\\"2v3\\\": 0.5893, \\\"3v4\\\": 0.5434, \\\"4v5\\\": 0.5343}, \\\"pairwise_auc_std\\\": {\\\"0v1\\\": 0.0005, \\\"1v2\\\": 0.0072, \\\"2v3\\\": 0.012, \\\"3v4\\\": 0.0053, \\\"4v5\\\": 0.0091}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.2669, \\\"1v2\\\": 0.0163, \\\"2v3\\\": 0.0069, \\\"3v4\\\": 0.0047, \\\"4v5\\\": 0.0041}, \\\"k_star\\\": 2, \\\"ordinal_mae\\\": 1.0163, \\\"ordinal_accuracy\\\": 0.4182}}}, \\\"count\\\": 75, \\\"total\\\": 75, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2975}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_pythia_retrain_depth7\": {\"status\": \"DONE\", \"metrics\": {\"kstar\": 7, \"pairwise_auc\": {\"0v1\": 0.9844, \"1v2\": 0.947, \"2v3\": 0.8891, \"3v4\": 0.7999, \"4v5\": 0.6907, \"5v6\": 0.6497, \"6v7\": 0.634}, \"pairwise_auc_ci\": {\"0v1\": [0.9829, 0.9858], \"1v2\": [0.9418, 0.9522], \"2v3\": [0.8822, 0.896], \"3v4\": [0.7951, 0.8047], \"4v5\": [0.688, 0.6934], \"5v6\": [0.6429, 0.6565], \"6v7\": [0.6275, 0.6406]}, \"pairwise_jsd\": {\"0v1\": 0.1775, \"1v2\": 0.1286, \"2v3\": 0.1069, \"3v4\": 0.0643, \"4v5\": 0.0331, \"5v6\": 0.0271, \"6v7\": 0.0138}}}, \"exp_qwen_retrain_depth7\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 7, \"theta\": 0.6, \"max_depth\": 7, \"analysis_method\": \"5-fold GroupKFold CV\", \"pairwise_auc\": {\"0v1\": {\"mean\": 0.9837, \"std\": 0.0019, \"ci_95\": [0.9821, 0.9854], \"folds\": [0.9832, 0.9821, 0.9837, 0.9823, 0.9873]}, \"1v2\": {\"mean\": 0.8971, \"std\": 0.0025, \"ci_95\": [0.8949, 0.8993], \"folds\": [0.8923, 0.8988, 0.8986, 0.8991, 0.8967]}, \"2v3\": {\"mean\": 0.8098, \"std\": 0.0052, \"ci_95\": [0.8052, 0.8144], \"folds\": [0.8086, 0.8074, 0.818, 0.8024, 0.8128]}, \"3v4\": {\"mean\": 0.76, \"std\": 0.0082, \"ci_95\": [0.7528, 0.7672], \"folds\": [0.7534, 0.7617, 0.7753, 0.7566, 0.7531]}, \"4v5\": {\"mean\": 0.7459, \"std\": 0.0091, \"ci_95\": [0.7379, 0.7538], \"folds\": [0.7429, 0.7562, 0.7521, 0.73, 0.7482]}, \"5v6\": {\"mean\": 0.7017, \"std\": 0.0068, \"ci_95\": [0.6958, 0.7076], \"folds\": [0.7006, 0.7077, 0.7104, 0.6915, 0.6984]}, \"6v7\": {\"mean\": 0.641, \"std\": 0.0039, \"ci_95\": [0.6376, 0.6445], \"folds\": [0.6419, 0.6349, 0.6464, 0.639, 0.643]}}, \"jsd\": {\"0v1\": 0.23005, \"1v2\": 0.103924, \"2v3\": 0.075049, \"3v4\": 0.065398, \"4v5\": 0.060509, \"5v6\": 0.034998, \"6v7\": 0.017652}}}, \"exp_code_pythia1b4\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"theta\": 0.6, \"pairwise_auc\": {\"0v1\": {\"mean\": 0.9592, \"std\": 0.0036, \"folds\": [0.9576, 0.9576, 0.9657, 0.96, 0.9552]}, \"1v2\": {\"mean\": 0.5983, \"std\": 0.005, \"folds\": [0.601, 0.5884, 0.6, 0.5997, 0.6024]}, \"2v3\": {\"mean\": 0.5215, \"std\": 0.0128, \"folds\": [0.5236, 0.5124, 0.5311, 0.5024, 0.5381]}, \"3v4\": {\"mean\": 0.5152, \"std\": 0.012, \"folds\": [0.4981, 0.5327, 0.5092, 0.5123, 0.5238]}, \"4v5\": {\"mean\": 0.5046, \"std\": 0.0137, \"folds\": [0.4983, 0.4822, 0.5074, 0.5224, 0.5128]}}, \"jsd\": {\"0v1\": 0.070173, \"1v2\": 0.008211, \"2v3\": 0.003674, \"3v4\": 0.002902, \"4v5\": 0.002685}, \"ordinal\": {\"mae\": 1.3268, \"accuracy\": 0.3357}, \"top_features\": [\"freq_entropy\", \"surp_d1_mean\", \"surp_d2_mean\", \"surp_mean\", \"surp_d1_skew\"], \"features_csv\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4/features.csv\"}}, \"exp_028_power_curve\": {\"status\": \"DONE\", \"metrics\": {\"min_n_100pct\": 2000, \"n500_auc\": 0.5808, \"n500_rate\": 0.2, \"n1000_auc\": 0.5911, \"n1000_rate\": 0.3, \"n2000_auc\": 0.6101, \"n2000_rate\": 1, \"n3000_auc\": 0.6166, \"n3000_rate\": 1, \"n4000_auc\": 0.622, \"n4000_rate\": 1, \"n5000_auc\": 0.6288, \"n5000_rate\": 1}}, \"exp_qwen_retrain_chain\": {\"status\": \"DONE\", \"metrics\": {\"K_star_lower_bound\": 4, \"theta\": 0.6, \"auc_0v1\": 0.9838, \"auc_1v2\": 0.8969, \"auc_2v3\": 0.81, \"auc_3v4\": 0.7624, \"ci_0v1\": [0.982, 0.9855], \"ci_1v2\": [0.8937, 0.9001], \"ci_2v3\": [0.8052, 0.8147], \"ci_3v4\": [0.7543, 0.7706], \"ci_method\": \"5-fold CV\", \"jsd_0v1\": 0.2263, \"jsd_1v2\": 0.1046, \"jsd_2v3\": 0.0752, \"jsd_3v4\": 0.0654}}, \"exp_code_qwen1b5\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 2, \"theta\": 0.6, \"auc_0v1\": 0.9388, \"auc_1v2\": 0.7382, \"auc_2v3\": 0.53, \"auc_3v4\": 0.5022, \"auc_4v5\": 0.5219, \"ci_0v1\": [0.929, 0.949], \"ci_1v2\": [0.709, 0.767], \"ci_2v3\": [0.514, 0.546], \"jsd_0v1\": 0.0814, \"jsd_1v2\": 0.0443, \"jsd_2v3\": 0.0038, \"ordinal_accuracy\": 0.359, \"ordinal_mae\": 1.204}}, \"exp_olmo_retrain_chain\": {\"status\": \"DONE\"}, \"exp_028_subsampling_power\": {\"status\": \"DONE\", \"metrics\": {\"n_1000\": {\"mean_auc\": 0.608, \"std\": 0.012, \"detection_prob\": 0.9}, \"n_2500\": {\"mean_auc\": 0.618, \"std\": 0.006, \"detection_prob\": 1}, \"n_5000\": {\"mean_auc\": 0.629, \"std\": 0, \"detection_prob\": 1}, \"key_finding\": \"n>=2500 gives 100% reliable K*=2 detection. n=1000 already 90%. Signal is robust, not large-sample artifact.\"}}, \"exp_026_arxiv_filtering\": {\"status\": \"DONE\", \"metrics\": {\"runs_completed\": \"15/15\", \"strategies\": [\"no_filter\", \"binary\", \"graduated_a09\"], \"seeds\": [42, 123, 456, 789, 1024], \"mmlu\": {\"no_filter\": \"0.5899±0.0008\", \"binary\": \"0.5876±0.0004\", \"graduated_a09\": \"0.5900±0.0011\"}, \"hellaswag\": {\"no_filter\": \"0.6600±0.0002\", \"binary\": \"0.6642±0.0004\", \"graduated_a09\": \"0.6599±0.0003\"}, \"delta_vs_no_filter\": {\"binary_mmlu\": \"-0.0023\", \"binary_hellaswag\": \"+0.0042\", \"graduated_mmlu\": \"+0.0001\", \"graduated_hellaswag\": \"-0.0001\"}, \"key_finding\": \"All three strategies produce nearly identical results. Graduated ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\"}}, \"exp_027_latex_ablation\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"k_star_preserved\": true, \"pairwise_auc_original\": {\"0v1\": 0.9948, \"1v2\": 0.8581, \"2v3\": 0.6436, \"3v4\": 0.544, \"4v5\": 0.5299}, \"pairwise_auc_stripped\": {\"0v1\": 0.9948, \"1v2\": 0.8297, \"2v3\": 0.6229, \"3v4\": 0.5468, \"4v5\": 0.5476}, \"auc_delta\": {\"0v1\": 0, \"1v2\": -0.028, \"2v3\": -0.021, \"3v4\": 0.003, \"4v5\": 0.018}, \"latex_reduction_by_depth\": {\"depth_0\": \"0.6%\", \"depth_5\": \"4.4%\"}, \"key_finding\": \"K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still >θ=0.60). LaTeX format is NOT a confound.\"}}, \"exp_025_pythia_filtering\": {\"status\": \"DONE\", \"metrics\": {\"runs_completed\": \"9/9\", \"strategies\": [\"no_filter\", \"binary_ours\", \"graduated_a09\"], \"seeds\": [42, 123, 456], \"mmlu\": {\"no_filter\": \"0.2568±0.0012\", \"binary_ours\": \"0.2585±0.0004\", \"graduated_a09\": \"0.2561±0.0009\"}, \"hellaswag\": {\"no_filter\": \"0.5250±0.0008\", \"binary_ours\": \"0.5251±0.0001\", \"graduated_a09\": \"0.5253±0.0007\"}, \"delta_vs_no_filter\": {\"binary_ours_mmlu\": \"+0.0017\", \"binary_ours_hellaswag\": \"+0.0000\", \"graduated_a09_mmlu\": \"-0.0007\", \"graduated_a09_hellaswag\": \"+0.0003\"}, \"key_finding\": \"All three filtering strategies produce nearly identical results on Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering binary>graduated>no_filter NOT confirmed.\"}}, \"exp_14b_c4\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9598, \"1v2\": 0.621, \"2v3\": 0.5494, \"3v4\": 0.5243, \"4v5\": 0.5154}, \"pairwise_jsd\": {\"0v1\": 0.1097, \"1v2\": 0.0112, \"2v3\": 0.0062, \"3v4\": 0.0044, \"4v5\": 0.0036}, \"bootstrap_ci\": {\"0v1\": [0.9564, 0.963], \"1v2\": [0.6119, 0.6304], \"2v3\": [0.5392, 0.5594], \"3v4\": [0.514, 0.5346], \"4v5\": [0.5045, 0.5265]}, \"permutation_p\": {\"0v1\": \"<0.001\", \"1v2\": \"<0.001\", \"2v3\": \"<0.001\", \"3v4\": \"<0.001\", \"4v5\": \"<0.001\"}, \"k_star_statistically_confirmed\": true, \"ordinal_mae\": 1.2266, \"ordinal_accuracy\": 0.3497, \"top_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_std\", \"surp_d1_mean\", \"surp_d2_mean\"], \"key_finding\": \"K*=2 confirmed at 14B scale with bootstrap CI. 1v2 CI lower (0.6119) > theta=0.60; 2v3 CI upper (0.5594) < theta=0.60. All permutation p<0.001.\"}}, \"exp_arXiv_mistral7b_crossscorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"scorer\": \"pythia-1.4b\", \"auc_0v1\": 0.9798, \"auc_1v2\": 0.8141, \"auc_2v3\": 0.6075, \"auc_3v4\": 0.5489, \"auc_4v5\": 0.5391, \"jsd_0v1\": 0.135575, \"jsd_1v2\": 0.078, \"jsd_2v3\": 0.020452, \"jsd_3v4\": 0.010992, \"jsd_4v5\": 0.008831, \"ordinal_mae\": 0.9061, \"ordinal_accuracy\": 0.4412}}, \"exp_arXiv_llama8b_crossscorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"auc_0v1\": 0.9629, \"auc_1v2\": 0.8433, \"auc_2v3\": 0.6201, \"auc_3v4\": 0.523, \"auc_4v5\": 0.5245, \"jsd_0v1\": 0.1214, \"jsd_1v2\": 0.0815, \"jsd_2v3\": 0.0195, \"jsd_3v4\": 0.0083, \"jsd_4v5\": 0.0082, \"ordinal_mae\": 0.9025, \"ordinal_accuracy\": 0.4407, \"scorer\": \"pythia-1.4b\"}}, \"exp_arXiv_qwen7b_crossscorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"auc_0v1\": 0.9575, \"auc_1v2\": 0.8171, \"auc_2v3\": 0.5989, \"auc_3v4\": 0.5417, \"auc_4v5\": 0.5192, \"jsd_0v1\": 0.137085, \"jsd_1v2\": 0.059688, \"jsd_2v3\": 0.013508, \"jsd_3v4\": 0.009125, \"jsd_4v5\": 0.006738, \"ordinal_mae\": 0.9617, \"ordinal_accuracy\": 0.4255}}, \"exp_arXiv_qwen1b5_crossscorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"auc_0v1\": 0.9748, \"auc_1v2\": 0.8105, \"auc_2v3\": 0.6317, \"auc_3v4\": 0.5437, \"auc_4v5\": 0.5294, \"jsd_0v1\": 0.154297, \"jsd_1v2\": 0.066782, \"jsd_2v3\": 0.019268, \"jsd_3v4\": 0.008867, \"jsd_4v5\": 0.006991, \"ordinal_mae\": 0.9017, \"ordinal_accuracy\": 0.4402}}, \"exp_wiki_scorer_confound_1b5\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"confound_verdict\": \"confirmed\", \"auc_0v1\": 0.9729, \"auc_1v2\": 0.5994, \"auc_2v3\": 0.533, \"auc_3v4\": 0.5214, \"auc_4v5\": 0.5068, \"jsd_0v1\": 0.0886, \"ordinal_mae\": 1.2995, \"ordinal_accuracy\": 0.3466}}, \"exp_wiki_scorer_confound\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"confound_verdict\": \"confirmed\", \"auc_0v1\": 0.9404, \"auc_1v2\": 0.587, \"auc_2v3\": 0.5456, \"auc_3v4\": 0.525, \"auc_4v5\": 0.5172, \"critical_delta_1v2\": -0.0238}}, \"exp_wiki_qwen7b\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 2, \"auc_0v1\": 0.9673, \"auc_1v2\": 0.6108, \"auc_2v3\": 0.5562, \"auc_3v4\": 0.5297, \"auc_4v5\": 0.529, \"jsd_0v1\": 0.083514, \"jsd_1v2\": 0.010991, \"jsd_2v3\": 0.00555, \"jsd_3v4\": 0.004611, \"jsd_4v5\": 0.003894, \"ordinal_mae\": 1.2501, \"ordinal_accuracy\": 0.3532}}, \"exp_wiki_mistral7b\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"ordinal_mae\": 1.3445, \"ordinal_accuracy\": 0.3273, \"auc_0v1\": 0.9607, \"auc_1v2\": 0.5552, \"auc_2v3\": 0.5236, \"auc_3v4\": 0.5181, \"auc_4v5\": 0.5012, \"jsd_0v1\": 0.054134, \"jsd_1v2\": 0.005678, \"jsd_2v3\": 0.003698, \"jsd_3v4\": 0.003459, \"jsd_4v5\": 0.003274}}, \"exp_wiki_llama8b\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"ordinal_mae\": 1.2954, \"ordinal_accuracy\": 0.3313, \"auc_0v1\": 0.9316, \"auc_1v2\": 0.5954, \"auc_2v3\": 0.5392, \"auc_3v4\": 0.5221, \"auc_4v5\": 0.5212, \"jsd_0v1\": 0.06169, \"jsd_1v2\": 0.00931}}, \"exp_arXiv_qwen7b\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.983, \"1v2\": 0.835, \"2v3\": 0.626, \"3v4\": 0.544, \"4v5\": 0.513}, \"pairwise_jsd\": {\"0v1\": 0.1656, \"1v2\": 0.0668, \"2v3\": 0.0156, \"3v4\": 0.0089, \"4v5\": 0.0061}, \"ordinal_mae\": 0.9, \"ordinal_accuracy\": 0.446}}, \"exp_arXiv_mistral7b\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9848, \"1v2\": 0.8201, \"2v3\": 0.6275, \"3v4\": 0.5295, \"4v5\": 0.5295}, \"jsd\": {\"0v1\": 0.14249, \"1v2\": 0.076232, \"2v3\": 0.018972, \"3v4\": 0.009908, \"4v5\": 0.008877}, \"ordinal_mae\": 0.8958, \"ordinal_accuracy\": 0.4474, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_d1_skew\", \"surp_mean\", \"surp_d2_mean\"]}}, \"exp_arXiv_llama8b\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 3, \"auc_0v1\": 0.9754, \"auc_1v2\": 0.8447, \"auc_2v3\": 0.6215, \"auc_3v4\": 0.5362, \"auc_4v5\": 0.5331, \"jsd_0v1\": 0.1296, \"jsd_1v2\": 0.0785, \"jsd_2v3\": 0.0177, \"ordinal_acc\": 0.4549, \"ordinal_mae\": 0.8806}}, \"exp_wiki_pythia_v2\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.975, \"auc_1v2\": 0.5846, \"auc_2v3\": 0.5445, \"auc_3v4\": 0.5205, \"auc_4v5\": 0.5168, \"jsd_0v1\": 0.080065, \"jsd_1v2\": 0.007773, \"ordinal_acc\": 0.3503}}, \"exp_wiki_olmo_v2\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9932, \"auc_1v2\": 0.4986, \"auc_2v3\": 0.5012, \"auc_3v4\": 0.5057, \"auc_4v5\": 0.5009, \"jsd_0v1\": 0.1688, \"ordinal_acc\": 0.3227}}, \"exp_arXiv_olmo\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9958, \"auc_1v2\": 0.5034, \"auc_2v3\": 0.5069, \"auc_3v4\": 0.5021, \"auc_4v5\": 0.5037, \"jsd_0v1\": 0.329, \"ordinal_acc\": 0.33}}, \"exp_wiki_olmo\": {\"status\": \"DONE\"}, \"exp_wiki_pythia\": {\"status\": \"DONE\"}, \"exp_009_dose_response\": {\"status\": \"DONE\", \"metrics\": {\"total_runs\": 45, \"seeds\": 5, \"ratios\": [0.1, 0.3, 0.5], \"strategies\": [\"no_filter\", \"binary_ours\", \"graduated\"], \"cross_ratio_finding\": \"Binary filtering consistently best across all ratios. Graduated filtering = no_filter at every ratio. Effect size of binary advantage increases with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp). Original C3 hypothesis (graduated > binary) rejected.\", \"gpu_hours_total\": 9.9}}, \"exp_009_dose_50pct_v3\": {\"status\": \"DONE\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6063±0.0013\", \"hellaswag\": \"0.6680±0.0005\"}, \"binary_ours\": {\"mmlu\": \"0.6088±0.0011\", \"hellaswag\": \"0.6731±0.0004\"}, \"graduated\": {\"mmlu\": \"0.6062±0.0009\", \"hellaswag\": \"0.6679±0.0002\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0025, \"p_mmlu\": 0.0377, \"delta_hellaswag\": 0.0051, \"p_hellaswag\": 2e-05}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.0026, \"p_mmlu\": 0.0257, \"delta_hellaswag\": -0.0052, \"p_hellaswag\": 3e-05}, \"graduated_vs_nofilter\": {\"delta_mmlu\": -0.0001, \"p_mmlu\": 0.89, \"delta_hellaswag\": -0.0001, \"p_hellaswag\": 0.706}}, \"key_finding\": \"Binary significantly best (HellaSwag p<0.001). Graduated = no_filter exactly.\"}}, \"exp_009_dose_30pct_v3\": {\"status\": \"DONE\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6069±0.0007\", \"hellaswag\": \"0.6664±0.0020\"}, \"binary_ours\": {\"mmlu\": \"0.6082±0.0012\", \"hellaswag\": \"0.6725±0.0007\"}, \"graduated\": {\"mmlu\": \"0.6072±0.0008\", \"hellaswag\": \"0.6665±0.0014\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0013, \"p_mmlu\": 0.0739, \"delta_hellaswag\": 0.0061, \"p_hellaswag\": 0.0036}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.001, \"p_mmlu\": 0.3018, \"delta_hellaswag\": -0.006, \"p_hellaswag\": 0.0009}, \"graduated_vs_nofilter\": {\"delta_mmlu\": 0.0003, \"p_mmlu\": 0.6638, \"delta_hellaswag\": 0.0002, \"p_hellaswag\": 0.6646}}, \"key_finding\": \"Binary best on HellaSwag (p=0.004). Graduated = no_filter.\"}}, \"exp_009_dose_10pct_v3\": {\"status\": \"DONE\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6058±0.0002\", \"hellaswag\": \"0.6689±0.0007\"}, \"binary_ours\": {\"mmlu\": \"0.6079±0.0005\", \"hellaswag\": \"0.6727±0.0008\"}, \"graduated\": {\"mmlu\": \"0.6066±0.0011\", \"hellaswag\": \"0.6700±0.0015\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0021, \"p_mmlu\": 0.001, \"delta_hellaswag\": 0.0038, \"p_hellaswag\": 0.0017}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.0014, \"p_mmlu\": 0.0917, \"delta_hellaswag\": -0.0027, \"p_hellaswag\": 0.0399}, \"graduated_vs_nofilter\": {\"delta_mmlu\": 0.0008, \"p_mmlu\": 0.2706, \"delta_hellaswag\": 0.0011, \"p_hellaswag\": 0.0611}}, \"key_finding\": \"Binary best. Graduated ≈ no_filter.\"}}, \"exp_027_retrain_bootstrap\": {\"status\": \"DONE\", \"metrics\": {\"bootstrap_iterations\": 10000, \"pairs\": {\"0v1\": {\"auc_point\": 0.9847, \"ci_lower\": 0.9828, \"ci_upper\": 0.9864, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"1v2\": {\"auc_point\": 0.9482, \"ci_lower\": 0.9443, \"ci_upper\": 0.952, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"2v3\": {\"auc_point\": 0.8885, \"ci_lower\": 0.8829, \"ci_upper\": 0.894, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"3v4\": {\"auc_point\": 0.7977, \"ci_lower\": 0.7903, \"ci_upper\": 0.8051, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}}, \"key_finding\": \"All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001.\"}}, \"exp_026_feature_stability_v2\": {\"status\": \"DONE\", \"metrics\": {\"data_source\": \"exp_001_pythia prompt-chain (K*=2)\", \"results\": {\"15D\": {\"num_tested\": 1, \"num_pass\": 1, \"min_1v2_auc\": 0.6262, \"mean_1v2_auc\": 0.6262}, \"10D\": {\"num_tested\": 5, \"num_pass\": 5, \"min_1v2_auc\": 0.6153, \"mean_1v2_auc\": 0.6191}, \"8D\": {\"num_tested\": 5, \"num_pass\": 5, \"min_1v2_auc\": 0.6056, \"mean_1v2_auc\": 0.6159}, \"5D\": {\"num_tested\": 5, \"num_pass\": 2, \"min_1v2_auc\": 0.5856, \"mean_1v2_auc\": 0.5998}, \"3D_top3\": {\"num_tested\": 1, \"num_pass\": 0, \"min_1v2_auc\": 0.5871, \"mean_1v2_auc\": 0.5871}}, \"key_finding\": \"8+ features sufficient for robust K*=2 (all pass θ=0.60). 5D fragile (2/5 pass). Top-3 alone fails. Feature diversity matters at the K* boundary.\"}}, \"exp_026_feature_stability\": {\"status\": \"DONE\", \"metrics\": {\"data_source\": \"exp_016_qwen_base (prompt-chain, K*=2)\", \"results\": {\"15D\": {\"num_tested\": 1, \"num_kstar_2\": 1, \"min_1v2_auc\": 0.6262, \"mean_1v2_auc\": 0.6262}, \"10D\": {\"num_tested\": 5, \"num_kstar_2\": 5, \"min_1v2_auc\": 0.6153, \"mean_1v2_auc\": 0.6191}, \"8D\": {\"num_tested\": 5, \"num_kstar_2\": 5, \"min_1v2_auc\": 0.6056, \"mean_1v2_auc\": 0.6159}, \"5D\": {\"num_tested\": 5, \"num_kstar_2\": 2, \"min_1v2_auc\": 0.5856, \"mean_1v2_auc\": 0.5998}, \"3D_top3\": {\"num_tested\": 1, \"num_kstar_2\": 0, \"min_1v2_auc\": 0.5871, \"mean_1v2_auc\": 0.5871}}, \"all_above_theta\": false, \"key_finding\": \"Feature selection MATTERS at K*=2 boundary. 15D/10D/8D all robust (min 1v2 AUC > 0.60). 5D random subsets: only 2/5 pass θ=0.60 (min=0.5856). Top-3 features alone (0.5871) fail θ. Contrast with retrain-chain (K*=4) where all subsets trivially passed (min=0.8314).\", \"previous_run_note\": \"v1 used retrain-chain data (K*=4), where all subsets trivially passed with min 1v2 AUC=0.8314. v2 uses prompt-chain data (K*=2) to test boundary robustness.\"}}, \"exp_027\": {\"status\": \"DONE\", \"metrics\": {\"kstar_ci\": 4, \"0v1_auc\": 0.9847, \"0v1_ci\": [0.9828, 0.9864], \"0v1_perm_p\": 0.0001, \"1v2_auc\": 0.9482, \"1v2_ci\": [0.9443, 0.952], \"1v2_perm_p\": 0.0001, \"2v3_auc\": 0.8885, \"2v3_ci\": [0.8829, 0.894], \"2v3_perm_p\": 0.0001, \"3v4_auc\": 0.7977, \"3v4_ci\": [0.7903, 0.8051], \"3v4_perm_p\": 0.0001, \"all_ci_lower_above_theta\": true}}, \"exp_005_degradation\": {\"status\": \"DONE\", \"metrics\": {\"cross_model_kendall_tau_by_first_auc\": {\"Pythia_vs_OLMo\": 0.733, \"Pythia_vs_Qwen_rewrite\": 0.467, \"Pythia_vs_Qwen_cont\": 0.695, \"OLMo_vs_Qwen_rewrite\": 0.429, \"OLMo_vs_Qwen_cont\": 0.543, \"Qwen_rewrite_vs_Qwen_cont\": 0.733}, \"cross_model_kendall_tau_by_avg_auc\": {\"Pythia_vs_OLMo\": 0.8476, \"Pythia_vs_Qwen_cont\": 0.7524, \"OLMo_vs_Qwen_cont\": 0.6762}, \"cross_model_spearman_rho_single_feature_auc\": {\"Pythia_vs_OLMo\": 0.95, \"Pythia_vs_Qwen_cont\": 0.9143, \"OLMo_vs_Qwen_cont\": 0.85, \"metric_definition\": \"Spearman ρ on per-feature AUC rankings (each feature independently classifies depth pairs)\"}, \"4model_tau_mean_continuation_by_first_auc\": 0.657, \"4model_tau_mean_all_by_first_auc\": 0.6, \"generation_mode_delta\": {\"Pythia_vs_Qwen\": \"+0.228\", \"OLMo_vs_Qwen\": \"+0.114\"}, \"top3_features_ranking_by_first_auc\": {\"Pythia\": [\"surp_d1_std\", \"surp_d2_std\", \"surp_std\"], \"OLMo\": [\"surp_std\", \"surp_d1_std\", \"surp_d2_std\"], \"Qwen_rewrite\": [\"freq_entropy\", \"surp_std\", \"surp_d1_std\"], \"Qwen_cont\": [\"surp_d1_std\", \"surp_std\", \"surp_d2_std\"]}, \"shared_top_discriminators\": \"surp_d1_std, surp_std, surp_d2_std shared across all architectures (single-feature AUC ranking)\", \"degradation_ordering_consistency\": \"Strong cross-model consistency (ρ≥0.85) on single-feature AUC ranking under controlled generation mode.\", \"residual_architecture_effect\": \"Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\", \"limitation_1v2_weakness\": \"depth-pair level consistency weakest at 1v2 (τ~0.37), near-generational feature importance ordering varies more across models\"}}, \"exp_024_arxiv_domain\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9946, \"1v2\": 0.858, \"2v3\": 0.6427, \"3v4\": 0.5437, \"4v5\": 0.5294}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9946, \"ci_lower\": 0.9929, \"ci_upper\": 0.9961, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.858, \"ci_lower\": 0.848, \"ci_upper\": 0.8679, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.6427, \"ci_lower\": 0.6275, \"ci_upper\": 0.6575, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5437, \"ci_lower\": 0.5276, \"ci_upper\": 0.5598, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5294, \"ci_lower\": 0.5133, \"ci_upper\": 0.5455, \"perm_p\": 0.0006}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\"}}, \"exp_017_qwen_continuation\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9972, \"1v2\": 0.6114, \"2v3\": 0.5609, \"3v4\": 0.5408, \"4v5\": 0.5139}, \"pairwise_jsd\": {\"0v1\": 0.28627, \"1v2\": 0.005107, \"2v3\": 0.003603, \"3v4\": 0.003395, \"4v5\": 0.003085}, \"ordinal_mae\": 1.1547, \"ordinal_accuracy\": 0.3819, \"top3_features\": [\"freq_entropy\", \"surp_mean\", \"surp_std\"]}}, \"exp_012_binary_confidence\": {\"status\": \"DONE\", \"metrics\": {\"n_samples\": 500, \"generators\": [\"qwen-rewrite\", \"pythia-1.4b\", \"olmo-1b\", \"qwen-cont\"], \"6class_accuracy\": {\"qwen-rewrite\": 0.1987, \"pythia-1.4b\": 0.1303, \"olmo-1b\": 0.127, \"qwen-cont\": 0.1833, \"random_baseline\": 0.1667}, \"spearman_rho\": {\"qwen-rewrite\": {\"log_ppl_ref\": -0.1233, \"log_ppl_obs\": 0.0815, \"ppl_ratio\": 0.1185}, \"pythia-1.4b\": {\"log_ppl_ref\": -0.2972, \"log_ppl_obs\": -0.4529, \"ppl_ratio\": -0.392}, \"olmo-1b\": {\"log_ppl_ref\": -0.378, \"log_ppl_obs\": -0.4614, \"ppl_ratio\": -0.4068}, \"qwen-cont\": {\"log_ppl_ref\": -0.3887, \"log_ppl_obs\": -0.162, \"ppl_ratio\": -0.058}}, \"binary_detector_kstar\": 1, \"obd_kstar\": 2, \"auc_non_monotonic\": true, \"key_finding\": \"Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but practically weak). AUC non-monotonic — binary detectors cannot maintain depth ordering. Confirms binary confidence ≠ depth estimation.\"}}, \"exp_C_permutation_10k\": {\"status\": \"DONE\", \"metrics\": {\"resamples\": 10000, \"all_boundary_pairs_p\": \"<0.0001\", \"key_finding\": \"10K permutation confirms all boundary p-values well below 0.01. FR-11 resolved.\"}}, \"exp_002_olmo_depth\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.997, \"1v2\": 0.6146, \"2v3\": 0.5497, \"3v4\": 0.509, \"4v5\": 0.5044}, \"pairwise_auc_std\": {\"0v1\": 0.0004, \"1v2\": 0.0029, \"2v3\": 0.004, \"3v4\": 0.0084, \"4v5\": 0.0136}, \"pairwise_jsd\": {\"0v1\": 0.23941, \"1v2\": 0.012972, \"2v3\": 0.00735, \"3v4\": 0.003968, \"4v5\": 0.003851}, \"ordinal_mae\": 1.1813, \"ordinal_accuracy\": 0.3685, \"top_features\": [\"surp_d1_mean\", \"surp_d1_skew\", \"freq_kurtosis\", \"surp_d2_mean\", \"surp_mean\"]}}, \"exp_009_dose_50pct_v2\": {\"status\": \"DONE\"}, \"exp_009_dose_30pct_v2\": {\"status\": \"DONE\"}, \"exp_009_dose_10pct_v2\": {\"status\": \"DONE\"}, \"exp_009_dose_50pct\": {\"status\": \"DONE\"}, \"exp_009_dose_30pct\": {\"status\": \"DONE\"}, \"exp_009_dose_10pct\": {\"status\": \"DONE\"}, \"exp_kstar_theta\": {\"status\": \"DONE\", \"metrics\": {\"output_files\": [\"kstar_theta_curve.pdf (32KB)\", \"kstar_theta_curve.png (335KB)\"], \"models\": [\"Qwen-rewrite\", \"Pythia\", \"OLMo\", \"Qwen-cont\"], \"depth_pairs\": 5, \"key_finding\": \"All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5. θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical resolved.\"}}, \"exp_022_cross_scorer_matrix\": {\"status\": \"DONE\", \"metrics\": {\"total_combos\": 12, \"completed\": 12, \"K_star_distribution\": {\"K2\": 11, \"K1\": 1}, \"matrix\": {\"pythia_greedy×olmo\": {\"K_star\": 2, \"1v2\": 0.8811}, \"pythia_greedy×pythia\": {\"K_star\": 2, \"1v2\": 0.8838}, \"pythia_greedy×qwen_base\": {\"K_star\": 2, \"1v2\": 0.8814}, \"pythia_greedy×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.8818}, \"qwen_base×olmo\": {\"K_star\": 2, \"1v2\": 0.6047}, \"qwen_base×pythia\": {\"K_star\": 2, \"1v2\": 0.617}, \"qwen_base×qwen_base\": {\"K_star\": 2, \"1v2\": 0.6262}, \"qwen_base×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.6273}, \"qwen_cont256×olmo\": {\"K_star\": 2, \"1v2\": 0.6028}, \"qwen_cont256×pythia\": {\"K_star\": 1, \"1v2\": 0.5979}, \"qwen_cont256×qwen_base\": {\"K_star\": 2, \"1v2\": 0.6282}, \"qwen_cont256×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.6072}}, \"key_finding\": \"Scorer independence confirmed: K*=2 in 11/12 combos. Only exception: qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.\"}}, \"exp_008_retrain_chain_v2\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": \">=4\", \"pairwise_auc\": {\"0v1\": 0.9847, \"1v2\": 0.9484, \"2v3\": 0.8888, \"3v4\": 0.7982}, \"pairwise_jsd\": {\"0v1\": 0.17, \"1v2\": 0.12, \"2v3\": 0.064, \"3v4\": 0.04}, \"key_finding\": \"Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic boundary.\"}}, \"exp-008-retrain-chain\": {\"status\": \"DONE\"}, \"exp_025_pythia_arxiv\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9877, \"1v2\": 0.8047, \"2v3\": 0.6545, \"3v4\": 0.5507, \"4v5\": 0.5287}, \"pairwise_jsd\": {\"0v1\": 0.171338, \"1v2\": 0.057344, \"2v3\": 0.019524, \"3v4\": 0.009917, \"4v5\": 0.008846}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9876, \"ci_lower\": 0.9851, \"ci_upper\": 0.99, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.8047, \"ci_lower\": 0.7934, \"ci_upper\": 0.8162, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.6544, \"ci_lower\": 0.6401, \"ci_upper\": 0.6688, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.55, \"ci_lower\": 0.534, \"ci_upper\": 0.5657, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5284, \"ci_lower\": 0.5122, \"ci_upper\": 0.5443, \"perm_p\": 0.001}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"n_samples\": 2200, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_mean\", \"surp_d1_skew\", \"surp_d1_mean\"], \"ordinal\": {\"MAE\": 0.8518, \"Accuracy\": 0.4545}, \"key_finding\": \"Pythia-1.4B on arXiv yields K*=3, identical to exp-024 (Qwen on arXiv). 2v3 CI lower=0.6401 > θ=0.60. Domain saturation depth is model-invariant for arXiv.\"}}, \"exp_020_pythia_decoding\": {\"status\": \"DONE\", \"metrics\": {\"greedy\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9992, \"1v2\": 0.8838, \"2v3\": 0.5342, \"3v4\": 0.5228, \"4v5\": 0.5162}}, \"nuc09\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9948, \"1v2\": 0.677, \"2v3\": 0.5549, \"3v4\": 0.5299, \"4v5\": 0.5013}}, \"t07\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9965, \"1v2\": 0.7265, \"2v3\": 0.5941, \"3v4\": 0.5698, \"4v5\": 0.5284}}, \"t12\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9933, \"1v2\": 0.6172, \"2v3\": 0.5226, \"3v4\": 0.517, \"4v5\": 0.5051}}}}, \"exp_021_length_ablation\": {\"status\": \"DONE\", \"metrics\": {\"128tok\": {\"K_star\": 2, \"1v2_auc\": 0.6219}, \"256tok\": {\"K_star\": 2, \"1v2_auc\": 0.6282}, \"512tok\": {\"K_star\": 2, \"1v2_auc\": 0.6073}, \"all_K_star_2\": true, \"bootstrap_ci\": {\"512tok_1v2\": {\"auc\": 0.6073, \"ci_lower\": 0.5979, \"ci_upper\": 0.6166, \"perm_p\": 0.0001, \"verdict\": \"BORDERLINE\"}}}}, \"exp_018_llama8b_depth\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9225, \"1v2\": 0.6123, \"2v3\": 0.5274, \"3v4\": 0.5138, \"4v5\": 0.5097}, \"jsd\": {\"0v1\": 0.077, \"1v2\": 0.012, \"2v3\": 0.005}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9224, \"ci_lower\": 0.9174, \"ci_upper\": 0.9272, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6123, \"ci_lower\": 0.6028, \"ci_upper\": 0.6216, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5273, \"ci_lower\": 0.5169, \"ci_upper\": 0.5378, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5168, \"ci_lower\": 0.5062, \"ci_upper\": 0.5275, \"perm_p\": 0.0037}, \"4v5\": {\"auc\": 0.5159, \"ci_lower\": 0.5052, \"ci_upper\": 0.5268, \"perm_p\": 0.0035}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000}}, \"exp_023_domain_ablation\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 2, \"1v2_auc\": 0.6193, \"2v3_auc\": 0.5498, \"all_folds_above_060\": true, \"top_feature\": \"freq_entropy\", \"ordinal_accuracy\": 0.377}}, \"exp_019b_mistral_cross_scorer\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9209, \"1v2\": 0.5695, \"2v3\": 0.5335, \"3v4\": 0.514, \"4v5\": 0.5184}, \"bootstrap_ci\": {\"0v1\": {\"mean\": 0.9209, \"ci_lower\": 0.9189, \"ci_upper\": 0.9229, \"pass_060\": true}, \"1v2\": {\"mean\": 0.5696, \"ci_lower\": 0.5645, \"ci_upper\": 0.5746, \"pass_060\": false}, \"2v3\": {\"mean\": 0.5335, \"ci_lower\": 0.5283, \"ci_upper\": 0.5382, \"pass_060\": false}, \"3v4\": {\"mean\": 0.514, \"ci_lower\": 0.5063, \"ci_upper\": 0.5213, \"pass_060\": false}, \"4v5\": {\"mean\": 0.5183, \"ci_lower\": 0.5128, \"ci_upper\": 0.5244, \"pass_060\": false}}, \"jsd\": {\"0v1\": 0.08355, \"1v2\": 0.007642, \"2v3\": 0.004752, \"3v4\": 0.004255, \"4v5\": 0.003758}, \"ordinal_mae\": 1.3737, \"ordinal_accuracy\": 0.3179, \"top3_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_d1_mean\"], \"key_finding\": \"Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2 AUC=0.5695 (self-scorer was 0.5935) — cross-scorer LOWER, not higher. Mistral K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact.\"}}, \"exp_019_mistral7b_depth\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9843, \"1v2\": 0.5935, \"2v3\": 0.5402, \"3v4\": 0.5232, \"4v5\": 0.5181}, \"bootstrap_ci_1v2\": {\"ci_lower\": 0.5835, \"ci_upper\": 0.6032, \"p_auc_leq_060\": 0.9017}, \"jsd\": {\"0v1\": 0.124194, \"1v2\": 0.008051, \"2v3\": 0.005047, \"3v4\": 0.004516, \"4v5\": 0.004109}, \"ordinal_mae\": 1.2275, \"ordinal_accuracy\": 0.3567, \"top3_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_d1_mean\"]}}, \"exp_016_base_vs_instruct\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.987, \"1v2\": 0.6262, \"2v3\": 0.5496, \"3v4\": 0.5294, \"4v5\": 0.5182}, \"pairwise_auc_std\": {\"0v1\": 0.0015, \"1v2\": 0.0152, \"2v3\": 0.0067, \"3v4\": 0.0132, \"4v5\": 0.0139}, \"pairwise_jsd\": {\"0v1\": 0.163726, \"1v2\": 0.01081, \"2v3\": 0.005311, \"3v4\": 0.003942, \"4v5\": 0.003522}, \"ordinal_mae\": 1.1691, \"ordinal_accuracy\": 0.3719, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_d1_skew\", \"surp_d1_mean\", \"surp_mean\"], \"n_samples\": 30000, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.987, \"ci_lower\": 0.9853, \"ci_upper\": 0.9885, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.626, \"ci_lower\": 0.6168, \"ci_upper\": 0.6353, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5397, \"ci_upper\": 0.56, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5293, \"ci_lower\": 0.5188, \"ci_upper\": 0.5399, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5181, \"ci_lower\": 0.5075, \"ci_upper\": 0.5288, \"perm_p\": 0.0016}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95% CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015, 0.6213] — no significant base-vs-instruct difference.\"}}, \"exp_003_decoding_ablation\": {\"status\": \"DONE\", \"metrics\": {\"K_star\": 2, \"K_star_robust\": true, \"bootstrap_ci\": {\"config1_greedy\": {\"0v1\": {\"auc\": 0.9796, \"ci\": [0.9772, 0.982], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6892, \"ci\": [0.6802, 0.6982], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5612, \"ci\": [0.5517, 0.5705], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.5405, \"ci\": [0.5308, 0.5502], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5137, \"ci\": [0.5033, 0.5238], \"perm_p\": 0.0082}}, \"config2_nuc09\": {\"0v1\": {\"auc\": 0.9945, \"ci\": [0.9934, 0.9956], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6862, \"ci\": [0.6774, 0.6951], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5917, \"ci\": [0.5824, 0.601], \"perm_p\": 0, \"note\": \"CI upper crosses theta=0.60\"}, \"3v4\": {\"auc\": 0.5468, \"ci\": [0.5369, 0.5568], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5066, \"ci\": [0.4959, 0.5173], \"perm_p\": 0.1199}}, \"config3_t07\": {\"0v1\": {\"auc\": 0.9877, \"ci\": [0.9857, 0.9896], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6885, \"ci\": [0.6797, 0.697], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5901, \"ci\": [0.5806, 0.5996], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.539, \"ci\": [0.5288, 0.5493], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5348, \"ci\": [0.5243, 0.5454], \"perm_p\": 0}}, \"config4_t12\": {\"0v1\": {\"auc\": 0.9982, \"ci\": [0.9975, 0.9987], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.7037, \"ci\": [0.6945, 0.7126], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.582, \"ci\": [0.5722, 0.5917], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.5293, \"ci\": [0.5185, 0.5399], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5237, \"ci\": [0.5132, 0.5347], \"perm_p\": 0.0001}}, \"resamples\": 10000, \"method\": \"GroupKFold(5) OOF + doc-level bootstrap + label permutation\"}}}, \"exp_004_7b_crossscale\": {\"status\": \"DONE\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9644, \"1v2\": 0.6178, \"2v3\": 0.546, \"3v4\": 0.5225, \"4v5\": 0.5091}, \"pairwise_auc_std\": {\"0v1\": 0.0034, \"1v2\": 0.0081, \"2v3\": 0.0028, \"3v4\": 0.0113, \"4v5\": 0.0052}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9638, \"ci_lower\": 0.9607, \"ci_upper\": 0.9665, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6168, \"ci_lower\": 0.6079, \"ci_upper\": 0.6261, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5492, \"ci_lower\": 0.5388, \"ci_upper\": 0.5594, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5276, \"ci_lower\": 0.517, \"ci_upper\": 0.5375, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5085, \"ci_lower\": 0.4988, \"ci_upper\": 0.5191, \"perm_p\": 0.0676}}, \"bootstrap_resamples\": 1000, \"permutation_resamples\": 10000, \"pairwise_jsd\": {\"0v1\": 0.127422, \"1v2\": 0.010114, \"2v3\": 0.004798, \"3v4\": 0.004821, \"4v5\": 0.003335}, \"ordinal_mae\": 1.2156, \"ordinal_accuracy\": 0.3523, \"top_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_std\", \"surp_d1_mean\", \"surp_mean\"], \"key_finding\": \"K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60 (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676). FR-4 Warning resolved.\"}}, \"exp_E_paired_stats\": {\"status\": \"DONE\", \"metrics\": {\"mmlu_significant_pairs\": \"8/15\", \"hellaswag_significant_pairs\": \"9/15\", \"binary_ours_vs_all_mmlu\": \"all significant\", \"max_cohen_d_mmlu\": 10.8, \"max_cohen_d_hellaswag\": 8.98, \"graduated_a09_vs_dsir_corrected_p\": 0.0523, \"cohen_d_method\": \"d_av (Lakens 2013)\", \"key_finding\": \"binary-ours significantly outperforms all alternatives on MMLU. On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni cummax bug fixed: MMLU 10/15→8/15. Cohen's d changed to d_av.\", \"bugfix_note\": \"Holm-Bonferroni cummax variable was never updated, causing 2 MMLU pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\"}}, \"exp_D_obd_n500\": {\"status\": \"DONE\", \"metrics\": {\"obd_accuracy_final\": 0.38, \"obd_ci\": [0.34, 0.422], \"mcnemar_vs_gpt55_p\": 0.0809, \"mcnemar_vs_claude_p\": 0.0693, \"mcnemar_significant\": false, \"multi_seed_std\": 0, \"per_depth\": {\"d0\": 0.96, \"d1\": 0.39, \"d2\": 0.14, \"d3\": 0.19, \"d4\": 0.22}, \"prob_merge_accuracy\": 0.444, \"prob_merge_d4_bias\": 0.8, \"note\": \"v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant — supports discussion.tex narrative\"}}, \"exp_B_14d_ablation\": {\"status\": \"DONE\", \"metrics\": {\"result\": \"K*=2 stable across all 4 models after removing self_BLEU (14D)\", \"key_finding\": \"self_BLEU removal does not change K* boundary. FR-3 resolved.\"}}, \"exp_A_alt_scorer\": {\"status\": \"DONE\", \"metrics\": {\"pythia_qwen_rw\": {\"k_star\": 2, \"auc_0v1\": 0.9923, \"auc_1v2\": 0.7012, \"auc_2v3\": 0.587, \"mae\": 1.006, \"accuracy\": 0.417, \"spearman_rho_vs_baseline\": 0.906}, \"pythia_qwen_cont\": {\"k_star\": 1, \"auc_0v1\": 0.99, \"auc_1v2\": 0.5923, \"auc_2v3\": null, \"mae\": 1.216, \"accuracy\": 0.371, \"spearman_rho_vs_baseline\": 0.942}, \"olmo_qwen_rw\": {\"k_star\": 2, \"auc_0v1\": 0.9918, \"auc_1v2\": 0.6947, \"auc_2v3\": null, \"mae\": 1.016, \"accuracy\": 0.413, \"spearman_rho_vs_baseline\": 0.92}, \"olmo_qwen_cont\": {\"k_star\": 1, \"auc_0v1\": 0.989, \"auc_1v2\": 0.5858, \"auc_2v3\": null, \"mae\": 1.229, \"accuracy\": 0.368, \"spearman_rho_vs_baseline\": 0.902}, \"key_finding\": \"K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1 (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer independence of feature ranking.\"}}, \"exp_015_neural_probe\": {\"status\": \"DONE\", \"metrics\": {\"pythia\": {\"k_star_neural\": 2, \"k_star_lgbm\": 2, \"accuracy\": 0.3892, \"pairwise_auc\": {\"0v1\": 0.966, \"1v2\": 0.676, \"2v3\": 0.596, \"3v4\": 0.555, \"4v5\": 0.532}}, \"olmo\": {\"k_star_neural\": 2, \"k_star_lgbm\": 2, \"accuracy\": 0.3729, \"pairwise_auc\": {\"0v1\": 0.95, \"1v2\": 0.657, \"2v3\": 0.589, \"3v4\": 0.547, \"4v5\": 0.53}}, \"qwen_cont\": {\"k_star_neural\": 3, \"k_star_lgbm\": 2, \"accuracy\": 0.4368, \"pairwise_auc\": {\"0v1\": 0.988, \"1v2\": 0.702, \"2v3\": 0.616, \"3v4\": 0.59, \"4v5\": 0.566}}, \"key_finding\": \"Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3 only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\"}}, \"exp_006_graduated_filtering\": {\"status\": \"DONE\", \"metrics\": {\"total_runs\": 51, \"binary_ours\": {\"mmlu\": \"0.5941±0.0008\", \"hellaswag\": \"0.6701±0.0006\"}, \"binary_drayson\": {\"mmlu\": \"0.5913±0.0009\", \"hellaswag\": \"0.6691±0.0004\"}, \"surprisal\": {\"mmlu\": \"0.5894±0.0009\", \"hellaswag\": \"0.6641±0.0006\"}, \"graduated_a09\": {\"mmlu\": \"0.5892±0.0008\", \"hellaswag\": \"0.6701±0.0007\"}, \"graduated_a07\": {\"mmlu\": \"0.5892±0.0014\", \"hellaswag\": \"0.6695±0.0004\"}, \"graduated_a05\": {\"mmlu\": \"0.5880±0.0013\", \"hellaswag\": \"0.6687±0.0008\"}, \"graduated_a03\": {\"mmlu\": \"0.5877±0.0013\", \"hellaswag\": \"0.6669±0.0005\"}, \"graduated_a01\": {\"mmlu\": \"0.5873±0.0019\", \"hellaswag\": \"0.6640±0.0009\"}, \"dsir\": {\"mmlu\": \"0.5869±0.0003\", \"hellaswag\": \"0.6631±0.0007\"}, \"no_filter\": {\"mmlu\": \"0.5865±0.0010\", \"hellaswag\": \"0.6638±0.0008\"}, \"base_model\": {\"mmlu\": \"0.6018\", \"hellaswag\": \"0.6821\"}, \"best_strategy\": \"binary-ours\", \"key_finding\": \"binary-ours is best filtering strategy. All strategies degrade vs base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR below all other strategies except no-filter.\"}}, \"exp_007_bootstrap_ci\": {\"status\": \"DONE\", \"metrics\": {\"qwen_rewrite\": {\"0v1\": {\"auc\": 0.9956, \"ci_lower\": 0.9946, \"ci_upper\": 0.9965, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6955, \"ci_lower\": 0.6859, \"ci_upper\": 0.7041, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5893, \"ci_lower\": 0.5795, \"ci_upper\": 0.5991, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5435, \"ci_lower\": 0.5333, \"ci_upper\": 0.5551, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.534, \"ci_lower\": 0.5238, \"ci_upper\": 0.5448, \"perm_p\": 0.002}}, \"pythia_cont\": {\"0v1\": {\"auc\": 0.9932, \"ci_lower\": 0.9921, \"ci_upper\": 0.9943, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6539, \"ci_lower\": 0.6454, \"ci_upper\": 0.663, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5514, \"ci_lower\": 0.5417, \"ci_upper\": 0.5628, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5152, \"ci_lower\": 0.5041, \"ci_upper\": 0.526, \"perm_p\": 0.006}, \"4v5\": {\"auc\": 0.5136, \"ci_lower\": 0.5021, \"ci_upper\": 0.5249, \"perm_p\": 0.008}}, \"olmo_cont\": {\"0v1\": {\"auc\": 0.997, \"ci_lower\": 0.9964, \"ci_upper\": 0.9975, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6145, \"ci_lower\": 0.6045, \"ci_upper\": 0.6247, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5399, \"ci_upper\": 0.5596, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5091, \"ci_lower\": 0.4973, \"ci_upper\": 0.52, \"perm_p\": 0.064}, \"4v5\": {\"auc\": 0.5045, \"ci_lower\": 0.4932, \"ci_upper\": 0.515, \"perm_p\": 0.232}}, \"qwen_cont\": {\"0v1\": {\"auc\": 0.9971, \"ci_lower\": 0.9963, \"ci_upper\": 0.9978, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6112, \"ci_lower\": 0.6015, \"ci_upper\": 0.6213, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5609, \"ci_lower\": 0.5511, \"ci_upper\": 0.5712, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5409, \"ci_lower\": 0.5308, \"ci_upper\": 0.5508, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.5141, \"ci_lower\": 0.5035, \"ci_upper\": 0.5255, \"perm_p\": 0.006}}, \"k_star_robust\": true, \"all_1v2_ci_lower_above_060\": true, \"most_marginal\": \"Qwen-cont CI lower=0.6015, only 0.0015 above threshold\"}}, \"exp_011_llm_zeroshot\": {\"status\": \"DONE\", \"metrics\": {\"gpt55_5class_acc\": 0.332, \"gpt55_mae\": 1.102, \"gpt55_spearman\": 0.383, \"gpt55_binary_acc\": 0.878, \"claude_5class_acc\": 0.331, \"claude_mae\": 1.15, \"claude_spearman\": 0.416, \"claude_binary_acc\": 0.882, \"odb_baseline_5class_acc\": 0.386, \"odb_baseline_mae\": 1.107, \"gpt55_per_depth_acc\": {\"depth_0\": 0.77, \"depth_1\": 0.19, \"depth_2\": 0.38, \"depth_3\": 0.24, \"depth_4\": 0.08}, \"claude_per_depth_acc\": {\"depth_0\": 0.69, \"depth_1\": 0.21, \"depth_2\": 0.28, \"depth_3\": 0.101, \"depth_4\": 0.37}, \"n_samples_per_model\": 500, \"key_finding\": \"Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails.\"}}, \"exp_013_cross_transfer\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_matrix\": {\"Qwen_rw→Qwen_rw\": 0.4229, \"Qwen_rw→Pythia\": 0.259, \"Qwen_rw→OLMo\": 0.2653, \"Qwen_rw→Qwen_cont\": 0.3466, \"Pythia→Qwen_rw\": 0.2718, \"Pythia→Pythia\": 0.3856, \"Pythia→OLMo\": 0.3531, \"Pythia→Qwen_cont\": 0.3287, \"OLMo→Qwen_rw\": 0.2768, \"OLMo→Pythia\": 0.345, \"OLMo→OLMo\": 0.3822, \"OLMo→Qwen_cont\": 0.3244, \"Qwen_cont→Qwen_rw\": 0.344, \"Qwen_cont→Pythia\": 0.3284, \"Qwen_cont→OLMo\": 0.3112, \"Qwen_cont→Qwen_cont\": 0.3875}, \"transfer_retention_accuracy\": {\"Pythia↔OLMo\": \"91-92%\", \"Qwen_rw→Pythia/OLMo\": \"61-63%\", \"Qwen_cont↔Pythia\": \"83-85%\", \"Qwen_cont↔OLMo\": \"80-85%\"}, \"transfer_retention_tau\": {\"Pythia↔OLMo\": \"85-86%\", \"Qwen_rw→Pythia/OLMo\": \"45-50%\", \"Qwen_cont↔others\": \"68-83%\"}, \"mean_pw_auc_matrix\": {\"within_avg\": 0.6099, \"cross_avg\": 0.5905, \"0v1_cross_all_above\": 0.96}, \"key_finding\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better.\"}}, \"exp_010_ordinal_baseline\": {\"status\": \"DONE\", \"metrics\": {\"qwen_rewrite\": {\"obd_lgbm\": {\"accuracy\": 0.4229, \"mae\": 0.9836, \"tau_b\": 0.5518, \"mean_pw_auc\": 0.6214}, \"multiclass_lgbm\": {\"accuracy\": 0.4182, \"mae\": 1.0163, \"tau_b\": 0.5367, \"mean_pw_auc\": 0.6246}, \"ordinal_logreg\": {\"accuracy\": 0.3636, \"mae\": 0.9105, \"tau_b\": 0.563, \"mean_pw_auc\": 0.5022}}, \"pythia\": {\"obd_lgbm\": {\"accuracy\": 0.3856, \"mae\": 1.1072, \"tau_b\": 0.4745, \"mean_pw_auc\": 0.6055}, \"multiclass_lgbm\": {\"accuracy\": 0.3832, \"mae\": 1.1399, \"tau_b\": 0.4622, \"mean_pw_auc\": 0.6062}, \"ordinal_logreg\": {\"accuracy\": 0.3179, \"mae\": 1.022, \"tau_b\": 0.49, \"mean_pw_auc\": 0.4767}}, \"olmo\": {\"obd_lgbm\": {\"accuracy\": 0.3822, \"mae\": 1.1469, \"tau_b\": 0.4683, \"mean_pw_auc\": 0.6015}, \"multiclass_lgbm\": {\"accuracy\": 0.3685, \"mae\": 1.1813, \"tau_b\": 0.4497, \"mean_pw_auc\": 0.5974}, \"ordinal_logreg\": {\"accuracy\": 0.3265, \"mae\": 1.0352, \"tau_b\": 0.4656, \"mean_pw_auc\": 0.4859}}}}, \"exp_001_pythia_depth\": {\"status\": \"DONE\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9932, \"1v2\": 0.6539, \"2v3\": 0.5515, \"3v4\": 0.5153, \"4v5\": 0.5135}, \"pairwise_auc_std\": {\"0v1\": 0.0007, \"1v2\": 0.0069, \"2v3\": 0.0137, \"3v4\": 0.0084, \"4v5\": 0.0078}, \"pairwise_jsd\": {\"0v1\": 0.2142, \"1v2\": 0.014, \"2v3\": 0.0051, \"3v4\": 0.0033, \"4v5\": 0.0031}, \"k_star\": 2, \"ordinal_mae\": 1.14, \"ordinal_accuracy\": 0.383}}, \"mvp_pilot_sat_v1\": {\"status\": \"DONE\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9956, \"1v2\": 0.6957, \"2v3\": 0.5893, \"3v4\": 0.5434, \"4v5\": 0.5343}, \"pairwise_auc_std\": {\"0v1\": 0.0005, \"1v2\": 0.0072, \"2v3\": 0.012, \"3v4\": 0.0053, \"4v5\": 0.0091}, \"pairwise_jsd\": {\"0v1\": 0.2669, \"1v2\": 0.0163, \"2v3\": 0.0069, \"3v4\": 0.0047, \"4v5\": 0.0041}, \"k_star\": 2, \"ordinal_mae\": 1.0163, \"ordinal_accuracy\": 0.4182}}}, \"count\": 75, \"total\": 75, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2975}}"
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
I have the data I need. Let me extract the exp_14b_c4 data:

From registry:
- exp_id: exp_14b_c4
- K*: 2
- AUC 1v2: 0.621
- Bootstrap CI: [0.6119, 0.6304]
- CI lower: 0.6119 > 0.60 ✅ (+1.19pp)

Now I need to:

1. Add Qwen2.5-14B row to the C1'(a) table. Currently the table has 7 models (mvp-001, exp-001, exp-016, exp-004, exp-002, exp-018, exp-017) + 1 exception (Mistral). 

After adding the 14B model, I'll have 8 models + 1 exception, so 8 out of 9 configurations achieve K*=2.

2. Add a new anticipated concern about C3 arXiv/Pythia filtering negative results. I'm checking exp-025 and exp-026 data—both show filtering strategies producing nearly identical results on their respective datasets, which are negative findings worth documenting.

Now I'm updating the paper_framing.md with these additions.

For the first task, I'm inserting Qwen2.5-14B into the sorted table. Its AUC of 0.621 with a CI of [0.6119, 0.6304] places it between Qwen-1.5B base and Qwen2.5-7B in the ranking.

Now I'm realizing the count needs updating — adding this model brings the total from 7 to 8 configurations, so I need to revise all references from "7/8" to "8/9" throughout the document, including the title and the statement about configurations meeting the CI threshold. I should also double-check whether the mention of "9 model configurations" in the opening paragraph refers to the total across all domains or just this section, since that might need to stay as is. I need to figure out whether "9 model configurations" in the C1' opening refers to the C4 section specifically or the overall count across all domains. The text mentions "1B-14B" range, so I'm checking if Qwen2.5-14B would be a new addition or if 14B was already included in that range. Let me trace through what needs updating: the C1'(a) section from 7/8 to 8/9, the Story Spine reference to "K*=2（C4 7/8 configurations）", and the headline result template that also mentions "7/8 configurations" — all need the same update to 8/9. I see the user wants the table updated from 7/8 to 8/9, with Mistral as the exception that doesn't yield K*=2. I need to update all references to "7/8" in the C1'(a) section and the Story Spine to reflect "8/9" instead, keeping the total at 9 model configurations as stated in the abstract. I'm checking whether the "9 model configurations" reference in the C1' paragraph needs updating. Since the abstract now says "8/9 model configurations" and C4 has 8 K*=2 cases plus 1 Mistral exception totaling 9, the existing "9 model configurations" in C1' describing the experimental setup across architecture families and size ranges should already be consistent with this count. I'm confirming the 14B model was already part of the 9 configurations, so the count is consistent. Now I need to insert the Qwen2.5-14B row into the table sorted by AUC — it slots between the base and 7B variants at 0.621 — and format its confidence interval as [0.6119, 0.6304] with a lower margin of 0.0119.

Looking at how other entries express this margin relative to the 0.60 baseline, I'm seeing a pattern where I calculate the difference and express it in percentage points. For the 14B model, that's 0.6119 - 0.60 = 0.0119, which rounds to +1.2pp to match the existing formatting style.

Now I'm constructing the table row with the AUC value formatted to four decimal places like the rest of the table, and I'm ready to build out the complete updated content. I need to systematically update all references from "7/8 configurations" to "8/9 configurations" throughout the document, add the new Qwen2.5-14B row to the table, and incorporate the reviewer concern about C3 filtering. Let me work through these edits methodically and then save the changes. I'm going through the file content and making several updates to the framing document. I need to change the configuration counts from 7/8 to 8/9 in multiple places, add a 14B model row to the table, and update the corresponding section headers and descriptions to reflect these changes. I'm going through the document systematically to update all the configuration counts from 7/8 to 8/9, add the missing 14B row, and incorporate the new reviewer concern. Rather than making individual edits, I'll reconstruct the full file with all changes applied at once using the save function, which is cleaner given how many scattered updates need to happen throughout the content. I'm updating the configuration counts throughout the document from 7/8 to 8/9 now that I've added the Qwen2.5-14B continuous model to the results table, and I need to make sure this change propagates consistently across all the summary statements, confidence interval descriptions, and result templates.

Now I'm adding reviewer concern #11 before the Venue Fit section to address why graduated filtering doesn't outperform binary on arXiv despite K* supposedly determining filtering granularity—the experiments show both strategies perform nearly identically on arXiv domains, suggesting the filtering advantage is constrained by downstream evaluation sensitivity and training scale rather than being a universal principle. I'm working through how to structure the concerns in the document to match the existing format—using bold quotes followed by "→" and then the response. Since the file is long, I'll use targeted edits rather than reconstructing it manually to avoid corruption. Let me start by reading the file to identify the unique strings I can use for precise replacements. I've found all 7 instances of "7/8" in the file, and they're all referring to C4 configurations, so I can safely do a global replace to change them to "8/9". Let me read the file and execute the replacement. I'm going to use the Edit tool directly for each change since it's more efficient for targeted modifications, then read the final file to confirm everything is saved properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "f77ad992-0ca0-4ca7-b63f-fa960a36e02e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JhFefGU42Ug7UzY9FASQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24575,
      "cache_read_input_tokens": 33858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24575
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

Registry 确认 exp_14b_c4 数据：K*=2, AUC 1v2=0.6210, CI [0.6119, 0.6304]。开始编辑 paper_framing.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "484c84fb-bcc2-461e-b695-75c054c73183",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JhFefGU42Ug7UzY9FASQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24575,
      "cache_read_input_tokens": 33858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24575
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

<details open><summary>🔧 Tool call — Read · `toolu_01WSi6Wnixgo1tF7Bn1oE946`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "180ace0e-3a9a-400e-b9a3-217d29cd653d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011JhFefGU42Ug7UzY9FASQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24575,
      "cache_read_input_tokens": 33858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24575
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

_source line 19 · 2026-05-19T05:10:37.332Z_

<details><summary>↩ Tool result · `toolu_01WSi6Wnixgo1tF7Bn1oE946`</summary>

```text
1	# Paper Framing — gen-depth-contamination
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)
5	- Fallback: EMNLP 2026 Findings
6	- Backup: AAAI 2027 (abstract July 25, paper August 1)
7	
8	## Canonical Experimental Condition
9	
10	**Continuation mode 是 cross-model 结论的基础。**
11	
12	> "We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons."
13	
14	| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |
15	|-----------|-------------|-------------|---------|
16	| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |
17	| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |
18	
19	**原则**：
20	- C1' 的跨模型 claim 必须基于 continuation mode 数据
21	- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据
22	- mvp-001 (Qwen-rewrite) 定位为 "pilot study demonstrating feasibility"，后续用 continuation mode rigorously validate
23	- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集
24	
25	## Core Claims (2+1 结构, updated D049/D050)
26	
27	### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)
28	首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。
29	
30	DPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：
31	
32	- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）
33	- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新
34	- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）
35	- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节
36	- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据
37	- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失
38	- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分
39	
40	**子组件：**
41	
42	**(a) K*=2 as dominant mode for web text (7/8 configurations)**
43	> **7/8 model configurations yield K*=2 on C4 web text：**
44	>
45	> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |
46	> |-------|-----------|---------|--------|-----------------|
47	> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |
48	> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |
49	> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |
50	> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |
51	> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |
52	> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |
53	> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |
54	>
55	> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*
56	>
57	> *Decoding strategy invariance (exp-003):*
58	> | Decoding | AUC 1v2 | K* |
59	> |----------|---------|-----|
60	> | greedy | 0.6893 | 2 |
61	> | nucleus p=0.9 | 0.6866 | 2 |
62	> | temp=0.7 | 0.6887 | 2 |
63	> | temp=1.2 | 0.7039 | 2 |
64	>
65	> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60
66	> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变
67	> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1
68	> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1
69	> - Paper 措辞："K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies."
70	
71	**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**
72	> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)
73	> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)
74	> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)
75	> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)
76	> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)
77	> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）
78	> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 "domain competence prerequisite" 分析放 Appendix
79	> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity
80	> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代
81	> - Sample size: n=2,200 per model
82	> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 "K*=3 with boundary pair AUC of 0.62" 而非 "robustly K*=3"
83	> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链
84	
85	**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**
86	> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1
87	> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）
88	> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**
89	> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash
90	> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素
91	
92	**(d) Cross-model transfer (scorer invariance)**
93	> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact
94	> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移
95	> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model
96	> - Feature ordering: scorer-invariant Spearman ρ > 0.90
97	> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus
98	
99	**(e) Representation dependence of K* (Neural Probe)**
100	> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:
101	>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅
102	>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌
103	>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌
104	> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2
105	> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*
106	> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显
107	> - 论文定位：validates choice of model-free 15D features for headline characterization
108	
109	**(f) Generation mode analysis (§4.x Analysis subsection)**
110	> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）
111	> - Transferability: continuation 80-92% retention vs rewrite 61-63%
112	> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集
113	> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性
114	> - 论文定位：Analysis subsection，不是独立 claim
115	
116	### Secondary: C3 (K*-Aware Data Curation Validation)
117	Domain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.
118	
119	> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim "universally beneficial"。维持 "consistent advantage" 措辞，以 HellaSwag 显著性为主要证据。
120	
121	### Supporting Analysis: Canonical Condition Selection
122	Generation mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。
123	
124	## Story Spine
125	
126	- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。
127	- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**
128	- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者"在什么深度以下，depth-aware curation 比 binary detection 更有价值"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（"one-wash laundering" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。
129	- **Headline result template**: "Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity."
130	
131	## Anticipated Reviewer Concerns & Responses
132	
133	1. **"K*∈{1,2,3} 范围太小，结论是否 trivial？"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。
134	2. **"只基于小模型（≤8B），能推广到更大模型吗？"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。
135	3. **"只是 feature engineering + off-the-shelf classifier，方法贡献弱"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。
136	4. **"arXiv K*=3 样本量够吗？"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。
137	5. **"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 "异常"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。
138	6. **"Prompt-chain 不代表真实世界递归污染"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。
139	7. **"同模型做生成和 surprisal 计算有 bias"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。
140	8. **"为什么不用 learned representations"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。
141	9. **"θ=0.60 选择是否 arbitrary？"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。
142	10. **"Graduated filtering 没和 data selection methods 比"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。
143	
144	## Venue Fit
145	
146	- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作
147	- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度
148	- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 "K*=2 everywhere" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证
149	- One-wash laundering effect 是 memorable concept 便于传播
150	- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "b9d12007-7b4d-4d31-9049-bc8047adbc8c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
      "content": "# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, updated D049/D050)\n\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\n\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\n- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\n\n**子组件：**\n\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\n> **7/8 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"\n\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \"domain competence prerequisite\" 分析放 Appendix\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\n> - Sample size: n=2,200 per model\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \"K*=3 with boundary pair AUC of 0.62\" 而非 \"robustly K*=3\"\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\n\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\n\n**(d) Cross-model transfer (scorer invariance)**\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\n\n**(e) Representation dependence of K* (Neural Probe)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\n> - 论文定位：validates choice of model-free 15D features for headline characterization\n\n**(f) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection，不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\n\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \"universally beneficial\"。维持 \"consistent advantage\" 措辞，以 HellaSwag 显著性为主要证据。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\n- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*∈{1,2,3} 范围太小，结论是否 trivial？\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\n2. **\"只基于小模型（≤8B），能推广到更大模型吗？\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\n3. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\n4. **\"arXiv K*=3 样本量够吗？\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\n5. **\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \"异常\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\n6. **\"Prompt-chain 不代表真实世界递归污染\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\n7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n",
      "numLines": 151,
      "startLine": 1,
      "totalLines": 151
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now I have the file read. Let me make the edits. I'll do them in parallel where possible.

Edits needed:
1. replace_all "7/8" → "8/9" (all 7 occurrences are about C4 configs)
2. Add Qwen2.5-14B row after Qwen-1.5B base cont line
3. Add new reviewer concern #11

Let me also update the θ-sensitivity note line 68: "θ=0.60 下 7/8 K*=2" → "θ=0.60 下 8/9 K*=2"


I'm verifying that the replace_all for "7/8" will catch all instances across the document—I found seven occurrences scattered throughout, from the configuration descriptions to the sensitivity analysis notes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "fad2221f-ef8d-4718-9ba6-48ae77b192c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QE7zZoH594S7kq9FEpLGzc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13771,
      "cache_read_input_tokens": 58433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13771
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

_source line 21_

文件已读取。现在执行三个编辑：(1) 全局替换 7/8→8/9，(2) 插入 14B 行，(3) 添加新 reviewer concern。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "ca0eb885-d0eb-4ba9-840d-abcfbd73b038",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QE7zZoH594S7kq9FEpLGzc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13771,
      "cache_read_input_tokens": 58433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13771
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01Fb7yvvyJY7AsfQCohxkgtV`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
  "old_string": "7/8",
  "new_string": "8/9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "a256c3f1-a1c0-4551-b4f7-a81010868d79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QE7zZoH594S7kq9FEpLGzc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13771,
      "cache_read_input_tokens": 58433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13771
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

_source line 23 · 2026-05-19T05:10:53.628Z_

<details><summary>↩ Tool result · `toolu_01Fb7yvvyJY7AsfQCohxkgtV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "5ea3e466-3341-4fa5-a1f5-d8c4da1f9a29",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
    "oldString": "7/8",
    "newString": "8/9",
    "originalFile": "# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, updated D049/D050)\n\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\n\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\n- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\n\n**子组件：**\n\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\n> **7/8 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"\n\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \"domain competence prerequisite\" 分析放 Appendix\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\n> - Sample size: n=2,200 per model\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \"K*=3 with boundary pair AUC of 0.62\" 而非 \"robustly K*=3\"\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\n\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\n\n**(d) Cross-model transfer (scorer invariance)**\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\n\n**(e) Representation dependence of K* (Neural Probe)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\n> - 论文定位：validates choice of model-free 15D features for headline characterization\n\n**(f) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection，不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\n\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \"universally beneficial\"。维持 \"consistent advantage\" 措辞，以 HellaSwag 显著性为主要证据。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\n- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*∈{1,2,3} 范围太小，结论是否 trivial？\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\n2. **\"只基于小模型（≤8B），能推广到更大模型吗？\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\n3. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\n4. **\"arXiv K*=3 样本量够吗？\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\n5. **\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \"异常\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\n6. **\"Prompt-chain 不代表真实世界递归污染\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\n7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 7,
        "newStart": 30,
        "newLines": 7,
        "lines": [
          " DPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：",
          " ",
          " - **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）",
          "-- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新",
          "+- **Web text K*=2 是 dominant mode**（C4 8/9 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新",
          " - **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）",
          " - **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节",
          " - **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据"
        ]
      },
      {
        "oldStart": 39,
        "oldLines": 8,
        "newStart": 39,
        "newLines": 8,
        "lines": [
          " ",
          " **子组件：**",
          " ",
          "-**(a) K*=2 as dominant mode for web text (7/8 configurations)**",
          "-> **7/8 model configurations yield K*=2 on C4 web text：**",
          "+**(a) K*=2 as dominant mode for web text (8/9 configurations)**",
          "+> **8/9 model configurations yield K*=2 on C4 web text：**",
          " >",
          " > | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |",
          " > |-------|-----------|---------|--------|-----------------|"
        ]
      },
      {
        "oldStart": 62,
        "oldLines": 11,
        "newStart": 62,
        "newLines": 11,
        "lines": [
          " > | temp=0.7 | 0.6887 | 2 |",
          " > | temp=1.2 | 0.7039 | 2 |",
          " >",
          "-> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60",
          "+> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60",
          " > - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变",
          " > - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1",
          "-> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1",
          "-> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"",
          "+> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1",
          "+> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"",
          " ",
          " **(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**",
          " > - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)"
        ]
      },
      {
        "oldStart": 125,
        "oldLines": 8,
        "newStart": 125,
        "newLines": 8,
        "lines": [
          " ",
          " - **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。",
          " - **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**",
          "-- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。",
          "-- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"",
          "+- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（8/9 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。",
          "+- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 8/9 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"",
          " ",
          " ## Anticipated Reviewer Concerns & Responses",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01AE2PfpTXT5DCHME2UQPfcX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
  "old_string": "> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |",
  "new_string": "> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "f4e38326-5761-44d0-ad29-97f98dcb7489",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QE7zZoH594S7kq9FEpLGzc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13771,
      "cache_read_input_tokens": 58433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13771
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

_source line 25 · 2026-05-19T05:10:58.063Z_

<details><summary>↩ Tool result · `toolu_01AE2PfpTXT5DCHME2UQPfcX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "4dc49e4f-39d4-49a3-bfee-11c93eeffae4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
    "oldString": "> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |",
    "newString": "> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |",
    "originalFile": "# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, updated D049/D050)\n\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\n\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\n- **Web text K*=2 是 dominant mode**（C4 8/9 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\n\n**子组件：**\n\n**(a) K*=2 as dominant mode for web text (8/9 configurations)**\n> **8/9 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"\n\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \"domain competence prerequisite\" 分析放 Appendix\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\n> - Sample size: n=2,200 per model\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \"K*=3 with boundary pair AUC of 0.62\" 而非 \"robustly K*=3\"\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\n\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\n\n**(d) Cross-model transfer (scorer invariance)**\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\n\n**(e) Representation dependence of K* (Neural Probe)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\n> - 论文定位：validates choice of model-free 15D features for headline characterization\n\n**(f) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection，不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\n\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \"universally beneficial\"。维持 \"consistent advantage\" 措辞，以 HellaSwag 显著性为主要证据。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（8/9 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\n- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 8/9 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*∈{1,2,3} 范围太小，结论是否 trivial？\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\n2. **\"只基于小模型（≤8B），能推广到更大模型吗？\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\n3. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\n4. **\"arXiv K*=3 样本量够吗？\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\n5. **\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \"异常\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\n6. **\"Prompt-chain 不代表真实世界递归污染\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\n7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n",
    "structuredPatch": [
      {
        "oldStart": 47,
        "oldLines": 6,
        "newStart": 47,
        "newLines": 7,
        "lines": [
          " > | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |",
          " > | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |",
          " > | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |",
          "+> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |",
          " > | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |",
          " > | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |",
          " > | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_01GB6yu4x8NBPbmacdqg1BsE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
  "old_string": "10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n\n## Venue Fit",
  "new_string": "10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n11. **\"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?\"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。\n\n## Venue Fit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "02e92bd4-33c7-42e3-b310-ddd4c55d8238",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QE7zZoH594S7kq9FEpLGzc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13771,
      "cache_read_input_tokens": 58433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13771
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

_source line 27 · 2026-05-19T05:11:08.845Z_

<details><summary>↩ Tool result · `toolu_01GB6yu4x8NBPbmacdqg1BsE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "a91c440a-0920-4c50-8b54-c8cbf4655e64",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
    "oldString": "10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n\n## Venue Fit",
    "newString": "10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n11. **\"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?\"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。\n\n## Venue Fit",
    "originalFile": "# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, updated D049/D050)\n\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\n\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\n- **Web text K*=2 是 dominant mode**（C4 8/9 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\n\n**子组件：**\n\n**(a) K*=2 as dominant mode for web text (8/9 configurations)**\n> **8/9 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"\n\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \"domain competence prerequisite\" 分析放 Appendix\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\n> - Sample size: n=2,200 per model\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \"K*=3 with boundary pair AUC of 0.62\" 而非 \"robustly K*=3\"\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\n\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\n\n**(d) Cross-model transfer (scorer invariance)**\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\n\n**(e) Representation dependence of K* (Neural Probe)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\n> - 论文定位：validates choice of model-free 15D features for headline characterization\n\n**(f) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection，不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\n\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \"universally beneficial\"。维持 \"consistent advantage\" 措辞，以 HellaSwag 显著性为主要证据。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（8/9 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\n- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 8/9 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*∈{1,2,3} 范围太小，结论是否 trivial？\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\n2. **\"只基于小模型（≤8B），能推广到更大模型吗？\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\n3. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\n4. **\"arXiv K*=3 样本量够吗？\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\n5. **\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \"异常\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\n6. **\"Prompt-chain 不代表真实世界递归污染\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\n7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n",
    "structuredPatch": [
      {
        "oldStart": 141,
        "oldLines": 6,
        "newStart": 141,
        "newLines": 7,
        "lines": [
          " 8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。",
          " 9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。",
          " 10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。",
          "+11. **\"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?\"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。",
          " ",
          " ## Venue Fit",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
All three edits succeeded. Let me now read the file to verify the changes, then save via save_project_file for MCP tracking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "9c437545-5074-4e57-8f0d-f9c6f34a787e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1pydDZywZuCWNnUhVx3LT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1862,
      "cache_read_input_tokens": 72204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1862
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

_source line 29_

验证修改结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "937dc524-f08f-44e4-91c8-28b2fddf9ebe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1pydDZywZuCWNnUhVx3LT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1862,
      "cache_read_input_tokens": 72204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1862
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

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_013rqxZywHr1XvpcZeA39kdX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
  "offset": 41,
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
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "e59f2141-3133-4e55-95cb-2f438e13a005",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1pydDZywZuCWNnUhVx3LT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1862,
      "cache_read_input_tokens": 72204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1862
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

_source line 31 · 2026-05-19T05:11:15.065Z_

<details><summary>↩ Tool result · `toolu_013rqxZywHr1XvpcZeA39kdX`</summary>

```text
41	
42	**(a) K*=2 as dominant mode for web text (8/9 configurations)**
43	> **8/9 model configurations yield K*=2 on C4 web text：**
44	>
45	> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |
46	> |-------|-----------|---------|--------|-----------------|
47	> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |
48	> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |
49	> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |
50	> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |
51	> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |
52	> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |
53	> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |
54	> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |
55	>
56	> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*
57	>
58	> *Decoding strategy invariance (exp-003):*
59	> | Decoding | AUC 1v2 | K* |
60	> |----------|---------|-----|
61	> | greedy | 0.6893 | 2 |
62	> | nucleus p=0.9 | 0.6866 | 2 |
63	> | temp=0.7 | 0.6887 | 2 |
64	> | temp=1.2 | 0.7039 | 2 |
65	>
66	> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60
67	> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变
68	> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1
69	> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1
70	> - Paper 措辞："K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "8f646e70-eb3b-4fde-aa0f-33ada64bf9e1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
      "content": "\n**(a) K*=2 as dominant mode for web text (8/9 configurations)**\n> **8/9 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"",
      "numLines": 30,
      "startLine": 41,
      "totalLines": 153
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01ArrNzYSSGTjd1WJg6wcE8T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
  "offset": 140,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "bdcbaa3a-bee0-404b-a3b1-d347ce27ff85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1pydDZywZuCWNnUhVx3LT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1862,
      "cache_read_input_tokens": 72204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1862
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

_source line 33 · 2026-05-19T05:11:15.670Z_

<details><summary>↩ Tool result · `toolu_01ArrNzYSSGTjd1WJg6wcE8T`</summary>

```text
140	7. **"同模型做生成和 surprisal 计算有 bias"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。
141	8. **"为什么不用 learned representations"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。
142	9. **"θ=0.60 选择是否 arbitrary？"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。
143	10. **"Graduated filtering 没和 data selection methods 比"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。
144	11. **"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。
145	
146	## Venue Fit
147	
148	- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作
149	- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度
150	- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 "K*=2 everywhere" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证
151	- One-wash laundering effect 是 memorable concept 便于传播
152	- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）
153	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "2e3cf7f4-e2fe-4f36-9935-5af961f470cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
      "content": "7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n11. **\"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?\"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n",
      "numLines": 14,
      "startLine": 140,
      "totalLines": 153
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
All changes look correct. Now I need to save via save_project_file to ensure MCP tracking. Let me read the full file and pass it to save_project_file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "f37bc5a0-ded0-4907-be59-2c7994d0ec82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqHMua5da8mx3c9gn3oJ7o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 74066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2417
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

_source line 35_

修改验证通过。通过 MCP 保存确保追踪。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "c47834ff-b4b4-4b60-a809-5a96e8bda145",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqHMua5da8mx3c9gn3oJ7o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 74066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2417
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

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_016Dj3o3jhyzjkssS2Q5FsM4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "cd44070d-ee7a-4761-9596-3ca0538f358d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqHMua5da8mx3c9gn3oJ7o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 74066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2417
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

_source line 37 · 2026-05-19T05:11:22.257Z_

<details><summary>↩ Tool result · `toolu_016Dj3o3jhyzjkssS2Q5FsM4`</summary>

```text
1	# Paper Framing — gen-depth-contamination
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)
5	- Fallback: EMNLP 2026 Findings
6	- Backup: AAAI 2027 (abstract July 25, paper August 1)
7	
8	## Canonical Experimental Condition
9	
10	**Continuation mode 是 cross-model 结论的基础。**
11	
12	> "We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons."
13	
14	| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |
15	|-----------|-------------|-------------|---------|
16	| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |
17	| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |
18	
19	**原则**：
20	- C1' 的跨模型 claim 必须基于 continuation mode 数据
21	- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据
22	- mvp-001 (Qwen-rewrite) 定位为 "pilot study demonstrating feasibility"，后续用 continuation mode rigorously validate
23	- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集
24	
25	## Core Claims (2+1 结构, updated D049/D050)
26	
27	### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)
28	首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。
29	
30	DPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：
31	
32	- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）
33	- **Web text K*=2 是 dominant mode**（C4 8/9 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新
34	- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）
35	- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节
36	- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据
37	- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失
38	- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分
39	
40	**子组件：**
41	
42	**(a) K*=2 as dominant mode for web text (8/9 configurations)**
43	> **8/9 model configurations yield K*=2 on C4 web text：**
44	>
45	> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |
46	> |-------|-----------|---------|--------|-----------------|
47	> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |
48	> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |
49	> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |
50	> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |
51	> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |
52	> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |
53	> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |
54	> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |
55	>
56	> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*
57	>
58	> *Decoding strategy invariance (exp-003):*
59	> | Decoding | AUC 1v2 | K* |
60	> |----------|---------|-----|
61	> | greedy | 0.6893 | 2 |
62	> | nucleus p=0.9 | 0.6866 | 2 |
63	> | temp=0.7 | 0.6887 | 2 |
64	> | temp=1.2 | 0.7039 | 2 |
65	>
66	> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60
67	> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变
68	> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1
69	> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1
70	> - Paper 措辞："K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies."
71	
72	**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**
73	> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)
74	> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)
75	> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)
76	> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)
77	> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)
78	> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）
79	> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 "domain competence prerequisite" 分析放 Appendix
80	> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity
81	> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代
82	> - Sample size: n=2,200 per model
83	> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 "K*=3 with boundary pair AUC of 0.62" 而非 "robustly K*=3"
84	> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链
85	
86	**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**
87	> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1
88	> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）
89	> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**
90	> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash
91	> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素
92	
93	**(d) Cross-model transfer (scorer invariance)**
94	> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact
95	> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移
96	> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model
97	> - Feature ordering: scorer-invariant Spearman ρ > 0.90
98	> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus
99	
100	**(e) Representation dependence of K* (Neural Probe)**
101	> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:
102	>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅
103	>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌
104	>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌
105	> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2
106	> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*
107	> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显
108	> - 论文定位：validates choice of model-free 15D features for headline characterization
109	
110	**(f) Generation mode analysis (§4.x Analysis subsection)**
111	> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）
112	> - Transferability: continuation 80-92% retention vs rewrite 61-63%
113	> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集
114	> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性
115	> - 论文定位：Analysis subsection，不是独立 claim
116	
117	### Secondary: C3 (K*-Aware Data Curation Validation)
118	Domain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.
119	
120	> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim "universally beneficial"。维持 "consistent advantage" 措辞，以 HellaSwag 显著性为主要证据。
121	
122	### Supporting Analysis: Canonical Condition Selection
123	Generation mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。
124	
125	## Story Spine
126	
127	- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。
128	- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**
129	- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者"在什么深度以下，depth-aware curation 比 binary detection 更有价值"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（8/9 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（"one-wash laundering" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。
130	- **Headline result template**: "Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 8/9 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity."
131	
132	## Anticipated Reviewer Concerns & Responses
133	
134	1. **"K*∈{1,2,3} 范围太小，结论是否 trivial？"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。
135	2. **"只基于小模型（≤8B），能推广到更大模型吗？"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。
136	3. **"只是 feature engineering + off-the-shelf classifier，方法贡献弱"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。
137	4. **"arXiv K*=3 样本量够吗？"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。
138	5. **"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 "异常"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。
139	6. **"Prompt-chain 不代表真实世界递归污染"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。
140	7. **"同模型做生成和 surprisal 计算有 bias"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。
141	8. **"为什么不用 learned representations"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。
142	9. **"θ=0.60 选择是否 arbitrary？"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。
143	10. **"Graduated filtering 没和 data selection methods 比"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。
144	11. **"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。
145	
146	## Venue Fit
147	
148	- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作
149	- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度
150	- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 "K*=2 everywhere" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证
151	- One-wash laundering effect 是 memorable concept 便于传播
152	- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）
153	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "91183fde-fe8a-4866-8763-e3486d09d4e7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md",
      "content": "# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, updated D049/D050)\n\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\n\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\n- **Web text K*=2 是 dominant mode**（C4 8/9 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\n\n**子组件：**\n\n**(a) K*=2 as dominant mode for web text (8/9 configurations)**\n> **8/9 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"\n\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \"domain competence prerequisite\" 分析放 Appendix\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\n> - Sample size: n=2,200 per model\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \"K*=3 with boundary pair AUC of 0.62\" 而非 \"robustly K*=3\"\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\n\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\n\n**(d) Cross-model transfer (scorer invariance)**\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\n\n**(e) Representation dependence of K* (Neural Probe)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\n> - 论文定位：validates choice of model-free 15D features for headline characterization\n\n**(f) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection，不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\n\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \"universally beneficial\"。维持 \"consistent advantage\" 措辞，以 HellaSwag 显著性为主要证据。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（8/9 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\n- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 8/9 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*∈{1,2,3} 范围太小，结论是否 trivial？\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\n2. **\"只基于小模型（≤8B），能推广到更大模型吗？\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\n3. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\n4. **\"arXiv K*=3 样本量够吗？\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\n5. **\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \"异常\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\n6. **\"Prompt-chain 不代表真实世界递归污染\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\n7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n11. **\"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?\"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n",
      "numLines": 153,
      "startLine": 1,
      "totalLines": 153
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_016dyTiSBN13C1ji7jTcg2v7`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_framing.md",
  "content": "# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, updated D049/D050)\n\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\n\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\n- **Web text K*=2 是 dominant mode**（C4 8/9 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\n\n**子组件：**\n\n**(a) K*=2 as dominant mode for web text (8/9 configurations)**\n> **8/9 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"\n\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \"domain competence prerequisite\" 分析放 Appendix\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\n> - Sample size: n=2,200 per model\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \"K*=3 with boundary pair AUC of 0.62\" 而非 \"robustly K*=3\"\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\n\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\n\n**(d) Cross-model transfer (scorer invariance)**\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\n\n**(e) Representation dependence of K* (Neural Probe)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\n> - 论文定位：validates choice of model-free 15D features for headline characterization\n\n**(f) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection，不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\n\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \"universally beneficial\"。维持 \"consistent advantage\" 措辞，以 HellaSwag 显著性为主要证据。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（8/9 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\n- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 8/9 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*∈{1,2,3} 范围太小，结论是否 trivial？\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\n2. **\"只基于小模型（≤8B），能推广到更大模型吗？\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\n3. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\n4. **\"arXiv K*=3 样本量够吗？\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\n5. **\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \"异常\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\n6. **\"Prompt-chain 不代表真实世界递归污染\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\n7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n11. **\"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?\"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "c2b61d29-ad65-485a-828e-c32b38d5a25b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFGfzu5KRqBiTEF28uZQbR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8115,
      "cache_read_input_tokens": 76483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8115
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

_source line 39 · 2026-05-19T05:14:28.456Z_

<details><summary>↩ Tool result · `toolu_016dyTiSBN13C1ji7jTcg2v7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "fc34b9ef-3567-4fb2-9a40-038a304809b3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 40_

两处修改完成：

1. **C1'(a) 表格**：添加 Qwen2.5-14B cont 行（exp_14b_c4, AUC 1v2=0.6210, CI [0.6119, 0.6304], CI lower > 0.60 ✅ +1.19pp），表格从 7/8 更新为 8/9，全文 8 处 "7/8" 引用同步替换。

2. **Reviewer Concern #11**：添加 C3 arXiv/Pythia filtering negative 的预期质疑与回应，覆盖 exp-026/exp-025 negative 结果、validated scope 限制、三个可能原因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "uuid": "606adacc-3678-4b7b-af55-6ba2a5ba99c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjc93YJ2gehgHQst3YRLea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7803,
      "cache_read_input_tokens": 84598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7803
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

_source line 41_

两处修改完成：

1. **C1'(a) 表格**：添加 Qwen2.5-14B cont 行（exp_14b_c4, AUC 1v2=0.6210, CI [0.6119, 0.6304], CI lower > 0.60 ✅ +1.19pp），表格从 7/8 更新为 8/9，全文 8 处 "7/8" 引用同步替换。

2. **Reviewer Concern #11**：添加 C3 arXiv/Pythia filtering negative 的预期质疑与回应，覆盖 exp-026/exp-025 negative 结果、validated scope 限制、三个可能原因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 374892,
  "duration_api_ms": 375235,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "f7cbde61-8178-4510-b490-adbd20b844fd",
  "total_cost_usd": 1.1531455,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 80560,
    "cache_read_input_tokens": 462241,
    "output_tokens": 16686,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 80560,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 198,
        "cache_read_input_tokens": 84598,
        "cache_creation_input_tokens": 7803,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 7803
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1225,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001315,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 16686,
      "cacheReadInputTokens": 462241,
      "cacheCreationInputTokens": 80560,
      "webSearchRequests": 0,
      "costUSD": 1.1518305,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a4bd1119-a9b8-4d3c-9b24-dcb40b187d69"
}
```

</details>

---
