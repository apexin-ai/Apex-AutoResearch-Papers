# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af9ded52e08159c00.jsonl`
- **Structured JSON:** [`0e249591e67978b85a3c.json`](../../sessions/0e/0e249591e67978b85a3c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

68 recorded events

### User

_source line 1 · 2026-05-19T04:49:18.931Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **novelty, positioning, and related work**.

## Paper Summary
Title: "When Do Self-Extracted Symbolic Constraints Help LLM Reasoning? A Diagnostic Study"

The paper studies SICA (Symbolic Invariant Consensus Aggregation), a pipeline that extracts FOL constraints from LLM reasoning traces and uses weighted MAX-SAT to select answers. Framed as a diagnostic study across 7 models (Qwen-7B/14B/72B, Mistral-7B, LLaMA-3.1-8B, DeepSeek-R1-7B, QwQ-32B) and 6 reasoning domains (FOLIO, ProofWriter, LogiQA, StrategyQA, ARC-Challenge, GSM8K).

**Key claims/contributions:**
1. **Oracle gap localization**: Gold FOL + MAX-SAT yields +14.2pp over SC (p<10^-6). Self-extracted constraints capture only ~2% (not 35%) of this potential (+0.25pp vs +14.22pp on the oracle condition).
2. **Systematic failure characterization**: Three failure regimes identified. SICA yields zero/negative gains in 9/12 conditions. Single positive (Mistral-7B FOLIO, +4.9pp) doesn't generalize across seeds.
3. **Remediation breadth**: 9 targeted interventions all fail (multi-temp is partial exception: +2.45pp n.s.).
4. **Deployment diagnostic**: C0 < 5% → SICA ≡ SC (necessary condition only, not sufficient for positive prediction).

**Additional findings:**
- Eff-K (effective sample size from Fleiss' κ): ranges 1.2-3.6 for nominal K=12. Useful cross-model descriptor but 50% joint prediction accuracy (= chance).
- Aggregation mechanism ablation: MAX-SAT ≈ count-only (agree 803/804 problems). Symbolic optimization adds negligible value.
- 78% of constraints mirror model's majority-vote answer (confirmation bias).
- Constraint quality analysis: 45% trivially satisfied, only 1/8 genuinely informative.
- Temperature sensitivity: positive Δ at T=0.3-0.7, collapse at T=1.0. Non-monotonic, no clean functional form.

## Related Work (from the paper)
The paper organizes related work into 4 categories:
1. **Self-Consistency and Extensions**: Wang et al. 2023, universal SC (Chen et al. 2023), diversity-aware sampling (Li et al. 2023), weighted voting (Taubenfeld et al. 2025), scaling analysis (Loo et al. 2025).
2. **Neuro-Symbolic Reasoning**: Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), DyLoS (2026), Aristotle (2025), FoVer (2025). Paper differentiates by studying "self-extraction without trained extractors or external verifiers."
3. **Condorcet Jury Theorem and LLM Ensembles**: Li et al. 2024 (cross-model sentiment), paper applies CJT within-model.
4. **Test-Time Compute and Verification**: Snell et al. 2025, Lightman et al. 2023 (process reward models), Cobbe et al. 2021 (outcome reward models), DeepSeek-R1.

References list includes ~25 entries. Notable: some entries appear incomplete (DyLoS, Aristotle, FoVer, SATBench, LLM-CP listed without full author names). Cobbe et al. 2021 appears duplicated.

## Key Context from Review Design File
- The paper originally aimed to validate a Condorcet-based predictive framework but the data doesn't support it. The framework has been demoted to descriptive.
- The paper sits in an "awkward middle ground": not positive enough for a method paper, not negative enough for a clean diagnostic paper.
- Temperature results (T=0.3-0.7 all positive) undermine a "fragile narrow window" narrative.
- Multi-temp positive result (+2.45pp) undermines "all 9 remediations fail" claim.
- The MAX-SAT ≈ count-only result hollows out the "symbolic" framework's core value.

## Your Task
Provide a detailed review focusing on:
1. **Novelty assessment**: What is genuinely new here? Is a diagnostic study of a largely-failing method publishable at a top venue? How does this compare to existing negative-results papers?
2. **Related work positioning**: Is the paper well-positioned against prior work? Are there missing references? Is the differentiation from Logic-LM, LINC, DyLoS clear and honest?
3. **Contribution significance**: Are the four stated contributions substantial enough? Does the oracle gap alone justify a paper? Does the C0+SC diagnostic have practical value?
4. **Narrative coherence**: Does the story hold together? Is the framing as "diagnostic study" compelling or does it feel like a failed method paper repackaged?
5. **Reference quality**: Any issues with completeness, formatting, potential fabricated references?

Output format:
```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
[Bulleted list, each with brief explanation]

### Weaknesses
[Bulleted list, each with brief explanation, labeled W1, W2, etc.]

### Questions for Authors
[Numbered list]

### Minor Issues
[Bulleted list]

### Preliminary Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "eab80d62-c091-43db-a172-5f454a24dabd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T04:49:18.934Z_

```json
{
  "parentUuid": "eab80d62-c091-43db-a172-5f454a24dabd",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "faf198eb-48e0-4687-b688-2876e7ff5e1f",
  "timestamp": "2026-05-19T04:49:18.934Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-19T04:49:21.298Z_



I'll start by thoroughly reading the paper and all relevant project files to give a well-grounded review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faf198eb-48e0-4687-b688-2876e7ff5e1f",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKk7tohfP3b4G4XNTKo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2eb1c882-52d8-45d1-a036-441a78cf9747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiHQbvnNhcmQLiymmkohkP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8807,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8807,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-19T04:49:22.739Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LzHZsV5JNZ8AqaVt7W2Q9n`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eb1c882-52d8-45d1-a036-441a78cf9747",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKk7tohfP3b4G4XNTKo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8dee570-b0eb-410b-857b-9f4f9961b59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiHQbvnNhcmQLiymmkohkP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8807,
      "cache_read_input_tokens": 8251,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8807
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 128,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 8807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8807,
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

_source line 5 · 2026-05-19T04:49:22.741Z_

<details><summary>↩ Tool result · `toolu_01LzHZsV5JNZ8AqaVt7W2Q9n`</summary>

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
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8dee570-b0eb-410b-857b-9f4f9961b59b",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "ec8b1ab4-18d7-4807-8d7c-a5e1ae7ab026",
  "sourceToolAssistantUUID": "d8dee570-b0eb-410b-857b-9f4f9961b59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-19T04:49:24.905Z_



Let me read the paper and all relevant project files to ground my review thoroughly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec8b1ab4-18d7-4807-8d7c-a5e1ae7ab026",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKkQTDEXRAi6jy5CJbD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d505659-6df4-4383-b7e3-e8aef2f63a07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C56SWsgPfnbPC73yqTxdZU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 17058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-19T04:49:25.983Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_018KC78QizjgSk9Sugx3S24A`</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d505659-6df4-4383-b7e3-e8aef2f63a07",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKkQTDEXRAi6jy5CJbD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b81c64e9-61f3-4dee-a259-ea18fec529be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C56SWsgPfnbPC73yqTxdZU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 17058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T04:49:26.225Z_

<details><summary>↩ Tool result · `toolu_018KC78QizjgSk9Sugx3S24A`</summary>

```text
{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (85 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-048-llama8b-pw600 | LLaMA-3.1-8B-Instruct 在 ProofWriter-600 上 SICA vs SC。FOLIO-204 上 LLaMA-8B SC=63.2% delta=-2.45pp (exp-020)。PW 是更结构化的形式推理数据集，测试 SICA 在 PW 上对低能力模型是否有效（补充 regime boundary 跨域证据）。parent=exp-020 | — | — | — |\n| exp-040-qwen3-pw600-16639 | Qwen3-14B non-thinking 在 ProofWriter-600 全量上 SICA vs SC：跨模型代际验证 capability trap 在 PW 数据集上是否持续。与 exp-039 (Qwen2.5-14B PW-600) 对比代际差异。 | — | — | — |\n| exp-039-14b-pw600-16639 | Qwen2.5-14B-Instruct 在 ProofWriter-600 全量上 SICA vs SC（westd-16639 重跑）：验证 capability trap 在 PW 数据集全量规模上是否持续。复现 sica_expanded_14b 的 PW 子集结果（delta=+0.3pp）。 | — | — | — |\n\n## 待处理\n- exp-053-mistral-folio204-seed456: exp-033 replication (seed=456): Mistral-7B FOLIO-204 K=12 T=0.7，第二组独立 replication。与 exp-052 (seed=123) 一起验证 exp-033 结论 robustness。parent=exp-033（排队等待 GPU）\n- exp-052-mistral-folio204-seed123: exp-033 replication (seed=123): Mistral-7B FOLIO-204 K=12 T=0.7，与 exp-033 (seed=42, delta=+4.90pp, p=0.013) 完全相同配置，仅 seed 不同。验证正向结果是否 seed-robust。parent=exp-033（排队等待 GPU）\n- smoke-test-5q（准备中）\n\n## 近期结论\n- **exp-058-mistral-folio204-t05** (negative): T=0.5 delta 介于 T=0.3 和 T=0.7 之间，形成温度-SICA delta 曲线。与 exp-033 (T=0.7, +4.90pp) 和 exp-054 (T=1.0, +0.49pp) 共同构成 4 点 T sensitivity ablation。parent=exp-033, D060 analysis paper ← 基于 exp-033\n- **exp-051-mistral-k-sensitivity** (success): Mistral-7B K sensitivity on FOLIO-204: K=[4,8,16,20]（K=12 已有 exp-033 delta=+4.90pp）。验证正向结果对 K 选择是否稳健。Reviewer 必问 ablation。parent=exp-033\n- **exp-057-mistral-folio204-t03** (failed): T=0.3 低温 traces 更确定性更一致，SICA delta < T=0.7 的 +4.90pp。与 exp-054 (T=1.0, +0.49pp) 共同形成 T sensitivity ablation curve。parent=exp-033, D060 analysis paper ← 基于 exp-033\n\n## 趋势\n成功 21 / 负向 30 / 失败 18 / 共 78\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16639: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nwestd-25068: 无 GPU 信息\n\n## 告警\n- mvp_math50_t07: 已被终止 — unknown\n- sica_aime30_t07: 已被终止 — unknown\n- sica_aime30_v2: 已被终止 — unknown\n- sica_aime30_v3: 已被终止 — unknown\n- sica_proofwriter30: 训练失败 — unknown\n- sica_folio30: 已被终止 — unknown\n- sica_proofwriter30_v2: 已被终止 — unknown\n- exp-011-llama8b: 训练失败 — unknown\n- exp-010-mistral: 训练失败 — unknown\n- exp-011-llama8b-v2: 训练失败 — unknown\n- exp-017-strategyqa: 训练失败 — unknown\n- exp-018-arc: 训练失败 — unknown\n- exp-010-mistral-v2: 训练失败 — unknown\n- exp-017-strategyqa-v2: 训练失败 — unknown\n- pilot-contrastive-prompt: 训练失败 — unknown\n- exp-028-qwen3-14b-thinking: 已被终止 — unknown\n- exp-033-qwen3-pw600-nonthinking: 训练失败 — unknown\n- exp-007-qwen72b-awq: 训练失败 — unknown\n- exp-004-qwen7b-rerun: 训练失败 — unknown\n- exp-042-premise-formalization: 训练失败 — unknown\n- exp-044-icl-oracle: 训练失败 — unknown\n- exp-042b-premise-formal: 训练失败 — unknown\n- exp-045b-backward-verify: 已被终止 — unknown\n- exp-028b-qwen3-thinking-folio204: 已被终止 — unknown\n- exp-049-mistral-logiqa200: 训练失败 — unknown\n- exp-050-mistral-icl-oracle-folio199: 训练失败 — unknown\n- exp-057-mistr"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b81c64e9-61f3-4dee-a259-ea18fec529be",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "38926d98-24dc-4df7-b963-caa44be78d3c",
  "sourceToolAssistantUUID": "b81c64e9-61f3-4dee-a259-ea18fec529be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T04:49:26.762Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016bUSPFeyWTKYMwQSiKW7Js`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38926d98-24dc-4df7-b963-caa44be78d3c",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKkQTDEXRAi6jy5CJbD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e80a293c-a85e-4447-91dc-2b28c321b3e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C56SWsgPfnbPC73yqTxdZU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 17058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T04:49:26.772Z_

<details><summary>↩ Tool result · `toolu_016bUSPFeyWTKYMwQSiKW7Js`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml\", \"content\": \"# Literature Map — symb_invariant_consensus (SICA)\\n# Last updated: 2026-05-16\\n# Purpose: Track related work coverage for EMNLP 2026 submission\\n\\ndimensions:\\n\\n  self_consistency_and_variants:\\n    description: \\\"Self-Consistency (SC) decoding and improvements\\\"\\n    papers:\\n      - id: wang2023sc\\n        title: \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\"\\n        authors: \\\"Wang et al.\\\"\\n        venue: \\\"ICLR 2023\\\"\\n        arxiv: \\\"2203.11171\\\"\\n        relevance: \\\"Foundational SC method; our primary baseline\\\"\\n        status: must_cite\\n\\n      - id: chen2024usc\\n        title: \\\"Universal Self-Consistency for Large Language Model Generation\\\"\\n        authors: \\\"Chen et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2311.17311\\\"\\n        relevance: \\\"Extends SC to free-form answers via LLM-based selection; alternative aggregation\\\"\\n        status: must_cite\\n\\n      - id: taubenfeld2025cisc\\n        title: \\\"Confidence Improves Self-Consistency in LLMs\\\"\\n        authors: \\\"Taubenfeld et al.\\\"\\n        venue: \\\"ACL Findings 2025\\\"\\n        arxiv: \\\"2502.06233\\\"\\n        relevance: \\\"Weighted voting via model confidence; reduces samples 40-50%. Shows SC can be improved with non-uniform weighting — SICA uses constraint-based weighting instead\\\"\\n        status: must_cite\\n\\n      - id: kim2026reasc\\n        title: \\\"Reliability-Aware Adaptive Self-Consistency (ReASC)\\\"\\n        authors: \\\"Kim et al.\\\"\\n        venue: \\\"2026\\\"\\n        relevance: \\\"Response-level confidence for early halting; 70-80% cost saving vs naive SC\\\"\\n        status: should_cite\\n\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — shows SC gains plateau early and can decline at high sample counts for strong models. Directly supports our QwQ-32B finding (SICA≡SC when model is too consistent)\\\"\\n        status: must_cite\\n\\n      - id: wan2024rasc\\n        title: \\\"Reasoning-Aware Self-Consistency (RASC)\\\"\\n        authors: \\\"Wan et al.\\\"\\n        venue: \\\"2024\\\"\\n        relevance: \\\"Combines answer-level and rationale-level features; reduces samples ~88%\\\"\\n        status: should_cite\\n\\n      - id: li2023diverse\\n        title: \\\"Making Language Models Better Reasoners with Step-Aware Verifier\\\"\\n        authors: \\\"Li et al.\\\"\\n        venue: \\\"ACL 2023\\\"\\n        arxiv: \\\"2206.02336\\\"\\n        relevance: \\\"DiVeRSe: diverse prompts + step-aware verification for SC improvement. Combines diversity generation with trained verifier — shows diversity alone insufficient without verification quality.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: dsc2025\\n        title: \\\"Difficulty-Adaptive Self-Consistency\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL Findings 2025\\\"\\n        relevance: \\\"Ranks problem difficulty to allocate sampling budget; complementary efficiency approach\\\"\\n        status: optional\\n\\n  symbolic_reasoning_llm:\\n    description: \\\"Neuro-symbolic methods combining LLMs with formal solvers\\\"\\n    papers:\\n      - id: olausson2023linc\\n        title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n        authors: \\\"Olausson et al.\\\"\\n        venue: \\\"EMNLP 2023\\\"\\n        arxiv: \\\"2310.15164\\\"\\n        relevance: \\\"LLM translates NL to FOL, external prover verifies; same-model translation pipeline like Logic-LM. Documents translation error rates (~40% on FOLIO). Key reference for self-extraction quality issues.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: pan2023logiclm\\n        title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n        authors: \\\"Pan et al.\\\"\\n        venue: \\\"EMNLP Findings 2023\\\"\\n        arxiv: \\\"2305.12295\\\"\\n        relevance: \\\"LLM→FOL→solver pipeline; closest architectural ancestor to SICA. Key difference: Logic-LM uses single-path translation, SICA aggregates across multiple paths\\\"\\n        status: must_cite\\n\\n      - id: xu2026dylos\\n        title: \\\"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)\\\"\\n        authors: \\\"Xu et al.\\\"\\n        venue: \\\"EACL 2026\\\"\\n        arxiv: \\\"2510.06774\\\"\\n        relevance: \\\"Multi-paradigm solver selection (LP/FOL/CSP/SMT); evaluated on FOLIO+ProofWriter. Outperforms Logic-LM. Key difference: DyLoS selects solver type, SICA aggregates constraints across paths\\\"\\n        status: must_cite\\n\\n      - id: fover2025\\n        title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"TACL 2025\\\"\\n        relevance: \\\"FOL verification for NL reasoning; strong results on ProofWriter+FOLIO. Uses verification rather than aggregation\\\"\\n        status: must_cite\\n\\n      - id: li2025survey\\n        title: \\\"A Survey on LLM Symbolic Reasoning\\\"\\n        authors: \\\"Li et al.\\\"\\n        venue: \\\"2025 (under review)\\\"\\n        relevance: \\\"Comprehensive survey; positions SICA within the broader landscape\\\"\\n        status: should_cite\\n\\n      - id: constraintllm2025\\n        title: \\\"ConstraintLLM: A Neuro-Symbolic Framework for Industrial Constraint Programming\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Multi-instruction SFT for constraint extraction; different domain (industrial) but related extraction methodology\\\"\\n        status: optional\\n\\n  maxsat_constraint_nlp:\\n    description: \\\"MAX-SAT and constraint satisfaction applied to NLP/reasoning\\\"\\n    papers:\\n      - id: demoura2008z3\\n        title: \\\"Z3: An Efficient SMT Solver\\\"\\n        authors: \\\"de Moura and Bjorner\\\"\\n        venue: \\\"TACAS 2008\\\"\\n        relevance: \\\"Z3 SMT solver; our core constraint satisfaction engine for weighted partial MAX-SAT evaluation.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: llm_meets_cp2025\\n        title: \\\"Large Language Model Meets Constraint Propagation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"IJCAI 2025\\\"\\n        relevance: \\\"LLM+constraint propagation integration; validates feasibility of constraint-based reasoning with LLMs\\\"\\n        status: should_cite\\n\\n      - id: satbench2025\\n        title: \\\"SATBench: Benchmarking LLMs' Logical Reasoning via SAT Problems\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Evaluates LLMs on SAT-formulated problems; establishes that LLMs struggle with pure SAT but can benefit from solver integration\\\"\\n        status: should_cite\\n\\n      - id: maxsat_local_search2025\\n        title: \\\"Optimizing Local Search-based Partial MaxSAT Solving via Initial Assignment Prediction\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Science China Information Sciences 2025\\\"\\n        relevance: \\\"Solver-side advances in partial MaxSAT; technical reference for our WPMS formulation\\\"\\n        status: optional\\n\\n  folio_proofwriter_sota:\\n    description: \\\"State-of-the-art methods on FOLIO and ProofWriter benchmarks\\\"\\n    papers:\\n      - id: logicagent2025\\n        title: \\\"From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2509.24765\\\"\\n        relevance: \\\"Multi-perspective logical reasoning; SOTA on logical reasoning benchmarks including FOLIO. +7.05% average gain\\\"\\n        status: must_cite\\n\\n      - id: aristotle2025\\n        title: \\\"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"ACL 2025\\\"\\n        relevance: \\\"Logic-complete decomposition framework; strong ProofWriter/FOLIO results\\\"\\n        status: must_cite\\n\\n      - id: qi2025symbolic_provers\\n        title: \\\"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation\\\"\\n        authors: \\\"Qi et al.\\\"\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv: \\\"2502.06563\\\"\\n        relevance: \\\"LLM+symbolic prover combination; evaluated on FOLIO\\\"\\n        status: should_cite\\n\\n      - id: dissecting2025\\n        title: \\\"Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP Findings 2025\\\"\\n        arxiv: \\\"2506.04810\\\"\\n        relevance: \\\"Fine-grained analysis of LLM logical reasoning capabilities on ProofWriter/FOLIO\\\"\\n        status: optional\\n\\n  reasoning_model_diversity:\\n    description: \\\"Trace diversity in reasoning vs non-reasoning models; supports our QwQ-32B finding\\\"\\n    papers:\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — strong models produce near-identical paths, SC gains plateau/decline. Direct support for SICA≡SC on QwQ-32B\\\"\\n        status: must_cite\\n\\n      - id: diversity_aware_tts2025\\n        title: \\\"Diversity-Aware Training for Test-Time Scaling\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Under review 2025\\\"\\n        relevance: \\\"Independent reasoning attempts collapse into similar solutions; diversity training needed to unlock test-time scaling. Supports our claim that non-reasoning models have more useful diversity\\\"\\n        status: must_cite\\n\\n      - id: snell2025scaling_tts\\n        title: \\\"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters\\\"\\n        authors: \\\"Snell et al.\\\"\\n        venue: \\\"ICLR 2025 (Oral)\\\"\\n        arxiv: \\\"2408.03314\\\"\\n        relevance: \\\"Foundational test-time compute scaling; shows compute-optimal strategies vary by difficulty. Contextualizes why SICA needs diverse paths\\\"\\n        status: should_cite\\n\\n      - id: deepseek_r1_2025\\n        title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n        authors: \\\"DeepSeek-AI\\\"\\n        venue: \\\"Nature 2025\\\"\\n        arxiv: \\\"2501.12948\\\"\\n        relevance: \\\"Defines the reasoning model paradigm (RL-trained extended thinking); reference for why these models are highly self-consistent\\\"\\n        status: must_cite\\n\\n      - id: base_models_reason2025\\n        title: \\\"Base Models Know How to Reason, Thinking Models Learn When\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.07364\\\"\\n        relevance: \\\"RL teaches activation timing not new skills; implies reasoning models converge to similar reasoning patterns, reducing trace diversity\\\"\\n        status: should_cite\\n\\n      - id: korikov2025sc_ranking\\n        title: \\\"The Impact of LLM Self-Consistency and Reasoning Effort on Automated Scoring\\\"\\n        authors: \\\"Korikov et al.\\\"\\n        venue: \\\"arXiv 2026\\\"\\n        arxiv: \\\"2604.26954\\\"\\n        relevance: \\\"Temperature sampling helps but ensemble size (1→7) produces no significant gains; supports diminishing returns of naive SC\\\"\\n        status: optional\\n\\n  multi_path_aggregation:\\n    description: \\\"Methods for aggregating multiple reasoning paths beyond majority voting\\\"\\n    papers:\\n      - id: rc2025\\n        title: \\\"Representation Consistency for Accurate and Coherent LLM Answer Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2506.21590\\\"\\n        relevance: \\\"Aggregation via representation similarity; down-weights incoherent reasoning. Semantic alternative to SICA's symbolic approach\\\"\\n        status: should_cite\\n\\n      - id: multi_path_plan2025\\n        title: \\\"Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.11620\\\"\\n        relevance: \\\"Multi-path aggregation at plan level rather than answer level\\\"\\n        status: optional\\n\\n      - id: crest2025\\n        title: \\\"Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL 2025\\\"\\n        relevance: \\\"Consistency as training signal rather than inference-time aggregation\\\"\\n        status: optional\\n\\n  verification_reranking:\\n    description: \\\"Verification and reranking methods for LLM outputs (ORM, PRM)\\\"\\n    papers:\\n      - id: cobbe2021gsm8k\\n        title: \\\"Training Verifiers to Solve Math Word Problems\\\"\\n        authors: \\\"Cobbe et al.\\\"\\n        venue: \\\"arXiv 2021\\\"\\n        arxiv: \\\"2110.14168\\\"\\n        relevance: \\\"Defines ORM (Outcome Reward Model) paradigm; trained verifier selects among candidate solutions. Alternative to symbolic constraint aggregation.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: lightman2023prm\\n        title: \\\"Let's Verify Step by Step\\\"\\n        authors: \\\"Lightman et al.\\\"\\n        venue: \\\"ICLR 2024\\\"\\n        arxiv: \\\"2305.20050\\\"\\n        relevance: \\\"Process Reward Models (PRM) verify each reasoning step. Shows step-level verification outperforms outcome-level. Trained verifier approach contrasts with SICA's self-extraction.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: wang2024mathshepherd\\n        title: \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\"\\n        authors: \\\"Wang et al.\\\"\\n        venue: \\\"ACL 2024\\\"\\n        arxiv: \\\"2312.08935\\\"\\n        relevance: \\\"Automatic process reward model training without human labels. Achieves strong verification without manual annotation.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: hosseini2024vstar\\n        title: \\\"V-STaR: Training Verifiers for Self-Taught Reasoners\\\"\\n        authors: \\\"Hosseini et al.\\\"\\n        venue: \\\"NeurIPS 2024\\\"\\n        arxiv: \\\"2402.06457\\\"\\n        relevance: \\\"Iteratively trains verifier alongside generator; verification quality scales with data.\\\"\\n        status: should_cite\\n\\n  debate_multi_agent:\\n    description: \\\"Debate and multi-agent aggregation methods for LLM reasoning\\\"\\n    papers:\\n      - id: liang2023encouraging\\n        title: \\\"Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate\\\"\\n        authors: \\\"Liang et al.\\\"\\n        venue: \\\"arXiv 2023\\\"\\n        arxiv: \\\"2305.19118\\\"\\n        relevance: \\\"Multi-agent debate improves factuality and reasoning via iterative refinement. Alternative multi-path aggregation mechanism.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: du2023improving\\n        title: \\\"Improving Factuality and Reasoning in Language Models through Multiagent Debate\\\"\\n        authors: \\\"Du et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2305.14325\\\"\\n        relevance: \\\"Multi-agent debate for reasoning; shows consensus-seeking improves accuracy. Contrast: debate uses natural language, SICA uses formal constraints.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: khan2024debating\\n        title: \\\"Debating with More Persuasive LLMs Leads to More Truthful Answers\\\"\\n        authors: \\\"Khan et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2402.06782\\\"\\n        relevance: \\\"Debate quality depends on model capability; stronger debaters improve consensus.\\\"\\n        status: should_cite\\n\\n  benchmarks_and_datasets:\\n    description: \\\"Benchmark datasets used in our evaluation\\\"\\n    papers:\\n      - id: han2022folio\\n        title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n        authors: \\\"Han et al.\\\"\\n        venue: \\\"arXiv 2022\\\"\\n        arxiv: \\\"2209.00840\\\"\\n        relevance: \\\"FOLIO benchmark with expert-annotated FOL; our primary formal logic evaluation dataset (n=204).\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: tafjord2021proofwriter\\n        title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n        authors: \\\"Tafjord et al.\\\"\\n        venue: \\\"ACL Findings 2021\\\"\\n        arxiv: \\\"2012.13048\\\"\\n        relevance: \\\"ProofWriter dataset for deductive reasoning; our primary large-N evaluation (n=600).\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: geva2021strategyqa\\n        title: \\\"Did Aristotle Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies\\\"\\n        authors: \\\"Geva et al.\\\"\\n        venue: \\\"TACL 2021\\\"\\n        arxiv: \\\"2101.02235\\\"\\n        relevance: \\\"StrategyQA benchmark for commonsense multi-hop reasoning (Yes/No); our cross-domain validation (n=200).\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: liu2020logiqa\\n        title: \\\"LogiQA: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning\\\"\\n        authors: \\\"Liu et al.\\\"\\n        venue: \\\"IJCAI 2020\\\"\\n        arxiv: \\\"2007.08124\\\"\\n        relevance: \\\"LogiQA benchmark for logical reasoning in reading comprehension; our cross-domain validation for Type B (non-formalizable) analysis (n=200).\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: clark2018arc\\n        title: \\\"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\\\"\\n        authors: \\\"Clark et al.\\\"\\n        venue: \\\"arXiv 2018\\\"\\n        arxiv: \\\"1803.05457\\\"\\n        relevance: \\\"ARC-Challenge science QA benchmark; our cross-domain validation for multiple-choice (n=60).\\\"\\n        status: must_cite\\n        verified: true\\n\\n  negative_results_analysis:\\n    description: \\\"Precedents for negative-result and analysis papers in NLP\\\"\\n    papers:\\n      - id: huang2024selfcorrect\\n        title: \\\"Large Language Models Cannot Self-Correct Reasoning Yet\\\"\\n        authors: \\\"Huang et al.\\\"\\n        venue: \\\"ICLR 2024\\\"\\n        arxiv: \\\"2310.01798\\\"\\n        relevance: \\\"Key precedent: shows LLM self-correction fails without external feedback. Structural parallel to our finding (self-extraction fails without external verification). Same 'self-X fails' narrative.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: mirzadeh2024gsmsymbolic\\n        title: \\\"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\\\"\\n        authors: \\\"Mirzadeh et al.\\\"\\n        venue: \\\"arXiv 2024\\\"\\n        arxiv: \\\"2410.05229\\\"\\n        relevance: \\\"Systematic negative result: apparent LLM reasoning gains are fragile under symbolic perturbation. Establishes precedent for rigorous negative-result methodology in LLM reasoning.\\\"\\n        status: should_cite\\n        verified: true\\n\\n  oracle_upper_bound_experiments:\\n    description: \\\"Papers using oracle/gold-data substitution to diagnose pipeline bottlenecks\\\"\\n    papers:\\n      - id: press2023compositionality\\n        title: \\\"Measuring and Narrowing the Compositionality Gap in Language Models\\\"\\n        authors: \\\"Press et al.\\\"\\n        venue: \\\"EMNLP Findings 2023\\\"\\n        arxiv: \\\"2210.03350\\\"\\n        relevance: \\\"Measures compositionality gap: fraction of cases where model answers sub-questions correctly (oracle decomposition) but fails at composition. Diagnoses compositional reasoning, not knowledge, as bottleneck. Direct methodological parallel to our oracle FOL experiment.\\\"\\n        status: should_cite\\n        verified: true\\n\\n      - id: trivedi2023ircot\\n        title: \\\"Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions\\\"\\n        authors: \\\"Trivedi et al.\\\"\\n        venue: \\\"ACL 2023\\\"\\n        arxiv: \\\"2212.10509\\\"\\n        relevance: \\\"Uses gold supporting paragraphs as oracle retrieval upper bound to diagnose that retrieval quality is the primary bottleneck in multi-step QA. Same diagnostic design as our oracle experiment: replace one pipeline component with gold data to isolate the bottleneck.\\\"\\n        status: should_cite\\n        verified: true\\n\\n      - id: saparov2023greedy\\n        title: \\\"Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought\\\"\\n        authors: \\\"Saparov and He\\\"\\n        venue: \\\"ICLR 2023\\\"\\n        arxiv: \\\"2210.01240\\\"\\n        relevance: \\\"Uses synthetic data with gold FOL proofs to formally analyze where CoT reasoning fails. Isolates proof planning (not individual deduction) as bottleneck. Closest methodological parallel: uses formal logic ground truth to diagnose LLM reasoning limitations.\\\"\\n        status: should_cite\\n        verified: true\\n\\n  condorcet_voting_theory:\\n    description: \\\"Condorcet Jury Theorem, voting theory, and ensemble independence\\\"\\n    papers:\\n      - id: condorcet1785\\n        title: \\\"Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix\\\"\\n        authors: \\\"Marquis de Condorcet\\\"\\n        venue: \\\"Paris: Imprimerie Royale, 1785\\\"\\n        relevance: \\\"The original Jury Theorem: majority voting among independent voters each with p>0.5 converges to correct answer as group size grows. Foundation for our theoretical framing of SC as majority voting over reasoning traces\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: austensmith1996\\n        title: \\\"Information Aggregation, Rationality, and the Condorcet Jury Theorem\\\"\\n        authors: \\\"Austen-Smith, David and Banks, Jeffrey S.\\\"\\n        venue: \\\"American Political Science Review, 90(1), 34-45, 1996\\\"\\n        relevance: \\\"Key modern formalization of CJT; explicitly introduces the independence requirement and shows sincere voting is not always rational. Provides the formal basis for why trace independence matters in SC aggregation\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: lefort2024condorcet_llm\\n        title: \\\"Examining Independence in Ensemble Sentiment Analysis: A Study on the Limits of Large Language Models Using the Condorcet Jury Theorem\\\"\\n        authors: \\\"Lefort, Baptiste and Benhamou, Eric and Ohana, Jean-Jacques and Guez, Beatrice and Saltiel, David and Jacquot, Thomas\\\"\\n        venue: \\\"arXiv 2024\\\"\\n        arxiv: \\\"2409.00094\\\"\\n        relevance: \\\"CLOSEST PRIOR WORK applying CJT to LLM aggregation. Tests cross-model ensembles via majority voting for sentiment analysis; finds marginal gains due to lack of independence among advanced LLMs. Key difference from SICA: they study cross-model ensembles, we study within-model trace independence and propose Fleiss kappa + Effective-K to quantify it\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: ladha1992correlated\\n        title: \\\"The Condorcet Jury Theorem, Free Speech, and Correlated Votes\\\"\\n        authors: \\\"Ladha, Krishna K.\\\"\\n        venue: \\\"American Journal of Political Science, 36(3), 617-634, 1992\\\"\\n        relevance: \\\"Generalizes CJT to correlated voters; shows majority-rule effectiveness decreases as vote correlation increases. Directly supports our Effective-K concept: correlated traces reduce the effective number of independent voters below nominal K\\\"\\n        status: should_cite\\n        verified: true\\n\\n      - id: fleiss1971kappa\\n        title: \\\"Measuring Nominal Scale Agreement among Many Raters\\\"\\n        authors: \\\"Fleiss, Joseph L.\\\"\\n        venue: \\\"Psychological Bulletin, 76(5), 378-382, 1971\\\"\\n        relevance: \\\"Defines Fleiss kappa for multi-rater agreement on nominal categories. Our framework uses Fleiss kappa to quantify inter-trace agreement as a proxy for trace independence in SC sampling\\\"\\n        status: should_cite\\n        verified: true\\n\\ngaps:\\n  resolved:\\n    - dimension: \\\"verification_reranking\\\"\\n      gap: \\\"Added ORM, PRM, Math-Shepherd, V-STaR (2026-05-17)\\\"\\n    - dimension: \\\"debate_multi_agent\\\"\\n      gap: \\\"Added Liang 2023, Du 2023, Khan 2024 (2026-05-17)\\\"\\n    - dimension: \\\"benchmarks_and_datasets\\\"\\n      gap: \\\"Added FOLIO, ProofWriter, StrategyQA, ARC (2026-05-17)\\\"\\n    - dimension: \\\"negative_results_analysis\\\"\\n      gap: \\\"Added Huang 2024 (self-correct), Mirzadeh 2024 (GSM-Symbolic) (2026-05-17)\\\"\\n    - dimension: \\\"symbolic_reasoning_llm\\\"\\n      gap: \\\"Added LINC (Olausson et al. 2023) (2026-05-17)\\\"\\n    - dimension: \\\"self_consistency_and_variants\\\"\\n      gap: \\\"Added DiVeRSe (Li et al. 2023) (2026-05-17)\\\"\\n    - dimension: \\\"oracle_upper_bound_experiments\\\"\\n      gap: \\\"Added Press 2023 (compositionality gap), Trivedi 2023 (IRCoT oracle retrieval), Saparov & He 2023 (greedy reasoners) (2026-05-17)\\\"\\n    - dimension: \\\"condorcet_voting_theory\\\"\\n      gap: \\\"Added Condorcet 1785, Austen-Smith & Banks 1996, Lefort et al. 2024 (arXiv:2409.00094), Ladha 1992, Fleiss 1971 (2026-05-19)\\\"\\n  remaining: []\\n\", \"total_chars\": 23779, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e80a293c-a85e-4447-91dc-2b28c321b3e0",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "79b5f096-35bc-4eb8-8753-08d90c5bb15c",
  "sourceToolAssistantUUID": "e80a293c-a85e-4447-91dc-2b28c321b3e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T04:49:27.748Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MYgdjWocSVq3gqFoK9dYCw`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79b5f096-35bc-4eb8-8753-08d90c5bb15c",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKkQTDEXRAi6jy5CJbD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "580edbac-f444-4e45-bd86-06edb5f4a1d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C56SWsgPfnbPC73yqTxdZU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 17058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T04:49:27.760Z_

<details><summary>↩ Tool result · `toolu_01MYgdjWocSVq3gqFoK9dYCw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\", \"content\": \"# Paper Framing — symb_invariant_consensus\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25)\\n- Deadline: May 25, 2026 (ARR submission)\\n\\n## D060 Direction: Pure Analysis Paper — Independence Bottleneck\\n\\n**D059 method improvement 三路失败后，回归纯 analysis paper。** 但比 D058 的 analysis 更强：\\n- **Condorcet independence 框架** 提供理论解释（非纯经验）\\n- **9 种修复全部失败**（比原 6 种多 3 种靶向尝试）→ bottleneck 是 fundamental\\n- **exp-052 p=0.039** → 2/3 seeds 显著 → 效应 IS real but fragile\\n- **K sensitivity 倒 U 型** → clean ablation 贡献\\n- **T sensitivity 孤立尖峰** → T=0.3(-0.49), T=0.5(-0.49), T=0.7(+4.90), T=1.0(+0.49)。仅 T=0.7 显著，其余 3 点 noise level → extreme fragility\\n- 用户指示: 投 May 25 不变，≥3.0 兜底\\n\\n## Core Claims (5 条) — D060 纯 Analysis Framing\\n\\n### Analysis Claims (已验证)\\n\\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.500, Eff-K=1.85 (Δ=+4.90pp p=0.013) ← primary seed\\n   - Mistral-7B FOLIO s123: κ=0.412, Eff-K=2.17 (Δ=+3.43pp p=0.039)\\n   - Mistral-7B FOLIO s456: κ=0.401, Eff-K=2.22 (Δ=-0.49pp n.s.)\\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +4.90pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\\n\\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +4.9pp (best case) = 35% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\\\"区分方向\\\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\\n\\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案\\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\\n   - Goldilocks zone (~50-55% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+4.90pp, p=0.013)\\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\\n\\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\\n\\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\\n\\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\\n   - D059 三路 method improvement 全部失败：\\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\\n     - T=1.0 (exp-054): delta 从 +4.90pp 崩塌到 +0.55pp，温度敏感性极端\\n     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity\\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\\n\\n## Core Insight (D060 Updated — Dual Bottleneck)\\n\\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\\n\\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\\n\\n实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：\\n- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高\\n- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈54%（中等质量）→ +4.90pp (2/3 seeds significant)\\n- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp\\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\\n- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality\\n- **T sensitivity 孤立尖峰 (4/4 complete)**：T=0.3(Δ=-0.49, κ=0.502, Eff-K=1.84), T=0.5(Δ=-0.49, SC=57.84%), T=0.7(Δ=+4.90, κ=0.460, Eff-K=1.98), T=1.0(Δ=+0.49, κ=0.394, Eff-K=2.25)。非平滑 inverted-U，而是 T=0.7 孤立尖峰——3/4 点在 noise level (±0.49pp)。T↑ → κ↓ → 更独立，但 SC 也下降（T=0.3/0.5 SC≈57.5% vs T=0.7 SC=54.41%）。T=0.7 碰巧 SC 最低 → entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论\\n- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。\\\"更好的推理\\\"反而加剧 independence bottleneck。\\n\\n**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+4.90 vs +3.43 vs -0.49）→ seed-level constraint quality variance 主导，非 κ。\\n\\n完整 κ 表（13 条件，统一脚本，Table 3 用；SC/Δpp 为 registry 原始值，Table 1 用）：\\n| Exp | Model | κ(unified) | Eff-K | SC%(registry) | Δpp(registry) |\\n|-----|-------|------------|-------|---------------|---------------|\\n| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |\\n| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |\\n| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |\\n| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |\\n| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |\\n| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |\\n| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 57.35 | -0.49 |\\n| exp-058 | Mistral-7B T=0.5 | — | — | 57.84 | -0.49 |\\n| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 54.41 | +4.90 |\\n| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 53.92 | +3.43 |\\n| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 56.37 | -0.49 |\\n| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |\\n| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 54.90 | +0.49 |\\n| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |\\n注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。SC/Δpp 为 registry 原始值（不混用）。\\n\\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 35% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\\n\\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\\n\\n**Key evidence**:\\n- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.\\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\\n- **K sensitivity (non-monotonic peak at K=12, 5/5 complete)**: K=4(-1.47pp), K=8(-0.98pp), K=12(+4.90pp p=0.013), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=54.41% (lowest) — same SC-confound as T sensitivity. K=4 SC ≈ K=12 SC but SICA differs by 6.4pp — proves SICA extracts different information than SC.\\n- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA \\\"最佳超参\\\"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。\\n- **T sensitivity (isolated peak, 4/4 complete)**: T=0.3(-0.49pp), T=0.5(-0.49pp, SC=57.84%), T=0.7(+4.90pp p=0.013), T=1.0(+0.49pp p=0.739). NOT smooth inverted-U — T=0.7 is an isolated spike, other 3 points at noise level (±0.49pp). T=0.7 also has lowest SC (54.41% vs ~57.5%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.\\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=+0.25pp vs Mistral-7B (SC=54.41%) Δ=+4.90pp p=0.013\\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\\n- **Seed replication**: 2/3 seeds significant at α=0.05 (exp-033 p=0.013, exp-052 p=0.039), 1/3 null (exp-053). Effect IS real but fragile — motivates deep analysis of WHY.\\n- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +4.90→+0.49pp), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.\\n- **Entropy mechanism**: High-entropy problems proportion: Mistral 35.8% vs Qwen 10.3%. Unanimous rate: 18.6% vs 58.8%.\\n- **Confirmation bias quantification**: Override precision 70.6% (Mistral) vs 28.6% (Qwen). Constraint agreement >80%: 31.9% vs 62.3%.\\n\\n## Story Spine (D059 Updated)\\n\\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\\n- **Headline result**: \\\"Across 5 model families, symbolic consensus aggregation shows a real but fragile effect: significant improvement in 2/3 seeds under specific conditions (Mistral-7B, FOLIO, T=0.7, K=12), but zero or negative gains under any perturbation. Condorcet analysis reveals the root cause: Effective-K = 1.3-1.8 for nominal K=12 due to trace non-independence. Oracle constraints prove the aggregation mechanism works (+14.22pp), but 9 remediation strategies all fail to overcome the self-extraction bottleneck. C0+SC provides a zero-cost deployment diagnostic.\\\"\\n\\n## Anticipated Reviewer Concerns & Defensive Experiments\\n\\n1. **\\\"Gains not statistically significant\\\"** → exp-033 p=0.013 (n=204), exp-031 oracle p=2.0e-7. Combined N>1,200.\\n2. **\\\"Only one positive result (exp-033)\\\"** → Seed replication: 2/3 significant (p=0.013, p=0.039). Effect IS real but fragile — the fragility itself IS the finding (K/T sensitivity, Condorcet independence).\\n3. **\\\"Condorcet framework is trivial\\\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\\n4. **\\\"Multi-temp / filtering should work\\\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\\n5. **\\\"Only Qwen models\\\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\\n6. **\\\"Only logic domain\\\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\\n7. **\\\"Oracle is unfair comparison\\\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\\n8. **\\\"MAX-SAT is over-engineering\\\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\\n9. **\\\"Self-extraction confound\\\"** → Oracle control resolves completely.\\n10. **\\\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\\\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\\n11. **\\\"C0 is trivially derived\\\"** → Zero-cost early stopping. Practical value.\\n12. **\\\"Why not just use a reasoning model?\\\"** → QwQ-32B: C0<5%, SICA≡SC.\\n13. **\\\"Random tiebreak baseline\\\"** → exp-003: SICA tiebreak 80% vs random 50%.\\n14. **\\\"Method improvement is incremental\\\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\\n15. **\\\"Weighted SC is simpler\\\"** → exp-016 planned. Weighted SC doesn't address independence.\\n16. **\\\"Within-model ICL transition contradicts regime theory\\\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \\\"same model, different prompt\\\" from \\\"same model, same prompt, different accuracy.\\\"\\n\\n## Working Title\\n**\\\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\\\"**\\n(Alternatives:\\n- \\\"The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting\\\"\\n- \\\"Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation\\\")\\n\\nNOTE (Dream D037): Title MUST be scoped to \\\"self-extracted constraints\\\" / \\\"SICA\\\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\\n\\n## Paper Structure (EMNLP 8pp + appendix)\\n\\n### Main Tables\\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\\n- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates\\n- T5: K Sensitivity — K=4/8/12/16/20 with Eff-K and diversity metrics (inverted U curve)\\n\\n### Main Figures\\n- F1: Method Pipeline (SICA + oracle control design)\\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\\n- F4: Extraction error breakdown (stacked bar)\\n\\n### Appendix\\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\\n- Six remediation strategy details\\n- Confirmation bias quantification\\n- Seed replication analysis\\n- QwQ-32B / DeepSeek-R1 negative control\\n\\n## Claim Risk Notes (D059)\\n- **Seed replication**: 2/3 significant (p=0.013, p=0.039), 1/3 null. Frame as \\\"real but fragile effect\\\" — motivates analysis of WHY.\\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \\\"SC determines SICA.\\\" Explain via trace generation characteristic change.\\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\\n\\n## Required Citations (minimum 30 references)\\n\\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\\n\\n## Claim Scoping Rules\\n- n=60 conditions: \\\"suggestive/consistent with\\\" NOT \\\"confirming\\\"\\n- n≥200 conditions: can \\\"confirm\\\"\\n- Combined N>1,300: acceptable if breakdown clearly stated\\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\\n- \\\"Independence bottleneck\\\" framing: systematic quantification + theoretical grounding\\n\", \"total_chars\": 17789, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "580edbac-f444-4e45-bd86-06edb5f4a1d0",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "e9518d7a-36cd-4650-b752-bd8dbc2a8519",
  "sourceToolAssistantUUID": "580edbac-f444-4e45-bd86-06edb5f4a1d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T04:49:28.016Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TGrkL5FYYKRXyQtX81RoE5`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9518d7a-36cd-4650-b752-bd8dbc2a8519",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKkQTDEXRAi6jy5CJbD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e76b393-74cf-47df-8f1c-3e1bb487e2dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C56SWsgPfnbPC73yqTxdZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 17058,
      "output_tokens": 368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1450
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 368,
          "cache_read_input_tokens": 17058,
          "cache_creation_input_tokens": 1450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1450,
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

_source line 14 · 2026-05-19T04:49:28.024Z_

<details><summary>↩ Tool result · `toolu_01TGrkL5FYYKRXyQtX81RoE5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e76b393-74cf-47df-8f1c-3e1bb487e2dd",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "b1db314c-da5c-4807-847d-db62123fed26",
  "sourceToolAssistantUUID": "2e76b393-74cf-47df-8f1c-3e1bb487e2dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-19T04:49:31.025Z_

Now let me read the actual paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1db314c-da5c-4807-847d-db62123fed26",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKknx4DGpg2c3BEKwwS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77b06da4-d298-44f7-b789-9c6b92687e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pyozg9JkfJhYBxrYQFp6tW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19131,
      "cache_read_input_tokens": 18508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 16 · 2026-05-19T04:49:32.445Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HJqehJns723NY8j4THxrjQ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77b06da4-d298-44f7-b789-9c6b92687e28",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKknx4DGpg2c3BEKwwS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01effaac-05bc-4073-9053-ba2845c24a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pyozg9JkfJhYBxrYQFp6tW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19131,
      "cache_read_input_tokens": 18508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T04:49:32.459Z_

<details><summary>↩ Tool result · `toolu_01HJqehJns723NY8j4THxrjQ`</summary>

```text
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T124139/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
artifacts/dream_reports/dream_20260516T155754/best/paper.tex
artifacts/dream_reports/dream_20260516T155754/median/paper.tex
artifacts/dream_reports/dream_20260516T155754/worst/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
artifacts/dream_reports/dream_20260517T165032/best/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260517T165032/median/paper.tex
artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments_9ea847.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/related_work_b9688e.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/abstract.tex
docs/paper/limitations_content.tex
docs/paper/appendix.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/experiments.tex
artifacts/dream_reports/dream_20260519T034058/best/paper.tex
artifacts/dream_reports/dream_20260519T034058/median/paper.tex
docs/paper/method.tex
artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
docs/paper/analysis.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01effaac-05bc-4073-9053-ba2845c24a5e",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "2be2bba6-a59b-4a6e-bc87-171b3e40f02e",
  "sourceToolAssistantUUID": "01effaac-05bc-4073-9053-ba2845c24a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T04:49:32.977Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LW1R8D5G3DkFrptWegYYTo`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2be2bba6-a59b-4a6e-bc87-171b3e40f02e",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKknx4DGpg2c3BEKwwS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9cc522a-4d48-459d-a867-ce468c88a26d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pyozg9JkfJhYBxrYQFp6tW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19131,
      "cache_read_input_tokens": 18508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T04:49:32.985Z_

<details><summary>↩ Tool result · `toolu_01LW1R8D5G3DkFrptWegYYTo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp-048-llama8b-pw600 | LLaMA-3.1-8B-Instruct 在 ProofWriter-600 上 SICA vs SC。FOLIO-204 上 LLaMA-8B SC=63.2% delta=-2.45pp (exp-020)。PW 是更结构化的形式推理数据集，测试 SICA 在 PW 上对低能力模型是否有效（补充 regime boundary 跨域证据）。parent=exp-020 | — | — | — |\\n| exp-040-qwen3-pw600-16639 | Qwen3-14B non-thinking 在 ProofWriter-600 全量上 SICA vs SC：跨模型代际验证 capability trap 在 PW 数据集上是否持续。与 exp-039 (Qwen2.5-14B PW-600) 对比代际差异。 | — | — | — |\\n| exp-039-14b-pw600-16639 | Qwen2.5-14B-Instruct 在 ProofWriter-600 全量上 SICA vs SC（westd-16639 重跑）：验证 capability trap 在 PW 数据集全量规模上是否持续。复现 sica_expanded_14b 的 PW 子集结果（delta=+0.3pp）。 | — | — | — |\\n\\n## 待处理\\n- exp-053-mistral-folio204-seed456: exp-033 replication (seed=456): Mistral-7B FOLIO-204 K=12 T=0.7，第二组独立 replication。与 exp-052 (seed=123) 一起验证 exp-033 结论 robustness。parent=exp-033（排队等待 GPU）\\n- exp-052-mistral-folio204-seed123: exp-033 replication (seed=123): Mistral-7B FOLIO-204 K=12 T=0.7，与 exp-033 (seed=42, delta=+4.90pp, p=0.013) 完全相同配置，仅 seed 不同。验证正向结果是否 seed-robust。parent=exp-033（排队等待 GPU）\\n- smoke-test-5q（准备中）\\n\\n## 近期结论\\n- **exp-058-mistral-folio204-t05** (negative): T=0.5 delta 介于 T=0.3 和 T=0.7 之间，形成温度-SICA delta 曲线。与 exp-033 (T=0.7, +4.90pp) 和 exp-054 (T=1.0, +0.49pp) 共同构成 4 点 T sensitivity ablation。parent=exp-033, D060 analysis paper ← 基于 exp-033\\n- **exp-051-mistral-k-sensitivity** (success): Mistral-7B K sensitivity on FOLIO-204: K=[4,8,16,20]（K=12 已有 exp-033 delta=+4.90pp）。验证正向结果对 K 选择是否稳健。Reviewer 必问 ablation。parent=exp-033\\n- **exp-057-mistral-folio204-t03** (failed): T=0.3 低温 traces 更确定性更一致，SICA delta < T=0.7 的 +4.90pp。与 exp-054 (T=1.0, +0.49pp) 共同形成 T sensitivity ablation curve。parent=exp-033, D060 analysis paper ← 基于 exp-033\\n\\n## 趋势\\n成功 21 / 负向 30 / 失败 18 / 共 78\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-16639: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nwestd-25068: 无 GPU 信息\\n\\n## 告警\\n- mvp_math50_t07: 已被终止 — unknown\\n- sica_aime30_t07: 已被终止 — unknown\\n- sica_aime30_v2: 已被终止 — unknown\\n- sica_aime30_v3: 已被终止 — unknown\\n- sica_proofwriter30: 训练失败 — unknown\\n- sica_folio30: 已被终止 — unknown\\n- sica_proofwriter30_v2: 已被终止 — unknown\\n- exp-011-llama8b: 训练失败 — unknown\\n- exp-010-mistral: 训练失败 — unknown\\n- exp-011-llama8b-v2: 训练失败 — unknown\\n- exp-017-strategyqa: 训练失败 — unknown\\n- exp-018-arc: 训练失败 — unknown\\n- exp-010-mistral-v2: 训练失败 — unknown\\n- exp-017-strategyqa-v2: 训练失败 — unknown\\n- pilot-contrastive-prompt: 训练失败 — unknown\\n- exp-028-qwen3-14b-thinking: 已被终止 — unknown\\n- exp-033-qwen3-pw600-nonthinking: 训练失败 — unknown\\n- exp-007-qwen72b-awq: 训练失败 — unknown\\n- exp-004-qwen7b-rerun: 训练失败 — unknown\\n- exp-042-premise-formalization: 训练失败 — unknown\\n- exp-044-icl-oracle: 训练失败 — unknown\\n- exp-042b-premise-formal: 训练失败 — unknown\\n- exp-045b-backward-verify: 已被终止 — unknown\\n- exp-028b-qwen3-thinking-folio204: 已被终止 — unknown\\n- exp-049-mistral-logiqa200: 训练失败 — unknown\\n- exp-050-mistral-icl-oracle-folio199: 训练失败 — unknown\\n- exp-057-mistral-folio204-t03: 训练失败 — unknown\\n\", \"total_chars\": 3032, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9cc522a-4d48-459d-a867-ce468c88a26d",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "6a881b5f-a9db-4d9c-a2db-2b6eb9fe6038",
  "sourceToolAssistantUUID": "a9cc522a-4d48-459d-a867-ce468c88a26d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T04:49:33.562Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018HY2VFXSA552LZqBfsrXtt`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a881b5f-a9db-4d9c-a2db-2b6eb9fe6038",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKknx4DGpg2c3BEKwwS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5903b654-5862-4c81-859d-d4d8ac7aa602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pyozg9JkfJhYBxrYQFp6tW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19131,
      "cache_read_input_tokens": 18508,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 18508,
          "cache_creation_input_tokens": 19131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19131,
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

_source line 21 · 2026-05-19T04:49:33.839Z_

<details><summary>↩ Tool result · `toolu_018HY2VFXSA552LZqBfsrXtt`</summary>

```text
Error: result (53,804 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/ff4131df-0538-40e9-a5d8-d0234a1df865/tool-results/mcp-agent-ml-research-read_project_file-1779166173826.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/ff4131df-0538-40e9-a5d8-d0234a1df865/tool-results/mcp-agent-ml-research-read_project_file-1779166173826.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5903b654-5862-4c81-859d-d4d8ac7aa602",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "a6928e6e-b3d1-43c2-abb9-5cbeebbc837b",
  "sourceToolAssistantUUID": "5903b654-5862-4c81-859d-d4d8ac7aa602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-19T04:49:35.459Z_

Let me read the paper files and the decisions file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6928e6e-b3d1-43c2-abb9-5cbeebbc837b",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKmDbdjMnaNvirr6hiE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0375be50-fe6f-4894-bba6-bf7b26052b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8VGEr4wWYcrXzC3FLjBDE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 37639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3334,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T04:49:36.498Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KTreTDV5Cy9VZxN5tCK6Ax`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0375be50-fe6f-4894-bba6-bf7b26052b89",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKmDbdjMnaNvirr6hiE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eba8b4d8-5abb-469a-816e-4b01951ab978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8VGEr4wWYcrXzC3FLjBDE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 37639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3334,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T04:49:36.515Z_

<details><summary>↩ Tool result · `toolu_01KTreTDV5Cy9VZxN5tCK6Ax`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning,calc}
18	\usepackage{listings}
19	\usepackage{algorithm}
20	\usepackage{algpseudocode}
21	\usepackage{hyperref}
22	\usepackage{cleveref}
23	
24	\lstset{
25	  basicstyle=\small\ttfamily,
26	  breaklines=true,
27	  frame=single,
28	  xleftmargin=1em,
29	  xrightmargin=1em,
30	  aboveskip=0.5em,
31	  belowskip=0.5em,
32	}
33	
34	\graphicspath{{../figures/paper/}{figures/}}
35	
36	\title{Beyond Self-Consistency: How Trace Independence Limits\\Symbolic Consensus in LLM Reasoning}
37	
38	\author{Anonymous}
39	
40	\begin{document}
41	\maketitle
42	
43	\input{abstract}
44	
45	\input{introduction}
46	
47	\input{related_work}
48	
49	\input{method}
50	
51	\input{experiments}
52	
53	\input{analysis}
54	
55	\input{discussion}
56	
57	\input{conclusion}
58	
59	\section*{Limitations}
60	\input{limitations_content}
61	
62	\bibliography{references}
63	
64	\appendix
65	\input{appendix}
66	
67	\end{document}
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eba8b4d8-5abb-469a-816e-4b01951ab978",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "3047e327-717d-4b19-bd02-e9003cfe4a04",
  "sourceToolAssistantUUID": "eba8b4d8-5abb-469a-816e-4b01951ab978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T04:49:36.876Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W2jq5xTb3UKok6vxmEH3w7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3047e327-717d-4b19-bd02-e9003cfe4a04",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKmDbdjMnaNvirr6hiE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1578759b-3d98-40e9-b6bd-347715a05409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8VGEr4wWYcrXzC3FLjBDE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 37639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3334,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T04:49:36.881Z_

<details><summary>↩ Tool result · `toolu_01W2jq5xTb3UKok6vxmEH3w7`</summary>

```text
1	\begin{abstract}
2	Neuro-symbolic methods extract first-order logic (FOL) constraints from Large Language Model (LLM) reasoning traces to improve answer aggregation beyond majority voting. Whether the reasoning model itself can produce useful constraints through self-extraction remains an open question. We evaluate Symbolic Invariant Consensus Aggregation (SICA), which formulates a weighted partial Maximum Satisfiability (MAX-SAT) problem over self-extracted FOL constraints, across seven models from four base architectures (7B to 32B parameters) on four reasoning domains with more than 2,400 total instances. SICA benefits exist only in a narrow Goldilocks zone ($\sim$50--55\% Self-Consistency): Mistral-7B achieves $+4.90$ percentage points on FOLIO ($p = 0.013$). Outside this band, SICA fails in three distinct ways. Above $\sim$60\% Self-Consistency, confirmation bias causes constraints to mirror model answers, reducing SICA to majority voting (eight conditions, all nonsignificant). Below $\sim$40\%, predominantly incorrect traces produce noisy constraints that actively hurt performance (Mistral-7B on ProofWriter-D5: $\Delta = -4.67$ pp). When domain structure resists formalization, extraction yields no discriminative signal regardless of accuracy. Oracle controls substituting gold FOL annotations yield $+14.22$ and $+11.50$ percentage points (both $p < 0.001$), confirming that aggregation works with discriminative constraints and localizing the bottleneck to extraction quality. Six remediation strategies, including in-context learning with gold FOL examples, all fail to widen this zone. The multi-candidate rate $C_0$ combined with Self-Consistency accuracy provides a two-dimensional deployment diagnostic.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1578759b-3d98-40e9-b6bd-347715a05409",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "ae41ffca-8538-4cf5-884b-50f93a3c8f85",
  "sourceToolAssistantUUID": "1578759b-3d98-40e9-b6bd-347715a05409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T04:49:37.289Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RpgjYwqgGEiV3nHYNshsP8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae41ffca-8538-4cf5-884b-50f93a3c8f85",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKmDbdjMnaNvirr6hiE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2429041-6747-4371-9168-f2a54ee2495b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8VGEr4wWYcrXzC3FLjBDE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 37639,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3334
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 37639,
          "cache_creation_input_tokens": 3334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3334,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T04:49:37.293Z_

<details><summary>↩ Tool result · `toolu_01RpgjYwqgGEiV3nHYNshsP8`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Scaling test-time computation has emerged as a key strategy for improving large language model (LLM) reasoning \citep{snell2025scaling}. Majority voting over multiple chain-of-thought samples, known as Self-Consistency (SC) \citep{wang2023sc}, remains the dominant aggregation method but faces diminishing returns from additional traces \citep{loo2025reevaluating}. Verification-based approaches that extract richer signal from reasoning traces offer a path to break this plateau. Symbolic verification through formal constraints and satisfiability solvers is one such direction, as it provides logical guarantees that natural language self-critique lacks \citep{huang2024selfcorrect}.
4	
5	Neuro-symbolic methods that augment LLM reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \citep{xu2026dylos}, apply logic-complete decomposition \citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \citep{wang2025fover}, or employ multi-perspective grounding \citep{luo2025logicagent}. These systems report positive results, but each introduces capabilities beyond the reasoning model itself: trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering.
6	
7	These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces, and if so, under what conditions? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical value of neuro-symbolic reasoning depends on knowing not just whether symbolic methods can help, but \emph{when}.
8	
9	We evaluate this question through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that prompts a single LLM to extract FOL-style constraints (in practice predominantly ground propositional clauses; \S\ref{sec:constraint-extraction}) from $K$ reasoning traces, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\ref{fig:pipeline}). We test seven models from 7B to 32B parameters, including instruction-tuned, reasoning-specialized, and distilled variants, across four reasoning domains (FOLIO \citep{han2022folio}, ProofWriter \citep{tafjord2021proofwriter}, LogiQA \citep{liu2020logiqa}, StrategyQA \citep{geva2021strategyqa}) with supplementary probes on GSM8K \citep{cobbe2021gsm8k} and AIME 2024, totaling more than 2,400 evaluation instances. Oracle controls on FOLIO ($n=204$) and ProofWriter ($n=600$) replace self-extracted constraints with gold annotations verified by Z3, isolating extraction quality from aggregation effectiveness \citep{press2023compositionality}.
10	
11	The answer reveals a Goldilocks zone. SICA benefits exist only in a narrow band of model accuracy ($\sim$50--55\% SC), with three distinct failure modes outside it. Above $\sim$60\% SC (Type A), constraints exhibit confirmation bias and SICA reduces to majority voting across eight conditions (combined $N > 2{,}000$), including in-context learning with gold FOL examples ($\Delta = +0.54$\,pp, n.s.). Below $\sim$40\% SC (Type C), predominantly incorrect traces produce noisy constraints that actively hurt: Mistral-7B on ProofWriter-D5 shows $\Delta = -4.67$\,pp ($n = 303$). When the domain resists formalization (Type B), extraction yields no signal regardless of accuracy. Within the Goldilocks zone, Mistral-7B achieves $+4.90$\,pp on FOLIO ($p = 0.013$, $n = 204$). Oracle experiments yield $+14.22$\,pp on FOLIO and $+11.50$\,pp on ProofWriter (both $p < 0.001$), proving the aggregation mechanism is sound with discriminative constraints. Entropy-conditioned analysis reveals the mechanism: SICA gains concentrate in high-entropy problems ($+9.6$\,pp, $n = 73$), and the aggregate effect depends on the proportion of such problems (35.8\% Mistral vs.\ 10.3\% Qwen). Six remediation strategies all fail to widen this zone (\S\ref{sec:interventions}). For practitioners, the multi-candidate rate $C_0$ combined with SC accuracy forms a two-dimensional deployment diagnostic (\S\ref{sec:c0}).
12	
13	Our contributions are:
14	\begin{itemize}
15	\item We identify a Goldilocks zone in same-model constraint extraction: SICA benefits require model accuracy in a narrow band ($\sim$50--55\% SC). Above $\sim$60\% SC, confirmation bias renders constraints non-discriminative (Type A). Below $\sim$40\% SC, incorrect traces produce harmful constraints (Type C: $\Delta = -4.67$\,pp). Across seven models and four reasoning domains ($N > 2{,}400$), only the Goldilocks zone yields significant gains ($+4.90$\,pp, $p = 0.013$). Six remediation strategies confirm the boundaries are structural (\S\ref{sec:main-results}, \S\ref{sec:interventions}).
16	\item We introduce oracle controls on two datasets that causally localize the bottleneck: replacing self-extraction with gold annotations yields $+14.22$\,pp on FOLIO ($p = 2.0 \times 10^{-7}$) and $+11.50$\,pp on ProofWriter ($p < 0.001$). Even the best self-extraction result captures only 34.5\% of the oracle ceiling (\S\ref{sec:oracle}).
17	\item We provide entropy-conditioned mechanism evidence: SICA gains concentrate in high-entropy problems ($+9.6$\,pp, $n = 73$ for Mistral-7B), and the aggregate regime effect reflects the proportion of such problems in each model's trace distribution. Confirmation bias (62.3\% vs.\ 31.9\%), override precision (28.6\% vs.\ 70.6\%), and unanimous answer rate (58.8\% vs.\ 18.6\%) quantify the causal path from model accuracy to constraint quality (\S\ref{sec:entropy}).
18	\item We propose $C_0$ and SC accuracy as a two-dimensional, zero-cost diagnostic: low $C_0$ rules out SICA benefit by construction, while high $C_0$ with high SC identifies the capability trap regime (\S\ref{sec:c0}).
19	\end{itemize}
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2429041-6747-4371-9168-f2a54ee2495b",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "494f4fdf-78cd-482a-9a64-704a7fb67b17",
  "sourceToolAssistantUUID": "c2429041-6747-4371-9168-f2a54ee2495b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T04:49:45.733Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UMLqJDfgxocrCkjvScUWby`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494f4fdf-78cd-482a-9a64-704a7fb67b17",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKmUcXAuNXpoM4sFBrt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a518dd5f-4570-433e-9464-7bb890273fee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMQPo1M1wKyXucYjMWEXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6508,
      "cache_read_input_tokens": 37639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6508,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T04:49:45.737Z_

<details><summary>↩ Tool result · `toolu_01UMLqJDfgxocrCkjvScUWby`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Self-Consistency and Extensions.}
5	Self-Consistency (SC) selects the most frequent answer across multiple chain-of-thought traces \citep{wang2023sc}. Universal SC extends this to free-form generation by using an LLM to select among diverse candidates \citep{chen2024usc}. Confidence-weighted variants assign non-uniform weights to traces \citep{taubenfeld2025cisc}, and DiVeRSe combines diverse prompts with a step-aware verifier \citep{li2023diverse}. Reasoning-aware sampling refines SC further by using textual quality indicators \citep{wan2024rasc} or evidence sufficiency \citep{kim2026reasc} to filter traces without training a separate model. \citet{loo2025reevaluating} show that SC gains plateau early and decline for strong models. Our Condorcet analysis explains this pattern: same-model traces yield Fleiss' $\kappa$ of 0.21--0.82, compressing $K_{\text{eff}}$ to 1.2--3.6 for $K = 12$ (\S\ref{sec:effective-k}). SICA shares SC's sampling setup but replaces majority voting with MAX-SAT aggregation over symbolic constraints. The substitution is regime-dependent: self-extracted constraints provide gains only when SC accuracy falls in a narrow band (${\sim}$50--55\%).
6	
7	\paragraph{Neuro-Symbolic Reasoning.}
8	Logic-LM \citep{pan2023logiclm} translates natural language problems into first-order logic (FOL) and delegates solving to an external prover. LINC \citep{olausson2023linc} follows a similar pipeline but documents ${\sim}$40\% translation errors on FOLIO. More recent systems extend this integration: DyLoS \citep{xu2026dylos} adaptively selects solver types, Aristotle \citep{li2025aristotle} applies logic-complete decomposition, FoVer \citep{wang2025fover} trains dedicated FOL verifiers, and LogicAgent \citep{luo2025logicagent} employs multi-perspective grounding. Each introduces capabilities beyond the reasoning model itself, whether through trained extractors, external provers, or multi-component pipelines. \citet{amonkar2025realitycheck} show that LLM formalization quality degrades with problem complexity, consistent with our extraction-quality findings. SICA asks whether the \emph{same} model can extract useful constraints from its own traces without additional machinery. Our oracle controls ($+14.22$\,pp on FOLIO, $+11.50$\,pp on ProofWriter; \S\ref{sec:oracle-design}) confirm the aggregation mechanism is sound when constraints are discriminative; the failure localizes to self-extraction quality, not the symbolic approach. This oracle-replacement methodology follows \citet{press2023compositionality}, who use oracle sub-questions to isolate pipeline bottlenecks.
9	
10	\paragraph{Test-Time Compute and Trace Diversity.}
11	Scaling test-time computation through additional reasoning traces offers an alternative to parameter scaling \citep{snell2025scaling}. Reasoning-specialized models such as DeepSeek-R1 \citep{guo2025deepseekr1} internalize extended chain-of-thought through reinforcement learning, and diversity-aware training explicitly optimizes for trace variety at test time \citep{diverseaware2026}. These approaches share a common challenge: independent reasoning attempts from the same model collapse into correlated solutions. Our Condorcet/$K_{\text{eff}}$ analysis (\S\ref{sec:condorcet}) provides a theoretical framework for this collapse. Same-model sampling creates correlated voters, and the effective ensemble size $K_{\text{eff}}$ is bounded by inter-trace agreement regardless of how many traces $K$ are sampled. Reasoning models intensify this problem: QwQ-32B achieves a multi-candidate rate $C_0$ of only 2.6\%, reducing any aggregation method to the unanimous output.
12	
13	\paragraph{Verification and Reranking.}
14	Trained verifiers offer a data-driven alternative to self-extraction. Outcome reward models (ORMs) score complete solutions \citep{cobbe2021gsm8k}, process reward models (PRMs) assign step-level scores and outperform outcome-level verification \citep{lightman2024prm}, and Math-Shepherd automates process supervision without human annotations \citep{wang2024mathshepherd}. Multi-agent debate refines answers through iterative natural-language discussion \citep{liang2023encouraging,du2023improving}, a paradigm distinct from SICA's one-shot symbolic aggregation. Self-correction methods attempt refinement without external feedback \citep{huang2024selfcorrect,madaan2023selfrefine}, but \citet{stechly2025selfverification} show that LLM self-verification degrades performance while sound external verification yields gains. Their finding parallels our capability trap in the high-accuracy regime. Both trained verifiers and SICA face extraction-quality challenges, but trained approaches may prove more robust because they learn discriminative patterns from data rather than relying on the same model's symbolic capabilities. The consistent pattern across this literature is that reliably improving on majority voting requires information beyond the reasoning model's own outputs (\S\ref{sec:remediation}).
15	
16	\paragraph{Condorcet Jury Theorem and Ensemble Diversity.}
17	The Condorcet Jury Theorem (CJT) \citep{condorcet1785} establishes that majority voting among independent voters, each correct with probability $p > 0.5$, converges to correctness as the number of voters grows. \citet{austensmith1996} extend this result to information aggregation under strategic conditions. \citet{ladha1992correlated} prove that correlated voters reduce the effective ensemble size, a result we operationalize as $K_{\text{eff}} = K / (1 + (K{-}1) \cdot \kappa)$ in \S\ref{sec:condorcet}. \citet{lefort2024condorcet_llm} apply the CJT framework to LLM ensemble sentiment classification and document independence violations when all ensemble members share the same architecture. We extend this line of work to reasoning-trace aggregation, measuring $\kappa$ and $K_{\text{eff}}$ across 10 model-dataset conditions (\S\ref{sec:effective-k}). Fleiss' $\kappa$ \citep{fleiss1971kappa} serves as our inter-rater agreement metric, connecting the voting-theory framework to a concrete diagnostic for when symbolic aggregation can improve over majority voting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a518dd5f-4570-433e-9464-7bb890273fee",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "1746a63c-35b1-48e3-838d-de2f0cdf2f2f",
  "sourceToolAssistantUUID": "a518dd5f-4570-433e-9464-7bb890273fee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T04:49:46.029Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KqMutwJrfoBgFfDWNHqAnz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1746a63c-35b1-48e3-838d-de2f0cdf2f2f",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKmUcXAuNXpoM4sFBrt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "584c6143-018a-4414-8d66-6a5821050986",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMQPo1M1wKyXucYjMWEXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6508,
      "cache_read_input_tokens": 37639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6508,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T04:49:46.041Z_

