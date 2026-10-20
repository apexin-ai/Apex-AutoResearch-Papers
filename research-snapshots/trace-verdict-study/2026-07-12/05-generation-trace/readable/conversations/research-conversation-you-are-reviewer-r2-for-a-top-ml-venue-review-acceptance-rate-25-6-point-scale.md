# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Y

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac1895a814ace99e3.jsonl`
- **Structured JSON:** [`3b616c0882a229c77ccd.json`](../../sessions/3b/3b616c0882a229c77ccd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-18T14:08:10.103Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus areas are **Novelty**, **Related Work**, and **Presentation/Writing**.

## Paper Summary
Title: "Exception Events Are All You Need: Fault Indicator Isolation as the Robust Mechanism for Execution Trace Verdict Prediction"

The paper studies which execution trace components matter for verdict prediction (binary pass/fail classification of code). Through ablation across 4 models (Qwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, CodeLlama-13B-Instruct), they find that exception events (compact error summaries) are the only universally robust trace component, achieving 99.83% accuracy on Qwen-7B. They propose VOTA (Verdict-Optimized Trace Abstraction), a three-component trace compression pipeline.

## Paper Structure (9 pages)
- Page 1: Title, Abstract, Introduction (starts)
- Page 2: Introduction (cont.), Related Work
- Page 3: Method (Task Definition, Dataset, Trace Representations, Training Setup)
- Pages 4-7: Experiments (8 subsections with 8 tables)
- Page 8: Discussion, Limitations
- Page 9: Conclusion, References (5 citations only)

## Key Claims/Contributions
1. Exception events are the most effective and only universally robust trace component for verdict prediction
2. Information density bottleneck: gradient dilution = 26% of gap, information overload = 74%
3. Two-tier diagnostic hierarchy: Tier 1 (exceptions, assertions) near-perfect; Tier 2 (loops) model-dependent

## Related Work Section (Page 2)
Three subsections:
- **Trace-augmented code models**: DCSH [1], TracePile [2], TRACED [3] — 3 citations
- **Code execution prediction**: CRUXEval [4], CodeExecutor [5] — 2 citations
- **LLM-based test verdict prediction**: No specific citations, only general description

Total references: **5 citations** for the entire paper.

## Key Results
- exception_only: 99.83% on Qwen-7B (2 irreducible GeneratorExit errors)
- ae_only actually scores 99.92% (higher than exception_only!) in Table 1
- GPT-4o 3-shot: 97.2% (only 2.63pp below SFT)
- Budget curves: 4 models show 4 completely different patterns
- OOD: 12.7pp degradation on LeetCode-style problems
- Cross-model calibration: ECE ranges from 0.0027 to 0.0523 (19x variation)
- Only 5 references in the entire paper

## Context Notes
- The paper was reframed from "universal phase transition" to "exception dominance as only universal finding" due to model-dependent budget curves
- The few-shot GPT-4o baseline (97.2%) is close to SFT (99.83%), raising questions about SFT necessity
- OOD generalization is limited; cross-language not feasible
- Many findings are model-dependent, limiting universality claims

## Your Review Task (R2: Novelty + Related Work + Presentation)

Evaluate the following dimensions thoroughly:

1. **Novelty Assessment**: Is the core finding (exception events dominate) surprising or expected? Is there sufficient intellectual contribution? Would practitioners/researchers gain meaningful new insight?

2. **Related Work Coverage**: Are there major missing references? Is the positioning against prior work adequate? Only 5 references is extremely low for any venue — assess how this affects credibility.

3. **Contribution Significance**: Are the three listed contributions genuinely novel and significant? The "two-tier hierarchy" is essentially "exceptions work, loops don't" — is this a contribution or an observation?

4. **Framing and Narrative**: The title claims "Exception Events Are All You Need" (echoing Attention Is All You Need). Is this framing earned by the results? The paper admits many findings are model-dependent.

5. **Writing Quality**: Assess clarity, organization, and presentation. Check for AI-writing indicators (dashes, -ing phrases, etc.).

6. **Scope and Generalizability**: The dataset is only Python, only HumanEval+MBPP, only 591 problems. How does this limit the claims?

7. **ae_only anomaly**: Table 1 shows ae_only (99.92%) actually outperforms exception_only (99.83%). The paper doesn't adequately address why exception_only is claimed as the "most effective" when ae_only is numerically higher.

8. **Missing Related Work**: Consider whether the paper cites enough work on: test outcome prediction, fault localization, program analysis, software testing, execution trace analysis, code LLMs, etc.

## Output Format

Provide your review in the following structure:
```
### R2 Review: Novelty & Related Work

**Summary**: (2-3 sentences)

**Strengths**:
- S1: ...
- S2: ...
- ...

**Weaknesses**:
- W1: ...
- W2: ...
- ...

**Questions for Authors**:
- Q1: ...
- Q2: ...

**Missing References**:
- ...

**Minor Issues**:
- ...

**Score**: X/6
**Confidence**: X/5
**Justification**: (2-3 sentences explaining score)
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "dba915af-3c0d-4662-b6cd-d937757d7925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T14:08:10.106Z_

```json
{
  "parentUuid": "dba915af-3c0d-4662-b6cd-d937757d7925",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
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
  "uuid": "b438eedf-2bf6-4568-9614-494e53aefda8",
  "timestamp": "2026-05-18T14:08:10.106Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T14:08:19.250Z_



I'll start by reading the paper and related project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b438eedf-2bf6-4568-9614-494e53aefda8",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAZBK5Up78G4yoe3afV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d64b25a9-911e-48bb-8e8e-18cb373a650a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NH7RrprzdsmScs5xGmk2LH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8698,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8698,
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

_source line 4 · 2026-05-18T14:08:19.496Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A4VxTwoHPt66qHCaFSkghZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d64b25a9-911e-48bb-8e8e-18cb373a650a",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAZBK5Up78G4yoe3afV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "783e2a78-3d9a-47bb-8ae3-ce22d2f19055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NH7RrprzdsmScs5xGmk2LH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8698,
      "cache_read_input_tokens": 8249,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8698
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 107,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 8698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8698,
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

_source line 5 · 2026-05-18T14:08:19.499Z_

<details><summary>↩ Tool result · `toolu_01A4VxTwoHPt66qHCaFSkghZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "783e2a78-3d9a-47bb-8ae3-ce22d2f19055",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "a2247fd7-13a6-4017-9afd-0d3b6eaf421c",
  "sourceToolAssistantUUID": "783e2a78-3d9a-47bb-8ae3-ce22d2f19055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T14:08:21.844Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2247fd7-13a6-4017-9afd-0d3b6eaf421c",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAZdUCArCqeN7S2Jav2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52ebfe0c-e631-4e97-bb4c-4a2d9d616def",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxzYerR8PdfgYaBRvNtR7G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 7 · 2026-05-18T14:08:22.845Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QvhTcaC9xJbjeR1vAWX6Bu`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52ebfe0c-e631-4e97-bb4c-4a2d9d616def",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAZdUCArCqeN7S2Jav2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ab3caf8-ac6b-4e76-80d1-4df70365d365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxzYerR8PdfgYaBRvNtR7G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 8 · 2026-05-18T14:08:22.859Z_

<details><summary>↩ Tool result · `toolu_01QvhTcaC9xJbjeR1vAWX6Bu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/report.md\", \"content\": \"# Handover — 2026-05-18\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- qwen1.5b_full_trace_seed42: Qwen-1.5B full_trace 应达 ≥96% accuracy，确认 1.5B 小模型在 full trace 条件下与 7B 可比（trace quality 主导而非 model capacity）（排队等待 GPU）\\n- qwen1.5b_exception_only_seed42: Qwen-1.5B exception_only 应达 ≥99% accuracy，确认 minimal sufficient signal 在 1.5B scale 有效，signal quality 主导 model capacity（排队等待 GPU）\\n- qwen1.5b_vota_seed42: Qwen-1.5B VOTA 应在 82-90% accuracy，可能略低于 7B 因 VOTA 条件下 scale-sensitivity 更明显（排队等待 GPU）\\n- qwen1.5b_no_trace_seed42: Qwen-1.5B no_trace 应在 65-75% (≈majority baseline)，确认无 trace 小模型表现更差、scale 无法补偿（排队等待 GPU）\\n- codellama_exception_only_seed42: CodeLlama-13B exception_only 应达 ≥99.33% accuracy，与其他 3 模型一致，确认 minimal sufficient signal 跨 4 模型 3 架构 1.5B-13B universal（排队等待 GPU）\\n- codellama_vota_seed42: CodeLlama-13B VOTA 应在 85-92% accuracy，与 Qwen-7B/DeepSeek VOTA 对齐，作 rebuttal 储备验证 ablation condition 跨 scale 一致性（排队等待 GPU）\\n- codellama_no_trace_seed42: CodeLlama-13B no_trace 应在 70-78% (≈majority baseline)，确认无 trace 时 13B scale 无法补偿信息缺失（排队等待 GPU）\\n- qwen15b_full_trace_tail384_seed42: Qwen-1.5B tail-384 应在 80-90% 之间（小模型在 transition zone 可能更低），精确定位 phase transition 曲线形状（已分配 ? GPU:?，等待提交）\\n- codellama13b_full_trace_tail384_seed42: CodeLlama-13B tail-384 (label_only_loss) 应在 85-95% 之间（256→512 phase transition 中间点），验证 label_only_loss 在短序列下也有效（已分配 ? GPU:?，等待提交）\\n\\n## 近期结论\\n- **qwen7b_full_trace_tail384_seed42** (success): Qwen-7B tail-384 应在 85-93% 之间（256→512 phase transition 的中间点），精确定位 phase transition 曲线形状\\n- **deepseek_full_trace_tail384_seed42** (success): DeepSeek-6.7B tail-384 应在 85-93% 之间（256→512 phase transition 的中间点），精确定位 phase transition 曲线形状\\n- **qwen7b_full_trace_head2048_seed42** (success): Qwen-7B head-2048 应在 75-82% (signal-poor convergence band)，与其他 3 模型 head-2048 (75.3-79.9%) 对齐，补全 4 模型 head-tail gap claim\\n\\n## 趋势\\n成功 68 / 负向 13 / 失败 5 / 共 96\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-11235: 无 GPU 信息\\n\\n## 告警\\n- no_trace_seed42: 已被终止 — unknown\\n- vota_seed42: 已被终止 — unknown\\n- no_trace_seed42_v2: 已被终止 — unknown\\n- vota_seed42_v2: 已被终止 — unknown\\n- no_trace_seed42_v3: 已被终止 — unknown\\n- vota_seed42_v3: 已被终止 — unknown\\n- full_trace_seed42: 已被终止 — unknown\\n- vota_exception_only_seed42: 训练失败 — unknown\\n- vota_seed123: 训练失败 — unknown\\n- vota_seed456: 训练失败 — unknown\\n- deepseek_full_trace_seed42_v2: 已被终止 — unknown\\n- full_trace_2048tok_seed42: 已被终止 — unknown\\n- codellama13b_nomarker_seed42: 已被终止 — unknown\\n- codellama13b_full_trace_tail1024_seed42: 训练失败 — unknown\\n- codellama13b_full_trace_tail2048_seed42: 训练失败 — unknown\\n\", \"total_chars\": 2544, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ab3caf8-ac6b-4e76-80d1-4df70365d365",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "8561a14e-1436-4db4-9095-6888d9f3783e",
  "sourceToolAssistantUUID": "4ab3caf8-ac6b-4e76-80d1-4df70365d365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T14:08:23.788Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018eGMNVWi1DntMvSKNmT8gn`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8561a14e-1436-4db4-9095-6888d9f3783e",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAZdUCArCqeN7S2Jav2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbb5c4cb-baa5-4dd9-a7b6-869cb4ec1e91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxzYerR8PdfgYaBRvNtR7G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 10 · 2026-05-18T14:08:23.803Z_

<details><summary>↩ Tool result · `toolu_018eGMNVWi1DntMvSKNmT8gn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml\", \"content\": \"categories:\\n  execution-trace-llm:\\n    description: \\\"Execution trace 辅助 LLM 代码理解/调试/推理\\\"\\n    papers:\\n      - title: \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\"\\n        authors: \\\"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        role: method-component\\n        key_finding: \\\"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\\\"\\n        metrics:\\n          mbpp_fix_rate_improvement: \\\"+26.1%\\\"\\n          humaneval_fix_rate_improvement: \\\"+14.3%\\\"\\n\\n      - title: \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\\\"\\n        authors: \\\"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\\\"\\n        year: 2025\\n        venue: \\\"Findings of EMNLP 2025\\\"\\n        arxiv_id: \\\"2509.11686\\\"\\n        role: direct-competitor\\n        key_finding: \\\"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Code Execution as Grounded Supervision for LLM Reasoning\\\"\\n        authors: \\\"Dongwon Jung, Wenxuan Zhou, Muhao Chen\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2506.10343\\\"\\n        role: method-component\\n        key_finding: \\\"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\\\"\\n        authors: \\\"Lorenzo Ferrando, Nicola Ferraro, et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2503.05703\\\"\\n        arxiv_id: \\\"2503.05703\\\"\\n        role: method-component\\n        key_finding: \\\"对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。\\\"\\n        metrics:\\n          cruxeval_accuracy: \\\"~80%\\\"\\n          mbpp_accuracy: \\\"~80%\\\"\\n\\n      - title: \\\"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation\\\"\\n        authors: \\\"Mohammad Abdollahi, Khandaker Rifah Tasnia, Soumit Kanti Saha, Jinqiu Yang, Song Wang, Hadi Hemmati\\\"\\n        year: 2025\\n        venue: \\\"arXiv\\\"\\n        arxiv_id: \\\"2512.00215\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)\\\"\\n        authors: \\\"Junkai Chen et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2403.16437\\\"\\n        role: evaluation\\n        key_finding: \\\"REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。\\\"\\n        metrics:\\n          avg_accuracy: \\\"44.4%\\\"\\n          avg_ic_score: \\\"10.3\\\"\\n\\n      - title: \\\"CodeMind: Evaluating Large Language Models for Code Reasoning\\\"\\n        authors: \\\"Changshu Liu et al. (UIUC)\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2402.09664\\\"\\n        role: evaluation\\n        key_finding: \\\"评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\"\\n        authors: \\\"Ruiyang Xu et al. (HKUST)\\\"\\n        year: 2025\\n        venue: \\\"ACL 2025\\\"\\n        arxiv_id: \\\"2408.13001\\\"\\n        role: evaluation\\n        key_finding: \\\"将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。\\\"\\n        metrics:\\n          languages: 19\\n          cross_lang_max_pass1: \\\"34.4%\\\"\\n\\n      - title: \\\"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\\\"\\n        authors: \\\"Nuo Chen, Zehua Li, Keqin Bao, Junyang Lin, Dayiheng Liu (Qwen/Alibaba, HKUST-GZ, USTC)\\\"\\n        year: 2025\\n        venue: \\\"NeurIPS 2025\\\"\\n        arxiv_id: \\\"2510.23629\\\"\\n        verified: true\\n        role: direct-competitor\\n        key_finding: \\\"提出 TracePile——2.6M Chain-of-Execution trace 样本（~19B tokens），涵盖数学/算法/竞赛代码。在 4 个 base model、20 个 benchmark 上验证 trace 监督提升推理能力，但仅评估生成任务，未涉及 verdict classification。\\\"\\n        metrics:\\n          dataset_size: \\\"2.6M samples\\\"\\n          dataset_tokens: \\\"~19B\\\"\\n          benchmarks_evaluated: 20\\n\\n      - title: \\\"TRACED: Execution-aware Pre-training for Source Code\\\"\\n        authors: \\\"Yangruibo Ding, Ben Steenhoek, Kexin Pei, Gail Kaiser, Wei Le, Baishakhi Ray\\\"\\n        year: 2024\\n        venue: \\\"ICSE 2024\\\"\\n        arxiv_id: \\\"2306.07487\\\"\\n        verified: true\\n        role: direct-competitor\\n        key_finding: \\\"用源码+可执行输入+execution trace 做 execution-aware 预训练（encoder-based），在执行路径预测提升 12.4%、运行时变量值预测提升 25.2%。证明 trace 有助于 encoder-based 分类任务，但仅用于预训练而非直接做 verdict classification。\\\"\\n        metrics:\\n          execution_path_prediction_improvement: \\\"+12.4%\\\"\\n          runtime_value_prediction_improvement: \\\"+25.2%\\\"\\n\\n  code-verdict:\\n    description: \\\"LLM 判断代码 pass/fail、正确性分类、mutation testing\\\"\\n    papers:\\n      - title: \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\"\\n        authors: \\\"iSEngLab (Nanjing University)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\\\"\\n        metrics:\\n          accuracy: \\\"79.7%\\\"\\n          recall: \\\"83.2%\\\"\\n          f1_improvement_from_finetuning: \\\"+10.22%\\\"\\n\\n      - title: \\\"LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\"\\n        authors: \\\"Xin Zhou et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。\\\"\\n        metrics:\\n          accuracy: \\\"84.4%\\\"\\n          f1: \\\"86.5%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment\\\"\\n        authors: \\\"Zhenyu Yang, Jingwen Wu, Zhen Yang, Zhongxing Yu\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2505.02629\\\"\\n        arxiv_id: \\\"2505.02629\\\"\\n        role: direct-competitor\\n        key_finding: \\\"提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。\\\"\\n        metrics:\\n          accuracy_improvement: \\\"+3.1-7.5%\\\"\\n          f1_improvement: \\\"+3.0-7.1%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Calibration and Correctness of Language Models for Code\\\"\\n        authors: \\\"Claudio Spiess, David Gros, et al.\\\"\\n        year: 2025\\n        venue: \\\"ICSE 2025\\\"\\n        arxiv_id: \\\"2402.02047\\\"\\n        role: evaluation\\n        key_finding: \\\"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n        authors: \\\"Christopher Foster et al. (Meta)\\\"\\n        year: 2025\\n        venue: \\\"FSE 2025 (Industry)\\\"\\n        arxiv_id: \\\"2501.12862\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\\\"\\n        metrics:\\n          precision: \\\"0.95\\\"\\n          recall: \\\"0.96\\\"\\n          classes_evaluated: \\\"10795\\\"\\n          test_acceptance_rate: \\\"73%\\\"\\n\\n      - title: \\\"FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning\\\"\\n        authors: \\\"Ratnadira Widyasari et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"SANER 2024\\\"\\n        role: background\\n        key_finding: \\\"融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。\\\"\\n        metrics:\\n          top1_improvement_over_baseline: \\\"+32.3%\\\"\\n          top1_improvement_over_sbfl: \\\"+68.4%\\\"\\n\\n      - title: \\\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\\\"\\n        authors: \\\"Alex Gu, Baptiste Rozière, Hugh James Leather, Armando Solar-Lezama, Gabriel Synnaeve, Sida Wang\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        arxiv_id: \\\"2401.03065\\\"\\n        verified: true\\n        role: evaluation\\n        key_finding: \\\"800 个 Python 函数的代码推理 benchmark，包含 input prediction 和 output prediction 两个任务。GPT-4+CoT 达 75%/81% pass@1。作为 VOTA 实验的数据集来源。\\\"\\n        metrics:\\n          benchmark_size: 800\\n          gpt4_cot_input_pass1: \\\"75%\\\"\\n          gpt4_cot_output_pass1: \\\"81%\\\"\\n\\n  trace-compression:\\n    description: \\\"Execution trace 的压缩、摘要、抽象方法\\\"\\n    papers:\\n      - title: \\\"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\\\"\\n        authors: \\\"Aashish Yadavally, Yi Li, Tien Nguyen\\\"\\n        year: 2024\\n        venue: \\\"FSE 2024\\\"\\n        role: method-component\\n        key_finding: \\\"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\\\"\\n        metrics:\\n          exact_match: \\\"81.31%\\\"\\n          rouge_lcs: \\\"0.954\\\"\\n          fault_localization_accuracy: \\\"63.88%\\\"\\n\\n      - title: \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\"\\n        authors: \\\"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\\\"\\n        year: 2025\\n        venue: \\\"KnowledgeNLP Workshop @ ACL 2025\\\"\\n        arxiv_id: \\\"2505.04441\\\"\\n        role: background\\n        key_finding: \\\"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\\\"\\n        authors: \\\"Koshi Eguchi, Takuya Akiba\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025 Workshop PRAL\\\"\\n        openreview_id: \\\"pFyBdPyOCQ\\\"\\n        role: method-component\\n        key_finding: \\\"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\\\"\\n        metrics:\\n          cruxeval_o: \\\"70.0%\\\"\\n          livecodebench_execution: \\\"88.3%\\\"\\n\\n      - title: \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\"\\n        authors: \\\"Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu\\\"\\n        year: 2026\\n        venue: \\\"ICSE 2026\\\"\\n        arxiv_id: \\\"2602.06875\\\"\\n        verified: true\\n        role: background\\n        key_finding: \\\"在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。\\\"\\n        metrics:\\n          pass_at_1_improvement: \\\"+34.43%\\\"\\n\\n      - title: \\\"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\\\"\\n        authors: \\\"Jiaqing Wu, Tong Wu, Manqing Zhang, Yunwei Dong, Bo Shen\\\"\\n        year: 2026\\n        venue: \\\"arXiv 2604.02647\\\"\\n        arxiv_id: \\\"2604.02647\\\"\\n        verified: true\\n        role: background\\n        key_finding: \\\"Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。\\\"\\n        metrics:\\n          defects_fixed: \\\"392\\\"\\n\\n      - title: \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\"\\n        authors: \\\"Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, Shuiguang Deng\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2510.18327\\\"\\n        arxiv_id: \\\"2510.18327\\\"\\n        role: background\\n        key_finding: \\\"首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。\\\"\\n        metrics:\\n          repair_accuracy_improvement: \\\"+5.10-60.37%\\\"\\n\\n      - title: \\\"MGDebugger: From Code to Correctness via Hierarchical Debugging\\\"\\n        authors: \\\"Yuling Shi et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2410.01215\\\"\\n        role: background\\n        key_finding: \\\"层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。\\\"\\n        metrics:\\n          humaneval_accuracy: \\\"94.5%\\\"\\n          humaneval_fix_accuracy: \\\"97.6%\\\"\\n\\n  debugging-agents:\\n    description: \\\"LLM 多智能体调试框架\\\"\\n    papers:\\n      - title: \\\"UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging\\\"\\n        authors: \\\"Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2404.17153\\\"\\n        role: background\\n        key_finding: \\\"三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。\\\"\\n        metrics:\\n          defects4j_improvement: \\\"1.25-2.56x\\\"\\n\\n      - title: \\\"Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach\\\"\\n        authors: \\\"Xuanming Zhang, Yuxuan Chen, Yuan Yuan, Minlie Huang\\\"\\n        year: 2025\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv_id: \\\"2410.06949\\\"\\n        role: background\\n        key_finding: \\\"5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。\\\"\\n        metrics:\\n          exception_handling_precision_improvement: \\\"+37%\\\"\\n\\n  sft-classification:\\n    description: \\\"用 SFT 做分类任务的方法论和 findings\\\"\\n    papers:\\n      - title: \\\"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\\\"\\n        authors: \\\"Amirhossein Yousefiramandi, Ciaran Cooney\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2512.12677\\\"\\n        arxiv_id: \\\"2512.12677\\\"\\n        role: method-component\\n        key_finding: \\\"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\\\"\\n        metrics: {}\\n\\n      - title: \\\"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\\\"\\n        authors: \\\"Rohan Deb, Kiran Koshy Thekumparampil, Kousha Kalantari, Gaurush Hiranandani, Shoham Sabach, Branislav Kveton\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025\\\"\\n        arxiv_id: \\\"2505.14826\\\"\\n        role: background\\n        key_finding: \\\"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\\\"\\n        authors: \\\"Martin Juan Jose Bucher, Marco Martini\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2406.08660\\\"\\n        role: background\\n        key_finding: \\\"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\\\"\\n        metrics: {}\\n\\n  cross-model-generalization:\\n    description: \\\"跨模型 SFT 泛化：不同 base model 上 SFT 效果的迁移与差异\\\"\\n    papers:\\n      - title: \\\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\\\"\\n        authors: \\\"Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng Ann Heng, Wai Lam\\\"\\n        year: 2024\\n        venue: \\\"NAACL 2024\\\"\\n        arxiv_id: \\\"2403.09162\\\"\\n        role: method-component\\n        key_finding: \\\"SFT 后分类任务跨域正迁移，生成任务跨域负迁移。对 VOTA 的跨模型实验设计有直接参考——verdict 分类属于分类任务，预期正迁移。\\\"\\n        metrics: {}\\n\\n      - title: \\\"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\\\"\\n        authors: \\\"Guanting Dong, Hongyi Yuan, Keming Lu, et al.\\\"\\n        year: 2024\\n        venue: \\\"ACL 2024\\\"\\n        arxiv_id: \\\"2310.05492\\\"\\n        role: method-component\\n        key_finding: \\\"更大/更强 base model 在相同 SFT 数据量下性能更优。DeepSeek-Coder-6.7B 预训练 2T tokens，Qwen 5.5T，比例 2.75x。对 VOTA 跨模型对比（DeepSeek vs Qwen）提供预训练数据量的基准参考。\\\"\\n        metrics:\\n          deepseek_coder_pretrain_tokens: \\\"2T\\\"\\n          qwen_pretrain_tokens: \\\"5.5T\\\"\\n\\n      - title: \\\"Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels\\\"\\n        authors: \\\"Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2509.16596\\\"\\n        role: background\\n        key_finding: \\\"SFT 中 90% 参数更新不贡献知识增强；知识掌握水平不同的训练数据导致 >12% 性能波动。对 VOTA 的数据质量控制有参考意义。\\\"\\n        metrics:\\n          non_contributing_param_ratio: \\\"90%\\\"\\n          performance_variation_from_data_quality: \\\">12%\\\"\\n\\n      - title: \\\"From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT\\\"\\n        authors: \\\"Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2605.03686\\\"\\n        arxiv_id: \\\"2605.03686\\\"\\n        role: background\\n        key_finding: \\\"DeepSeek-Coder-7B-Instruct LoRA 微调做代码分类 80% accuracy。验证 DeepSeek-Coder 系列在代码分类 SFT 上的可行性。\\\"\\n        metrics:\\n          code_classification_accuracy: \\\"80%\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, et al. (Qwen Team)\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2409.12186\\\"\\n        arxiv_id: \\\"2409.12186\\\"\\n        role: background\\n        key_finding: \\\"Qwen2.5-Coder 5.5T tokens 预训练，HumanEval 92.7%。作为 VOTA 跨模型实验的 base model 之一，提供预训练规模和代码能力基准。\\\"\\n        metrics:\\n          pretrain_tokens: \\\"5.5T\\\"\\n          humaneval_pass1: \\\"92.7%\\\"\\n\\nmeta:\\n  last_updated: \\\"2026-05-15\\\"\\n  total_papers: 34\\n  search_scope: \\\"2024-2026, top ML/NLP/SE venues\\\"\\n  scan_date: \\\"2026-05-15\\\"\\n  scan_queries: 16\\n  key_gaps:\\n    - \\\"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\\\"\\n    - \\\"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\\\"\\n    - \\\"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\\\"\\n    - \\\"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\\\"\\n    - \\\"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\\\"\\n\", \"total_chars\": 18596, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbb5c4cb-baa5-4dd9-a7b6-869cb4ec1e91",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "fea3fc04-289f-4b9f-afdf-a5c586d6176d",
  "sourceToolAssistantUUID": "bbb5c4cb-baa5-4dd9-a7b6-869cb4ec1e91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T14:08:24.404Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014XEcYgWTp71pXfuvWjHBRM`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fea3fc04-289f-4b9f-afdf-a5c586d6176d",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAZdUCArCqeN7S2Jav2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70c54387-2452-4876-8699-be682f5dc9c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxzYerR8PdfgYaBRvNtR7G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 12 · 2026-05-18T14:08:24.413Z_

