# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**. Review the paper below usi

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6c99a2559f41878a.jsonl`
- **Structured JSON:** [`ab678736c6b66c8aa4d9.json`](../../sessions/ab/ab678736c6b66c8aa4d9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-18T12:24:04.223Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title:** "Exception Events Are All You Need: Diagnostic Signal Locality in Execution Trace Verdict Prediction"

**Core claim:** For binary pass/fail verdict prediction on execution traces, exception events (compact structured error summaries of ~400-500 tokens at trace tail) are sufficient and optimal. Full traces hurt due to information overload (74%) and gradient dilution (26%).

**Models:** 4 code LLMs: Qwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, CodeLlama-13B-Instruct.

**Dataset:** HumanEval (164) + MBPP-sanitized (427) = 591 problems, 10 solutions each → 5910 triples. Train 4720 / Test 1190. Class distribution: 71.5% pass / 28.5% fail.

**Key results:**
- Exception-only SFT: 99.83% (Qwen-7B, 3 seeds identical), 99.83% (Qwen-1.5B), 99.33% (DeepSeek), 99.83% (CodeLlama)
- Full trace: 81.76%, VOTA: 99.41%, No trace: 75.13% (all Qwen-7B)
- Causal decomposition: label-only loss on full trace → 86.22%. So gradient dilution = 26%, info overload = 74%
- Two-tier hierarchy: Tier 1 (exceptions 99.83%, assertions 99.92%) > Tier 2 (loops 85.63%)
- Token budget curve: sharp phase transition at 384→512 tail tokens (mean Δ=17.1pp, gradient ratio 8.8:1) across all 4 models
- Cross-seed tail-512: all std < 1pp across 4 models
- Training dynamics: exception-only crosses full-trace ceiling in ~45 steps
- Failure mode: only 2 errors (GeneratorExit FP), fully deterministic
- Calibration: ECE < 0.01 for all 4 models on exception-only
- OOD: Java 97.2%, JavaScript 96.3% (only Qwen-7B tested)
- Frontier model comparison: SFT exc-only 1.5B (99.83%) > Claude 3-shot (96.1%) > GPT-4o 3-shot (95.1%)

**5 claimed contributions:**
1. Exception dominance universal across 4 models/3 families/2 scales
2. 26%/74% causal decomposition
3. Two-tier diagnostic hierarchy
4. Universal sharp phase transition at ~400 tokens
5. LoRA training stability as practical bottleneck

**Training:** LoRA rank 16, α=32, lr=2e-4, batch 4, 3 epochs, single A100-80GB.

**Evaluation:** Accuracy, per-class F1, ECE, Brier score, McNemar's test, bootstrap CI.

## Experiment Design Reference (from review_context.yaml)

The full experiment plan includes these imagined experiments:
1. **tail-384 × 4 models** (plan_016): Filling in 384-token budget point for all 4 models. Expected: all ≤81%, statistically equivalent to tail-256 (McNemar p>0.1).
2. **cross-seed tail-512 × 4 models** (plan_017): 3 seeds each at tail-512. Expected: all std < 1pp.
3. **CodeLlama-13B tail-2048** (plan_016): Completing the budget curve matrix.
4. **Failure mode analysis** (plan_018): Systematic error analysis across conditions.
5. **Cross-model calibration** (plan_019): 4-model ECE/Brier on exception-only.
6. **Few-shot prompting baseline** (plan_020): GPT-4o/Claude 0-shot and 3-shot.
7. **OOD generalization** (plan_021): Java/JavaScript cross-language.
8. **Training dynamics** (plan_022): Step-level learning curves.

The paper covers ALL of these experiments. Judge whether the results are presented convincingly.

## Your Review Structure

Please produce a structured review with:
1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, focus on methods and experimental design)
3. **Weaknesses** (bulleted, focus on methods and experimental design)
4. **Questions for Authors**
5. **Missing Experiments or Analyses**
6. **Minor Issues**
7. **Score** (1-6) with justification
8. **Confidence** (1-5, where 5=expert)

Be rigorous. Consider:
- Is the experimental design sound? Are controls adequate?
- Is the dataset sufficient? Any data leakage concerns?
- Are statistical tests appropriate?
- Are the claimed contributions supported by the evidence?
- Are there confounds or alternative explanations not addressed?
- How do the frontier model comparisons (GPT-4o, Claude) hold up? Are they real experiments or estimates?
- Is the OOD evaluation convincing?
- Is the "causal decomposition" truly causal?
- Does the phase transition claim hold up to scrutiny?


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "81123471-e1b4-438f-8862-ff5056adf38e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T12:24:04.228Z_

```json
{
  "parentUuid": "81123471-e1b4-438f-8862-ff5056adf38e",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
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
  "uuid": "5ea6c737-0dbe-4793-b972-36ac12cad503",
  "timestamp": "2026-05-18T12:24:04.228Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T12:24:07.438Z_



I'll start by reading the paper and any relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ea6c737-0dbe-4793-b972-36ac12cad503",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2cX7MPpVr7CFrn8Mtc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1c1e22e-2cbb-4ada-84f0-0d69f05aaf2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVbeW7uXjXVfT1h9i5AbVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16715,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16715,
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

_source line 4 · 2026-05-18T12:24:07.849Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Y4hdrd6rj87ydRqvDDxGjm`</summary>

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
  "parentUuid": "f1c1e22e-2cbb-4ada-84f0-0d69f05aaf2d",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2cX7MPpVr7CFrn8Mtc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "823c1c05-23c6-4653-a0a0-c258c2436c81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVbeW7uXjXVfT1h9i5AbVd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16715,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16715,
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

_source line 5 · 2026-05-18T12:24:07.859Z_

<details><summary>↩ Tool result · `toolu_01Y4hdrd6rj87ydRqvDDxGjm`</summary>

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
  "parentUuid": "823c1c05-23c6-4653-a0a0-c258c2436c81",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "65ead250-cac1-4d2d-98b0-e918eafa15e9",
  "sourceToolAssistantUUID": "823c1c05-23c6-4653-a0a0-c258c2436c81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T12:24:10.414Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65ead250-cac1-4d2d-98b0-e918eafa15e9",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2cnoAvUMccVo8H4y2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1871635c-f033-422f-9961-0697fbe6fbd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012odbMbJGCzmXAKfgvedMft",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-18T12:24:11.415Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01T2wYNFaE9CmcoiaBEVZBtq`</summary>

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
  "parentUuid": "1871635c-f033-422f-9961-0697fbe6fbd8",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2cnoAvUMccVo8H4y2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44574d25-fe21-4715-9024-20341be23393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012odbMbJGCzmXAKfgvedMft",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 8 · 2026-05-18T12:24:11.430Z_

<details><summary>↩ Tool result · `toolu_01T2wYNFaE9CmcoiaBEVZBtq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/report.md\", \"content\": \"# Handover — 2026-05-18\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- codellama13b_full_trace_tail384_seed42: CodeLlama-13B tail-384 (label_only_loss) 应在 85-95% 之间（256→512 phase transition 中间点），验证 label_only_loss 在短序列下也有效（等待人工审批）\\n- qwen15b_full_trace_tail384_seed42: Qwen-1.5B tail-384 应在 80-90% 之间（小模型在 transition zone 可能更低），精确定位 phase transition 曲线形状（等待人工审批）\\n- qwen1.5b_full_trace_seed42: Qwen-1.5B full_trace 应达 ≥96% accuracy，确认 1.5B 小模型在 full trace 条件下与 7B 可比（trace quality 主导而非 model capacity）（排队等待 GPU）\\n- qwen1.5b_exception_only_seed42: Qwen-1.5B exception_only 应达 ≥99% accuracy，确认 minimal sufficient signal 在 1.5B scale 有效，signal quality 主导 model capacity（排队等待 GPU）\\n- qwen1.5b_vota_seed42: Qwen-1.5B VOTA 应在 82-90% accuracy，可能略低于 7B 因 VOTA 条件下 scale-sensitivity 更明显（排队等待 GPU）\\n- qwen1.5b_no_trace_seed42: Qwen-1.5B no_trace 应在 65-75% (≈majority baseline)，确认无 trace 小模型表现更差、scale 无法补偿（排队等待 GPU）\\n- codellama_exception_only_seed42: CodeLlama-13B exception_only 应达 ≥99.33% accuracy，与其他 3 模型一致，确认 minimal sufficient signal 跨 4 模型 3 架构 1.5B-13B universal（排队等待 GPU）\\n- codellama_vota_seed42: CodeLlama-13B VOTA 应在 85-92% accuracy，与 Qwen-7B/DeepSeek VOTA 对齐，作 rebuttal 储备验证 ablation condition 跨 scale 一致性（排队等待 GPU）\\n- codellama_no_trace_seed42: CodeLlama-13B no_trace 应在 70-78% (≈majority baseline)，确认无 trace 时 13B scale 无法补偿信息缺失（排队等待 GPU）\\n- deepseek_full_trace_tail384_seed42: DeepSeek-6.7B tail-384 应在 85-93% 之间（256→512 phase transition 的中间点），精确定位 phase transition 曲线形状（已分配 ? GPU:?，等待提交）\\n- …另有 1 项\\n\\n## 近期结论\\n- **qwen7b_full_trace_head2048_seed42** (success): Qwen-7B head-2048 应在 75-82% (signal-poor convergence band)，与其他 3 模型 head-2048 (75.3-79.9%) 对齐，补全 4 模型 head-tail gap claim\\n- **codellama13b_full_trace_tail2048_seed42_v3** (negative): CodeLlama-13B tail-2048 用 label_only_loss 应恢复到 95-98%（与其他 3 模型 tail-2048 对齐），确认 v2 的 29.6% 源于 full-sequence loss 稀释 ← 基于 codellama13b_full_trace_tail2048_seed42_v2\\n- **codellama13b_full_trace_tail1024_seed42_v3** (success): CodeLlama-13B tail-1024 用 label_only_loss 应恢复到 ~96.5%（与 DeepSeek 96.47%、Qwen-1.5B 96.6% 对齐），确认 v2 的 87.6% 源于 full-sequence loss 稀释而非 tail-1024 条件本身 ← 基于 codellama13b_full_trace_tail1024_seed42_v2\\n\\n## 趋势\\n成功 66 / 负向 13 / 失败 5 / 共 94\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-11235: 无 GPU 信息\\n\\n## 告警\\n- no_trace_seed42: 已被终止 — unknown\\n- vota_seed42: 已被终止 — unknown\\n- no_trace_seed42_v2: 已被终止 — unknown\\n- vota_seed42_v2: 已被终止 — unknown\\n- no_trace_seed42_v3: 已被终止 — unknown\\n- vota_seed42_v3: 已被终止 — unknown\\n- full_trace_seed42: 已被终止 — unknown\\n- vota_exception_only_seed42: 训练失败 — unknown\\n- vota_seed123: 训练失败 — unknown\\n- vota_seed456: 训练失败 — unknown\\n- deepseek_full_trace_seed42_v2: 已被终止 — unknown\\n- full_trace_2048tok_seed42: 已被终止 — unknown\\n- codellama13b_nomarker_seed42: 已被终止 — unknown\\n- codellama13b_full_trace_tail1024_seed42: 训练失败 — unknown\\n- codellama13b_full_trace_tail2048_seed42: 训练失败 — unknown\\n\", \"total_chars\": 2881, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44574d25-fe21-4715-9024-20341be23393",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "9332f4ec-4d8b-45aa-9cde-e000d479a11f",
  "sourceToolAssistantUUID": "44574d25-fe21-4715-9024-20341be23393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T12:24:12.359Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CrMgRUVi8NSGbAifV9C8vQ`</summary>

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
  "parentUuid": "9332f4ec-4d8b-45aa-9cde-e000d479a11f",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2cnoAvUMccVo8H4y2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dde422e5-7e56-49ca-83e7-afedd6283205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012odbMbJGCzmXAKfgvedMft",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 10 · 2026-05-18T12:24:12.384Z_

<details><summary>↩ Tool result · `toolu_01CrMgRUVi8NSGbAifV9C8vQ`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dde422e5-7e56-49ca-83e7-afedd6283205",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "42d7321a-813f-49e2-a02c-20ddddb71a83",
  "sourceToolAssistantUUID": "dde422e5-7e56-49ca-83e7-afedd6283205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T12:24:12.994Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011MzRGpCZg8b8iWQqtpxXXD`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42d7321a-813f-49e2-a02c-20ddddb71a83",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2cnoAvUMccVo8H4y2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbbffab1-fcf7-4680-810f-8769717551a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012odbMbJGCzmXAKfgvedMft",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16715,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 283,
          "cache_read_input_tokens": 16715,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 12 · 2026-05-18T12:24:13.034Z_

<details><summary>↩ Tool result · `toolu_011MzRGpCZg8b8iWQqtpxXXD`</summary>

```text
artifacts/dream_reports/dream_20260515T013018/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T013018/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T013018/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T013018/best/review_context.yaml
artifacts/dream_reports/dream_20260515T013018/median/review_context.yaml
artifacts/dream_reports/dream_20260515T013018/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T013018/meta.yaml
artifacts/literature_map.yaml
artifacts/dream_reports/dream_20260515T084908/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T084908/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T084908/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T084908/best/review_context.yaml
artifacts/dream_reports/dream_20260515T084908/median/review_context.yaml
artifacts/dream_reports/dream_20260515T084908/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T084908/meta.yaml
literature_map.yaml
writing_plan.yaml
artifacts/review_issues.yaml
artifacts/dream_reports/dream_20260516T105259/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T105259/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T105259/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T105259/best/review_context.yaml
artifacts/dream_reports/dream_20260516T105259/median/review_context.yaml
artifacts/dream_reports/dream_20260516T105259/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T105259/meta.yaml
constraints.yaml
artifacts/dream_reports/dream_20260516T155731/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T155731/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T155731/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T155731/best/review_context.yaml
artifacts/dream_reports/dream_20260516T155731/median/review_context.yaml
artifacts/dream_reports/dream_20260516T155731/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T155731/meta.yaml
paper_provenance.yaml
experiment_plan.yaml
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260518T113804/best/imagined_experiments.yaml
decisions.yaml
registry.yaml
artifacts/dream_reports/dream_20260518T113804/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T113804/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260518T113804/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbbffab1-fcf7-4680-810f-8769717551a4",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "813835e6-5c6d-45f2-9fc5-94639a2ba47d",
  "sourceToolAssistantUUID": "dbbffab1-fcf7-4680-810f-8769717551a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-18T12:24:17.689Z_

Let me read the latest dream report paper (the most recent one) and the actual paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "813835e6-5c6d-45f2-9fc5-94639a2ba47d",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2dAoW3Q6oECw3FW6uJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b05fb8cb-d4a3-475b-80b3-42c35708f15e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZdV5AD1pu8jgi4Qe8YR61",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3476,
      "cache_read_input_tokens": 18162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3476,
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

_source line 14 · 2026-05-18T12:24:18.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_011d1WeW1dTnqJzX3rgYeosh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b05fb8cb-d4a3-475b-80b3-42c35708f15e",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2dAoW3Q6oECw3FW6uJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4d05c70-5ece-4367-92bf-63b7f98f9a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZdV5AD1pu8jgi4Qe8YR61",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3476,
      "cache_read_input_tokens": 18162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3476,
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

_source line 15 · 2026-05-18T12:24:18.512Z_

<details><summary>↩ Tool result · `toolu_011d1WeW1dTnqJzX3rgYeosh`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{amsmath}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage{subcaption}
11	\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}
12	
13	\title{Exception Events Are All You Need: Diagnostic Signal Locality \\in Execution Trace Verdict Prediction}
14	
15	\author{Anonymous}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Execution traces are increasingly used to improve code Large Language Model (LLM) performance, yet no prior work has identified which trace components drive verdict prediction (binary pass/fail classification). We reframe verdict prediction as fault detection and conduct a systematic ablation across four code LLMs spanning three model families and two parameter scales (1.5B to 13B). We find that exception events, compact structured error summaries occupying roughly 400--500 tokens at the trace tail, consistently achieve the highest accuracy across all models (95--99\%), outperforming full traces (81.8\%) by up to 18 percentage points. A causal decomposition of the full-trace-to-compressed-trace gap reveals that information overload accounts for 74\% of the deficit while gradient dilution contributes only 26\%. Component ablation uncovers a strict two-tier diagnostic hierarchy: Tier~1 signals (exceptions, assertion outcomes) are individually near-perfect and sufficient; Tier~2 signals (loop summaries) carry moderate information but are fully subsumed. A token budget analysis across all four models reveals a universal sharp phase transition between 384 and 512 tail tokens (mean gradient ratio 8.8:1), confirming that diagnostic information is highly localized in the final trace segment. Cross-seed validation (3 seeds per model) shows tight convergence bands (max standard deviation 0.9 percentage points), and LoRA training stability emerges as the practical bottleneck differentiating model families. These findings establish that verdict-optimized trace design should extract the highest-specificity diagnostic signal and discard everything else.
22	\end{abstract}
23	
24	\section{Introduction}
25	
26	Execution traces provide a detailed record of program runtime behavior, including variable states, control flow paths, and exception events. Recent work has explored using traces to improve code LLM capabilities through supervised fine-tuning (SFT). DCSH \cite{ni2024dcsh} evaluated five trace formats across generative code tasks and concluded that ``no single trace representation consistently outperforms others.'' TracePile \cite{tracepile2025} scaled trace-augmented pretraining to 2.6 million samples but focused exclusively on code generation, not classification. TRACED \cite{traced2024} demonstrated that traces help encoder-based test verdict classification but did not investigate which trace components are responsible. A fundamental question remains unanswered: what minimal diagnostic signal in an execution trace is sufficient for accurate verdict prediction?
27	
28	This question matters for two practical reasons. First, full execution traces are prohibitively long (often thousands of tokens), causing both computational overhead and, as we show, information overload that degrades model performance. Second, deployment at scale requires trace representations that are robust across model families, parameter counts, and training seeds, not just effective on a single architecture.
29	
30	Existing trace formats are designed for execution simulation: they preserve sequential state changes so that a model can mentally re-execute the program. For verdict prediction, however, the task reduces to fault detection, and the relevant information may be far more localized. We hypothesize that the diagnostic moment, specifically the exception event indicating a runtime fault, concentrates the vast majority of verdict-relevant signal, and that the surrounding trace context is largely redundant.
31	
32	We test this hypothesis through a systematic study across four code LLMs from three families (Qwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, CodeLlama-13B-Instruct). Our contributions are:
33	
34	\begin{enumerate}
35	\item \textbf{Exception dominance is universal.} Exception-only SFT achieves the highest verdict accuracy across all four models and three model families (99.8\% on Qwen-7B, 97.2\% mean on CodeLlama-13B with 3-seed validation), consistently outperforming full traces and compressed traces (Section~\ref{sec:exception_dominance}).
36	\item \textbf{Causal decomposition of the trace compression gap.} A label-only loss ablation quantifies that information overload (74\%) dominates gradient dilution (26\%) in explaining why full traces underperform compressed representations (Section~\ref{sec:causal}).
37	\item \textbf{Two-tier diagnostic hierarchy.} Component ablation reveals a strict hierarchy: Tier~1 signals (exceptions, assertion outcomes; each individually $\geq$99.4\%) subsume Tier~2 signals (loop summaries; 85.6\%), and combining tiers introduces noise rather than benefit (Section~\ref{sec:hierarchy}).
38	\item \textbf{Universal sharp phase transition in token budget curves.} Across all four models, verdict accuracy undergoes a sharp transition between 384 and 512 tail tokens (mean $\Delta_{384 \to 512}$ = 17.1 percentage points, gradient ratio 8.8:1), confirming that diagnostic information is concentrated in the final $\sim$400--500 tokens (Section~\ref{sec:phase_transition}).
39	\item \textbf{LoRA training stability as practical bottleneck.} Cross-seed experiments (3 seeds $\times$ 4 models) reveal tight post-transition convergence bands (max std = 0.9pp) but expose LoRA initialization sensitivity as the key factor differentiating model families (Section~\ref{sec:training_stability}).
40	\end{enumerate}
41	
42	\section{Related Work}
43	
44	\paragraph{Trace-augmented code LLMs.}
45	Several recent efforts incorporate execution traces into code LLM training. DCSH \cite{ni2024dcsh} compared five trace representations (step-by-step, compressed, output-only, assertion-level, and variable-focused) on generative code tasks, finding inconsistent results across formats and models. TracePile \cite{tracepile2025} assembled 2.6M trace-augmented samples for continued pretraining and observed modest downstream gains on code generation benchmarks. Both studies focus on generative tasks and do not evaluate verdict prediction. TRACED \cite{traced2024} is closest to our setting: it trains encoder-based classifiers on execution traces for test verdict prediction and demonstrates that traces improve over code-only baselines. However, TRACED treats traces as monolithic inputs without decomposing which components carry diagnostic signal.
46	
47	\paragraph{Verdict prediction and fault localization.}
48	Test verdict prediction (classifying test executions as pass or fail) is a well-studied software engineering task, traditionally addressed with hand-crafted features from coverage matrices or statistical fault localization techniques \cite{wong2016survey}. LLM-based approaches are more recent: CodeT \cite{chen2023codet} uses dual execution to filter generated solutions, and similar execute-then-classify pipelines appear in competitive programming evaluators. These approaches treat the execution oracle as a black box. Our work opens this box and asks what trace information the classifier actually needs.
49	
50	\paragraph{Execution reasoning in LLMs.}
51	CRUXEval \cite{gu2024cruxeval} benchmarks LLMs on predicting execution outputs, revealing substantial variation across model families. This execution reasoning capability is related to but distinct from verdict prediction: output prediction requires simulating full program state, while verdict prediction reduces to detecting whether a fault occurred. Our findings suggest this distinction is practically important, as signals requiring deep execution reasoning (loop summaries, full traces) show model-dependent effectiveness, while structurally simple fault indicators (exceptions) generalize.
52	
53	\section{Method}
54	
55	\subsection{Task Definition}
56	
57	Given an execution trace $t$ produced by running a candidate solution against a test suite, verdict prediction is the binary classification task: $f(t) \to \{$\textsc{pass}, \textsc{fail}$\}$. A \textsc{pass} verdict indicates all assertions succeeded; \textsc{fail} indicates at least one assertion failed or an unhandled exception occurred.
58	
59	\subsection{Dataset}
60	
61	We construct our dataset from HumanEval (164 problems) and MBPP-sanitized (427 problems), totaling 591 programming problems. For each problem, we collect 10 LLM-generated candidate solutions and execute them against the provided test suites using an instrumented Python tracer, yielding 5,910 (solution, trace, verdict) triples. The dataset is split into 4,720 training and 1,190 test samples with no problem-level overlap. The test set class distribution is 71.5\% pass / 28.5\% fail (majority baseline: 71.5\%).
62	
63	\subsection{Trace Representations}
64	
65	Our tracer captures full execution traces including variable assignments, control flow, loop iterations, assertion outcomes, and exception events. We define the following representations, ordered by information specificity:
66	
67	\begin{itemize}
68	\item \textbf{Full trace}: The complete execution trace, averaging thousands of tokens. Contains all runtime information but substantial noise from loop iterations, intermediate variable states, and memory addresses.
69	\item \textbf{VOTA (Verdict-Optimized Trace Abstraction)}: A compressed trace that retains three structured components: (1) loop summaries (iteration counts and patterns), (2) exception events (\texttt{[ERROR] type: message}), and (3) assertion actual/expected value pairs.
70	\item \textbf{Exception-only}: Only the exception component of VOTA. Structurally simple: presence or absence of \texttt{[ERROR]} tags with exception type and message. Typically 50--200 tokens for failing traces, near-empty for passing traces.
71	\item \textbf{Assertion-point only (AE-only)}: Only the assertion outcome component, recording actual versus expected values at each assertion point.
72	\item \textbf{Loop-only}: Only the loop summary component.
73	\item \textbf{No trace}: Code and test inputs only, without any execution information.
74	\end{itemize}
75	
76	\subsection{Tail-Truncation Token Budget Analysis}
77	
78	To investigate the spatial distribution of diagnostic information within traces, we define a \emph{tail-$k$} condition: retain only the final $k$ tokens of the full trace. We evaluate $k \in \{256, 384, 512, 1024, 2048\}$ across all four models, producing a token budget curve that reveals where diagnostic signal concentrates.
79	
80	\subsection{Training Protocol}
81	
82	All models are fine-tuned using LoRA (rank 16, $\alpha$=32) with a learning rate of $2 \times 10^{-4}$ and batch size 4 for 3 epochs. We evaluate at each epoch boundary and report the final epoch result as the primary metric. For cross-seed validation, we use seeds 42, 123, and 456. Training is conducted on single NVIDIA A100-80GB GPUs.
83	
84	\subsection{Evaluation Metrics}
85	
86	We report accuracy, per-class F1, Expected Calibration Error (ECE), and Brier score. Statistical comparisons use McNemar's test for paired binary outcomes and bootstrap confidence intervals (95\%, 10,000 resamples).
87	
88	\section{Experiments and Results}
89	
90	\subsection{Exception Dominance Across Models}
91	\label{sec:exception_dominance}
92	
93	Table~\ref{tab:exception_dominance} presents verdict accuracy for exception-only SFT across all four models. Exception events achieve the highest accuracy in every model tested. On Qwen-7B, all three seeds produce identical results (99.83\%), with the only two errors traced to GeneratorExit false positives from a single HumanEval problem (Section~\ref{sec:error_analysis}). CodeLlama-13B achieves 97.5\% (seed 42), while both Qwen-1.5B (99.83\%) and DeepSeek-6.7B (99.33\%, 2-of-3 seeds) confirm that exception signal effectiveness spans three distinct model families and two parameter scales.
94	
95	\begin{table}[t]
96	\centering
97	\small
98	\begin{tabular}{lccc}
99	\toprule
100	\textbf{Model} & \textbf{Acc.} & \textbf{Pass F1} & \textbf{Fail F1} \\
101	\midrule
102	Qwen-7B & 99.83\% & 0.999 & 0.996 \\
103	Qwen-1.5B & 99.83\% & 0.999 & 0.996 \\
104	DeepSeek-6.7B & 99.33\% & --- & --- \\
105	CodeLlama-13B & 99.83\% & --- & --- \\
106	\midrule
107	\multicolumn{4}{l}{\emph{Comparison conditions (Qwen-7B)}} \\
108	VOTA & 99.41\% & 0.996 & 0.987 \\
109	Full trace & 81.76\% & 0.877 & 0.696 \\
110	No trace & 75.13\% & 0.833 & 0.539 \\
111	\bottomrule
112	\end{tabular}
113	\caption{Exception-only verdict accuracy across four models. Comparison conditions shown for Qwen-7B. Exception-only achieves the highest accuracy in every model, outperforming full VOTA (which includes additional components) and full traces.}
114	\label{tab:exception_dominance}
115	\end{table}
116	
117	The gap between exception-only and full traces is striking: on Qwen-7B, exception-only (99.83\%) outperforms full traces (81.76\%) by 18.1 percentage points, despite containing far fewer tokens. This gap cannot be explained by the exception signal being a simple keyword feature: full traces also contain the same \texttt{[ERROR]} markers, yet achieve only 81.8\% because the diagnostic signal is buried in thousands of irrelevant tokens.
118	
119	\paragraph{Comparison with frontier model prompting.}
120	Table~\ref{tab:fewshot} compares SFT exception-only with few-shot prompting of frontier models. Even the best few-shot configuration (Claude 3-shot, 96.1\%) produces 11.5 times more errors than SFT exception-only on a 1.5B model (46 vs.\ 2 errors). SFT with the right signal and a small model outperforms frontier-model prompting at a fraction of the inference cost.
121	
122	\begin{table}[t]
123	\centering
124	\small
125	\begin{tabular}{lcc}
126	\toprule
127	\textbf{Method} & \textbf{Acc.} & \textbf{Errors} \\
128	\midrule
129	SFT exc-only (Qwen-7B) & 99.83\% & 2 \\
130	SFT exc-only (Qwen-1.5B) & 99.83\% & 2 \\
131	Claude 3-shot & 96.1\% & $\sim$46 \\
132	GPT-4o 3-shot & 95.1\% & $\sim$58 \\
133	Claude 0-shot & 94.2\% & $\sim$69 \\
134	GPT-4o 0-shot & 93.2\% & $\sim$81 \\
135	Qwen-1.5B 0-shot (base) & 93.45\% & 78 \\
136	Qwen-7B 0-shot (base) & 89.08\% & 130 \\
137	\bottomrule
138	\end{tabular}
139	\caption{SFT exception-only vs.\ few-shot prompting. SFT on a 1.5B model with exception signal produces 11.5$\times$ fewer errors than Claude 3-shot prompting, at a fraction of the cost.}
140	\label{tab:fewshot}
141	\end{table}
142	
143	\subsection{Causal Decomposition of the Compression Gap}
144	\label{sec:causal}
145	
146	Full traces achieve 81.76\% while VOTA achieves 99.41\%, a 17.6 percentage point gap. Two mechanisms could explain this: (1) gradient dilution, where non-verdict tokens in full traces dilute the training signal, and (2) information overload, where irrelevant tokens overwhelm the model's attention. To disentangle these, we train a label-only loss variant that computes loss exclusively on the verdict token while keeping the full trace as input, eliminating gradient dilution by construction.
147	
148	Label-only full-trace training achieves 86.22\%, a 4.5pp improvement over standard full-trace (81.76\%) but still 13.2pp below VOTA (99.41\%). This quantifies the causal decomposition: gradient dilution accounts for $\frac{4.5}{17.6} \approx 26\%$ of the gap, while information overload accounts for $\frac{13.0}{17.6} \approx 74\%$. Even with oracle loss masking that perfectly eliminates gradient dilution, full traces still substantially underperform compressed representations.
149	
150	This result has practical implications: simply changing the loss function cannot close the gap. The primary bottleneck is that irrelevant trace tokens overwhelm the model's capacity to attend to diagnostic signals, and only trace-level information filtering (compression or extraction) can address this.
151	
152	\subsection{Two-Tier Diagnostic Hierarchy}
153	\label{sec:hierarchy}
154	
155	Component ablation on Qwen-7B reveals a strict two-tier structure in verdict-relevant trace information (Table~\ref{tab:hierarchy}).
156	
157	\begin{table}[t]
158	\centering
159	\small
160	\begin{tabular}{lccc}
161	\toprule
162	\textbf{Component} & \textbf{Acc.} & \textbf{ECE} & \textbf{Tier} \\
163	\midrule
164	AE-only & 99.92\% & 0.0004 & 1 \\
165	Exception-only & 99.83\% & 0.0027 & 1 \\
166	VOTA (all) & 99.41\% & 0.0054 & 1+2 \\
167	VOTA no-AE & 99.41\% & --- & 1+2 \\
168	Loop-only & 85.63\% & 0.0831 & 2 \\
169	Label-only loss & 86.22\% & 0.1107 & --- \\
170	Full trace & 81.76\% & 0.0958 & --- \\
171	No trace & 75.13\% & 0.1715 & --- \\
172	\bottomrule
173	\end{tabular}
174	\caption{Two-tier diagnostic hierarchy (Qwen-7B). Tier~1 signals (exceptions, assertion outcomes) are each individually near-perfect and sufficient. Tier~2 (loop summaries) carries moderate signal but is fully subsumed. Combining tiers introduces noise: exception-only (99.83\%) $>$ VOTA (99.41\%), $p$=0.01.}
175	\label{tab:hierarchy}
176	\end{table}
177	
178	\textbf{Tier 1} consists of exception events (99.83\%) and assertion-point information (99.92\%). These two components are statistically equivalent ($p$=0.80) and each individually sufficient for near-perfect verdict prediction. They encode direct fault indicators: whether an exception was raised, and whether assertions matched expected values.
179	
180	\textbf{Tier 2} consists of loop summaries (85.63\%), which carry substantial signal (10.5pp above the no-trace baseline) but are entirely subsumed by either Tier~1 component. Loop-only accuracy closely matches label-only full-trace (86.22\%), confirming that VOTA's loop compression extracts precisely the useful behavioral signal from full traces without additional information.
181	
182	Combining Tier~1 and Tier~2 signals (full VOTA at 99.41\%) slightly degrades performance relative to exception-only (99.83\%, $p$=0.01), suggesting that non-diagnostic tokens from loop summaries dilute attention on the fault indicator signal.
183	
184	Calibration data reinforce this hierarchy. Exception-only ECE (0.0027) is 63 times lower than no-trace ECE (0.1715), and exception-only Brier score (0.0013) is 150 times lower than no-trace (0.1972). The diagnostic signal not only improves accuracy but fundamentally improves model calibration: the model ``knows that it knows.''
185	
186	\subsection{Cross-Model Calibration}
187	
188	Table~\ref{tab:calibration} extends calibration analysis across all four models on exception-only traces. All models achieve ECE below 0.01, with the best calibration on CodeLlama-13B (ECE=0.0024). The ECE improvement over no-trace ranges from 21$\times$ (DeepSeek) to 71$\times$ (CodeLlama), confirming that calibration benefit is model-agnostic.
189	
190	\begin{table}[t]
191	\centering
192	\small
193	\begin{tabular}{lccc}
194	\toprule
195	\textbf{Model} & \textbf{ECE} & \textbf{Brier} & \textbf{ECE/no-trace} \\
196	\midrule
197	Qwen-7B & 0.0027 & 0.0013 & 63$\times$ \\
198	Qwen-1.5B & 0.0031 & 0.0015 & 55$\times$ \\
199	DeepSeek-6.7B & 0.0082 & 0.0055 & 21$\times$ \\
200	CodeLlama-13B & 0.0024 & 0.0011 & 71$\times$ \\
201	\bottomrule
202	\end{tabular}
203	\caption{Exception-only calibration across four models. All models achieve ECE $<$ 0.01. Improvement over the no-trace baseline (ECE=0.1715) ranges from 21$\times$ to 71$\times$.}
204	\label{tab:calibration}
205	\end{table}
206	
207	DeepSeek's slightly higher ECE (0.0082) reflects residual LoRA seed sensitivity (Section~\ref{sec:training_stability}), but remains excellent in absolute terms. The universally low calibration error confirms that exception-based verdict prediction produces well-calibrated confidence estimates across model families.
208	
209	\subsection{Universal Phase Transition in Token Budget Curves}
210	\label{sec:phase_transition}
211	
212	To understand why exception events work, we examine how verdict accuracy varies with the number of tail tokens retained from full traces. If diagnostic information is spatially concentrated, we expect a sharp transition at the token budget where exception events first enter the retained window.
213	
214	Table~\ref{tab:budget} presents the complete budget curve across all four models at five token budgets. The results reveal a universal, sharp phase transition between 384 and 512 tail tokens.
215	
216	\begin{table}[t]
217	\centering
218	\small
219	\begin{tabular}{lccccc}
220	\toprule
221	\textbf{Model} & \textbf{256} & \textbf{384} & \textbf{512} & \textbf{1024} & \textbf{2048} \\
222	\midrule
223	Qwen-7B & 77.5 & 79.5 & 93.6 & 96.5 & 97.3 \\
224	Qwen-1.5B & 72.6 & 74.8 & 95.6 & 96.6 & 97.9 \\
225	DS-6.7B & 76.4 & 78.1 & 93.9 & 96.5 & 95.0 \\
226	CL-13B & 77.9 & 79.8 & 97.5 & 98.2 & 96.5 \\
227	\midrule
228	Mean & 76.1 & 78.1 & 95.2 & 96.9 & 96.7 \\
229	\bottomrule
230	\end{tabular}
231	\caption{Verdict accuracy (\%) by tail-token budget across four models. A sharp phase transition occurs between 384 and 512 tokens universally. DS = DeepSeek, CL = CodeLlama.}
232	\label{tab:budget}
233	\end{table}
234	
235	Three key patterns emerge. First, the \textbf{pre-transition plateau} (256--384 tokens): accuracy remains flat, with the 256-to-384 increment averaging only 1.95pp across models. All four McNemar tests comparing tail-384 to tail-256 yield $p > 0.1$, confirming statistical equivalence. The diagnostic signal has not yet entered the observation window.
236	
237	Second, the \textbf{sharp cliff} (384--512 tokens): accuracy jumps by a mean of 17.1pp (range: 14.1--20.8pp). The gradient ratio (512-increment / 384-increment) averages 8.8:1 across models. This is consistent with a phase transition at approximately 400--450 tail tokens, where exception tracebacks (typically 150--400 tokens) first become fully visible.
238	
239	Third, the \textbf{ceiling plateau} (512--2048 tokens): accuracy stabilizes, with the 1024-to-2048 increment averaging less than 1pp. Additional tail tokens beyond 512 provide diminishing returns, confirming that the diagnostic signal is concentrated in the final segment. DeepSeek and CodeLlama show slight accuracy decreases at 2048 tokens ($-$1.5pp and $-$1.7pp respectively), possibly reflecting attention dilution at longer sequences.
240	
241	\paragraph{Interpreting the phase transition.}
242	The phase transition location is consistent with the physical structure of Python exception tracebacks. An exception event typically comprises an error type, message, and the final few stack frames, occupying 150--400 tokens. At 384 tail tokens, most exception tracebacks are partially truncated; at 512 tokens, nearly all are fully captured. The transition is sharp because exception information has a binary character: a partially truncated exception traceback provides little diagnostic value, while a complete one provides nearly all the information needed.
243	
244	This provides the mechanistic explanation for why exception-only SFT works: exception events are informationally equivalent to the final 400--500 tokens of a trace. The phase transition confirms that diagnostic information is not distributed throughout the trace but concentrated in a localized ``diagnostic moment.''
245	
246	\subsection{Cross-Seed Convergence and Training Stability}
247	\label{sec:training_stability}
248	
249	We validate the phase transition finding with 3-seed cross-validation at the post-transition point (tail-512) across all four models.
250	
251	\begin{table}[t]
252	\centering
253	\small
254	\begin{tabular}{lcccc}
255	\toprule
256	\textbf{Model} & \textbf{Mean} & \textbf{Std} & \textbf{Range} \\
257	\midrule
258	Qwen-7B (7B) & 93.5\% & 0.6pp & [92.9, 94.1] \\
259	Qwen-1.5B (1.5B) & 95.5\% & 0.4pp & [95.1, 95.8] \\
260	DeepSeek (6.7B) & 93.5\% & 0.9pp & [92.5, 94.2] \\
261	CodeLlama (13B) & 97.2\% & 0.3pp & [96.9, 97.5] \\
262	\bottomrule
263	\end{tabular}
264	\caption{Cross-seed tail-512 convergence (3 seeds per model). All standard deviations are below 1pp. The worst seed for any model (92.5\%) far exceeds the best tail-384 result (79.8\%).}
265	\label{tab:cross_seed}
266	\end{table}
267	
268	All four models show tight convergence bands with standard deviations below 1pp (Table~\ref{tab:cross_seed}). The worst individual seed across all models (DeepSeek seed 123, 92.5\%) still exceeds the best tail-384 result by 12.7pp, confirming that the phase transition location is seed-robust: there is no seed under which the transition shifts beyond 512 tokens.
269	
270	Two additional observations are noteworthy. First, Qwen-1.5B achieves a higher post-transition mean (95.5\%) than the larger Qwen-7B (93.5\%). This apparent reversal is consistent with the exception-only results: once diagnostic signal is sufficient, the smaller model's higher LoRA parameter-to-total-parameter ratio provides more efficient adaptation. Performance in the pre-transition regime, where signal is insufficient, is model-size-dependent (Qwen-1.5B at 74.8\% is the worst), but post-transition performance is signal-limited rather than capacity-limited.
271	
272	Second, DeepSeek shows the highest variance (0.9pp), consistent with its LoRA initialization sensitivity observed in exception-only experiments. CodeLlama shows the lowest variance (0.3pp) and highest absolute accuracy (97.2\%), suggesting that larger models exhibit smoother LoRA loss landscapes.
273	
274	\subsection{Training Dynamics}
275	
276	Step-level learning curves provide complementary evidence for the information density hypothesis. Table~\ref{tab:dynamics} compares convergence milestones for exception-only and full-trace training on Qwen-7B.
277	
278	\begin{table}[t]
279	\centering
280	\small
281	\begin{tabular}{lcc}
282	\toprule
283	\textbf{Milestone} & \textbf{Exception-only} & \textbf{Full trace} \\
284	\midrule
285	80\% accuracy & $\sim$30 steps (4 min) & $\sim$250 steps (35 min) \\
286	90\% accuracy & $\sim$60 steps (8 min) & never \\
287	95\% accuracy & $\sim$80 steps (11 min) & never \\
288	99\% accuracy & $\sim$150 steps (21 min) & never \\
289	Final & 99.83\% @ $\sim$200 steps & 81.76\% @ $\sim$900 steps \\
290	\bottomrule
291	\end{tabular}
292	\caption{Convergence milestones for exception-only vs.\ full-trace SFT (Qwen-7B). Exception-only surpasses the full-trace ceiling in under 50 steps and converges 4.2$\times$ faster to the full-trace final accuracy.}
293	\label{tab:dynamics}
294	\end{table}
295	
296	Exception-only training crosses the full-trace ceiling (81.76\%) in approximately 45 steps, roughly 6 minutes of single-GPU training. By step 200, it reaches 99.83\%, while full-trace training plateaus at 81.76\% after 900 steps (3 full epochs). The convergence speed ratio is 4.2$\times$ when measured at the full-trace ceiling. This reflects the near-binary nature of the exception signal: the model needs only to learn the mapping from \texttt{[ERROR]} presence to \textsc{fail}, which requires few gradient updates. Full-trace training faces a two-stage learning problem: first learning to ignore irrelevant tokens, then extracting fault signal from the remainder.
297	
298	\subsection{Failure Mode Analysis}
299	\label{sec:error_analysis}
300	
301	We systematically analyze prediction errors across conditions on Qwen-7B to characterize the diagnostic hierarchy qualitatively (Table~\ref{tab:errors}).
302	
303	\begin{table}[t]
304	\centering
305	\small
306	\begin{tabular}{lccc}
307	\toprule
308	\textbf{Condition} & \textbf{Errors} & \textbf{Dominant mode} & \textbf{Interp.} \\
309	\midrule
310	Exception-only & 2 & GeneratorExit FP & 100\% \\
311	VOTA & 7 & Loop noise + edge AE & $\sim$60\% \\
312	Full trace & $\sim$217 & Information overload & $<$20\% \\
313	No trace & $\sim$296 & Majority-class bias & 100\% \\
314	\bottomrule
315	\end{tabular}
316	\caption{Error mode analysis by condition (Qwen-7B). Error interpretability correlates with tier level: Tier~1 errors are deterministic and representation-inherent; lower-tier errors are diffuse and stochastic. FP = false positive. Interp.\ = fraction of errors with identifiable root cause.}
317	\label{tab:errors}
318	\end{table}
319	
320	Exception-only's two errors are fully deterministic: both come from HumanEval/95 (\texttt{check\_dict\_case}), where Python's \texttt{all()} short-circuits a generator expression, triggering \texttt{GeneratorExit} (a \texttt{BaseException} subclass used for control flow, not a real error). The tracer marks this as \texttt{[ERROR]}, and the model reasonably but incorrectly predicts \textsc{fail}. All three seeds produce identical errors, confirming this is a representation-inherent limitation, not training stochasticity. The error is actionable: distinguishing \texttt{BaseException} subclasses from \texttt{Exception} subclasses in the tracer would eliminate it.
321	
322	Error interpretability decreases monotonically down the hierarchy. VOTA's 7 errors include the 2 GeneratorExit cases plus 5 from loop noise confusion. Full trace's approximately 217 errors are scattered across problem types with no dominant pattern, characteristic of information overload. No-trace's approximately 296 errors follow a single systematic pattern: majority-class bias (under-predicting \textsc{fail}).
323	
324	The error containment hierarchy ($\text{exception}(2) \subset \text{VOTA}(7) \subset \text{full\_trace}(217)$) provides a third evidence dimension (alongside accuracy and calibration) for the two-tier diagnostic hierarchy: the highest-specificity signal produces not only the fewest errors but the most interpretable and most actionable ones.
325	
326	\subsection{Out-of-Domain Generalization}
327	
328	To assess whether the exception signal generalizes beyond Python, we evaluate the Qwen-7B exception-only model on Java and JavaScript traces formatted with the same \texttt{[ERROR]} structure (Table~\ref{tab:ood}).
329	
330	\begin{table}[t]
331	\centering
332	\small
333	\begin{tabular}{lcc}
334	\toprule
335	\textbf{Language} & \textbf{Accuracy} & \textbf{$n$} \\
336	\midrule
337	Python (in-domain) & 99.83\% & 1190 \\
338	Java (OOD) & 97.2\% & $\sim$500 \\
339	JavaScript (OOD) & 96.3\% & $\sim$500 \\
340	\bottomrule
341	\end{tabular}
342	\caption{Cross-language generalization of exception-only SFT (Qwen-7B). OOD accuracy remains above 96\%, with only a 3.1pp mean gap versus in-domain, suggesting the model learns language-agnostic fault detection rather than Python-specific patterns.}
343	\label{tab:ood}
344	\end{table}
345	
346	OOD accuracy averages 96.8\%, only 3.1pp below in-domain performance and 21.6pp above the Python no-trace baseline (75.1\%). The modest degradation likely reflects novel exception types (Java's \texttt{NullPointerException}, JavaScript's \texttt{TypeError}) absent from the Python training set, rather than a failure of the general fault detection mechanism.
347	
348	\section{Discussion}
349	
350	\paragraph{VOTA as fault indicator isolation.}
351	Our results reposition VOTA from a generic trace compression method to a fault indicator isolation mechanism. VOTA's value lies not in making traces shorter, but in separating high-specificity fault indicators (exception events) from low-specificity behavioral patterns (loop summaries). The evidence is clear: exception-only ($\geq$ VOTA) and removing assertion-point data from VOTA does not degrade performance (99.41\% in both cases). VOTA's practical contribution is automatically extracting the diagnostic moment from noisy traces.
352	
353	\paragraph{Signal-limited, not capacity-limited.}
354	A recurring pattern across experiments is that post-transition performance depends on signal availability, not model capacity. Qwen-1.5B outperforms Qwen-7B at tail-512 (95.5\% vs.\ 93.5\%), while the reverse holds pre-transition (74.8\% vs.\ 79.5\%). Once the diagnostic signal enters the observation window, even small models achieve strong performance. This suggests that verdict-optimized trace design matters more than scaling model parameters for this task.
355	
356	\paragraph{Training stability as practical bottleneck.}
357	DeepSeek exception-only shows seed-dependent performance (91--99\% across seeds) compared to Qwen's perfect stability (99.83\% $\pm$ 0.00). Notably, DeepSeek seeds with near-identical training loss (0.1225 vs.\ 0.122) produce accuracy gaps of 8.2pp, concentrated entirely in fail-class recall (1.0 vs.\ 0.705). Token-level loss masks sample-level classification ability, a general phenomenon in class-imbalanced settings. For deployment, we recommend multi-seed validation and task-specific (not loss-based) checkpoint selection.
358	
359	\paragraph{Addressing the ``feature engineering'' concern.}
360	One might argue that exception extraction is merely feature engineering rather than a scientific contribution. The universality of our findings argues against this characterization: if exception dominance were an artifact of a particular model or dataset, we would not observe identical S-curve phase transitions across three model families at two parameter scales. The sharp phase transition at 384--512 tokens, with gradient ratios of 7--10:1 and consistent location across all four models, reflects a structural property of how diagnostic information distributes in execution traces, not an engineering trick.
361	
362	\paragraph{Limitations.}
363	Our study evaluates a single task type (verdict prediction) on a single data source (HumanEval + MBPP). While our cross-model validation provides generalization evidence across architectures, evaluation on additional datasets and task types (e.g., fault localization, repair) is needed to assess broader applicability. The VOTA cross-model comparison is confounded by training-time trace truncation on DeepSeek (91.7\% of samples truncated), which inflates the apparent model-capability gap. OOD language generalization results are preliminary and require dedicated cross-language benchmarks for definitive claims.
364	
365	\section{Conclusion}
366	
367	We present the first systematic study of which execution trace components drive verdict prediction. Across four code LLMs from three model families, exception events, structurally simple fault indicators, consistently achieve the highest accuracy, best calibration, and most interpretable failure modes. A causal decomposition reveals that information overload (74\%) dominates gradient dilution (26\%) in explaining why full traces underperform, and component ablation uncovers a strict two-tier diagnostic hierarchy. Token budget analysis reveals a universal sharp phase transition confirming that diagnostic information is concentrated in a localized moment occupying roughly 400--500 tokens at the trace tail. For verdict-oriented trace design, we recommend extracting the highest-specificity diagnostic signal and discarding everything else.
368	
369	\begin{thebibliography}{6}
370	
371	\bibitem{ni2024dcsh}
372	A.~Ni, M.~Allamanis, A.~Cohan, Y.~Deng, K.~Shi, C.~Sutton, and P.~Yin.
373	DCSH: Diverse code solution hints for programming tasks.
374	In \emph{Findings of EMNLP}, 2024.
375	
376	\bibitem{tracepile2025}
377	S.~Jiang, Z.~Zheng, B.~Zheng, et~al.
378	TracePile: A large-scale trace-augmented dataset for code language models.
379	In \emph{NeurIPS}, 2025.
380	
381	\bibitem{traced2024}
382	J.~Wang, G.~Chen, and H.~Mei.
383	TRACED: Execution-aware pre-training for source code.
384	In \emph{ICSE}, 2024.
385	
386	\bibitem{wong2016survey}
387	W.~E. Wong, R.~Gao, Y.~Li, R.~Abreu, and F.~Wotawa.
388	A survey on software fault localization.
389	\emph{IEEE Trans. Software Eng.}, 42(8):707--740, 2016.
390	
391	\bibitem{chen2023codet}
392	B.~Chen, F.~Zhang, A.~Nguyen, D.~Zan, Z.~Lin, J.-G.~Lou, and W.~Chen.
393	CodeT: Code generation with generated tests.
394	In \emph{ICLR}, 2023.
395	
396	\bibitem{gu2024cruxeval}
397	A.~Gu, B.~Rozi\`{e}re, H.~Leather, A.~Solar-Lezama, G.~Synnaeve, and S.~I.~Wang.
398	CRUXEval: A benchmark for code reasoning, understanding and execution.
399	In \emph{ICML}, 2024.
400	
401	\end{thebibliography}
402	
403	\end{document}
404	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4d05c70-5ece-4367-92bf-63b7f98f9a54",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "050ff32e-ba53-4f7b-a3e8-caf670c0a67a",
  "sourceToolAssistantUUID": "a4d05c70-5ece-4367-92bf-63b7f98f9a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T12:24:18.608Z_

<details open><summary>🔧 Tool call — Read · `toolu_011brz42B5Qpfo7sBBPTNEQ7`</summary>

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
  "parentUuid": "050ff32e-ba53-4f7b-a3e8-caf670c0a67a",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2dAoW3Q6oECw3FW6uJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99619111-5f10-42c6-849a-9d2320569d80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZdV5AD1pu8jgi4Qe8YR61",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3476,
      "cache_read_input_tokens": 18162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3476,
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

_source line 17 · 2026-05-18T12:24:18.615Z_

<details><summary>↩ Tool result · `toolu_011brz42B5Qpfo7sBBPTNEQ7`</summary>

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
  "parentUuid": "99619111-5f10-42c6-849a-9d2320569d80",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "513fb1f7-bab0-4ae2-8f8f-b4e90216f613",
  "sourceToolAssistantUUID": "99619111-5f10-42c6-849a-9d2320569d80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T12:24:19.189Z_

<details open><summary>🔧 Tool call — Read · `toolu_016hZpXeWryNtmsXpytbDrQR`</summary>

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
  "parentUuid": "513fb1f7-bab0-4ae2-8f8f-b4e90216f613",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2dAoW3Q6oECw3FW6uJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb93457a-2848-4eb4-8475-83aa6632f092",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZdV5AD1pu8jgi4Qe8YR61",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3476,
      "cache_read_input_tokens": 18162,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3476
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 18162,
          "cache_creation_input_tokens": 3476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3476,
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

_source line 19 · 2026-05-18T12:24:19.194Z_

<details><summary>↩ Tool result · `toolu_016hZpXeWryNtmsXpytbDrQR`</summary>

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
  "parentUuid": "fb93457a-2848-4eb4-8475-83aa6632f092",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "1abef664-f83d-471c-9ea0-6d4ba37bf3dd",
  "sourceToolAssistantUUID": "fb93457a-2848-4eb4-8475-83aa6632f092",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-18T12:24:25.772Z_

Now let me read the rest of the experiments, appendix, introduction, method, and discussion sections, plus the review context and paper provenance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1abef664-f83d-471c-9ea0-6d4ba37bf3dd",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2ddJhMCHm41a7jhc2o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d44d0a85-0104-4c4f-9568-312e88f4d75a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016D6fNVHmYEPDQNWN444cHb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18519,
      "cache_read_input_tokens": 21638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18519,
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

_source line 21 · 2026-05-18T12:24:27.173Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FXUaaNcGBcR8bKN4k5et7x`</summary>

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
  "parentUuid": "d44d0a85-0104-4c4f-9568-312e88f4d75a",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2ddJhMCHm41a7jhc2o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a0ccc20-b664-413e-9ec2-3182da397a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016D6fNVHmYEPDQNWN444cHb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18519,
      "cache_read_input_tokens": 21638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18519,
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

_source line 22 · 2026-05-18T12:24:27.186Z_

<details><summary>↩ Tool result · `toolu_01FXUaaNcGBcR8bKN4k5et7x`</summary>

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
  "parentUuid": "9a0ccc20-b664-413e-9ec2-3182da397a12",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "cd8b35bc-5232-4cc1-a716-20470bb3418e",
  "sourceToolAssistantUUID": "9a0ccc20-b664-413e-9ec2-3182da397a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T12:24:27.698Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RkuWnz9qaxXeLT93LUCQ1y`</summary>

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
  "parentUuid": "cd8b35bc-5232-4cc1-a716-20470bb3418e",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2ddJhMCHm41a7jhc2o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "361e710d-ed1f-46f4-b5f0-ab3af6d4e1e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016D6fNVHmYEPDQNWN444cHb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18519,
      "cache_read_input_tokens": 21638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18519,
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

_source line 24 · 2026-05-18T12:24:27.709Z_

<details><summary>↩ Tool result · `toolu_01RkuWnz9qaxXeLT93LUCQ1y`</summary>

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
  "parentUuid": "361e710d-ed1f-46f4-b5f0-ab3af6d4e1e3",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "99dc4510-6963-461c-b822-ff831bec5284",
  "sourceToolAssistantUUID": "361e710d-ed1f-46f4-b5f0-ab3af6d4e1e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T12:24:28.592Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TbtyKoVDrXZhqPbamqNEh5`</summary>

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
  "parentUuid": "99dc4510-6963-461c-b822-ff831bec5284",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2ddJhMCHm41a7jhc2o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cdf0408-e75c-40b9-8b09-4db43b47dc97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016D6fNVHmYEPDQNWN444cHb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18519,
      "cache_read_input_tokens": 21638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18519,
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

_source line 26 · 2026-05-18T12:24:28.598Z_

<details><summary>↩ Tool result · `toolu_01TbtyKoVDrXZhqPbamqNEh5`</summary>

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
  "parentUuid": "7cdf0408-e75c-40b9-8b09-4db43b47dc97",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "63003604-73ff-4d10-a0c4-60948075a23d",
  "sourceToolAssistantUUID": "7cdf0408-e75c-40b9-8b09-4db43b47dc97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T12:24:28.823Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PaPEBbWCFnL4CmeKF1ySkV`</summary>

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
  "parentUuid": "63003604-73ff-4d10-a0c4-60948075a23d",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2ddJhMCHm41a7jhc2o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8bcb2ef-6770-49f3-9c0c-35cb02f7eede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016D6fNVHmYEPDQNWN444cHb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18519,
      "cache_read_input_tokens": 21638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18519,
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

_source line 28 · 2026-05-18T12:24:29.171Z_

<details><summary>↩ Tool result · `toolu_01PaPEBbWCFnL4CmeKF1ySkV`</summary>

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
  "parentUuid": "f8bcb2ef-6770-49f3-9c0c-35cb02f7eede",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "d5172189-a1a5-4ff4-b0e5-ad7ff4907726",
  "sourceToolAssistantUUID": "f8bcb2ef-6770-49f3-9c0c-35cb02f7eede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-18T12:24:34.324Z_

Now let me read the remaining sections and the review context for the latest dream report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5172189-a1a5-4ff4-b0e5-ad7ff4907726",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2eMman6rKgp4R1Pm2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55c51235-6c3b-4e77-ae4e-fa5504d828e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbakmhbmznEJSi3XACTkZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22062,
      "cache_read_input_tokens": 40157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22062,
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

_source line 30 · 2026-05-18T12:24:36.279Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D3iTKc5LubghknPnnuD275`</summary>

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
  "parentUuid": "55c51235-6c3b-4e77-ae4e-fa5504d828e7",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2eMman6rKgp4R1Pm2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca9576c8-8b5b-4657-a58e-8b49b06d8228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbakmhbmznEJSi3XACTkZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22062,
      "cache_read_input_tokens": 40157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22062,
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

_source line 31 · 2026-05-18T12:24:36.284Z_

<details><summary>↩ Tool result · `toolu_01D3iTKc5LubghknPnnuD275`</summary>

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
  "parentUuid": "ca9576c8-8b5b-4657-a58e-8b49b06d8228",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "62b99913-87ee-4937-b47f-2a9991883007",
  "sourceToolAssistantUUID": "ca9576c8-8b5b-4657-a58e-8b49b06d8228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T12:24:36.752Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K3N5HgZ5j9yvxFXkMWPJQm`</summary>

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
  "parentUuid": "62b99913-87ee-4937-b47f-2a9991883007",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2eMman6rKgp4R1Pm2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab000417-e725-4b87-9a32-7aa8115d4ee8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbakmhbmznEJSi3XACTkZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22062,
      "cache_read_input_tokens": 40157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22062,
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

_source line 33 · 2026-05-18T12:24:36.757Z_

<details><summary>↩ Tool result · `toolu_01K3N5HgZ5j9yvxFXkMWPJQm`</summary>

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
  "parentUuid": "ab000417-e725-4b87-9a32-7aa8115d4ee8",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "415509ec-5561-4120-8fa5-9865c60d32df",
  "sourceToolAssistantUUID": "ab000417-e725-4b87-9a32-7aa8115d4ee8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T12:24:37.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_016zNjWK1GuVPr6cUW2AkraE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "415509ec-5561-4120-8fa5-9865c60d32df",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2eMman6rKgp4R1Pm2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7580a4a-cfd7-4b74-ae1b-367d0032bfad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbakmhbmznEJSi3XACTkZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22062,
      "cache_read_input_tokens": 40157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22062,
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

_source line 35 · 2026-05-18T12:24:38.080Z_

<details><summary>↩ Tool result · `toolu_016zNjWK1GuVPr6cUW2AkraE`</summary>

```text
1	narrative_guidance: 'P1 实验全面确认 budget curve universal phase transition。tail-384 ×
2	  4 模型均 ≤81%（与 tail-256 统计等价, McNemar p>0.1），
3	
4	  phase transition 在 384-512 之间是 sharp cliff（gradient ratio 8-10:1）。cross-seed tail-512
5	  全 4 模型 std ≤ 0.9pp，
6	
7	  convergence band 紧密。CodeLlama tail-2048 正常完成（~96.5%），4 模型 budget curve 完整。
8	
9	  论文 5 contributions 清晰闭环: (1) exception dominance universal across 4 models/3 families/2
10	  scales,
11	
12	  (2) 26%/74% causal decomposition, (3) two-tier diagnostic hierarchy,
13	
14	  (4) universal sharp phase transition at ~400 tokens confirming diagnostic signal
15	  locality,
16	
17	  (5) LoRA training stability as practical bottleneck。
18	
19	  Budget curve 作为核心 Figure 展示 ''why exception works''——exception 等价于 trace 末尾 ~400-500
20	  token 的 diagnostic moment，
21	
22	  phase transition 证明这个 moment 的信息高度局部化。''Feature engineering'' 批评被 4-model universality
23	  + phase transition structure 有效反驳：
24	
25	  若只是 feature engineering，不会在 3 个 model family × 2 个 scale 上产生完全一致的 S-curve phase
26	  transition pattern。
27	
28	  EMNLP main 强竞争力（accept prob 0.55-0.75）。
29	
30	  '
31	imagined_experiments:
32	- name: tail-384 × Qwen-7B
33	  plan_id: plan_016
34	  description: Qwen-2.5-Coder-7B full_trace tail-384 tokens SFT，精确定位 256→512 phase
35	    transition 左边界
36	  expected_results:
37	    accuracy: 0.795
38	    accuracy_ci_lower: 0.772
39	    accuracy_ci_upper: 0.818
40	    majority_baseline: 0.7151
41	    lift_over_majority_pp: 8.0
42	    pass_f1: 0.849
43	    fail_f1: 0.682
44	    diff_vs_tail256_pp: 2.0
45	    mcnemar_vs_tail256_p: 0.15
46	    diff_vs_tail512_pp: -14.1
47	  result_rationale: 'Qwen-7B tail-256 = 77.48%。384 tokens 仅多 128 tokens（约 6-8 行代码）。trace
48	    末尾的 diagnostic 信号分布呈高度右偏：
49	
50	    exception trace 的核心内容（[ERROR] type + message + traceback 最后几帧）集中在 trace 的最后 400-500
51	    tokens。
52	
53	    在 384 token 窗口下，仅有少数 "短 exception"（如单行 AssertionError）的样本能被完整捕获，
54	
55	    大多数样本的 exception 信息仍被截断或完全缺失。因此 accuracy 仅小幅提升 ~2pp。
56	
57	    McNemar p>0.1 说明提升在统计上不显著——384 和 256 处于同一个 "insufficient signal" regime。
58	
59	    这与 information density 假说一致：trace 末尾的 marginal information 在 384 之前主要是 loop 尾部和
60	    assertion 结构的碎片，
61	
62	    尚未到达 exception 信号的密集区，因此 accuracy 曲线保持 flat。
63	
64	    '
65	  tables:
66	  - name: Qwen-7B tail budget curve (complete)
67	    rows:
68	    - tokens: 256
69	      accuracy: 77.5%
70	      regime: pre-transition plateau
71	    - tokens: 384
72	      accuracy: 79.5% (pred)
73	      regime: pre-transition plateau
74	    - tokens: 512
75	      accuracy: 93.6%
76	      regime: post-transition rise
77	    - tokens: 1024
78	      accuracy: 96.5%
79	      regime: ceiling plateau
80	    - tokens: 2048
81	      accuracy: 97.3%
82	      regime: ceiling plateau
83	  figures_description:
84	  - 'Budget curve: x=token budget (log scale), y=accuracy。256-384 flat (~78%), 384→512
85	    sharp cliff (+14pp), 512→2048 diminishing returns。'
86	  analysis: '256→384 Δ=2.0pp vs 384→512 Δ=14.1pp，gradient ratio ~7:1。
87	
88	    384 是 "sharp cliff 的左脚"——phase transition 的数学定义要求存在一个 token budget t*
89	
90	    使得 accuracy(t*-ε) ≈ accuracy(t*-2ε) 但 accuracy(t*+ε) >> accuracy(t*)。
91	
92	    384 的数据精确刻画了这个 t* ≈ 400-450 的位置。
93	
94	    '
95	- name: tail-384 × Qwen-1.5B
96	  plan_id: plan_016
97	  description: Qwen-2.5-Coder-1.5B full_trace tail-384 tokens SFT
98	  expected_results:
99	    accuracy: 0.748
100	    accuracy_ci_lower: 0.722
101	    accuracy_ci_upper: 0.773
102	    majority_baseline: 0.7151
103	    lift_over_majority_pp: 3.3
104	    diff_vs_tail256_pp: 2.2
105	    mcnemar_vs_tail256_p: 0.12
106	    diff_vs_tail512_pp: -20.8
107	  result_rationale: 'Qwen-1.5B tail-256 = 72.6%，甚至低于 majority baseline（71.5%），lift
108	    CI 跨 0。
109	
110	    更小模型在 insufficient signal 条件下表现更差——1.5B 的 attention capacity 有限，
111	
112	    在信号被 noise 淹没时无法有效 extract 任何 useful pattern。384 tokens 同样 signal-insufficient，
113	
114	    accuracy 仅提升到 ~74.8%。然而 1.5B 在 tail-512 时跳到 95.6%（高于 7B 的 93.6%！），
115	
116	    说明一旦 exception signal 充足，1.5B 因 LoRA 参数占比更高而更 efficient。
117	
118	    这是 "signal-limited not capacity-limited" 论点的最强佐证：pre-transition 区间模型越大越好（noise
119	    tolerance），
120	
121	    post-transition 区间模型大小几乎无关（signal dominates）。
122	
123	    '
124	  tables: []
125	  figures_description: []
126	  analysis: '1.5B 的 pre-transition→post-transition jump 是 4 模型中最大的（72.6%→95.6% = 23.0pp），
127	
128	    因为它在 pre-transition 区间最差（最小模型最不耐 noise），但在 post-transition 区间并不落后。
129	
130	    这放大了 phase transition 的 visual contrast，使 S-curve 最为陡峭。
131	
132	    '
133	- name: tail-384 × DeepSeek-6.7B
134	  plan_id: plan_016
135	  description: DeepSeek-Coder-6.7B full_trace tail-384 tokens SFT
136	  expected_results:
137	    accuracy: 0.781
138	    accuracy_ci_lower: 0.757
139	    accuracy_ci_upper: 0.805
140	    majority_baseline: 0.7151
141	    lift_over_majority_pp: 6.6
142	    diff_vs_tail256_pp: 1.7
143	    mcnemar_vs_tail256_p: 0.18
144	    diff_vs_tail512_pp: -15.8
145	  result_rationale: 'DeepSeek tail-256 = 76.39%。DeepSeek tokenizer 效率与 Qwen 不同（DeepSeek
146	    使用 32K vocab 的 BPE），
147	
148	    同一段 Python trace 在 DeepSeek tokenizer 下可能需要更多 tokens。384 tokens 对应的实际文本覆盖
149	
150	    比 Qwen 略少，信息增量更受限。1.7pp 的提升在 bootstrap CI 上与 tail-256 完全重叠。
151	
152	    tail-384 不受 VOTA 截断问题影响（独立的固定长度 tail 截断策略），结果 clean。
153	
154	    DeepSeek 的 pre-transition plateau（76-78%）与 Qwen-7B（77-80%）接近，
155	
156	    说明两个模型在 "猜测能力"（insufficient signal 下的 baseline performance）上几乎一致，
157	
158	    真正的差异由 post-transition 的 model-specific factors（LoRA stability、execution reasoning）决定。
159	
160	    '
161	  tables: []
162	  figures_description: []
163	  analysis: 'DeepSeek 384→512 jump = 15.8pp，虽然是 4 模型中最小的（因 DeepSeek tail-512 = 93.9%，post-transition
164	    值最低），
165	
166	    但仍远大于 256→384 的 1.7pp（ratio 9.3:1），sharp cliff 结论成立。
167	
168	    '
169	- name: tail-384 × CodeLlama-13B
170	  plan_id: plan_016
171	  description: CodeLlama-13B-Instruct full_trace tail-384 tokens SFT
172	  expected_results:
173	    accuracy: 0.798
174	    accuracy_ci_lower: 0.775
175	    accuracy_ci_upper: 0.821
176	    majority_baseline: 0.7151
177	    lift_over_majority_pp: 8.3
178	    diff_vs_tail256_pp: 1.9
179	    mcnemar_vs_tail256_p: 0.14
180	    diff_vs_tail512_pp: -17.7
181	  result_rationale: 'CodeLlama-13B tail-256 = 77.9%。尽管是 4 模型中最大的（13B vs 7B/6.7B/1.5B），
182	
183	    其 tail-384 仍受限于相同的 signal availability bottleneck——模型 capacity 无法弥补 data 中 signal
184	    的缺失。
185	
186	    CodeLlama 在 tail-512 时达到 97.5%（4 模型最高 post-transition 值），
187	
188	    说明更大 capacity 在 signal 充足后的 utilization efficiency 更高。
189	
190	    但 384 tokens 下 signal 仍不足，accuracy 停留在 pre-transition plateau。
191	
192	    这是 "phase transition is signal-driven, not capacity-driven" 的关键证据：
193	
194	    13B 模型在 diagnostic signal 不足时也无法突破 80%。
195	
196	    '
197	  tables:
198	  - name: 4-model tail-384 universal summary
199	    rows:
200	    - model: Qwen-7B
201	      tail256: 77.5%
202	      tail384: 79.5%
203	      tail512: 93.6%
204	      Δ_256_384: +2.0pp
205	      Δ_384_512: +14.1pp
206	      ratio: 7.1x
207	    - model: Qwen-1.5B
208	      tail256: 72.6%
209	      tail384: 74.8%
210	      tail512: 95.6%
211	      Δ_256_384: +2.2pp
212	      Δ_384_512: +20.8pp
213	      ratio: 9.5x
214	    - model: DeepSeek-6.7B
215	      tail256: 76.4%
216	      tail384: 78.1%
217	      tail512: 93.9%
218	      Δ_256_384: +1.7pp
219	      Δ_384_512: +15.8pp
220	      ratio: 9.3x
221	    - model: CodeLlama-13B
222	      tail256: 77.9%
223	      tail384: 79.8%
224	      tail512: 97.5%
225	      Δ_256_384: +1.9pp
226	      Δ_384_512: +17.7pp
227	      ratio: 9.3x
228	    - model: 4-model mean
229	      tail256: 76.1%
230	      tail384: 78.1%
231	      tail512: 95.2%
232	      Δ_256_384: +1.95pp
233	      Δ_384_512: +17.10pp
234	      ratio: 8.8x
235	  figures_description:
236	  - '核心 Figure: 4-model overlaid S-curve budget plot。4 条曲线在 256-384 flat（72-80%），384-512
237	    synchronized sharp jump，512+ ceiling plateau（93-98%）。visual impact: universal
238	    phase transition pattern。'
239	  - 'Gradient ratio bar chart: 每个模型显示 Δ(256→384) vs Δ(384→512) 的对比柱。所有模型的 384→512
240	    柱高 7-10x 于 256→384 柱。'
241	  analysis: '4-model mean tail-384 = 78.1%，在关键指标 [76, 81] 范围内。max diff vs tail-256
242	    = 2.2pp（Qwen-1.5B），在 [0, 3] 内。
243	
244	    所有 4 模型 gradient ratio ≥ 7:1，minimum 256→512 jump = 16.1pp（Qwen-7B），在 [15, 23]
245	    内。
246	
247	    Phase transition 在 384-512 之间是 universal sharp cliff，构成独立 contribution（Contribution
248	    #4）。
249	
250	    Cliff 的位置与 exception trace 的典型 token 长度吻合（Python exception traceback + error message
251	    通常 150-400 tokens），
252	
253	    说明 phase transition 的 physical cause 就是 exception 信号的 inclusion/exclusion threshold。
254	
255	    '
256	- name: cross-seed tail-512 × Qwen-7B
257	  plan_id: plan_017
258	  description: Qwen-7B tail-512 × 3 seeds (42/123/456)，验证 post-transition convergence
259	    band robustness
260	  expected_results:
261	    seed42_accuracy: 0.936
262	    seed123_accuracy: 0.929
263	    seed456_accuracy: 0.941
264	    mean_accuracy: 0.935
265	    std_pp: 0.6
266	    max_min_range_pp: 1.2
267	    all_seeds_above_tail384_max: true
268	  result_rationale: 'Qwen-7B exception_only 3-seed variance = 0（99.83% 完全一致），说明 signal
269	    充足时该模型对 LoRA 初始化完全不敏感。
270	
271	    tail-512 是 post-transition 第一个点（93.6%），signal 已充分但处于 "刚过阈值" 状态——
272	
273	    部分样本的 exception 信息在 tail-384→512 窗口的边界上，这些 "边界样本" 的 prediction 对 LoRA 初始化略有敏感。
274	
275	    但由于 Qwen 在 exception_only 上展现了极强的训练稳定性，tail-512 的 variance 也应该是 4 模型中最小的。
276	
277	    std ≈ 0.6pp 远低于 2pp 阈值。关键: 即使最差 seed (92.9%) 也远高于 tail-384 最好情况 (~80%)，
278	
279	    证明 phase transition 的位置是 seed-robust 的——不存在某个 seed 下 phase transition 右移到 >512
280	    的情况。
281	
282	    '
283	  tables: []
284	  figures_description: []
285	  analysis: 'Convergence band [92.9%, 94.1%] 窄且完全位于 post-transition regime。
286	
287	    与 exception_only ceiling (99.83%) 的 ~6pp gap 来自 tail-512 truncation 导致的 partial
288	    signal loss，
289	
290	    而非训练随机性——这 6pp 是 deterministic information gap，不是 stochastic training gap。
291	
292	    '
293	- name: cross-seed tail-512 × Qwen-1.5B
294	  plan_id: plan_017
295	  description: Qwen-1.5B tail-512 × 3 seeds
296	  expected_results:
297	    seed42_accuracy: 0.956
298	    seed123_accuracy: 0.951
299	    seed456_accuracy: 0.958
300	    mean_accuracy: 0.955
301	    std_pp: 0.4
302	  result_rationale: 'Qwen-1.5B exception_only = 99.83%（与 7B 一致，3 seeds 完美），训练稳定性同样极好。
303	
304	    tail-512 single-seed 95.6% 高于 7B 的 93.6%——更小模型在 "near-threshold signal" 条件下
305	
306	    可能因 LoRA 参数占总参数比例更高而更 efficient（LoRA rank 相同时，1.5B 的 LoRA 适配能力相对于模型规模更大）。
307	
308	    3-seed std ≈ 0.4pp，比 7B 还小，因为 1.5B 的 LoRA landscape 在这个 signal regime 下可能更 smooth。
309	
310	    '
311	  tables: []
312	  figures_description: []
313	  analysis: '1.5B tail-512 mean (95.5%) > 7B tail-512 mean (93.5%) 看似反直觉，
314	
315	    但与 exception_only 的 "signal-limited not capacity-limited" 完全一致：
316	
317	    tail-512 的 signal 已足够简单（接近 exception_only 的 signal quality），
318	
319	    1.5B 的参数效率优势在此显现。
320	
321	    '
322	- name: cross-seed tail-512 × DeepSeek-6.7B
323	  plan_id: plan_017
324	  description: DeepSeek-6.7B tail-512 × 3 seeds
325	  expected_results:
326	    seed42_accuracy: 0.939
327	    seed123_accuracy: 0.925
328	    seed456_accuracy: 0.942
329	    mean_accuracy: 0.935
330	    std_pp: 0.9
331	  result_rationale: 'DeepSeek exception_only 显示 seed 敏感性（seed123=91.09% 离群，σ≈4.8pp），
332	
333	    但 2/3 seeds 鲁棒（99.33%）。tail-512 的 signal 比 exception_only 更 noisy（包含 exception
334	    + trace 尾部混合），
335	
336	    但 signal 主体仍来自 exception 事件。tail-512 的 "effective signal strength" 处于中间地带——
337	
338	    足以学到核心 fault detection pattern 但不足以达 ceiling——
339	
340	    这反而限制了 seed-dependent LoRA 初始化差异的影响范围。
341	
342	    不会出现 exception_only seed123 那样的极端离群值（91.09%），
343	
344	    因为 tail-512 的 mixed signal 降低了模型对单一 mapping (exception→fail) 的依赖。
345	
346	    std ≈ 0.9pp，是 4 模型中最高的，但仍 ≤ 2pp 阈值。
347	
348	    '
349	  tables: []
350	  figures_description: []
351	  analysis: "DeepSeek tail-512 convergence band [92.5%, 94.2%] 比 exception_only [91.09%,\
352	    \ 99.33%] 窄得多。\nParadox: mixed signal 降低了 ceiling 但也降低了 variance。这暗示极端 seed sensitivity\
353	    \ \n主要是 \"pure signal\" 条件下的现象——signal 越纯，对 LoRA→signal mapping 的初始化越敏感。\n"
354	- name: cross-seed tail-512 × CodeLlama-13B
355	  plan_id: plan_017
356	  description: CodeLlama-13B tail-512 × 3 seeds
357	  expected_results:
358	    seed42_accuracy: 0.975
359	    seed123_accuracy: 0.969
360	    seed456_accuracy: 0.973
361	    mean_accuracy: 0.972
362	    std_pp: 0.3
363	  result_rationale: 'CodeLlama-13B exception_only 3-seed 高度一致（seed42/456=99.83%, seed123=100.0%），
364	
365	    训练稳定性极佳——13B 模型的 LoRA landscape 最 smooth。
366	
367	    tail-512 single-seed = 97.5%（4 模型最高 post-transition 值），
368	
369	    说明 CodeLlama 的 13B capacity 在 signal utilization 上有优势。
370	
371	    在如此接近 ceiling 的 accuracy 下，seed variance 极小（≤0.3pp）。
372	
373	    几乎所有样本都被正确分类，variance 仅来自极少数边界样本的 stochastic prediction。
374	
375	    '
376	  tables:
377	  - name: 4-model cross-seed tail-512 summary
378	    rows:
379	    - model: Qwen-7B (7B)
380	      mean: 93.5%
381	      std: 0.6pp
382	      range: '[92.9, 94.1]'
383	      n_seeds: 3
384	    - model: Qwen-1.5B (1.5B)
385	      mean: 95.5%
386	      std: 0.4pp
387	      range: '[95.1, 95.8]'
388	      n_seeds: 3
389	    - model: DeepSeek (6.7B)
390	      mean: 93.5%
391	      std: 0.9pp
392	      range: '[92.5, 94.2]'
393	      n_seeds: 3
394	    - model: CodeLlama (13B)
395	      mean: 97.2%
396	      std: 0.3pp
397	      range: '[96.9, 97.5]'
398	      n_seeds: 3
399	    - model: All models
400	      mean: 94.9%
401	      max_std: 0.9pp
402	      note: all < 2pp threshold
403	  figures_description:
404	  - '4-model convergence band error-bar plot at tail-512: 每模型 mean ± std。4 条 bar 均窄（≤0.9pp），清晰展示
405	    post-transition convergence 的 seed-robustness。'
406	  - 'Overlay on budget curve: 在 4-model S-curve 图的 x=512 点处添加 3-seed error bar，直观显示
407	    convergence band 远离 pre-transition plateau。'
408	  analysis: 'max std = 0.9pp (DeepSeek)，远低于 2pp 阈值。所有模型的 worst seed 都远高于 tail-384
409	    best case (~80%)，
410	
411	    确认 phase transition 位置 seed-robust。cross-seed 验证消除了 "single-seed lucky draw" 的审稿人疑虑。
412	
413	    结合 plan_016 的 tail-384 数据，可以 claim: phase transition 在 384-512 之间是 universal +
414	    sharp + seed-robust。
415	
416	    '
417	- name: CodeLlama-13B tail-2048 (v3 completion)
418	  plan_id: plan_016
419	  description: CodeLlama-13B tail-2048 v3 完成，闭合 4-model budget curve 的最后一个缺失点
420	  expected_results:
421	    accuracy: 0.965
422	    accuracy_ci_lower: 0.954
423	    accuracy_ci_upper: 0.975
424	    pass_f1: 0.976
425	    fail_f1: 0.938
426	    diff_vs_tail1024_pp: -1.7
427	  result_rationale: 'CodeLlama tail-1024 v3 = 98.24%（epoch1 best）。tail-2048 与 tail-1024
428	    的信息增量极小
429	
430	    （1024-2048 区间主要是 loop iterations 和 variable dumps，与 diagnostic signal 无关）。
431	
432	    v2 曾 catastrophic failure（29.6%）因 full-sequence loss dilution + CodeLlama tokenizer
433	    在 2048 tokens 时
434	
435	    生成大量 non-diagnostic tokens，loss 被稀释到 label token 无法获得足够梯度。
436	
437	    v3 采用 label-preserving truncation fix 应避免 catastrophic failure。
438	
439	    但 2048 tokens 的 attention dilution 可能导致 accuracy 略低于 tail-1024（98.24%→96.5%），
440	
441	    类似 Qwen-7B tail-1024 (96.47%) → tail-2048 (97.3%) 的 pattern，但 CodeLlama 因 tokenizer
442	    效率差异可能退化。
443	
444	    其他模型 tail-2048 参照: Qwen-7B 97.3%, Qwen-1.5B 97.9%, DeepSeek 94.96%。
445	
446	    CodeLlama 96.5% 处于合理范围，在 [95, 98] 关键指标内。
447	
448	    '
449	  tables:
450	  - name: 4-model complete tail-2048 comparison
451	    rows:
452	    - model: Qwen-7B
453	      tail2048: 97.3%
454	      tail1024: 96.5%
455	      delta: +0.8pp
456	    - model: Qwen-1.5B
457	      tail2048: 97.9%
458	      tail1024: 96.6%
459	      delta: +1.3pp
460	    - model: DeepSeek-6.7B
461	      tail2048: 95.0%
462	      tail1024: 96.5%
463	      delta: -1.5pp
464	    - model: CodeLlama-13B
465	      tail2048: 96.5% (pred)
466	      tail1024: 98.2%
467	      delta: -1.7pp (pred)
468	  figures_description: []
469	  analysis: 'CodeLlama tail-2048 完成后 4 模型 budget curve 矩阵完整（4 models × 6 token budgets）。
470	
471	    所有模型的 tail-1024→tail-2048 delta 均 ≤ 2pp（正或负），confirming ceiling plateau。
472	
473	    DeepSeek 和 CodeLlama 在 tail-2048 略低于 tail-1024 可能反映 attention dilution at longer
474	    sequences。
475	
476	    '
477	- name: Failure mode analysis (no GPU)
478	  plan_id: plan_018
479	  description: 用已有 predictions.jsonl 系统分析 exception_only/VOTA/full_trace/no_trace
480	    的 failure modes
481	  expected_results:
482	    exception_only_errors:
483	      total: 2
484	      generator_exit_false_positive: 2
485	      error_concentration: 100% from HumanEval/95 check_dict_case
486	      interpretability: fully deterministic, representation-inherent
487	    vota_errors:
488	      total: 7
489	      exception_overlap_with_exc_only: 2
490	      loop_noise_confusion: 3
491	      ae_edge_case: 2
492	      interpretability: partially interpretable
493	    full_trace_errors:
494	      total: 217
495	      fail_recall_dominated: true
496	      scattered_distribution: true
497	      top_error_category: information overload — no dominant pattern
498	      interpretability: low — diffuse across problem types
499	    no_trace_errors:
500	      total: 296
501	      majority_class_bias: true
502	      fail_recall: 0.7345
503	      systematic_pattern: under-predicts fail (minority class)
504	      interpretability: high — systematic bias, single root cause
505	    tier1_vs_tier2_failure_modes_qualitatively_distinct: true
506	    error_overlap_hierarchy: exc_only(2) ⊂ vota(7) ⊂ full_trace(217)
507	  result_rationale: "exception_only 的 2 个错误已被彻底分析（GeneratorExit, id=901/905），error\
508	    \ analysis 将确认无新发现。\nVOTA 在 exception_only 基础上增加了 loop + ae 信号，VOTA 的 7 个错误中 2\
509	    \ 个与 exception_only 重叠（GeneratorExit），\n剩余 5 个是 loop compression 引入的噪声：部分样本的 loop\
510	    \ 行为 \"看似正常\" 但实际有 subtle fault，\n或者正常 loop 信息稀释了 exception signal 的 attention\
511	    \ weight。\nfull_trace 的 ~217 个错误（81.76% accuracy, 1190 × (1-0.8176) ≈ 217）呈散射分布——\n\
512	    information overload 使模型无法对任何 single signal source 形成 stable attention pattern，\n\
513	    错误跨越多种程序类型和错误类型，无清晰聚类。fail_recall 尤其差（69.6%），因为 fail 样本的 diagnostic signal \n\
514	    被 irrelevant trace tokens 淹没。\nno_trace 的 ~296 个错误主要来自 fail class under-prediction（majority\
515	    \ class bias）。\n关键发现: error interpretability 与 tier level 正相关——Tier 1 error 100%\
516	    \ interpretable，\nTier 2/full_trace error 呈 stochastic noise pattern。\n"
517	  tables:
518	  - name: Error mode summary by condition
519	    rows:
520	    - condition: exception_only
521	      n_errors: 2
522	      dominant_mode: GeneratorExit false positive
523	      interpretable: 100%
524	      actionable: tracer fix
525	    - condition: VOTA
526	      n_errors: 7
527	      dominant_mode: loop noise + edge assertion
528	      interpretable: ~60%
529	      actionable: component pruning
530	    - condition: full_trace
531	      n_errors: ~217
532	      dominant_mode: scattered / information overload
533	      interpretable: <20%
534	      actionable: unclear
535	    - condition: no_trace
536	      n_errors: ~296
537	      dominant_mode: majority-class bias
538	      interpretable: 100%
539	      actionable: add any signal
540	  figures_description:
541	  - 'Error heatmap: x=problem_id (sorted), y=condition。Tier 1 errors 高度集中在 2 个 problem，full_trace
542	    errors 均匀分散。'
543	  - 'Error overlap Venn diagram: exception_only(2) ⊂ VOTA(7) ⊂ full_trace(217) ⊂ no_trace(296)。strict
544	    subset 关系可视化 tier hierarchy。'
545	  analysis: 'Error analysis 为 two-tier hierarchy 增加第三个 evidence dimension（accuracy
546	    / calibration / error interpretability）。
547	
548	    Tier 1 的 failure mode 是 deterministic + representation-inherent（可通过 tracer 改进消除），
549	
550	    lower-tier 的 failure mode 是 stochastic + capability-dependent（改进路径不明确）。
551	
552	    这强化 design principle: 最高 specificity 的 signal 不仅 accuracy 最高、calibration 最好，
553	
554	    其 failure mode 也最可解释和最可修复。
555	
556	    '
557	- name: Cross-model calibration (4 models × exception_only)
558	  plan_id: plan_019
559	  description: 4 models exception_only 的 ECE/Brier Score 对比，验证 calibration quality
560	    跨模型 universal
561	  expected_results:
562	    qwen7b:
563	      ece: 0.0027
564	      brier: 0.0013
565	      accuracy: 0.9983
566	      note: existing data
567	    qwen15b:
568	      ece: 0.0031
569	      brier: 0.0015
570	      accuracy: 0.9983
571	    deepseek:
572	      ece: 0.0082
573	      brier: 0.0055
574	      accuracy: 0.9933
575	    codellama13b:
576	      ece: 0.0024
577	      brier: 0.0011
578	      accuracy: 0.9983
579	    max_ece: 0.0082
580	    min_ece_ratio_vs_notrace: 21x (DeepSeek)
581	    max_ece_ratio_vs_notrace: 71x (CodeLlama)
582	    calibration_universally_excellent: true
583	  result_rationale: 'Qwen-7B 已有数据（ECE=0.0027, Brier=0.0013），作为参照。
584	
585	    Qwen-1.5B 与 7B 的 exception_only 结果完全一致（99.83%, 相同 2 个 irreducible errors），
586	
587	    其 softmax 分布应高度相似。1.5B 模型的 logit scale 可能略大（更少参数→更少 regularization→logits 更尖锐），
588	
589	    但由于 accuracy 完全一致，ECE 应同样极低。预测 ECE≈0.003, Brier≈0.0015。
590	
591	    CodeLlama-13B exception_only 同为 99.83%（seed42/456）且 seed123=100%，
592	
593	    更大模型通常 logit 更 smooth → calibration 可能更好。预测 ECE≈0.0024, Brier≈0.0011。
594	
595	    DeepSeek exception_only = 99.33%（seed42），8/1190 errors 比 Qwen 多 6 个，
596	
597	    这些额外错误样本的 confidence 分布可能不那么极端（错误样本可能 confidence 居中而非极高），
598	
599	    导致 ECE 略高（~0.008）。但仍远低于 no_trace baseline（0.171），ratio ≈ 21x。
600	
601	    关键: 所有 4 模型 ECE < 0.01，跨 3 families/2 scales calibration 一致优秀，
602	
603	    确认 Tier 1 signal 的 calibration benefit 是 model-agnostic 的。
604	
605	    '
606	  tables:
607	  - name: 4-model exception_only calibration comparison
608	    rows:
609	    - model: Qwen-7B
610	      accuracy: 99.83%
611	      ece: 0.0027
612	      brier: 0.0013
613	      ece/notrace_ece: 63x
614	    - model: Qwen-1.5B
615	      accuracy: 99.83%
616	      ece: 0.0031
617	      brier: 0.0015
618	      ece/notrace_ece: 55x
619	    - model: DeepSeek-6.7B
620	      accuracy: 99.33%
621	      ece: 0.0082
622	      brier: 0.0055
623	      ece/notrace_ece: 21x
624	    - model: CodeLlama-13B
625	      accuracy: 99.83%
626	      ece: 0.0024
627	      brier: 0.0011
628	      ece/notrace_ece: 71x
629	  figures_description:
630	  - '4-panel reliability diagram: 每个模型一个 panel，exception_only 点紧贴 perfect calibration
631	    对角线。'
632	  - 'ECE bar chart: 4 models side-by-side，所有 bars 极低（<0.01），baseline no_trace bar
633	    高出 20-70x。'
634	  analysis: '4-model calibration universality 是论文的 supplementary evidence。与 accuracy
635	    universality 互补：
636	
637	    exception signal 不仅让所有模型 "预测对"，更让所有模型 "知道自己对"。
638	
639	    DeepSeek ECE 略高 (0.008 vs 0.002-0.003) 反映其 LoRA seed sensitivity 的残余效应，
640	
641	    但在 practical 意义上仍属 "近完美校准"。
642	
643	    '
644	- name: Few-shot prompting baseline (GPT-4o / Claude)
645	  plan_id: plan_020
646	  description: GPT-4o 和 Claude 在 exception_only traces 上的 0-shot + 3-shot verdict
647	    prediction，作为 non-SFT upper bound
648	  expected_results:
649	    gpt4o_0shot:
650	      accuracy: 0.932
651	      fail_recall: 0.83
652	      pass_recall: 0.97
653	    gpt4o_3shot:
654	      accuracy: 0.951
655	      fail_recall: 0.88
656	      pass_recall: 0.98
657	    claude_0shot:
658	      accuracy: 0.942
659	      fail_recall: 0.86
660	      pass_recall: 0.98
661	    claude_3shot:
662	      accuracy: 0.961
663	      fail_recall: 0.91
664	      pass_recall: 0.98
665	    sft_exception_only_best: 0.9983
666	    sft_advantage_over_best_fewshot_pp: 3.7
667	    sft_error_rate_ratio: 11.5x fewer errors
668	  result_rationale: '已有 base model zero-shot 数据: Qwen-7B 89.08%, DeepSeek-7B 90.59%,
669	    Qwen-1.5B 93.45%, CodeLlama-13B 51.01%。
670	
671	    Frontier 模型（GPT-4o, Claude）有更强的 instruction following、更大 context window、更好的 reasoning，
672	
673	    zero-shot 应 > 所有 base model zero-shot。GPT-4o zero-shot 预测 ~93%（类似 Qwen-1.5B zero-shot
674	    93.45%，
675	
676	    但 GPT-4o 对 structured error data 的理解更好）。Claude 可能略高（~94%）因其 instruction following
677	    更精准。
678	
679	    3-shot 提供 exemplars 帮助模型理解 output format 和 decision boundary，预计提升 2-3pp：
680	
681	    GPT-4o 3-shot ~95%, Claude 3-shot ~96%。
682	
683	    然而 few-shot 受限于 in-context learning 的 fundamental limitation: (1) 仅 3 个 examples
684	    无法覆盖所有 edge cases，
685	
686	    (2) attention 需同时处理 instructions + examples + query，(3) 无 parameter-level adaptation。
687	
688	    SFT exception_only (99.83%) 仍 > best few-shot (~96%) 约 3.7pp。
689	
690	    虽然 3.7pp 看似小，但在 error rate 上是 11.5x 差异（0.17% vs 3.9%）——
691	
692	    SFT 达到 representation 理论上限，few-shot 仍有 ~39 个额外错误。
693	
694	    关键: fail_recall 差距更大（SFT 100% vs few-shot ~91%），说明 few-shot 在 minority class 上更差。
695	
696	    '
697	  tables:
698	  - name: SFT vs Few-shot vs Zero-shot comparison
699	    rows:
700	    - method: SFT exception_only (Qwen-7B, 3 seeds mean)
701	      accuracy: 99.83%
702	      errors: 2
703	      type: parameter adaptation
704	    - method: SFT exception_only (Qwen-1.5B)
705	      accuracy: 99.83%
706	      errors: 2
707	      type: parameter adaptation
708	    - method: Claude 3-shot
709	      accuracy: ~96.1%
710	      errors: ~46
711	      type: in-context learning
712	    - method: GPT-4o 3-shot
713	      accuracy: ~95.1%
714	      errors: ~58
715	      type: in-context learning
716	    - method: Claude 0-shot
717	      accuracy: ~94.2%
718	      errors: ~69
719	      type: instruction following
720	    - method: GPT-4o 0-shot
721	      accuracy: ~93.2%
722	      errors: ~81
723	      type: instruction following
724	    - method: Qwen-1.5B 0-shot (base)
725	      accuracy: 93.45%
726	      errors: 78
727	      type: base model
728	    - method: Qwen-7B few-shot (base)
729	      accuracy: 90.84%
730	      errors: 109
731	      type: base model
732	    - method: Qwen-7B 0-shot (base)
733	      accuracy: 89.08%
734	      errors: 130
735	      type: base model
736	  figures_description:
737	  - 'Accuracy comparison bar chart: SFT bars (green, ~99.8%) vs frontier few-shot
738	    bars (blue, ~95-96%) vs base model bars (gray, ~89-93%)。SFT 1.5B = SFT 7B 是 visual
739	    highlight。'
740	  analysis: 'Few-shot baseline 回答两个潜在审稿人问题:
741	
742	    (1) "为什么需要 SFT? Frontier model 不能直接做?" → No, 即使 GPT-4o/Claude 3-shot 也比 SFT 7B
743	    差 3.7pp (11.5x more errors)。
744	
745	    (2) "SFT 的 value 是什么?" → parameter-level adaptation 将 error rate 从 ~4% 压到 representation-inherent
746	    floor 0.17%。
747	
748	    更深层: SFT exception_only (1.5B, ~$0.5 GPU-hr) > Claude 3-shot (~$50 API)，
749	
750	    说明 "right signal + cheap SFT" 优于 "frontier model + expensive inference"，
751	
752	    这是论文 practical impact 的核心论点。
753	
754	    '
755	- name: OOD generalization (cross-language traces)
756	  plan_id: plan_021
757	  description: 在 Python 外的编程语言 (Java/JavaScript) trace 上测试 exception_only 泛化性
758	  expected_results:
759	    java_exception_only_accuracy: 0.972
760	    javascript_exception_only_accuracy: 0.963
761	    python_in_domain_accuracy: 0.9983
762	    ood_mean_accuracy: 0.968
763	    ood_gap_vs_in_domain_pp: 3.1
764	    ood_vs_python_no_trace_pp: '+21.6'
765	  result_rationale: 'exception_only 学到的核心 pattern 是 "[ERROR] 标记存在 → fault detected
766	    → predict fail" 的映射。
767	
768	    这个 pattern 的语言依赖性极低: Java (try/catch → Exception class + message)、
769	
770	    JavaScript (try/catch → Error type + message) 的 exception 结构与 Python 高度同构。
771	
772	    tracer 生成的 [ERROR] tag 格式跨语言一致（由 tracer 标准化），因此 SFT 模型学到的 pattern 可迁移。
773	
774	    accuracy 从 99.83% 降到 ~97% 的 gap 来源: (1) OOD exception message 的 lexical distribution
775	    与 Python 不同
776	
777	    （Java 的 NullPointerException、JavaScript 的 TypeError 在训练集中缺失），
778	
779	    (2) 少数语言特有 edge case（如 Java checked exception 是正常控制流，非 fault indicator）。
780	
781	    关键: 如果 OOD > 96%，说明 exception signal 的 fault detection 语义跨语言 universal，
782	
783	    SFT 学到的不是 Python-specific pattern 而是 general fault indicator recognition。
784	
785	    风险: 构建高质量 OOD 测试集需要 non-trivial 工程（不同语言的 tracer + benchmark），
786	
787	    如果时间不足应优先确保 plan_016/017 的 core experiments。
788	
789	    '
790	  tables:
791	  - name: Cross-language exception_only accuracy
792	    rows:
793	    - language: Python (in-domain)
794	      accuracy: 99.83%
795	      n: 1190
796	      note: training language
797	    - language: Java (OOD)
798	      accuracy: ~97.2%
799	      n: ~500
800	      note: NullPointerException 等 novel types
801	    - language: JavaScript (OOD)
802	      accuracy: ~96.3%
803	      n: ~500
804	      note: TypeError/ReferenceError novel
805	  figures_description:
806	  - 'Cross-language accuracy grouped bar: Python >> Java ≈ JavaScript，gap 小（<4pp），证明
807	    exception signal 跨语言 robust。'
808	  analysis: 'OOD 是 "nice-to-have" 而非 "must-have"。4 models × 3 families × 2 scales
809	    的 in-domain universality
810	
811	    已构成充分证据。OOD 数据若好（>96%）则是 reviewer concern 的 decisive counter-argument，
812	
813	    但构建成本高。建议: 如果 plan_016/017 结果确认 best tier，OOD 可留为 camera-ready supplement；
814	
815	    如果 plan_016/017 结果弱于预期，OOD 的必要性上升。
816	
817	    '
818	- name: Training dynamics (step-level learning curve)
819	  plan_id: plan_022
820	  description: exception_only vs full_trace 的 step-level eval learning curve，量化 convergence
821	    speed 差异
822	  expected_results:
823	    exception_only:
824	      steps_to_90pct: 60
825	      steps_to_95pct: 80
826	      steps_to_99pct: 150
827	      steps_to_final: 200
828	      final_accuracy: 0.9983
829	      loss_at_step50: 0.15
830	    full_trace:
831	      steps_to_80pct: 250
832	      steps_to_final: 900 (3 epochs)
833	      final_accuracy: 0.8176
834	      never_reaches_90: true
835	      loss_at_step50: 0.35
836	    convergence_speed_ratio: 4.2x (steps to reach full_trace ceiling)
837	    crossover_step: 45
838	  result_rationale: 'exception_only 的有效训练信号高度集中: pass 样本对应 "无 [ERROR]"，fail 样本对应 "有
839	    [ERROR] + type + message"。
840	
841	    这是一个 near-binary feature，模型只需学习 "[ERROR] presence → fail" 的 mapping，
842	
843	    所需训练步数极少。训练集 effective unique 样本仅 2858 条，batch_size=4 时 ~715 steps/epoch。
844	
845	    50-100 steps（约 7-14% epoch）内模型应已捕获核心 pattern，accuracy > 95%。
846	
847	    full_trace 包含大量 irrelevant tokens（variable values, memory addresses, loop iterations），
848	
849	    模型需要 (1) 先学到忽略 irrelevant tokens 的 attention pattern，
850	
851	    (2) 再从 relevant tokens 中 extract fault signal。这是两阶段 learning，天然更慢。
852	
853	    且 information overload 导致 attention 无法稳定聚焦，收敛到 ~82% 后 plateau（受 noise ceiling
854	    限制）。
855	
856	    crossover 预测在 ~45 steps: exception_only 在不到 50 steps 时就超过 full_trace 的最终 accuracy
857	    (81.76%)。
858	
859	    这意味着 SFT exception_only 10 分钟的训练 > SFT full_trace 3 个 epoch 的训练，
860	
861	    是论文中极具冲击力的 figure。
862	
863	    '
864	  tables:
865	  - name: Convergence milestone comparison
866	    rows:
867	    - milestone: 80% accuracy
868	      exception_only: ~30 steps (~4 min)
869	      full_trace: ~250 steps (~35 min)
870	    - milestone: 90% accuracy
871	      exception_only: ~60 steps (~8 min)
872	      full_trace: never reached
873	    - milestone: 95% accuracy
874	      exception_only: ~80 steps (~11 min)
875	      full_trace: never reached
876	    - milestone: 99% accuracy
877	      exception_only: ~150 steps (~21 min)
878	      full_trace: never reached
879	    - milestone: final
880	      exception_only: 99.83% @ ~200 steps
881	      full_trace: 81.76% @ ~900 steps
882	  figures_description:
883	  - '核心 Figure: dual-panel learning curve。Left panel: x=training steps, y=accuracy。exception_only
884	    steep S-curve 快速 saturate at 99.83%，full_trace slow rise plateau at 81.76%。vertical
885	    dashed line at crossover step ~45。Right panel: same x-axis, y=train loss。exception_only
886	    loss drops fast and stays low，full_trace loss drops slowly and converges to higher
887	    floor。'
888	  - 'Supplementary: convergence speed as function of signal density (scatter plot
889	    with exception_only, VOTA, full_trace as data points)。'
890	  analysis: "Training dynamics 提供 information density 假说的 dynamic evidence，与 label_only\
891	    \ ablation 的 static evidence 互补:\n- Static evidence (plan_002): gradient dilution\
892	    \ 贡献 26%，information overload 贡献 74%\n- Dynamic evidence (plan_022): exception_only\
893	    \ converge 4.2x faster + reaches higher ceiling\n两者共同证明: 高信息密度信号不仅提升 accuracy\
894	    \ ceiling，更 dramatically 加速 learning。\nCrossover at ~45 steps 是论文中最直观的 \"why exception\
895	    \ works\" evidence —— \n\"一个极简信号在 50 步内超越完整 trace 训练 3 个 epoch 的结果\"。"
896	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7580a4a-cfd7-4b74-ae1b-367d0032bfad",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "b455245c-1c66-4d06-b594-a95fa32e596b",
  "sourceToolAssistantUUID": "a7580a4a-cfd7-4b74-ae1b-367d0032bfad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T12:24:38.331Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LzH7iQgcWaqa4WTtWnXNKZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_provenance.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b455245c-1c66-4d06-b594-a95fa32e596b",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2eMman6rKgp4R1Pm2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "656139ea-c1e3-415f-9022-9d058082ee5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbakmhbmznEJSi3XACTkZf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22062,
      "cache_read_input_tokens": 40157,
      "output_tokens": 331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22062
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 331,
          "cache_read_input_tokens": 40157,
          "cache_creation_input_tokens": 22062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22062,
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

_source line 37 · 2026-05-18T12:24:38.596Z_

<details><summary>↩ Tool result · `toolu_01LzH7iQgcWaqa4WTtWnXNKZ`</summary>

```text
1	paper:
2	  title: ''
3	  version: 45
4	  generated_at: '2026-05-18T07:19:46.822458+00:00'
5	claims:
6	- id: C001
7	  location:
8	    section: experiments
9	    paragraph: 0
10	    sentence: 0
11	  text: test claim
12	  type: quantitative
13	  evidence:
14	  - exp_id: vota_exception_only_seed42_v2
15	    metric: accuracy
16	    value: 0.9983
17	  decisions: []
18	  deprecated: true
19	- id: C002
20	  location:
21	    section: experiments
22	    paragraph: 0
23	    sentence: 0
24	  text: Cross-model gap under exception_only is 0.50pp (Qwen 99.83%, DeepSeek 99.33%)
25	  type: quantitative
26	  evidence:
27	  - exp_id: vota_exception_only_seed42_v2
28	    metric: accuracy
29	    value: 0.9983
30	  - exp_id: deepseek_exception_only_seed42
31	    metric: accuracy
32	    value: 0.9933
33	  decisions: []
34	  deprecated: false
35	- id: C004
36	  location:
37	    section: experiments
38	    paragraph: 0
39	    sentence: 0
40	  text: Cross-model gap under VOTA is 14.96pp (Qwen 99.41%, DeepSeek 84.45%)
41	  type: quantitative
42	  evidence:
43	  - exp_id: vota_seed42_v5
44	    metric: accuracy
45	    value: 0.9941
46	  - exp_id: deepseek_vota_seed42
47	    metric: accuracy
48	    value: 0.8445
49	  decisions: []
50	  deprecated: false
51	- id: C007
52	  location:
53	    section: experiments
54	    paragraph: 0
55	    sentence: 0
56	  text: 'No-trace baseline: Qwen 75.13%, DeepSeek 73.36%, marginally above majority
57	    71.51%'
58	  type: quantitative
59	  evidence:
60	  - exp_id: no_trace_seed42_v5
61	    metric: accuracy
62	    value: 0.7513
63	  - exp_id: deepseek_no_trace_seed42
64	    metric: accuracy
65	    value: 0.7336
66	  decisions: []
67	  deprecated: false
68	- id: C011
69	  location:
70	    section: experiments
71	    paragraph: 0
72	    sentence: 0
73	  text: 'Seed robustness: 99.83% sigma=0 n=3 seeds, exactly 2 errors each'
74	  type: quantitative
75	  evidence:
76	  - exp_id: vota_exception_only_seed42_v2
77	    metric: accuracy
78	    value: 0.9983
79	  - exp_id: exception_only_seed123
80	    metric: accuracy
81	    value: 0.9983
82	  - exp_id: exception_only_seed456
83	    metric: accuracy
84	    value: 0.9983
85	  decisions: []
86	  deprecated: false
87	- id: C016
88	  location:
89	    section: experiments
90	    paragraph: 0
91	    sentence: 0
92	  text: ae_only (99.92%) and exception_only (99.83%) indistinguishable (p=0.80 McNemar)
93	  type: quantitative
94	  evidence:
95	  - exp_id: vota_ae_only_seed42
96	    metric: accuracy
97	    value: 0.9992
98	  - exp_id: vota_ae_only_seed42
99	    metric: pairwise_p_value
100	    value: 0.8
101	  decisions: []
102	  deprecated: false
103	- id: C022
104	  location:
105	    section: experiments
106	    paragraph: 0
107	    sentence: 0
108	  text: exception_only exceeds VOTA (p=0.01)
109	  type: quantitative
110	  evidence:
111	  - exp_id: vota_exception_only_seed42_v2
112	    metric: lift_vs_vota_pvalue
113	    value: 0.01
114	  decisions: []
115	  deprecated: false
116	- id: C029
117	  location:
118	    section: experiments
119	    paragraph: 0
120	    sentence: 0
121	  text: VOTA_no_ae 99.40% ≈ VOTA 99.41% (statistically equivalent)
122	  type: quantitative
123	  evidence:
124	  - exp_id: vota_no_ae_seed42
125	    metric: accuracy
126	    value: 0.994
127	  - exp_id: vota_seed42_v5
128	    metric: accuracy
129	    value: 0.9941
130	  decisions: []
131	  deprecated: false
132	- id: C037
133	  location:
134	    section: experiments
135	    paragraph: 0
136	    sentence: 0
137	  text: loop_only 85.63% improves over no_trace 75.13% by 10.50pp
138	  type: quantitative
139	  evidence:
140	  - exp_id: vota_loop_only_seed42
141	    metric: accuracy
142	    value: 0.8563
143	  - exp_id: no_trace_seed42_v5
144	    metric: accuracy
145	    value: 0.7513
146	  decisions: []
147	  deprecated: false
148	- id: C046
149	  location:
150	    section: experiments
151	    paragraph: 0
152	    sentence: 0
153	  text: Gradient dilution 26% (+4.46pp), information overload 74% (+13.19pp)
154	  type: quantitative
155	  evidence:
156	  - exp_id: full_trace_seed42_v5
157	    metric: accuracy
158	    value: 0.8176
159	  - exp_id: full_trace_label_only_seed42
160	    metric: accuracy
161	    value: 0.8622
162	  - exp_id: vota_seed42_v5
163	    metric: accuracy
164	    value: 0.9941
165	  decisions: []
166	  deprecated: false
167	- id: C056
168	  location:
169	    section: experiments
170	    paragraph: 0
171	    sentence: 0
172	  text: 'Calibration ECE: ae_only=0.0004, exception_only=0.003, VOTA=0.005, full_trace=0.096,
173	    no_trace=0.172'
174	  type: quantitative
175	  evidence:
176	  - exp_id: calibration_analysis_seed42
177	    metric: ae_only.ece
178	    value: 0.000415
179	  - exp_id: calibration_analysis_seed42
180	    metric: exception_only.ece
181	    value: 0.002717
182	  - exp_id: calibration_analysis_seed42
183	    metric: vota.ece
184	    value: 0.00541
185	  - exp_id: calibration_analysis_seed42
186	    metric: full_trace.ece
187	    value: 0.095817
188	  - exp_id: calibration_analysis_seed42
189	    metric: no_trace.ece
190	    value: 0.171476
191	  decisions: []
192	  deprecated: false
193	- id: C067
194	  location:
195	    section: experiments
196	    paragraph: 0
197	    sentence: 0
198	  text: 'Brier: exception_only=0.001, ae_only=0.001, no_trace=0.197'
199	  type: quantitative
200	  evidence:
201	  - exp_id: calibration_analysis_seed42
202	    metric: exception_only.brier_score
203	    value: 0.001311
204	  - exp_id: calibration_analysis_seed42
205	    metric: ae_only.brier_score
206	    value: 0.000847
207	  - exp_id: calibration_analysis_seed42
208	    metric: no_trace.brier_score
209	    value: 0.197152
210	  decisions: []
211	  deprecated: false
212	- id: C079
213	  location:
214	    section: experiments
215	    paragraph: 0
216	    sentence: 0
217	  text: 'DeepSeek exception_only: 99.83% at epoch 1, degraded to 99.33%'
218	  type: quantitative
219	  evidence:
220	  - exp_id: deepseek_exception_only_seed42
221	    metric: epoch1_accuracy
222	    value: 0.9983
223	  - exp_id: deepseek_exception_only_seed42
224	    metric: accuracy
225	    value: 0.9933
226	  decisions: []
227	  deprecated: false
228	- id: C092
229	  location:
230	    section: experiments
231	    paragraph: 0
232	    sentence: 0
233	  text: 'DeepSeek full_trace v3: 79.16% accuracy (label-preserving truncation fix)'
234	  type: quantitative
235	  evidence:
236	  - exp_id: deepseek_full_trace_seed42_v3
237	    metric: accuracy
238	    value: 0.7916
239	  decisions:
240	  - note: Updated from invalidated v1 (10.59%) to v3 (79.16%) per Director P2 instruction
241	      2026-05-16
242	  deprecated: false
243	- id: C093
244	  location:
245	    section: method
246	    paragraph: 0
247	    sentence: 0
248	  text: 'Dataset: 4720 train, 1190 test, 71.5% pass / 28.5% fail, majority baseline
249	    71.51%'
250	  type: quantitative
251	  evidence:
252	  - exp_id: no_trace_seed42_v5
253	    metric: majority_baseline
254	    value: 0.7151
255	  decisions: []
256	  deprecated: false
257	- id: C095
258	  location:
259	    section: method
260	    paragraph: 0
261	    sentence: 0
262	  text: LoRA rank=16 alpha=32, 3 epochs, batch 4, grad accum 8, lr 2e-4, max seq 2048
263	  type: methodological
264	  evidence:
265	  - exp_id: vota_seed42_v5
266	    metric: train_loss
267	    value: 0.05
268	  - exp_id: vota_seed42_v5
269	    metric: epochs
270	    value: 3
271	  decisions:
272	  - note: LoRA hyperparameters verified from train_sft.py source code and vota_seed42_v5
273	      training config. All values match code defaults.
274	  deprecated: false
275	- id: C098
276	  location:
277	    section: method
278	    paragraph: 0
279	    sentence: 0
280	  text: full_trace_label_only masks trace tokens, loss only on verdict token
281	  type: methodological
282	  evidence:
283	  - exp_id: full_trace_label_only_seed42
284	    metric: description
285	    value: 0
286	  decisions: []
287	  deprecated: false
288	- id: C099
289	  location:
290	    section: introduction
291	    paragraph: 0
292	    sentence: 0
293	  text: exception events alone achieve >=99.3% accuracy, cross-model gap = 0.50pp
294	  type: quantitative
295	  evidence:
296	  - exp_id: vota_exception_only_seed42_v2
297	    metric: accuracy
298	    value: 0.9983
299	  - exp_id: deepseek_exception_only_seed42
300	    metric: accuracy
301	    value: 0.9933
302	  decisions: []
303	  deprecated: false
304	- id: C101
305	  location:
306	    section: introduction
307	    paragraph: 0
308	    sentence: 0
309	  text: VOTA degrades by 14.96pp on the weaker model
310	  type: quantitative
311	  evidence:
312	  - exp_id: vota_seed42_v5
313	    metric: accuracy
314	    value: 0.9941
315	  - exp_id: deepseek_vota_seed42
316	    metric: accuracy
317	    value: 0.8445
318	  decisions: []
319	  deprecated: false
320	- id: C104
321	  location:
322	    section: introduction
323	    paragraph: 0
324	    sentence: 0
325	  text: gradient dilution 26%, information overload 74%
326	  type: quantitative
327	  evidence:
328	  - exp_id: full_trace_seed42_v5
329	    metric: accuracy
330	    value: 0.8176
331	  - exp_id: full_trace_label_only_seed42
332	    metric: accuracy
333	    value: 0.8622
334	  - exp_id: vota_seed42_v5
335	    metric: accuracy
336	    value: 0.9941
337	  decisions: []
338	  deprecated: false
339	- id: C108
340	  location:
341	    section: introduction
342	    paragraph: 0
343	    sentence: 0
344	  text: Tier 1 signals >=99.8%, Tier 2 (loop) 85.6%
345	  type: quantitative
346	  evidence:
347	  - exp_id: vota_ae_only_seed42
348	    metric: accuracy
349	    value: 0.9992
350	  - exp_id: vota_exception_only_seed42_v2
351	    metric: accuracy
352	    value: 0.9983
353	  - exp_id: vota_loop_only_seed42
354	    metric: accuracy
355	    value: 0.8563
356	  decisions: []
357	  deprecated: false
358	- id: C113
359	  location:
360	    section: introduction
361	    paragraph: 0
362	    sentence: 0
363	  text: exception_only 99.83%/99.33% across two models
364	  type: quantitative
365	  evidence:
366	  - exp_id: vota_exception_only_seed42_v2
367	    metric: accuracy
368	    value: 0.9983
369	  - exp_id: deepseek_exception_only_seed42
370	    metric: accuracy
371	    value: 0.9933
372	  decisions: []
373	  deprecated: false
374	- id: C114
375	  location:
376	    section: related_work
377	    paragraph: 0
378	    sentence: 0
379	  text: gradient dilution 26%, information overload 74% (referenced in Related Work
380	    positioning)
381	  type: quantitative
382	  evidence:
383	  - exp_id: full_trace_seed42_v5
384	    metric: accuracy
385	    value: 0.8176
386	  - exp_id: full_trace_label_only_seed42
387	    metric: accuracy
388	    value: 0.8622
389	  - exp_id: vota_seed42_v5
390	    metric: accuracy
391	    value: 0.9941
392	  decisions: []
393	  deprecated: false
394	- id: C115
395	  location:
396	    section: discussion
397	    paragraph: 0
398	    sentence: 0
399	  text: exception_only 2 errors are identical across 3 seeds (id=901, id=905, check_dict_case,
400	    false negatives)
401	  type: quantitative
402	  evidence:
403	  - exp_id: vota_exception_only_seed42_v2
404	    metric: accuracy
405	    value: 0.9983
406	  - exp_id: exception_only_seed123
407	    metric: accuracy
408	    value: 0.9983
409	  - exp_id: exception_only_seed456
410	    metric: accuracy
411	    value: 0.9983
412	  decisions: []
413	  deprecated: false
414	- id: C117
415	  location:
416	    section: discussion
417	    paragraph: 0
418	    sentence: 0
419	  text: 100% error overlap sigma=0 across seeds — irreducible samples
420	  type: quantitative
421	  evidence:
422	  - exp_id: exception_only_seed123
423	    metric: seed_comparison.max_diff
424	    value: 0
425	  decisions: []
426	  deprecated: false
427	- id: C120
428	  location:
429	    section: discussion
430	    paragraph: 0
431	    sentence: 0
432	  text: 'DeepSeek full_trace v3: 79.16% (truncation mismatch fixed in v3, v1 invalidated)'
433	  type: quantitative
434	  evidence:
435	  - exp_id: deepseek_full_trace_seed42_v3
436	    metric: accuracy
437	    value: 0.7916
438	  decisions:
439	  - note: Updated from invalidated v1 (10.59%) to v3 (79.16%) per Director P2 instruction
440	      2026-05-16
441	  deprecated: false
442	- id: C121
443	  location:
444	    section: conclusion
445	    paragraph: 0
446	    sentence: 0
447	  text: 'Exception events: 99.83% Qwen, 99.33% DeepSeek, gap 0.50pp'
448	  type: quantitative
449	  evidence:
450	  - exp_id: vota_exception_only_seed42_v2
451	    metric: accuracy
452	    value: 0.9983
453	  - exp_id: deepseek_exception_only_seed42
454	    metric: accuracy
455	    value: 0.9933
456	  decisions: []
457	  deprecated: false
458	- id: C123
459	  location:
460	    section: conclusion
461	    paragraph: 0
462	    sentence: 0
463	  text: VOTA degrades 14.96pp on weaker model
464	  type: quantitative
465	  evidence:
466	  - exp_id: vota_seed42_v5
467	    metric: accuracy
468	    value: 0.9941
469	  - exp_id: deepseek_vota_seed42
470	    metric: accuracy
471	    value: 0.8445
472	  decisions: []
473	  deprecated: false
474	- id: C126
475	  location:
476	    section: conclusion
477	    paragraph: 0
478	    sentence: 0
479	  text: '17.65pp gap: gradient dilution 26%, information overload 74%'
480	  type: quantitative
481	  evidence:
482	  - exp_id: full_trace_seed42_v5
483	    metric: accuracy
484	    value: 0.8176
485	  - exp_id: full_trace_label_only_seed42
486	    metric: accuracy
487	    value: 0.8622
488	  - exp_id: vota_seed42_v5
489	    metric: accuracy
490	    value: 0.9941
491	  decisions: []
492	  deprecated: false
493	- id: C130
494	  location:
495	    section: conclusion
496	    paragraph: 0
497	    sentence: 0
498	  text: Tier 1 >=99.8%, Tier 2 85.6%, VOTA 99.41%
499	  type: quantitative
500	  evidence:
501	  - exp_id: vota_ae_only_seed42
502	    metric: accuracy
503	    value: 0.9992
504	  - exp_id: vota_exception_only_seed42_v2
505	    metric: accuracy
506	    value: 0.9983
507	  - exp_id: vota_loop_only_seed42
508	    metric: accuracy
509	    value: 0.8563
510	  - exp_id: vota_seed42_v5
511	    metric: accuracy
512	    value: 0.9941
513	  decisions: []
514	  deprecated: false
515	- id: C132
516	  location:
517	    section: experiments
518	    paragraph: 0
519	    sentence: 0
520	  text: Best regex heuristic (B5_format_marker) 99.33% vs SFT exception_only 99.83%,
521	    gap 0.50pp (McNemar p=0.041). B5 exploits format artifact; best non-trivial regex
522	    (B4_exception_type) 93.61%, gap 6.22pp vs SFT.
523	  type: quantitative
524	  evidence:
525	  - exp_id: regex_baseline_analysis
526	    metric: regex_B5_format_marker
527	    value: 0.9933
528	  - exp_id: regex_baseline_analysis
529	    metric: regex_B4_exception_type
530	    value: 0.9361
531	  - exp_id: regex_baseline_analysis
532	    metric: sft_exception_only
533	    value: 0.9983
534	  - exp_id: regex_baseline_analysis
535	    metric: B5_mcnemar_p
536	    value: 0.041
537	  decisions:
538	  - note: B5 is highest accuracy but exploits format marker artifact. B4 is strongest
539	      legitimate regex. Both reported per Director P1 2026-05-16.
540	  deprecated: false
541	- id: C133
542	  location:
543	    section: experiments
544	    paragraph: 0
545	    sentence: 0
546	  text: DebugBench exception_only 100% (426/426), perfect cross-task generalization
547	  type: quantitative
548	  evidence:
549	  - exp_id: debugbench_exception_only_seed42
550	    metric: accuracy
551	    value: 1.0
552	  decisions: []
553	  deprecated: false
554	- id: C134
555	  location:
556	    section: experiments
557	    paragraph: 0
558	    sentence: 0
559	  text: DebugBench VOTA 99.77% (425/426)
560	  type: quantitative
561	  evidence:
562	  - exp_id: debugbench_vota_seed42
563	    metric: accuracy
564	    value: 0.9977
565	  decisions: []
566	  deprecated: false
567	- id: C135
568	  location:
569	    section: experiments
570	    paragraph: 0
571	    sentence: 0
572	  text: DebugBench no_trace 96.71% baseline
573	  type: quantitative
574	  evidence:
575	  - exp_id: debugbench_no_trace_seed42
576	    metric: accuracy
577	    value: 0.9671
578	  decisions: []
579	  deprecated: false
580	- id: C136
581	  location:
582	    section: experiments
583	    paragraph: 0
584	    sentence: 0
585	  text: 'Trace length ablation: 256tok=78.82%, 512tok=80.42%, 1024tok=77.23%, no_limit=81.76%
586	    — non-monotonic, all far below exception_only 99.83%'
587	  type: quantitative
588	  evidence:
589	  - exp_id: full_trace_256tok_seed42
590	    metric: accuracy
591	    value: 0.7882
592	  - exp_id: full_trace_512tok_seed42
593	    metric: accuracy
594	    value: 0.8042
595	  - exp_id: full_trace_1024tok_seed42
596	    metric: accuracy
597	    value: 0.7723
598	  - exp_id: full_trace_seed42_v5
599	    metric: accuracy
600	    value: 0.8176
601	  decisions: []
602	  deprecated: false
603	- id: C137
604	  location:
605	    section: experiments
606	    paragraph: 0
607	    sentence: 0
608	  text: B4 regex achieves 93.61% accuracy (F1=0.876), SFT exception_only 99.83% (F1=0.997),
609	    gap 6.22pp (McNemar p<0.001)
610	  type: quantitative
611	  evidence:
612	  - exp_id: regex_baseline_analysis
613	    metric: regex_B4_exception_type
614	    value: 0.9361
615	  - exp_id: regex_baseline_analysis
616	    metric: regex_B4_f1
617	    value: 0.876
618	  - exp_id: regex_baseline_analysis
619	    metric: sft_exception_only
620	    value: 0.9983
621	  - exp_id: regex_baseline_analysis
622	    metric: sft_exception_only_f1
623	    value: 0.997
624	  decisions:
625	  - note: F1 scores added per Director P1 2026-05-17 regex baseline integration
626	  deprecated: false
627	- id: C138
628	  location:
629	    section: experiments
630	    paragraph: 0
631	    sentence: 0
632	  text: 'SFT outperforms best regex across all formats: +3.62pp (no_trace) to +23.86pp
633	    (VOTA)'
634	  type: quantitative
635	  evidence:
636	  - exp_id: regex_baseline_analysis
637	    metric: no_trace_sft_vs_regex_gap
638	    value: 3.62
639	  - exp_id: regex_baseline_analysis
640	    metric: vota_sft_vs_regex_gap
641	    value: 23.86
642	  decisions:
643	  - note: Cross-format regex comparison added per Director P1 2026-05-17
644	  deprecated: false
645	- id: C139
646	  location:
647	    section: experiments
648	    paragraph: 0
649	    sentence: 0
650	  text: Zero-shot Qwen-7B achieves 89.08% (fail recall 66.96%), below regex 93.61%
651	    and SFT 99.83% (+10.75pp)
652	  type: quantitative
653	  evidence:
654	  - exp_id: zeroshot_qwen7b
655	    metric: accuracy
656	    value: 0.8908
657	  - exp_id: zeroshot_qwen7b
658	    metric: fail_recall
659	    value: 0.6696
660	  - exp_id: regex_baseline_analysis
661	    metric: regex_B4_exception_type
662	    value: 0.9361
663	  - exp_id: vota_exception_only_seed42_v2
664	    metric: accuracy
665	    value: 0.9983
666	  decisions:
667	  - note: Zero-shot baseline added per Director P2 2026-05-17
668	  deprecated: false
669	- id: C140
670	  location:
671	    section: experiments
672	    paragraph: 0
673	    sentence: 0
674	  text: DeepSeek-7B zero-shot 90.59% with aggressive fail recall 94.10%, opposite
675	    bias to Qwen conservative pattern
676	  type: quantitative
677	  evidence:
678	  - exp_id: zeroshot_deepseek7b
679	    metric: accuracy
680	    value: 0.9059
681	  - exp_id: zeroshot_deepseek7b
682	    metric: fail_recall
683	    value: 0.941
684	  decisions:
685	  - note: Cross-model zero-shot comparison per Director P2 2026-05-17
686	  deprecated: false
687	- id: C141
688	  location:
689	    section: discussion
690	    paragraph: 0
691	    sentence: 0
692	  text: Zero-shot 89.08% underperforms regex 93.61% because LLM cannot calibrate caught
693	    vs uncaught exception verdict without task-specific training
694	  type: qualitative
695	  evidence:
696	  - exp_id: zeroshot_qwen7b
697	    metric: accuracy
698	    value: 0.8908
699	  - exp_id: zeroshot_qwen7b
700	    metric: fail_recall
701	    value: 0.6696
702	  - exp_id: zeroshot_deepseek7b
703	    metric: fail_recall
704	    value: 0.941
705	  decisions:
706	  - note: Discussion analysis of zero-shot failure mode per Director P2 2026-05-17
707	  deprecated: false
708	- id: C142
709	  location:
710	    section: experiments
711	    paragraph: 0
712	    sentence: 0
713	  text: Zero-shot spans 51.0-90.6% across 3 families (CL-13B 51.01%, Qwen-7B 89.08%,
714	    DS-6.7B 90.59%), 39.58pp range compressed to <0.56pp by SFT
715	  type: quantitative
716	  evidence:
717	  - exp_id: zeroshot_codellama13b
718	    metric: accuracy
719	    value: 0.5101
720	  - exp_id: zeroshot_qwen7b
721	    metric: accuracy
722	    value: 0.8908
723	  - exp_id: zeroshot_deepseek7b
724	    metric: accuracy
725	    value: 0.9059
726	  decisions:
727	  - note: CodeLlama-13B zero-shot added per Director P3 2026-05-17. Cross-architecture
728	      normalization framing.
729	  deprecated: false
730	- id: C143
731	  location:
732	    section: experiments
733	    paragraph: 0
734	    sentence: 0
735	  text: CodeLlama-13B zero-shot shows extreme fail bias (72.4% predictions are fail),
736	    accuracy 51.01% below majority baseline 71.51%
737	  type: quantitative
738	  evidence:
739	  - exp_id: zeroshot_codellama13b
740	    metric: accuracy
741	    value: 0.5101
742	  - exp_id: zeroshot_codellama13b
743	    metric: fail_prediction_rate
744	    value: 0.724
745	  decisions:
746	  - note: CodeLlama extreme bias per Director P3 2026-05-17
747	  deprecated: false
748	- id: C144
749	  location:
750	    section: experiments
751	    paragraph: 0
752	    sentence: 0
753	  text: 'Zero-shot spans 51.0-93.5% across 4 models (42.44pp range), SFT compresses
754	    to 0.56pp. Qwen-1.5B (93.45%) > Qwen-7B (89.08%): size does not predict zero-shot
755	    performance'
756	  type: quantitative
757	  evidence:
758	  - exp_id: zeroshot_qwen1.5b
759	    metric: accuracy
760	    value: 0.9345
761	  - exp_id: zeroshot_qwen7b
762	    metric: accuracy
763	    value: 0.8908
764	  - exp_id: zeroshot_codellama13b
765	    metric: accuracy
766	    value: 0.5101
767	  - exp_id: zeroshot_deepseek7b
768	    metric: accuracy
769	    value: 0.9059
770	  decisions:
771	  - note: '4-model zero-shot data + 1.5B>7B finding per Director P4 2026-05-17. Framing:
772	      cross-architecture normalization, not scale normalization.'
773	  deprecated: false
774	- id: C145
775	  location:
776	    section: experiments
777	    paragraph: 0
778	    sentence: 0
779	  text: 3-shot Qwen-7B 90.84% (fail recall 80.53%), +1.76pp over zero-shot, -8.99pp
780	    vs SFT
781	  type: quantitative
782	  evidence:
783	  - exp_id: fewshot_3shot_qwen7b
784	    metric: accuracy
785	    value: 0.9084
786	  - exp_id: fewshot_3shot_qwen7b
787	    metric: fail_recall
788	    value: 0.8053
789	  decisions:
790	  - note: Few-shot baseline per Director P4 2026-05-17
791	  deprecated: false
792	- id: C146
793	  location:
794	    section: experiments
795	    paragraph: 0
796	    sentence: 0
797	  text: 'Cross-model tail-2048: Qwen-1.5B 97.90% (gap 1.93pp), DeepSeek-6.7B 94.96%
798	    (gap 4.37pp), positional concentration holds across architectures'
799	  type: quantitative
800	  evidence:
801	  - exp_id: qwen1.5b_tail2048_seed42
802	    metric: accuracy
803	    value: 0.979
804	  - exp_id: deepseek_tail2048_seed42
805	    metric: accuracy
806	    value: 0.9496
807	  decisions:
808	  - note: Cross-model tail-2048 verification per Director P5 2026-05-17
809	  deprecated: false
810	- id: C147
811	  location:
812	    section: appendix
813	    paragraph: 0
814	    sentence: 0
815	  text: ''
816	  type: quantitative
817	  evidence: []
818	  decisions: []
819	  deprecated: false
820	- id: C148
821	  location:
822	    section: appendix
823	    paragraph: 0
824	    sentence: 0
825	  text: ''
826	  type: quantitative
827	  evidence: []
828	  decisions: []
829	  deprecated: false
830	- id: C149
831	  location:
832	    section: appendix
833	    paragraph: 0
834	    sentence: 0
835	  text: ''
836	  type: quantitative
837	  evidence: []
838	  decisions: []
839	  deprecated: false
840	- id: C150
841	  location:
842	    section: appendix
843	    paragraph: 0
844	    sentence: 0
845	  text: ''
846	  type: quantitative
847	  evidence: []
848	  decisions: []
849	  deprecated: false
850	- id: C151
851	  location:
852	    section: appendix
853	    paragraph: 0
854	    sentence: 0
855	  text: ''
856	  type: quantitative
857	  evidence: []
858	  decisions: []
859	  deprecated: false
860	tables:
861	- id: tab:cross_model
862	  location:
863	    section: experiments
864	    table_number: 0
865	  caption: ''
866	  cells:
867	  - row: exception_only
868	    col: Qwen
869	    value: 99.83%
870	    source:
871	      exp_id: vota_exception_only_seed42_v2
872	      metric: accuracy
873	  deprecated: true
874	- id: tab:cross_model
875	  location:
876	    section: experiments
877	    table_number: 0
878	  caption: ''
879	  cells:
880	  - row: exception_only
881	    col: Qwen
882	    value: 99.83%
883	    source:
884	      exp_id: vota_exception_only_seed42_v2
885	      metric: accuracy
886	  - row: exception_only
887	    col: DeepSeek
888	    value: 99.33%
889	    source:
890	      exp_id: deepseek_exception_only_seed42
891	      metric: accuracy
892	  - row: VOTA
893	    col: Qwen
894	    value: 99.41%
895	    source:
896	      exp_id: vota_seed42_v5
897	      metric: accuracy
898	  - row: VOTA
899	    col: DeepSeek
900	    value: 84.45%
901	    source:
902	      exp_id: deepseek_vota_seed42
903	      metric: accuracy
904	  - row: full_trace
905	    col: Qwen
906	    value: 81.76%
907	    source:
908	      exp_id: full_trace_seed42_v5
909	      metric: accuracy
910	  - row: full_trace
911	    col: DeepSeek
912	    value: 79.16%
913	    source:
914	      exp_id: deepseek_full_trace_seed42_v3
915	      metric: accuracy
916	  - row: no_trace
917	    col: Qwen
918	    value: 75.13%
919	    source:
920	      exp_id: no_trace_seed42_v5
921	      metric: accuracy
922	  - row: no_trace
923	    col: DeepSeek
924	    value: 73.36%
925	    source:
926	      exp_id: deepseek_no_trace_seed42
927	      metric: accuracy
928	  deprecated: false
929	- id: tab:ablation
930	  location:
931	    section: experiments
932	    table_number: 0
933	  caption: ''
934	  cells:
935	  - row: ae_only
936	    col: Acc
937	    value: 99.92%
938	    source:
939	      exp_id: vota_ae_only_seed42
940	      metric: accuracy
941	  - row: exception_only
942	    col: Acc
943	    value: 99.83%
944	    source:
945	      exp_id: vota_exception_only_seed42_v2
946	      metric: accuracy
947	  - row: VOTA
948	    col: Acc
949	    value: 99.41%
950	    source:
951	      exp_id: vota_seed42_v5
952	      metric: accuracy
953	  - row: VOTA_no_ae
954	    col: Acc
955	    value: 99.40%
956	    source:
957	      exp_id: vota_no_ae_seed42
958	      metric: accuracy
959	  - row: loop_only
960	    col: Acc
961	    value: 85.63%
962	    source:
963	      exp_id: vota_loop_only_seed42
964	      metric: accuracy
965	  deprecated: false
966	- id: tab:density
967	  location:
968	    section: experiments
969	    table_number: 0
970	  caption: ''
971	  cells:
972	  - row: full_trace
973	    col: Acc
974	    value: 81.76%
975	    source:
976	      exp_id: full_trace_seed42_v5
977	      metric: accuracy
978	  - row: label_only
979	    col: Acc
980	    value: 86.22%
981	    source:
982	      exp_id: full_trace_label_only_seed42
983	      metric: accuracy
984	  - row: VOTA
985	    col: Acc
986	    value: 99.41%
987	    source:
988	      exp_id: vota_seed42_v5
989	      metric: accuracy
990	  deprecated: false
991	- id: tab:calibration
992	  location:
993	    section: experiments
994	    table_number: 0
995	  caption: ''
996	  cells:
997	  - row: ae_only
998	    col: ECE
999	    value: '0.0004'
1000	    source:
1001	      exp_id: calibration_analysis_seed42
1002	      metric: ae_only.ece
1003	  - row: exception_only
1004	    col: ECE
1005	    value: '0.003'
1006	    source:
1007	      exp_id: calibration_analysis_seed42
1008	      metric: exception_only.ece
1009	  - row: no_trace
1010	    col: ECE
1011	    value: '0.172'
1012	    source:
1013	      exp_id: calibration_analysis_seed42
1014	      metric: no_trace.ece
1015	  deprecated: false
1016	- id: tab:regex_baseline
1017	  location:
1018	    section: experiments
1019	    table_number: 0
1020	  caption: Regex/heuristic baselines vs SFT on exception_only test set
1021	  cells:
1022	  - row: B4_exception_type
1023	    col: Acc
1024	    value: 93.61%
1025	    source:
1026	      exp_id: regex_baseline_analysis
1027	      metric: regex_B4_exception_type
1028	  - row: B5_format_marker
1029	    col: Acc
1030	    value: 99.33%
1031	    source:
1032	      exp_id: regex_baseline_analysis
1033	      metric: regex_B5_format_marker
1034	  - row: SFT_exception_only
1035	    col: Acc
1036	    value: 99.83%
1037	    source:
1038	      exp_id: regex_baseline_analysis
1039	      metric: sft_exception_only
1040	  deprecated: false
1041	- id: tab:debugbench
1042	  location:
1043	    section: experiments
1044	    table_number: 0
1045	  caption: DebugBench cross-task generalization
1046	  cells:
1047	  - row: exception_only
1048	    col: Acc
1049	    value: 100.0%
1050	    source:
1051	      exp_id: debugbench_exception_only_seed42
1052	      metric: accuracy
1053	  - row: VOTA
1054	    col: Acc
1055	    value: 99.77%
1056	    source:
1057	      exp_id: debugbench_vota_seed42
1058	      metric: accuracy
1059	  - row: no_trace
1060	    col: Acc
1061	    value: 96.71%
1062	    source:
1063	      exp_id: debugbench_no_trace_seed42
1064	      metric: accuracy
1065	  deprecated: false
1066	- id: tab:trace_length
1067	  location:
1068	    section: experiments
1069	    table_number: 0
1070	  caption: Trace length ablation (full_trace, Qwen-2.5-Coder-7B)
1071	  cells:
1072	  - row: 256tok
1073	    col: Acc
1074	    value: 78.82%
1075	    source:
1076	      exp_id: full_trace_256tok_seed42
1077	      metric: accuracy
1078	  - row: 512tok
1079	    col: Acc
1080	    value: 80.42%
1081	    source:
1082	      exp_id: full_trace_512tok_seed42
1083	      metric: accuracy
1084	  - row: 1024tok
1085	    col: Acc
1086	    value: 77.23%
1087	    source:
1088	      exp_id: full_trace_1024tok_seed42
1089	      metric: accuracy
1090	  - row: no_limit
1091	    col: Acc
1092	    value: 81.76%
1093	    source:
1094	      exp_id: full_trace_seed42_v5
1095	      metric: accuracy
1096	  deprecated: false
1097	figures:
1098	- id: fig2_calibration
1099	  location:
1100	    section: experiments
1101	    figure_number: 0
1102	  caption: Reliability diagrams
1103	  type: reliability_diagram
1104	  source:
1105	    exp_id: calibration_analysis_seed42
1106	  output_path: figures/paper/fig2_calibration.pdf
1107	  deprecated: true
1108	- id: fig2_calibration
1109	  location:
1110	    section: experiments
1111	    figure_number: 0
1112	  caption: Reliability diagrams for 4 trace conditions on Qwen-2.5-7B
1113	  type: reliability_diagram
1114	  source:
1115	    exp_id: calibration_analysis_seed42
1116	  output_path: figures/paper/fig2_calibration.pdf
1117	  deprecated: false
1118	- id: fig3_cross_model_gap
1119	  location:
1120	    section: experiments
1121	    figure_number: 0
1122	  caption: Cross-model accuracy gap bar chart
1123	  type: bar_chart
1124	  source:
1125	    exp_id: cross_model_comparison
1126	  output_path: figures/paper/fig3_cross_model_gap.pdf
1127	  deprecated: false
1128	- id: fig1_trace_overview
1129	  location:
1130	    section: method
1131	    figure_number: 0
1132	  caption: Overview of verdict prediction pipeline with 4 trace conditions
1133	  type: conceptual
1134	  source:
1135	    exp_id: pipeline_overview
1136	  output_path: figures/paper/fig1_trace_overview.pdf
1137	  deprecated: false
1138	_completeness:
1139	  coverage: 44/52
1140	  claims: 49
1141	  tables: 7
1142	  figures: 3
1143	  tier_counts:
1144	    tier1: 0
1145	    tier2: 44
1146	    tier3: 8
1147	    tierX: 0
1148	  last_checked: '2026-05-18T07:19:46.822506+00:00'
1149	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "656139ea-c1e3-415f-9022-9d058082ee5e",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "84e42481-21bb-4fc5-8d5c-ff425aa54e62",
  "sourceToolAssistantUUID": "656139ea-c1e3-415f-9022-9d058082ee5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-18T12:24:47.115Z_

Now I have a thorough understanding of both the dream report paper and the actual paper. Let me also check the imagined experiments to understand what was real vs imagined.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84e42481-21bb-4fc5-8d5c-ff425aa54e62",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2f44W5JewMAhJAeEZa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60e696a8-b6d3-4670-8c7a-dcf77749b9aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrUWqv22XipojuA2r3GjJk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29457,
      "cache_read_input_tokens": 62219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29457,
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

_source line 39 · 2026-05-18T12:24:49.129Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XMRCLE96VcnLBNN2VotGEE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/best/imagined_experiments.yaml",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60e696a8-b6d3-4670-8c7a-dcf77749b9aa",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2f44W5JewMAhJAeEZa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5e2ffba-14c1-4313-85b9-45ad8c29f54f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrUWqv22XipojuA2r3GjJk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29457,
      "cache_read_input_tokens": 62219,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29457
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 156,
          "cache_read_input_tokens": 62219,
          "cache_creation_input_tokens": 29457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29457,
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

_source line 40 · 2026-05-18T12:24:49.134Z_

<details><summary>↩ Tool result · `toolu_01XMRCLE96VcnLBNN2VotGEE`</summary>

```text
1	tier: best
2	narrative_guidance: 'P1 实验全面确认 budget curve universal phase transition。tail-384 ×
3	  4 模型均 ≤81%（与 tail-256 统计等价, McNemar p>0.1），
4	
5	  phase transition 在 384-512 之间是 sharp cliff（gradient ratio 8-10:1）。cross-seed tail-512
6	  全 4 模型 std ≤ 0.9pp，
7	
8	  convergence band 紧密。CodeLlama tail-2048 正常完成（~96.5%），4 模型 budget curve 完整。
9	
10	  论文 5 contributions 清晰闭环: (1) exception dominance universal across 4 models/3 families/2
11	  scales,
12	
13	  (2) 26%/74% causal decomposition, (3) two-tier diagnostic hierarchy,
14	
15	  (4) universal sharp phase transition at ~400 tokens confirming diagnostic signal
16	  locality,
17	
18	  (5) LoRA training stability as practical bottleneck。
19	
20	  Budget curve 作为核心 Figure 展示 ''why exception works''——exception 等价于 trace 末尾 ~400-500
21	  token 的 diagnostic moment，
22	
23	  phase transition 证明这个 moment 的信息高度局部化。''Feature engineering'' 批评被 4-model universality
24	  + phase transition structure 有效反驳：
25	
26	  若只是 feature engineering，不会在 3 个 model family × 2 个 scale 上产生完全一致的 S-curve phase
27	  transition pattern。
28	
29	  EMNLP main 强竞争力（accept prob 0.55-0.75）。
30	
31	  '
32	imagined_experiments:
33	- name: tail-384 × Qwen-7B
34	  plan_id: plan_016
35	  description: Qwen-2.5-Coder-7B full_trace tail-384 tokens SFT，精确定位 256→512 phase
36	    transition 左边界
37	  expected_results:
38	    accuracy: 0.795
39	    accuracy_ci_lower: 0.772
40	    accuracy_ci_upper: 0.818
41	    majority_baseline: 0.7151
42	    lift_over_majority_pp: 8.0
43	    pass_f1: 0.849
44	    fail_f1: 0.682
45	    diff_vs_tail256_pp: 2.0
46	    mcnemar_vs_tail256_p: 0.15
47	    diff_vs_tail512_pp: -14.1
48	  result_rationale: 'Qwen-7B tail-256 = 77.48%。384 tokens 仅多 128 tokens（约 6-8 行代码）。trace
49	    末尾的 diagnostic 信号分布呈高度右偏：
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5e2ffba-14c1-4313-85b9-45ad8c29f54f",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "7d518f1b-ed8c-428b-8612-7e73f5e61e7f",
  "sourceToolAssistantUUID": "b5e2ffba-14c1-4313-85b9-45ad8c29f54f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-18T12:24:52.772Z_

Now I have comprehensive understanding of the paper. Let me now produce the structured review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d518f1b-ed8c-428b-8612-7e73f5e61e7f",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2fqaC3xd4RGqiDfBgx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "304aa833-3f8b-4c7e-941c-92fa05f66fcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6hXxnhCpzw2XK3aS3Eo5a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 991,
      "cache_read_input_tokens": 91676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 991,
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

_source line 42 · 2026-05-18T12:24:53.138Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017KYFvv9NyDP2ePefNmFCpb`</summary>

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
  "parentUuid": "304aa833-3f8b-4c7e-941c-92fa05f66fcb",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2fqaC3xd4RGqiDfBgx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72b74f9b-034e-431e-8cce-05380c691364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6hXxnhCpzw2XK3aS3Eo5a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 991,
      "cache_read_input_tokens": 91676,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 991
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 91676,
          "cache_creation_input_tokens": 991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 991,
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

_source line 43 · 2026-05-18T12:24:53.140Z_

<details><summary>↩ Tool result · `toolu_017KYFvv9NyDP2ePefNmFCpb`</summary>

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
  "parentUuid": "72b74f9b-034e-431e-8cce-05380c691364",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "f1a73f4a-8878-408f-a37a-abc34ef68564",
  "sourceToolAssistantUUID": "72b74f9b-034e-431e-8cce-05380c691364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-18T12:24:57.562Z_



Now I have thoroughly read both versions of the paper (the dream report "best" version and the actual docs/paper version), the review context, the paper provenance, and the project report. Let me produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1a73f4a-8878-408f-a37a-abc34ef68564",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2g8UgoSpZoDHJza3zL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2838f8c-6bbb-4b3e-baff-dfa05725f5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SoCVjrYB2kawknZFNhSdmE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 92667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 685,
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

_source line 45 · 2026-05-18T12:26:26.964Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01NX6KCyqSyuZhbfyH6gNXqY`</summary>

```json
{
  "project": "trace-verdict-study",
  "tier": "best",
  "dream_id": "dream_20260518T113804",
  "overall_score": "Weak Accept (4)",
  "report": "\n# Reviewer 1 (R1): Methods and Experiments\n\n## 1. Summary\n\nThis paper studies which components of execution traces are sufficient for binary pass/fail verdict prediction. Through systematic ablation across four code LLMs (1.5B--13B, three families), the authors find that exception events alone achieve 99.33--99.83% accuracy, dramatically outperforming full traces (81.76%). The paper decomposes the full-trace deficit into information overload (~74%) and gradient dilution (~26%), identifies a two-tier diagnostic hierarchy among trace components, and reports a sharp phase transition at ~400--500 tail tokens. The experimental coverage is extensive and the core finding is convincing, though several methodological concerns limit the strength of the claimed contributions.\n\n## 2. Strengths\n\n- **Comprehensive ablation design.** The paper systematically varies trace components (exception, assertion, loop, combinations, no-trace), truncation direction (head vs. tail), token budgets (256--2048), loss masking, and format markers. This is one of the most thorough ablation studies I have seen for trace-based code tasks. The experimental matrix is well-structured and the conditions are clearly motivated.\n\n- **Multi-model validation.** Testing across four models from three architecture families (Qwen, DeepSeek, CodeLlama) at two scales (1.5B, 6.7B/7B, 13B) substantially strengthens the generalizability claim. The finding that exception-only accuracy is nearly identical (0.56pp range excluding the DeepSeek outlier) across these diverse architectures is compelling.\n\n- **Strong baselines and controls.** The inclusion of regex baselines (6 variants), zero-shot baselines (4 models), few-shot baselines, a format-marker ablation (nomarker), and a label-only loss ablation demonstrates methodological rigor. The regex baselines in particular are valuable for understanding what fraction of the signal is trivially extractable.\n\n- **Transparent reporting of failures.** The paper openly discusses the DeepSeek seed-123 outlier (91.09%), the CodeLlama tail-2048 training failures requiring retraining, the tokenizer-driven truncation confound for DeepSeek VOTA, and the format-marker shortcut (B5 at 99.33%). This honesty strengthens credibility.\n\n- **Statistical methodology.** Paired bootstrap resampling, McNemar's tests, Wilson CIs, ECE/Brier calibration metrics, and cross-seed validation are all appropriate and well-applied. The explicit reporting of p-values for key comparisons is good practice.\n\n- **Irreducible error analysis.** The root-cause analysis of the 2 persistent errors (GeneratorExit false positives from HumanEval/95) is thorough and actionable. The observation that CodeLlama seed 123 achieves 100% demonstrates these are convergence artifacts, not hard limits.\n\n- **DebugBench cross-dataset evaluation.** Testing on an independent dataset with a different fault distribution (synthetic mutations vs. LLM-generated errors) adds generalization evidence beyond the primary benchmark.\n\n## 3. Weaknesses\n\n- **The core finding is arguably unsurprising, and the paper overstates its novelty.** For binary verdict prediction, the presence/absence of an unhandled exception is nearly definitional of pass/fail for the failure modes in these benchmarks (TypeError, ValueError, etc.). The B5 regex baseline achieving 99.33% by detecting a format marker, and B4 achieving 93.61% by matching exception class names, confirms that this is largely a pattern-matching task. The 0.50pp SFT advantage over B5 (p=0.041) is statistically significant but practically marginal. Framing this as five distinct contributions inflates the perceived novelty.\n\n- **Dataset is too small and homogeneous to support the universality claims.** 591 problems from HumanEval + MBPP, with solutions generated by a single model (Qwen-7B-Instruct), is a narrow evaluation setting. The 71.5%/28.5% class imbalance means only ~339 fail samples in the test set. The paper's failure distribution is dominated by standard Python exceptions (TypeError, ValueError, IndexError), which are the easiest failure modes to detect. Silent logic errors (where the program produces wrong output without raising an exception) are acknowledged in the Limitations but represent a critical gap: for such errors, the exception-only approach would be blind. The paper title (\"Exception Events Are All You Need\") overpromises given this limitation.\n\n- **The \"causal decomposition\" claim is not truly causal.** The label-only loss ablation changes two things simultaneously: (1) it eliminates gradient dilution on trace tokens, but (2) it also changes the effective learning rate on the verdict token (since the loss is now concentrated on a single token rather than distributed). The authors acknowledge the decomposition is \"approximate\" and that \"the two factors may interact,\" but still present 26%/74% as a precise causal split. This is a correlational decomposition at best. A truly causal analysis would require controlled interventions that isolate each mechanism independently.\n\n- **Phase transition claim is mechanistically trivial.** The \"sharp phase transition at 384--512 tokens\" is explained by the fact that exception tracebacks are 150--400 tokens long and appear at the trace end. When the tail window is too small to capture the traceback, accuracy is low; when it captures it, accuracy is high. This is not a phase transition in any meaningful physical or information-theoretic sense; it is a truncation artifact. The gradient ratio metric (8.8:1) quantifies the steepness of a step function caused by including vs. excluding the diagnostic signal, which is expected by construction. The universality across models simply confirms that all models can use exception information when it is present and cannot when it is absent.\n\n- **OOD cross-language evaluation (Java/JavaScript) appears to be imagined, not real.** The dream report's review_context.yaml explicitly lists this as an \"imagined experiment\" under plan_021 with approximate (~) accuracy values. The actual paper (docs/paper/) does not contain a cross-language OOD section. If these results are included in the dream-report version of the paper, they should be flagged as fabricated. The actual paper uses DebugBench as its cross-dataset evaluation, which is more credible but remains Python-only.\n\n- **Frontier model comparison (GPT-4o, Claude) is also imagined.** The review_context.yaml shows these as plan_020 imagined experiments with predicted values (GPT-4o 3-shot ~95.1%, Claude 3-shot ~96.1%). The actual paper does not include these comparisons; instead it has real zero-shot and 3-shot results for the four open-source models. The dream paper version includes these numbers with ~ prefixes, which is a red flag. If presented as real results, this is a serious integrity concern.\n\n- **Component ablation is single-model for key conditions.** ae_only and loop_only are evaluated only on Qwen-7B. The paper justifies this as \"targeting the trace composition mechanism rather than cross-model generalization,\" but the two-tier hierarchy is presented as a general finding. Without cross-model validation of loop_only and ae_only, the hierarchy could be Qwen-specific.\n\n- **Test set duplication inflates effective sample size.** The exception_only test set has 48.99% duplicate inputs (607 unique of 1,190). The paper treats all 1,190 as independent Bernoulli trials for CI computation. Under deduplication, the effective test set shrinks substantially and CIs widen (the paper acknowledges Qwen accuracy drops to 99.67% with CI [98.81, 99.91] under n=607). This is not adequately addressed in the main text. The near-identical passing traces (no exception = same input regardless of solution) mean the model is being tested on the same input multiple times.\n\n- **Self-familiarity bias.** Solutions are generated by Qwen-7B-Instruct, which is also one of the evaluation models. While the paper notes this \"does not affect verdict prediction,\" it may affect the pass/fail distribution and error characteristics in ways that favor models from the same family. The Limitations section acknowledges this but it deserves more attention.\n\n- **Missing important baselines.** (1) No comparison with encoder-based models (e.g., CodeBERT, TRACED's approach) on the same task. TRACED is cited as closest prior work but never compared against directly. (2) No comparison with simple MLP/logistic regression on exception features, which would clarify how much of the SFT benefit comes from the LLM architecture vs. the feature itself.\n\n## 4. Questions for Authors\n\n1. What fraction of fail-class samples in your dataset involve silent logic errors (wrong output, no exception raised)? If exception_only achieves 99.83% overall, and the only errors are 2 GeneratorExit FPs, does this mean every fail-class sample with a genuine exception is correctly classified? What is the fail-class recall on silent failures specifically?\n\n2. For the label-only loss ablation: did you control for the effective learning rate on the verdict token? When loss is computed on 1 token vs. ~1000 tokens, the gradient magnitude on the verdict token differs substantially. Did you try adjusting the learning rate to account for this?\n\n3. The DeepSeek seed-123 outlier (91.09%) is attributed to \"LoRA initialization sensitivity,\" but the paper acknowledges \"direct evidence is lacking.\" Have you investigated the specific LoRA weight initialization that caused this? Is it reproducible with the same seed?\n\n4. For the DebugBench evaluation: what is the exception rate among fail-class samples? If DebugBench bugs predominantly raise exceptions (which synthetic mutations often do), then 100% accuracy is expected and does not test the method's limits.\n\n5. The paper claims exception_only > VOTA (p=0.01). But VOTA is a superset of exception_only (it includes exceptions + assertions + loops). Can you explain mechanistically why adding information strictly degrades performance? Is this an attention dilution effect, or is the VOTA formatting introducing confusing tokens?\n\n## 5. Missing Experiments or Analyses\n\n1. **Silent logic error analysis.** Stratify fail-class samples by whether an exception was raised. Report exception_only accuracy on the \"no exception raised but test failed\" subset. This is the critical failure mode for the proposed approach.\n\n2. **Encoder-based baseline.** Compare against TRACED or a fine-tuned CodeBERT/CodeT5 on the same task and data. This contextualizes the contribution relative to the most directly relevant prior work.\n\n3. **Simple classifier baseline.** Train a logistic regression or small MLP on binary features (exception present/absent, exception type one-hot) to quantify how much of the signal is capturable without an LLM.\n\n4. **Larger/real-world dataset.** The 591-problem, single-language benchmark is the main limitation. Even a preliminary evaluation on a larger Python dataset (e.g., CodeContests, APPS) would strengthen claims.\n\n5. **Cross-model loop_only and ae_only.** Extend the component ablation to at least one other model to validate the two-tier hierarchy is not Qwen-specific.\n\n6. **Effect of class balance.** The 71.5/28.5 split means the majority baseline is already 71.5%. How does exception_only perform under more balanced or more extreme class ratios?\n\n## 6. Minor Issues\n\n- The dream report paper version uses em-dashes (400--500) throughout, which is fine for number ranges but should be checked for non-range usage per the writing norms.\n- Table 1 in the dream version has missing F1 values (\"---\") for DeepSeek and CodeLlama, reducing comparability.\n- The \"gradient ratio 8.8:1\" metric is non-standard. It would be clearer to simply report the accuracy deltas and let readers assess the steepness.\n- The paper could benefit from a single consolidated results table rather than spreading results across many small tables.\n- Some numbers differ slightly between the dream paper and the actual paper (e.g., CodeLlama exception_only: 99.83% in dream vs. 99.89% in actual). The review is based primarily on the actual paper.\n\n## 7. Score: 4 (Weak Accept)\n\n**Justification:** The paper presents a thorough and well-executed empirical study. The experimental design is strong: multi-model, multi-seed, with appropriate statistical tests, good baselines, and transparent reporting. The core finding that exception events are sufficient for verdict prediction is convincingly demonstrated within the evaluated setting.\n\nHowever, the contribution is limited by several factors: (1) the finding is partially expected given that verdict prediction on these benchmarks is largely reducible to exception detection (as the 93--99% regex baselines confirm); (2) the dataset is small and homogeneous, with limited failure diversity; (3) the \"causal decomposition\" and \"phase transition\" claims are overclaimed relative to their actual content; (4) the OOD and frontier-model comparisons in the dream version appear to be imagined rather than real; and (5) the absence of silent-logic-error analysis leaves the most important practical limitation unaddressed.\n\nThe paper is above the reject threshold because the ablation methodology is exemplary, the multi-model validation is convincing, and the practical implications (use compact exception signals rather than full traces) are useful for practitioners. It falls short of a clear accept because the intellectual contribution, once stripped of framing inflation, is narrower than the paper suggests.\n\nAt a 25% acceptance rate venue, this is borderline. The execution quality argues for acceptance; the limited novelty and overclaiming argue against.\n\n## 8. Confidence: 4/5\n\nI have substantial expertise in code LLM evaluation, SFT methodology, and execution trace analysis. I am confident in my assessment of the experimental design, statistical methodology, and the distinction between real and imagined results. I am slightly less certain about the broader fault localization literature and whether the findings would generalize to production settings.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2838f8c-6bbb-4b3e-baff-dfa05725f5c1",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2g8UgoSpZoDHJza3zL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9708af93-366b-4fe2-a2cd-937bdbe67ad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SoCVjrYB2kawknZFNhSdmE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 92667,
      "output_tokens": 3480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3480,
          "cache_read_input_tokens": 92667,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 685,
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

_source line 46 · 2026-05-18T12:26:30.312Z_

<details><summary>↩ Tool result · `toolu_01NX6KCyqSyuZhbfyH6gNXqY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/best/review_report.md\", \"dream_id\": \"dream_20260518T113804\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9708af93-366b-4fe2-a2cd-937bdbe67ad3",
  "isSidechain": true,
  "promptId": "52251d33-ecd1-412c-883f-7e082d1e4e2a",
  "agentId": "a6c99a2559f41878a",
  "type": "user",
  "uuid": "78810b6e-3436-4246-b7cf-2be7401c8f5d",
  "sourceToolAssistantUUID": "9708af93-366b-4fe2-a2cd-937bdbe67ad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-18T12:26:40.275Z_

The review has been submitted. Here is a summary of the key findings:

**Score: 4 (Weak Accept) | Confidence: 4/5**

**Core assessment:** The paper presents an exemplary ablation methodology across four models and three architecture families, convincingly demonstrating that exception events alone achieve 99.33--99.83% verdict accuracy. The experimental design is thorough (regex baselines, format-marker ablation, label-only loss ablation, cross-seed validation, DebugBench generalization).

**Main weaknesses identified:**

1. **Limited novelty** -- the core finding that exception presence/absence predicts pass/fail is partially expected, as regex baselines achieve 93--99% on the same task.
2. **Overclaimed contributions** -- the "causal decomposition" is correlational (not truly causal due to confounded effective learning rate), and the "phase transition" is a mechanistically trivial truncation artifact.
3. **Small, homogeneous dataset** -- 591 problems from HumanEval+MBPP with solutions from a single generator model; no evaluation on silent logic errors where exception-only would be blind.
4. **Imagined experiments** -- the OOD cross-language (Java/JavaScript) and frontier model (GPT-4o/Claude) results in the dream paper appear fabricated based on the review_context.yaml, as the actual paper does not contain these experiments.
5. **Test set duplication** -- 49% duplicate inputs in the exception_only test set inflates effective sample size.

**Key missing experiments:** silent logic error stratification, encoder-based baselines (TRACED comparison), simple classifier baseline, and cross-model validation of the two-tier hierarchy beyond Qwen-7B.

Review saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T113804/best/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78810b6e-3436-4246-b7cf-2be7401c8f5d",
  "isSidechain": true,
  "agentId": "a6c99a2559f41878a",
  "requestId": "req_011CbA2oHhGGh7zyaRfZSJTY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6f3c4b0-fb1f-41c0-9314-4a8646f75c1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "dcb29bac-0892-40d8-9a83-9cc5c54535a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NC8xJmgthBYSf3fJ1HRY55",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3609,
      "cache_read_input_tokens": 93352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3609,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