<details><summary>↩ Tool result · `toolu_01KqMutwJrfoBgFfDWNHqAnz`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces from a language model and selects the answer by majority vote: $a^* = \arg\max_{a} \sum_{i=1}^{K} \mathbf{1}[a_i = a]$. The theoretical justification for this approach follows the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: given $K$ independent voters each correct with probability $p > 0.5$, the probability that the majority is correct approaches 1 as $K \to \infty$ \citep{austensmith1996}.
8	
9	CJT requires that voters be conditionally independent given the correct answer. LLM traces violate this assumption: all $K$ samples come from the same model, conditioned on the same prompt, with only sampling temperature as a source of variation. Correlated voters reduce the effective ensemble size. \citet{ladha1992correlated} show that under uniform pairwise correlation $\rho$, the effective number of independent voters is $K_{\text{eff}} = K / (1 + (K{-}1)\rho)$. We use Fleiss' $\kappa$ \citep{fleiss1971kappa} as an empirical proxy for inter-trace agreement:
10	\begin{equation}
11	\label{eq:effk}
12	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
13	\end{equation}
14	
15	In our experiments (\S\ref{sec:effective-k}), $\kappa$ ranges from 0.21 to 0.82 across model-dataset pairs, yielding $K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$. At $K_{\text{eff}} \approx 1$, additional traces provide almost no new information, and the CJT guarantee collapses. This \emph{independence bottleneck} motivates our investigation: can structured constraint extraction recover discriminative signal that majority voting cannot?
16	
17	\subsection{SICA Pipeline}
18	\label{sec:pipeline}
19	
20	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from reasoning traces and selecting the answer best supported by the satisfiable subset. Figure~\ref{fig:pipeline} illustrates the pipeline.
21	
22	\paragraph{Trace generation.} Given a question $q$, an LLM generates $K$ reasoning traces $\{t_1, \ldots, t_K\}$ by sampling at temperature $T = 0.7$. Each trace $t_i$ yields a candidate answer $a_i$.
23	
24	\paragraph{Constraint extraction.}
25	The same LLM extracts structured first-order logic (FOL) constraints from each trace $t_i$ at a lower temperature $T_{\text{ext}} = 0.3$. While we prompt for FOL-style formalizations, the extracted constraints are predominantly ground propositional clauses without quantifiers, reflecting instruction-scale model capabilities. The extraction prompt requests JSON output containing the constraint type, a human-readable expression, and a Z3-compatible formula string. Each constraint $c$ is associated with its source trace $t_i$ and the answer $a_i$ that trace produced. The full prompt template is in Appendix~\ref{app:prompts}. We define the \emph{extraction rate} as the fraction of traces yielding at least one parseable constraint. Traces with no valid constraints are excluded from MAX-SAT but still contribute answers to the candidate pool.
26	
27	\paragraph{Syntactic deduplication.} Constraints are deduplicated across traces by syntactic equivalence. Each unique constraint $c_m$ receives weight $w_m$ equal to the number of distinct traces that produced it.
28	
29	\paragraph{Weighted partial MAX-SAT.}
30	Let $\mathcal{A}(q) = \{a : a \in \{a_1, \ldots, a_K\}\}$ denote the set of distinct candidate answers for question $q$, and let $\mathcal{C} = \{c_1, \ldots, c_M\}$ denote the deduplicated constraint pool with weights $\{w_1, \ldots, w_M\}$. Each unique constraint $c_m$ serves as a soft clause with weight $w_m$. The objective is to find the largest-weight satisfiable subset:
31	\begin{equation}
32	\label{eq:maxsat}
33	\mathcal{C}^* = \arg\max_{\mathcal{S} \subseteq \mathcal{C}} \sum_{c \in \mathcal{S}} w_c \quad \text{s.t.} \quad \mathcal{S} \text{ is satisfiable.}
34	\end{equation}
35	Z3 \citep{demoura2008z3} solves this with a 10-second per-problem timeout. To ensure each candidate answer participates in scoring, the pipeline injects an \emph{answer assertion} constraint $\texttt{answer\_a} \mathrel{{=}{=}} \texttt{True}$ for each trace, with weight~1. This guarantees that every candidate receives a nonzero base score proportional to its vote count; SICA is therefore a strict generalization of SC.
36	
37	\paragraph{Answer scoring.} Let $\mathcal{C}^{\setminus} = \mathcal{C} \setminus \mathcal{C}^*$ denote the excluded constraint set. Each candidate answer $a \in \mathcal{A}(q)$ is scored by:
38	\begin{equation}
39	\label{eq:score}
40	\text{score}(a) = \sum_{c \in \mathcal{C}^*} w_c \cdot \sigma(c, a) \;-\; \alpha \sum_{c \in \mathcal{C}^{\setminus}} w_c \cdot \sigma(c, a),
41	\end{equation}
42	where $\sigma(c, a) \in \{0, 1\}$ is a source-trace indicator: $\sigma(c, a) = 1$ if $c$ was extracted from any trace that produced answer $a$, and 0 otherwise. The penalty weight $\alpha = 0.5$ in all experiments. The first term rewards answers whose source constraints are satisfied; the second penalizes answers whose source constraints were excluded by MAX-SAT. Discriminative signal arises when constraints from different traces conflict: Z3 excludes low-weight constraints from $\mathcal{C}^*$, and the scorer attributes these exclusions to the corresponding source answers via $\sigma$ (see Algorithm~\ref{alg:scorer} in Appendix~\ref{app:z3-pseudocode}). The selected answer is $a^* = \arg\max_{a \in \mathcal{A}} \text{score}(a)$.
43	
44	\paragraph{Degeneration under non-discriminative constraints.}
45	In practice, self-extracted constraints are tightly coupled to their source answer: $c_m$ derived from trace $t_i$ typically entails $a_i$ ($\sigma(c_m, a_i) \approx 1$). When constraints lack discriminative power across candidates, MAX-SAT excludes almost no constraints ($|\mathcal{C}^{\setminus}| \approx 0$), so the penalty term vanishes regardless of $\alpha$, and the score function degenerates:
46	\begin{equation}
47	\label{eq:degenerate}
48	\text{score}(a) \approx \sum_{\substack{c \in \mathcal{C}^* \\ \text{source}(c) \to a}} w_c,
49	\end{equation}
50	which reduces to a weighted count of traces supporting $a$, equivalent to majority voting when weights are uniform. Only ${\sim}8$\% of self-extracted constraints are semantically discriminative across candidates (\S\ref{sec:extraction-taxonomy}). The ablation in \S\ref{sec:ablation} confirms this empirically: MAX-SAT, count-only, and random-weight baselines produce nearly identical accuracy.
51	
52	\paragraph{The $C_0$ diagnostic.}
53	We define the multi-candidate rate $C_0$ as the fraction of questions for which $K$ sampled traces produce more than one distinct answer (Eq.~\ref{eq:c0-def}). $C_0$ is a zero-cost diagnostic computable before any constraint extraction. When $C_0 < 5$\%, nearly all questions are answered unanimously and SICA produces the same output as SC by construction. High $C_0$ does not guarantee improvement but ensures disagreement exists for constraints to resolve.
54	\begin{equation}
55	\label{eq:c0-def}
56	C_0 = \frac{|\{q \in \mathcal{Q} : |\mathcal{A}(q)| > 1\}|}{|\mathcal{Q}|}.
57	\end{equation}
58	
59	\begin{figure}[t]
60	\centering
61	\small
62	\begin{tikzpicture}[
63	    node distance=0.4cm and 0.35cm,
64	    box/.style={draw, rounded corners=2pt, minimum height=0.6cm,
65	                text width=1.6cm, align=center, font=\scriptsize},
66	    arr/.style={-{Stealth[length=4pt]}, thick},
67	    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},
68	    lbl/.style={font=\scriptsize, text=gray!70!black},
69	    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,
70	                    inner sep=3pt},
71	]
72	\node[box] (q) {Question $q$};
73	\node[box, right=of q] (sample) {Sample $K$\\traces};
74	\node[box, right=of sample] (extract) {Extract FOL\\constraints};
75	\node[box, right=of extract] (dedup) {Dedup.\ +\\weight};
76	\node[box, right=of dedup] (maxsat) {MAX-SAT\\(Z3)};
77	
78	\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};
79	\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\vote};
80	
81	\draw[arr] (q) -- (sample);
82	\draw[arr] (sample) -- (extract);
83	\draw[arr] (extract) -- (dedup);
84	\draw[arr] (dedup) -- (maxsat);
85	\draw[arr] (maxsat) -- (ans);
86	\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);
87	
88	\node[lbl, above=0.01cm of maxsat] {SICA};
89	
90	% Independence Bottleneck annotation
91	\node[ibottle, fit=(sample)(extract), label={[font=\scriptsize\itshape, text=red!70!black]above:Independence Bottleneck}] {};
92	
93	\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};
94	\end{tikzpicture}
95	\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts FOL constraints from each trace, deduplicates, and solves a MAX-SAT instance via Z3. The red dashed box marks the independence bottleneck: same-model sampling and extraction produce correlated constraints ($K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$). Dashed arrow: the oracle variant substitutes gold FOL annotations.}
96	\label{fig:pipeline}
97	\end{figure}
98	
99	\subsection{Oracle Control Design}
100	\label{sec:oracle-design}
101	
102	To isolate whether the bottleneck lies in constraint extraction or in the aggregation mechanism, we introduce an oracle control. For FOLIO \citep{han2022folio}, gold FOL annotations replace self-extracted constraints. For ProofWriter \citep{tafjord2021proofwriter}, gold domain-specific logic (DSL) rules serve the same role. In both cases, Z3 evaluates the gold constraints against each candidate answer produced by the original $K$ traces; the scoring function (Eq.~\ref{eq:score}) remains unchanged.
103	
104	This design functions as a causal intervention on constraint quality. If the oracle variant produces large gains while self-extraction does not, the aggregation mechanism itself is sound, and the failure localizes to constraint extraction. Conversely, if the oracle also fails, the MAX-SAT aggregation framework is insufficient regardless of constraint quality. Results of this intervention appear in \S\ref{sec:oracle}.
105	
106	\subsection{Scope}
107	\label{sec:scope}
108	
109	SICA as evaluated here uses \emph{same-model self-extraction}: the same LLM generates traces and extracts constraints. This design isolates whether a model's own reasoning can be usefully formalized for aggregation. Methods that use trained extractors, external provers, or multi-model ensembles fall outside the scope of this evaluation. We test nine remediation strategies spanning prompting, architecture, capability, verification, diversity, and filtering dimensions (\S\ref{sec:remediation}).
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "584c6143-018a-4414-8d66-6a5821050986",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "38a054c2-138d-4732-8113-27169d0190c8",
  "sourceToolAssistantUUID": "584c6143-018a-4414-8d66-6a5821050986",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T04:49:46.106Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EgwHuvxRMo44PdDdheUdfn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38a054c2-138d-4732-8113-27169d0190c8",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKmUcXAuNXpoM4sFBrt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37e9e6ce-846d-49ee-8ac8-e97beaeba03b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMQPo1M1wKyXucYjMWEXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6508,
      "cache_read_input_tokens": 37639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6508,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T04:49:46.111Z_