<details><summary>↩ Tool result · `toolu_014XEcYgWTp71pXfuvWjHBRM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'trace-verdict-study'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70c54387-2452-4876-8699-be682f5dc9c8",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "14cdf9e1-97ad-458d-b9b1-fd268b13959f",
  "sourceToolAssistantUUID": "70c54387-2452-4876-8699-be682f5dc9c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T14:08:25.243Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LFEda3hKBARxAgDvVXb1az`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14cdf9e1-97ad-458d-b9b1-fd268b13959f",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAZdUCArCqeN7S2Jav2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bd224cb-dfae-4454-88d3-388e995626eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxzYerR8PdfgYaBRvNtR7G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16947,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 383,
          "cache_read_input_tokens": 16947,
          "cache_creation_input_tokens": 1289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1289,
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

_source line 14 · 2026-05-18T14:08:25.263Z_

<details><summary>↩ Tool result · `toolu_01LFEda3hKBARxAgDvVXb1az`</summary>

```text
artifacts/dream_reports/dream_20260515T013018/best/paper.tex
artifacts/dream_reports/dream_20260515T013018/median/paper.tex
artifacts/dream_reports/dream_20260515T013018/worst/paper.tex
artifacts/dream_reports/dream_20260515T084908/best/paper.tex
artifacts/dream_reports/dream_20260515T084908/median/paper.tex
artifacts/dream_reports/dream_20260515T084908/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/per_class_breakdown.tex
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex
artifacts/_project/paper/section3_experimental_setup.tex
artifacts/_project/paper/ethics_statement.tex
artifacts/_project/paper/ethics_statement_77cf5f.tex
artifacts/_project/paper/arr_checklist.tex
artifacts/_project/paper/main_results_tables.tex
artifacts/_project/paper/main_results_tables_d8c8b6.tex
artifacts/paper_tables/main_results_tables.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260516T105259/best/paper.tex
artifacts/dream_reports/dream_20260516T105259/median/paper.tex
artifacts/dream_reports/dream_20260516T105259/worst/paper.tex
artifacts/dream_reports/dream_20260516T155731/best/paper.tex
artifacts/dream_reports/dream_20260516T155731/median/paper.tex
artifacts/dream_reports/dream_20260516T155731/worst/paper.tex
docs/paper/arr_checklist.tex
docs/paper/method.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/appendix.tex
docs/paper/experiments.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
artifacts/dream_reports/dream_20260518T113804/best/paper.tex
artifacts/dream_reports/dream_20260518T113804/median/paper.tex
artifacts/dream_reports/dream_20260518T113804/worst/paper.tex
artifacts/dream_reports/dream_20260518T125926/best/paper.tex
artifacts/dream_reports/dream_20260518T125926/median/paper.tex
artifacts/dream_reports/dream_20260518T125926/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bd224cb-dfae-4454-88d3-388e995626eb",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "8a3e863d-1c1c-4544-a6c0-0a93415eeb5b",
  "sourceToolAssistantUUID": "4bd224cb-dfae-4454-88d3-388e995626eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T14:08:28.340Z_

Now let me read the actual paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a3e863d-1c1c-4544-a6c0-0a93415eeb5b",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAa42owTxKYtZNAMvBp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dcfa164-4276-4702-b74b-a90d4db4b51f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1xo6ap5W8VZoFtuNRofCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 18236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11653,
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

_source line 16 · 2026-05-18T14:08:29.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_016yVgVuRfrb3JzdqPBXio1f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dcfa164-4276-4702-b74b-a90d4db4b51f",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAa42owTxKYtZNAMvBp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57d84e2a-bfff-4818-ba28-ec2aa3da06db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1xo6ap5W8VZoFtuNRofCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 18236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11653,
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

_source line 17 · 2026-05-18T14:08:29.760Z_

<details><summary>↩ Tool result · `toolu_016yVgVuRfrb3JzdqPBXio1f`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	% \usepackage{acl}  % uncomment for camera-ready (remove [review])
4	\usepackage{times,latexsym}
5	\usepackage{amsmath,amssymb}
6	\usepackage{graphicx}
7	\graphicspath{{../../figures/paper/}}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Exception Events Are All You Need: \\Component Ablation for Trace-Based Verdict Prediction}
13	\author{Anonymous ACL submission}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	Execution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.
20	We present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models spanning three architecture families and 1.5B to 13B parameters.
21	Exception events alone achieve ${\geq}$99.33\% accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while a code-only baseline shows 9.19pp scale sensitivity (67.3--76.5\%).
22	Adding more trace information actively hurts: a multi-component representation underperforms exception-only, and the full-trace gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%).
23	Tail-truncation experiments reveal that diagnostic signal concentrates near the trace terminus (in a localized window, not the absolute end), recovering 86\% of the gap to exception-only.
24	A format-marker ablation confirms ${\sim}$91\% of the exception signal is semantic (learned by SFT to distinguish caught from uncaught exceptions) rather than format-driven.
25	These results reveal a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99\%, while Tier~2 (loop compression) reaches 85.6\%.
26	Cross-dataset evaluation on DebugBench ($N{=}426$) confirms generalization, with exception-only achieving 100\%.
27	We reframe verdict prediction as fault detection: the minimal sufficient signal is a compact exception event (median 150 tokens) that is scale-invariant, architecture-independent, and deployable in token-constrained settings.
28	\end{abstract}
29	
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{discussion}
34	\input{related_work}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	Our study has several limitations.
40	First, our primary experiments use a single dataset (591 problems from HumanEval and MBPP-sanitized); while a cross-dataset evaluation on DebugBench (\S\ref{sec:debugbench}) confirms that exception dominance generalizes to synthetically injected bugs, generalization to other languages, larger codebases, or real-world fault distributions remains untested.
41	Second, while we evaluate four models spanning 1.5B to 13B parameters across three architecture families, all are code-specialized; generalization to general-purpose models or larger scales remains untested.
42	Third, DeepSeek \texttt{exception\_only} exhibits seed-dependent variance: 2/3 seeds achieve 99.33\% while seed 123 yields 91.09\% ($\sigma{=}4.76$pp, $n{=}3$), which we hypothesize reflects LoRA initialization sensitivity in DeepSeek-Coder, though direct evidence is lacking (fail recall = 70.5\% for the outlier vs.\ 100\% for others).
43	Qwen \texttt{exception\_only} shows perfect seed robustness ($\sigma{=}0$, $n{=}3$), but Qwen \texttt{ae\_only} also exhibits seed variance ($\sigma{=}$0.40pp; seed 123 = 99.08\% vs.\ seeds 42/456 = 99.92\%), though far smaller than DeepSeek's ($\sigma{=}$4.76pp).
44	Whether training stabilization techniques can eliminate DeepSeek's seed sensitivity is unexplored; other conditions use a single seed.
45	Fourth, the initial DeepSeek \texttt{full\_trace} run was invalidated by context overflow; a re-run with extended context yields 79.16\% (CI [76.80\%, 81.30\%]), 2.60pp below Qwen (Table~\ref{tab:cross_model}).
46	Fifth, the candidate solutions were generated by Qwen-2.5-Coder-7B-Instruct, which also serves as one of our evaluation models; this does not affect verdict prediction but may influence the pass/fail distribution.
47	Sixth, self-familiarity bias may inflate absolute accuracy: both Qwen-2.5-Coder and DeepSeek-Coder were likely exposed to HumanEval and MBPP solutions during pretraining, so the models may partially recognize solutions rather than purely reasoning from trace signals; our cross-dataset evaluation on DebugBench mitigates but does not eliminate this concern.
48	Seventh, the error distribution in our test set may not reflect real-world fault distributions: exceptions (especially \texttt{TypeError}, \texttt{ValueError}) dominate LLM-generated failures, but production code may exhibit a broader spectrum of silent logic errors where no exception is raised, potentially reducing the effectiveness of exception-based verdict prediction.
49	Finally, our analysis is limited to verdict prediction; whether exception dominance extends to other classification tasks or generation tasks is an open question.
50	
51	\section*{Ethics Statement}
52	
53	This work uses publicly available benchmarks (HumanEval, MBPP-sanitized, DebugBench) and does not involve human subjects, crowdsourced annotations, or personally identifiable information.
54	All models evaluated are open-source and publicly accessible.
55	Training uses parameter-efficient LoRA fine-tuning on two RTX PRO 6000 Blackwell GPUs, with each experiment using a single GPU and total compute under 20 GPU-hours across all experiments, resulting in minimal environmental impact.
56	We do not foresee direct negative societal impacts from this work; verdict prediction is a developer-facing tool for automated testing.
57	
58	\bibliography{references}
59	
60	\appendix
61	\input{appendix}
62	
63	\end{document}
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57d84e2a-bfff-4818-ba28-ec2aa3da06db",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "a2fdf0a3-03ab-4293-87f1-4015a72bec0c",
  "sourceToolAssistantUUID": "57d84e2a-bfff-4818-ba28-ec2aa3da06db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T14:08:30.236Z_

<details open><summary>🔧 Tool call — Read · `toolu_0186Ro5ATtxaQLzxFinTbYbZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2fdf0a3-03ab-4293-87f1-4015a72bec0c",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAa42owTxKYtZNAMvBp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1c4402c-c349-478a-80a7-775fa7eef4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1xo6ap5W8VZoFtuNRofCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 18236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11653,
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

_source line 19 · 2026-05-18T14:08:30.241Z_

<details><summary>↩ Tool result · `toolu_0186Ro5ATtxaQLzxFinTbYbZ`</summary>

```text
1	\section{Introduction}
2	
3	Execution traces (line-by-line records of a program's runtime behavior) have emerged as a promising input modality for code language models \citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}.
4	Yet feeding thousands of trace lines to a model can be no better than feeding none: the diagnostic signal drowns in routine execution steps.
5	\emph{Which trace components actually carry the signal that matters?}
6	
7	Prior work found no single trace representation consistently outperforms others \citep{wang2025dcsh}, but focused on generation-oriented tasks.
8	\emph{Verdict prediction}, classifying whether a test passes or fails, is fundamentally different: it is fault detection, not generation.
9	The model need not simulate execution; it need only determine whether something went wrong.
10	This distinction suggests that a small, fault-specific trace component may suffice.
11	
12	We test this hypothesis through the first systematic component ablation of trace representations for verdict prediction.
13	Using 591 problems from HumanEval \citep{chen2021evaluating} and MBPP-sanitized \citep{austin2021program}, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components across four models spanning 1.5B to 13B parameters and three architecture families: Qwen-2.5-Coder-7B/1.5B-Instruct \citep{qwen2025coder}, CodeLlama-13B-Instruct \citep{roziere2024code}, and DeepSeek-Coder-6.7B-Instruct \citep{deepseek2024coder}.
14	
15	\textbf{Exception events alone achieve ${\geq}$99.33\% verdict accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%).}
16	This near-perfect accuracy holds from 1.5B to 13B parameters, while the code-only baseline (\texttt{no\_trace}) varies from 67.3\% to 76.5\% with strong scale dependence.
17	The exception signal eliminates the need for model capacity to compensate for missing information.
18	
19	More surprisingly, adding trace information beyond exceptions actively \emph{hurts}: VOTA (99.41\%) underperforms \texttt{exception\_only} (99.83\%), and the degradation reaches 14.96pp on DeepSeek, compounded by tokenizer-driven truncation.
20	We approximately decompose this gap: ${\sim}$74\% stems from information overload (irrelevant trace content at inference) and ${\sim}$26\% from gradient dilution (dispersed training signal).
21	Tail-truncation experiments across four models and three architecture families confirm the mechanism: a sharp phase transition at ${\sim}$500 tail tokens (matching the typical exception traceback length) separates near-baseline from near-ceiling accuracy, and \texttt{tail\_2048} captures 95--98\% of \texttt{exception\_only}'s performance.
22	
23	Our contributions:
24	\begin{enumerate}
25	\item \textbf{Exception events are the minimal sufficient signal}: ${\geq}$99.33\% across four models and three families (1.5B--13B), with ${\sim}$91\% of the signal being semantic rather than format-driven (\S\ref{sec:cross_model}, \S\ref{sec:nomarker}). SFT closes a 6--49pp zero-shot gap across four models and three architecture families, and outperforms both few-shot prompting and the best regex heuristic (\S\ref{sec:ablation}). Cross-dataset evaluation on DebugBench ($N{=}426$) yields 100\% (\S\ref{sec:debugbench}).
26	\item \textbf{Richer traces actively hurt}: We approximately decompose why into gradient dilution (${\sim}$26\%) and information overload (${\sim}$74\%). A budget sweep across four models and three families reveals a phase transition at ${\sim}$500 tail tokens, with \texttt{tail\_2048} recovering 95--98\% of \texttt{exception\_only} (\S\ref{sec:density}, \S\ref{sec:trace_length}).
27	\item \textbf{Two-tier diagnostic hierarchy}: Tier~1 signals (exceptions, assertions) individually achieve ${\geq}$99\%; Tier~2 (loop compression) reaches 85.6\%, still +10.5pp over no trace (\S\ref{sec:ablation}).
28	\end{enumerate}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1c4402c-c349-478a-80a7-775fa7eef4b3",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "cf5f11ec-dd8d-4050-939b-c5db444ccb7d",
  "sourceToolAssistantUUID": "f1c4402c-c349-478a-80a7-775fa7eef4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T14:08:30.700Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NuQ3xc4zc4MShFiKNdNLN7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf5f11ec-dd8d-4050-939b-c5db444ccb7d",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAa42owTxKYtZNAMvBp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47aadfb3-ab2e-418f-912a-4cb2e34f4637",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1xo6ap5W8VZoFtuNRofCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 18236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11653,
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

_source line 21 · 2026-05-18T14:08:30.704Z_

<details><summary>↩ Tool result · `toolu_01NuQ3xc4zc4MShFiKNdNLN7`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Execution Traces for Code LLMs.}
4	TracePile \citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples; \citet{wang2025dcsh} found trace utility to be task- and format-dependent, a finding we extend by identifying exception events as the dominant signal for verdict prediction.
5	NExT \citep{ni2024next} and ET-CoT \citep{eguchi2025etcot} leveraged trace chain-of-thought for repair and execution reasoning.
6	\citet{ferrando2025execute} found compact traces comparable to full traces, supporting our information density finding.
7	CRUXEval \citep{gu2024cruxeval} established execution reasoning benchmarks, extended to 19 languages by \citet{xu2025cruxevalx}.
8	None decompose which trace components contribute to \emph{classification} accuracy.
9	
10	\paragraph{Code Verdict and Patch Classification.}
11	TRACED \citep{ding2024traced} showed execution-aware pretraining improves vulnerability and clone detection.
12	In patch correctness, APPT \citep{appt2024} achieved 79.7\% with BERT+LSTM; LLM4PatchCorrect \citep{zhou2024llm4patch} reached 84.4\% using execution traces.
13	FuseFL \citep{widyasari2024fusefl} demonstrated that structured fault signals improve fault localization.
14	\citet{foster2025mutation} deployed LLM-based equivalence detection at Meta with 0.95 precision.
15	These approaches treat traces as monolithic inputs; none isolate individual components, compare against rule-based baselines to quantify the value of learned representations, or test cross-model generalization.
16	
17	\paragraph{Fault Localization.}
18	Spectrum-based fault localization (SBFL) ranks program elements by statistical suspiciousness computed from passing/failing test spectra.
19	Classic metrics (Ochiai \citep{abreu2007accuracy}, Tarantula \citep{jones2002visualization}, DStar \citep{wong2014dstar}) share a core insight with our work: abnormal execution events (here, coverage patterns correlated with failure) are the most informative diagnostic signal.
20	Recent LLM-based approaches extend this: AutoFL \citep{kang2024autofl} uses function-level call graphs with ChatGPT; AgentFL \citep{qin2024agentfl} introduces multi-agent localization; LLM4FL \citep{widyasari2024llm4fl} combines SBFL spectra with LLM reasoning; and \citet{mukherjee2025llmfl} demonstrate that LLMs can localize faults from test failure information alone.
21	Verdict prediction is a prerequisite to fault localization: one must first determine \emph{whether} a fault exists before localizing \emph{where} it is.
22	Our exception-based approach and SBFL share the principle that anomalous execution events carry the strongest diagnostic signal, but operate at different granularities: we classify at the test level (pass/fail) while FL localizes at the statement or method level.
23	
24	\paragraph{Trace Compression and Selection.}
25	TraceCoder \citep{huang2026tracecoder} and InspectCoder \citep{wang2025inspectcoder} use selective trace extraction for debugging; \citet{haque2025traces} found raw traces provide limited repair benefit, supporting our compression finding.
26	Our approximate information density decomposition (gradient dilution ${\sim}$26\% vs.\ information overload ${\sim}$74\%) provides the first quantitative framework for \emph{why} compression helps, complementing these methods' focus on \emph{how} to compress.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47aadfb3-ab2e-418f-912a-4cb2e34f4637",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "88d14984-d9e1-46e6-93c3-fb208074d840",
  "sourceToolAssistantUUID": "47aadfb3-ab2e-418f-912a-4cb2e34f4637",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T14:08:31.189Z_

<details open><summary>🔧 Tool call — Read · `toolu_012odSzXCH3iHnSQn1MKCko1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88d14984-d9e1-46e6-93c3-fb208074d840",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAa42owTxKYtZNAMvBp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dcf0e46-5ffb-48b9-a544-fa566991e622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1xo6ap5W8VZoFtuNRofCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 18236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11653,
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

_source line 23 · 2026-05-18T14:08:31.200Z_

<details><summary>↩ Tool result · `toolu_012odSzXCH3iHnSQn1MKCko1`</summary>

```text
1	\section{Method}
2	
3	\subsection{Task Definition}
4	
5	We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
6	The model produces a single token (\texttt{pass} or \texttt{fail}), making this a binary classification task.
7	Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution.
8	
9	\subsection{Dataset}
10	\label{sec:dataset}
11	
12	We sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\_p 0.95) for 591 problems from HumanEval \citep{chen2021evaluating} (164) and MBPP-sanitized \citep{austin2021program} (427), executed each against canonical tests with \texttt{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\% pass, 33\% fail).
13	The dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\%).
14	The \texttt{exception\_only} format collapses passing solutions into identical rows (39.45\% train, 48.99\% test duplicates); train--test input overlap is zero (Appendix~\ref{sec:dedup_stats}).
15	
16	\subsection{Trace Representations}
17	
18	We define seven conditions that vary the trace information available (Figure~\ref{fig:trace_overview}):
19	\begin{itemize}
20	\item \texttt{no\_trace}: Source code and test input only.
21	\item \texttt{full\_trace}: Complete line-by-line trace with variable states.
22	\item \texttt{VOTA}: Exception events + assertion-point comparisons + loop compression.
23	\item \texttt{exception\_only}: Only exception/error events.
24	\item \texttt{ae\_only}: Only assertion-point actual/expected pairs.
25	\item \texttt{loop\_only}: Only loop compression summaries.
26	\item \texttt{VOTA\_no\_ae}: VOTA without assertion-point information.
27	\end{itemize}
28	
29	\begin{figure*}[t]
30	\centering
31	\includegraphics[width=\textwidth]{fig1_trace_overview}
32	\caption{Overview of the verdict prediction pipeline. Source code and a test input are executed to produce a full raw trace. Four conditions vary the trace information: \texttt{no\_trace} (75.13\%), \texttt{full\_trace} (81.76\%), VOTA (99.41\%), and \texttt{exception\_only} (99.83\%). Accuracies for Qwen-2.5-7B (seed=42, $N{=}1{,}190$).}
33	\label{fig:trace_overview}
34	\end{figure*}
35	
36	\subsection{Models and Training}
37	
38	We evaluate four models spanning three architecture families: \textbf{Qwen-2.5-Coder-7B/1.5B-Instruct} \citep{qwen2025coder}, \textbf{CodeLlama-13B-Instruct} \citep{roziere2024code}, and \textbf{DeepSeek-Coder-6.7B-Instruct} \citep{deepseek2024coder}, covering a 1.5B--13B parameter range (8.7$\times$).
39	All conditions use LoRA \citep{hu2022lora} (rank=16, $\alpha$=32, dropout=0.05) on all linear layers, 3 epochs, effective batch size 32, LR $2 \times 10^{-4}$ with linear warmup/decay, max sequence length 2{,}048 tokens.
40	Sequences exceeding this limit are truncated while preserving the verdict label.
41	The primary seed is 42; seeds 123 and 456 test \texttt{exception\_only} robustness (Appendix~\ref{sec:training_details}).
42	
43	\subsection{Loss Ablation}
44	
45	To disentangle training signal from input signal quality, we introduce \texttt{full\_trace\_label\_only}: identical full-trace input but loss computed only on the verdict token (trace positions masked).
46	Improvement over standard \texttt{full\_trace} is attributable to \emph{gradient dilution}; the remaining gap to VOTA reflects \emph{information overload} at inference time.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dcf0e46-5ffb-48b9-a544-fa566991e622",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "e4cc63d7-3206-48e4-976f-18d53e1b5924",
  "sourceToolAssistantUUID": "8dcf0e46-5ffb-48b9-a544-fa566991e622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T14:08:31.642Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HxeVTBJj1ZnY4PjQD8Du75`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4cc63d7-3206-48e4-976f-18d53e1b5924",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAa42owTxKYtZNAMvBp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77514bd3-3922-4143-83ad-fdf8a58b941f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1xo6ap5W8VZoFtuNRofCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 18236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11653,
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

_source line 25 · 2026-05-18T14:08:31.648Z_

<details><summary>↩ Tool result · `toolu_01HxeVTBJj1ZnY4PjQD8Du75`</summary>