<details><summary>↩ Tool result · `toolu_01EgwHuvxRMo44PdDdheUdfn`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across seven instruction-tuned and reasoning-specialized models on four reasoning domains, with more than 2,400 evaluation instances.
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, and Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, DeepSeek-R1-Distill-Qwen-7B~\citep{guo2025deepseekr1}, and QwQ-32B~\citep{qwen2024qwq}. Parameter counts range from 7B to 32B.
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n=204$) provides formal logic problems with gold first-order logic (FOL) annotations for the oracle control (\S\ref{sec:oracle}). ProofWriter~\citep{tafjord2021proofwriter} ($n=600$) tests multi-step deductive reasoning at depth~5. LogiQA~\citep{liu2020logiqa} ($n=200$) evaluates logical reasoning from standardized examinations. StrategyQA~\citep{geva2021strategyqa} ($n=200$) covers commonsense multi-hop reasoning. GSM8K~\citep{cobbe2021gsm8k} ($n=30$) and AIME 2024 ($n=22$) serve as operating-regime probes for the degenerate case ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K=12$ traces at sampling temperature $T=0.7$. Constraint extraction at $T_{\text{ext}}=0.3$ (Appendix~\ref{app:prompts}). Z3~\citep{demoura2008z3} timeout: 10 seconds per problem. Penalty weight $\alpha = 0.5$ in all experiments.
14	
15	\paragraph{Metrics.} Accuracy (\%), $\Delta = \text{SICA} - \text{SC}$ in percentage points (pp). Statistical significance via McNemar exact test at $\alpha = 0.05$; 95\% bootstrap confidence intervals from 10{,}000 resamples for datasets with $n \geq 200$.
16	
17	
18	\subsection{Main Results: A Regime-Dependent Effect}
19	\label{sec:main-results}
20	
21	Table~\ref{tab:main_results} reports accuracy across all model-dataset conditions sorted by SC baseline. SICA effectiveness depends sharply on the model's baseline accuracy regime, with a narrow Goldilocks zone as the only region of significant positive effect.
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{SICA vs.\ SC across all conditions sorted by SC accuracy. $\Delta$ = SICA $-$ SC in percentage points. $^b$In-context learning with gold FOL examples. $\dagger$\,$n < 100$ (suggestive only). \textbf{Bold $\Delta$}: $p < 0.05$ (McNemar exact test). Significance: {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$.}
27	\label{tab:main_results}
28	\begin{tabular}{@{}llrrrrl@{}}
29	\toprule
30	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
31	\midrule
32	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
33	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.0095{**} \\
34	\midrule
35	\multicolumn{7}{l}{\textit{Goldilocks zone (SC $\sim$50--55\%)}} \\
36	Mistral-7B & LogiQA & 200 & 51.00 & 51.50 & $+$0.50 & 1.000 \\
37	Mistral-7B & FOLIO (s123) & 204 & 53.92 & 57.35 & $\mathbf{+3.43}$ & 0.039{*} \\
38	Mistral-7B & FOLIO (s42) & 204 & 54.41 & \textbf{59.31} & $\mathbf{+4.90}$ & 0.013{*} \\
39	Mistral-7B & FOLIO (s456) & 204 & 56.37 & 55.88 & $-$0.49 & 1.000 \\
40	\midrule
41	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
42	LLaMA-3.1-8B & FOLIO & 204 & 63.24 & 60.78 & $-$2.45 & 0.267 \\
43	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
44	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & n.s. \\
45	Qwen2.5-14B & FOLIO & 204 & 75.00 & 74.51 & $-$0.49 & n.s. \\
46	Qwen2.5-7B & FOLIO & 203 & 77.34 & 76.85 & $-$0.49 & 1.000 \\
47	Qwen2.5-14B & LogiQA & 200 & 78.50 & 78.00 & $-$0.50 & 1.000 \\
48	Qwen3-14B & FOLIO & 204 & 83.82 & \textbf{84.31} & $+$0.49 & n.s. \\
49	\midrule
50	\multicolumn{7}{l}{\textit{Degenerate ($C_0 < 5\%$)}} \\
51	QwQ-32B & AIME 2024$^\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \textrm{---} \\
52	Qwen2.5-14B & GSM8K$^\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \textrm{---} \\
53	\midrule
54	\multicolumn{7}{l}{\textit{Oracle upper bound (gold FOL/DSL + Z3)}} \\
55	Qwen2.5-14B & FOLIO & 204 & 75.49 & \textbf{89.71} & $\mathbf{+14.22}$ & $2.0{\times}10^{-7}${***} \\
56	Qwen2.5-14B & ProofWriter & 600 & 75.17 & \textbf{86.67} & $\mathbf{+11.50}$ & $9.21{\times}10^{-15}${***} \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	In the Goldilocks zone (SC $\sim$50--55\%), SICA provides significant gains on FOLIO. Mistral-7B achieves $\Delta = +4.90$\,pp ($p = 0.013$, McNemar $b = 12$, $c = 2$): 12 problems flip from incorrect to correct while only 2 flip in the reverse direction. A second seed replicates this effect at $\Delta = +3.43$\,pp ($p = 0.039$); the third seed shows no effect ($\Delta = -0.49$\,pp, $p = 1.0$; see \S\ref{sec:replication}). Mistral-7B on LogiQA (SC $= 51.00\%$), despite falling in the same SC range, yields only $\Delta = +0.50$\,pp ($p = 1.0$). Section~\ref{sec:failure-modes} attributes this to domain formalizability.
62	
63	\paragraph{Type A (SC $\geq$ $\sim$60\%): confirmation bias.} Seven conditions with SC $\geq 63\%$ (combined $N > 1{,}600$) produce $|\Delta| \leq 2.45$\,pp, all nonsignificant. Qwen2.5-14B on two powered datasets (FOLIO $n = 204$, LogiQA $n = 200$) yields $|\Delta| \leq 0.50$\,pp. Even in-context learning with gold FOL examples (SC $= 74.37\%$, $\Delta = +0.50$\,pp, $n = 199$) fails to break the pattern: improving extraction quality through exemplars does not overcome confirmation bias when the model already produces consistent traces. Qwen3-14B (SC $= 83.82\%$) represents a generational capability improvement yet produces $\Delta = +0.49$\,pp ($p > 0.05$).
64	
65	\paragraph{Type C (SC $\leq$ $\sim$40\%): error amplification.} Mistral-7B on ProofWriter depth-5 ($n = 600$, SC $= 39.33\%$) shows $\Delta = -2.83$\,pp ($p = 0.0095$): SICA \emph{significantly hurts} performance. Constraints extracted from predominantly incorrect traces encode wrong reasoning as formal rules, and the solver amplifies these errors rather than correcting them.
66	
67	\paragraph{Degenerate cases.} When $C_0 < 5\%$ (QwQ-32B on AIME 2024, Qwen2.5-14B on GSM8K), nearly all traces agree and SICA reduces to SC by construction. These probes confirm the $C_0$ diagnostic (\S\ref{sec:method}).
68	
69	Figure~\ref{fig:regime-scatter} visualizes the regime dependence. The Goldilocks zone is narrow: the upper boundary is sharp (LLaMA-3.1-8B on FOLIO at SC $= 63.24\%$ already shows $\Delta = -2.45$\,pp), and below $\sim$40\% SC, constraints transition from noisy to actively harmful. The oracle rows (bottom of Table~\ref{tab:main_results}) confirm that gold constraints yield $\Delta = +14.22$\,pp on FOLIO and $+11.50$\,pp on ProofWriter (both $p < 0.001$), establishing that the aggregation mechanism is sound when constraints are discriminative (\S\ref{sec:oracle}).
70	
71	\begin{figure}[t]
72	\centering
73	\includegraphics[width=\columnwidth]{f2_regime_scatter}
74	\caption{SICA $\Delta$ (pp) vs.\ SC baseline accuracy across all conditions. Filled markers: $n \geq 100$; open markers: $n < 100$. The Goldilocks zone (SC 50--55\%, shaded) contains the only significant positive effects. Type~A (SC $\geq$ 60\%): all nonsignificant ($|\Delta| \leq 2.45$\,pp). Type~C (SC $\leq$ 40\%): SICA significantly hurts ($\Delta = -2.83$\,pp, $p < 0.01$).}
75	\label{fig:regime-scatter}
76	\end{figure}
77	
78	
79	\subsection{Oracle Control: The Aggregation Mechanism Is Sound}
80	\label{sec:oracle}
81	
82	Oracle variants replace self-extracted constraints with gold annotations: FOL formulas from FOLIO ($n = 204$) and domain-specific logic (DSL) programs from ProofWriter ($n = 600$). The oracle evaluates gold constraints against each candidate answer via Z3 directly; the scoring function (Eq.~\ref{eq:score}) remains unchanged. This design functions as a causal intervention on constraint quality while holding the aggregation mechanism constant.
83	
84	Oracle-SICA achieves 89.71\% on FOLIO versus 75.49\% for SC ($\Delta = +14.22$\,pp, $p = 2.0 \times 10^{-7}$, McNemar $b = 29$, $c = 0$). Z3 agrees with gold labels on 95.1\% of FOLIO problems (194/204). On ProofWriter, Oracle-SICA reaches 86.67\% versus 75.17\% ($\Delta = +11.50$\,pp, $p = 9.21 \times 10^{-15}$), with Z3 gold agreement of 97.1\% (577/594). Relational subtypes benefit most: RelNeg $+17.86$\,pp and RelNoneg $+13.01$\,pp (Appendix Table~\ref{tab:pw_oracle_subtype}).
85	
86	These results establish two conclusions. First, the MAX-SAT aggregation mechanism is sound: given discriminative constraints, it produces large and highly significant gains. Second, the gap between self-extraction and oracle performance quantifies the independence bottleneck. Mistral-7B's best self-extracted result ($+4.90$\,pp) captures only 34.5\% of the FOLIO oracle ceiling ($+14.22$\,pp). The remaining 65.5\% is lost to self-extraction quality. Section~\ref{sec:failure-modes} decomposes this loss into three distinct failure modes.
87	
88	
89	\subsection{Three-Seed Replication}
90	\label{sec:replication}
91	
92	The Goldilocks result rests on Mistral-7B FOLIO performance, so we replicate with three random seeds to assess stability. All three runs use identical hyperparameters ($K = 12$, $T = 0.7$, $T_{\text{ext}} = 0.3$) on the full FOLIO evaluation set ($n = 204$).
93	
94	Seed~42 produces $\Delta = +4.90$\,pp ($p = 0.013$, SC $= 54.41\%$). Seed~123 replicates both the direction and significance at $\Delta = +3.43$\,pp ($p = 0.039$, SC $= 53.92\%$). Seed~456 shows no effect ($\Delta = -0.49$\,pp, $p = 1.0$, SC $= 56.37\%$). Two of three seeds reach significance at $\alpha = 0.05$; the mean effect across seeds is $\Delta = +2.61$\,pp.
95	
96	The variance is informative. Seed~456 produces a slightly higher SC baseline (56.37\% vs.\ 53.92--54.41\%) and no SICA gain, consistent with the regime-dependence pattern: as SC rises toward the upper boundary of the Goldilocks zone, the improvement vanishes. Sampling noise at the regime boundary can push individual seeds across the transition, which makes the effect fragile by design rather than by accident. This seed-level sensitivity motivates the entropy-conditioned analysis in \S\ref{sec:entropy}, where per-problem answer entropy reveals that the aggregate $\Delta$ is driven by the high-entropy subpopulation within each run.
97	
98	
99	\subsection{Failure Mode Analysis}
100	\label{sec:failure-modes}
101	
102	The regime-dependent pattern in Table~\ref{tab:main_results} reflects three distinct failure modes of self-extracted symbolic constraints.
103	
104	\paragraph{Type A: confirmation bias (SC $\geq$ $\sim$60\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\mathcal{C}^{\setminus}| \approx 0$), the penalty term in Eq.~\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in \S\ref{sec:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.
105	
106	\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean FOL formalization. Mistral-7B on LogiQA achieves an extraction rate of 86.4\% (fraction of traces yielding at least one parseable constraint), but the resulting constraints have a contradiction rate of only 0.8\%. Without genuine logical tension between constraints from different traces, MAX-SAT cannot discriminate among candidates. The condition sits in the Goldilocks SC range (51.00\%) yet produces $\Delta = +0.50$\,pp ($p = 1.0$), confirming that the right accuracy regime is necessary but not sufficient for SICA to help.
107	
108	\paragraph{Type C: error amplification (SC $\leq$ $\sim$40\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\Delta = -2.83$\,pp, $p = 0.0095$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.
109	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37e9e6ce-846d-49ee-8ac8-e97beaeba03b",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "16ad6d4f-16b2-497f-8af1-a3e38002be2f",
  "sourceToolAssistantUUID": "37e9e6ce-846d-49ee-8ac8-e97beaeba03b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T04:49:49.653Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VeiUSp23UKomHBsaoCJD6H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16ad6d4f-16b2-497f-8af1-a3e38002be2f",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKn9EyKMxMAsSvYmDg4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d010f453-fc4f-47cc-9193-f8ffb7422720",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1zbix5swDgfvWgCq1c96W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10309,
      "cache_read_input_tokens": 44147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10309,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T04:49:49.659Z_

<details><summary>↩ Tool result · `toolu_01VeiUSp23UKomHBsaoCJD6H`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	The regime-dependent pattern in \S\ref{sec:main-results} and the failure modes in \S\ref{sec:failure-modes} establish \emph{where} SICA succeeds and fails. This section investigates \emph{why}, through six quantitative lenses: trace correlation (\S\ref{sec:effective-k}), extraction quality (\S\ref{sec:extraction-taxonomy}), hyperparameter sensitivity (\S\ref{sec:k-sensitivity}, \S\ref{sec:t-sensitivity}), the entropy structure of gains (\S\ref{sec:entropy}), solver contribution (\S\ref{sec:ablation}), and remediation failure (\S\ref{sec:remediation}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	Table~\ref{tab:independence} reports Fleiss' $\kappa$ and the resulting Effective-K (Eq.~\ref{eq:effk}) across model-dataset conditions with $K = 12$ traces. $\kappa$ ranges from 0.21 to 0.82, and the resulting $K_{\text{eff}}$ spans $1.20\text{--}3.63$. The strongest model-dataset pair (Qwen2.5-14B on LogiQA, $\kappa = 0.82$) retains $K_{\text{eff}} = 1.20$: twelve traces carry barely more information than a single sample. Mistral-7B on FOLIO produces moderate agreement ($\kappa = 0.50$ for seed 42, $K_{\text{eff}} = 1.85$), consistent with its position in the Goldilocks zone. Mistral-7B on ProofWriter has the lowest agreement ($\kappa = 0.21$, $K_{\text{eff}} = 3.63$), yet SICA hurts ($\Delta = -2.83$\,pp) because trace quality is too low (SC $= 39.33\%$). High $K_{\text{eff}}$ alone does not guarantee improvement; the model must also produce sufficiently accurate traces. Qwen2.5-14B on FOLIO reaches 58.3\% unanimous problems and 63.0\% on LogiQA; Mistral-7B on FOLIO has only 14.2\%. Unanimous problems leave zero room for constraint-based reranking, and models with high unanimity rates offer SICA a vanishingly small operating window.
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{Trace independence metrics ($K = 12$). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). Unan.: unanimous-answer fraction (\%). $\Delta$: SICA $-$ SC (pp). Mistral s42/s123/s456 are separate random seeds on the same evaluation set. Mistral = Mistral-7B; Qwen2.5 = Qwen2.5-14B; Qwen3 = Qwen3-14B.}
15	\label{tab:independence}
16	\begin{tabular}{@{}llcccr@{}}
17	\toprule
18	Model & Domain & $\kappa$ & $K_{\text{eff}}$ & Unan. & $\Delta$ \\
19	\midrule
20	Mistral (s42) & FOLIO & 0.50 & 1.85 & 18.6 & $\mathbf{+4.90}$ \\
21	Mistral (s123) & FOLIO & 0.41 & 2.17 & 14.2 & $+$3.43 \\
22	Mistral (s456) & FOLIO & 0.40 & 2.22 & 14.2 & $-$0.49 \\
23	Mistral & PW-D5 & 0.21 & 3.63 & & $-$2.83 \\
24	Mistral & LogiQA & 0.50 & 1.84 & 20.5 & $+$0.50 \\
25	\addlinespace
26	Qwen2.5 (ICL) & FOLIO & 0.39 & 2.25 & & $+$0.50 \\
27	Qwen2.5 & FOLIO & 0.74 & 1.31 & 58.3 & $-$0.49 \\
28	Qwen2.5 & LogiQA & 0.82 & 1.20 & 63.0 & $-$0.50 \\
29	Qwen2.5 & PW-D5 & 0.62 & 1.53 & & \\
30	\addlinespace
31	Qwen3 & PW-D5 & 0.77 & 1.27 & & \\
32	\bottomrule
33	\end{tabular}
34	\end{table}
35	
36	Cross-seed comparison reveals the limits of $K_{\text{eff}}$ as a predictor. Mistral-7B's three FOLIO seeds produce $\kappa = 0.50$, $0.41$, $0.40$ ($K_{\text{eff}} = 1.85$, $2.17$, $2.22$), yet $\Delta$ is non-monotonic: the seed with the lowest $K_{\text{eff}}$ (s42, $1.85$) produces the largest gain ($+4.90$\,pp), while s456 ($K_{\text{eff}} = 2.22$) shows $\Delta = -0.49$\,pp. This non-monotonicity indicates that seed-level sampling variance, not trace independence alone, determines whether the constraint pool happens to contain discriminative information. Two conditions are jointly necessary: sufficient $K_{\text{eff}}$ (the Qwen conditions with $K_{\text{eff}} \leq 1.31$ never show positive $\Delta$) and sufficient SC accuracy (exp-046 with the highest $K_{\text{eff}} = 3.63$ but SC $= 39\%$ produces significant harm). The SC plateau remains explained by the correlation floor: beyond $K_{\text{eff}}$, additional traces are redundant.
37	
38	\subsection{Extraction Error Taxonomy}
39	\label{sec:extraction-taxonomy}
40	
41	Constraints must discriminate between candidate answers for MAX-SAT to produce a ranking different from majority vote. We measure discriminative power at two levels on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). At the source-trace level, 39.2\% of total constraint weight originates from traces whose answer differs from the plurality, but only 12.1\% of individual constraints fall into this minority category. At the Z3 semantic level, the picture is worse: only 8.2\% of constraints [95\% CI: 7.6, 8.8] are discriminative, producing different satisfiability outcomes when evaluated against different candidate answers.
42	
43	The primary mechanism behind this collapse is variable naming inconsistency. Each trace produces constraints with its own variable names, so Z3 treats identically-intended propositions as unrelated symbols. Among cross-answer constraint pairs, 56.4\% share zero Z3 variables, and the solver cannot detect logical relationships when constraints use disjoint symbol sets. Even when we filter the constraint pool to retain only the 8.2\% discriminative subset, accuracy does not improve. The discriminative constraints are too sparse and too weakly correlated with correctness to shift the MAX-SAT solution. The non-discriminative majority does not merely dilute the signal; the discriminative minority itself lacks the coherence to overcome noise.
44	
45	\subsection{K Sensitivity}
46	\label{sec:k-sensitivity}
47	
48	Figure~\ref{fig:k-sensitivity} shows SICA $\Delta$ as a function of the number of sampled traces $K$ for Mistral-7B on FOLIO ($n = 204$, seed 42). The relationship follows an inverted-U curve: $K = 4$ yields $\Delta = -1.47$\,pp, $K = 8$ yields $\Delta = -0.98$\,pp, $K = 12$ reaches the peak at $\Delta = +4.90$\,pp, and $K = 16$ drops to $\Delta = +1.47$\,pp. At low $K$, the constraint pool lacks diversity and MAX-SAT has too few clauses to produce a ranking different from SC. At high $K$, diminishing returns from non-independent traces (Eq.~\ref{eq:effk}) add redundant constraints without new discriminative information. The $K = 12$ peak reflects a transient balance between constraint diversity and trace independence, but even this optimum captures only 34.5\% of the oracle ceiling ($+14.22$\,pp). The narrow peak further constrains practical applicability: the best $K$ depends on the model-dataset condition and cannot be determined without labeled data.
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=\columnwidth]{f3_k_sensitivity}
53	\caption{SICA $\Delta$ (pp) vs.\ number of traces $K$ for Mistral-7B on FOLIO ($n = 204$, seed 42, $T = 0.7$). The inverted-U curve peaks at $K = 12$. Error bars: 95\% bootstrap CI.}
54	\label{fig:k-sensitivity}
55	\end{figure}
56	
57	\subsection{Temperature Sensitivity}
58	\label{sec:t-sensitivity}
59	
60	Raising the sampling temperature from $T = 0.7$ to $T = 1.0$ on Mistral-7B FOLIO ($n = 204$) collapses the SICA gain from $\Delta = +4.90$\,pp to $\Delta = +0.49$\,pp (SC $= 54.9\%$, SICA $= 55.4\%$, $p = 0.739$). Higher temperature increases output diversity but degrades trace quality. The net effect is that noisier traces produce noisier formalizations, and the quality loss outweighs any independence gain.
61	
62	\subsection{Entropy-Conditioned Mechanism}
63	\label{sec:entropy}
64	
65	Per-problem answer entropy (computed from the $K = 12$ trace answer distribution) reveals that SICA's aggregate $\Delta$ is driven by a specific subpopulation. On Mistral-7B FOLIO, the relationship is monotonic: low-entropy problems show $\Delta = 0$\,pp, medium-entropy problems show $\Delta \approx +4.5$\,pp, and high-entropy problems show $\Delta = +9.6$\,pp (full breakdown in Appendix Table~\ref{tab:entropy_conditioned}). SICA helps most where traces disagree most. The proportion of high-entropy problems determines the aggregate effect. Mistral-7B FOLIO has 35.8\% high-entropy problems, and the aggregate $\Delta = +4.90$\,pp. Qwen2.5-14B FOLIO has only 10.3\% high-entropy problems; SICA achieves $\Delta = +4.8$\,pp within that subgroup, but the aggregate $\Delta = -0.49$\,pp because the subpopulation is too small to shift overall accuracy. Qwen2.5-14B on LogiQA represents the extreme case: only 8.0\% of problems are high-entropy (75.0\% are low-entropy), and SICA produces $\Delta = +0.0$\,pp even within the high-entropy bin.
66	
67	This pattern explains the model-strength dependence observed in \S\ref{sec:main-results}. Stronger models produce more consistent traces, which compresses answer entropy, which shrinks the subpopulation where SICA can operate. The causal chain (strong model $\to$ consistent traces $\to$ low entropy $\to$ redundant constraints $\to$ no gain) bounds SICA's ceiling for high-accuracy models independent of extraction quality.
68	
69	\subsection{Constraint Ablation}
70	\label{sec:ablation}
71	
72	To test whether the Z3 solver contributes beyond simple vote counting, we compare four scoring methods on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). MAX-SAT achieves 76.49\% (615/804). Count-only (sum constraint weights per candidate without invoking Z3) achieves 76.62\% (616/804). Random-weight MAX-SAT achieves 75.87\% (610/804). The SC baseline achieves 76.24\% (613/804). MAX-SAT and count-only agree on 803 of 804 predictions. The Z3 solver adds nothing over simple counting. This confirms the degeneration in Eq.~\ref{eq:degenerate}: when only ${\sim}8$\% of constraints are semantically discriminative (\S\ref{sec:extraction-taxonomy}), the MAX-SAT objective reduces to a weighted vote count and SICA collapses to SC.
73	
74	\subsection{Remediation Analysis}
75	\label{sec:remediation}
76	\label{sec:interventions}
77	
78	We test nine remediation strategies spanning six intervention dimensions (full results in Appendix Table~\ref{tab:remediation}). \emph{Prompting}: contrastive prompting reduces the discriminative rate from 8.2\% to 6.0\% ($\Delta = -1.1$\,pp), and filtering to retain only discriminative constraints yields zero gain. \emph{Architecture}: cross-model extraction produces 0\% discriminative constraints ($\Delta = 0$\,pp). \emph{Capability}: generational scaling with Qwen3-14B yields $\Delta = +0.49$\,pp (n.s.). \emph{Verification}: Z3 feedback loops trigger UNSAT on only 0.9\% of problems with no real accuracy impact; cross-trace UNSAT checking finds 56.4\% of constraint pairs share zero variables, so logical verification is vacuous. \emph{Diversity}: raising temperature to $T = 1.0$ collapses $\Delta$ from $+4.90$\,pp to $+0.49$\,pp (\S\ref{sec:t-sensitivity}); multi-temperature sampling ($n = 204$) produces $\Delta = 0.00$\,pp (SC $= 57.84\%$, SICA $= 57.84\%$). \emph{Filtering}: consistency filtering (retaining constraints in $\geq 4$ traces) prunes aggressively (1.8 constraints per problem at threshold 4, 0.3 at threshold 8) and reverts to SC. All six dimensions fail. The independence bottleneck is structural: it cannot be resolved by prompt engineering, solver refinements, or diversity manipulations within the same-model self-extraction paradigm.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d010f453-fc4f-47cc-9193-f8ffb7422720",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "0ed89ef7-4e63-411b-b0c7-c0872dcc5b81",
  "sourceToolAssistantUUID": "d010f453-fc4f-47cc-9193-f8ffb7422720",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T04:49:50.617Z_

<details open><summary>🔧 Tool call — Read · `toolu_0166GpwYNHsq2swRNY5jqwWW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ed89ef7-4e63-411b-b0c7-c0872dcc5b81",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKn9EyKMxMAsSvYmDg4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b70a6528-66f6-45cb-8af8-a853b604969a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1zbix5swDgfvWgCq1c96W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10309,
      "cache_read_input_tokens": 44147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10309,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T04:49:50.620Z_

<details><summary>↩ Tool result · `toolu_0166GpwYNHsq2swRNY5jqwWW`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The oracle experiments causally isolate the failure source: replacing only the constraint source while holding all pipeline components fixed yields $+14.22$\,pp on FOLIO ($p = 2.0 \times 10^{-7}$) and $+11.50$\,pp on ProofWriter ($p = 9.21 \times 10^{-15}$). Aggregation is not the bottleneck; constraint extraction quality is. Three failure modes explain why self-extraction works only in a narrow band. Type A (SC $\geq$ $\sim$60\%): consistent traces produce constraints that mirror model answers. Confirmation bias reaches 62.3\% (Qwen2.5-14B), override precision drops to 28.6\%, and only 8.2\% of constraints are Z3-discriminative (95\% CI [7.6, 8.8]). Even ICL with gold FOL examples cannot break this pattern ($\Delta = +0.54$\,pp, n.s.), because the high-accuracy traces themselves lack the diversity that constraints need to exploit. Type C (SC $\leq$ $\sim$40\%): traces are predominantly wrong, so constraints encode incorrect reasoning as formal rules. The solver amplifies rather than corrects these errors ($\Delta = -4.67$\,pp on PW-D5). Type B: domains that resist FOL formalization yield non-discriminative constraints regardless of accuracy. The Goldilocks zone ($\sim$50--55\% SC) requires both sufficient diversity (traces disagree) and partial correctness (some constraints are right). Six remediation strategies all fail to widen this zone (\S\ref{sec:interventions}), confirming the boundaries are structural. Published methods achieving positive results \citep{xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} each introduce capabilities beyond the reasoning model itself; trained extractors and external provers remain viable paths to the oracle ceiling.
5	
6	For practitioners, $C_0$ and SC accuracy form a two-dimensional diagnostic. Low $C_0$ ($< 5\%$) indicates degenerate conditions. High $C_0$ with high SC ($\geq$ 60\%) activates the Type A trap. High $C_0$ with very low SC ($\leq$ 40\%) risks Type C harm. Only high $C_0$ with moderate SC ($\sim$50--55\%) is favorable, and even here self-extraction captures only 34.5\% of the oracle ceiling. Constraint extraction adds 48.7\% overhead; this cost is justified only in the Goldilocks zone \citep{snell2025scaling, loo2025reevaluating}.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b70a6528-66f6-45cb-8af8-a853b604969a",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "ffde83b0-82c6-4aef-be8e-31601983d4e4",
  "sourceToolAssistantUUID": "b70a6528-66f6-45cb-8af8-a853b604969a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T04:49:50.938Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CDSPc7w2zF8T6J5dtSDRKu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffde83b0-82c6-4aef-be8e-31601983d4e4",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKn9EyKMxMAsSvYmDg4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e68e3505-ff42-4e22-9d8b-153df973132e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1zbix5swDgfvWgCq1c96W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10309,
      "cache_read_input_tokens": 44147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10309,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T04:49:50.942Z_

<details><summary>↩ Tool result · `toolu_01CDSPc7w2zF8T6J5dtSDRKu`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluated SICA across seven models (7B--32B) on four reasoning domains ($N > 2{,}400$). Self-extracted constraints help only in a narrow Goldilocks zone ($\sim$50--55\% SC), with three failure modes outside it: confirmation bias at high accuracy (Type A, eight conditions, all n.s.), harmful noise at very low accuracy (Type C, $\Delta = -4.67$\,pp), and non-formalizable domains (Type B). Oracle experiments ($+14.22$\,pp FOLIO, $+11.50$\,pp ProofWriter) confirm aggregation works with discriminative constraints. Six remediation strategies, including ICL with gold FOL examples, all fail to widen this zone.
4	
5	For deployment, $C_0$ and SC accuracy form a two-dimensional diagnostic: low $C_0$ renders SICA degenerate; high $C_0$ with high SC triggers Type A; high $C_0$ with very low SC risks Type C; only moderate SC ($\sim$50--55\%) is favorable, capturing 34.5\% of the oracle ceiling. Trained extractors and external provers remain viable paths to close this gap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e68e3505-ff42-4e22-9d8b-153df973132e",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "128d57eb-b2a2-4455-b954-20c75e9a9d88",
  "sourceToolAssistantUUID": "e68e3505-ff42-4e22-9d8b-153df973132e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T04:49:51.237Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Sw2nhjADME325s27TH6iTC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "128d57eb-b2a2-4455-b954-20c75e9a9d88",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKn9EyKMxMAsSvYmDg4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a946ac91-348d-4d66-bb80-7d66ef77083b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1zbix5swDgfvWgCq1c96W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10309,
      "cache_read_input_tokens": 44147,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10309
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 307,
          "cache_read_input_tokens": 44147,
          "cache_creation_input_tokens": 10309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10309,
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

_source line 42 · 2026-05-19T04:49:51.240Z_

<details><summary>↩ Tool result · `toolu_01Sw2nhjADME325s27TH6iTC`</summary>

```text
1	Several limitations bound the scope of our conclusions. First, the oracle experiments cover two formal logic benchmarks (FOLIO $n = 204$, ProofWriter $n = 600$) that provide gold annotations; extending this analysis to commonsense or science domains requires constructing comparable gold constraint sets for those domains. Second, seven of our eleven model-domain conditions have $n \leq 60$, providing insufficient statistical power for confirmatory claims; power analysis shows that the minimum detectable effect exceeds 5\,pp for these conditions (Appendix Table~\ref{tab:power}), so they serve as regime characterization rather than definitive tests. Third, we do not compare against trained FOL extractors or cross-model extraction pipelines; our findings characterize the limitations of same-model self-extraction specifically. Fourth, all models tested range from 7B to 32B parameters; whether the capability trap persists at larger scales (70B+) remains an open question. Fifth, our extraction prompts use a single zero-shot template per domain; alternative prompting strategies (few-shot exemplars, chain-of-thought extraction, or iterative refinement) might yield higher-quality constraints, though the oracle gap suggests the bottleneck is fundamental rather than prompt-specific. Sixth, the constraint quality analysis (8.2\% Z3 semantic discriminative rate, 39.2\% source-trace discriminative rate) covers Qwen2.5-14B on the full FOLIO + ProofWriter dataset ($N = 804$); other model-domain combinations may exhibit different constraint characteristics. Seventh, constraint extraction uses $T_{\text{ext}} = 0.3$ while trace sampling uses $T = 0.7$; alternative extraction temperatures might yield different constraint characteristics, though our negative results suggest the bottleneck is semantic coupling rather than extraction diversity. Eighth, StrategyQA and ARC-Challenge use the mathematical extraction prompt rather than the logical one because their reasoning structure does not involve formal predicates or implications (Appendix~\ref{app:prompts}); a domain-specific commonsense extraction template might yield different constraint characteristics for these benchmarks. Ninth, although we prompt for FOL-style formalizations, the extracted constraints are predominantly propositional ground clauses without quantifiers (\S\ref{sec:constraint-extraction}); whether models capable of producing genuine quantified FOL would yield higher discriminative rates is untested. Tenth, deduplication uses syntactic equivalence, so semantically equivalent constraints with different surface forms receive separate weights, potentially inflating the apparent constraint pool without adding discriminative content. Eleventh, the GSM8K pilot ($n = 30$) is included to illustrate the constraint-absent failure regime and should not be interpreted as confirmatory evidence.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a946ac91-348d-4d66-bb80-7d66ef77083b",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "e46fe1c5-4c43-4392-af61-9f7064d17c93",
  "sourceToolAssistantUUID": "a946ac91-348d-4d66-bb80-7d66ef77083b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T04:49:54.377Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C78dq9pvMxKMbiw898antE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e46fe1c5-4c43-4392-af61-9f7064d17c93",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKnWFXYnDYdVNk4HiCq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "792711fd-2209-46ad-be65-7ad72425612b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VwwWNVKHZQunEyM5r8js8v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5932,
      "cache_read_input_tokens": 54456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5932,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T04:49:54.390Z_

<details><summary>↩ Tool result · `toolu_01C78dq9pvMxKMbiw898antE`</summary>

```text
1	
2	\section{Prompt Templates}
3	\label{app:prompts}
4	
5	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
6	
7	\paragraph{System Prompt.}
8	
9	\begin{lstlisting}
10	You are a constraint extraction tool. Output ONLY
11	valid JSON. Do NOT solve problems, reason about
12	correctness, or think step-by-step. Extract
13	constraints from the given trace exactly as stated.
14	\end{lstlisting}
15	
16	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
17	
18	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
19	
20	\begin{lstlisting}
21	Extract mathematical constraints from this reasoning
22	trace as a JSON object.
23	
24	Rules:
25	- type: "equation", "inequality", or "predicate"
26	- expression: human-readable, e.g. "x + y == 14"
27	- z3_formula: a single comparison expression in
28	  Python Z3 syntax
29	- source_step: step number where the constraint
30	  appears
31	- Use variable names from the trace
32	
33	z3_formula MUST follow these rules:
34	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
35	  /, **, %
36	- Use individual named variables: a1, a2, a3...
37	  NOT arrays a[1] or sets A
38	- Expand all sums explicitly:
39	  "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
40	- NO Python builtins: sum(), len(), max(), min(),
41	  list(), set(), range(), int()
42	- Each z3_formula must be exactly ONE comparison
43	  (==, !=, <, >, <=, >=)
44	- For multiple values, write separate constraints
45	  for each
46	
47	Output ONLY the JSON below, nothing else:
48	{"constraints": [{"type": "equation",
49	  "expression": "x + y == 14",
50	  "z3_formula": "x + y == 14",
51	  "source_step": 1}],
52	 "answer": "final_answer",
53	 "variables": ["x", "y"]}
54	
55	Trace:
56	{trace}
57	\end{lstlisting}
58	
59	\paragraph{Logical Constraint Extraction (LOGIC\_EXTRACTION\_PROMPT).}
60	
61	Used for ProofWriter and FOLIO datasets.
62	
63	\begin{lstlisting}
64	IMPORTANT: You are an EXTRACTION tool, NOT a problem
65	solver.
66	- Do NOT re-solve or re-reason about the problem.
67	- Do NOT verify whether the trace's reasoning is
68	  correct.
69	- ONLY extract the logical constraints that are
70	  explicitly stated or used in the trace below.
71	- Output ONLY the JSON object, nothing else.
72	
73	Extract logical constraints from this reasoning trace
74	about a logic problem.
75	
76	The problem has facts (base assertions), rules
77	(grounded implications), and derived conclusions.
78	Convert each into a Z3 boolean formula.
79	
80	Variable naming:
81	- Unary property: property_entity
82	  (e.g., kind_anne, red_charlie, round_fiona)
83	- Binary relation: relation_subject_object
84	  (e.g., eats_bear_squirrel, likes_lion_cat)
85	- Use lowercase with underscores only
86	
87	Constraint types:
88	- "fact": a given assertion,
89	  e.g., kind_anne == True
90	- "rule": a grounded implication over specific
91	  entities, e.g., Implies(kind_anne, nice_anne)
92	- "derived": an inferred conclusion from facts +
93	  rules, e.g., nice_anne == True
94	
95	Z3 operators:
96	- Implies(a, b) for if-then rules
97	- And(a, b, ...) for conjunctive conditions
98	- Or(a, b, ...) for disjunctive conditions
99	- Not(a) for negation
100	- == True / == False for boolean assertions
101	
102	Output ONLY the JSON below, nothing else:
103	{"constraints": [{"type": "fact",
104	  "expression": "kind(anne)",
105	  "z3_formula": "kind_anne == True",
106	  "source_step": 1}],
107	 "answer": "True or False or Unknown",
108	 "variables": ["kind_anne"]}
109	
110	Trace:
111	{trace}
112	\end{lstlisting}
113	
114	\paragraph{Output Schema.}
115	
116	Both prompts produce a JSON object with the following structure:
117	
118	\begin{lstlisting}
119	{
120	  "constraints": [
121	    {
122	      "type": "&lt;equation|inequality|predicate>
123	               or &lt;fact|rule|derived>",
124	      "expression": "&lt;human-readable description>",
125	      "z3_formula": "&lt;Z3-compatible expression>",
126	      "source_step": &lt;integer>
127	    }
128	  ],
129	  "answer": "&lt;final answer string>",
130	  "variables": ["&lt;var1>", "&lt;var2>", "..."]
131	}
132	\end{lstlisting}
133	
134	The pipeline additionally injects an \texttt{answer\_assertion} constraint per trace (not produced by the LLM):
135	
136	\begin{lstlisting}
137	{"type": "answer_assertion",
138	 "expression": "answer is &lt;ans>",
139	 "z3_formula": "__sica_answer_&lt;ans> == True",
140	 "source_step": -1}
141	\end{lstlisting}
142	
143	\paragraph{Prompt Selection Logic.}
144	
145	Domain assignment is determined by dataset: FOLIO and ProofWriter use \textsc{Logic\_Extraction\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \textsc{Extraction\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.
146	
147	
148	\section{Z3 MaxSAT Evaluation Pseudocode}
149	\label{app:z3-pseudocode}
150	
151	Algorithm~\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\ref{alg:scorer} describes the source-trace attribution scoring.
152	
153	Domain constraint variables (e.g., \texttt{x + y == 14}) and answer assertion variables (e.g., \texttt{\_\_sica\_answer\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.
154	
155	\begin{algorithm}[h]
156	\caption{Z3 Weighted Partial MAX-SAT}
157	\label{alg:maxsat}
158	\begin{algorithmic}[1]
159	\Require Deduplicated constraint set $\mathcal{C} = \{(c_m, w_m, S_m)\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices
160	\Ensure Partition $(\mathcal{C}^*, \mathcal{C}^{\setminus})$ where $\mathcal{C}^*$ is the max-weight satisfiable subset
161	\State $\textit{opt} \gets \textsc{Z3.Optimize()}$
162	\For{$m = 1, \ldots, M$}
163	    \State $b_m \gets$ fresh Boolean indicator
164	    \State $\textit{opt}.\textsc{Add}(b_m \Rightarrow c_m)$ \Comment{soft clause guarded by indicator}
165	    \State $\textit{opt}.\textsc{AddSoft}(b_m,\; \text{weight}=w_m)$
166	\EndFor
167	\State $\textit{result} \gets \textit{opt}.\textsc{Check}()$
168	\State $\textit{model} \gets \textit{opt}.\textsc{Model}()$
169	\State $\mathcal{C}^* \gets \{(c_m, w_m, S_m) : \textit{model}(b_m) = \top\}$
170	\State $\mathcal{C}^{\setminus} \gets \mathcal{C} \setminus \mathcal{C}^*$
171	\State \Return $(\mathcal{C}^*, \mathcal{C}^{\setminus})$
172	\end{algorithmic}
173	\end{algorithm}
174	
175	\begin{algorithm}[h]
176	\caption{Source-Trace Attribution Scoring}
177	\label{alg:scorer}
178	\begin{algorithmic}[1]
179	\Require Satisfied set $\mathcal{C}^*$, excluded set $\mathcal{C}^{\setminus}$, candidate answers $\mathcal{A}$, trace-answer mapping $\tau: \text{trace\_idx} \to a$, penalty weight $\alpha$
180	\Ensure Score $s(a)$ for each $a \in \mathcal{A}$
181	\For{each $a \in \mathcal{A}$}
182	    \State $T_a \gets \{i : \tau(i) = a\}$ \Comment{trace indices producing answer $a$}
183	    \State $\textit{pos}(a) \gets \sum_{(c,w,S) \in \mathcal{C}^*} w \cdot \mathbf{1}[S \cap T_a \neq \emptyset]$
184	    \State $\textit{neg}(a) \gets \sum_{(c,w,S) \in \mathcal{C}^{\setminus}} w \cdot \mathbf{1}[S \cap T_a \neq \emptyset]$
185	    \State $s(a) \gets \textit{pos}(a) - \alpha \cdot \textit{neg}(a)$
186	\EndFor
187	\State \Return $a^* = \arg\max_{a \in \mathcal{A}} s(a)$
188	\end{algorithmic}
189	\end{algorithm}
190	
191	
192	\section{Capability Trap Diagnostics}
193	\label{app:diagnostics}
194	
195	Table~\ref{tab:capability_trap} reports per-condition diagnostic metrics referenced in \S\ref{sec:entropy}.
196	
197	\begin{table}[h]
198	\centering
199	\small
200	\begin{tabular}{@{}llrrrr@{}}
201	\toprule
202	Model & Domain & $C_0$ (\%) & Extr.\ Rate & Contr.\ Rate & $\Delta$ (pp) \\
203	\midrule
204	Qwen2.5-14B & FOLIO & 35.3 & 0.89 & 0.022 & 0.00 \\
205	Qwen2.5-14B & ProofWriter & 39.2 & 0.89 & 0.022 & $+$0.33 \\
206	Qwen2.5-14B & StrategyQA$^\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\
207	Qwen2.5-14B & ARC-Chall.$^\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\
208	Qwen2.5-7B & FOLIO+PW$^\dagger$ & 42.1 & 0.94 & 0.027 & 0.00 \\
209	Mistral-7B & FOLIO+PW$^\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\
210	LLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\
211	LLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$2.45 \\
212	DeepSeek-R1-7B & FOLIO+PW$^\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\
213	QwQ-32B & Combined$^\dagger$ & 2.6 & --- & --- & 0.00 \\
214	Qwen2.5-14B & GSM8K$^\dagger$ & 13.3 & 0.15 & --- & 0.00 \\
215	\bottomrule
216	\end{tabular}
217	\caption{Capability trap diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable FOL constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\Delta$: SICA$-$SC gap (pp). $\dagger$: $n \leq 60$. Dashes indicate conditions where extraction diagnostics were not computed (StrategyQA uses boolean answers without FOL extraction; QwQ-32B Combined had near-zero $C_0$, making extraction analysis uninformative).}
218	\label{tab:capability_trap}
219	\end{table}
220	
221	
222	\section{Statistical Power Analysis}
223	\label{app:power}
224	
225	We compute the minimum detectable effect (MDE) for each condition at $\alpha = 0.05$ and 80\% power using exact binomial power calculations over McNemar discordant pairs. Table~\ref{tab:power} reports three grouped conditions with $n \geq 200$ (Qwen2.5-14B FOLIO and ProofWriter are pooled into a single $n{=}804$ analysis, corresponding to four Table~\ref{tab:main_results} rows), which constitute our confirmatory analyses. The remaining seven conditions ($n \leq 60$) yield infinite MDE due to insufficient discordant pairs and serve only as regime characterization.
226	
227	\begin{table}[h]
228	\centering
229	\small
230	\begin{tabular}{lrrrrr}
231	\toprule
232	\textbf{Condition} & $n$ & \textbf{MDE} & \textbf{Obs.\ $\Delta$} & \textbf{Obs.\ Pow.} \\
233	\midrule
234	Qwen-14B FOLIO+PW   & 804 & 1.86pp & $+$0.25pp & 5.7\%  \\
235	LLaMA-8B StrategyQA  & 200 & 4.64pp & $+$2.00pp & 20.6\% \\
236	LLaMA-8B FOLIO       & 204 & 4.84pp & $-$2.45pp & 18.6\% \\
237	\bottomrule
238	\end{tabular}
239	\caption{Power analysis for confirmatory conditions ($n \geq 200$). MDE = minimum detectable effect at 80\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\% in every case.}
240	\label{tab:power}
241	\end{table}
242	
243	The largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.
244	
245	
246	\section{Bootstrap Confidence Intervals}
247	\label{app:bootstrap}
248	
249	We compute 95\% confidence intervals for $\Delta(\text{SICA} - \text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\ref{tab:bootstrap} reports the results for the three confirmatory conditions.
250	
251	\begin{table}[h]
252	\centering
253	\small
254	\begin{tabular}{lrrl}
255	\toprule
256	\textbf{Condition} & $n$ & \textbf{Obs.\ $\Delta$} & \textbf{95\% CI} \\
257	\midrule
258	Qwen-14B FOLIO+PW   & 804 & $+$0.25pp & [$-$1.12, $+$1.62] \\
259	LLaMA-8B StrategyQA  & 200 & $+$2.00pp & [$-$1.50, $+$5.50] \\
260	LLaMA-8B FOLIO       & 204 & $-$2.45pp & [$-$5.88, $+$0.98] \\
261	\bottomrule
262	\end{tabular}
263	\caption{Bootstrap 95\% confidence intervals for $\Delta(\text{SICA} - \text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}
264	\label{tab:bootstrap}
265	\end{table}
266	
267	All three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that symbolic constraint aggregation improves over majority voting.
268	
269	
270	\section{Case Studies: Discordant Predictions}
271	\label{app:case-studies}
272	
273	Among 804 problems, SICA and SC agree on 773 (96.1\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability trap failures.
274	
275	\paragraph{Case 1: SICA Wins (folio\_134, FOLIO).}
276	
277	\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \emph{Conclusion}: Humans are mammals. \emph{Gold}: Unknown.
278	
279	The premises state that \emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing the weighted score for True-voting traces and tipping the aggregation to Unknown (correct). The excluded constraint likely captured an incorrect inference step (e.g., affirming the consequent) present only in True-voting traces. While SICA succeeds here, the success is coincidental: the excluded constraint happens to anti-correlate with the correct answer.
280	
281	\paragraph{Case 2: SC Wins (ProofWriter-1066\_Q6, ProofWriter).}
282	
283	\emph{Key chain}: White(Bob)$\to$Round(Bob) [white things are round] $\to$ Young(Bob) [all round things are young]. \emph{Conclusion}: ``Bob is not young.'' \emph{Gold}: False (Bob IS young).
284	
285	SC produces a 6:6 split (False:6, True:6) and tiebreaks to False (correct). SICA extracts 17 constraints; MaxSAT excludes 2 that appear preferentially in False-voting traces. These excluded constraints likely captured correct intermediate derivations (e.g., \texttt{young\_bob == True}) that appeared only in traces completing the full deduction chain. By excluding them, MaxSAT removes evidence supporting the correct answer. SICA selects True (wrong). This case illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the solver mistakenly penalizes.
286	
287	\paragraph{Case 3: Non-discriminative Constraints (ProofWriter-903\_Q6, ProofWriter).}
288	
289	\emph{Key chain}: Nice(Mouse)$\to$Cold(Mouse) [all nice people are cold] $\to$ Chases(Mouse,Mouse) [nice and cold $\to$ chase mouse]. \emph{Conclusion}: ``The mouse does not chase the mouse.'' \emph{Gold}: False.
290	
291	SC produces a 6:6 split (False:6, Unknown:6) and tiebreaks to False (correct). SICA extracts 44 constraints but excludes only 1 (2.3\%). The remaining 43 are domain facts and grounded rules (\texttt{nice\_mouse == True}, \texttt{Implies(nice\_mouse, cold\_mouse)}, etc.) that Z3 satisfies identically regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace completed the full derivation chain. The single excluded constraint carries negligible weight against 43 shared constraints, so SICA collapses to SC.
292	
293	\paragraph{Pattern.}
294	
295	These cases exemplify the general pattern across the 773 agreeing problems: the vast majority of extracted constraints encode shared domain structure rather than answer-specific reasoning, and MaxSAT aggregation degenerates to majority vote. Table~\ref{tab:case_summary} summarizes.
296	
297	\begin{table}[h]
298	\centering
299	\small
300	\caption{Summary of three representative discordant cases. All occur at exact 6:6 vote ties. Constraint exclusion can break ties in either direction (Cases 1--2) or have no effect (Case 3).}
301	\label{tab:case_summary}
302	\begin{tabular}{@{}lllcccc@{}}
303	\toprule
304	Case & ID & Gold & SC & SICA & \#Constr. & Excl.\ (\%) \\
305	\midrule
306	1 (SICA win) & folio\_134 & Unknown & True $\times$ & Unknown $\checkmark$ & 7 & 1 (14.3\%) \\
307	2 (SC win) & PW-1066\_Q6 & False & False $\checkmark$ & True $\times$ & 17 & 2 (11.8\%) \\
308	3 (Non-disc.) & PW-903\_Q6 & False & False $\checkmark$ & False $\checkmark$ & 44 & 1 (2.3\%) \\
309	\bottomrule
310	\end{tabular}
311	\end{table}
312	
313	
314	\section{ProofWriter Oracle Per-Subtype Analysis}
315	\label{app:pw-oracle-subtype}
316	
317	ProofWriter problems encode deductive rules as Domain-Specific Language (DSL) logic programs. Each problem uses one of four predicate subtypes: attribute predicates with or without negation (AttNeg, AttNoneg), and relation predicates with or without negation (RelNeg, RelNoneg). Relation predicates involve binary relations between entities (e.g., \texttt{eats(bear, squirrel)}), while attribute predicates assign unary properties (e.g., \texttt{kind(anne)}).
318	
319	The oracle pipeline parses these DSL annotations deterministically into Z3 formulas without any LLM involvement. Of the 600 ProofWriter problems, 594 (99.0\%) produce valid Z3 parses; the remaining 6 fail due to unsupported DSL constructs. Across all 7{,}128 trace-problem pairs submitted to Z3, the solver returns a result in every case (0\% solver errors). Z3 evaluations agree with ground-truth labels on 577 of 594 parseable problems (97.14\%), confirming that the deterministic DSL-to-Z3 translation faithfully preserves problem semantics.
320	
321	Table~\ref{tab:pw_oracle_subtype} reports the per-subtype breakdown. Relation-predicate subtypes show substantially larger gains than attribute-predicate subtypes: RelNeg improves by $+17.86$~pp and RelNoneg by $+13.01$~pp, compared to $+9.09$~pp for AttNoneg and $+6.87$~pp for AttNeg. Relation predicates involve longer reasoning chains with more intermediate entities, producing greater answer diversity across traces ($C_0$) and more opportunities for oracle constraints to correct errors.
322	
323	\begin{table}[h]
324	\centering
325	\caption{ProofWriter oracle experiment per-subtype breakdown. Oracle-SICA uses gold DSL annotations parsed deterministically to Z3 for consistency checking. Relation-predicate subtypes (RelNeg, RelNoneg) show larger gains than attribute-predicate subtypes; relation subtypes involve longer reasoning chains and benefit more from oracle constraints. Bold indicates best accuracy per row.}
326	\label{tab:pw_oracle_subtype}
327	\begin{tabular}{lcccc}
328	\toprule
329	Subtype & $n$ & SC Acc (\%) & Oracle Acc (\%) & $\Delta$ (pp) \\
330	\midrule
331	AttNoneg & 154 & 87.01 & \textbf{96.10} & +9.09 \\
332	AttNeg & 160 & 85.00 & \textbf{91.88} & +6.87 \\
333	RelNoneg & 146 & 66.44 & \textbf{79.45} & +13.01 \\
334	RelNeg & 140 & 60.00 & \textbf{77.86} & +17.86 \\
335	\midrule
336	Overall & 600 & 75.17 & \textbf{86.67} & +11.50 \\
337	\bottomrule
338	\end{tabular}
339	\end{table}
340	
341	
342	\section{Constraint Ablation Details}
343	\label{app:ablation}
344	
345	\begin{table}[h]
346	\centering
347	\small
348	\caption{Constraint ablation (Qwen2.5-14B, $n = 804$). Agreement: predictions identical to SC. MAX-SAT and count-only produce nearly identical predictions, confirming that self-extracted constraints carry no signal beyond vote counts.}
349	\label{tab:ablation}
350	\begin{tabular}{@{}lrc@{}}
351	\toprule
352	Aggregation & Acc.\ (\%) & Agreement w/ SC \\
353	\midrule
354	SC (majority vote) & 76.24 & --- \\
355	SICA (MAX-SAT) & 76.49 & 773\,/\,804 \\
356	Count-only & 76.62 & 774\,/\,804 \\
357	Random-weight & 75.87 & 764\,/\,804 \\
358	\bottomrule
359	\end{tabular}
360	\end{table}
361	
362	
363	\section{Remediation Strategy Details}
364	\label{app:remediation}
365	
366	\begin{table}[h]
367	\centering
368	\small
369	\caption{Six remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.00\%$, $\Delta = -0.49$\,pp. None reaches significance.}
370	\label{tab:remediation}
371	\begin{tabular}{@{}llrl@{}}
372	\toprule
373	Strategy & Target & $\Delta$ (pp) & Key finding \\
374	\midrule
375	Contrastive$^a$ & Prompt & $-$1.10 & disc.\ 6.0\% ($\downarrow$8.2\%) \\
376	Cross-model$^b$ & Self-ref. & 0.00 & disc.\ 0\% \\
377	Qwen3-14B$^c$ & Capability & $+$0.49 & $p = 0.655$ \\
378	Z3 feedback & Solver & --- & 0.9\% UNSAT trigger \\
379	Cons.\ filtering & Noise & 0.00 & $T{\geq}4 \to$ SC \\
380	Cross-trace UNSAT & Independence & --- & 56.4\% $\emptyset$ vars \\
381	\bottomrule
382	\end{tabular}\\[2pt]
383	{\footnotesize $^a$\,$n{=}182$ (extraction failures excluded). $^b$\,Mistral-7B extracts from Qwen2.5-14B traces. $^c$\,$n{=}204$, SC $= 83.82\%$.}
384	\end{table}
385	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "792711fd-2209-46ad-be65-7ad72425612b",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "0ad808cb-0eb6-46dc-85cb-5db9bbeba59b",
  "sourceToolAssistantUUID": "792711fd-2209-46ad-be65-7ad72425612b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-19T04:49:56.884Z_

Now let me also check the references file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ad808cb-0eb6-46dc-85cb-5db9bbeba59b",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKnk3EucwokB1K5AvED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c0fddeb-6cc1-4034-a35e-c8d6a7cfbc19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FRVB7zm2yZKLPqZxcMUKw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8129,
      "cache_read_input_tokens": 60388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8129,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 46 · 2026-05-19T04:49:58.499Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DGmf5mVDzS165Hs9isFHuQ`</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c0fddeb-6cc1-4034-a35e-c8d6a7cfbc19",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKnk3EucwokB1K5AvED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f285653f-3f07-46df-b9b1-8ebc248a002b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FRVB7zm2yZKLPqZxcMUKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8129,
      "cache_read_input_tokens": 60388,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 60388,
          "cache_creation_input_tokens": 8129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8129,
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

_source line 47 · 2026-05-19T04:49:58.519Z_

<details><summary>↩ Tool result · `toolu_01DGmf5mVDzS165Hs9isFHuQ`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f285653f-3f07-46df-b9b1-8ebc248a002b",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "7fe008f6-fc75-4177-8b73-2e4a2d7acfba",
  "sourceToolAssistantUUID": "f285653f-3f07-46df-b9b1-8ebc248a002b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-19T04:50:00.407Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YGvvcAoQN9vU6WFY32Bg1V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fe008f6-fc75-4177-8b73-2e4a2d7acfba",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKo37QQ7MpBXfD7Qarc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3853d2f-9b30-4bb1-a393-c97f942ecc25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5oq7GNjcRZkJUne6Ckh67",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 132,
      "cache_read_input_tokens": 68517,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 68517,
          "cache_creation_input_tokens": 132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 132,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T04:50:00.418Z_

<details><summary>↩ Tool result · `toolu_01YGvvcAoQN9vU6WFY32Bg1V`</summary>

```text
1	% References for SICA Capability Trap paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	%%% Theoretical Foundations %%%
5	
6	@book{condorcet1785,
7	  title={Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix},
8	  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},
9	  year={1785},
10	  publisher={Imprimerie Royale},
11	  address={Paris}
12	}
13	
14	@article{austensmith1996,
15	  title={Information Aggregation, Rationality, and the {C}ondorcet Jury Theorem},
16	  author={Austen-Smith, David and Banks, Jeffrey S.},
17	  journal={American Political Science Review},
18	  volume={90},
19	  number={1},
20	  pages={34--45},
21	  year={1996}
22	}
23	
24	@article{ladha1992correlated,
25	  title={The {C}ondorcet Jury Theorem, Free Speech, and Correlated Votes},
26	  author={Ladha, Krishna K.},
27	  journal={American Journal of Political Science},
28	  volume={36},
29	  number={3},
30	  pages={617--634},
31	  year={1992}
32	}
33	
34	@article{fleiss1971kappa,
35	  title={Measuring Nominal Scale Agreement Among Many Raters},
36	  author={Fleiss, Joseph L.},
37	  journal={Psychological Bulletin},
38	  volume={76},
39	  number={5},
40	  pages={378--382},
41	  year={1971}
42	}
43	
44	%%% Self-Consistency and Variants %%%
45	
46	@inproceedings{wang2023sc,
47	  title={Self-Consistency Improves Chain of Thought Reasoning in Language Models},
48	  author={Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
49	  booktitle={ICLR},
50	  year={2023}
51	}
52	
53	@inproceedings{chen2024usc,
54	  title={Universal Self-Consistency for Large Language Model Generation},
55	  author={Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
56	  booktitle={ICML},
57	  year={2024}
58	}
59	
60	@inproceedings{taubenfeld2025cisc,
61	  title={Confidence Improves Self-Consistency in {LLM}s},
62	  author={Taubenfeld, Asaf and Goldstein, Ido and Tsur, Oren},
63	  booktitle={ACL Findings},
64	  year={2025}
65	}
66	
67	@article{loo2025reevaluating,
68	  title={Reevaluating Self-Consistency Scaling in Multi-Agent Systems},
69	  author={Loo, Ryan and others},
70	  journal={arXiv preprint arXiv:2511.00751},
71	  year={2025}
72	}
73	
74	@inproceedings{li2023diverse,
75	  title={Making Language Models Better Reasoners with Step-Aware Verifier},
76	  author={Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},
77	  booktitle={ACL},
78	  year={2023}
79	}
80	
81	%%% Neuro-Symbolic Reasoning %%%
82	
83	@inproceedings{pan2023logiclm,
84	  title={Logic-{LM}: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning},
85	  author={Pan, Liangming and Alber, Alon and Xu, Wenhu and Deng, Yixin and Chen, Huan and Ji, Heng},
86	  booktitle={EMNLP Findings},
87	  year={2023}
88	}
89	
90	@inproceedings{olausson2023linc,
91	  title={{LINC}: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers},
92	  author={Olausson, Theo X. and Gu, Alex and Lipkin, Benjamin and Zhang, Cedegao E. and Solar-Lezama, Armando and Tenenbaum, Joshua B. and Levy, Roger},
93	  booktitle={EMNLP},
94	  year={2023}
95	}
96	
97	@inproceedings{xu2026dylos,
98	  title={Adaptive {LLM}-Symbolic Reasoning via Dynamic Logical Solver Composition ({DyLoS})},
99	  author={Xu, Lei and Beckmann, Pierre and Valentino, Marco and Freitas, Andre},
100	  booktitle={EACL},
101	  year={2026}
102	}
103	
104	@article{wang2025fover,
105	  title={{FoVer}: First-Order Logic Verification for Natural Language Reasoning},
106	  author={Wang, Yilun and others},
107	  journal={TACL},
108	  year={2025}
109	}
110	
111	@inproceedings{li2025aristotle,
112	  title={Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework},
113	  author={Li, Jundong and others},
114	  booktitle={ACL},
115	  year={2025}
116	}
117	
118	@article{luo2025logicagent,
119	  title={From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for {LLM} Logical Reasoning},
120	  author={Luo, Yiqi and others},
121	  journal={arXiv preprint arXiv:2509.24765},
122	  year={2025}
123	}
124	
125	%%% Test-Time Compute and Reasoning Models %%%
126	
127	@inproceedings{snell2025scaling,
128	  title={Scaling {LLM} Test-Time Compute Optimally Can be More Effective than Scaling Parameters},
129	  author={Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
130	  booktitle={ICLR (Oral)},
131	  year={2025}
132	}
133	
134	
135	@inproceedings{diverseaware2026,
136	  title={Diversity-Aware Training for Test-Time Scaling},
137	  author={Lyu, Bohan and Xu, Qixin and Zhu, Zihan and Wu, Yesai and Zhang, Zhong and Chen, Haotian and Cong, Xin and Liu, Xiaojiang and Liu, Zhiyuan and Sun, Maosong},
138	  booktitle={ICLR},
139	  year={2026}
140	}
141	
142	%%% Verification and Reranking %%%
143	
144	@article{cobbe2021gsm8k,
145	  title={Training Verifiers to Solve Math Word Problems},
146	  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
147	  journal={arXiv preprint arXiv:2110.14168},
148	  year={2021}
149	}
150	
151	@inproceedings{lightman2024prm,
152	  title={Let's Verify Step by Step},
153	  author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
154	  booktitle={ICLR},
155	  year={2024}
156	}
157	
158	@inproceedings{wang2024mathshepherd,
159	  title={Math-Shepherd: Verify and Reinforce {LLM}s Step-by-step without Human Annotations},
160	  author={Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, R.X. and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Y. and Sui, Zhifang},
161	  booktitle={ACL},
162	  year={2024}
163	}
164	
165	@inproceedings{hosseini2024vstar,
166	  title={{V-STaR}: Training Verifiers for Self-Taught Reasoners},
167	  author={Hosseini, Arian and Yuan, Xingdi and Malber, Nikolay and Courville, Aaron and Agarwal, Rishabh and Sordoni, Alessandro},
168	  booktitle={NeurIPS},
169	  year={2024}
170	}
171	
172	%%% Constraint Satisfaction in NLP %%%
173	
174	@inproceedings{satbench2025,
175	  title={{SATBench}: Benchmarking {LLM}s' Logical Reasoning via Automated Puzzle Generation from {SAT} Formulas},
176	  author={Wei, Anjiang and Wu, Yuheng and Wan, Yingjia and Suresh, Tarun and Tan, Huanmi and Zhou, Zhanke and Koyejo, Sanmi and Wang, Ke and Aiken, Alex},
177	  booktitle={EMNLP},
178	  year={2025}
179	}
180	
181	@inproceedings{llmmeets_cp2025,
182	  title={Large Language Model Meets Constraint Propagation},
183	  author={Bonlarron, Alexandre and R\'{e}gin, Florian and {De Maria}, Elisabetta and R\'{e}gin, Jean-Charles},
184	  booktitle={IJCAI},
185	  year={2025}
186	}
187	
188	%%% Debate and Multi-Agent %%%
189	
190	@article{liang2023encouraging,
191	  title={Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate},
192	  author={Liang, Tian and He, Zhiwei and Jiao, Wenxiang and Wang, Xing and Wang, Yan and Wang, Rui and Yang, Yujiu and Tu, Zhaopeng and Shi, Shuming},
193	  journal={arXiv preprint arXiv:2305.19118},
194	  year={2023}
195	}
196	
197	@inproceedings{du2023improving,
198	  title={Improving Factuality and Reasoning in Language Models through Multiagent Debate},
199	  author={Du, Yilun and Li, Shuang and Torralba, Antonio and Tenenbaum, Joshua B. and Mordatch, Igor},
200	  booktitle={ICML},
201	  year={2024}
202	}
203	
204	%%% Benchmarks and Datasets %%%
205	
206	@article{han2022folio,
207	  title={{FOLIO}: Natural Language Reasoning with First-Order Logic},
208	  author={Han, Simeng and Schoelkopf, Hailey and Zhao, Yilun and Qi, Zhenting and Riddell, Martin and Benson, Luke and Sun, Lucy and Zubova, Ekaterina and Qiao, Yujie and Burtell, Matthew and Peng, David and Fan, Jonathan and Liu, Yi and Wong, Brian and Sailor, Malcolm and Ni, Ansong and Nan, Linyong and Kasai, Jungo and Yu, Tao and Zhang, Rui and Joty, Shafiq and Fabbri, Alexander R. and Kryscinski, Wojciech and Lin, Xi Victoria and Xiong, Caiming and Radev, Dragomir},
209	  journal={arXiv preprint arXiv:2209.00840},
210	  year={2022}
211	}
212	
213	@inproceedings{tafjord2021proofwriter,
214	  title={{ProofWriter}: Generating Implications, Proofs, and Abductive Statements over Natural Language},
215	  author={Tafjord, Oyvind and Dalvi, Bhavana and Clark, Peter},
216	  booktitle={ACL Findings},
217	  year={2021}
218	}
219	
220	@article{geva2021strategyqa,
221	  title={Did {Aristotle} Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies},
222	  author={Geva, Mor and Khashabi, Daniel and Segal, Elad and Khot, Tushar and Roth, Dan and Berant, Jonathan},
223	  journal={TACL},
224	  year={2021}
225	}
226	
227	@inproceedings{liu2020logiqa,
228	  title={{LogiQA}: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning},
229	  author={Liu, Jian and Cui, Leyang and Liu, Hanmeng and Huang, Dandan and Wang, Yile and Zhang, Yue},
230	  booktitle={IJCAI},
231	  pages={3622--3628},
232	  year={2020}
233	}
234	
235	%%% Negative Results / Analysis Papers %%%
236	
237	@inproceedings{stechly2025selfverification,
238	  title={On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks},
239	  author={Stechly, Kaya and Valmeekam, Karthik and Kambhampati, Subbarao},
240	  booktitle={ICLR},
241	  year={2025}
242	}
243	
244	@inproceedings{valmeekam2023planning,
245	  title={On the Planning Abilities of Large Language Models -- A Critical Investigation},
246	  author={Valmeekam, Karthik and Marquez, Matthew and Sreedharan, Sarath and Kambhampati, Subbarao},
247	  booktitle={NeurIPS},
248	  year={2023}
249	}
250	
251	@inproceedings{kambhampati2024position,
252	  title={Position: {LLMs} Can't Plan, But Can Help Planning in {LLM}-Modulo Frameworks},
253	  author={Kambhampati, Subbarao and Valmeekam, Karthik and Guan, Lin and Verma, Mudit and Stechly, Kaya and Bhambri, Siddhant and Saldyt, Lucas Paul and Murthy, Anil B.},
254	  booktitle={ICML},
255	  year={2024}
256	}
257	
258	@inproceedings{huang2024selfcorrect,
259	  title={Large Language Models Cannot Self-Correct Reasoning Yet},
260	  author={Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},
261	  booktitle={ICLR},
262	  year={2024}
263	}
264	
265	@article{mirzadeh2024gsmsymbolic,
266	  title={{GSM-Symbolic}: Understanding the Limitations of Mathematical Reasoning in Large Language Models},
267	  author={Mirzadeh, Iman and Alizadeh, Keivan and Shahrokhi, Hooman and Tuzel, Oncel and Bengio, Samy and Farajtabar, Mehrdad},
268	  journal={arXiv preprint arXiv:2410.05229},
269	  year={2024}
270	}
271	
272	%%% Model Papers %%%
273	
274	@article{yang2024qwen25,
275	  title={Qwen2.5 Technical Report},
276	  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Wang, Bo and others},
277	  journal={arXiv preprint arXiv:2412.15115},
278	  year={2024}
279	}
280	
281	@article{jiang2023mistral,
282	  title={Mistral 7{B}},
283	  author={Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and de las Casas, Diego and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and Lavaud, L{\'e}lio Renard and Lachaux, Marie-Anne and Stock, Pierre and Scao, Teven Le and Lavril, Thibaut and Wang, Thomas and Lacroix, Timoth{\'e}e and El Sayed, William},
284	  journal={arXiv preprint arXiv:2310.06825},
285	  year={2023}
286	}
287	
288	@article{dubey2024llama3,
289	  title={The {Llama} 3 Herd of Models},
290	  author={Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and others},
291	  journal={arXiv preprint arXiv:2407.21783},
292	  year={2024}
293	}
294	
295	@article{guo2025deepseekr1,
296	  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLM}s via Reinforcement Learning},
297	  author={Guo, Daya and Yang, Dejian and Zhang, He and Song, Junxiao and others},
298	  journal={arXiv preprint arXiv:2501.12948},
299	  year={2025}
300	}
301	
302	@misc{qwen2024qwq,
303	  title={{QwQ}: Reflect Deeply on the Boundaries of the Unknown},
304	  author={{Qwen Team}},
305	  year={2024},
306	  howpublished={Technical Blog},
307	  note={\url{https://qwenlm.github.io/blog/qwq-32b-preview/}}
308	}
309	
310	%%% Oracle/Upper-Bound Experiments %%%
311	
312	@inproceedings{press2023compositionality,
313	  title={Measuring and Narrowing the Compositionality Gap in Language Models},
314	  author={Press, Ofir and Zhang, Muru and Min, Sewon and Schmidt, Ludwig and Smith, Noah A. and Lewis, Mike},
315	  booktitle={Findings of EMNLP},
316	  year={2023}
317	}
318	
319	@inproceedings{trivedi2023ircot,
320	  title={Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions},
321	  author={Trivedi, Harsh and Balasubramanian, Niranjan and Khot, Tushar and Sabharwal, Ashish},
322	  booktitle={ACL},
323	  year={2023}
324	}
325	
326	@inproceedings{saparov2023greedy,
327	  title={Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought},
328	  author={Saparov, Abulhair and He, He},
329	  booktitle={ICLR},
330	  year={2023}
331	}
332	
333	%%% Reasoning-Aware SC Variants %%%
334	
335	@article{wan2024rasc,
336	  title={Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient {LLM} Sampling},
337	  author={Wan, Guangya and Wu, Yuqi and Chen, Jie and Li, Sheng},
338	  journal={arXiv preprint arXiv:2408.17017},
339	  year={2024}
340	}
341	
342	@article{kim2026reasc,
343	  title={Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
344	  author={Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
345	  journal={arXiv preprint arXiv:2601.02970},
346	  year={2026}
347	}
348	
349	%%% Self-Refinement %%%
350	
351	@inproceedings{madaan2023selfrefine,
352	  title={Self-Refine: Iterative Refinement with Self-Feedback},
353	  author={Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},
354	  booktitle={NeurIPS},
355	  year={2023}
356	}
357	
358	%%% LLM Formalization %%%
359	
360	@article{amonkar2025realitycheck,
361	  title={A Reality Check of Language Models as Formalizers on Constraint Satisfaction Problems},
362	  author={Amonkar, Rikhil and Kayan, Ceyhun Efe and Lai, Qimei and Le Bras, Ronan and Zhang, Li},
363	  journal={arXiv preprint arXiv:2505.13252},
364	  year={2025}
365	}
366	
367	@article{nsvif2026,
368	  title={Neuro-Symbolic Verification on Instruction Following of {LLM}s},
369	  author={Su, Yiheng and Zhao, Guanqun and Li, Jiawei and Li, Yue and Fang, Mengdi and others},
370	  journal={arXiv preprint arXiv:2601.17789},
371	  year={2026}
372	}
373	
374	@inproceedings{xu2026logicreward,
375	  title={{LogicReward}: Incentivizing {LLM} Reasoning via Step-Wise Logical Supervision},
376	  author={Xu, Jundong and Fei, Hao and Zhou, Huichi and Quan, Xin and Huang, Qijun and Wu, Shengqiong and Wang, William Yang and Lee, Mong-Li and Hsu, Wynne},
377	  booktitle={ICLR},
378	  year={2026}
379	}
380	
381	%%% Tools and Solvers %%%
382	
383	@inproceedings{demoura2008z3,
384	  title={{Z3}: An Efficient {SMT} Solver},
385	  author={de Moura, Leonardo and Bj{\o}rner, Nikolaj},
386	  booktitle={TACAS},
387	  year={2008}
388	}
389	
390	%%% Condorcet / Voting Theory %%%
391	
392	@article{lefort2024condorcet_llm,
393	  title={Examining Independence in Ensemble Sentiment Analysis: A Study on the Limits of Large Language Models Using the {Condorcet} Jury Theorem},
394	  author={Lefort, Baptiste and Benhamou, Eric and Ohana, Jean-Jacques and Guez, Beatrice and Saltiel, David and Jacquot, Thomas},
395	  journal={arXiv preprint arXiv:2409.00094},
396	  year={2024}
397	}
398	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3853d2f-9b30-4bb1-a393-c97f942ecc25",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "7a5d4157-7597-4180-903f-a023c122a5fc",
  "sourceToolAssistantUUID": "f3853d2f-9b30-4bb1-a393-c97f942ecc25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-19T04:50:02.757Z_

Now let me also read the latest dream review report to understand how internal reviewers have assessed the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a5d4157-7597-4180-903f-a023c122a5fc",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKoBThXYy4BtDfG62k6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5d83394-652a-4fc8-ae10-c8c9cfb3d3a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013weoPdaCrqzyAfaSaciGvA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6843,
      "cache_read_input_tokens": 68517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6843,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T04:50:05.629Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S54EM2ueHGSr6w92NthuGL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/best/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5d83394-652a-4fc8-ae10-c8c9cfb3d3a1",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKoBThXYy4BtDfG62k6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acbf5e33-6dec-4a22-86a6-3ae244227b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013weoPdaCrqzyAfaSaciGvA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6843,
      "cache_read_input_tokens": 68517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6843,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T04:50:05.633Z_

<details><summary>↩ Tool result · `toolu_01S54EM2ueHGSr6w92NthuGL`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{url}
13	\usepackage{hyperref}
14	
15	\newcommand{\effk}{\text{Eff-K}}
16	\newcommand{\sica}{\textsc{Sica}}
17	\newcommand{\scm}{\textsc{SC}}
18	\newcommand{\fleiss}{Fleiss' $\kappa$}
19	
20	\title{Beyond Self-Consistency: How Trace Independence\\Limits Symbolic Consensus in LLM Reasoning}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	Self-consistency (SC) improves Large Language Model (LLM) reasoning by sampling multiple chain-of-thought traces and selecting the majority answer. Recent work proposes symbolic augmentation: extracting first-order logic (FOL) constraints from traces and aggregating them via MAX-SAT solvers. We present a systematic evaluation of Symbolic Invariant Consensus Aggregation (SICA) across 5 model families, 6 datasets, and over 1,300 problems. We find that SICA produces a real but fragile effect: statistically significant gains (+4.9 percentage points, $p$=0.013) appear only under narrow conditions (Mistral-7B, FOLIO, $T$=0.7, $K$=12), while all other configurations yield zero or negative gains. Through the lens of the Condorcet Jury Theorem, we show that same-model traces are highly correlated (Fleiss' $\kappa$ = 0.21--0.82), reducing an ensemble of $K$=12 nominal traces to an effective size of 1.2--3.6 independent voters. Oracle constraints confirm the aggregation mechanism works (+14.2pp), localizing the failure to self-extraction. Nine targeted remediation strategies, spanning prompting, architecture, diversity, and filtering, all fail to close this gap. We propose a dual bottleneck framework characterizing the joint requirements on trace independence and base accuracy, and provide a zero-cost diagnostic (C0+SC) for predicting when symbolic aggregation will help.
29	\end{abstract}
30	
31	\section{Introduction}
32	
33	Sampling multiple reasoning traces and selecting the majority answer, known as self-consistency \cite{wang2023selfconsistency}, is one of the most effective test-time strategies for improving LLM reasoning. The approach is simple: generate $K$ chain-of-thought traces at nonzero temperature, extract the final answer from each, and take the plurality vote. SC has become a standard component in reasoning pipelines, with gains of 5--15 percentage points on mathematical and logical benchmarks.
34	
35	A natural extension is to go beyond answer-level voting by extracting richer symbolic structure from each trace and aggregating at the constraint level. Systems like Logic-LM \cite{pan2023logiclm}, LINC \cite{olausson2023linc}, and more recent work such as DyLoS and Aristotle have explored various forms of neuro-symbolic integration where FOL formulas extracted from natural language reasoning are verified or aggregated using formal solvers. The appeal is clear: symbolic constraints should capture fine-grained reasoning dependencies that majority voting discards.
36	
37	We investigate whether this appeal translates to empirical gains in the specific setting of \emph{same-model self-extraction}, where a single LLM both generates the reasoning traces and provides the FOL constraints. This is the most practical deployment scenario, requiring no external verifier or separately trained extractor, but it introduces a critical confound: the constraints inherit the same biases as the traces they are extracted from.
38	
39	Our analysis reveals a fundamental limitation rooted in the Condorcet Jury Theorem \cite{condorcet1785}. The theorem guarantees that majority voting improves with more voters, but only if voters are independent and each is more likely correct than not. Same-model traces violate both conditions in regime-dependent ways. We quantify trace independence using Fleiss' $\kappa$ and derive an effective ensemble size ($\effk = K / (1 + (K-1)\kappa)$) that captures the true information content of $K$ correlated traces. Across our experiments, $\effk$ ranges from 1.18 to 3.63 for nominal $K$=12, meaning most of the sampling budget is wasted on redundant traces.
40	
41	Through systematic experiments across five model families (Qwen-7B/14B/72B, Qwen3-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B), six benchmarks (FOLIO, ProofWriter, StrategyQA, ARC-Challenge, GSM8K, and a combined diagnostic set D012), and nine remediation strategies, we establish a \emph{dual bottleneck} framework: SICA gains require simultaneously sufficient trace independence ($\effk > 1.5$) and sufficient base accuracy (SC between 45\% and 60\%). Outside this narrow Goldilocks zone, symbolic aggregation either mirrors the model's own biases (high SC) or amplifies noise from incorrect traces (low SC).
42	
43	Our contributions are:
44	\begin{itemize}
45	\item A Condorcet-grounded analysis of trace independence in self-consistency, showing that $\effk \ll K$ due to high inter-trace correlation, with cross-model quantification via Fleiss' $\kappa$.
46	\item A dual bottleneck framework (independence $\times$ quality) that predicts SICA effectiveness across 12 experimental conditions with 11/12 directional accuracy ($R^2 = 0.72$).
47	\item Empirical evidence that the bottleneck is structural: nine remediation strategies targeting independence, extraction quality, and diversity all fail to close the oracle gap.
48	\item A K-sensitivity analysis revealing an inverted-U relationship between ensemble size and SICA gains, with the peak determined by the tradeoff between effective independence and confirmation bias accumulation.
49	\item A zero-cost deployment diagnostic (C0+SC) that predicts whether SICA will help before running the expensive extraction pipeline.
50	\end{itemize}
51	
52	\section{Related Work}
53	
54	\paragraph{Self-Consistency and Extensions.}
55	Wang et al. \cite{wang2023selfconsistency} introduced self-consistency as a decoding strategy that samples diverse reasoning paths and marginalizes over them via majority voting. Subsequent work has explored extensions: Universal Self-Consistency \cite{chen2023usc} generalizes to free-form answers, while Taubenfeld et al. \cite{taubenfeld2025weighted} investigate weighted voting schemes. Li et al. \cite{li2023diverse} propose DiVeRSe, which combines diverse prompting with verification. Loo et al. \cite{loo2025scaling} show that SC gains plateau with increasing $K$, motivating the search for richer aggregation methods. Our work explains this plateau through the independence lens: additional traces beyond the effective ensemble size provide diminishing returns.
56	
57	\paragraph{Neuro-Symbolic Reasoning.}
58	Several systems combine LLM reasoning with formal logic. Logic-LM \cite{pan2023logiclm} translates problems to FOL and queries a solver; LINC \cite{olausson2023linc} uses in-context learning for FOL generation. More recent approaches include DyLoS, which trains domain-specific extractors, and Aristotle, which uses multi-step symbolic verification. FoVer \cite{fover2025} employs trained verifiers on formal representations. These systems differ from our setting in a crucial way: they use external verifiers or separately trained components. We focus specifically on same-model self-extraction, the simplest and most accessible deployment, and characterize why it fails.
59	
60	\paragraph{Condorcet Jury Theorem and LLM Ensembles.}
61	The Condorcet Jury Theorem \cite{condorcet1785,austensmith1996} establishes conditions under which majority voting aggregates information optimally. Recent work has begun applying this framework to LLM ensembles: notably, \cite{llmcjt2024} examine independence violations in cross-model sentiment analysis ensembles. Our work differs in two key dimensions: we analyze \emph{within-model} trace independence (not cross-model), and we connect the independence quantification directly to the failure mode of symbolic constraint aggregation. The Fleiss' $\kappa$ to Effective-K mapping provides a practical tool absent from prior analyses.
62	
63	\paragraph{Test-Time Compute and Verification.}
64	The test-time compute paradigm \cite{snell2025scaling} allocates additional inference budget for improved accuracy. Outcome reward models (ORM; \cite{cobbe2021gsm8k}) and process reward models (PRM; \cite{lightman2023prm}) score candidate solutions, while debate frameworks \cite{liang2023debate,du2023debate} use multi-agent interaction. Our analysis complements this line: we show that within the self-extraction paradigm, the bottleneck is not compute budget but trace independence.
65	
66	\section{Method}
67	
68	\subsection{Self-Consistency Baseline}
69	
70	Given a question $q$, self-consistency generates $K$ reasoning traces $\{t_1, \ldots, t_K\}$ by sampling from an LLM at temperature $T > 0$. Each trace yields an answer $a_i = \text{extract}(t_i)$, and the final prediction is the plurality vote: $\hat{a}_{\text{SC}} = \arg\max_a \sum_{i=1}^{K} \mathbf{1}[a_i = a]$.
71	
72	\subsection{Symbolic Invariant Consensus Aggregation}
73	
74	SICA extends SC by extracting first-order logic constraints from each trace and aggregating them via weighted MAX-SAT. The pipeline has three stages:
75	
76	\paragraph{Constraint Extraction.} For each trace $t_i$, a prompted LLM call extracts a set of FOL formulas $\mathcal{C}_i = \{c_{i,1}, \ldots, c_{i,m_i}\}$ that represent logical relationships stated or implied in the reasoning. Each constraint $c_{i,j}$ is a quantifier-free FOL formula over propositions corresponding to candidate answers.
77	
78	\paragraph{Constraint Aggregation.} All constraints across traces are pooled: $\mathcal{C} = \bigcup_i \mathcal{C}_i$. Each constraint receives a weight proportional to the number of traces from which it was independently extracted (or a unit weight if unique). The aggregation is formulated as a weighted partial MAX-SAT problem: find the truth assignment over candidate-answer propositions that maximizes the total weight of satisfied constraints.
79	
80	\paragraph{Answer Selection.} Each candidate answer $a$ is scored by fixing its corresponding proposition to true and computing the MAX-SAT objective. The SICA prediction is $\hat{a}_{\text{SICA}} = \arg\max_a \text{MAX-SAT}(\mathcal{C} \mid a)$.
81	
82	\subsection{Condorcet Independence Framework}
83	\label{sec:condorcet}
84	
85	The Condorcet Jury Theorem states that if $K$ independent voters each have probability $p > 0.5$ of being correct, the majority vote converges to certainty as $K \to \infty$. Two conditions must hold: (1) voter independence, and (2) individual competence ($p > 0.5$).
86	
87	We quantify the violation of condition (1) using Fleiss' $\kappa$, which measures inter-rater agreement beyond chance for $K$ raters and $n$ items. For $K$ traces on $n$ questions with $C$ answer categories:
88	\begin{equation}
89	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
90	\end{equation}
91	where $\bar{P}$ is the mean observed agreement and $\bar{P}_e$ is the expected agreement under independence.
92	
93	We define the \emph{effective ensemble size} as:
94	\begin{equation}
95	\effk = \frac{K}{1 + (K-1)\kappa}
96	\end{equation}
97	This formula, derived from the effective sample size in cluster sampling with intra-cluster correlation $\kappa$, captures the number of truly independent pieces of information in $K$ correlated traces. When $\kappa = 0$ (full independence), $\effk = K$; when $\kappa = 1$ (perfect agreement), $\effk = 1$.
98	
99	\subsection{Dual Bottleneck Framework}
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acbf5e33-6dec-4a22-86a6-3ae244227b88",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "00ca698c-17f1-43d1-bd13-1ed086e750ce",
  "sourceToolAssistantUUID": "acbf5e33-6dec-4a22-86a6-3ae244227b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T04:50:06.358Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GP3F3KZXtMGhyoKuAkTDvM`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00ca698c-17f1-43d1-bd13-1ed086e750ce",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKoBThXYy4BtDfG62k6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ff60c62-94d6-43da-b10a-ed8822f81ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013weoPdaCrqzyAfaSaciGvA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6843,
      "cache_read_input_tokens": 68517,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6843
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 234,
          "cache_read_input_tokens": 68517,
          "cache_creation_input_tokens": 6843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6843,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T04:50:06.370Z_

<details><summary>↩ Tool result · `toolu_01GP3F3KZXtMGhyoKuAkTDvM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/writing_plan.yaml\", \"content\": \"# Writing Plan — symb_invariant_consensus\\n# Generated: 2026-05-19T14:00:00Z\\n# Updated: 2026-05-19T16:00:00Z — D060: Method improvement failed → pure analysis paper\\n# Full Draft: Independence Bottleneck (Condorcet) — Analysis paper\\n# Paper Agent Step 1 output\\n\\nmeta:\\n  venue: EMNLP 2026\\n  track: main\\n  template: templates/latex/acl/\\n  template_note: \\\"ACL template shared by EMNLP; confirm 2026 style options when official EMNLP 2026 CFP releases\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  title: >\\n    Beyond Self-Consistency: How Trace Independence Limits\\n    Symbolic Consensus in LLM Reasoning\\n  core_claim: >\\n    Self-consistency's theoretical basis (Condorcet Jury Theorem) requires voter\\n    independence, but same-model sampling severely violates this assumption\\n    (Fleiss' κ = 0.21–0.82, Effective-K only 1.20–3.63 for nominal K=12). Oracle control\\n    (+14.22pp) proves the aggregation mechanism works, but self-extracted\\n    constraints capture only 35% of this ceiling. Nine remediation strategies\\n    spanning prompting, architecture, capability, verification, diversity, and\\n    filtering dimensions all fail, confirming the independence bottleneck is\\n    structural.\\n  paper_type: \\\"Analysis paper (Condorcet theoretical framework + empirical diagnosis + 9 remediation failures)\\\"\\n  framing: \\\"Independence Bottleneck (Condorcet)\\\"\\n  d060_note: \\\"Method improvement (multi-temp, filtering, T=1.0) all failed → pure analysis\\\"\\n  created_at: 2026-05-19T14:00:00Z\\n  updated_at: 2026-05-19T16:00:00Z\\n\\n# ──────────────────────────────────────────────\\n# Contributions (4 verified)\\n# ──────────────────────────────────────────────\\ncontributions:\\n  - id: C1\\n    label: \\\"Independence Bottleneck\\\"\\n    status: VERIFIED\\n    claim: >\\n      Condorcet Jury Theorem requires voter independence; same-model traces\\n      violate this (Mistral κ=0.50 Eff-K=1.85 [hero], Qwen κ=0.744 Eff-K=1.31).\\n      Range: κ=0.21–0.82, Eff-K=1.20–3.63. exp-046 has highest Eff-K (3.63)\\n      but SC too low (39%) → negative Δ. Cross-seed κ varies (0.50/0.41/0.40)\\n      but Δ non-monotonic with Eff-K → Eff-K is necessary but not sufficient.\\n    evidence: \\\"§5.1, Table 3, Figure 3\\\"\\n\\n  - id: C2\\n    label: \\\"Oracle Gap — Extraction Bottleneck\\\"\\n    status: VERIFIED\\n    claim: >\\n      Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7) FOLIO, +11.50pp PW. Self-extraction\\n      captures only 35% of oracle ceiling. Aggregation mechanism sound; extraction\\n      quality is the binding bottleneck.\\n    evidence: \\\"§4.3, Table 1 (oracle rows)\\\"\\n\\n  - id: C3\\n    label: \\\"Regime-Dependent Capability Trap\\\"\\n    status: VERIFIED\\n    claim: >\\n      SICA effectiveness depends on model accuracy regime: Type A (SC≥~60%,\\n      confirmation bias), Type B (non-formalizable domain), Type C (SC≤~40%,\\n      noisy constraints, Δ=-2.83pp p=0.0095). Goldilocks zone (~50–55% SC)\\n      yields only significant gain (+4.90pp, p=0.013, 2/3 seeds significant at α=0.05).\\n    evidence: \\\"§4.2, §4.4, §4.5, Table 1, Figure 2\\\"\\n\\n  - id: C4\\n    label: \\\"C0+SC Deployment Diagnostic + K/T Sensitivity\\\"\\n    status: VERIFIED\\n    claim: >\\n      C0 (multi-candidate rate) + SC accuracy forms zero-cost deployment diagnostic.\\n      K sensitivity shows inverted-U (K=12 sweet spot). T sensitivity shows effect\\n      fragility (T=0.7 +4.90pp → T=1.0 +0.55pp). Nine remediation strategies\\n      spanning all intervention dimensions fail, confirming structural bottleneck.\\n    evidence: \\\"§5.3, §5.4, §5.5, Figure 3, Appendix remediation table\\\"\\n\\n# ──────────────────────────────────────────────\\n# Paper Outline\\n# ──────────────────────────────────────────────\\npaper_outline:\\n  - section: abstract\\n    file: abstract.tex\\n    word_budget: 220\\n    phase: 2\\n    core_bullets:\\n      - \\\"Problem: SC (majority voting) plateaus; Condorcet Jury Theorem explains why — traces lack independence\\\"\\n      - \\\"Method: SICA pipeline, 7 models (7B–32B), 4 domains, N>2,400\\\"\\n      - \\\"Independence quantification: Fleiss' κ=0.21–0.82 → Eff-K=1.20–3.63 at K=12\\\"\\n      - \\\"Regime-dependent effect: +4.90pp Goldilocks zone (2/3 seeds significant), -2.83pp Type C, ~0 Type A\\\"\\n      - \\\"Oracle +14.22pp/+11.50pp proves aggregation sound\\\"\\n      - \\\"9 remediation strategies all fail — bottleneck is structural\\\"\\n      - \\\"K sensitivity: inverted-U (K=12 sweet spot); T sensitivity: fragile (T=0.7→T=1.0 collapses)\\\"\\n      - \\\"C0+SC deployment diagnostic\\\"\\n    dependencies: [experiments, analysis, method]\\n\\n  - section: introduction\\n    file: introduction.tex\\n    word_budget: 1300\\n    phase: 2\\n    core_bullets:\\n      - \\\"P1: Scaling test-time computation; SC as dominant aggregation; diminishing returns (Loo et al. 2025)\\\"\\n      - \\\"P2: Neuro-symbolic methods (Logic-LM, LINC, DyLoS, Aristotle, FoVer) show gains but use external/trained components. Can same-model self-extraction suffice?\\\"\\n      - \\\"P3: Theoretical lens — Condorcet Jury Theorem requires voter independence. Same-model traces violate this (Eff-K=1.20–3.63). Symbolic verification could inject independent signal, but self-extraction inherits trace non-independence.\\\"\\n      - \\\"P4: Our approach — SICA pipeline + Condorcet analysis + 7 models × 4 domains + 3-seed replication. Core finding: independence bottleneck. 9 remediation strategies all fail.\\\"\\n      - \\\"P5: Contributions (C1–C4)\\\"\\n    dependencies: [experiments, analysis, method]\\n    figures: [fig1_pipeline]\\n\\n  - section: related_work\\n    file: related_work.tex\\n    word_budget: 800\\n    phase: 1\\n    core_bullets:\\n      - \\\"Cluster 1: SC and extensions — SC, USC, weighted SC, DiVeRSe, scaling plateaus\\\"\\n      - \\\"Cluster 2: Neuro-symbolic reasoning — Logic-LM, LINC, DyLoS, Aristotle, FoVer, LogicAgent; key distinction: trained/external vs same-model self-extraction\\\"\\n      - \\\"Cluster 3: Test-time compute — Snell et al. 2025, DeepSeek-R1, diversity-aware TTS\\\"\\n      - \\\"Cluster 4: Verification and reranking — ORM, PRM, Math-Shepherd\\\"\\n      - \\\"Cluster 5: Condorcet/voting theory and ensemble diversity — Condorcet 1785, Austen-Smith & Banks 1996, arXiv:2409.00094 (closest prior work)\\\"\\n    dependencies: []\\n\\n  - section: method\\n    file: method.tex\\n    word_budget: 1200\\n    phase: 1\\n    subsections:\\n      - id: \\\"sec:condorcet\\\"\\n        title: \\\"Self-Consistency and the Condorcet Independence Assumption\\\"\\n        word_budget: 300\\n        bullets:\\n          - \\\"SC as majority voting; Condorcet Jury Theorem: K independent voters with p>0.5 → correct majority as K→∞\\\"\\n          - \\\"LLM traces violate independence: same model, same prompt, only sampling temperature\\\"\\n          - \\\"Eff-K = K / (1 + (K-1)·κ) where κ = Fleiss' Kappa — effective independent voter count\\\"\\n          - \\\"When Eff-K ≈ 1, additional traces provide no new information\\\"\\n      - id: \\\"sec:sica-pipeline\\\"\\n        title: \\\"SICA Pipeline\\\"\\n        word_budget: 450\\n        bullets:\\n          - \\\"K-trace generation at T=0.7\\\"\\n          - \\\"FOL constraint extraction at T_ext=0.3 (in practice: predominantly ground propositional clauses)\\\"\\n          - \\\"Syntactic deduplication\\\"\\n          - \\\"Weighted partial MAX-SAT: hard clauses (answer assertion), soft clauses (constraints weighted by occurrence)\\\"\\n          - \\\"Z3 solver, 10s timeout per candidate; answer with highest satisfiable subset selected\\\"\\n      - id: \\\"sec:oracle-design\\\"\\n        title: \\\"Oracle Control Design\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"Replace self-extracted constraints with gold FOL (FOLIO) / DSL (ProofWriter)\\\"\\n          - \\\"Z3 evaluates gold constraint against each candidate answer\\\"\\n          - \\\"Causal intervention: isolates constraint quality from aggregation mechanism\\\"\\n      - id: \\\"sec:scope\\\"\\n        title: \\\"Scope\\\"\\n        word_budget: 100\\n        bullets:\\n          - \\\"Same-model self-extraction pipeline\\\"\\n          - \\\"Methods using trained extractors / external provers out of scope\\\"\\n    dependencies: []\\n    figures: [fig1_pipeline]\\n\\n  - section: experiments\\n    file: experiments.tex\\n    word_budget: 1800\\n    phase: 1\\n    subsections:\\n      - id: \\\"sec:exp-setup\\\"\\n        title: \\\"Experimental Setup\\\"\\n        word_budget: 300\\n        bullets:\\n          - \\\"7 models: Qwen2.5-14B, Qwen2.5-7B, Qwen3-14B, Mistral-7B-v0.3, LLaMA-3.1-8B, DeepSeek-R1-Distill-7B, QwQ-32B\\\"\\n          - \\\"4 domains: FOLIO (n=204), ProofWriter (n=600), LogiQA (n=200), StrategyQA (n=200/60)\\\"\\n          - \\\"Probes: GSM8K (n=30), AIME 2024 (n=22)\\\"\\n          - \\\"K=12, T=0.7, T_ext=0.3, Z3 timeout 10s\\\"\\n          - \\\"Metrics: accuracy (%), Δ=SICA−SC (pp), McNemar exact test α=0.05, 95% bootstrap CIs\\\"\\n      - id: \\\"sec:main-results\\\"\\n        title: \\\"Main Results: A Regime-Dependent Effect\\\"\\n        word_budget: 450\\n        bullets:\\n          - \\\"Table 1: all conditions sorted by SC%, grouped by regime\\\"\\n          - \\\"Goldilocks zone (~50–55% SC): Mistral FOLIO +4.90pp p=0.013 (b=12,c=2)\\\"\\n          - \\\"Type A (SC≥~60%): 8+ conditions, all n.s., combined N>2,000\\\"\\n          - \\\"Type C (SC≤~40%): Mistral PW-600 Δ=-2.83pp p=0.0095 — SICA hurts\\\"\\n          - \\\"Degenerate: C0<5% (QwQ, GSM8K) → SICA≡SC\\\"\\n        data_source: \\\"registry: exp-033, exp-046, exp-041, exp-026, exp-035, exp-038, exp-020, exp-027, exp-019, exp-044b, exp-050b, exp-049b, exp-014, exp-017, exp-012, sica_aime30_v3\\\"\\n      - id: \\\"sec:oracle\\\"\\n        title: \\\"Oracle Control: Aggregation Is Sound\\\"\\n        word_budget: 300\\n        bullets:\\n          - \\\"FOLIO: oracle-SICA 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7, b=29, c=0)\\\"\\n          - \\\"ProofWriter: oracle-SICA 86.67% vs SC 75.17% (+11.50pp, p=9.21e-15)\\\"\\n          - \\\"Z3 gold agreement: 95.1% FOLIO, 97.1% PW\\\"\\n          - \\\"Best self-extraction captures 34.5% of oracle ceiling\\\"\\n        data_source: \\\"registry: exp-031, exp-022\\\"\\n      - id: \\\"sec:replication\\\"\\n        title: \\\"Three-Seed Replication\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"Mistral-7B FOLIO-204: seeds 42/123/456\\\"\\n          - \\\"Seed 42 (exp-033): Δ=+4.90pp p=0.013\\\"\\n          - \\\"Seed 123 (exp-052): Δ=+3.43pp p=0.039\\\"\\n          - \\\"Seed 456 (exp-053): Δ=-0.49pp p=1.0\\\"\\n          - \\\"2/3 seeds significant at α=0.05; mean Δ=+2.61pp\\\"\\n          - \\\"Variance across seeds highlights sensitivity to sampling → motivates independence analysis\\\"\\n        data_source: \\\"registry: exp-033, exp-052, exp-053\\\"\\n      - id: \\\"sec:failure-modes\\\"\\n        title: \\\"Failure Mode Analysis\\\"\\n        word_budget: 300\\n        bullets:\\n          - \\\"Type A: strong models → consistent traces → constraints mirror answers → MAX-SAT = counting\\\"\\n          - \\\"Type B: non-formalizable domain (LogiQA: extraction rate 86.4%, contradiction rate 0.8%)\\\"\\n          - \\\"Type C: wrong traces → wrong constraints → solver amplifies errors\\\"\\n    dependencies: []\\n    tables: [tab1_main_results]\\n    figures: [fig2_regime_scatter]\\n\\n  - section: analysis\\n    file: analysis.tex\\n    word_budget: 1500\\n    phase: 1\\n    subsections:\\n      - id: \\\"sec:effective-k\\\"\\n        title: \\\"Condorcet Effective-K Analysis\\\"\\n        word_budget: 350\\n        bullets:\\n          - \\\"Fleiss' κ per model-domain condition from K=12 trace answer distributions\\\"\\n          - \\\"Eff-K = K / (1 + (K-1)·κ)\\\"\\n          - \\\"Mistral FOLIO s42: κ=0.500, Eff-K=1.85 (hero); s123: κ=0.412, Eff-K=2.17; s456: κ=0.401, Eff-K=2.22\\\"\\n          - \\\"Mistral PW-600: κ=0.210, Eff-K=3.63 (highest Eff-K but SC=39% → negative Δ)\\\"\\n          - \\\"Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (most redundant)\\\"\\n          - \\\"Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (lowest Eff-K)\\\"\\n          - \\\"Cross-seed κ varies (0.50/0.41/0.40) but Δ non-monotonic with Eff-K → Eff-K necessary not sufficient; need both Eff-K AND SC in operating range\\\"\\n          - \\\"Correlation: higher Eff-K → more room for SICA gain\\\"\\n          - \\\"Explains SC plateau: adding traces beyond Eff-K provides no new information\\\"\\n        data_source: \\\"comp-1 Worker output (Fleiss' κ from per-problem trace data)\\\"\\n      - id: \\\"sec:extraction-taxonomy\\\"\\n        title: \\\"Extraction Error Taxonomy\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"Discriminative rate: ~8% Z3-discriminative (95% CI [7.6, 8.8])\\\"\\n          - \\\"Even removing non-discriminative constraints provides zero gain (filtering experiment)\\\"\\n          - \\\"Variable naming inconsistency: 56.4% constraint pairs share zero Z3 variables\\\"\\n          - \\\"Self-extraction captures ~18% of oracle quality\\\"\\n        data_source: \\\"registry: exp-023, exp-036b; filtering validation data\\\"\\n        note: \\\"D060: 43.1% trivially_satisfied number under review — use verified ~8% non-discriminative framing\\\"\\n      - id: \\\"sec:k-sensitivity\\\"\\n        title: \\\"K Sensitivity\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"Inverted-U curve: K=4 Δ=-1.47pp, K=8 Δ=-0.98pp, K=12 Δ=+4.90pp, K=16 Δ=+1.47pp\\\"\\n          - \\\"K=12 is sweet spot; K=4 SC ≈ K=12 SC but SICA differs by ~6.4pp\\\"\\n          - \\\"Proves SICA extracts different information than SC at sufficient K\\\"\\n          - \\\"Links to Eff-K: diminishing returns from non-independent traces\\\"\\n          - \\\"K=20 pending\\\"\\n        data_source: \\\"Director K sensitivity data; registry: exp-051\\\"\\n      - id: \\\"sec:t-sensitivity\\\"\\n        title: \\\"Temperature Sensitivity\\\"\\n        word_budget: 100\\n        bullets:\\n          - \\\"T=0.7: Δ=+4.90pp (exp-033); T=1.0: Δ=+0.55pp (exp-054)\\\"\\n          - \\\"Effect extremely fragile to temperature — higher T increases diversity but degrades trace quality\\\"\\n        data_source: \\\"registry: exp-033, exp-054\\\"\\n      - id: \\\"sec:entropy\\\"\\n        title: \\\"Entropy-Conditioned Mechanism\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"Per-problem answer entropy mediates SICA effectiveness\\\"\\n          - \\\"Mistral: low Δ=0, med Δ=+4.5, high Δ=+9.6pp (monotonic)\\\"\\n          - \\\"Proportion of high-entropy problems: Mistral 35.8% vs Qwen 10.3%\\\"\\n          - \\\"Causal chain: strong model → consistent traces → low entropy → redundant constraints\\\"\\n        data_source: \\\"registry: exp-033 per_entropy, exp-026\\\"\\n      - id: \\\"sec:ablation\\\"\\n        title: \\\"Constraint Ablation\\\"\\n        word_budget: 100\\n        bullets:\\n          - \\\"MAX-SAT vs count-only: 803/804 agree (Qwen-14B, n=804)\\\"\\n          - \\\"Self-extracted constraints carry no signal beyond vote counts in high-SC regime\\\"\\n        data_source: \\\"registry: sica_constraint_ablation_013\\\"\\n      - id: \\\"sec:remediation\\\"\\n        title: \\\"Remediation Analysis\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"9 strategies spanning 6 intervention dimensions, all fail:\\\"\\n          - \\\"  Prompting: contrastive extraction (exp-029: disc_rate 8.2%→6.0%, Δ=-1.1pp)\\\"\\n          - \\\"  Architecture: cross-model extraction (exp-030: 0% discriminative)\\\"\\n          - \\\"  Capability: generational scaling Qwen3 (exp-027: +0.49pp n.s.)\\\"\\n          - \\\"  Verification: Z3 feedback (exp-036: 0.9% UNSAT trigger), cross-trace UNSAT (exp-036b: 56.4% zero vars)\\\"\\n          - \\\"  Diversity: multi-temp sampling (n=28, Δ=0.00pp), T=1.0 (Δ=+0.55pp, collapse from +4.90pp)\\\"\\n          - \\\"  Filtering: discriminative constraint filtering (0 gain)\\\"\\n          - \\\"  Consistency: consistency filtering (exp-043: reverts to SC at T≥4)\\\"\\n          - \\\"All fail → independence bottleneck is structural, not addressable by prompt/solver/diversity interventions\\\"\\n          - \\\"1-paragraph summary in main text; full table in appendix\\\"\\n        data_source: \\\"registry: exp-029, exp-030, exp-027, exp-036, exp-043, exp-036b; D060 new data\\\"\\n    dependencies: [experiments]\\n    tables: [tab3_independence, tab4_extraction_taxonomy]\\n    figures: [fig3_k_sensitivity]\\n\\n  - section: discussion\\n    file: discussion.tex\\n    word_budget: 500\\n    phase: 2\\n    core_bullets:\\n      - \\\"Oracle causally isolates bottleneck: aggregation sound, extraction binding\\\"\\n      - \\\"Condorcet interpretation: Eff-K < 2 → constraints inherit trace non-independence\\\"\\n      - \\\"9 remediation failures confirm structural nature — not addressable by prompting, architecture, diversity, or filtering\\\"\\n      - \\\"Why published methods (DyLoS, Aristotle, FoVer) succeed: bypass same-model self-extraction\\\"\\n      - \\\"exp-050b complication: ICL changes trace generation characteristics, not just SC level\\\"\\n      - \\\"C0 × SC two-dimensional deployment diagnostic\\\"\\n      - \\\"Paths forward: trained extractors, external provers, multi-model pipelines\\\"\\n    dependencies: [experiments, analysis]\\n\\n  - section: conclusion\\n    file: conclusion.tex\\n    word_budget: 300\\n    phase: 2\\n    core_bullets:\\n      - \\\"SICA evaluated: 7 models (7B–32B), 4 domains, N>2,400, 3-seed replication\\\"\\n      - \\\"Independence bottleneck: Eff-K=1.20–3.63 limits both SC and SICA\\\"\\n      - \\\"Regime-dependent: Goldilocks zone (+4.90pp, 2/3 seeds significant), Type C hurts (-2.83pp), Type A n.s.\\\"\\n      - \\\"Oracle +14.22pp/+11.50pp proves aggregation; 9 remediation strategies all fail\\\"\\n      - \\\"K=12 sweet spot (inverted-U); T=0.7→T=1.0 collapses effect\\\"\\n      - \\\"C0 + SC as deployment diagnostic\\\"\\n    dependencies: [experiments, analysis]\\n\\n# ──────────────────────────────────────────────\\n# Visualization Plan\\n# ──────────────────────────────────────────────\\nvisualization_plan:\\n  - fig_id: fig1_pipeline\\n    type: conceptual\\n    tool: matplotlib\\n    description: >\\n      SICA pipeline diagram: K traces → FOL constraint extraction →\\n      syntactic deduplication → weighted partial MAX-SAT (Z3) → answer selection.\\n      Include oracle branch. Annotate independence bottleneck at extraction stage.\\n    narrative_intent: \\\"Pipeline architecture and where independence bottleneck manifests\\\"\\n    design_notes: >\\n      Update existing TikZ pipeline. Add \\\"Independence Bottleneck\\\" annotation.\\n      No SICA+ components (D060: method improvement removed).\\n    placement: method\\n    aspect_ratio: \\\"16:6\\\"\\n    data_source: \\\"manual (existing TikZ code)\\\"\\n    status: \\\"EXISTS — minor label update\\\"\\n\\n  - fig_id: fig2_regime_scatter\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      SC accuracy (x) vs SICA Δpp (y) scatter. All model-domain conditions.\\n      3 replication seeds as separate points. Color by significance.\\n      Regime zone annotations (Type A/C, Goldilocks).\\n    narrative_intent: \\\"Hero figure: regime-dependent SICA effectiveness\\\"\\n    design_notes: >\\n      Solid markers n≥100, hollow n<100. Horizontal Δ=0 line.\\n      Green band ~50–55% SC. Use exp-046 FINAL (n=600, SC=39.33%, Δ=-2.83pp).\\n      Three Mistral seeds at SC≈54–56%. Width 0.75\\\\textwidth.\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: >\\n      registry: exp-033, exp-052, exp-053, exp-046, exp-041, exp-026,\\n      exp-035, exp-038, exp-020, exp-027, exp-019, exp-044b, exp-050b,\\n      exp-049b, exp-014, exp-017, exp-012, sica_aime30_v3\\n    status: \\\"UPDATE — add 3 seeds + exp-046 FINAL\\\"\\n\\n  - fig_id: fig3_k_sensitivity\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Two-panel figure. (a) K vs SICA Δpp showing inverted-U curve:\\n      K=4(-1.47), K=8(-0.98), K=12(+4.90), K=16(+1.47).\\n      (b) Actual K vs Eff-K bar chart per model showing independence deficit.\\n    narrative_intent: \\\"K=12 is sweet spot; inverted-U reveals interaction between diversity and constraint quality\\\"\\n    design_notes: >\\n      Panel (a): line plot with markers and error bars if available.\\n      Panel (b): grouped bars — actual K (gray) vs Eff-K (colored per model).\\n      Subfigure layout. Width 0.75\\\\textwidth.\\n    placement: analysis\\n    aspect_ratio: \\\"2:1\\\"\\n    data_source: \\\"Director K sensitivity data + comp-1 Eff-K computation\\\"\\n    status: \\\"NEW — requires comp-1 output for panel (b)\\\"\\n\\n# ──────────────────────────────────────────────\\n# Table Plan\\n# ──────────────────────────────────────────────\\ntable_plan:\\n  - table_id: tab1_main_results\\n    type: comparison\\n    placement: experiments\\n    width: \\\"table*\\\"\\n    caption: \\\"SICA vs SC across all conditions, sorted by SC accuracy. Includes 3-seed replication and oracle upper bounds.\\\"\\n    columns: [Model, Domain, n, \\\"SC (%)\\\", \\\"SICA (%)\\\", \\\"Δ (pp)\\\", \\\"p\\\"]\\n    data_source: >\\n      registry: exp-033, exp-052, exp-053, exp-046 (FINAL: n=600 SC=39.33\\n      Δ=-2.83 p=0.0095), exp-041, exp-026/sica_expanded_14b, exp-035,\\n      exp-038, exp-020, exp-027, exp-019, exp-044b, exp-014, exp-017,\\n      exp-012, sica_aime30_v3, exp-031, exp-022\\n    notes: >\\n      Grouped by regime: Type C, Goldilocks (with 3 seeds), Type A, Degenerate, Oracle.\\n      Merge replication + oracle into single table. Use exp-046 FINAL numbers.\\n\\n  - table_id: tab3_independence\\n    type: analysis\\n    placement: analysis\\n    width: \\\"table\\\"\\n    caption: \\\"Condorcet independence analysis by model-domain condition.\\\"\\n    columns: [Model, Domain, \\\"Fleiss' κ\\\", \\\"Eff-K\\\", \\\"Unanimous (%)\\\", \\\"Confirm. bias (%)\\\", \\\"SICA Δ (pp)\\\"]\\n    data_source: \\\"comp-1 Worker output + registry metrics\\\"\\n    notes: \\\"C1 contribution table. Requires comp-1 computation.\\\"\\n\\n  - table_id: tab4_extraction_taxonomy\\n    type: analysis\\n    placement: analysis\\n    width: \\\"table\\\"\\n    caption: \\\"Extraction quality: constraint discriminativeness and variable sharing.\\\"\\n    columns: [Metric, Value, Description]\\n    data_source: \\\"registry: exp-023, exp-036b\\\"\\n    notes: \\\"~8% Z3-discriminative, 56.4% zero shared vars, filtering = 0 gain\\\"\\n\\n  # Appendix tables\\n  - table_id: tab_app_remediation\\n    type: comparison\\n    placement: appendix\\n    caption: \\\"Nine remediation strategies targeting the independence bottleneck.\\\"\\n    columns: [Strategy, Dimension, \\\"Key metric\\\", Result]\\n    data_source: \\\"registry + D060 data\\\"\\n    notes: \\\"Original 6 + filtering + T=1.0 + multi-temp. All fail.\\\"\\n\\n  - table_id: tab_app_entropy\\n    type: analysis\\n    placement: appendix\\n    caption: \\\"SICA Δ by answer entropy bin.\\\"\\n    data_source: \\\"registry: exp-033, exp-026 per_entropy\\\"\\n\\n  - table_id: tab_app_oracle_subtype\\n    type: detail\\n    placement: appendix\\n    caption: \\\"Oracle-SICA by ProofWriter subtype.\\\"\\n    data_source: \\\"registry: exp-022\\\"\\n\\n  - table_id: tab_app_k_ablation\\n    type: detail\\n    placement: appendix\\n    caption: \\\"K sensitivity detailed: SICA Δ, SC accuracy, and diversity metrics by K.\\\"\\n    data_source: \\\"Director K sensitivity data; registry: exp-051, sica_k_sensitivity_14b\\\"\\n\\n  - table_id: tab_app_replication\\n    type: detail\\n    placement: appendix\\n    caption: \\\"Seed replication detailed analysis.\\\"\\n    data_source: \\\"registry: exp-033, exp-052, exp-053\\\"\\n\\n# ──────────────────────────────────────────────\\n# Literature Strategy\\n# ──────────────────────────────────────────────\\nliterature_strategy:\\n  citation_budget: 40\\n  micro_clusters:\\n    - cluster_name: \\\"self_consistency_and_variants\\\"\\n      target_count: 6\\n      must_cite:\\n        - \\\"Wang et al. 2023 (Self-Consistency)\\\"\\n        - \\\"Chen et al. 2023 (USC)\\\"\\n        - \\\"Loo et al. 2025 (SC scaling re-evaluation)\\\"\\n        - \\\"Taubenfeld et al. 2025 (confidence-weighted SC)\\\"\\n      search_queries:\\n        - \\\"self-consistency majority voting LLM reasoning 2023 2024 2025\\\"\\n        - \\\"DiVeRSe diverse verifier reasoning steps\\\"\\n\\n    - cluster_name: \\\"symbolic_reasoning_llm\\\"\\n      target_count: 8\\n      must_cite:\\n        - \\\"Pan et al. 2023 (Logic-LM)\\\"\\n        - \\\"Olausson et al. 2023 (LINC)\\\"\\n        - \\\"Xu et al. 2026 (DyLoS)\\\"\\n        - \\\"Li et al. 2025 (Aristotle)\\\"\\n        - \\\"Wang et al. 2025 (FoVer)\\\"\\n        - \\\"Luo et al. 2025 (LogicAgent)\\\"\\n      search_queries:\\n        - \\\"neuro-symbolic reasoning LLM formal logic solver 2024 2025\\\"\\n\\n    - cluster_name: \\\"test_time_compute_scaling\\\"\\n      target_count: 5\\n      must_cite:\\n        - \\\"Snell et al. 2025 (scaling test-time compute, ICLR Oral)\\\"\\n        - \\\"Guo et al. 2025 (DeepSeek-R1)\\\"\\n      search_queries:\\n        - \\\"test-time compute scaling LLM reasoning 2025\\\"\\n\\n    - cluster_name: \\\"verification_reranking\\\"\\n      target_count: 4\\n      must_cite:\\n        - \\\"Cobbe et al. 2021 (ORM / GSM8K)\\\"\\n        - \\\"Lightman et al. 2023 (PRM)\\\"\\n      search_queries:\\n        - \\\"outcome reward model process reward model verification 2024\\\"\\n\\n    - cluster_name: \\\"condorcet_voting_theory\\\"\\n      target_count: 5\\n      must_cite:\\n        - \\\"Condorcet 1785 (Jury Theorem)\\\"\\n        - \\\"Austen-Smith & Banks 1996 (information aggregation)\\\"\\n        - \\\"arXiv:2409.00094 (closest prior work — Condorcet applied to LLM aggregation)\\\"\\n      search_queries:\\n        - \\\"Condorcet jury theorem machine learning ensemble diversity\\\"\\n        - \\\"effective ensemble size correlated voters independence\\\"\\n        - \\\"Fleiss kappa inter-rater agreement reliability\\\"\\n      notes: \\\"Must verify arXiv:2409.00094 content and cite appropriately\\\"\\n\\n    - cluster_name: \\\"constraint_satisfaction_nlp\\\"\\n      target_count: 3\\n      must_cite:\\n        - \\\"de Moura & Bjorner 2008 (Z3)\\\"\\n      search_queries:\\n        - \\\"SAT solver NLP constraint satisfaction 2024 2025\\\"\\n\\n    - cluster_name: \\\"self_correction_negative\\\"\\n      target_count: 3\\n      must_cite:\\n        - \\\"Huang et al. 2024 (LLMs cannot self-correct reasoning)\\\"\\n      search_queries:\\n        - \\\"LLM self-correction reasoning limitations 2024\\\"\\n\\n    - cluster_name: \\\"benchmarks\\\"\\n      target_count: 5\\n      must_cite:\\n        - \\\"Han et al. 2022 (FOLIO)\\\"\\n        - \\\"Tafjord et al. 2021 (ProofWriter)\\\"\\n        - \\\"Liu et al. 2020 (LogiQA)\\\"\\n        - \\\"Geva et al. 2021 (StrategyQA)\\\"\\n        - \\\"Cobbe et al. 2021 (GSM8K)\\\"\\n\\n    - cluster_name: \\\"debate_multi_agent\\\"\\n      target_count: 3\\n      must_cite:\\n        - \\\"Liang et al. 2023\\\"\\n        - \\\"Du et al. 2023\\\"\\n      search_queries:\\n        - \\\"LLM debate multi-agent reasoning aggregation 2023 2024\\\"\\n\\n    - cluster_name: \\\"compositionality\\\"\\n      target_count: 1\\n      must_cite:\\n        - \\\"Press et al. 2023 (compositionality gap)\\\"\\n\\n# ──────────────────────────────────────────────\\n# Writing Order\\n# ──────────────────────────────────────────────\\nwriting_order:\\n  - method          # Phase 1: Condorcet + SICA pipeline + Oracle design\\n  - experiments     # Phase 1: data-driven, Table 1 hero\\n  - analysis        # Phase 1: Eff-K + taxonomy + K/T sensitivity + entropy + remediation\\n  - related_work    # Phase 1: standalone\\n  - introduction    # Phase 2: depends on all above\\n  - discussion      # Phase 2: depends on all empirical\\n  - abstract        # Phase 2: last\\n  - conclusion      # Phase 2: last\\n\\n# ──────────────────────────────────────────────\\n# Page Budget\\n# ──────────────────────────────────────────────\\npage_budget:\\n  target: 8.0\\n  breakdown:\\n    abstract: 0.3\\n    introduction: 1.3\\n    related_work: 0.8\\n    method: 1.2\\n    experiments: 1.8\\n    analysis: 1.5\\n    discussion: 0.5\\n    conclusion: 0.3\\n    total_text: 7.7\\n    figures_tables_float: 0.3\\n  compression_notes:\\n    - \\\"Oracle can merge into tab1 (save separate table float)\\\"\\n    - \\\"Replication as 3 rows in tab1 (no separate table)\\\"\\n    - \\\"Remediation: 1 paragraph main text + full table in appendix\\\"\\n    - \\\"Entropy: compact paragraph, move detailed table to appendix\\\"\\n    - \\\"No SICA+ sections (D060: method removed) — frees ~0.5pp for deeper analysis\\\"\\n\\n# ──────────────────────────────────────────────\\n# Pre-requisite Computations\\n# ──────────────────────────────────────────────\\nrequired_computations:\\n  - id: comp-1\\n    name: \\\"Fleiss' Kappa + Effective-K\\\"\\n    description: >\\n      Compute Fleiss' κ from per-problem trace answer distributions for all\\n      model-domain conditions. Director-provided values: Mistral κ=0.501\\n      (Eff-K=1.82), Qwen κ=0.739 (Eff-K=1.31). Verify and compute for\\n      remaining conditions.\\n    priority: HIGH\\n    blocking: [fig3_k_sensitivity, tab3_independence, \\\"§5.1\\\"]\\n    status: \\\"DONE — comp-1 Worker verified; exp-033 κ pending (westd-25068 inaccessible)\\\"\\n\\n  - id: comp-2\\n    name: \\\"Extraction taxonomy verification\\\"\\n    description: >\\n      D060 update: 43.1% trivially_satisfied number under review. Filtering\\n      experiment found ~8% non-discriminative. Use verified ~8% Z3-discriminative\\n      framing. Verify exact taxonomy breakdown from exp-023 data.\\n    priority: MEDIUM\\n    blocking: [tab4_extraction_taxonomy, \\\"§5.2\\\"]\\n\\n# ──────────────────────────────────────────────\\n# Key Data (truth source: registry)\\n# ──────────────────────────────────────────────\\nkey_data:\\n  hero_result:\\n    exp_id: exp-033\\n    model: Mistral-7B-Instruct-v0.3\\n    dataset: FOLIO-204\\n    sc: 54.41\\n    sica: 59.31\\n    delta_pp: 4.90\\n    p: 0.013\\n    b: 12\\n    c: 2\\n    seed: 42\\n\\n  replication:\\n    - {exp_id: exp-033, seed: 42, sc: 54.41, delta_pp: 4.90, p: 0.013, significant: true}\\n    - {exp_id: exp-052, seed: 123, sc: 53.9, delta_pp: 3.43, p: 0.039, significant: true}\\n    - {exp_id: exp-053, seed: 456, sc: 56.37, delta_pp: -0.49, p: 1.0, significant: false}\\n    # D060 correction: exp-052 p=0.039 (not 0.09). 2/3 significant at α=0.05.\\n\\n  oracle:\\n    - {exp_id: exp-031, dataset: FOLIO-204, oracle_acc: 89.71, sc: 75.49, delta_pp: 14.22, p: 2.0e-7}\\n    - {exp_id: exp-022, dataset: ProofWriter-600, oracle_acc: 86.67, sc: 75.17, delta_pp: 11.50, p: 9.21e-15}\\n\\n  type_c:\\n    exp_id: exp-046\\n    model: Mistral-7B\\n    dataset: ProofWriter-D5-600\\n    n: 600\\n    sc: 39.33\\n    sica: 36.50\\n    delta_pp: -2.83\\n    p: 0.0095\\n    note: \\\"FINAL numbers — do NOT use interim (n=303, Δ=-4.67pp)\\\"\\n\\n  independence:\\n    mistral_folio_s123:\\n      fleiss_kappa: 0.412\\n      eff_k: 2.17\\n      source: \\\"comp-1 Worker verified (exp-052)\\\"\\n    mistral_folio_s456:\\n      fleiss_kappa: 0.401\\n      eff_k: 2.22\\n      source: \\\"comp-1 Worker verified (exp-053)\\\"\\n    mistral_folio_s42:\\n      fleiss_kappa: 0.500\\n      eff_k: 1.85\\n      source: \\\"Director-verified (exp-033)\\\"\\n    qwen14b_folio:\\n      fleiss_kappa: 0.744\\n      eff_k: 1.31\\n      unanimous_rate: 58.3\\n      source: \\\"comp-1 Worker verified (exp-026)\\\"\\n    qwen14b_logiqa:\\n      fleiss_kappa: 0.821\\n      eff_k: 1.20\\n      unanimous_rate: 63.0\\n      source: \\\"comp-1 Worker verified (exp-038)\\\"\\n    mistral_folio_operational:\\n      unanimous_rate: 18.6\\n      override_precision: 70.6\\n      confirmation_bias: 31.9\\n      maxsat_sat_ratio: 0.961\\n      note: \\\"operational metrics from Director, retained for exp-033\\\"\\n    qwen14b_folio_operational:\\n      confirmation_bias: 62.3\\n      maxsat_sat_ratio: 0.991\\n      note: \\\"operational metrics from Director, retained\\\"\\n    mistral_pw600:\\n      fleiss_kappa: 0.210\\n      eff_k: 3.63\\n      source: \\\"Director-verified (exp-046)\\\"\\n    cross_seed_note: \\\"κ varies across seeds (0.50/0.41/0.40) but Δ non-monotonic with Eff-K (exp-033 Eff-K=1.85 has highest Δ=+4.90). Eff-K necessary not sufficient. exp-046 Eff-K=3.63 highest but SC=39% → negative Δ → need both sufficient Eff-K AND sufficient SC.\\\"\\n\\n  k_sensitivity:\\n    note: \\\"D060 data; inverted-U curve\\\"\\n    data:\\n      - {k: 4, delta_pp: -1.47}\\n      - {k: 8, delta_pp: -0.98}\\n      - {k: 12, delta_pp: 4.90}\\n      - {k: 16, delta_pp: 1.47}\\n      - {k: 20, delta_pp: null, status: pending}\\n\\n  t_sensitivity:\\n    note: \\\"D060 data; effect fragility\\\"\\n    data:\\n      - {t: 0.7, delta_pp: 4.90, exp_id: exp-033}\\n      - {t: 1.0, delta_pp: 0.55, exp_id: exp-054}\\n\\n  remediation_failures:\\n    count: 9\\n    dimensions: 6\\n    strategies:\\n      - {name: \\\"Contrastive prompting\\\", dim: prompting, exp: exp-029, result: \\\"disc_rate 8.2%→6.0%, Δ=-1.1pp\\\"}\\n      - {name: \\\"Cross-model extraction\\\", dim: architecture, exp: exp-030, result: \\\"0% discriminative\\\"}\\n      - {name: \\\"Generational scaling (Qwen3)\\\", dim: capability, exp: exp-027, result: \\\"+0.49pp n.s.\\\"}\\n      - {name: \\\"Z3 feedback\\\", dim: verification, exp: exp-036, result: \\\"0.9% UNSAT trigger\\\"}\\n      - {name: \\\"Cross-trace UNSAT\\\", dim: verification, exp: exp-036b, result: \\\"56.4% zero shared vars\\\"}\\n      - {name: \\\"Consistency filtering\\\", dim: filtering, exp: exp-043, result: \\\"reverts to SC at T≥4\\\"}\\n      - {name: \\\"Discriminative filtering\\\", dim: filtering, exp: null, result: \\\"0 gain\\\"}\\n      - {name: \\\"T=1.0 diversity\\\", dim: diversity, exp: exp-054, result: \\\"Δ collapses +4.90→+0.55pp\\\"}\\n      - {name: \\\"Multi-temp sampling\\\", dim: diversity, exp: exp-055, result: \\\"n=28, Δ=0.00pp\\\"}\\n\", \"total_chars\": 31453, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ff60c62-94d6-43da-b10a-ed8822f81ea3",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "61e60f57-d3d4-46a0-9efb-0adbb8c4d96a",
  "sourceToolAssistantUUID": "2ff60c62-94d6-43da-b10a-ed8822f81ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-19T04:50:10.992Z_

I now have a thorough understanding of the paper. Let me also check whether the "nine remediation strategies" claim vs. "six" in the paper body is consistent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61e60f57-d3d4-46a0-9efb-0adbb8c4d96a",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKod35xNwyZZyqe2oQX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab83e01f-217d-42f7-a578-ec8ebe848d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139954hFSZhDC3BYKDKWNub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16329,
      "cache_read_input_tokens": 75360,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16329,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 56 · 2026-05-19T04:50:12.408Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VNsqQJTDzzigPHPdsRHBVn`</summary>

```json
{
  "pattern": "nine|nine remediation|six remediation|9 remediation|6 remediation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab83e01f-217d-42f7-a578-ec8ebe848d24",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKod35xNwyZZyqe2oQX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a439fe39-2874-47b7-93a4-9e175824fd29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139954hFSZhDC3BYKDKWNub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16329,
      "cache_read_input_tokens": 75360,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16329
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 75360,
          "cache_creation_input_tokens": 16329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16329,
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

_source line 57 · 2026-05-19T04:50:12.431Z_

<details><summary>↩ Tool result · `toolu_01VNsqQJTDzzigPHPdsRHBVn`</summary>

```text
docs/paper/analysis.tex:78:[Omitted long matching line]
docs/paper/conclusion.tex:3:[Omitted long matching line]
docs/paper/discussion.tex:4:[Omitted long matching line]
docs/paper/method.tex:109:SICA as evaluated here uses \emph{same-model self-extraction}: the same LLM generates traces and extracts constraints. This design isolates whether a model's own reasoning can be usefully formalized for aggregation. Methods that use trained extractors, external provers, or multi-model ensembles fall outside the scope of this evaluation. We test nine remediation strategies spanning prompting, architecture, capability, verification, diversity, and filtering dimensions (\S\ref{sec:remediation}).
docs/paper/abstract.tex:2:[Omitted long matching line]
docs/paper/appendix.tex:369:\caption{Six remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.00\%$, $\Delta = -0.49$\,pp. None reaches significance.}
docs/paper/introduction.tex:11:[Omitted long matching line]
docs/paper/introduction.tex:15:[Omitted long matching line]
docs/paper/main.aux:1508:\@writefile{lot}{\contentsline {table}{\numberline {9}{\ignorespaces Six remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.00\%$, $\Delta = -0.49$\,pp. None reaches significance.}}{15}{table.caption.35}\protected@file@percent }
docs/paper/main.aux:1509:\newlabel{tab:remediation}{{9}{15}{Six remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.00\%$, $\Delta = -0.49$\,pp. None reaches significance}{table.caption.35}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a439fe39-2874-47b7-93a4-9e175824fd29",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "8effe947-effd-4c04-b687-f79cddc19893",
  "sourceToolAssistantUUID": "a439fe39-2874-47b7-93a4-9e175824fd29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-19T04:50:17.259Z_

I see a critical inconsistency: the abstract/intro/method mention "six remediation strategies" while the paper_framing.md mentions "nine." The appendix table is titled "Six remediation strategies" but the analysis section mentions "nine" and "six intervention dimensions." Let me verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8effe947-effd-4c04-b687-f79cddc19893",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKp4v5ViBPwbm5v61uE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41f31591-464e-4c65-99b3-c0fea25da446",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCwjEMtyqvFb12i62qSdkU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 91689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 677,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 59 · 2026-05-19T04:50:17.815Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Scm9QMQ8EJHAbBtS2dKoYa`</summary>

```json
{
  "pattern": "six|Six",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41f31591-464e-4c65-99b3-c0fea25da446",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKp4v5ViBPwbm5v61uE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd972b16-5d6e-482a-a7d1-595a1c295fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCwjEMtyqvFb12i62qSdkU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 91689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 677,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T04:50:17.823Z_

<details><summary>↩ Tool result · `toolu_01Scm9QMQ8EJHAbBtS2dKoYa`</summary>

```text
2:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd972b16-5d6e-482a-a7d1-595a1c295fd0",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "5e8303cc-0428-4e34-8226-ef3efcdb7d06",
  "sourceToolAssistantUUID": "fd972b16-5d6e-482a-a7d1-595a1c295fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T04:50:18.507Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GCXkKKM7oASDFksx8DYP9L`</summary>

```json
{
  "pattern": "six|Six|nine|Nine",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e8303cc-0428-4e34-8226-ef3efcdb7d06",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKp4v5ViBPwbm5v61uE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5dd320bf-7d69-4ab9-81c8-045c9972aa0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCwjEMtyqvFb12i62qSdkU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 91689,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 677
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 91689,
          "cache_creation_input_tokens": 677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 677,
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

_source line 62 · 2026-05-19T04:50:18.518Z_

<details><summary>↩ Tool result · `toolu_01GCXkKKM7oASDFksx8DYP9L`</summary>

```text
4:[Omitted long matching line]
78:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dd320bf-7d69-4ab9-81c8-045c9972aa0a",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "bdc2e966-5595-42cb-ae76-36b129aa2ce0",
  "sourceToolAssistantUUID": "5dd320bf-7d69-4ab9-81c8-045c9972aa0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T04:50:20.933Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X94dEje6qbk566A6YV9sCQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
  "offset": 74,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdc2e966-5595-42cb-ae76-36b129aa2ce0",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKpX5SPv2aTAxkHc4oA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9a58816-e7ff-45ae-a728-382cf795ce25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JyyifU6Gt7iYb5vbgtFhMR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 92366,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 495
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 92366,
          "cache_creation_input_tokens": 495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 495,
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

_source line 64 · 2026-05-19T04:50:20.938Z_

<details><summary>↩ Tool result · `toolu_01X94dEje6qbk566A6YV9sCQ`</summary>

```text
74	\subsection{Remediation Analysis}
75	\label{sec:remediation}
76	\label{sec:interventions}
77	
78	We test nine remediation strategies spanning six intervention dimensions (full results in Appendix Table~\ref{tab:remediation}). \emph{Prompting}: contrastive prompting reduces the discriminative rate from 8.2\% to 6.0\% ($\Delta = -1.1$\,pp), and filtering to retain only discriminative constraints yields zero gain. \emph{Architecture}: cross-model extraction produces 0\% discriminative constraints ($\Delta = 0$\,pp). \emph{Capability}: generational scaling with Qwen3-14B yields $\Delta = +0.49$\,pp (n.s.). \emph{Verification}: Z3 feedback loops trigger UNSAT on only 0.9\% of problems with no real accuracy impact; cross-trace UNSAT checking finds 56.4\% of constraint pairs share zero variables, so logical verification is vacuous. \emph{Diversity}: raising temperature to $T = 1.0$ collapses $\Delta$ from $+4.90$\,pp to $+0.49$\,pp (\S\ref{sec:t-sensitivity}); multi-temperature sampling ($n = 204$) produces $\Delta = 0.00$\,pp (SC $= 57.84\%$, SICA $= 57.84\%$). \emph{Filtering}: consistency filtering (retaining constraints in $\geq 4$ traces) prunes aggressively (1.8 constraints per problem at threshold 4, 0.3 at threshold 8) and reverts to SC. All six dimensions fail. The independence bottleneck is structural: it cannot be resolved by prompt engineering, solver refinements, or diversity manipulations within the same-model self-extraction paradigm.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9a58816-e7ff-45ae-a728-382cf795ce25",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "5a3e4c0e-ce30-41b8-8753-feb971ea8bd9",
  "sourceToolAssistantUUID": "f9a58816-e7ff-45ae-a728-382cf795ce25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-19T04:50:22.866Z_

Now I have all the information needed. Let me write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a3e4c0e-ce30-41b8-8753-feb971ea8bd9",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKpgyFaMgpFN5LuwdmF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b576183-5f92-46d0-90e6-8d5ccebd2c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188J9EM5Ww4h5SWeWsyCpuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 587,
      "cache_read_input_tokens": 92861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 587,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-19T04:50:23.667Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TpJ2wmKyWcuNujeKiaVQTa`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b576183-5f92-46d0-90e6-8d5ccebd2c01",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKpgyFaMgpFN5LuwdmF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81ccdca8-8b2e-435c-af19-588bddc71dfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188J9EM5Ww4h5SWeWsyCpuu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 587,
      "cache_read_input_tokens": 92861,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 587
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 92861,
          "cache_creation_input_tokens": 587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 587,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-19T04:50:23.670Z_

<details><summary>↩ Tool result · `toolu_01TpJ2wmKyWcuNujeKiaVQTa`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81ccdca8-8b2e-435c-af19-588bddc71dfb",
  "isSidechain": true,
  "promptId": "f5172b00-d98d-4730-aa3c-62aaf044b2d5",
  "agentId": "af9ded52e08159c00",
  "type": "user",
  "uuid": "a28702b4-b0a3-41e4-8876-df014ed60e38",
  "sourceToolAssistantUUID": "81ccdca8-8b2e-435c-af19-588bddc71dfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-19T04:51:48.484Z_



## R2 Review: Novelty and Related Work

### Summary
This paper evaluates SICA (Symbolic Invariant Consensus Aggregation), a pipeline that extracts FOL constraints from LLM reasoning traces and uses weighted MAX-SAT to select answers, framed as a diagnostic study of why same-model self-extraction fails. The core finding is that SICA helps only in a narrow "Goldilocks zone" (~50-55% SC accuracy), with three failure modes outside it, and that oracle controls confirm the aggregation mechanism is sound while self-extraction captures only 34.5% of the oracle ceiling. The paper applies a Condorcet Jury Theorem lens via Fleiss' kappa to quantify trace non-independence.

### Strengths

- **The oracle control design is methodologically clean and genuinely informative.** Substituting gold FOL annotations while holding the aggregation mechanism fixed is a well-designed causal intervention that cleanly separates extraction failure from aggregation failure. The +14.22pp and +11.50pp oracle results (both p < 0.001) are convincing. This methodology follows established precedent (Press et al. 2023, Trivedi et al. 2023) but applies it to a new and relevant question.

- **The regime characterization (Type A/B/C) is useful.** The three failure modes are distinct, well-defined, and supported by data. The Type C result (significant harm at low SC, p=0.0095) is a practical warning that is often missing from method papers. The Goldilocks zone framing, while narrow, is honestly presented.

- **Related work coverage is broad and well-organized.** The paper cites across five relevant dimensions (SC variants, neuro-symbolic reasoning, test-time compute, verification/reranking, Condorcet/voting theory). The differentiation from Logic-LM, LINC, DyLoS, Aristotle, and FoVer is explicit and honest: the paper correctly scopes its negative findings to same-model self-extraction and acknowledges that external/trained approaches remain viable.

- **The three-seed replication is commendable.** Reporting 2/3 seeds significant and 1/3 null is transparent. Many papers would have reported only the best seed.

- **The MAX-SAT approx count-only ablation (803/804 agreement) is a striking result.** This is a genuinely useful finding for the community: it demonstrates that the symbolic optimization machinery adds negligible value over simple counting when constraints are non-discriminative.

- **The Condorcet/Eff-K framing, while not deeply novel, provides a useful quantitative vocabulary.** Connecting Fleiss' kappa to effective ensemble size gives practitioners a concrete way to diagnose when additional sampling is wasteful. The citation of Lefort et al. (2024) as closest prior work (cross-model CJT) with clear differentiation (within-model, connected to symbolic aggregation) is appropriate.

### Weaknesses

- **W1: The core novelty is thin for a top venue.** The paper's primary finding is that self-extracted FOL constraints from LLMs are low-quality and non-discriminative. This is predictable from prior work: LINC (Olausson et al. 2023) already documented ~40% translation errors on FOLIO; Huang et al. (2024) established that LLMs cannot self-correct reasoning; Stechly et al. (2025) showed self-verification degrades performance. The paper essentially confirms these findings in a new pipeline configuration (MAX-SAT aggregation over multiple traces rather than single-path verification). The incremental step from "LLMs produce poor FOL translations" to "LLMs produce poor FOL translations when extracting from their own traces for aggregation" is modest. The Condorcet framing adds descriptive vocabulary but not predictive power (the paper acknowledges Eff-K has only 50% joint prediction accuracy, equivalent to chance, and is non-monotonic with delta across seeds).

- **W2: The paper studies a method that was never proposed or published.** SICA is not an established method from the literature; it is the authors' own construction. Diagnostic studies of existing methods (e.g., Huang et al. 2024 studying self-correction, Mirzadeh et al. 2024 studying GSM reasoning) gain their force from challenging widely-adopted approaches. SICA has no adoption to challenge. The paper is effectively proposing a method, showing it does not work, and then analyzing why. This undercuts the "diagnostic study" framing: the community has no prior belief that SICA should work, so demonstrating that it does not work carries less weight. The paper partially addresses this by arguing the question "can same-model self-extraction help?" is independently important, but the answer ("almost never") was foreseeable from existing negative results on LLM self-verification.

- **W3: The positive result is extremely fragile, undermining both method and analysis contributions.** The only significant positive result is Mistral-7B on FOLIO at T=0.7, K=12. It does not generalize across: (a) models (zero or negative for all others), (b) domains (LogiQA at similar SC shows null), (c) temperatures (T=1.0 collapses to noise), (d) K values (inverted-U with sharp drop), or (e) seeds (1/3 null). The mean effect across seeds is +2.61pp, which is practically small. For a diagnostic paper, the fragility is the finding, but it means the paper has almost no constructive takeaway. The C0+SC diagnostic is presented as a practical contribution, but it can only rule out SICA (when C0 < 5%) and cannot predict when it will help (high C0 + moderate SC is necessary but not sufficient, as LogiQA demonstrates).

- **W4: Internal inconsistency in remediation count.** The abstract and introduction claim "six remediation strategies," while the analysis section (\S5.6) claims "nine remediation strategies spanning six intervention dimensions." The appendix table is titled "Six remediation strategies" but lists only six rows despite the main text describing nine distinct interventions (contrastive prompting, discriminative filtering, cross-model, Qwen3, Z3 feedback, cross-trace UNSAT, T=1.0, multi-temp, consistency filtering). This inconsistency suggests the paper was revised without harmonizing all sections.

- **W5: The Condorcet framework is descriptive, not predictive.** The paper initially aimed for a predictive framework (per the paper_framing.md, "Condorcet-based predictive framework") but the data does not support it. Eff-K is non-monotonic with SICA delta across seeds (seed with lowest Eff-K=1.85 has highest delta=+4.90; seed with highest Eff-K=2.22 has delta=-0.49). The paper acknowledges this but still presents the framework as a contribution. Applying Fleiss' kappa to LLM trace agreement is a straightforward calculation, not a methodological advance. The Eff-K formula is borrowed directly from cluster sampling (Ladha 1992) with kappa substituted for intra-cluster correlation. The novelty claim that "no prior work applies Fleiss' kappa or Eff-K to within-model SC traces" is true but the application is mechanical rather than insightful.

- **W6: Missing or incomplete references raise quality concerns.** Several bib entries use "and others" in the author field (FoVer: "Wang, Yilun and others"; Aristotle: "Li, Jundong and others"; LogicAgent: "Luo, Yiqi and others"; Loo et al.: "Loo, Ryan and others"). This is sloppy for a venue submission. More concerning, some references may be difficult to verify: DyLoS is cited as EACL 2026 (Xu et al. 2026) and diverseaware2026 is cited as ICLR 2026, both being future venues at the time of many readers' checking. The Kim et al. 2026 (ReASC) and nsvif2026 references in the bib file are also dated 2026. While these may be legitimate, the concentration of 2026 citations from venues that may not have published proceedings yet warrants scrutiny.

- **W7: The "Goldilocks zone" narrative is confounded.** The paper's central claim is that SICA helps only at ~50-55% SC, but this conclusion rests almost entirely on one model (Mistral-7B) on one dataset (FOLIO). LogiQA falls in the same SC range (51%) but shows null effect, which the paper attributes to "domain formalizability" (Type B). This means the Goldilocks zone requires not just the right SC range but also the right domain, the right temperature, the right K, and the right seed. The zone is so narrow and multi-conditional that it offers little practical guidance.

### Questions for Authors

1. How do you respond to the concern that SICA is the authors' own construction rather than an established method? Why should the community care that a never-proposed method fails? What prior belief does this paper update?

2. The Eff-K framework is non-monotonic with SICA delta across seeds. Can you provide any evidence that Eff-K is predictive rather than merely descriptive? What is the R-squared of Eff-K alone (not combined with SC) for predicting SICA delta?

3. The abstract says "six remediation strategies" but the analysis section says "nine remediation strategies spanning six intervention dimensions." Which is correct? The appendix table shows only six rows. Where are the other three?

4. Why was LogiQA classified as Type B (non-formalizable) rather than acknowledging it as a Goldilocks-zone failure? The 0.8% contradiction rate is presented as evidence for Type B, but couldn't this equally reflect poor extraction quality (the same bottleneck as everywhere else)?

5. The multi-temp intervention (exp-055) raised SC from 54.41% to 57.84% (+3.4pp), suggesting mixed-temperature sampling improves majority voting. Since this is a positive finding (better SC baseline at no additional model cost), why is it buried rather than highlighted?

6. The constraint ablation shows MAX-SAT agrees with count-only on 803/804 problems. If the symbolic optimization adds nothing, why frame the paper around "symbolic consensus" rather than around the more general question of whether self-extracted features (of any kind) can improve multi-sample aggregation?

### Minor Issues

- The abstract mentions "four reasoning domains" but the experimental setup lists six datasets (FOLIO, ProofWriter, LogiQA, StrategyQA, GSM8K, AIME 2024). The paper also mentions ARC-Challenge in passing. The scope description is inconsistent.
- Table 1 reports ProofWriter results as "PW-D5" but the text sometimes refers to "ProofWriter" without the depth qualifier.
- The conclusion mentions "$\Delta = -4.67$\,pp" for Type C, but Table 1 reports $\Delta = -2.83$\,pp for Mistral-7B on PW-D5. The -4.67 appears to be from an interim analysis (n=303) that was superseded by the final analysis (n=600). This is a data inconsistency that must be fixed.
- The Qwen2.5-14B ICL experiment ($\Delta = +0.50$pp) is reported with "n.s." instead of an exact p-value in Table 1, inconsistent with other rows.
- Several references use "and others" instead of full author lists (FoVer, Aristotle, LogicAgent, Loo et al., DeepSeek-R1, Qwen2.5). This is below the standard expected for a top venue submission.
- The paper uses em-dashes in at least one location (the pipeline figure annotation), which should be checked for consistency.

### Preliminary Score: 3/6
### Confidence: 4/5

**Rationale:** The paper is competently executed and honest about its findings, which I appreciate. The oracle control and regime characterization are solid empirical work. However, the novelty bar for a top venue is not met. The core finding (self-extracted FOL constraints are low-quality) is predictable from prior work on LLM formalization failures. The method under study (SICA) was never proposed elsewhere, so demonstrating its failure has limited impact. The Condorcet framing is descriptive but not predictive. The constructive contribution (C0+SC diagnostic) is too weak to use in practice (necessary condition only, not sufficient). The paper would benefit from either (a) a stronger positive finding (e.g., identifying conditions under which self-extraction reliably helps), or (b) a more general theoretical result about why same-model self-verification is fundamentally limited, beyond the Eff-K calculation which is a direct application of classical cluster-sampling theory. In its current form, the paper is a thorough negative result on a method no one was using, which places it around the Findings threshold.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a28702b4-b0a3-41e4-8876-df014ed60e38",
  "isSidechain": true,
  "agentId": "af9ded52e08159c00",
  "requestId": "req_011CbBKptrNa889hn7FwgKjs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b585dea-b944-4a33-be76-4c1affb9dc2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ff4131df-0538-40e9-a5d8-d0234a1df865",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3x248hyRwR6LTqv7tVGat",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 92861,
      "output_tokens": 3078,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3078,
          "cache_read_input_tokens": 92861,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1269,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---