```text
1	\section{Experiments}
2	
3	We evaluate across two research questions:
4	(1)~Do Tier~1 exception signals generalize across models?
5	(2)~What is the relative contribution of each trace component?
6	All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.
8	
9	\subsection{Cross-Model Comparison}
10	\label{sec:cross_model}
11	
12	Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.
13	
14	\begin{table}[t]
15	\centering
16	\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\pm$std (3 seeds). $^\dag$2/3 seeds; one seed excluded due to LoRA initialization failure (91.09\%, fail recall = 70.5\%; see Appendix~\ref{sec:training_dynamics}). \texttt{ae\_only} and \texttt{loop\_only} ablations tested on Qwen-7B (3 seeds) to isolate component contributions; cross-model validation focused on the primary conditions. Full CIs in Appendix~\ref{sec:full_results}.}
17	\label{tab:cross_model}
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{lcccc}
21	\toprule
22	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{CL-13B} & \textbf{DS-6.7B} \\
23	\midrule
24	exception\_only & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.83} & \textbf{99.89}{\scriptsize$\pm$0.10} & \textbf{99.33}$^\dag$ \\
25	ae\_only & 99.64{\scriptsize$\pm$0.49} & --- & --- & --- \\
26	VOTA & 99.41 & 99.58 & 98.57 & 84.45 \\
27	no\_trace & 75.13 & 67.31 & 76.50 & 73.36 \\
28	\midrule
29	Majority baseline & \multicolumn{4}{c}{71.51} \\
30	\bottomrule
31	\end{tabular}%
32	}
33	\end{table}
34	
35	\paragraph{Exception dominance across families.}
36	Under \texttt{exception\_only}, the Qwen and CodeLlama families achieve ${\geq}$99.83\% (mean): Qwen-7B (99.83\%$\pm$0.00, 3 seeds), Qwen-1.5B (99.83\%), and CodeLlama-13B (99.89\%$\pm$0.10, 3 seeds; seed 123 achieves 100\%).
37	DeepSeek-6.7B reaches 99.33\% on 2/3 seeds with one LoRA-sensitivity outlier at 91.09\% (seed 123; fail recall = 70.5\%); even the outlier outperforms VOTA (84.45\%) by 6.64pp.
38	Excluding the DeepSeek outlier, the cross-model range is 0.56pp (99.33--99.89\%), the tightest of any condition.
39	
40	\paragraph{Scale invariance of exception signals.}
41	Exception-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\%+ on the same representation.
42	CodeLlama-13B seed 123 achieves 100\% (0/1190 errors), confirming that Qwen's two persistent errors (from \texttt{GeneratorExit}; Appendix~\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.
43	In contrast, \texttt{no\_trace} scales monotonically with capacity: 67.31\% (1.5B) $\to$ 75.13\% (7B) $\to$ 76.50\% (13B), a 9.19pp range that exception events completely eliminate (Figure~\ref{fig:cross_scale}).
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=\columnwidth]{fig3_cross_model_gap}
48	\caption{Verdict accuracy vs.\ model scale. \texttt{exception\_only} maintains ${\geq}$99.33\% regardless of scale (1.5B--13B), while \texttt{no\_trace} shows monotonic scale sensitivity (+9.19pp from 1.5B to 13B). The \texttt{nomarker} condition (format markers removed) shows no degradation at smaller scale (${\sim}$97.7--97.8\%).}
49	\label{fig:cross_scale}
50	\end{figure}
51	
52	\paragraph{VOTA cross-family variation.}
53	VOTA accuracy varies across families: 99.58\% (Qwen-1.5B) $>$ 99.41\% (Qwen-7B) $>$ 98.57\% (CodeLlama-13B; \texttt{codellama13b\_vota\_seed42}, CI [97.9, 99.2]) $\gg$ 84.45\% (DeepSeek-6.7B).
54	The CodeLlama result (17 errors) narrows the gap: among models without tokenizer-driven truncation, the VOTA range is only 1.01pp (98.57--99.58\%), suggesting that the 14.96pp DeepSeek deficit is primarily a truncation artifact rather than an inherent model capability limitation (91.7\% of DeepSeek training samples were affected; Appendix~\ref{sec:tokenizer_analysis}).
55	In contrast, \texttt{exception\_only} inputs are compact (median 150 tokens, mean 398 due to verbose fail-class exceptions), making the cross-model comparison clean.
56	
57	\subsection{Component Ablation}
58	\label{sec:ablation}
59	
60	We restrict \texttt{ae\_only} and \texttt{loop\_only} ablations to Qwen-7B, as these component-level analyses target the trace composition mechanism rather than cross-model generalization.
61	Table~\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B (seed=42) and reveals a two-tier hierarchy.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. $^\dag$\texttt{ae\_only}: 3-seed mean 99.64\% ($\pm$0.49; seeds 42: 99.92, 123: 99.08, 456: 99.92). \texttt{exception\_only}: 99.83\% ($\pm$0.00, 3 seeds), more stable ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).}
66	\label{tab:ablation}
67	\small
68	\resizebox{\columnwidth}{!}{%
69	\begin{tabular}{llccc}
70	\toprule
71	\textbf{Condition} & \textbf{Components} & \textbf{Acc (\%)} & \textbf{95\% CI} & \textbf{Tier} \\
72	\midrule
73	ae\_only & assertion-point & 99.64$^\dag$ & [99.26, 99.87] & 1 \\
74	exception\_only & exception events & \textbf{99.83} & [99.58, 100.00] & 1 \\
75	VOTA & exc+ae+loop & 99.41 & [98.82, 99.83] & --- \\
76	VOTA\_no\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\
77	loop\_only & loop compression & 85.63 & [83.53, 87.56] & 2 \\
78	full\_trace & complete trace & 81.76 & [79.70, 83.90] & --- \\
79	no\_trace & none & 75.13 & [72.77, 77.48] & --- \\
80	\midrule
81	Regex (best) & exc.\ type regex & 93.61 & --- & --- \\
82	3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\
83	Zero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\
84	\bottomrule
85	\end{tabular}%
86	}
87	\end{table}
88	
89	Tier~1 signals are individually sufficient: \texttt{ae\_only} (3-seed mean 99.64\% $\pm$ 0.49) and \texttt{exception\_only} (99.83\% $\pm$ 0.00) both exceed VOTA ($p{=}0.01$), implying that combining signals introduces noise; \texttt{exception\_only} is more stable across seeds ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).
90	Removing assertion points has no effect (\texttt{VOTA\_no\_ae} = 99.41\%), confirming exception dominance.
91	Tier~2 \texttt{loop\_only} (85.63\%) improves 10.50pp over \texttt{no\_trace} ($p{<}0.0001$) but falls far short of Tier~1.
92	\paragraph{Rule-based baseline comparison.}
93	The strongest non-trivial regex heuristic (B4: exception class name matching) achieves 93.61\% accuracy (F1=0.876), trailing SFT \texttt{exception\_only} (99.83\%, F1=0.997) by 6.22pp (McNemar $p{<}0.001$).
94	The gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\ref{sec:regex_baselines}).
95	Across trace formats, SFT consistently outperforms the best applicable regex, from +3.62pp (\texttt{no\_trace} over majority baseline) to +23.86pp (VOTA), with the largest gains on formats requiring semantic interpretation (Appendix~\ref{sec:regex_baselines}).
96	
97	\paragraph{Zero-shot and few-shot LLM baselines.}
98	Zero-shot prompting spans 51.0--93.5\% across four models (CodeLlama-13B: 51.01\%, Qwen-7B: 89.08\%, DeepSeek-6.7B: 90.59\%, Qwen-1.5B: 93.45\%), a 42.44pp range that SFT compresses to 0.56pp (99.33--99.89\%).
99	Zero-shot performance does not correlate with model size: Qwen-1.5B (93.45\%) outperforms both Qwen-7B (89.08\%) and CodeLlama-13B (51.01\%), indicating that pretraining data distribution, not capacity, determines zero-shot verdict ability.
100	CodeLlama-13B drops below the majority baseline (71.51\%), showing extreme fail bias (72.4\% of predictions are \texttt{fail}).
101	Three-shot in-context learning on Qwen-7B (90.84\%, fail recall = 80.53\%) improves only 1.76pp over zero-shot and still trails both the regex heuristic (93.61\%) and SFT by 8.99pp, confirming that a few examples cannot substitute for task-specific fine-tuning.
102	SFT normalizes this cross-architecture variance, closing a 6--49pp gap to ${\geq}$99.33\% across all models with 4,720 training samples (Appendix~\ref{sec:zeroshot_cross_model}).
103	
104	\subsection{Format Marker Ablation}
105	\label{sec:nomarker}
106	
107	The \texttt{exception\_only} format includes a \texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\% accuracy; Appendix~\ref{sec:regex_baselines}).
108	To quantify the marker's contribution, we retrain with all format markers removed (\texttt{nomarker} condition).
109	
110	Qwen-7B 3-seed mean: 97.65\% $\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\%), a drop of 2.18pp from \texttt{exception\_only} (99.83\%).
111	Qwen-1.5B: 97.82\%, drop of 2.01pp.
112	The marker contribution (${\sim}$2pp) accounts for only ${\sim}$9\% of the total exception lift over \texttt{no\_trace} (24.70pp on 7B).
113	Exception events thus provide two signal layers that show no degradation at smaller scale: structural markers (${\sim}$2pp, regex-learnable) and semantic exception content (${\sim}$22pp, requiring SFT to distinguish caught from uncaught exceptions).
114	
115	\subsection{Information Density Decomposition}
116	\label{sec:density}
117	
118	The 17.65pp gap between \texttt{full\_trace} (81.76\%) and VOTA (99.41\%) decomposes via \texttt{full\_trace\_label\_only}, which retains the full trace but masks all trace tokens from the loss.
119	
120	\begin{table}[t]
121	\centering
122	\caption{Approximate information density decomposition: gradient dilution (${\sim}$26\%) vs.\ information overload (${\sim}$74\%).}
123	\label{tab:density}
124	\small
125	\begin{tabular}{lccc}
126	\toprule
127	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs.\ full\_trace} & \textbf{Gap explained} \\
128	\midrule
129	full\_trace & 81.76 & --- & --- \\
130	label\_only & 86.22 & +4.46pp & 26\% \\
131	VOTA & 99.41 & +17.65pp & 100\% \\
132	\bottomrule
133	\end{tabular}
134	\end{table}
135	
136	Gradient dilution accounts for approximately 26\% of the gap (+4.46pp, $p{<}0.0001$, bootstrap 95\% CI $[{+}2.35, {+}6.55]$): when the model no longer wastes gradient updates on predicting trace tokens, accuracy improves even with identical input.
137	The remaining ${\sim}$74\% (+13.19pp) reflects information overload at inference: the model receives thousands of irrelevant trace lines that compete for attention with the diagnostic signal, regardless of loss design.
138	This asymmetry implies that trace compression methods should prioritize \emph{content selection} (removing irrelevant lines) over \emph{loss engineering} (masking non-target tokens), as the larger bottleneck is what the model sees, not how it is trained.
139	The two factors may interact, so this decomposition is approximate.
140	
141	\subsection{Additional Analyses}
142	\label{sec:additional}
143	
144	\paragraph{Trace length ablation.}
145	\label{sec:trace_length}
146	Varying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\%--81.8\% band with a non-monotonic pattern: 1024-token prefixes (77.23\%) underperform 512-token prefixes (80.42\%, $p{=}0.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\ref{sec:trace_length_full}).
147	This non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\to$tail-2048 ($-$1.5pp).
148	
149	\paragraph{Truncation direction and budget curve.}
150	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: among the three models with complete data, tail-2048 exceeds head-2048 by 15.5--22.6pp, with the gap widening at smaller scale (Qwen-1.5B: +22.6pp vs.\ Qwen-7B: +15.5pp; Appendix~\ref{sec:trace_length_full}, Table~\ref{tab:head_vs_tail}).
151	All four models' head-2048 accuracies converge into a narrow 75.3--81.8\% band (6.5pp), comparable to the tail-256 band (72.6--78.9\%, 6.3pp), indicating that signal-poor conditions produce a shared performance floor regardless of scale or architecture.
152	
153	A cross-model budget sweep across four models and three architecture families reveals a sharp phase transition at 256$\to$512 tail tokens: all four models jump +14.7--23.0pp in a single budget doubling, crossing from near-baseline (${\sim}$73--79\%) to near-ceiling (${\sim}$94--98\%).
154	The threshold aligns with the typical exception traceback length (${\sim}$500 tokens): below it, the diagnostic event is truncated; above it, the event is captured regardless of architecture or scale.
155	Beyond 512 tokens, accuracy converges further; where tail-1024 data is available, three models reach a 96.5--96.6\% band, eliminating the 6.3pp cross-model spread observed at tail-256 (Table~\ref{tab:tail_cross_model}).
156	\texttt{tail\_2048} captures 95--98\% of \texttt{exception\_only}'s accuracy across all completed configurations.
157	The residual 2--5pp gap confirms that semantic extraction (identifying exception type and message) still outperforms positional extraction (retaining a fixed window containing non-diagnostic lines).
158	
159	\paragraph{Calibration.}
160	\label{sec:calibration}
161	Calibration mirrors the tier hierarchy: \texttt{exception\_only} ECE = 0.0027 vs.\ \texttt{no\_trace} ECE = 0.171, a 63$\times$ gap (Appendix~\ref{sec:calibration_full}).
162	
163	\paragraph{Error orthogonality.}
164	\texttt{exception\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\ref{sec:error_overlap}).
165	
166	\paragraph{Exception type breakdown.}
167	A per-exception-type breakdown (Appendix~\ref{sec:exception_type}) confirms that all standard exception types achieve 100\% accuracy; the only failures arise from \texttt{GeneratorExit}, a benign \texttt{BaseException} subclass.
168	
169	\paragraph{Cross-dataset generalization.}
170	\label{sec:debugbench}
171	On DebugBench \citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \texttt{exception\_only} 100\%, VOTA 99.77\%, \texttt{no\_trace} 96.71\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\ref{sec:debugbench_full}).
172	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77514bd3-3922-4143-83ad-fdf8a58b941f",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "db4144fa-ba68-4ac0-a1a7-5ac9d51c83de",
  "sourceToolAssistantUUID": "77514bd3-3922-4143-83ad-fdf8a58b941f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T14:08:32.556Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T5Khqis7MDePvDEQXsCRLU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db4144fa-ba68-4ac0-a1a7-5ac9d51c83de",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAa42owTxKYtZNAMvBp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01736224-becc-43b1-9468-a8fa13ce2ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1xo6ap5W8VZoFtuNRofCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 18236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11653,
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

_source line 27 · 2026-05-18T14:08:32.560Z_

<details><summary>↩ Tool result · `toolu_01T5Khqis7MDePvDEQXsCRLU`</summary>

```text
1	\section{Discussion}
2	
3	Verdict prediction is fundamentally fault detection: the model must determine whether execution deviated from expected behavior.
4	Exception events succeed because they are the runtime's primary fault indicator.
5	When Python raises an unhandled exception, it records exactly what went wrong (the error type), where it happened (the stack frame), and why (the error message).
6	This is precisely the information needed for a pass/fail decision, packaged in a compact, self-contained format.
7	Non-exception trace components (variable states, loop iterations, line-by-line control flow) record \emph{how} the program ran, not \emph{whether} it failed, and dilute the model's attention without providing complementary diagnostic information.
8	
9	This mechanistic account explains three key results.
10	First, adding trace information beyond exceptions actively \emph{hurts} (VOTA $<$ \texttt{exception\_only}, Table~\ref{tab:ablation}), because non-diagnostic content competes for attention.
11	Second, a budget sweep across four models and three architecture families reveals a sharp phase transition at 256$\to$512 tail tokens (+14.7--23.0pp) that aligns with the typical exception traceback length (${\sim}$500 tokens; \S\ref{sec:trace_length}).
12	Below this threshold, all models perform at or near the \texttt{no\_trace} baseline; above it, they converge into a tight accuracy band regardless of scale or architecture.
13	\texttt{tail\_2048} captures 95--98\% of \texttt{exception\_only}'s accuracy across all completed configurations.
14	This binary pattern confirms that the diagnostic signal is spatially concentrated rather than distributed: Python's error propagation records exceptions near the trace terminus, and a single budget doubling suffices to capture or miss them entirely.
15	Third, the 6.22pp SFT advantage over the best regex baseline concentrates on caught-exception boundary cases (Appendix~\ref{sec:regex_baselines}), confirming the model learns to distinguish \emph{whether an exception terminated execution} rather than merely detecting exception presence.
16	The 0.56pp cross-model exception gap (Appendix~\ref{sec:robustness_analysis}) and the format-collapse nature of the DeepSeek outlier (Appendix~\ref{sec:training_dynamics}) further support that the signal, not the model, is the binding constraint.
17	
18	\paragraph{Why exception\_only outperforms ae\_only.}
19	Although \texttt{ae\_only} achieves 99.92\% on seed 42, it is a strict superset of the exception signal: assertion-point comparisons include the exception event (when present) plus additional information such as fallback local variable states.
20	Multi-seed evaluation reveals that this extra content introduces noise: \texttt{ae\_only} achieves 99.64\% mean accuracy ($\pm$0.49, seeds 42/123/456) while \texttt{exception\_only} achieves 99.83\% ($\pm$0.00).
21	The zero-variance result for \texttt{exception\_only} indicates that it captures a minimal sufficient signal (the compact exception event), while \texttt{ae\_only}'s additional components (fallback locals, assertion formatting) occasionally mislead the model, manifesting as seed-dependent variance ($\sigma{=}$0.49pp).
22	Attention analysis on representative samples confirms this interpretation: within exception events, the error type and location markers receive 5--10$\times$ higher per-token attention than the verbose locals context (module paths, imported objects), suggesting the model learns to focus on diagnostic signals rather than incidental runtime state.
23	Thus \texttt{exception\_only} is both more precise and more stable than its superset.
24	
25	\paragraph{SFT vs.\ regex incremental analysis.}
26	The gap between B5 (format marker, 99.33\%) and SFT \texttt{exception\_only} (99.83\%) isolates the value of learned semantic understanding (McNemar $p{=}0.041$, Table~\ref{tab:regex}).
27	Among 8 test samples where pass-labeled code triggers exceptions (from 2 distinct problems), the SFT model correctly classifies 6 (all from MBPP/113, a try/except ValueError pattern) while B5 misclassifies all 8. The 2 remaining errors (HumanEval/95, GeneratorExit) are misclassified by most training configurations (see Appendix~\ref{sec:irreducible}). At the problem level, SFT handles 1/2 exception-type edge cases vs B5's 0/2.
28	This confirms that SFT learns a genuine semantic boundary (distinguishing caught from uncaught exceptions) rather than merely detecting exception presence or format markers.
29	
30	\paragraph{Why zero-shot and few-shot prompting fall short.}
31	Zero-shot prompting spans 51.0--93.5\% across four models, with cross-architecture variance (42.44pp) dwarfing the SFT range (0.56pp).
32	The failure is not in exception detection but in verdict calibration: the model recognizes that an exception occurred but cannot reliably determine whether it terminated execution or was caught by a \texttt{try/except} block.
33	Performance does not correlate with model size: Qwen-1.5B (93.45\%) outperforms Qwen-7B (89.08\%) and CodeLlama-13B (51.01\%, extreme fail bias with 72.4\% of predictions as \texttt{fail}).
34	Within the Qwen family, the 1.5B model's higher zero-shot accuracy likely reflects consistent code training data quality across scales: the smaller model already understands exception format, but both lack the verdict-specific calibration that SFT provides (SFT gap: 6.38pp for 1.5B vs.\ 10.75pp for 7B).
35	Three-shot in-context learning (90.84\% on Qwen-7B, fail recall = 80.53\%) improves fail recall by 13.57pp over zero-shot but still trails SFT by 8.99pp: three examples cannot cover the diversity of caught-exception patterns in the training distribution.
36	SFT normalizes this cross-architecture variance by grounding exception patterns in task-specific verdict labels, compressing a 42.44pp zero-shot range to 0.56pp.
37	
38	\paragraph{Format marker sensitivity.}
39	The B5 baseline (Appendix~\ref{sec:regex_baselines}) achieves 99.33\% by exploiting a deterministic format marker (\texttt{[No exception data in trace]}) present in all pass samples.
40	This near-ceiling performance from a trivial pattern raises a concern: does SFT also learn this shortcut?
41	The answer is partially yes: the format marker correlates perfectly with the pass class. But the SFT model additionally handles the 8 boundary samples where exceptions occur in passing code, achieving 6/8 correct vs.\ B5's 0/8.
42	A \emph{nomarker} ablation (\S\ref{sec:nomarker}) confirms genuine exception semantics: Qwen-7B 3-seed mean 97.65\%$\pm$0.96 and Qwen-1.5B 97.82\%, a drop of only ${\sim}$2pp.
43	The marker contribution (${\sim}$9\% of total lift) is small relative to semantic content (${\sim}$91\%), confirming that SFT learns exception semantics rather than format shortcuts.
44	Both signal layers show comparable accuracy across the two tested scales (1.5B and 7B produce 97.8\% and 97.7\% nomarker accuracy, respectively).
45	
46	\paragraph{Near-perfect floor, not hard ceiling.}
47	Samples 901 and 905 (HumanEval/95, \texttt{check\_dict\_case}) are misclassified by most configurations: Qwen-7B (3 seeds), Qwen-1.5B, and CodeLlama-13B seed 42/456 all produce exactly these 2 errors.
48	The root cause is deterministic: Python's \texttt{all()} raises \texttt{GeneratorExit} (a \texttt{BaseException} subclass) during generator short-circuit, recorded as \texttt{[ERROR]} despite the test passing.
49	However, CodeLlama-13B seed 123 achieves 100\% (0/1190 errors), correctly classifying both samples.
50	This confirms that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most initializations) rather than a hard data limitation: the representation supports perfect accuracy, though most LoRA initializations converge to the same 2-error basin.
51	On this task, exception-only accuracy is \emph{signal-limited} rather than \emph{capacity-limited}: three architecture families spanning 1.5B to 13B converge on the same floor, while \texttt{no\_trace} shows monotonic scale dependence (67.3\% $\to$ 75.1\% $\to$ 76.5\%).
52	
53	\paragraph{Tokenizer efficiency and training dynamics.}
54	CodeLlama's tokenizer produces ${\sim}$20\% more tokens than Qwen's on identical trace inputs (mean 1{,}174 vs.\ 978 tokens), reducing the verdict label's share of the training loss to ${\sim}$0.085\%.
55	Under standard next-token loss, the model allocates the vast majority of gradient updates to predicting trace tokens rather than learning the verdict classification boundary.
56	This tokenizer-driven dilution is invisible at short trace budgets (tail-256/512), where CodeLlama performs comparably to other models (77.9\% and 97.5\%, respectively), but is expected to compound at longer budgets (1{,}024+ tokens) where trace tokens dominate the loss landscape.
57	A label-only loss variant (computing loss only on the verdict token, masking all trace positions) addresses this by decoupling verdict learning from trace prediction; results for CodeLlama tail-1024/2048 under this regime are pending.
58	This finding highlights tokenizer efficiency as a previously overlooked variable in trace-based training: architectures with less efficient tokenizers require adapted training strategies (e.g., label-only loss) to prevent the diagnostic signal from being drowned by trace token prediction.
59	
60	\paragraph{Tier hierarchy: practical implications.}
61	The two-tier structure (Tier~1 ${\geq}$99\%; Tier~2 = 85.6\%) has direct engineering implications for trace-augmented systems.
62	First, it implies a \emph{diminishing returns} principle: once a Tier~1 signal is available, adding more trace information provides no benefit and may actively degrade performance through attention dilution.
63	Second, the hierarchy suggests a fallback design: systems should attempt Tier~1 extraction (exception events) and only resort to Tier~2 signals (loop compression) when no exception is raised. Even Tier~2 alone substantially outperforms no-trace baselines (+10.50pp).
64	Third, the minimal token footprint of Tier~1 signals (median 150 tokens vs.\ ${\sim}$1{,}900 for VOTA post-truncation) makes them viable for deployment in token-constrained settings (e.g., real-time CI pipelines, mobile inference).
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01736224-becc-43b1-9468-a8fa13ce2ffb",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "b7c3c035-34b1-401a-b445-0a1ba79a2269",
  "sourceToolAssistantUUID": "01736224-becc-43b1-9468-a8fa13ce2ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T14:08:33.057Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SF24ZETC13npEz7yywVVzt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7c3c035-34b1-401a-b445-0a1ba79a2269",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAa42owTxKYtZNAMvBp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "408094cf-a69c-4e7d-aaa7-74267f9d5376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1xo6ap5W8VZoFtuNRofCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 18236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11653,
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

_source line 29 · 2026-05-18T14:08:33.069Z_

<details><summary>↩ Tool result · `toolu_01SF24ZETC13npEz7yywVVzt`</summary>

```text
1	\section{Conclusion}
2	
3	We presented the first systematic component ablation of trace representations for verdict prediction across four models (1.5B--13B, three architecture families).
4	Exception events alone achieve ${\geq}$99.33\% across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while \texttt{no\_trace} shows 9.19pp scale sensitivity (67.3--76.5\%).
5	Adding more trace information actively hurts: the gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%), and tail-truncation confirms that diagnostic signal concentrates at the trace terminus.
6	A format-marker ablation shows ${\sim}$91\% of the exception signal is semantic rather than format-driven, and cross-dataset evaluation on DebugBench confirms generalization (\texttt{exception\_only}: 100\%, $N{=}426$).
7	
8	The broader implication is that verdict prediction is not an information-starved task that benefits from richer context.
9	It is a fault detection task where the runtime has already surfaced the critical diagnostic signal; the model's role is to interpret whether that signal indicates a terminal fault (as the SFT advantage over regex on caught-exception cases confirms).
10	This reframing suggests a design principle for trace-augmented systems: extract the highest-specificity diagnostic signal (median 150 tokens) and discard everything else.
11	Future work should test whether this principle extends to additional programming languages, larger real-world codebases, silent logic errors where no exception is raised, and tasks beyond verdict prediction.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "408094cf-a69c-4e7d-aaa7-74267f9d5376",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "3db81764-7bf7-46c4-8f4a-1e6443b62d6a",
  "sourceToolAssistantUUID": "408094cf-a69c-4e7d-aaa7-74267f9d5376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T14:08:33.224Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BTQhirwF6y7tUiSduvJCLF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3db81764-7bf7-46c4-8f4a-1e6443b62d6a",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAa42owTxKYtZNAMvBp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc0e1a55-5987-4aac-b6ee-c86bcc9a1a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1xo6ap5W8VZoFtuNRofCH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 18236,
      "output_tokens": 590,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11653
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 590,
          "cache_read_input_tokens": 18236,
          "cache_creation_input_tokens": 11653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11653,
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

_source line 31 · 2026-05-18T14:08:33.521Z_

<details><summary>↩ Tool result · `toolu_01BTQhirwF6y7tUiSduvJCLF`</summary>

```text
1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\% fail precision but only 45.4\% fail recall, indicating systematic bias toward predicting \texttt{pass}. DeepSeek \texttt{exception\_only} seed 42 achieves 100\% fail recall, but seed 123 drops to 70.5\% (see Table~\ref{tab:full_deepseek}).}
9	\label{tab:per_class}
10	\small
11	\begin{tabular}{llccccccc}
12	\toprule
13	\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
14	\midrule
15	No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
16	Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
17	Full Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
22	VOTA\_no\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	\bottomrule
29	\end{tabular}
30	\end{table*}
31	
32	%% ============================================================
33	\section{Training Details}
34	\label{sec:training_details}
35	
36	Table~\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.
37	All experiments use the HuggingFace TRL \texttt{SFTTrainer} with LoRA \citep{hu2022lora} applied to all linear layers.
38	
39	\begin{table}[t]
40	\centering
41	\caption{Training hyperparameters (shared across all conditions).}
42	\label{tab:hyperparams}
43	\small
44	\resizebox{\columnwidth}{!}{%
45	\begin{tabular}{ll}
46	\toprule
47	\textbf{Hyperparameter} & \textbf{Value} \\
48	\midrule
49	LoRA rank ($r$)            & 16 \\
50	LoRA alpha ($\alpha$)      & 32 \\
51	LoRA dropout               & 0.05 \\
52	LoRA target modules        & all linear layers \\
53	\midrule
54	Epochs                     & 3 \\
55	Per-device batch size       & 4 \\
56	Gradient accumulation steps & 8 \\
57	Effective batch size        & 32 \\
58	\midrule
59	Learning rate               & $2 \times 10^{-4}$ \\
60	LR scheduler                & linear decay \\
61	Warmup ratio                & 0.1 \\
62	Weight decay                & 0.01 \\
63	\midrule
64	Max sequence length         & 2048 tokens \\
65	Primary seed                & 42 \\
66	Robustness seeds            & 123, 456 \\
67	\midrule
68	Hardware                    & 1$\times$ RTX PRO 6000 Blackwell (96\,GB VRAM) \\
69	Framework                   & HuggingFace TRL SFTTrainer \\
70	\bottomrule
71	\end{tabular}%
72	}
73	\end{table}
74	
75	Table~\ref{tab:train_time} reports per-condition training wall-clock times.
76	Conditions with longer trace inputs (e.g., \texttt{full\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.
77	
78	\begin{table}[t]
79	\centering
80	\caption{Training wall-clock time per condition on a single RTX PRO 6000 Blackwell GPU. Where multiple seeds were run, individual times are listed.}
81	\label{tab:train_time}
82	\small
83	\begin{tabular}{llr}
84	\toprule
85	\textbf{Condition} & \textbf{Seed(s)} & \textbf{Time (h)} \\
86	\midrule
87	no\_trace       & 42         & ${\sim}$0.5 \\
88	full\_trace     & 42         & ${\sim}$2.2 \\
89	label\_only     & 42         & ${\sim}$2.2 \\
90	VOTA                     & 42         & ${\sim}$2.3 \\
91	exception\_only & 42         & ${\sim}$2.1 \\
92	exception\_only & 123        & ${\sim}$2.1 \\
93	exception\_only & 456        & ${\sim}$1.3 \\
94	ae\_only        & 42         & ${\sim}$1.8 \\
95	loop\_only      & 42         & ${\sim}$2.1 \\
96	VOTA\_no\_ae    & 42         & ${\sim}$1.8 \\
97	\bottomrule
98	\end{tabular}
99	\end{table}
100	
101	%% ============================================================
102	\section{VOTA Trace Examples}
103	\label{sec:vota_examples}
104	
105	We provide two representative VOTA trace examples illustrating the fail and pass cases.
106	In the fail case, the exception event provides an unambiguous fault signal.
107	In the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.
108	
109	\paragraph{Fail example.}
110	A \texttt{ZeroDivisionError} triggers an \texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \texttt{fail}.
111	
112	\begin{small}
113	\begin{verbatim}
114	## Function
115	def divide(a, b):
116	    return a / b
117	
118	## Test Input
119	divide(1, 0)
120	
121	## Expected Output
122	inf
123	
124	## VOTA Trace
125	[ERROR] ZeroDivisionError: division by zero
126	
127	## Verdict
128	fail
129	\end{verbatim}
130	\end{small}
131	
132	\paragraph{Pass example.}
133	No exception is raised, and the assertion point confirms that the actual output matches the expected value.
134	
135	\begin{small}
136	\begin{verbatim}
137	## Function
138	def add(a, b):
139	    return a + b
140	
141	## Test Input
142	add(2, 3)
143	
144	## Expected Output
145	5
146	
147	## VOTA Trace
148	[LOOP] No loops detected.
149	[ASSERT] actual=5, expected=5
150	
151	## Verdict
152	pass
153	\end{verbatim}
154	\end{small}
155	
156	These examples illustrate the core asymmetry exploited by the \texttt{exception\_only} condition: fail cases produce an explicit \texttt{[ERROR]} event, while pass cases are characterized by its absence.
157	This binary signal (presence vs.\ absence of an exception) is sufficient for near-perfect verdict prediction.
158	
159	%% ============================================================
160	\section{Full Experimental Results}
161	\label{sec:full_results}
162	
163	Tables~\ref{tab:full_qwen} and \ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.
164	
165	\begin{table}[t]
166	\centering
167	\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \texttt{exception\_only} achieves 99.83\% across all three seeds ($\sigma{=}$0). \texttt{ae\_only} achieves 99.64\% mean ($\pm$0.49; seed 123 at 99.08\% is the outlier).}
168	\label{tab:full_qwen}
169	\small
170	\resizebox{\columnwidth}{!}{%
171	\begin{tabular}{lcccc}
172	\toprule
173	\textbf{Condition} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean $\pm$ Std} \\
174	\midrule
175	exception\_only & 99.83 & 99.83 & 99.83 & 99.83 $\pm$ 0.00 \\
176	ae\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\pm$ 0.49 \\
177	VOTA                     & 99.41 & ---   & ---   & --- \\
178	VOTA\_no\_ae    & 99.41 & ---   & ---   & --- \\
179	label\_only     & 86.22 & ---   & ---   & --- \\
180	loop\_only      & 85.63 & ---   & ---   & --- \\
181	full\_trace     & 81.76 & ---   & ---   & --- \\
182	no\_trace       & 75.13 & ---   & ---   & --- \\
183	\bottomrule
184	\end{tabular}%
185	}
186	\end{table}
187	
188	\begin{table}[t]
189	\centering
190	\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \texttt{exception\_only} shows bimodal seed behavior: seeds 42 and 456 achieve 99.33\%, while seed 123 yields 91.09\% (LoRA initialization outlier, fail recall = 70.5\%).}
191	\label{tab:full_deepseek}
192	\small
193	\resizebox{\columnwidth}{!}{%
194	\begin{tabular}{llcc}
195	\toprule
196	\textbf{Condition} & \textbf{Seed} & \textbf{Accuracy} & \textbf{Notes} \\
197	\midrule
198	exception\_only & 42  & 99.33 & epoch 1: 99.83 \\
199	exception\_only & 456 & 99.33 & CI [98.82, 99.75] \\
200	exception\_only & 123 & 91.09 & fail recall = 70.5\%; CI [89.40, 92.60] \\
201	\midrule
202	VOTA                     & 42  & 84.45 & \\
203	no\_trace       & 42  & 73.36 & \\
204	full\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\
205	\bottomrule
206	\end{tabular}%
207	}
208	\end{table}
209	
210	%% ============================================================
211	\section{Tokenizer and Truncation Analysis}
212	\label{sec:tokenizer_analysis}
213	
214	The VOTA cross-model gap (14.96pp, Table~\ref{tab:cross_model}; confounded by tokenizer-driven truncation; 91.7\% of DeepSeek training samples were affected) is driven by a training-time truncation asymmetry.
215	The DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.
216	The training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.
217	
218	A post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\%).
219	Per-class analysis (Table~\ref{tab:per_class}) confirms that DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}---in contrast to Qwen VOTA, which achieves 100\% fail recall.
220	
221	Seed robustness diverges across models: Qwen \texttt{exception\_only} produces identical 99.83\% across all three seeds ($\sigma{=}0$), while DeepSeek shows bimodal behavior: seeds 42 and 456 achieve 99.33\% (fail recall = 100\%), seed 123 yields 91.09\% (fail recall = 70.5\%).
222	Because \texttt{exception\_only} test inputs contain 48.99\% duplicates (607 unique of 1,190; \S\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\% (Wilson CI [98.81, 99.91]).
223	
224	%% ============================================================
225	\section{Irreducible Sample Analysis}
226	\label{sec:irreducible}
227	
228	The \texttt{exception\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\% overlap across seeds.
229	Both samples (IDs 901 and 905) share the following characteristics:
230	
231	\begin{itemize}
232	\item \textbf{Function:} \texttt{check\_dict\_case} (HumanEval/95)---a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.
233	\item \textbf{Ground-truth label:} \texttt{pass}.
234	\item \textbf{Predicted label:} \texttt{fail} (false negative).
235	\item \textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.
236	\end{itemize}
237	
238	Manual inspection reveals the root cause: \texttt{check\_dict\_case} uses \texttt{all()} over a generator expression, and Python's \texttt{all()} short-circuits on the first \texttt{True} value, raising \texttt{GeneratorExit} to terminate the generator.
239	Because \texttt{GeneratorExit} is a \texttt{BaseException} subclass, the tracer records it as seven \texttt{[ERROR] GeneratorExit} lines---even though the function executes correctly and the test passes.
240	The model observes these spurious error markers and reasonably but incorrectly predicts \texttt{fail}.
241	This is not a model failure but a representation ambiguity: the \texttt{exception\_only} format cannot distinguish genuine exceptions from benign \texttt{BaseException} subclasses triggered by Python's iterator protocol.
242	
243	Most configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\{901, 905\}$.
244	However, CodeLlama-13B seed 123 achieves 100\% accuracy (0/1190 errors), correctly classifying both samples.
245	This demonstrates that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.
246	The practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.
247	
248	%% ============================================================
249	\section{Exception Type Accuracy Breakdown}
250	\label{sec:exception_type}
251	
252	Table~\ref{tab:exception_type} reports \texttt{exception\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).
253	All standard exception types (\texttt{TypeError}, \texttt{ValueError}, \texttt{IndexError}, etc.) achieve 100\% accuracy.
254	The only misclassifications arise from \texttt{GeneratorExit}, a \texttt{BaseException} subclass that is not an \texttt{Exception}---it is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.
255	
256	\begin{table}[t]
257	\centering
258	\caption{Exception type accuracy breakdown for \texttt{exception\_only} (Qwen-7B, seed=42). All true error types achieve 100\%. The only failures come from \texttt{GeneratorExit} (a \texttt{BaseException} subclass, not an \texttt{Exception}), which appears in 2 passing samples.}
259	\label{tab:exception_type}
260	\small
261	\begin{tabular}{lcc}
262	\toprule
263	\textbf{Exception Type} & \textbf{Samples} & \textbf{Accuracy} \\
264	\midrule
265	TypeError & 96 & 100\% \\
266	ValueError & 62 & 100\% \\
267	IndexError & 41 & 100\% \\
268	KeyError & 28 & 100\% \\
269	AttributeError & 19 & 100\% \\
270	AssertionError & 15 & 100\% \\
271	RecursionError & 12 & 100\% \\
272	Other Exception & 66 & 100\% \\
273	\midrule
274	GeneratorExit (BaseException) & 2 & 0\% \\
275	No exception (pass class) & 849 & 100\% \\
276	\bottomrule
277	\end{tabular}
278	\end{table}
279	
280	This confirms that the model has learned a clean decision boundary: any true \texttt{Exception} subclass in the trace implies failure.
281	The \texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \S\ref{sec:irreducible}.
282	
283	%% ============================================================
284	\section{Trace Length Ablation}
285	\label{sec:trace_length_full}
286	
287	To test whether the \texttt{full\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.
288	
289	\begin{table}[t]
290	\centering
291	\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\% CIs ($B{=}10{,}000$).}
292	\label{tab:trace_length}
293	\small
294	\begin{tabular}{llcc}
295	\toprule
296	\textbf{Direction} & \textbf{Max Tokens} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
297	\midrule
298	Head & 256  & 78.82 & [76.4, 81.0] \\
299	Head & 512  & 80.42 & [78.2, 82.6] \\
300	Head & 1024 & 77.23 & [74.9, 79.6] \\
301	Head & no\_limit ($\infty$) & 81.76 & [79.7, 83.9] \\
302	\midrule
303	Tail & 256  & 77.48 & --- \\
304	Tail & 512  & 93.61 & --- \\
305	Tail & 1024 & 96.47 & --- \\
306	Tail & 2048 & 97.31 & --- \\
307	\bottomrule
308	\end{tabular}
309	\end{table}
310	
311	\begin{figure}[t]
312	\centering
313	\includegraphics[width=\columnwidth]{budget_curve}
314	\caption{Accuracy as a function of token budget and truncation direction (Qwen-2.5-7B, $N{=}1{,}190$). Tail-truncation (keeping last $k$ tokens) monotonically improves beyond 256 tokens and consistently outperforms head-truncation by 13--19pp at budgets ${\geq}$512. The flat head-truncation curve (77--82\%) contrasts with the steep tail-truncation rise, confirming that diagnostic signal is localized near trace end. Dashed lines show \texttt{exception\_only} (99.83\%) and \texttt{no\_trace} (75.13\%) as upper and lower bounds. Tail-256 (${\approx}$ \texttt{no\_trace}) indicates the signal window begins approximately 256 tokens from the trace terminus.}
315	\label{fig:trace_length}
316	\end{figure}
317	
318	As shown in Table~\ref{tab:trace_length} and Figure~\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\%--81.8\%).
319	To quantify the reliability of the observed differences, Table~\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.
320	
321	\begin{table}[t]
322	\centering
323	\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}
324	\label{tab:trace_length_pairwise}
325	\small
326	\resizebox{\columnwidth}{!}{%
327	\begin{tabular}{llccc}
328	\toprule
329	& \textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
330	\midrule
331	\multirow{4}{*}{\rotatebox{90}{\scriptsize Budget}}
332	& 512 vs.\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\
333	& 1024 vs.\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\
334	& no\_limit vs.\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\
335	& no\_limit vs.\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\
336	\midrule
337	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ no\_trace}}
338	& 256 $-$ no\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\
339	& 512 $-$ no\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\
340	& 1024 $-$ no\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\
341	& no\_limit $-$ no\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\
342	\midrule
343	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ exc.}}
344	& 256 $-$ exc\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\
345	& 512 $-$ exc\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\
346	& 1024 $-$ exc\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\
347	& no\_limit $-$ exc\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\
348	\bottomrule
349	\end{tabular}%
350	}
351	\end{table}
352	
353	\paragraph{Non-monotonic pattern (head-truncation).}
354	Under head-truncation (retaining trace prefixes), the trend is non-monotonic: 512 tokens (80.42\%) slightly outperforms 256 tokens (78.82\%), but doubling to 1024 tokens \emph{decreases} accuracy to 77.23\%, a statistically significant 3.19pp drop ($p{=}0.002$, 95\% CI [$-$5.29, $-$1.09]).
355	The no-limit condition (81.76\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than \texttt{no\_trace} (75.13\%; $\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\% CI [$-$0.17, $+$4.37]).
356	This non-monotonicity is specific to head-truncation: the 1024-token prefix retains enough irrelevant content to mislead the model while discarding diagnostic events that appear near the trace terminus.
357	Under tail-truncation, accuracy increases monotonically for Qwen-7B and Qwen-1.5B (Table~\ref{tab:tail_cross_model}); only DeepSeek-6.7B shows a mild $-$1.5pp decrease at tail-1024$\to$tail-2048, attributable to architecture-specific long-context sensitivity rather than a systematic mid-length pathology.
358	
359	\paragraph{Comparison to baselines.}
360	All four trace budget conditions significantly exceed \texttt{no\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.
361	The gap to \texttt{exception\_only} (99.83\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.
362	The best full-trace condition (no\_limit, 81.76\%) still lags \texttt{exception\_only} by 18.07pp (95\% CI [$-$20.34, $-$15.88]).
363	
364	\paragraph{Interpretation.}
365	These results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.
366	The non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.
367	The result reinforces the information density interpretation (\S\ref{sec:density}): the gap between full traces and VOTA is driven by the \emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \emph{length}.
368	In contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\S\ref{sec:cross_model}).
369	
370	\paragraph{Truncation direction.}
371	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \texttt{tail\_2048} achieves 97.31\% vs.\ \texttt{head\_2048} (no\_limit) at 81.76\%, a 15.55pp improvement.
372	Even \texttt{tail\_512} (93.61\%) exceeds every head-truncation condition by over 11pp.
373	
374	However, \texttt{tail\_256} (77.48\%) performs at the \texttt{no\_trace} baseline level (75.13\%), indicating that the diagnostic signal does not reside in the very last trace lines.
375	The critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.
376	This is consistent with Python's execution model: exception tracebacks and assertion comparisons appear near the end of the trace but are preceded by the final function call frames, placing them typically 300--500 tokens from the terminus rather than at the absolute end.
377	
378	The 18.07pp gap from \texttt{full\_trace} to \texttt{exception\_only} decomposes as: 86\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\% residual content noise (the 2.52pp gap from \texttt{tail\_2048} to \texttt{exception\_only} that persists regardless of truncation direction).
379	The fact that \texttt{exception\_only} (99.83\%) still outperforms \texttt{tail\_2048} (97.31\%) confirms that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.
380	
381	\paragraph{Cross-model budget curve.}
382	Table~\ref{tab:tail_cross_model} extends the tail-truncation analysis to a full budget sweep across four models spanning three architecture families and an 8.7$\times$ parameter range.
383	
384	\begin{table}[t]
385	\centering
386	\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$). A sharp phase transition occurs at 256$\to$512 tokens across all four models (+14.7--23.0pp), after which accuracy converges regardless of scale or architecture. $\downarrow$: non-monotonic decrease (DeepSeek only). $^\dag$CodeLlama tail-1024/2048 pending retraining with label-only loss (\S\ref{sec:tokenizer_analysis}).}
387	\label{tab:tail_cross_model}
388	\small
389	\resizebox{\columnwidth}{!}{%
390	\begin{tabular}{lccccc}
391	\toprule
392	\textbf{Model} & \textbf{tail-256} & \textbf{tail-512} & \textbf{tail-1024} & \textbf{tail-2048} & \textbf{exc\_only} \\
393	\midrule
394	Qwen-7B (7B) & 78.9 & 93.6 & 96.5 & 97.3 & 99.83 \\
395	DeepSeek (6.7B) & 76.4 & 93.9 & 96.5 & 95.0$\downarrow$ & 99.33 \\
396	CodeLlama (13B) & 77.9 & 97.5 & ---$^\dag$ & ---$^\dag$ & 99.89 \\
397	Qwen-1.5B (1.5B) & 72.6 & 95.6 & 96.6 & 97.9 & 99.83 \\
398	\bottomrule
399	\end{tabular}%
400	}
401	\end{table}
402	
403	\begin{table}[t]
404	\centering
405	\caption{Cross-model truncation direction comparison ($N{=}1{,}190$). Head-truncation retains the first 2,048 tokens; tail-truncation retains the last 2,048. All four models' head-2048 accuracies converge into a narrow 75.3--81.8\% band (6.5pp), comparable to the tail-256 signal-poor band (72.6--78.9\%, 6.3pp). $^\dag$CodeLlama tail-2048 pending retraining (\S\ref{sec:tokenizer_analysis}).}
406	\label{tab:head_vs_tail}
407	\small
408	\begin{tabular}{lccc}
409	\toprule
410	\textbf{Model} & \textbf{head-2048 (\%)} & \textbf{tail-2048 (\%)} & \textbf{Gap (pp)} \\
411	\midrule
412	Qwen-1.5B & 75.3 & 97.9 & +22.6 \\
413	DeepSeek-6.7B & 78.7 & 95.0 & +16.3 \\
414	CodeLlama-13B & 79.9 & ---$^\dag$ & ---$^\dag$ \\
415	Qwen-7B & 81.8 & 97.3 & +15.5 \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	Four patterns emerge from the budget curve.
421	\emph{Phase transition at 256$\to$512 tokens}: all four models jump +14.7--23.0pp (Qwen-7B +14.7, DeepSeek +17.5, CodeLlama +19.6, Qwen-1.5B +23.0), crossing from near-baseline to near-ceiling in a single budget doubling.
422	The threshold aligns with the typical exception traceback length (${\sim}$500 tokens): below this budget, the diagnostic event is truncated; above it, the event is captured regardless of model capacity or architecture family.
423	
424	\emph{Convergence at tail-512+}: once the phase transition is crossed, accuracy converges across all models into a 93.6--97.5\% band at tail-512; where tail-1024 data is available, the band tightens further to 96.5--96.6\%.
425	Scale and architecture differences that dominate the signal-poor regime (tail-256 range: 72.6--78.9\%, 6.3pp) compress dramatically in the signal-rich regime.
426	
427	\emph{Signal-poor convergence band}: head-2048 accuracies across all four models also converge into a narrow 75.3--81.8\% band (6.5pp; Table~\ref{tab:head_vs_tail}), comparable in width to the tail-256 band (72.6--78.9\%, 6.3pp).
428	When the diagnostic signal is absent (head-truncation discards trace terminus) or unreachable (tail-256 is too short), models of different scale and architecture collapse to similar performance, suggesting a shared floor determined by code comprehension rather than trace processing.
429	
430	\emph{Scale behavior inversion}: in the signal-poor regime (tail-256), smaller models perform worse (Qwen-1.5B 72.6\% vs.\ Qwen-7B 78.9\%, $-$6.3pp), mirroring the \texttt{no\_trace} scale pattern.
431	In the signal-rich regime (tail-512+), this reverses: Qwen-1.5B matches or exceeds Qwen-7B (95.6\% vs.\ 93.6\% at tail-512; 97.9\% vs.\ 97.3\% at tail-2048), confirming that sufficient trace signal eliminates the capacity advantage.
432	
433	\emph{Non-monotonicity}: DeepSeek-6.7B shows a $-$1.5pp decrease from tail-1024 (96.5\%) to tail-2048 (95.0\%), while Qwen-7B and Qwen-1.5B increase monotonically.
434	This architecture-specific sensitivity is consistent with DeepSeek's known vulnerability to long-context formatting (\S\ref{sec:training_dynamics}): additional tokens beyond the diagnostic window introduce noise that this model cannot filter as effectively.
435	
436	Table~\ref{tab:head_vs_tail} confirms the truncation direction effect: among the three models with complete data, tail-2048 outperforms head-2048 by 15.5--22.6pp.
437	The gap is largest for Qwen-1.5B (+22.6pp), indicating that smaller models benefit most from positional proximity to the diagnostic signal, as they lack the capacity to locate it within longer, noisier prefixes.
438	
439	%% ============================================================
440	\section{Calibration Analysis}
441	\label{sec:calibration_full}
442	
443	Beyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \citep{spiess2025calibration}.
444	
445	\begin{table}[t]
446	\centering
447	\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}
448	\label{tab:calibration}
449	\small
450	\begin{tabular}{lcc}
451	\toprule
452	\textbf{Condition} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} \\
453	\midrule
454	ae\_only & \textbf{0.0004} & \textbf{0.0008} \\
455	exception\_only & 0.0027 & 0.0013 \\
456	VOTA & 0.0054 & 0.005 \\
457	full\_trace & 0.096 & 0.144 \\
458	no\_trace & 0.171 & 0.197 \\
459	\bottomrule
460	\end{tabular}
461	\end{table}
462	
463	Table~\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.
464	Tier~1 conditions (\texttt{ae\_only}: ECE=0.0004; \texttt{exception\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \texttt{full\_trace} (ECE=0.096) and \texttt{no\_trace} (ECE=0.171) exhibit substantial miscalibration.
465	VOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.
466	
467	The Brier scores tell a consistent story: \texttt{ae\_only} (0.0008) and \texttt{exception\_only} (0.0013) achieve near-zero scores, while \texttt{no\_trace} (0.197) indicates substantial miscalibration.
468	
469	\begin{figure}[t]
470	\centering
471	\includegraphics[width=\columnwidth]{fig2_calibration}
472	\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \texttt{exception\_only} (ECE=0.0027) clusters near the diagonal, while \texttt{no\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\times$ gap.}
473	\label{fig:calibration}
474	\end{figure}
475	
476	%% ============================================================
477	\section{Error Overlap Analysis}
478	\label{sec:error_overlap}
479	
480	We analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\ref{fig:error_overlap}).
481	
482	\texttt{exception\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).
483	This orthogonality arises because \texttt{exception\_only} errors are caused by \texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.
484	
485	Among non-exception conditions, error sets exhibit hierarchical containment: \texttt{ae\_only} $\subset$ VOTA $\subset$ \texttt{loop\_only} $\subset$ \texttt{no\_trace}, with pairwise Jaccard indices increasing with signal overlap.
486	\texttt{loop\_only} and \texttt{full\_trace} share the highest overlap (Jaccard ${\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.
487	
488	This analysis confirms that \texttt{exception\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.
489	
490	\begin{figure}[t]
491	\centering
492	\includegraphics[width=\columnwidth]{error_overlap}
493	\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \texttt{exception\_only} (exc\_only) has zero overlap with all other conditions, confirming it operates on an independent signal dimension.}
494	\label{fig:error_overlap}
495	\end{figure}
496	
497	%% ============================================================
498	\section{Cross-Dataset Generalization: DebugBench}
499	\label{sec:debugbench_full}
500	
501	To test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \citep{tian2024debugbench}---a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).
502	After filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\%).
503	
504	\begin{table}[t]
505	\centering
506	\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\% CIs. The component ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is preserved, and exception\_only achieves perfect accuracy.}
507	\label{tab:debugbench}
508	\small
509	\begin{tabular}{lcc}
510	\toprule
511	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
512	\midrule
513	exception\_only & \textbf{100.00} & [99.14, 100.00] \\
514	VOTA & 99.77 & [99.30, 100.00] \\
515	no\_trace & 96.71 & [94.80, 98.40] \\
516	\midrule
517	Majority baseline & 51.41 & --- \\
518	\bottomrule
519	\end{tabular}
520	\end{table}
521	
522	Table~\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \texttt{exception\_only} (100.00\%) $\geq$ VOTA (99.77\%) $>$ \texttt{no\_trace} (96.71\%).
523	The \texttt{exception\_only} condition achieves perfect accuracy, confirming that the exception-based representation generalizes to a different fault distribution without degradation.
524	
525	The absolute margins are much narrower than on the main dataset: the \texttt{no\_trace} baseline already achieves 96.71\%---compared to 75.13\% on HumanEval+MBPP---leaving only 3.29pp of headroom for trace-based improvement.
526	This ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.
527	In contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.
528	
529	These results support exception-based verdict prediction as a generalizable approach---the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is consistent across both datasets---but the narrow DebugBench margins are insufficient to independently validate trace importance.
530	The 24.70pp trace lift on the main dataset (no\_trace 75.13\% $\to$ exception\_only 99.83\%) remains the primary evidence for the value of exception-based trace signals.
531	
532	%% ============================================================
533	\section{Cross-Model Robustness Analysis}
534	\label{sec:robustness_analysis}
535	
536	The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
537	Exception events are consistently the most effective component on both models, and their structural simplicity---a fixed-format error message---ensures that the relative advantage over richer representations holds across all seeds.
538	Two of three DeepSeek seeds match Qwen-level accuracy (99.33\%); the outlier (seed 123, 91.09\%) we hypothesize reflects LoRA initialization sensitivity landing in a suboptimal basin (fail recall = 70.5\%, though direct evidence is lacking), not a failure of the exception signal itself---even this outlier outperforms VOTA (84.45\%) by 6.64pp.
539	The VOTA cross-model gap is confounded by two factors: (1)~tokenizer efficiency---the DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus Qwen's 1{,}929, causing 91.7\% of training samples to exceed the 2{,}048-token context window; content-aware truncation preferentially removes the terminal structured prompt, preserving the verdict label but truncating trace content---and (2)~base model capability differences, consistent with findings that SFT generalization depends on pretrain quality \citep{yang2024generalization}.
540	The two factors cannot be disentangled in the current experimental design.
541	Our \texttt{exception\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.
542	The resulting 0.56pp cross-model gap (Table~\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.
543	The practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.
544	
545	%% ============================================================
546	\section{Training Dynamics and Loss Decoupling}
547	\label{sec:training_dynamics}
548	
549	The DeepSeek \texttt{exception\_only} results reveal two instructive training dynamics.
550	First, epoch-level analysis shows mild degradation in 2/3 seeds: seed 42 peaks at 99.83\% after epoch~1 but settles at 99.33\% by epoch~3 ($-$0.50pp), seed 123 degrades from 91.43\% to 91.09\% ($-$0.34pp), while seed 456 shows no epoch degradation (99.33\% at both epoch~1 and epoch~3).
551	Early stopping may yield marginal gains for some seeds, but the epoch effect is small (${\leq}$0.5pp) compared to the seed effect (8.24pp between seeds 42 and 123).
552	
553	Second, seeds 123 and 456 converge to nearly identical final training losses (0.122 and 0.123 respectively), yet their accuracies differ by 8.24pp (91.09\% vs.\ 99.33\%).
554	The critical difference lies in fail recall: seeds 42 and 456 achieve 100\%, while seed 123 achieves only 70.5\%---the LoRA initialization in seed 123 fails to learn the exception$\to$fail mapping for a substantial fraction of failing samples, even though the per-token loss appears converged.
555	This demonstrates that token-level training loss can mask fundamental differences in sample-level classification ability, suggesting a parallel to the eval-loss/accuracy decoupling observed in DeepSeek VOTA (where eval loss rose 65\% from epoch 1 to 3 while accuracy improved by 6.3pp) at the training phase.
556	The practical recommendation is twofold: (1)~use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training or evaluation loss, and (2)~for deployment on smaller models, train multiple seeds and select the best, as a single run may not reliably converge to the correct classification boundary.
557	
558	\paragraph{Format collapse, not semantic failure.}
559	The 100 errors of seed 123 are not semantic failures but generation format collapse: on inputs exceeding 4,000 characters (those containing verbose locals dumps), the model echoes trace content instead of emitting a verdict token, while achieving zero errors on shorter inputs.
560	This indicates that the LoRA initialization of seed 123 specifically compromises long-context format compliance rather than exception signal comprehension, further supporting the robustness advantage of compact \texttt{exception\_only} inputs.
561	
562	The contrast with VOTA is instructive: DeepSeek VOTA accuracy monotonically increases from 78.15\% to 84.45\% across epochs, but is consistent with a performance limit associated with the high trace truncation rate (\S\ref{sec:cross_model})---the model progressively extracts signal from samples with intact trace content but cannot fully compensate for the information loss in the truncated majority.
563	The 84.45\% accuracy reflects a combination of trace information loss and model capability constraints.
564	
565	%% ============================================================
566	\section{Deduplication Statistics}
567	\label{sec:dedup_stats}
568	
569	Table~\ref{tab:dedup} reports the duplication rates across trace formats.
570	Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format---correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic---the dataset contains duplicate rows.
571	Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
572	The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
573	The \texttt{exception\_only} test set contains 48.99\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.
574	
575	\begin{table}[t]
576	\centering
577	\caption{Deduplication statistics. The \texttt{exception\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}
578	\label{tab:dedup}
579	\small
580	\begin{tabular}{lccc}
581	\toprule
582	\textbf{Split} & \textbf{Total} & \textbf{Unique} & \textbf{Dup.\ rate} \\
583	\midrule
584	exception\_only train & 4{,}720 & 2{,}858 & 39.45\% \\
585	exception\_only test  & 1{,}190 &   607 & 48.99\% \\
586	raw\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\% \\
587	\bottomrule
588	\end{tabular}
589	\end{table}
590	
591	%% ============================================================
592	\section{Regex Baseline Analysis}
593	\label{sec:regex_baselines}
594	
595	To establish a non-learning upper bound, we evaluate six regex-based baselines on the \texttt{exception\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \texttt{full\_trace} inputs.
596	
597	\begin{table}[t]
598	\centering
599	\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \texttt{exception\_only}, McNemar $p{<}0.001$). B6 uses an error count threshold. $^\ddag$B5 exploits a data formatting artifact: the \texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}
600	\label{tab:regex}
601	\small
602	\begin{tabular}{llc}
603	\toprule
604	\textbf{Baseline} & \textbf{Method} & \textbf{Acc (\%)} \\
605	\midrule
606	B1: \texttt{[ERROR]} presence & string match & 93.45 \\
607	B2: Traceback presence & string match & 71.51 \\
608	B3: Any keyword & union of B1+B2+Exception & 93.45 \\
609	B4: Exception type regex & regex on exception class names & \textbf{93.61} \\
610	B5: Format marker & \texttt{[No exception data]} $\to$ pass & 99.33$^\ddag$ \\
611	B6: Error count $\geq$2 & count threshold & 92.02 \\
612	\midrule
613	VOTA format regex & best regex on VOTA traces & 75.55 \\
614	full\_trace format regex & best regex on full traces & 77.39 \\
615	\bottomrule
616	\end{tabular}
617	\end{table}
618	
619	The strongest legitimate baseline (B4, 93.61\%) applies regex pattern-matching on Python exception class names (e.g., \texttt{ValueError}, \texttt{TypeError}).
620	Its errors concentrate on 8 boundary samples where a \texttt{ValueError} is raised inside a \texttt{try/except} block and caught---the program passes despite an exception occurring in the trace.
621	SFT \texttt{exception\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.
622	B5 (99.33\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\ SFT yields $p{=}0.041$, confirming a statistically significant difference.
623	
624	\paragraph{Cross-format comparison.}
625	Table~\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.
626	The SFT advantage increases with format complexity: \texttt{no\_trace} (+3.62pp over majority baseline) $<$ \texttt{full\_trace} (+4.37pp) $<$ \texttt{exception\_only} (+6.22pp) $\ll$ VOTA (+23.86pp).
627	The VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \texttt{exception\_only}'s simpler format allows regex to capture most of the signal.
628	
629	\begin{table}[t]
630	\centering
631	\caption{SFT vs.\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \texttt{no\_trace}, keyword matching for \texttt{full\_trace}, pattern matching for VOTA, exception type regex (B4) for \texttt{exception\_only}.}
632	\label{tab:regex_cross_format}
633	\small
634	\begin{tabular}{lccc}
635	\toprule
636	\textbf{Format} & \textbf{SFT (\%)} & \textbf{Regex (\%)} & \textbf{$\Delta$ (pp)} \\
637	\midrule
638	exception\_only & 99.83 & 93.61 & +6.22 \\
639	VOTA & 99.41 & 75.55 & +23.86 \\
640	full\_trace & 81.76 & 77.39 & +4.37 \\
641	no\_trace & 75.13 & 71.51 & +3.62 \\
642	\bottomrule
643	\end{tabular}
644	\end{table}
645	
646	%% ============================================================
647	\section{Cross-Model Zero-Shot Comparison}
648	\label{sec:zeroshot_cross_model}
649	
650	Table~\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \texttt{exception\_only} accuracy across four models.
651	Zero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.
652	SFT compresses the 42.44pp zero-shot range to 0.56pp, eliminating architecture-dependent variance.
653	
654	\begin{table}[t]
655	\centering
656	\caption{Zero-shot vs.\ SFT \texttt{exception\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.56pp.}
657	\label{tab:zeroshot_cross_model}
658	\small
659	\begin{tabular}{llccc}
660	\toprule
661	\textbf{Model} & \textbf{Size} & \textbf{Zero-shot (\%)} & \textbf{SFT (\%)} & \textbf{$\Delta$ (pp)} \\
662	\midrule
663	Qwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\
664	DeepSeek-6.7B & 6.7B & 90.59 & 99.33 & +8.74 \\
665	Qwen-7B & 7B & 89.08 & 99.83 & +10.75 \\
666	CodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\
667	\midrule
668	Range & --- & 42.44pp & 0.56pp & --- \\
669	\bottomrule
670	\end{tabular}
671	\end{table}
672	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc0e1a55-5987-4aac-b6ee-c86bcc9a1a98",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "0bb48217-93b1-4420-bf0b-24ff3af8bdbc",
  "sourceToolAssistantUUID": "dc0e1a55-5987-4aac-b6ee-c86bcc9a1a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-18T14:08:37.247Z_

Now let me check the references file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bb48217-93b1-4420-bf0b-24ff3af8bdbc",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAaf6hP53MsG59BD5Ni",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "384f1e4a-f101-4445-a1a5-8b8939438bc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAi6vrzGmcD6ri5bStDxhy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30822,
      "cache_read_input_tokens": 29889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30822,
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

_source line 33 · 2026-05-18T14:08:38.841Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XQp4gYRS66oan9prwe5YxK`</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "384f1e4a-f101-4445-a1a5-8b8939438bc8",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAaf6hP53MsG59BD5Ni",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd83899b-09a9-4722-88fc-cf3fd09c0c1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAi6vrzGmcD6ri5bStDxhy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30822,
      "cache_read_input_tokens": 29889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30822,
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

_source line 34 · 2026-05-18T14:08:38.868Z_

<details><summary>↩ Tool result · `toolu_01XQp4gYRS66oan9prwe5YxK`</summary>

```text
artifacts/dream_reports/dream_20260516T155731/worst/references.bib
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd83899b-09a9-4722-88fc-cf3fd09c0c1b",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "92c299f5-dcdf-4974-b0b1-0fa44878d4ef",
  "sourceToolAssistantUUID": "dd83899b-09a9-4722-88fc-cf3fd09c0c1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T14:08:41.726Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WwqLUoySViTL651JEjbHDJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92c299f5-dcdf-4974-b0b1-0fa44878d4ef",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAb4S9LvBSHWjZMNdSp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58420cc6-908c-450a-8479-caabaa9fa8ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPJwYpLXJwLwJbrdaLi56F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 151,
      "cache_read_input_tokens": 60711,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 151
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 60711,
          "cache_creation_input_tokens": 151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 151,
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

_source line 36 · 2026-05-18T14:08:41.731Z_

<details><summary>↩ Tool result · `toolu_01WwqLUoySViTL651JEjbHDJ`</summary>

```text
1	@inproceedings{chen2025tracepile,
2	  title={Chain of Execution Supervision Promotes General Reasoning in Large Language Models},
3	  author={Nuo Chen and Zehua Li and Keqin Bao and Junyang Lin and Dayiheng Liu},
4	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2510.23629},
7	}
8	
9	@inproceedings{ding2024traced,
10	  title={TRACED: Execution-aware Pre-training for Source Code},
11	  author={Yangruibo Ding and Ben Steenhoek and Kexin Pei and Gail Kaiser and Wei Le and Baishakhi Ray},
12	  booktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},
13	  year={2024},
14	  doi={10.1145/3597503.3608140},
15	  url={https://arxiv.org/abs/2306.07487},
16	}
17	
18	@article{chen2021evaluating,
19	  title={Evaluating Large Language Models Trained on Code},
20	  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},
21	  journal={arXiv preprint arXiv:2107.03374},
22	  year={2021},
23	  url={https://arxiv.org/abs/2107.03374},
24	}
25	
26	@article{austin2021program,
27	  title={Program Synthesis with Large Language Models},
28	  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and Sutton, Charles},
29	  journal={arXiv preprint arXiv:2108.07732},
30	  year={2021},
31	  url={https://arxiv.org/abs/2108.07732},
32	}
33	
34	@inproceedings{gu2024cruxeval,
35	  title={CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution},
36	  author={Alex Gu and Baptiste Rozi{\`e}re and Hugh Leather and Armando Solar-Lezama and Gabriel Synnaeve and Sida I. Wang},
37	  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},
38	  year={2024},
39	  url={https://arxiv.org/abs/2401.03065},
40	}
41	
42	@inproceedings{hu2022lora,
43	  title={LoRA: Low-Rank Adaptation of Large Language Models},
44	  author={Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},
45	  booktitle={Proceedings of the 10th International Conference on Learning Representations (ICLR)},
46	  year={2022},
47	  url={https://arxiv.org/abs/2106.09685},
48	}
49	
50	@article{qwen2025coder,
51	  title={Qwen2.5-Coder Technical Report},
52	  author={Qwen Team},
53	  journal={arXiv preprint arXiv:2409.12186},
54	  year={2024},
55	  url={https://arxiv.org/abs/2409.12186},
56	}
57	
58	@article{deepseek2024coder,
59	  title={DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence},
60	  author={Daya Guo and Qihao Zhu and Dejian Yang and Zhenda Xie and Kai Dong and Wentao Zhang and Guanting Chen and Xiao Bi and Y. Wu and Y.K. Li and Fuli Luo and Yingfei Xiong and Wenfeng Liang},
61	  journal={arXiv preprint arXiv:2401.14196},
62	  year={2024},
63	  url={https://arxiv.org/abs/2401.14196},
64	}
65	
66	@inproceedings{wang2025dcsh,
67	  title={Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models},
68	  author={Jian Wang and Xiaofei Xie and Qiang Hu and Shangqing Liu and Yi Li},
69	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
70	  year={2025},
71	  url={https://arxiv.org/abs/2509.11686},
72	}
73	
74	@inproceedings{ni2024next,
75	  title={NExT: Teaching Large Language Models to Reason about Code Execution},
76	  author={Ansong Ni and Miltiadis Allamanis and Arman Cohan and Yinlin Deng and Kensen Shi and Charles Sutton and Pengcheng Yin},
77	  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},
78	  year={2024},
79	  url={https://arxiv.org/abs/2404.14662},
80	}
81	
82	@inproceedings{eguchi2025etcot,
83	  title={Making LLMs Program Interpreters via Execution Trace Chain of Thought},
84	  author={Koshi Eguchi and Takuya Akiba},
85	  booktitle={ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)},
86	  year={2025},
87	}
88	
89	@article{ferrando2025execute,
90	  title={What I Cannot Execute, I Do Not Understand: Training and Evaluating {LLMs} on Program Execution Traces},
91	  author={Jordi Armengol-Estape and Quentin Carbonneaux and Tianjun Zhang and Aram H. Markosyan and Volker Seeker and Chris Cummins and Melanie Kambadur and Michael F.P. O'Boyle and Sida Wang and Gabriel Synnaeve and Hugh Leather},
92	  journal={arXiv preprint arXiv:2503.05703},
93	  year={2025},
94	  url={https://arxiv.org/abs/2503.05703},
95	}
96	
97	@inproceedings{xu2025cruxevalx,
98	  title={{CRUXEval-X}: A Benchmark for Multilingual Code Reasoning, Understanding and Execution},
99	  author={Ruiyang Xu and others},
100	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
101	  year={2025},
102	  url={https://arxiv.org/abs/2408.13001},
103	}
104	
105	@article{appt2024,
106	  title={{APPT}: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models},
107	  author={Quanjun Zhang and Chunrong Fang and Weisong Sun and Yan Liu and Tieke He and Xiaodong Hao and Zhenyu Chen},
108	  journal={IEEE Transactions on Software Engineering},
109	  year={2024},
110	  volume={50},
111	  number={3},
112	}
113	
114	@article{zhou2024llm4patch,
115	  title={Leveraging Large Language Model for Automatic Patch Correctness Assessment},
116	  author={Xin Zhou and Bowen Xu and Kisub Kim and DongGyun Han and Hung Huu Nguyen and Thanh Le-Cong and Junda He and Bach Le and David Lo},
117	  journal={IEEE Transactions on Software Engineering},
118	  year={2024},
119	  volume={50},
120	  number={11},
121	}
122	
123	@inproceedings{spiess2025calibration,
124	  title={Calibration and Correctness of Language Models for Code},
125	  author={Claudio Spiess and David Gros and others},
126	  booktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},
127	  year={2025},
128	  url={https://arxiv.org/abs/2402.02047},
129	}
130	
131	@inproceedings{foster2025mutation,
132	  title={Mutation-Guided {LLM}-based Test Generation at Meta},
133	  author={Christopher Foster and others},
134	  booktitle={Proceedings of the ACM International Conference on the Foundations of Software Engineering (FSE), Industry Track},
135	  year={2025},
136	  url={https://arxiv.org/abs/2501.12862},
137	}
138	
139	@inproceedings{widyasari2024fusefl,
140	  title={Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization},
141	  author={Ratnadira Widyasari and Jia Wei Ang and Truong Giang Nguyen and Neil Sharma and David Lo},
142	  booktitle={Proceedings of the IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)},
143	  year={2024},
144	}
145	
146	@inproceedings{huang2026tracecoder,
147	  title={{TraceCoder}: A Trace-Driven Multi-Agent Framework for Automated Debugging of {LLM}-Generated Code},
148	  author={Jiangping Huang and Wenguang Ye and Weisong Sun and Jian Zhang and Mingyue Zhang and Yang Liu},
149	  booktitle={Proceedings of the 48th IEEE/ACM International Conference on Software Engineering (ICSE)},
150	  year={2026},
151	  url={https://arxiv.org/abs/2602.06875},
152	}
153	
154	@article{wang2025inspectcoder,
155	  title={{InspectCoder}: Dynamic Analysis-Enabled Self Repair through Interactive {LLM}-Debugger Collaboration},
156	  author={Yunkun Wang and Yue Zhang and Guochang Li and Chen Zhi and Binhua Li and Fei Huang and Yongbin Li and Shuiguang Deng},
157	  journal={arXiv preprint arXiv:2510.18327},
158	  year={2025},
159	  url={https://arxiv.org/abs/2510.18327},
160	}
161	
162	@inproceedings{haque2025traces,
163	  title={Towards Effectively Leveraging Execution Traces for Program Repair with Code {LLMs}},
164	  author={Mirazul Haque and Petr Babkin and Farima Farmahinifarahani and Manuela Veloso},
165	  booktitle={KnowledgeNLP Workshop at ACL 2025},
166	  year={2025},
167	  url={https://arxiv.org/abs/2505.04441},
168	}
169	
170	@inproceedings{yang2024generalization,
171	  title={Unveiling the Generalization Power of Fine-Tuned Large Language Models},
172	  author={Haoran Yang and Yumeng Zhang and Jiaqi Xu and Hongyuan Lu and Pheng Ann Heng and Wai Lam},
173	  booktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
174	  year={2024},
175	  url={https://arxiv.org/abs/2403.09162},
176	}
177	
178	@inproceedings{dong2024composition,
179	  title={How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition},
180	  author={Guanting Dong and Hongyi Yuan and Keming Lu and Chengpeng Li and Mingfeng Xue and Dayiheng Liu and Wei Wang and Zheng Yuan and Chang Zhou and Jingren Zhou},
181	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
182	  year={2024},
183	  url={https://arxiv.org/abs/2310.05492},
184	}
185	
186	@inproceedings{tian2024debugbench,
187	  title={{DebugBench}: Evaluating Debugging Capability of Large Language Models},
188	  author={Runchu Tian and Yining Ye and Yujia Qin and Xin Cong and Yankai Lin and Yinxu Pan and Yesai Wu and Haotian Hui and Weichuan Liu and Zhiyuan Liu and Maosong Sun},
189	  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
190	  year={2024},
191	  url={https://arxiv.org/abs/2401.04621},
192	}
193	
194	@article{abreu2007accuracy,
195	  title={On the Accuracy of Spectrum-based Fault Localization},
196	  author={Rui Abreu and Peter Zoeteweij and Arjan J.C. van Gemund},
197	  journal={Testing: Academic and Industrial Conference Practice and Research Techniques (MUTATION)},
198	  year={2007},
199	  doi={10.1109/TAIC.PART.2007.13},
200	}
201	
202	@inproceedings{jones2002visualization,
203	  title={Visualization of Test Information to Assist Fault Localization},
204	  author={James A. Jones and Mary Jean Harrold and John Stasko},
205	  booktitle={Proceedings of the 24th International Conference on Software Engineering (ICSE)},
206	  year={2002},
207	  doi={10.1145/581339.581397},
208	}
209	
210	@article{wong2014dstar,
211	  title={{DStar}: An Effective Spectrum-Based Fault Localization Technique},
212	  author={W. Eric Wong and Vidroha Debroy and Ruizhi Gao and Yihao Li},
213	  journal={Journal of Systems and Software},
214	  volume={91},
215	  pages={44--58},
216	  year={2014},
217	  doi={10.1016/j.jss.2013.12.020},
218	}
219	
220	@inproceedings{kang2024autofl,
221	  title={{AutoFL}: Automated Fault Localization via Large Language Models},
222	  author={Sungmin Kang and Gabin An and Shin Yoo},
223	  booktitle={Proceedings of the 46th IEEE/ACM International Conference on Software Engineering (ICSE)},
224	  year={2024},
225	  url={https://arxiv.org/abs/2305.16397},
226	}
227	
228	@inproceedings{qin2024agentfl,
229	  title={{AgentFL}: Scaling LLM-based Fault Localization to Project-Level Context},
230	  author={Yihao Qin and Shangwen Wang and Yiling Lou and Jinhao Dong and Kaixin Wang and Xiaoling Li and Xiaoguang Mao},
231	  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)},
232	  year={2024},
233	  url={https://arxiv.org/abs/2403.16362},
234	}
235	
236	@inproceedings{widyasari2024llm4fl,
237	  title={{LLM4FL}: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair},
238	  author={Ratnadira Widyasari and Gopi Krishnan Rajbahadur and Shin Hwei Tan and Xin Xia and David Lo},
239	  booktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},
240	  year={2025},
241	}
242	
243	@inproceedings{mukherjee2025llmfl,
244	  title={Can Large Language Models Localize Faults like Developers? A Comprehensive Study},
245	  author={Soneya Binta Hossain and Nan Jiang and Qiang Zhou and Xiaopeng Li and Wen-Hao Chiang and Yingjun Lyu and Hoan Nguyen and Omer Tripp},
246	  booktitle={Proceedings of the 47th IEEE/ACM International Conference on Software Engineering (ICSE)},
247	  year={2025},
248	  url={https://arxiv.org/abs/2312.02986},
249	}
250	
251	@article{roziere2024code,
252	  title={Code Llama: Open Foundation Models for Code},
253	  author={Baptiste Rozi{\`e}re and Jonas Gehring and Fabian Gloeckle and Sten Sootla and Itai Gat and Xiaoqing Ellen Tan and Yossi Adi and Jingyu Liu and R{\'e}mi Lacroix and Tal Remez and J{\'e}r{\'e}my Rapin and Artyom Kozhevnikov and Ivan Evtimov and Joanna Bitton and Manish Bhatt and Cristian Canton Ferrer and Aaron Grattafiori and Wenhan Xiong and Alexandre D{\'e}fossez and Jade Copet and Faisal Azhar and Hugo Touvron and Louis Martin and Nicolas Usunier and Thomas Scialom and Gabriel Synnaeve},
254	  journal={arXiv preprint arXiv:2308.12950},
255	  year={2024},
256	}
257	
258	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58420cc6-908c-450a-8479-caabaa9fa8ca",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "64c6ccb9-e5fa-4f6c-b447-6571f97b0a98",
  "sourceToolAssistantUUID": "58420cc6-908c-450a-8479-caabaa9fa8ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-18T14:08:46.555Z_

Now let me also check the latest dream review report if available, and the paper_framing file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64c6ccb9-e5fa-4f6c-b447-6571f97b0a98",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAbGRiHJqEQ7Efvn8YJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2589ed01-8fd8-4637-abed-5dcfe1a69374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gzu7oC4FZamAeqoqfcQShr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4944,
      "cache_read_input_tokens": 60862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4944,
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

_source line 38 · 2026-05-18T14:08:47.026Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DbE7kHrkHjqvkrxfecydNS`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2589ed01-8fd8-4637-abed-5dcfe1a69374",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAbGRiHJqEQ7Efvn8YJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14b6b855-dbac-4f64-a6a1-8a3016017a94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gzu7oC4FZamAeqoqfcQShr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4944,
      "cache_read_input_tokens": 60862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4944,
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

_source line 39 · 2026-05-18T14:08:47.044Z_

<details><summary>↩ Tool result · `toolu_01DbE7kHrkHjqvkrxfecydNS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_framing.md\", \"content\": \"# Paper Framing — trace-verdict-study\\n\\n> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 \\\"label truncation/corruption\\\" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Insight\\n\\nVerdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.\\n\\nVOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The \\\"compression helps\\\" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\\n\\n## Core Claims (3)\\n\\n### Claim 1: Exception events are the most effective trace component for verdict prediction\\n\\nException summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.\\n\\n**Supporting evidence:**\\n- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027\\n- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)\\n- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致\\n- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier\\n- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)\\n- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)\\n- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison\\n\\n**DeepSeek seed analysis** ✅ (FINALIZED, D029):\\n\\n| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |\\n|------|-----------------|-------------|-------------|------------|--------|-----|\\n| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |\\n| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |\\n| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |\\n\\nseed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。\\n\\n**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**\\n\\n**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：\\n\\n| Seed | Accuracy | 95% CI | Errors |\\n|------|----------|--------|--------|\\n| 42 | 99.83% | [99.58, 100] | 2/1190 |\\n| 123 | 99.83% | [99.58, 100] | 2/1190 |\\n| 456 | 99.83% | [99.58, 100] | 2/1190 |\\n\\n3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。\\n\\n**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。\\n\\n### Claim 2: Information density, not gradient dilution, drives trace compression benefit\\n\\nFull traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.\\n\\nCross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).\\n\\n**Supporting evidence:**\\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)\\n- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)\\n- `vota_seed42_v5`: 99.41%, ECE=0.0054\\n- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)\\n- CRUXEval literature data (Wang et al.)\\n\\n### Claim 3: Two-tier diagnostic hierarchy for verdict prediction\\n\\nComponent ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:\\n- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.\\n- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.\\n\\nCombining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.\\n\\n**Supporting evidence:**\\n- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)\\n- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)\\n- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)\\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)\\n- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)\\n- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)\\n\\n**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：\\n\\n| Condition | Accuracy | ECE | Brier | 解读 |\\n|-----------|----------|-----|-------|------|\\n| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |\\n| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |\\n| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |\\n| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |\\n| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |\\n| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |\\n| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |\\n\\nno_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。\\n\\n**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.\\n\\n## Cross-Model Evidence Summary\\n\\n| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |\\n|-----------|-------------------|---------------------|-----------------|----------------|\\n| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |\\n| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |\\n| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |\\n| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |\\n\\n**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.\\n\\n## VOTA Repositioning\\n\\n**旧叙事**: VOTA 是 trace compression 方法，价值在于\\\"压缩使 trace 更有效\\\"。\\n\\n**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。\\n\\n**证据链**:\\n1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise\\n2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）\\n3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）\\n4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient\\n\\n**论文中的表述**: \\\"VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns.\\\"\\n\\n**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。\\n\\n## Story Spine\\n\\n- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.\\n\\n- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that \\\"no single trace representation consistently outperforms others.\\\" TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.\\n\\n- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.\\n\\n- **Headline result**: \\\"Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models.\\\"\\n\\n## Story Arc\\n\\n1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.\\n\\n2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.\\n\\n3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The \\\"trace reasoning\\\" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).\\n\\n4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。\\n\\n5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.\\n\\n## Dataset Characteristics\\n\\n### Data duplication analysis\\n\\n| Condition | Total | Unique | Duplication rate | Cause |\\n|-----------|-------|--------|------------------|-------|\\n| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |\\n| exception_only_test | 1190 | 607 | 48.99% | 同上 |\\n| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |\\n\\n**Train-test input overlap: 0（无数据泄漏）**\\n\\n**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。\\n\\n## DeepSeek full_trace 处理\\n\\n**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。\\n\\n**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。\\n\\n**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):\\n- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。\\n- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。\\n- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。\\n\\n**对论文叙事的影响**: 论文中所有 \\\"right-truncation corrupts/removes the verdict label\\\" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: \\\"trace content truncation causes information loss\\\"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。\\n\\n## External Benchmark (DebugBench) Positioning\\n\\n**DebugBench 仅作泛化性验证，不作 trace importance 证据。**\\n\\n| Condition | Main Dataset | DebugBench | Δ interpretation |\\n|-----------|-------------|------------|------------------|\\n| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |\\n| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |\\n| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |\\n\\n**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。\\n\\n**论文定位规则**：\\n- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）\\n- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）\\n- 禁止用 DebugBench 的 3.29pp lift 论证 \\\"trace 的核心价值\\\"——审稿人会攻击天花板效应\\n\\n## Venue Fit Risks\\n\\n| Risk | Assessment | Mitigation |\\n|------|-----------|------------|\\n| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |\\n| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |\\n| \\\"只是 feature engineering\\\" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |\\n| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |\\n| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |\\n| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |\\n| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |\\n| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |\\n| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Planned Response |\\n|---------|-----------------|\\n| \\\"exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？\\\" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |\\n| \\\"为什么 exception_only > VOTA? adding info 反而降?\\\" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |\\n| \\\"CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence\\\" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |\\n| \\\"只有 2 个模型，universality claim 太强\\\" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |\\n| \\\"99.83% 可能 saturated, 看不出 exception 到底学了什么\\\" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |\\n| \\\"只用了 1 个 seed\\\" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |\\n| \\\"eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?\\\" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |\\n| \\\"DeepSeek full_trace 坍塌是 bug 不是 finding\\\" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |\\n| \\\"calibration 数据只有 1 个 seed\\\" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |\\n| \\\"DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?\\\" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |\\n| \\\"DeepSeek seed sensitivity 说明 exception signal 不 robust\\\" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |\\n| \\\"exception_only 数据集 ~40-49% 重复，有效训练样本不足？\\\" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |\\n\\n## Discussion 要点\\n\\n### D1: eval_loss vs verdict accuracy 解耦\\nDeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.\\n\\n### D2: CRUXEval gap 假说 (revised — D030 confound)\\nVOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model \\\"execution reasoning readiness\\\" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。\\n\\n### D3: Simplicity as robustness (revised)\\nException signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。\\n\\n### D4: Checkpoint selection 与 gap 报告 (revised)\\n正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。\\n\\n### D5: Irreducible samples — GeneratorExit 根因分析\\n3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。\\n\\n**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。\\n\\n**为何不可约**:\\n1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。\\n2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。\\n3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。\\n4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。\\n\\n**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型\\\"理解\\\"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。\\n\\n### D6: Calibration as secondary evidence\\nCalibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 \\\"sufficient signal\\\" 论点——exception 不仅让模型预测对，还让模型 \\\"知道自己对\\\"。\\n\\n### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)\\n3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。\\n\\n### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]\\nDeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。\\n\\n### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]\\nDeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。\\n\\n### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]\\nD030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。\\n\\n**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。\\n\\n**Implications**: (1) 论文中所有 \\\"right-truncation corrupts/removes the verdict label\\\" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 \\\"most robust component\\\" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。\\n\\n### D8: Data duplication as representation signature\\nexception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。\\n\\n## Contingency Framing (已解决, 留存档)\\n\\n### Claim 1 — RESOLVED (D029: seed456=99.33% confirms \\\"consistently best component\\\")\\nseed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 \\\"exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds\\\"。\\\"0pp universal gap\\\" 叙事已放弃，转为数据驱动的 nuanced framing。\\n\\n### Claim 2 — RESOLVED (D006 + D009)\\nv5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.\\n\\n## 与 v1 Framing 的关键差异\\n\\n| 维度 | v1 | v2.9 |\\n|------|----|----|\\n| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |\\n| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |\\n| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |\\n| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |\\n| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |\\n| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |\\n| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |\\n| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |\\n| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |\\n| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |\\n| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |\\n| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |\\n| Narrative arc | \\\"VOTA helps\\\" | \\\"Exception events are consistently best; VOTA's value is isolating them; training stability matters\\\" |\\n\", \"total_chars\": 30551, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14b6b855-dbac-4f64-a6a1-8a3016017a94",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "4500f905-14f7-40b7-8f0b-fc838977ecab",
  "sourceToolAssistantUUID": "14b6b855-dbac-4f64-a6a1-8a3016017a94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-18T14:08:48.864Z_

<details open><summary>🔧 Tool call — Read · `toolu_017GUhGWAXCjm1sKUfcK8g7m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/best/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4500f905-14f7-40b7-8f0b-fc838977ecab",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAbGRiHJqEQ7Efvn8YJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d8e1fb3-361e-4552-a2c0-8a0a91682f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gzu7oC4FZamAeqoqfcQShr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4944,
      "cache_read_input_tokens": 60862,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 60862,
          "cache_creation_input_tokens": 4944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4944,
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

_source line 41 · 2026-05-18T14:08:48.874Z_

<details><summary>↩ Tool result · `toolu_017GUhGWAXCjm1sKUfcK8g7m`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=1in]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	\usepackage{array}
14	
15	\newcolumntype{R}{>{\raggedleft\arraybackslash}p{1.3cm}}
16	\newcolumntype{L}{>{\raggedright\arraybackslash}p{2.8cm}}
17	
18	\title{Exception Events Are the Minimal Sufficient Signal for\\Trace-Based Verdict Prediction}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\begin{abstract}
28	Execution traces can improve code language models, yet prior work on trace-enhanced supervised fine-tuning (SFT) has focused on generative tasks and found inconsistent benefits across models. We study a different setting: \textbf{verdict prediction}, the binary classification of whether a code solution passes or fails its test suite. Through systematic component ablation across four models spanning 1.5B to 13B parameters, we discover that \textbf{exception events}, compact structured summaries of runtime errors, are the minimal sufficient diagnostic signal.
29	On Qwen-2.5-Coder-7B, exception-only SFT achieves 99.83\% accuracy ($\pm$0.00 across 3 seeds) with near-perfect calibration (ECE = 0.0027). This result is scale-invariant: three of four models (1.5B, 7B, 13B) reach identical 99.83\%, while the fourth (DeepSeek-6.7B) reaches 99.33\% in 2 of 3 seeds. A sharp phase transition in the trace information budget concentrates over 87\% of the accuracy gain within a 128-token window (384 to 512 tail tokens), and this staircase pattern is consistent across all four models. Richer trace representations that require execution reasoning are model-dependent: VOTA compressed traces degrade by 14.96 percentage points on DeepSeek relative to Qwen. Few-shot prompting with GPT-4o and Claude Sonnet plateaus at 95.8\%, 4.0 points below the 7B SFT model. These results establish that verdict prediction is fundamentally a fault detection task, and that extracting the highest-specificity diagnostic signal outperforms both richer trace representations and larger general-purpose models.
30	\end{abstract}
31	
32	\section{Introduction}
33	
34	Execution traces record the runtime behavior of programs and carry rich diagnostic information about program correctness. Recent work has explored using traces to enhance code language models through supervised fine-tuning (SFT). DCSH \citep{dcsh2025} tested five trace formats on generation tasks and found that ``no single trace representation consistently outperforms others.'' TracePile \citep{tracepile2025} scaled trace data to 2.6M samples but evaluated only generative tasks. These studies leave open a fundamental question: what trace component, if any, is the \emph{active ingredient} that drives prediction quality?
35	
36	This question matters most for tasks where trace information is structurally relevant but where the right representation is unknown. Verdict prediction, determining whether a code solution passes or fails its test suite, is one such task. Unlike generation tasks where traces provide execution context for code completion, verdict prediction is binary classification where the model must detect the presence or absence of faults. Prior work on trace-enhanced classification \citep{traced2024} demonstrated that traces help encoder-based models, but did not decompose which trace components contribute to performance.
37	
38	Existing trace representations were designed for execution simulation rather than fault detection. Full execution traces are verbose (often exceeding 2,000 tokens), mixing diagnostic signals with irrelevant execution details. Compressed trace formats like VOTA (Verdict-Optimized Trace Abstraction) reduce length, but it remains unclear whether compression helps by reducing noise or by incidentally isolating specific diagnostic signals. No prior work has performed fine-grained component ablation to identify the minimal sufficient trace signal for classification tasks.
39	
40	We address this gap through a systematic ablation study. We decompose VOTA traces into three components (exception summaries, loop compression, assertion-point information) and train separate models on each component, plus full traces and a no-trace baseline. Our central finding is that \textbf{exception events} alone are sufficient: on Qwen-2.5-Coder-7B, exception-only SFT achieves 99.83\% accuracy with zero variance across three random seeds, matching the theoretical ceiling imposed by representation-inherent ambiguity (2 irreducible errors from Python \texttt{GeneratorExit}). Extending to four models spanning 1.5B to 13B parameters, we observe scale-invariant performance (three models at 99.83\%) and a sharp phase transition in the trace information budget where over 87\% of the accuracy gain concentrates in a 128-token window.
41	
42	Our contributions are:
43	\begin{enumerate}
44	    \item \textbf{Exception dominance}: Exception events are consistently the most effective trace component across all four models tested. Three models (1.5B, 7B, 13B) achieve identical 99.83\% accuracy; scale does not improve performance when the signal is already near-optimal. (Section~\ref{sec:main_results}, Table~\ref{tab:main})
45	    \item \textbf{Information density as primary bottleneck}: Label-only loss ablation decomposes the full-trace-to-VOTA gap into 26\% gradient dilution and 74\% information overload. A sharp phase transition across four models confirms that trace information density, not model capacity, determines the budget threshold. (Section~\ref{sec:phase_transition}, Table~\ref{tab:budget_curve})
46	    \item \textbf{Two-tier diagnostic hierarchy}: Component ablation reveals a strict hierarchy: Tier~1 (exception and assertion-point signals, each $\geq$99.83\%) subsumes Tier~2 (loop compression, 85.63\%). Combining tiers introduces noise rather than complementary information. (Section~\ref{sec:hierarchy}, Table~\ref{tab:ablation})
47	    \item[\textbf{+}] \textbf{Phase transition in trace budget} (bonus finding): All four models exhibit a staircase-shaped budget curve with a sharp transition between 384 and 512 tail tokens (sharpness index = 0.887). This transition is a dataset property, not a model property (cross-model standard deviation = 2.08 percentage points). (Section~\ref{sec:phase_transition}, Table~\ref{tab:budget_curve})
48	\end{enumerate}
49	
50	\section{Related Work}
51	
52	\paragraph{Trace-enhanced code understanding.}
53	Several recent efforts incorporate execution traces into code model training. DCSH \citep{dcsh2025} systematically compared five trace formats (print-based, variable-state, step-by-step, full execution, compressed) for generation tasks. Their finding that no single format consistently wins motivates our component-level ablation. TracePile \citep{tracepile2025} scaled trace data to 2.6M samples across multiple programming languages but evaluated only on code generation benchmarks (HumanEval, MBPP, DS-1000). TRACED \citep{traced2024} showed that execution traces improve encoder-based fault localization at ICSE 2024, providing the closest precedent for trace-enhanced classification. Our work differs from all three by (a) focusing on verdict prediction as a distinct task, (b) performing component-level ablation within a single trace format, and (c) identifying the minimal sufficient signal.
54	
55	\paragraph{Automated program repair and fault detection.}
56	The verdict prediction task is related to automated fault detection, where the goal is to identify buggy programs. DebugBench \citep{debugbench2024} provides a benchmark for LLM-based debugging with categorized bug types. Defects4J \citep{defects4j} is a standard benchmark for Java fault localization. Our work reframes verdict prediction explicitly as fault detection and shows that the optimal trace representation for this task is qualitatively different from what prior work assumed for generation tasks.
57	
58	\paragraph{Information compression for language models.}
59	The observation that compressed inputs can outperform verbose ones connects to work on prompt compression \citep{llmlingua2023} and context distillation. In our setting, VOTA's compression is not generic length reduction but incidental isolation of fault indicators. This finding aligns with recent observations that task-relevant information density matters more than total information quantity for LLM performance.
60	
61	\section{Method}
62	
63	\subsection{Task Definition}
64	
65	Given a programming problem $p$, a candidate solution $s$, and (optionally) an execution trace $t$ from running $s$ against the test suite for $p$, the goal is to predict the binary verdict $v \in \{\texttt{pass}, \texttt{fail}\}$. This is a standard binary classification task where the model is fine-tuned to output the verdict token.
66	
67	\subsection{Dataset}
68	\label{sec:dataset}
69	
70	We construct our dataset from HumanEval (164 problems) and MBPP-sanitized (427 problems), yielding 591 unique programming problems. For each problem, we collect 10 LLM-generated solutions, producing 5,910 samples total. Each sample consists of the problem description, the candidate solution, the execution trace from running the solution against the problem's test suite, and the ground-truth verdict. We split into 4,720 training and 1,190 test samples with zero train-test input overlap.
71	
72	The exception-only representation has a natural duplication rate of 39.45\% in training (4,720 total, 2,858 unique) and 48.99\% in testing (1,190 total, 607 unique). This duplication arises because multiple correct solutions to the same problem produce identical ``no exception'' traces. Raw full traces have only 1.81\% duplication (5,803 unique out of 5,910) because they contain solution-specific details such as variable values and memory addresses. The high duplication rate in exception-only data is a natural consequence of representation compactness, not a data quality issue.
73	
74	\subsection{VOTA Trace Compression}
75	
76	VOTA (Verdict-Optimized Trace Abstraction) compresses full execution traces into three components:
77	
78	\begin{itemize}
79	    \item \textbf{Exception summaries}: Structured records of runtime errors in the format \texttt{[ERROR] type: message}. These capture the diagnostic moment when a fault manifests.
80	    \item \textbf{Loop compression}: Repetitive loop iterations are collapsed into a summary that preserves iteration count and representative values while removing redundant detail.
81	    \item \textbf{Assertion-point information}: Records of assertion checks, including actual vs.\ expected values at test assertion points.
82	\end{itemize}
83	
84	\subsection{Experimental Conditions}
85	
86	We evaluate the following trace representations:
87	
88	\begin{itemize}
89	    \item \texttt{no\_trace}: Problem description and solution only, without any execution information.
90	    \item \texttt{full\_trace}: Complete uncompressed execution trace appended to the input.
91	    \item \texttt{full\_trace\_label\_only}: Full trace with label-only loss masking (gradient computed only on the verdict token, not on trace tokens). This isolates the gradient dilution effect.
92	    \item \texttt{VOTA}: The full compressed trace containing all three VOTA components.
93	    \item \texttt{exception\_only}: Only the exception summary component from VOTA.
94	    \item \texttt{ae\_only}: Only the assertion-point (actual/expected) component.
95	    \item \texttt{loop\_only}: Only the loop compression component.
96	    \item \texttt{vota\_no\_ae}: VOTA with assertion-point information removed.
97	\end{itemize}
98	
99	Additionally, we define tail-$N$ conditions that truncate the raw execution trace to its last $N$ tokens, for $N \in \{256, 384, 512, 1024, 2048\}$. These conditions probe the spatial distribution of diagnostic information within traces.
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d8e1fb3-361e-4552-a2c0-8a0a91682f4c",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "cb69b5ff-fc9e-4ba4-ae1a-aadba8ccf6f0",
  "sourceToolAssistantUUID": "3d8e1fb3-361e-4552-a2c0-8a0a91682f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-18T14:08:52.307Z_

Now let me load the tool needed to submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb69b5ff-fc9e-4ba4-ae1a-aadba8ccf6f0",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAbnhdJKkZ9WE93a8M2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19c790ad-321e-432f-acf7-2c1d143676b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKbrMcXaySqwasMXQ8n6CM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16918,
      "cache_read_input_tokens": 65806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16918,
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

_source line 43 · 2026-05-18T14:08:52.939Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01R9xs1NmwWc7fqVRV25nj9S`</summary>

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
  "parentUuid": "19c790ad-321e-432f-acf7-2c1d143676b3",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAbnhdJKkZ9WE93a8M2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25df2aa9-ff56-4b7c-b31e-5432349bb444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKbrMcXaySqwasMXQ8n6CM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16918,
      "cache_read_input_tokens": 65806,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 65806,
          "cache_creation_input_tokens": 16918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16918,
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

_source line 44 · 2026-05-18T14:08:52.942Z_

<details><summary>↩ Tool result · `toolu_01R9xs1NmwWc7fqVRV25nj9S`</summary>

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
  "parentUuid": "25df2aa9-ff56-4b7c-b31e-5432349bb444",
  "isSidechain": true,
  "promptId": "b7425a62-3dba-4b9a-a2d0-258c4838a220",
  "agentId": "ac1895a814ace99e3",
  "type": "user",
  "uuid": "00c0e34d-2109-461a-b0b6-6263bbbaf91d",
  "sourceToolAssistantUUID": "25df2aa9-ff56-4b7c-b31e-5432349bb444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-18T14:10:15.973Z_



I have now read the complete paper (main text + appendix), the references file (27 bib entries), the literature map (34 papers tracked), and the paper framing document. Let me compose the review.

### R2 Review: Novelty & Related Work

**Summary**: This paper performs a component ablation of execution trace representations for verdict prediction (pass/fail classification) across four code LLMs. The core finding is that exception events alone achieve 99.33-99.83% accuracy, outperforming richer trace representations. The paper is a competent empirical study with thorough ablations, but the core finding has limited surprise value, the related work coverage has improved substantially from the initial 5 citations but still has gaps in software testing literature, and several framing choices overstate the contribution.

**Strengths**:

- S1: **Thorough experimental design.** The ablation across seven trace conditions, four models, three architecture families, and multiple seeds is systematic. The loss decomposition (gradient dilution vs. information overload) is a genuinely useful analytical contribution. The tail-truncation experiments localizing the diagnostic signal to a specific token window are well-designed.

- S2: **Honest reporting of negative and inconvenient results.** The paper transparently reports the DeepSeek seed sensitivity (91.09% outlier), the ae_only vs. exception_only anomaly, irreducible GeneratorExit errors, and VOTA's cross-model degradation. The limitations section is uncommonly thorough. This candor builds trust.

- S3: **Practical utility is clear.** The finding that median 150 tokens suffice for near-perfect verdict prediction, compared to thousands of tokens for full traces, has direct engineering value for CI/CD pipelines and token-constrained deployments.

- S4: **Statistical rigor.** Paired bootstrap resampling with 10,000 iterations, Wilson CIs, McNemar tests, and multi-seed robustness checks exceed the statistical standards of most empirical NLP papers.

- S5: **Calibration analysis.** Going beyond accuracy to report ECE and Brier scores adds a meaningful dimension. The 63x ECE gap between exception_only and no_trace is striking.

**Weaknesses**:

- W1: **The core finding is largely expected, limiting novelty.** That exception events (explicit error messages) predict pass/fail better than verbose execution logs is intuitive to anyone who has debugged code. The paper frames this as a discovery ("more surprisingly, adding trace information beyond exceptions actively hurts"), but an exception is a direct, unambiguous fault indicator by definition. A skilled developer or a regex can achieve 93-99% from exception presence alone (as the paper's own B4/B5 baselines demonstrate). The intellectual contribution is confirming and quantifying an intuition, not overturning one. This is fine for a findings paper but the "Exception Events Are All You Need" framing implies a deeper insight than is delivered.

- W2: **The title and framing borrow unjustified gravitas.** "Exception Events Are All You Need" echoes the Transformer paper, implying a paradigm-shifting finding. The actual contribution is an ablation study on a narrow binary classification task using a single dataset family (HumanEval+MBPP). The gap between the title's ambition and the paper's scope is a presentation problem that will irritate reviewers.

- W3: **Related work, while improved from the initial draft, still has coverage gaps.** The paper now has ~27 references, which is adequate in quantity, but there are notable omissions:
  - No citation of classical software testing literature on test oracle problems (Barr et al., "The Oracle Problem in Software Testing," IEEE TSE 2015).
  - No mention of mutation testing literature, which is directly relevant to fault detection (Papadakis et al., "Mutation Testing Advances," Advances in Computers 2019).
  - The fault localization paragraph (Ochiai, Tarantula, DStar, AutoFL, AgentFL, LLM4FL) is well-done, but the connection to SBFL is stated without adequately explaining how verdict prediction differs from or contributes to the FL pipeline beyond "verdict prediction is a prerequisite."
  - No citation of test outcome prediction work in the SE community (e.g., Spieker et al., "Reinforcement Learning for Automatic Test Case Prioritization," ISSTA 2017; or Bertolino et al.'s work on adaptive testing).
  - The prompt compression citation (LLMLingua) appears only in the dream report version, not in the submitted paper's bib file. The related work mentions "prompt compression" conceptually but no actual citation exists in the main paper's references.bib.

- W4: **The "two-tier diagnostic hierarchy" contribution is an observation, not a method.** Saying "exceptions work well, loops work less well" and labeling it a "hierarchy" adds terminology without adding insight. The tiers are not derived from any principled analysis; they are post-hoc labels on empirical accuracy numbers. This would not be listed as a contribution at a top venue.

- W5: **The ae_only anomaly undermines the headline claim.** Table 2 shows ae_only achieves 99.92% on seed 42 (and 99.64% mean across 3 seeds), while exception_only achieves 99.83% (and 99.83% mean). The paper claims exception_only is "the minimal sufficient signal" and "the most effective component," but ae_only has a numerically higher single-seed accuracy. The paper addresses this in the Discussion by arguing exception_only has zero seed variance vs. ae_only's sigma=0.49, making it "more stable." This is a reasonable argument, but the framing should be more nuanced: ae_only and exception_only are statistically indistinguishable (the paper itself notes p=0.80 in the framing doc), and exception_only's advantage is stability, not accuracy. The paper's current framing in the Abstract and Introduction obscures this.

- W6: **Narrow scope limits generalizability claims.** The study uses only Python, only HumanEval+MBPP (591 problems), only LLM-generated solutions (from the same model family used for evaluation), and only exceptions that produce explicit error messages. The paper acknowledges that "production code may exhibit a broader spectrum of silent logic errors where no exception is raised," which is precisely the real-world scenario where verdict prediction is most needed and where exceptions would be least useful. The DebugBench evaluation (100% exception_only, but also 96.7% no_trace) does not meaningfully address this concern because DebugBench bugs are structurally distinctive single-point mutations.

- W7: **The information density decomposition is approximate and underspecified.** The 26%/74% split (gradient dilution vs. information overload) comes from a single intermediate point (label_only_loss at 86.22%). The paper acknowledges "the two factors may interact, so this decomposition is approximate," but then proceeds to cite "~74%" and "~26%" as if they are robust findings throughout the paper, including in the Abstract. A single ablation point does not support a precise percentage decomposition, especially when interactions are acknowledged.

- W8: **The "phase transition" language is overstated.** The accuracy jump from tail-256 to tail-512 is a natural consequence of the exception traceback fitting within 500 tokens. Calling this a "phase transition" (a term with specific meaning in physics and learning theory) is imprecise. It is a threshold effect: below 500 tokens the exception is truncated, above it the exception is captured. This is expected behavior, not a phase transition.

**Questions for Authors**:

- Q1: Given that ae_only achieves 99.92% on seed 42 (higher than exception_only's 99.83%) and the two are statistically indistinguishable (p=0.80 per your framing document), why does the paper consistently claim exception_only is "the most effective" rather than framing both as co-equal Tier 1 signals? The zero-variance argument for exception_only is about robustness, not effectiveness.

- Q2: What fraction of failing test cases in your dataset actually raise exceptions? If nearly all failures produce exceptions, then exception_only is trivially sufficient. If a significant fraction of failures are silent logic errors (wrong output, no exception), then exception_only's near-perfect accuracy is more impressive. This number is critical for interpreting the results but is not reported.

- Q3: The regex baseline B5 (format marker detection) achieves 99.33%. The SFT model achieves 99.83%. The incremental value of SFT over a trivial pattern match is 0.50pp (6 additional correct samples out of 1,190). Is this increment sufficient to justify the SFT approach? How would you respond to a reviewer who argues the practical value of SFT over regex is negligible for this task?

- Q4: You evaluate on models that were likely exposed to HumanEval/MBPP during pretraining (acknowledged in Limitations). Have you considered evaluating on a held-out benchmark that is less likely to be in pretraining data? The self-familiarity concern is non-trivial for a 99.83% accuracy claim.

- Q5: The paper states that verdict prediction is "a prerequisite to fault localization." In practice, test frameworks already provide pass/fail verdicts. What is the real-world deployment scenario where a model must predict verdicts from traces rather than simply reading the test runner's output?

**Missing References**:

- Barr et al., "The Oracle Problem in Software Testing: A Survey," IEEE TSE 2015 (directly relevant to verdict/oracle prediction)
- Papadakis et al., "Mutation Testing Advances: An Analysis and Survey," Advances in Computers 2019 (fault detection methodology)
- Spieker et al., "Reinforcement Learning for Automatic Test Case Prioritization and Selection in Continuous Integration," ISSTA 2017 (test outcome prediction in CI)
- Yefet et al. or Alon et al. on code representation learning (code2vec, code2seq) as alternative code representations
- LLMLingua (Jiang et al., 2023) is referenced conceptually in the dream report but absent from the actual paper's bibliography
- Defects4J (Just et al., 2014) is mentioned in the dream report's related work but absent from the submitted paper's references despite being a standard fault detection benchmark
- REval (Chen et al., 2024) and CodeMind (Liu et al., 2024) from your own literature map are relevant to execution reasoning evaluation but uncited

**Minor Issues**:

- The paper uses em-dashes in several places in the Discussion section (e.g., "whether it failed, and dilute the model's attention without providing complementary diagnostic information"). While most are avoided, a thorough pass is needed.
- The Conclusion largely repeats the Abstract. At 9 pages, space could be better used to address scope limitations or add missing analysis.
- Figure 1 (trace overview) is described in the caption but I cannot verify its information density without seeing it. Ensure it is not a trivial pipeline diagram.
- The paper title in main.tex ("Component Ablation for Trace-Based Verdict Prediction") differs from the title given in the review prompt ("Fault Indicator Isolation as the Robust Mechanism for Execution Trace Verdict Prediction"). Ensure consistency.
- Some conditions (ae_only, loop_only) are tested only on Qwen-7B, limiting the cross-model generalizability of the tier hierarchy claim.
- The Appendix is very long (~15 pages of tables and analysis). While thorough, some of this material (e.g., the regex baseline analysis, deduplication statistics) could be condensed.

**Score**: 2.5/6 (Borderline Findings)

**Confidence**: 4/5

**Justification**: The paper is a well-executed empirical study with commendable statistical rigor and honest reporting. However, the core finding (exceptions predict pass/fail) has limited novelty, as it confirms rather than overturns intuition. The narrow scope (Python only, HumanEval+MBPP only, exception-raising failures only), the overstatement in framing ("All You Need," "phase transition," "two-tier hierarchy" as a contribution), and the remaining gaps in related work positioning against the broader software testing literature place this below the Main conference threshold. The 0.50pp improvement of SFT over a regex baseline (B5) raises questions about whether the learned component adds meaningful value beyond pattern matching. With stronger positioning against SE literature, a more honest framing of novelty (empirical quantification of an expected finding rather than a surprising discovery), and evaluation on scenarios with silent logic errors, this could reach Findings quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00c0e34d-2109-461a-b0b6-6263bbbaf91d",
  "isSidechain": true,
  "agentId": "ac1895a814ace99e3",
  "requestId": "req_011CbAAc668wMcjMnvkf6ruJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1f0bef7-3b14-41d8-af53-4aafc06df542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "1de37377-3b2d-4064-93c3-e74486d99dc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016v7CdubeajzGWfUyPPWGLb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 82724,
      "output_tokens": 2981,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2981,
          "cache_read_input_tokens": 82724,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 680,
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
