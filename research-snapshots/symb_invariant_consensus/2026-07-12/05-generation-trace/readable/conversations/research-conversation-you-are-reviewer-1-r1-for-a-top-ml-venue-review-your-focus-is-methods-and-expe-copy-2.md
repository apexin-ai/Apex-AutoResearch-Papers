# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. Review the paper below and

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3261b1309aeb449c.jsonl`
- **Structured JSON:** [`595c312c6c13bfb0a57a.json`](../../sessions/59/595c312c6c13bfb0a57a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-15T07:49:32.673Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. Review the paper below and provide your independent assessment. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target acceptance rate ~25%.

## Paper Summary

**Title:** Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors

The paper proposes Cross-Representation Disagreement Diagnosis (CRD), a framework that generates two executable formalizations of a reasoning problem (FOL+Z3 and Python), detects disagreements, classifies errors into a 4-type taxonomy (logic_error, negation_error, exec_crash, quantifier_error), localizes the faulty representation via stability testing, and optionally performs diagnosis-guided repair.

**Three Claims:**
1. Disagreement as high-precision diagnostic signal: 28–42% disagreement rates, 76–87% diagnostic precision, at 40% token cost of k=5 self-consistency
2. Structured error taxonomy with prescriptive value: 4-type taxonomy stable across models (κ=0.67), taxonomy-guided repair outperforms fixed-strategy by +5.0pp (p=0.042)
3. GT-label-dependent repair effect: helps Unknown (+22.1pp) and False (+10.4pp), hurts True (−11.2pp). Asymmetry reverses across domains (FOL-favored in logic 5.6:1, Code-favored in math 1.8:1)

## Experiments Conducted (from paper)

### Primary (FOLIO, n=204, Qwen3-32B):
- Table 1: C1-C5 metrics with bootstrap 95% CI. C2=87.21% [81.3, 94.7], C4=+4.65pp n.s.
- Table 2: Error taxonomy distribution (logic_error 25.5%, negation_error 10.8%, exec_crash 5.4%, quantifier_error 2.0%)
- Table 3: GT-label-stratified repair (True −13.6pp, False +6.7pp, Unknown +14.7pp)
- Table 4: Multi-round repair (Unknown improves from +14.7 to +22.1pp over 3 rounds)
- Table 5: Repair success by error type (exec_crash 81.8% easiest, quantifier_error 50% hardest)

### Cross-model (Table 6): 
- Qwen within: C2=87.2%, DeepSeek within: C2=83.5%, Cross-model: C2=80.9%. All FOL-favored.

### Cross-benchmark:
- Table 7: LogiQA (n=200): C1=34.0%, C2=81.5%, asymmetry 3.2:1 FOL
- Table 8: ProofWriter pilot (n=30): 6.7% disagree, FAIL → switch
- Table 9: MATH Level 5 (n=200): C1=28.5%, C2=76.0%, asymmetry **reversed** to 1.8:1 Code-favored
- Table 10: Asymmetry direction across domains

### Ablations:
- Table 11: Correlated failure analysis (false agreement 12.3%, phi=0.189)
- Table 12: Selection vs Repair on GT≠True (Selection +11.3pp, Repair +3.5pp additional)
- Table 13: Taxonomy-guided vs fixed-strategy (+5.0pp, McNemar p=0.042)
- Table 14: Cross-model taxonomy validation (κ=0.67 [0.54, 0.80])
- Table 15: CRD vs SC5 (CRD Pareto-dominates: +4.9pp avg at 0.40 cost)
- Table 16: Model scale ablation (8B: C1=55.4%, C2=74.5%)
- Table 17: Cross-domain boundary (GPQA: C1=22.0%, C2=72.7%)
- Table 18: Statistical significance summary

### Experiment Design Coverage Check
The review_context.yaml lists these imagined experiments:
- exp-001 (FOLIO analysis) ✓ covered
- exp-002 (cross-model ablation) ✓ covered
- exp-003 (ProofWriter/LogiQA) ✓ covered
- exp-004 (MATH Level 5) ✓ covered
- exp-005 (multi-round repair) ✓ covered
- exp-006 (Unknown analysis + correlated failure) ✓ covered
- exp-007 (selection vs repair) ✓ covered
- exp-008 (taxonomy ablation) ✓ covered
- exp-009 (statistical significance) ✓ covered
- exp-010 (Qwen3-8B ablation) ✓ covered
- exp-011 (GPQA Diamond) ✓ covered
- exp-012 (self-consistency baseline) ✓ covered
- exp-013 (taxonomy cross-validation) ✓ covered

All 13 imagined experiments appear covered in the paper.

## Your Review Template

Provide your review in exactly this format:

### R1 Review: Methods & Experiments

**Score:** X/6

**Summary:** (2-3 sentences)

**Strengths:**
- S1: ...
- S2: ...
- S3: ...

**Weaknesses:**
- W1: ...
- W2: ...
- W3: ...

**Questions for Authors:**
- Q1: ...
- Q2: ...

**Minor Issues:**
- ...

**Confidence:** X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "2209ba40-ac3d-439c-ad02-c76a03cb6ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T07:49:32.682Z_

```json
{
  "parentUuid": "2209ba40-ac3d-439c-ad02-c76a03cb6ce5",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
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
  "uuid": "be38730a-fffc-40c2-81fb-271ad8e0e40d",
  "timestamp": "2026-05-15T07:49:32.682Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T07:49:35.370Z_



I need to read the paper and any related project files to provide a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be38730a-fffc-40c2-81fb-271ad8e0e40d",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zFavTVTGvCmNPJpTQ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77148923-3d46-48e2-9da2-f3cce92a471c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W13gwAe7MRvc5n9C3F9ggR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15653,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15653,
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

_source line 4 · 2026-05-15T07:49:36.979Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ARth3r2gNffxVvweqPXyAJ`</summary>

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
  "parentUuid": "77148923-3d46-48e2-9da2-f3cce92a471c",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zFavTVTGvCmNPJpTQ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e914460b-90a4-45f9-af6d-e113c1ba2833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W13gwAe7MRvc5n9C3F9ggR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15653,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15653
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15653,
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

_source line 5 · 2026-05-15T07:49:36.984Z_

<details><summary>↩ Tool result · `toolu_01ARth3r2gNffxVvweqPXyAJ`</summary>

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
  "parentUuid": "e914460b-90a4-45f9-af6d-e113c1ba2833",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "3c22858a-6f2f-4ea3-b6dd-c4b3110a2b16",
  "sourceToolAssistantUUID": "e914460b-90a4-45f9-af6d-e113c1ba2833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T07:49:40.569Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c22858a-6f2f-4ea3-b6dd-c4b3110a2b16",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zFub7ctcbXURJ5rc7w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c796f840-17d9-485d-a95e-0a4affcfc2f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PntJLNPBi221xFiTgKo6dH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-15T07:49:42.104Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AHZXLWLgAk9WhxtuybyvMQ`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c796f840-17d9-485d-a95e-0a4affcfc2f7",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zFub7ctcbXURJ5rc7w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b39a7e1-c344-40b1-8a86-fae0f237c6d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PntJLNPBi221xFiTgKo6dH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-15T07:49:42.121Z_

<details><summary>↩ Tool result · `toolu_01AHZXLWLgAk9WhxtuybyvMQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp_pipeline_004 | v4 truncation detection + thinking-off retry, 204 samples | RUNNING (PID 47964, 127/204, ETA ~08:30 BJT) | All-mode 5/5 PASS @126样本 | — |\\n\\n## 126 样本 C1-C5 指标（evaluate_mvp.py 权威数据）\\n| 指标 | All-mode (N=117) | 阈值 | 状态 | Excl-Unknown (N=75) | 状态 |\\n|------|-----------------|------|------|-------------------|------|\\n| C1 disagree_rate | 35.9% (42/117) | ≥10% | PASS | 34.7% (26/75) | PASS |\\n| C2 diagnostic_rate | 88.1% (37/42) | ≥40% | PASS | 88.5% (23/26) | PASS |\\n| C3 error_types | 3 | ≥2 | PASS | 2 | PASS |\\n| C4 targeted_delta | +7.4pp (T:35/54 B:31/54) | >5pp | PASS | +0.0pp (T:22/35 B:22/35) | FAIL |\\n| C5 localization | 79.2% (19/24) | ≥60% | PASS | 87.5% (14/16) | PASS |\\n\\n## 已完成修复\\n- repair.py: repr_type 动态 prompt（C4 excl-unknown 根因修复）\\n- pipeline.py: streaming JSONL + gc.collect（内存泄漏修复）\\n- pipeline.py: JSON→JSONL in-place 转换（数据损坏 bug 修复）\\n- repair_only.py: repair-only 重跑脚本就绪\\n\\n## 待处理\\n- 等 204 全量完成 → evaluate_mvp.py 最终评估\\n- 204 完成后 → repair_only.py 重跑 repair+eval（用修复后的 prompt）\\n\\n## 近期结论\\n- **mvp_pipeline_004** (success, 127/204): All-mode 5/5 PASS，C4 趋势下滑需关注\\n- **mvp_pipeline_002** (negative): FOL crash 修复但 C4/C5 仍 FAIL\\n- **mvp_pipeline_001** (negative): 首轮 2/5 PASS\\n\\n## 趋势\\n成功 1 / 负向 2 / 失败 0 / 终止 2 / 共 6\\nMVP 指标持续改善: v1(2/5) → v2(2/5) → v4@80(4/5) → v4@126(5/5 all-mode)\\n\\n## 资源状态\\nautodl-rtx6000pro: cuda:0 pipeline (PID 47964) + vLLM serving 运行中\\n\", \"total_chars\": 1517, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b39a7e1-c344-40b1-8a86-fae0f237c6d1",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "ffb18b3d-1f60-43d8-8a1a-e62fab6c51df",
  "sourceToolAssistantUUID": "8b39a7e1-c344-40b1-8a86-fae0f237c6d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T07:49:42.581Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HQTJi2hzVK2Y2MXjLLShR2`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffb18b3d-1f60-43d8-8a1a-e62fab6c51df",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zFub7ctcbXURJ5rc7w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61864544-72ef-44a7-91e3-7a8b62035b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PntJLNPBi221xFiTgKo6dH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 10 · 2026-05-15T07:49:42.598Z_

<details><summary>↩ Tool result · `toolu_01HQTJi2hzVK2Y2MXjLLShR2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/paper_framing.md\", \"content\": \"# Paper Framing — cross_representation_disagreement_diagno\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (10 days)\\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\\n\\n## Core Insight\\nWhen the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This \\\"disagreement as diagnostic\\\" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.\\n\\n## Core Claims (3 条)\\n\\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\\n\\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\\n\\n### Claim 2: Error Classification and Conditional Localization\\nDisagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is 94.6%. The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.\\n\\n**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return \\\"ambiguous\\\" (especially Unknown: 61%). C3=4 error types.\\n\\n**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.\\n\\n**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled \\\"the error.\\\"\\n\\n### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral\\nDiagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:\\n\\n| GT Label | n | Targeted | Blind | Delta | Interpretation |\\n|----------|---|----------|-------|-------|----------------|\\n| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |\\n| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |\\n| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |\\n\\nThis is NOT simply \\\"conditional advantage\\\" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal (\\\"Code disagrees with FOL\\\") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.\\n\\n**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.\\n\\n**Presentation strategy**: \\n1. Report C4 stratified by GT label as the PRIMARY result (table above)\\n2. Aggregate C4 only as context, with explicit caveat about non-significance\\n3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness\\n4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)\\n\\n## Story Spine\\n\\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\\n\\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\\n\\n- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).\\n\\n- **Headline result template**: \\\"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\\\"\\n\\n## Venue Fit\\n\\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n| # | Concern | Response Strategy | Required Experiment |\\n|---|---------|-------------------|---------------------|\\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\\n| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |\\n| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |\\n| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as \\\"cross-representation\\\" is imprecise | Frame MATH domain as \\\"cross-executable-paradigm\\\" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |\\n| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |\\n\", \"total_chars\": 9217, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61864544-72ef-44a7-91e3-7a8b62035b58",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "73e50179-f8a3-41ae-8436-231956fb4f1f",
  "sourceToolAssistantUUID": "61864544-72ef-44a7-91e3-7a8b62035b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T07:49:43.278Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RxJDbD9q8GpwTpggzJ7GyN`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73e50179-f8a3-41ae-8436-231956fb4f1f",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zFub7ctcbXURJ5rc7w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11bf3339-8393-485f-9702-ea5f0d75ab77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PntJLNPBi221xFiTgKo6dH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15653,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 15653,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
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

_source line 12 · 2026-05-15T07:49:43.288Z_

<details><summary>↩ Tool result · `toolu_01RxJDbD9q8GpwTpggzJ7GyN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11bf3339-8393-485f-9702-ea5f0d75ab77",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "470657e9-60ef-4e4b-b9e5-0f2a21108106",
  "sourceToolAssistantUUID": "11bf3339-8393-485f-9702-ea5f0d75ab77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T07:49:47.854Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JAtEp2YEbDeEmykq4j5p6K`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "470657e9-60ef-4e4b-b9e5-0f2a21108106",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zGNMSSDyrvRDotBQuc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbd4dcfe-1c25-4dd5-bea5-32cad50ee4e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkJRQNFeuYUP1G8zriKfjn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 17099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 14 · 2026-05-15T07:49:47.867Z_

<details><summary>↩ Tool result · `toolu_01JAtEp2YEbDeEmykq4j5p6K`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbd4dcfe-1c25-4dd5-bea5-32cad50ee4e6",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "67f2a68c-422b-474a-ad55-a80424eaea12",
  "sourceToolAssistantUUID": "bbd4dcfe-1c25-4dd5-bea5-32cad50ee4e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T07:49:48.799Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SLu6y2wTVRXv8nRPEjsHX6`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67f2a68c-422b-474a-ad55-a80424eaea12",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zGNMSSDyrvRDotBQuc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aaddf99b-570d-4c41-9bf5-8489a7839700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkJRQNFeuYUP1G8zriKfjn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 17099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 16 · 2026-05-15T07:49:48.810Z_

<details><summary>↩ Tool result · `toolu_01SLu6y2wTVRXv8nRPEjsHX6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/decisions.yaml\", \"content\": \"_next_id: 14\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:22 UTC\\n  summary: MVP 方案：FOLIO + Qwen3-32B + FOL/Python 双表征验证分歧诊断假设\\n  rationale: 选择 FOLIO 因为：(1) 逻辑推理任务天然适合 FOL+Z3 表征，同时也可写 Python 约束代码，双路径互补性最强；(2) 数据集较小（~200条），MVP\\n    成本低；(3) 已有 ground truth label，可直接评估诊断准确性。选择 Qwen3-32B thinking mode 因为：(1) IDEA_BRIEF\\n    指定的主模型；(2) Apache 2.0 开源；(3) Qwen Cloud API 价格低（$0.08/M input）。Pass/fail 标准：分歧率≥10%、诊断信息量≥40%、≥2种错误类型、定向修复>盲目重生成。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:25 UTC\\n  summary: 采纳 Reviewer 反馈修订 MVP：增加 Step 0 baseline 门控、C4≥5pp、C5 定位准确率≥60%、灰色区间规则\\n  rationale: Reviewer 指出四个有效问题：(1) C4 无量化阈值可能放行无意义差异→加≥5pp；(2) C1/C2 灰色地带未定义→灰色区间扩展到第二数据集；(3)\\n    Qwen3-32B FOLIO baseline 未知，若>90%错误样本不足→增加 Step 0 前置测试；(4) 错误定位是核心环节但未纳入 MVP→增加\\n    C5 定位准确率≥60%。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:26 UTC\\n  summary: 增加 post-MVP 时间骨架和 MVP fail 应急方案（FOLIO fail→ProofWriter→Qwen3-8B→kill）\\n  rationale: Reviewer 指出 ROADMAP 缺少 MVP 后阶段规划和 fail 应急方案。11 天 DDL 下任何决策延迟代价极高。时间骨架仅为粗粒度分配（不是详细研究规划），fail\\n    路径按成本递增排列：换数据集(低成本)→换模型(中成本)→kill(止损)。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 05:28 UTC\\n  summary: 回退 qwen3.6-plus → 要求 Qwen3-32B 或同级开源模型，Reviewer critical 判定\\n  rationale: Reviewer 指出两个 critical 问题：(1) qwen3.6-plus 是闭源 API 模型，EMNLP 要求可复现性；(2)\\n    模型能力远超 Qwen3-32B（GPQA Diamond 88% vs 66.8%），FOLIO baseline 可能>90%导致错误样本不足，headroom\\n    story 不成立。Agent 无权自行做核心方法论变更（模型选择是 IDEA_BRIEF 设计决策），必须上报 Director。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D005\\n  date: 2026-05-14 08:17 UTC\\n  summary: MVP 第一轮未通过（2/5），根因是 Z3 prompt 质量（78% crash），非假设失败。启动 iteration 2 修复 prompt\\n  rationale: FOL 路径 78% exec_crash 导致真分歧样本极少（4%），修复优势为负（-28pp）。但 baseline 74% 确认 FOLIO\\n    是合适的数据集、headroom 充足。Code 路径 52% accuracy 表明 Python 表征可行。核心问题是 Z3 代码生成质量——加 few-shot\\n    examples + 输出验证预期可大幅降低 crash 率。Day 4 硬截止前有足够时间做 1-2 次 prompt 迭代。\\n  related_experiments:\\n  - exp_id: mvp_baseline_001\\n    role: baseline\\n    result: 74% accuracy, PASS_FOLIO\\n  - exp_id: mvp_pipeline_001\\n    role: mvp_v1\\n    result: NOT PASSED 2/5, FOL 78% crash\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D006\\n  date: 2026-05-14 09:47 UTC\\n  summary: MVP v2 结果：FOL crash 78%→10%、C4/C5 翻转为 PASS，但 Code crash 40% 需修复后迭代 v3\\n  rationale: Few-shot + syntax fix 大幅改善 FOL 侧（accuracy 14%→90%）。C4 从 -28pp 翻转为 +40pp，C5\\n    从 42% 翻转为 100%。新瓶颈是 Python Code 侧 thinking token 泄漏导致 40% crash，压缩了有效双表征样本量。C1=0%\\n    在仅 10 条中不具统计意义，修复 Code crash 后扩大样本是关键。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_002\\n    role: mvp_v2_test10\\n    result: FOL crash 10%, Code crash 40%, C1=0%, C4=+40pp, C5=100%\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 13:07 UTC\\n  summary: 撤回 v5 closed-world 方案，改为 v5b：保持 3-way 输出但改进 prompt 减少 lazy Unknown\\n  rationale: v5 强制 Code 路径 closed-world 2-way 输出，而 FOL 保持 open-world 3-way。FOLIO ~39%\\n    GT=Unknown，导致这些样本上 FOL=Unknown vs Code=False 的人为 disagreement。审稿人会质疑分歧信号有多少来自语义假设差异而非推理错误。正确做法：保持两条路径同一语义基础（都\\n    3-way），通过改进 few-shot 和指令减少\\\"不敢判断就输出 Unknown\\\"的 lazy 行为。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: baseline\\n    result: running, 41/204, Code Unknown rate 46.3%\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 18:03 UTC\\n  summary: repair.py prompt bug 确认为 C4 下降根因，修复后 repair-only 重跑全量 204 样本\\n  rationale: Reviewer 发现 BLIND_REGEN_PROMPT 和 TARGETED_REPAIR_PROMPT 硬编码 \\\"Python script\\\"，FOL(Z3)\\n    修复时给模型矛盾指令，导致 FOL-side targeted repair 50% vs blind 90%（-40pp）。C4 从 +22.6→+7.4\\n    的下降趋势直接由此解释。修复方案：动态 repr_type 替换硬编码，pipeline 完成后对全部 204 样本仅重跑 repair+eval 阶段得到干净可比数据。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: affected\\n    result: C4 All-mode +7.4pp (suppressed by bug), C4 excl-Unknown +0.0pp\\n  depends_on:\\n  - D006\\n  - D007\\n- id: D009\\n  date: 2026-05-15 05:59 UTC\\n  summary: 通过 MVP gate，C4 作为已知弱点进入 research 阶段解决\\n  rationale: All-mode 5/5 PASS（原始+repair后均通过）。核心假设（跨表征分歧→诊断→定位）由 C1(39.6%), C2(86.8%),\\n    C3(3 types), C5(85.4%) 强力支持。C4 技术上通过（+5.2pp > 5pp）但 margin 仅 0.2pp，Excl-Unknown\\n    组 0.0pp，统计上不显著。C4 弱点是 paper framing 问题而非方法论根本缺陷——repair 是下游应用，核心贡献在 diagnosis+localization。Research\\n    阶段需要：(1) 改进 repair 机制拉大 delta，或 (2) reframe paper 弱化 repair claim 聚焦 diagnosis+localization。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: primary\\n    result: All-mode 5/5 PASS, C4 margin 0.2pp\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 06:06 UTC\\n  summary: D008 假设（prompt bug = C4 根因）未获支撑；C4 reframe 为 error-type-conditional advantage\\n  rationale: Reviewer 统计分析：修复前后仅 3/192 次结果翻转（targeted +1, blind +2），blind 改善多于 targeted，C4\\n    delta 反而从 +6.25pp 降到 +5.2pp。C4 aggregate +5.2pp 的 p≈0.23 无统计显著性。但 Unknown 子组 +13.5pp\\n    (T:23/37 vs B:18/37) 显示诊断信号在系统性错误（Code overclaiming）上有效，非 Unknown 组 +0.0pp 显示对随机推理错误无效。C4\\n    弱不是 bug 导致的，是方法论层面的 error-type-dependent 局限。Paper framing Claim 3 已更新：不 claim\\n    aggregate repair superiority，claim conditional advantage + boundary characterization。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: primary\\n    result: C4 aggregate +5.2pp (p≈0.23), Unknown +13.5pp, non-Unknown +0.0pp\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-15 06:15 UTC\\n  summary: 统一指标为 per-sample 计算；Claim 3 更新为 GT-label-dependent 三分效应（Unknown +14.7pp\\n    / False +6.7pp / True -13.6pp）\\n  rationale: Reviewer 发现 evaluate_mvp.py (per-side) 和 deep_analysis.py (per-sample)\\n    两套指标不一致。per-sample 更贴合论文叙事（每个问题一个诊断），选为标准。GT=True 子组发现 targeted repair 反效果 -13.6pp（blind\\n    77.3% vs targeted 63.6%），不只是\\\"无帮助\\\"而是\\\"有害\\\"。Claim 3 从 \\\"conditional advantage\\\" 升级为\\n    \\\"GT-label-dependent three-way split\\\"——这是更有价值的发现。5.6:1 不对称性（非 9:1）已修正到 framing。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: primary\\n    result: GT=True -13.6pp, GT=False +6.7pp, GT=Unknown +14.7pp. Asymmetry 5.6:1.\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-15 06:57 UTC\\n  summary: C5 报告双指标：C5-committed (85.4%, 仅明确预测) + C5-coverage (53.0%, 含 ambiguous=fail)；D009\\n    MVP 判定维持\\n  rationale: evaluate_mvp.py 过滤 ambiguous 预测 → C5=85.4% (35/41)；evaluate_unified.py\\n    不过滤 → C5=53.0% (35/66)。差异根因是 38% 样本 stability test 返回 ambiguous。两个视角都有效：committed\\n    衡量\\\"做了预测时的精度\\\"，coverage 衡量\\\"整体覆盖率\\\"。论文应诚实报告两个数字。D009 MVP 使用 C5-committed，判定维持——localization\\n    的 coverage 局限是已知弱点，不否定核心假设（分歧作为诊断信号）。GT=Unknown C5=35.7% 但 C4=+14.7pp 的悖论说明修复效用来自\\n    disagreement pattern（信息含量）而非 error_side 定位精度——这本身是有价值的发现。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_004\\n    role: primary\\n    result: C5-committed 85.4% (35/41), C5-coverage 53.0% (35/66), ambiguous rate\\n      38%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-15 07:17 UTC\\n  summary: 'Dream #1 三档均 3/6 (borderline/weak reject)，识别 5 个结构性问题，更新 framing+plan\\n    后 re-dream'\\n  rationale: 'Dream dream_20260515T060408 三档评分: Best=3/6 borderline reject, Median=3/6\\n    weak reject, Worst=3/6 borderline reject。未达 \\\"best ≥ weak accept\\\" 门槛。跨三档一致的结构性问题:\\n    (1) Related work 严重不足——缺 self-consistency/LEVER/Faithful CoT/self-debug/multi-agent\\n    debate; (2) 引用不完整; (3) Error taxonomy 未验证; (4) \\\"first systematic study\\\" claim\\n    过强; (5) 缺 self-consistency baseline 对比。已采取行动: paper_framing.md 降低 novelty claim\\n    + 加 R8-R11 reviewer concerns; experiment_plan.yaml 新增 exp-012 (self-consistency\\n    baseline, P0) + exp-013 (taxonomy cross-validation, P1) + exp-007 升 P0。需 re-dream\\n    验证改进效果后才能批准 P0 实验。'\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: 新增 P0 — self-consistency baseline\\n  - exp_id: exp-013\\n    role: 新增 P1 — taxonomy validation\\n  - exp_id: exp-007\\n    role: P1→P0 升级 — selection vs repair\\n  depends_on:\\n  - D009\\n\", \"total_chars\": 7500, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaddf99b-570d-4c41-9bf5-8489a7839700",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "6ce7e4ed-2fb0-487e-a09a-b4b317b0eadb",
  "sourceToolAssistantUUID": "aaddf99b-570d-4c41-9bf5-8489a7839700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T07:49:49.322Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PBS9HW4SkqZi8zVbxLvYYN`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ce7e4ed-2fb0-487e-a09a-b4b317b0eadb",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zGNMSSDyrvRDotBQuc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec68573c-9c27-4c41-b651-073479b04458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkJRQNFeuYUP1G8zriKfjn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 17099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4036,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 18 · 2026-05-15T07:49:49.331Z_

<details><summary>↩ Tool result · `toolu_01PBS9HW4SkqZi8zVbxLvYYN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec68573c-9c27-4c41-b651-073479b04458",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "f0de8f67-7b29-488d-a186-69fb18ea4923",
  "sourceToolAssistantUUID": "ec68573c-9c27-4c41-b651-073479b04458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T07:49:54.642Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Y8zK3LjJQtvUuAYjDKbhUQ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0de8f67-7b29-488d-a186-69fb18ea4923",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zGpL8bAgL2nWBYsaEW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5aca8f6-a117-4794-a5b8-17fa666d6a59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFWXuf442sWugRyhc3zEe7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4953,
      "cache_read_input_tokens": 21135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4953,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 20 · 2026-05-15T07:49:54.683Z_

<details><summary>↩ Tool result · `toolu_01Y8zK3LjJQtvUuAYjDKbhUQ`</summary>

```text
artifacts/dream_reports/dream_20260515T060408/best/paper.tex
artifacts/dream_reports/dream_20260515T060408/median/paper.tex
artifacts/dream_reports/dream_20260515T060408/worst/paper.tex
artifacts/dream_reports/dream_20260515T071730/best/paper.tex
artifacts/dream_reports/dream_20260515T071730/median/paper.tex
artifacts/dream_reports/dream_20260515T071730/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5aca8f6-a117-4794-a5b8-17fa666d6a59",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "185cc442-73a5-47db-868b-f914b1f86217",
  "sourceToolAssistantUUID": "e5aca8f6-a117-4794-a5b8-17fa666d6a59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T07:49:55.567Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Kkf82AiaprKLegUXkV5frP`</summary>

```json
{
  "pattern": "**/paper*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "185cc442-73a5-47db-868b-f914b1f86217",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zGpL8bAgL2nWBYsaEW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df126d50-8c03-49d8-bb72-a68badf09038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFWXuf442sWugRyhc3zEe7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4953,
      "cache_read_input_tokens": 21135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4953,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 22 · 2026-05-15T07:49:55.606Z_

<details><summary>↩ Tool result · `toolu_01Kkf82AiaprKLegUXkV5frP`</summary>

```text
artifacts/dream_reports/dream_20260515T060408/best/paper_framing.md
artifacts/dream_reports/dream_20260515T060408/median/paper_framing.md
artifacts/dream_reports/dream_20260515T060408/worst/paper_framing.md
paper_framing.md
artifacts/dream_reports/dream_20260515T071730/best/paper_framing.md
artifacts/dream_reports/dream_20260515T071730/median/paper_framing.md
artifacts/dream_reports/dream_20260515T071730/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df126d50-8c03-49d8-bb72-a68badf09038",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "da0069be-d7ad-49a6-aa46-bd4d1f482256",
  "sourceToolAssistantUUID": "df126d50-8c03-49d8-bb72-a68badf09038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T07:49:56.025Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GCEv168M9L4zXYhRYDbSaN`</summary>

```json
{
  "project": "cross_representation_disagreement_diagno",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da0069be-d7ad-49a6-aa46-bd4d1f482256",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zGpL8bAgL2nWBYsaEW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1a6a9b2-c748-4c41-8cea-c9748a619f0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFWXuf442sWugRyhc3zEe7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4953,
      "cache_read_input_tokens": 21135,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4953
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 21135,
          "cache_creation_input_tokens": 4953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4953,
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

_source line 24 · 2026-05-15T07:49:56.036Z_

<details><summary>↩ Tool result · `toolu_01GCEv168M9L4zXYhRYDbSaN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'cross_representation_disagreement_diagno'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1a6a9b2-c748-4c41-8cea-c9748a619f0b",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "9cd3d3df-4ee6-4dd0-b9f0-64d9fcd049be",
  "sourceToolAssistantUUID": "e1a6a9b2-c748-4c41-8cea-c9748a619f0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T07:49:58.708Z_

Let me read the most recent dream report paper (the one that would have all the experiments incorporated).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cd3d3df-4ee6-4dd0-b9f0-64d9fcd049be",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zHJvM5Exvu5pRyqQRk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ff34b90-2f3e-4411-b766-f2c1aabdcb87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJy669Ff87nEpUHYcD9wk6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 26088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 807,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 26 · 2026-05-15T07:49:59.438Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KvzXNZ8eAW7rAMQMRfSzVu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ff34b90-2f3e-4411-b766-f2c1aabdcb87",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zHJvM5Exvu5pRyqQRk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62ff8864-b361-45eb-9597-d00e30834e4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJy669Ff87nEpUHYcD9wk6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 26088,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 807
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 26088,
          "cache_creation_input_tokens": 807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 807,
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

_source line 27 · 2026-05-15T07:49:59.898Z_

<details><summary>↩ Tool result · `toolu_01KvzXNZ8eAW7rAMQMRfSzVu`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage[T1]{fontenc}
12	\usepackage[utf8]{inputenc}
13	\usepackage{hyperref}
14	
15	\newcommand{\method}{CRD}
16	\newcommand{\pp}{\,pp}
17	
18	\title{Cross-Representation Disagreement for Diagnosis and Characterization\\of LLM Formalization Errors}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	\begin{abstract}
27	When a large language model formalizes a reasoning problem into two distinct executable representations---first-order logic verified by Z3 and executable Python code---disagreements between their outputs serve as a structured diagnostic signal.
28	We present \emph{Cross-Representation Disagreement} (\method{}), a lightweight inference-time framework that detects formalization errors, classifies them into an empirically motivated taxonomy, and localizes the erroneous representation.
29	On FOLIO (204 samples), \method{} achieves an 87.2\% diagnostic precision among disagreeing samples with 94.6\% localization accuracy on committed predictions, while requiring only 2 LLM calls compared to 5 for self-consistency baselines at comparable detection precision.
30	A 5.6:1 asymmetry in favor of the FOL pathway reveals systematic differences in how LLMs handle formal logic versus imperative code generation.
31	We extend \method{} to LogiQA and MATH Level~5, finding that the diagnostic signal generalizes (72\% and 65\% diagnostic rates, respectively) but attenuates as the formalization bottleneck weakens.
32	Selection based on the diagnosed error side matches repair-based approaches ($p{=}0.72$, McNemar) at zero additional cost, supporting a framing where the primary contribution is the diagnostic analysis itself---error type classification, error-side localization, and paradigm asymmetry characterization---rather than downstream accuracy improvement.
33	\end{abstract}
34	
35	% ============================================================
36	\section{Introduction}
37	
38	Neurosymbolic reasoning pipelines that translate natural language into formal representations suffer from a dominant failure mode: the LLM's formalization step introduces subtle corruptions that downstream solvers faithfully propagate~\cite{pan2023logic,olausson2023linc}.
39	Current approaches either select one representation~\cite{hybrid2024}, verify within a single representation~\cite{vericot2024,roundtrip2026}, or discard disagreeing solutions without further analysis~\cite{liang2024}.
40	None exploit the \emph{pattern} of cross-representation disagreement---which representation failed, what type of error occurred, and what this reveals about the relative reliability of different formalization paradigms.
41	
42	We observe that when the same LLM formalizes a problem into both first-order logic (FOL, verified by Z3) and executable Python code, the resulting disagreements are far from random noise.
43	On FOLIO, 42.2\% of samples produce disagreeing outputs, and 87.2\% of these disagreements are diagnostically informative---at least one pathway produced the correct answer.
44	This diagnostic precision is comparable to 5-sample self-consistency voting (85.0\%) but at 40\% of the cost (2 LLM calls vs.\ 5) and with qualitative advantages that self-consistency fundamentally cannot provide: error type classification, error-side localization, and paradigm asymmetry characterization.
45	
46	Our contributions are:
47	\begin{enumerate}
48	\item We establish cross-representation disagreement as a high-precision diagnostic signal (87.2\% on FOLIO, 72.0\% on LogiQA, 65.0\% on MATH), characterizing its domain boundary: effectiveness correlates with the degree to which formalization is the reasoning bottleneck.
49	\item We develop an empirically motivated error taxonomy (3 stable types, cross-model $\kappa{=}0.54$) and a stability-based localization method achieving 94.6\% accuracy on committed predictions, revealing a 5.6:1 FOL-over-Code asymmetry.
50	\item We demonstrate that simple selection based on diagnosed error side matches diagnosis-guided repair ($p{=}0.72$) at zero additional LLM cost, and that repair exhibits a GT-label-dependent effect: helping for Unknown (+14.7\pp{}) and False (+6.7\pp{}) but hurting for True ($-$13.6\pp{}).
51	\end{enumerate}
52	
53	% ============================================================
54	\section{Related Work}
55	
56	\paragraph{Neurosymbolic reasoning.}
57	Logic-LM~\cite{pan2023logic} and LINC~\cite{olausson2023linc} translate problems to FOL and use symbolic solvers, while Program-of-Thought~\cite{chen2023program} generates executable code.
58	HybridMind~\cite{hybrid2024} and adaptive selection approaches choose one representation per problem but do not exploit disagreement patterns.
59	
60	\paragraph{Self-consistency and ensemble methods.}
61	Self-consistency~\cite{wang2023selfconsistency} samples multiple reasoning paths within a single representation and takes the majority vote.
62	This captures generation variance but not systematic paradigm-level differences.
63	Multi-agent debate~\cite{du2023improving,liang2024encouraging} uses multiple LLM agents but typically within the same representation modality.
64	We show that cross-representation disagreement captures qualitatively different information from within-representation sampling.
65	
66	\paragraph{Verification and refinement.}
67	VeriCoT~\cite{vericot2024}, LEVER~\cite{ni2023lever}, and Faithful CoT~\cite{lyu2023faithful} verify or refine within a single representation.
68	Roundtrip Verification~\cite{roundtrip2026} demonstrated diagnosis-guided repair within one representation on 150 traffic rules.
69	Self-debug~\cite{chen2024teaching} and self-refine~\cite{madaan2024selfrefine} iteratively improve code but lack cross-representation diagnostic signals.
70	
71	\paragraph{Cross-representation filtering.}
72	Liang et al.~\cite{liang2024} proved that CoT--PoT disagreement is informative for filtering incorrect answers but stopped at discarding disagreements.
73	We extend this from a binary filter to a structured diagnostic tool enabling error categorization, localization, and targeted repair.
74	
75	\paragraph{Correlated failures.}
76	Denisov-Blanch et al.~\cite{denisov2026} analyze failure correlation in LLM ensembles.
77	We explicitly quantify correlated failures via $\phi$ coefficients and show that cross-representation disagreement partially decorrelates failure modes ($\phi{=}0.189$ within-model vs.\ $\phi{=}0.14$ cross-model).
78	
79	% ============================================================
80	\section{Method}
81	
82	\subsection{Overview}
83	
84	Given a reasoning problem $q$, \method{} proceeds in five stages:
85	\begin{description}
86	\item[C1 --- Disagreement Detection.]
87	The LLM formalizes $q$ into two executable representations: FOL (verified by Z3) and Python code.
88	If their outputs disagree, the sample is flagged.
89	\item[C2 --- Diagnostic Assessment.]
90	Among disagreeing samples, we assess whether the disagreement is diagnostically informative---i.e., at least one pathway produced the correct answer.
91	\item[C3 --- Error Classification.]
92	A rule-based taxonomy classifies the error into one of three stable categories: \texttt{logic\_error}, \texttt{negation\_error}, or \texttt{formalization\_other} (merging \texttt{quantifier\_error} and \texttt{exec\_crash}).
93	\item[C4 --- Repair / Selection.]
94	The diagnosed error side and type inform either (a) \emph{selection}: directly adopting the answer from the more reliable pathway, or (b) \emph{repair}: prompting the LLM to fix the erroneous representation guided by the diagnosis.
95	\item[C5 --- Localization.]
96	A stability test reruns each pathway with perturbation; the pathway yielding inconsistent outputs is identified as the error side.
97	When the test commits (produces a definitive verdict), localization accuracy reaches 94.6\%.
98	\end{description}
99	
100	\subsection{Representation Pathways}
101	
102	\paragraph{FOL + Z3.}
103	The LLM translates $q$ into first-order logic premises and a conclusion.
104	Z3 determines satisfiability, returning \textsc{True}, \textsc{False}, or \textsc{Unknown}.
105	Z3 provides a formal verification guarantee: if the FOL encoding is correct, the answer is provably correct.
106	
107	\paragraph{Executable Python.}
108	The LLM generates a Python program that encodes the problem's logic and prints its answer.
109	Python execution is deterministic given correct code but offers no formal guarantee on the correctness of the encoding.
110	
111	\paragraph{Cross-executable extension.}
112	For mathematical reasoning (MATH), we instantiate the framework as SymPy (symbolic algebra) versus Python (numerical computation), maintaining the cross-executable-paradigm structure while adapting to a domain where FOL is not applicable.
113	
114	\subsection{Error Taxonomy}
115	
116	We define an empirically motivated taxonomy based on analysis of FOLIO disagreement patterns:
117	
118	\begin{itemize}
119	\item \textbf{logic\_error} (25.5\%): Incorrect logical operators, missing premises, or flawed inference chains in formalization.
120	\item \textbf{negation\_error} (10.8\%): Omitted or incorrectly handled negation during translation.
121	\item \textbf{formalization\_other} (7.4\%): Quantifier scope errors, execution crashes, and other formalization failures.
122	\end{itemize}
123	
124	The taxonomy is validated via cross-model agreement (Qwen3-32B vs.\ DeepSeek V4 Pro), achieving $\kappa{=}0.54$ on the merged 3-type scheme (\S\ref{sec:taxonomy-validation}).
125	
126	\subsection{Paradigm Asymmetry}
127	
128	A key finding is the systematic asymmetry between representation pathways.
129	On FOLIO with Qwen3-32B, FOL produces the correct answer 5.6$\times$ more often than Code among disagreeing samples.
130	This asymmetry is directionally consistent across models and benchmarks but its magnitude is model- and domain-dependent (\S\ref{sec:cross-model}, \S\ref{sec:generalization}).
131	
132	% ============================================================
133	\section{Experimental Setup}
134	
135	\paragraph{Benchmarks.}
136	(1)~\textbf{FOLIO}~\cite{han2022folio}: 204 FOL reasoning problems with 3-valued labels (True/False/Unknown); our primary benchmark.
137	(2)~\textbf{LogiQA}~\cite{liu2021logiqa}: 200 multiple-choice logical reasoning problems; secondary benchmark for generalization.
138	(3)~\textbf{MATH Level~5}~\cite{hendrycks2021math}: 200 competition-level math problems; cross-executable extension using SymPy vs.\ Python.
139	(4)~\textbf{GPQA Diamond}~\cite{rein2024gpqa}: 198 graduate-level science questions; domain boundary test.
140	
141	\paragraph{Models.}
142	Primary: Qwen3-32B.
143	Cross-model ablation: DeepSeek V4 Pro (within-model) and DeepSeek FOL $\times$ Qwen Code (cross-model).
144	Scale ablation: Qwen3-8B.
145	Taxonomy validation: DeepSeek V4 Pro as independent classifier.
146	
147	\paragraph{Metrics.}
148	C1: disagreement rate.
149	C2: diagnostic rate (fraction of disagreements where $\geq$1 pathway is correct).
150	C3: error type distribution.
151	C4: accuracy improvement from repair/selection vs.\ blind baseline.
152	C5: localization accuracy on committed predictions.
153	We report bootstrap 95\% CIs (10{,}000 resamples) and Fisher exact / McNemar tests throughout.
154	
155	\paragraph{Baselines.}
156	(1)~\emph{Blind baseline}: single-pass FOL answer without diagnosis.
157	(2)~\emph{Self-consistency $k{=}5$}: majority vote over 5 FOL-only or 5 Code-only samples.
158	(3)~\emph{Oracle}: always selecting the correct pathway when one exists.
159	
160	% ============================================================
161	\section{Results}
162	
163	\subsection{Main Results on FOLIO}
164	\label{sec:main-results}
165	
166	Table~\ref{tab:main} summarizes \method{}'s diagnostic performance on FOLIO.
167	
168	\begin{table}[t]
169	\centering
170	\small
171	\begin{tabular}{lcc}
172	\toprule
173	\textbf{Metric} & \textbf{Value} & \textbf{95\% CI} \\
174	\midrule
175	C1: Disagree Rate & 42.2\% & [35.3, 49.0] \\
176	C2: Diagnostic Rate & 87.2\% & [81.3, 94.7] \\
177	C5: Committed Acc. & 94.6\% & [86.1, 100] \\
178	C5: Coverage & 53.0\% & --- \\
179	Asymmetry (FOL:Code) & 5.6:1 & --- \\
180	$\phi$ coefficient & 0.189 & --- \\
181	\bottomrule
182	\end{tabular}
183	\caption{CRD diagnostic metrics on FOLIO ($n{=}204$, Qwen3-32B). C2 and C5 are conditioned on disagreeing samples. All metrics except C4 are significant after Bonferroni correction ($p{<}0.004$).}
184	\label{tab:main}
185	\end{table}
186	
187	Among the 86 disagreeing samples, 75 (87.2\%) contain at least one correct pathway.
188	The stability-based localization test commits on 53\% of diagnostic cases, achieving 94.6\% accuracy---when the test produces a definitive verdict, it is almost always correct.
189	The remaining 47\% are returned as ``ambiguous,'' driven primarily by GT=Unknown samples (61\% ambiguous rate) where Code's tendency to overclaim creates systematically unstable predictions.
190	
191	\subsection{CRD vs.\ Self-Consistency}
192	\label{sec:sc-comparison}
193	
194	Table~\ref{tab:sc} compares \method{} with $k{=}5$ self-consistency voting.
195	
196	\begin{table}[t]
197	\centering
198	\small
199	\begin{tabular}{lcccl}
200	\toprule
201	\textbf{Benchmark} & \textbf{SC5-Best} & \textbf{CRD} & $\boldsymbol{\Delta}$ & \textbf{Cost} \\
202	\midrule
203	FOLIO & 85.0\% & 87.2\% & +2.2\pp{} & 0.40$\times$ \\
204	LogiQA & 76.0\% & 72.0\% & $-$4.0\pp{} & 0.38$\times$ \\
205	MATH & 74.0\% & 65.0\% & $-$9.0\pp{} & 0.35$\times$ \\
206	\bottomrule
207	\end{tabular}
208	\caption{Detection precision: CRD (2 calls) vs.\ best self-consistency baseline (5 calls). CRD cost ratio is relative to SC5.}
209	\label{tab:sc}
210	\end{table}
211	
212	On FOLIO, \method{} achieves slightly higher detection precision (+2.2\pp{}) at 40\% of the cost.
213	On LogiQA and MATH, precision is lower ($-$4.0\pp{} and $-$9.0\pp{}, respectively), reflecting the attenuated diagnostic signal when formalization is less of a bottleneck.
214	Critically, \method{} provides structured diagnostic information that self-consistency cannot: error type classification (3--4 types), error-side localization (C5: 82--95\% accuracy), and paradigm asymmetry characterization.
215	Self-consistency reveals \emph{that} something may be wrong; \method{} reveals \emph{why}.
216	
217	\subsection{Selection vs.\ Repair}
218	\label{sec:selection-repair}
219	
220	Table~\ref{tab:sel-rep} compares selection (adopting the answer from the diagnosed correct side) with diagnosis-guided repair.
221	
222	\begin{table}[t]
223	\centering
224	\small
225	\begin{tabular}{lccc}
226	\toprule
227	\textbf{Method} & \textbf{Accuracy} & \textbf{Extra Calls} & \textbf{vs.\ Blind} \\
228	\midrule
229	Blind baseline & 81.4\% & 0 & --- \\
230	Selection (ours) & 82.8\% & 0 & +1.4\pp{} \\
231	Repair (ours) & 83.8\% & ${\sim}$2/sample & +2.4\pp{} \\
232	Oracle & 87.8\% & --- & +6.4\pp{} \\
233	\bottomrule
234	\end{tabular}
235	\caption{Selection vs.\ repair on FOLIO. McNemar $p{=}0.72$; the difference is not significant.}
236	\label{tab:sel-rep}
237	\end{table}
238	
239	Selection nearly matches repair (82.8\% vs.\ 83.8\%, McNemar $p{=}0.72$) at zero additional LLM cost.
240	The oracle upper bound (87.8\%) indicates 5.0\pp{} headroom from perfect localization.
241	
242	Stratified by ground-truth label (Table~\ref{tab:sel-rep-gt}), selection outperforms repair on GT=True (+2.8\pp{}) by avoiding overcorrection, while repair excels on GT=Unknown ($-$4.3\pp{} in favor of repair) where generating a better answer from the disagreement pattern is beneficial.
243	
244	\begin{table}[t]
245	\centering
246	\small
247	\begin{tabular}{lccr}
248	\toprule
249	\textbf{GT Label} & \textbf{Selection} & \textbf{Repair} & $\boldsymbol{\Delta}$ \\
250	\midrule
251	True & 79.2\% & 76.4\% & +2.8\pp{} \\
252	False & 81.0\% & 82.5\% & $-$1.5\pp{} \\
253	Unknown & 81.2\% & 85.5\% & $-$4.3\pp{} \\
254	\bottomrule
255	\end{tabular}
256	\caption{Selection vs.\ repair by GT label on FOLIO.}
257	\label{tab:sel-rep-gt}
258	\end{table}
259	
260	\subsection{Repair Analysis}
261	\label{sec:repair}
262	
263	Though repair is not our primary contribution, we analyze its behavior to characterize the boundary of diagnosis-guided correction.
264	
265	\paragraph{GT-label-dependent effects.}
266	Repair exhibits a striking three-way pattern (Table~\ref{tab:repair-gt}): it helps substantially for GT=Unknown (+14.7\pp{} in Round~1), modestly for GT=False (+6.7\pp{}), and actively \emph{hurts} for GT=True ($-$13.6\pp{}).
267	The mechanism: when Code incorrectly outputs False or Unknown for a True problem, the diagnostic signal triggers overcorrection---the repair prompt leads the model to change the (correct) FOL answer.
268	
269	\begin{table}[t]
270	\centering
271	\small
272	\begin{tabular}{lcccc}
273	\toprule
274	\textbf{Round} & \textbf{Aggregate} & \textbf{GT=True} & \textbf{GT=False} & \textbf{GT=Unk.} \\
275	\midrule
276	Round 1 & +4.65\pp{} & $-$13.6\pp{} & +6.7\pp{} & +14.7\pp{} \\
277	Round 2 & +6.2\pp{} & $-$12.3\pp{} & +7.8\pp{} & +14.2\pp{} \\
278	Round 3 & +6.8\pp{} & $-$11.5\pp{} & +8.2\pp{} & +13.0\pp{} \\
279	\bottomrule
280	\end{tabular}
281	\caption{Multi-round repair results on FOLIO. Aggregate C4 is not significant (Fisher $p{=}0.626$ for Round~1). Diminishing returns are evident after Round~1.}
282	\label{tab:repair-gt}
283	\end{table}
284	
285	\paragraph{Multi-round repair.}
286	Additional repair rounds yield diminishing returns: Round~1$\to$2 adds +1.55\pp{} aggregate, Round~2$\to$3 adds only +0.6\pp{}.
287	GT=True overcorrection improves from $-$13.6\pp{} to $-$11.5\pp{} but remains a structural limitation.
288	
289	\paragraph{Error-type-specific repair.}
290	Taxonomy-guided repair (dispatching repair strategy by error type) achieves 84.5\% vs.\ 83.8\% for fixed-strategy repair ($\Delta{=}{+}0.7\pp{}$, McNemar $p{=}0.68$; Table~\ref{tab:taxonomy-repair}).
291	The taxonomy's value is primarily descriptive (understanding error distributions) rather than prescriptive (guiding repair strategies).
292	
293	\begin{table}[t]
294	\centering
295	\small
296	\begin{tabular}{lcccc}
297	\toprule
298	\textbf{Error Type} & $n$ & \textbf{Guided} & \textbf{Fixed} & $\boldsymbol{\Delta}$ \\
299	\midrule
300	logic\_error & 52 & 87\% & 85\% & +2\pp{} \\
301	negation\_error & 22 & 86\% & 82\% & +4\pp{} \\
302	exec\_crash & 11 & 91\% & 91\% & 0\pp{} \\
303	quantifier\_error & 4 & 75\% & 75\% & 0\pp{} \\
304	\midrule
305	Overall & 89 & 84.5\% & 83.8\% & +0.7\pp{} \\
306	\bottomrule
307	\end{tabular}
308	\caption{Taxonomy-guided vs.\ fixed-strategy repair. McNemar $p{=}0.68$.}
309	\label{tab:taxonomy-repair}
310	\end{table}
311	
312	\subsection{Unknown Sample Analysis and Correlated Failures}
313	\label{sec:unknown}
314	
315	GT=Unknown samples exhibit a paradox: the highest false agreement rate (26.1\%) yet the highest repair delta (+14.7\pp{}).
316	Table~\ref{tab:unknown} reveals the mechanism: Code outputs \textsc{True} or \textsc{False} for 72.5\% of GT=Unknown samples (overclaiming), while FOL correctly returns \textsc{Unknown} 41\% of the time.
317	This systematic Code overclaiming creates detectable disagreements that are highly actionable.
318	
319	\begin{table}[t]
320	\centering
321	\small
322	\begin{tabular}{lcc}
323	\toprule
324	\textbf{Code Output (GT=Unk.)} & \textbf{Count} & \textbf{Rate} \\
325	\midrule
326	True (overclaim) & 28 & 40.6\% \\
327	False (overclaim) & 22 & 31.9\% \\
328	Unknown (correct) & 14 & 20.3\% \\
329	Crash & 5 & 7.2\% \\
330	\bottomrule
331	\end{tabular}
332	\caption{Code pathway outputs on GT=Unknown samples ($n{=}69$). Python execution lacks native \textsc{Unknown} semantics, leading to overclaiming in 72.5\% of cases.}
333	\label{tab:unknown}
334	\end{table}
335	
336	Failure correlation ($\phi$ coefficient) varies by GT label: $\phi{=}0.12$ (True), $\phi{=}0.18$ (False), $\phi{=}0.31$ (Unknown).
337	Higher correlation on Unknown samples reflects shared difficulty from specification ambiguity, but the differing \emph{failure modes} (FOL returns Unknown; Code guesses) make the disagreement diagnostically valuable.
338	
339	We further distinguish specification-level errors (12.3\% of all samples), where the problem itself is ambiguous enough that both representations produce reasonable but different formalizations, from formalization-specific errors (36.8\%), where one representation introduces a clear bug.
340	Repair is effective for the latter (+7.8\pp{}) but not the former (+1.2\pp{}), delineating the method's actionable boundary.
341	
342	\subsection{Cross-Model Ablation}
343	\label{sec:cross-model}
344	
345	To test whether the diagnostic signal depends on a specific model, we compare three conditions on FOLIO (Table~\ref{tab:cross-model}).
346	
347	\begin{table}[t]
348	\centering
349	\small
350	\begin{tabular}{lcccc}
351	\toprule
352	\textbf{Condition} & \textbf{C1} & \textbf{C2} & \textbf{Asym.} & $\boldsymbol{\phi}$ \\
353	\midrule
354	Qwen3-32B (within) & 42.2\% & 87.2\% & 5.6:1 & 0.189 \\
355	DeepSeek V4 (within) & 35.0\% & 74.0\% & 2.5:1 & 0.280 \\
356	DeepSeek$\times$Qwen (cross) & 48.0\% & 78.0\% & 3.2:1 & 0.140 \\
357	\bottomrule
358	\end{tabular}
359	\caption{Cross-model ablation on FOLIO ($n{=}204$). Asymmetry direction (FOL$>$Code) is consistent across all conditions.}
360	\label{tab:cross-model}
361	\end{table}
362	
363	The asymmetry direction is consistent across all three conditions: FOL outperforms Code by 5.6:1, 2.5:1, and 3.2:1.
364	This supports the interpretation that the signal reflects representation-level differences rather than model-specific artifacts.
365	However, the effect magnitude is model-dependent---DeepSeek V4 Pro's stronger Code generation compresses the asymmetry from 5.6:1 to 2.5:1.
366	
367	The cross-model condition reduces failure correlation ($\phi{=}0.14$ vs.\ 0.189 within-model), providing partial evidence that using different models for each pathway decorrelates failures, though the reduction is modest.
368	Jaccard failure overlap of 0.42 indicates substantial shared specification-level failure patterns remain.
369	
370	\subsection{Generalization across Benchmarks}
371	\label{sec:generalization}
372	
373	\paragraph{ProofWriter pilot failure.}
374	We first piloted on ProofWriter ($n{=}30$), a synthetic dataset with fully formalized premises.
375	The disagree rate was only 6.7\% (below our 10\% threshold), with baseline accuracy of 93.3\%.
376	This confirms that \method{} provides limited value when both representations are already highly accurate---the method's utility requires formalization to be the bottleneck.
377	
378	\paragraph{LogiQA.}
379	On 200 LogiQA multiple-choice problems (Table~\ref{tab:generalization}), \method{} achieves C1=22.0\% and C2=72.0\% [CI: 63--81\%].
380	The lower disagreement rate reflects LogiQA's multiple-choice format (smaller error surface).
381	Asymmetry compresses to 3.8:1 as the logical structure is less pure than FOLIO.
382	C4 is +3.5\pp{} (Fisher $p{=}0.42$, not significant).
383	
384	\paragraph{MATH Level 5.}
385	On 200 competition math problems using SymPy (symbolic) vs.\ Python (numerical), C1=15.5\% and C2=65.0\% [CI: 53--76\%].
386	The asymmetry drops to 1.8:1 ($p{=}0.18$, not significant)---the critical weakness for this domain.
387	Unlike FOL+Z3 vs.\ Python (where Z3 provides formal verification guarantees), SymPy and Python offer no fundamental verification gap, flattening the asymmetry.
388	Error types require domain adaptation: \texttt{symbolic\_algebra\_error} (8.5\%), \texttt{numerical\_precision\_error} (4.0\%), \texttt{exec\_crash} (3.0\%).
389	
390	\begin{table}[t]
391	\centering
392	\small
393	\begin{tabular}{lcccc}
394	\toprule
395	\textbf{Metric} & \textbf{FOLIO} & \textbf{LogiQA} & \textbf{MATH} & \textbf{GPQA} \\
396	\midrule
397	$n$ & 204 & 200 & 200 & 198 \\
398	C1 & 42.2\% & 22.0\% & 15.5\% & 12.0\% \\
399	C2 & 87.2\% & 72.0\% & 65.0\% & 58.0\% \\
400	Asymmetry & 5.6:1 & 3.8:1 & 1.8:1 & 1.4:1 \\
401	C5 Committed & 94.6\% & 84.0\% & 82.0\% & 75.0\% \\
402	C4 $\Delta$ & +4.65\pp{} & +3.5\pp{} & +2.8\pp{} & +1.0\pp{} \\
403	\bottomrule
404	\end{tabular}
405	\caption{CRD metrics across benchmarks. GPQA is a boundary case included for completeness. All C4 values are not statistically significant.}
406	\label{tab:generalization}
407	\end{table}
408	
409	\paragraph{GPQA Diamond.}
410	GPQA represents the method's domain boundary: C1=12.0\%, C2=58.0\%, asymmetry 1.4:1.
411	Knowledge-intensive science reasoning has its bottleneck in domain knowledge, not formalization---cross-representation disagreement provides limited diagnostic value.
412	
413	\subsection{Error Taxonomy Validation}
414	\label{sec:taxonomy-validation}
415	
416	We validate the error taxonomy by having DeepSeek V4 Pro independently classify the same 86 FOLIO disagreement samples (Table~\ref{tab:taxonomy}).
417	
418	\begin{table}[t]
419	\centering
420	\small
421	\begin{tabular}{lcccr}
422	\toprule
423	\textbf{Error Type} & \textbf{Qwen} & \textbf{DeepSeek} & $\boldsymbol{\kappa}$ & \textbf{Agree.} \\
424	\midrule
425	logic\_error & 25.5\% & 27.1\% & 0.58 & 78\% \\
426	negation\_error & 10.8\% & 9.3\% & 0.51 & 73\% \\
427	quantifier\_error & 2.0\% & 4.7\% & 0.22 & 65\% \\
428	exec\_crash & 5.4\% & 4.7\% & 0.82 & 95\% \\
429	\midrule
430	Overall (4 types) & --- & --- & 0.43 & --- \\
431	Overall (3 types) & --- & --- & 0.54 & --- \\
432	\bottomrule
433	\end{tabular}
434	\caption{Cross-model taxonomy agreement on FOLIO ($n{=}86$). The 3-type scheme merges quantifier\_error and exec\_crash into formalization\_other.}
435	\label{tab:taxonomy}
436	\end{table}
437	
438	With the original 4-type taxonomy, $\kappa{=}0.43$ (moderate agreement).
439	Merging \texttt{quantifier\_error} (low frequency, ambiguous definition, $\kappa{=}0.22$) and \texttt{exec\_crash} into \texttt{formalization\_other} yields $\kappa{=}0.54$, reaching moderate-to-fair agreement.
440	The main categories---\texttt{logic\_error} ($\kappa{=}0.58$) and \texttt{negation\_error} ($\kappa{=}0.51$)---are reasonably stable.
441	\texttt{exec\_crash} achieves near-perfect agreement ($\kappa{=}0.82$) as crashes are objectively verifiable.
442	
443	An LLM-as-proxy evaluation on 50 samples achieved $\kappa{=}0.61$ (vs.\ Qwen) and $\kappa{=}0.57$ (vs.\ DeepSeek), suggesting the categories capture meaningful distinctions.
444	The error type distributions do not differ significantly between models ($\chi^2$ test, $p{=}0.12$).
445	
446	\subsection{Statistical Significance}
447	\label{sec:stats}
448	
449	Table~\ref{tab:stats} summarizes significance testing across all benchmarks.
450	
451	\begin{table}[t]
452	\centering
453	\small
454	\begin{tabular}{lcccc}
455	\toprule
456	\textbf{Metric} & \textbf{FOLIO} & \textbf{LogiQA} & \textbf{MATH} & \textbf{All Sig.?} \\
457	\midrule
458	C1 (vs.\ 0\%) & $p{<}.001$ & $p{<}.001$ & $p{<}.001$ & Yes \\
459	C2 (vs.\ 50\%) & $p{<}.001$ & $p{=}.002$ & $p{=}.018$ & Yes \\
460	C4 (Fisher) & $p{=}.626$ & $p{=}.42$ & $p{=}.58$ & No \\
461	C5 (vs.\ 50\%) & $p{<}.001$ & $p{=}.003$ & $p{=}.008$ & Yes \\
462	\bottomrule
463	\end{tabular}
464	\caption{Statistical significance summary. All tests remain significant after Bonferroni correction (12 tests, threshold $p{<}0.004$) except C4, which is not significant on any benchmark.}
465	\label{tab:stats}
466	\end{table}
467	
468	The diagnostic metrics (C1, C2, C5) are robustly significant across all three benchmarks, surviving Bonferroni correction.
469	C4 (repair improvement) is consistently non-significant---the smallest $p$-value is 0.42 (LogiQA)---with bootstrap CIs including zero on every benchmark (e.g., FOLIO: [$-$8.8, +18.1]).
470	This supports our framing: the contribution is the diagnostic analysis, not aggregate accuracy improvement.
471	
472	\subsection{Model Scale Ablation}
473	
474	Running \method{} with Qwen3-8B on FOLIO reveals an instructive pattern: disagreement rate \emph{increases} to 55.0\% (+12.8\pp{}) while diagnostic rate \emph{decreases} to 68.0\% ($-$19.2\pp{}).
475	The 8B model's weaker formalization produces more frequent but less informative disagreements---more ``both wrong'' cases.
476	Asymmetry compresses to 2.8:1 as the FOL pathway degrades faster than Code (formal logic requires more precise generation capability).
477	This confirms that \method{}'s effectiveness scales with model capability: more disagreement does not equal better diagnosis.
478	
479	% ============================================================
480	\section{Discussion}
481	
482	\paragraph{When does CRD work?}
483	Our results trace a clear effectiveness gradient: FOLIO (87.2\% C2) $>$ LogiQA (72.0\%) $>$ MATH (65.0\%) $>$ GPQA (58.0\%).
484	This gradient correlates with the degree to which formalization is the reasoning bottleneck.
485	When the LLM's primary challenge is translating natural language into formal representations (FOLIO), cross-representation disagreement is highly diagnostic.
486	When the challenge shifts to domain knowledge (GPQA) or when both representations lack fundamental verification gaps (MATH), the signal attenuates.
487	
488	\paragraph{Cost-efficiency argument.}
489	\method{} requires exactly 2 LLM calls per sample (one FOL, one Code).
490	Self-consistency with $k{=}5$ requires 5 calls.
491	On FOLIO, \method{} achieves comparable detection precision (+2.2\pp{}) at 40\% cost while additionally providing error type classification, error-side localization, and paradigm asymmetry characterization.
492	Even on benchmarks where \method{} has lower precision than SC5 (LogiQA: $-$4\pp{}, MATH: $-$9\pp{}), the structured diagnostic information has no self-consistency equivalent.
493	
494	\paragraph{Repair is not the point.}
495	The consistently non-significant C4 across all benchmarks could be seen as a weakness.
496	We argue it is a feature of our framing: if simple selection (0 additional calls) matches repair ($p{=}0.72$), the value of \method{} lies in the diagnostic signal itself, not in what one does with it.
497	The GT-label-dependent repair effect (helps Unknown/False, hurts True) is itself a finding that characterizes the boundary of diagnosis-guided correction.
498	
499	\paragraph{Limitations.}
500	(1)~The error taxonomy requires domain adaptation (logic types for FOLIO vs.\ algebraic types for MATH) and achieves only moderate cross-model agreement ($\kappa{=}0.54$).
501	(2)~The MATH asymmetry (1.8:1) is not statistically significant ($p{=}0.18$), limiting the paradigm asymmetry claim to FOL-based domains.
502	(3)~False agreement rates of 5.6--26.1\% represent a hard diagnostic ceiling---correlated failures where both representations appear to agree but are both wrong.
503	(4)~Specification-level errors (12.3\% of FOLIO) are fundamentally unaddressable by our approach.
504	(5)~All experiments use a single primary model family; cross-model validation is limited to two models.
505	
506	% ============================================================
507	\section{Conclusion}
508	
509	We introduced Cross-Representation Disagreement (\method{}), a framework that transforms cross-representation disagreement from a binary filtering signal into a structured diagnostic tool.
510	On FOLIO, \method{} detects formalization errors with 87.2\% diagnostic precision, classifies them into a 3-type taxonomy ($\kappa{=}0.54$), and localizes the error side with 94.6\% committed accuracy---all at 40\% of the cost of self-consistency baselines.
511	The method generalizes to LogiQA and MATH with attenuated but significant diagnostic rates, tracing a clear boundary: effectiveness requires formalization to be the reasoning bottleneck.
512	Rather than claiming accuracy improvement, we contribute the diagnostic analysis itself: understanding \emph{why} LLM formalizations fail, \emph{which} representation is more reliable, and \emph{when} diagnosis helps versus hurts downstream correction.
513	
514	% ============================================================
515	% Placeholder references
516	\begin{thebibliography}{25}
517	
518	\bibitem[Pan et al.(2023)]{pan2023logic}
519	Liangming Pan, Alon Albalak, Xinyi Wang, and William Yang Wang. 2023.
520	Logic-LM: Empowering large language models with symbolic solvers for faithful logical reasoning.
521	In \emph{Findings of EMNLP}.
522	
523	\bibitem[Olausson et al.(2023)]{olausson2023linc}
524	Theo X. Olausson, Alex Gu, Ben Lipkin, Cedegao E. Zhang, Armando Solar-Lezama, Joshua B. Tenenbaum, and Roger Levy. 2023.
525	LINC: A neurosymbolic approach for logical reasoning by combining language models with first-order logic provers.
526	In \emph{Proc. EMNLP}.
527	
528	\bibitem[Chen et al.(2023)]{chen2023program}
529	Wenhu Chen, Xueguang Ma, Xinyi Wang, and William W. Cohen. 2023.
530	Program of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks.
531	\emph{TMLR}.
532	
533	\bibitem[HybridMind(2024)]{hybrid2024}
534	Anonymous. 2024.
535	HybridMind: Adaptive selection of reasoning representations.
536	Preprint.
537	
538	\bibitem[VeriCoT(2024)]{vericot2024}
539	Anonymous. 2024.
540	VeriCoT: Verification of chain-of-thought reasoning.
541	Preprint.
542	
543	\bibitem[Roundtrip(2026)]{roundtrip2026}
544	Anonymous. 2026.
545	Roundtrip verification for diagnosis-guided repair.
546	Preprint.
547	
548	\bibitem[Liang et al.(2024)]{liang2024}
549	Zijian Liang, Tianqing Fang, Tongtong Wu, Weiqi Wang, and Yangqiu Song. 2024.
550	Cross-modal reasoning disagreement for filtering unreliable answers.
551	In \emph{Proc. ACL}.
552	
553	\bibitem[Wang et al.(2023)]{wang2023selfconsistency}
554	Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023.
555	Self-consistency improves chain of thought reasoning in language models.
556	In \emph{Proc. ICLR}.
557	
558	\bibitem[Du et al.(2023)]{du2023improving}
559	Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. 2023.
560	Improving factuality and reasoning in language models through multiagent debate.
561	\emph{arXiv preprint}.
562	
563	\bibitem[Liang et al.(2024b)]{liang2024encouraging}
564	Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, and Zhaopeng Tu. 2024.
565	Encouraging divergent thinking in large language models through multi-agent debate.
566	\emph{arXiv preprint}.
567	
568	\bibitem[Ni et al.(2023)]{ni2023lever}
569	Ansong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-tau Yih, Sida Wang, and Xi Victoria Lin. 2023.
570	LEVER: Learning to verify language-to-code generation with execution.
571	In \emph{Proc. ICML}.
572	
573	\bibitem[Lyu et al.(2023)]{lyu2023faithful}
574	Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, and Chris Callison-Burch. 2023.
575	Faithful chain-of-thought reasoning.
576	In \emph{Proc. IJCNLP-AACL}.
577	
578	\bibitem[Chen et al.(2024)]{chen2024teaching}
579	Xinyun Chen, Maxwell Lin, Nathanael Sch\"{a}rli, and Denny Zhou. 2024.
580	Teaching large language models to self-debug.
581	In \emph{Proc. ICLR}.
582	
583	\bibitem[Madaan et al.(2024)]{madaan2024selfrefine}
584	Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. 2024.
585	Self-refine: Iterative refinement with self-feedback.
586	In \emph{Proc. NeurIPS}.
587	
588	\bibitem[Denisov-Blanch et al.(2026)]{denisov2026}
589	Nikita Denisov-Blanch, Yuri Denisov-Blanch, and Elena Voita. 2026.
590	Correlated failures in LLM ensembles: When diversity isn't enough.
591	\emph{arXiv preprint}.
592	
593	\bibitem[Han et al.(2022)]{han2022folio}
594	Simeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell, Luke Benson, Lucy Sun, Ekaterina Zubova, Yujie Qiao, Matthew Burtell, et al. 2022.
595	FOLIO: Natural language reasoning with first-order logic.
596	\emph{arXiv preprint}.
597	
598	\bibitem[Liu et al.(2021)]{liu2021logiqa}
599	Jian Liu, Leyang Cui, Hanmeng Liu, Dandan Huang, Yile Wang, and Yue Zhang. 2021.
600	LogiQA: A challenge dataset for machine reading comprehension with logical reasoning.
601	In \emph{Proc. IJCAI}.
602	
603	\bibitem[Hendrycks et al.(2021)]{hendrycks2021math}
604	Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. 2021.
605	Measuring mathematical problem solving with the MATH dataset.
606	In \emph{Proc. NeurIPS}.
607	
608	\bibitem[Rein et al.(2024)]{rein2024gpqa}
609	David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman. 2024.
610	GPQA: A graduate-level Google-proof Q\&A benchmark.
611	In \emph{Proc. NAACL}.
612	
613	\end{thebibliography}
614	
615	\end{document}
616	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62ff8864-b361-45eb-9597-d00e30834e4b",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "2537e31e-5c09-46b2-975d-95fb342145c0",
  "sourceToolAssistantUUID": "62ff8864-b361-45eb-9597-d00e30834e4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T07:50:04.130Z_

Now let me also look at the experiment data and review context for any additional details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2537e31e-5c09-46b2-975d-95fb342145c0",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zHbDsSnqMXQn14KETj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57bda483-6168-46c7-9fc2-32be5aeeeb97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGWH63DzKB7tU57YcVTQQa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13005,
      "cache_read_input_tokens": 26895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13005,
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

_source line 29 · 2026-05-15T07:50:06.612Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YYHsLwvbRCuDNTcxBzWopB`</summary>

```json
{
  "pattern": "**/review_context*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57bda483-6168-46c7-9fc2-32be5aeeeb97",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zHbDsSnqMXQn14KETj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a12a85d-0b88-4e08-9920-d2cddc012b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGWH63DzKB7tU57YcVTQQa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13005,
      "cache_read_input_tokens": 26895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13005,
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

### Tool result

_source line 30 · 2026-05-15T07:50:06.696Z_

<details><summary>↩ Tool result · `toolu_01YYHsLwvbRCuDNTcxBzWopB`</summary>

```text
artifacts/dream_reports/dream_20260515T060408/best/review_context.yaml
artifacts/dream_reports/dream_20260515T060408/median/review_context.yaml
artifacts/dream_reports/dream_20260515T060408/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T071730/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a12a85d-0b88-4e08-9920-d2cddc012b42",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "21cfe460-87ed-4519-b04e-f0833faeae5f",
  "sourceToolAssistantUUID": "5a12a85d-0b88-4e08-9920-d2cddc012b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T07:50:06.748Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GxEd5NjjNo28zvPmP2Ee3d`</summary>

```json
{
  "pattern": "**/experiment_plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21cfe460-87ed-4519-b04e-f0833faeae5f",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zHbDsSnqMXQn14KETj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13b238af-0433-4727-a263-f326f003e184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGWH63DzKB7tU57YcVTQQa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13005,
      "cache_read_input_tokens": 26895,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13005
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 26895,
          "cache_creation_input_tokens": 13005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13005,
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

_source line 32 · 2026-05-15T07:50:06.788Z_

<details><summary>↩ Tool result · `toolu_01GxEd5NjjNo28zvPmP2Ee3d`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13b238af-0433-4727-a263-f326f003e184",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "2cf96d15-72e7-4082-8dd6-a87197edcb65",
  "sourceToolAssistantUUID": "13b238af-0433-4727-a263-f326f003e184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T07:50:09.622Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DG5rYTjwy4nU5g1JZkEEFL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cf96d15-72e7-4082-8dd6-a87197edcb65",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zJ7GPirWfJM8BA5Jot",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa6f2bd6-4655-4a2f-b209-234220680dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1sFNHSxvMjP4GitV5mKz7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 366,
      "cache_read_input_tokens": 39900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 366,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 34 · 2026-05-15T07:50:09.957Z_

<details><summary>↩ Tool result · `toolu_01DG5rYTjwy4nU5g1JZkEEFL`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。Cross-representation disagreement 是一个比 within-representation
2	  self-consistency 更高效的诊断信号：用 1/3 的 token 成本获得相当或更高的诊断精度。三条 claim 无需调整——C1/C2 跨三个基准和两个模型稳定，
3	  C3 的 GT-label-dependent 效应在新基准复现，taxonomy 跨模型一致。论文双轨叙事（分析为主 + 方法为辅）自然成立。 Selection
4	  ablation 展示 repair 在可诊断子集上的增量价值。Repair 的 GT=True overcorrection 作为 discovered boundary
5	  是加分项而非弱点。
6	
7	  '
8	imagined_experiments:
9	- name: FOLIO 完整分析（MVP 数据深度挖掘）
10	  plan_id: exp-001
11	  description: '基于 204 样本 MVP 数据的统计检验、错误分类、子集分层分析、不对称性 breakdown、 失败相关性定量分析和 cost-effectiveness
12	    分析。纯分析，无新实验运行。
13	
14	    '
15	  expected_results:
16	    C1_disagree_rate: 42.16% [35.3%, 49.0%]
17	    C2_diagnostic_rate: 87.21% [81.3%, 94.7%]
18	    C3_error_types: 4
19	    C4_targeted_delta_aggregate: +4.65pp (Fisher p=0.626, n.s.)
20	    C4_GT_True: -13.6pp
21	    C4_GT_False: +11.6pp
22	    C4_GT_Unknown: +14.7pp
23	    C5_committed_accuracy: 94.6% (35/37)
24	    C5_coverage: 53.0% (35/66)
25	    asymmetry_ratio: 5.6:1 (FOL=56, Code=10, Both=10)
26	    phi_coefficient: 0.189
27	    phi_p_value: 0.007
28	    complementary_error_rate: 75% (75/100)
29	    cost_multiplier_vs_code_only: 5.76x tokens
30	    accuracy_gain_over_code_only: +21.6pp
31	    dominant_error: logic_error 25.5%
32	  result_rationale: '这是已有 MVP 数据的深度挖掘，数值已固定。在 best 档位下，关键价值在于：(1) Bootstrap CI 对 C1/C2
33	    给出了紧致的区间，C2 下界 81.3% 远超 75% 阈值，为高精度诊断信号提供统计支撑； (2) phi=0.189 (p=0.007) 表明 FOL/Code
34	    失败相关性低但统计显著——恰好落在"足够独立以产生互补信号， 又不完全独立"的理想区间；(3) 75% 单侧失败率直接支撑 cross-representation
35	    的互补性叙事； (4) GT-stratified C4 揭示三路分裂是 Claim 3 的核心发现，aggregate 非显著反而强化了 "必须分层报告"的方法论贡献。cost_multiplier
36	    5.76x 看似高，但对比 k=5 self-consistency 的 5x 成本，CRD 以相近成本获得更丰富的诊断信息（错误类型 + 定位），而非仅
37	    majority vote。
38	
39	    '
40	  tables:
41	  - name: 'Table 1: FOLIO C1-C5 Metrics with Bootstrap 95% CI'
42	    columns:
43	    - Metric
44	    - Point Estimate
45	    - 95% CI
46	    - MVP Gate
47	    rows:
48	    - - C1 (Disagree Rate)
49	      - 42.16%
50	      - '[35.3%, 49.0%]'
51	      - PASS (≥15%)
52	    - - C2 (Diagnostic Rate)
53	      - 87.21%
54	      - '[81.3%, 94.7%]'
55	      - PASS (≥75%)
56	    - - C3 (Error Types)
57	      - 4 types
58	      - —
59	      - PASS (≥3)
60	    - - C4 (Repair Delta)
61	      - +4.65pp
62	      - '[-8.8%, +18.1%]'
63	      - FAIL (CI includes 0)
64	    - - C5 (Localization)
65	      - 53.0%
66	      - '[41.0%, 65.1%]'
67	      - FAIL (<70%)
68	  - name: 'Table 2: GT-Label-Stratified Repair Effect'
69	    columns:
70	    - GT Label
71	    - n
72	    - Targeted Acc
73	    - Blind Acc
74	    - Delta
75	    - Interpretation
76	    rows:
77	    - - 'True'
78	      - 72
79	      - 63.6%
80	      - 77.3%
81	      - -13.6pp
82	      - Overcorrection
83	    - - 'False'
84	      - 63
85	      - 76.7%
86	      - 70.0%
87	      - +6.7pp
88	      - Modest help
89	    - - Unknown
90	      - 69
91	      - 67.7%
92	      - 52.9%
93	      - +14.7pp
94	      - Diagnosis helps
95	  - name: 'Table 3: Error Taxonomy Distribution'
96	    columns:
97	    - Error Type
98	    - Count
99	    - Proportion
100	    rows:
101	    - - logic_error
102	      - 52
103	      - 25.5%
104	    - - negation_error
105	      - 22
106	      - 10.8%
107	    - - exec_crash
108	      - 11
109	      - 5.4%
110	    - - quantifier_error
111	      - 4
112	      - 2.0%
113	  figures_description:
114	  - 'Fig 1: Confusion matrix heatmap — FOL correct/wrong × Code correct/wrong，标注 5.6:1
115	    不对称'
116	  - 'Fig 2: GT-stratified repair delta bar chart，三色柱状图显示三路分裂效应'
117	  - 'Fig 3: phi coefficient 按 GT label 分层的热图'
118	  analysis: 'exp-001 作为 anchor 实验，所有数值已确定。best 档位下的分析重点是将 C4 aggregate 非显著 和 C5 低覆盖率重新
119	    frame 为方法论发现而非失败：(1) aggregate 非显著正是因为 GT-label-dependent 效应相互抵消，分层报告是正确的分析粒度；(2)
120	    C5 coverage 53% 但 committed accuracy 94.6% 是高精度/低召回的 deliberate tradeoff，ambiguous
121	    标签中 61% 来自 GT=Unknown 驱动—— 这些样本恰好是 repair delta 最大的子集，说明即使定位不确定，disagreement pattern
122	    本身 就有修复价值。
123	
124	    '
125	- name: 跨模型消融（FOLIO）
126	  plan_id: exp-002
127	  description: '三组条件：(a) Qwen3-32B within-model (MVP baseline), (b) DeepSeek V4 Pro
128	    within-model, (c) DeepSeek FOL + Qwen Code cross-model。区分分歧来源。
129	
130	    '
131	  expected_results:
132	    deepseek_within_C1: 38.7%
133	    deepseek_within_C2: 83.5%
134	    deepseek_within_C2_CI: '[74.2%, 91.8%]'
135	    deepseek_within_asymmetry: 4.2:1 (FOL-favored)
136	    deepseek_within_C4_GT_Unknown: +12.1pp
137	    deepseek_within_C4_GT_True: -10.3pp
138	    deepseek_within_C4_GT_False: +8.4pp
139	    cross_model_C1: 47.5%
140	    cross_model_C2: 80.9%
141	    cross_model_asymmetry: 3.8:1 (FOL-favored)
142	    C2_delta_vs_MVP: -3.7pp (within ±8pp gate)
143	    asymmetry_direction: consistent (FOL-favored in all 3 conditions)
144	  result_rationale: '在 best 档位下，DeepSeek within-model C2 落在 MVP ±8pp 内（83.5% vs 87.2%，delta=-3.7pp），
145	    证明诊断精度不是 Qwen3-32B 的特异性质，而是 cross-representation disagreement 的结构性属性。 DeepSeek
146	    C1 略低（38.7% vs 42.2%）合理——DeepSeek 作为更强模型，两条表征路径各自精度更高， 分歧率自然略低，但 C2 保持在 80%+ 说明分歧样本仍然高度诊断性。不对称方向一致（FOL-favored）
147	    是关键：这不是模型偶然，而是 FOL+Z3 的形式验证保证系统性地比 Python 执行更可靠。 Cross-model 条件 C1 更高（47.5%）因为两个不同模型的
148	    formalization bias 不同， 增加了分歧概率，但 C2 略降（80.9%）因为部分分歧来自模型差异而非 formalization 错误。
149	    这个分离正好支撑论文的核心论点：within-model cross-representation disagreement 更纯粹地反映 formalization
150	    错误，cross-model 混入了 capability 噪声。
151	
152	    '
153	  tables:
154	  - name: 'Table 4: Cross-Model Ablation Results on FOLIO (n=204)'
155	    columns:
156	    - Condition
157	    - C1
158	    - C2
159	    - C2 95% CI
160	    - Asymmetry
161	    - C4 (Unknown)
162	    - C4 (True)
163	    rows:
164	    - - Qwen3-32B within (MVP)
165	      - 42.2%
166	      - 87.2%
167	      - '[81.3%, 94.7%]'
168	      - 5.6:1 FOL
169	      - +14.7pp
170	      - -13.6pp
171	    - - DeepSeek within
172	      - 38.7%
173	      - 83.5%
174	      - '[74.2%, 91.8%]'
175	      - 4.2:1 FOL
176	      - +12.1pp
177	      - -10.3pp
178	    - - DeepSeek×Qwen cross
179	      - 47.5%
180	      - 80.9%
181	      - '[71.8%, 89.1%]'
182	      - 3.8:1 FOL
183	      - +9.8pp
184	      - -8.7pp
185	  figures_description:
186	  - 'Fig 4: 三条件 C1/C2 对比柱状图，带 error bars'
187	  - 'Fig 5: 不对称比例的 stacked bar，三条件均 FOL-favored'
188	  analysis: '三组数据形成清晰的叙事梯度：within-model(同模型) > cross-model(跨模型) 在 C2 上， 说明 within-model
189	    的诊断信号更纯净。DeepSeek GT-stratified 效应方向完全一致 （Unknown 正, True 负, False 正），证明 Claim
190	    3 的 GT-label-dependent 效应 是表征结构属性而非模型特异。C2 delta -3.7pp 在 ±8pp gate 内——这是 best
191	    档的 sweet spot，既证明泛化，又不大到暗示 MVP 是 outlier。
192	
193	    '
194	- name: ProofWriter / LogiQA 扩展
195	  plan_id: exp-003
196	  description: '第二逻辑推理基准。先 pilot 20-30 样本验证 disagree_rate ≥ 10%， 通过则全量跑 ProofWriter；失败则切换
197	    LogiQA。
198	
199	    '
200	  expected_results:
201	    dataset_used: LogiQA
202	    pilot_proofwriter_disagree_rate: 6.7% (2/30) — pilot FAIL
203	    pilot_switch_reason: ProofWriter 合成数据过于规则，FOL/Code 均高精度 (>93%)，分歧率不足
204	    logiqA_n: 200
205	    logiqA_C1: 34.0%
206	    logiqA_C2: 81.5%
207	    logiqA_C2_CI: '[73.8%, 88.2%]'
208	    logiqA_C3_error_types: 4
209	    logiqA_asymmetry: 3.2:1 (FOL-favored)
210	    logiqA_C4_GT_stratified_positive_subset: +11.3pp
211	    logiqA_C4_GT_stratified_negative_subset: -9.8pp
212	    logiqA_C5_committed: 91.2%
213	    logiqA_C5_coverage: 48.5%
214	  result_rationale: '在 best 档位下，ProofWriter pilot 失败是预期且合理的——合成数据的逻辑结构简单规则， 两条表征路径都能高精度处理，分歧率仅
215	    6.7%。这不是坏消息：切换到 LogiQA（自然语言逻辑， 4 选 1）反而更好，因为 NL 歧义性更高，更能展示 CRD 在真实场景中的价值。LogiQA
216	    C1=34% 略低于 FOLIO（42%）合理——选择题格式约束了输出空间，减少了 formalization 分歧；但 C2=81.5% 仍然高（≥75%
217	    gate），证明分歧样本跨基准稳定诊断。不对称比仍 FOL-favored（3.2:1）但比 FOLIO 的 5.6:1 低——LogiQA 的命题逻辑复杂度低于
218	    FOLIO 的一阶逻辑，FOL 路径的优势 相对缩小。GT-stratified 效应方向复现（正/负分裂），证明 Claim 3 跨基准泛化。 C5 committed
219	    91.2% 保持在 90%+ 高精度区间。
220	
221	    '
222	  tables:
223	  - name: 'Table 5: LogiQA Results (n=200, Qwen3-32B)'
224	    columns:
225	    - Metric
226	    - LogiQA
227	    - FOLIO (ref)
228	    - Delta
229	    rows:
230	    - - C1 (Disagree Rate)
231	      - 34.0%
232	      - 42.2%
233	      - -8.2pp
234	    - - C2 (Diagnostic Rate)
235	      - 81.5%
236	      - 87.2%
237	      - -5.7pp
238	    - - C3 (Error Types)
239	      - '4'
240	      - '4'
241	      - —
242	    - - C5 Committed Acc
243	      - 91.2%
244	      - 94.6%
245	      - -3.4pp
246	    - - Asymmetry (FOL:Code)
247	      - 3.2:1
248	      - 5.6:1
249	      - narrower
250	  - name: 'Table 5b: ProofWriter Pilot Results (n=30)'
251	    columns:
252	    - Metric
253	    - Value
254	    - Gate
255	    - Decision
256	    rows:
257	    - - Disagree Rate
258	      - 6.7%
259	      - ≥10%
260	      - FAIL → switch to LogiQA
261	    - - FOL Accuracy
262	      - 93.3%
263	      - —
264	      - —
265	    - - Code Accuracy
266	      - 90.0%
267	      - —
268	      - —
269	  figures_description:
270	  - 'Fig 6: FOLIO vs LogiQA C1/C2 并排对比，带 CI error bars'
271	  - 'Fig 7: LogiQA GT-stratified repair delta 复现 FOLIO 三路分裂模式'
272	  analysis: 'LogiQA 作为第二基准完美补充 FOLIO：不同数据源（中国公务员考试 vs 专家标注 FOL）， 不同任务格式（4 选 1 vs 3
273	    分类），C2 仍在 [75%, 92%] range 内。ProofWriter pilot 失败在论文中可以作为 1 段讨论："合成数据过于规则，分歧信号需要自然语言的
274	    formalization 挑战"——这反而强化了 CRD 适用场景的 characterization。
275	
276	    '
277	- name: MATH Level 5 双可执行表征扩展
278	  plan_id: exp-004
279	  description: 'MATH Level 5 使用 SymPy 符号推理 vs Python 数值计算两条可执行路径， 保持 cross-executable-representation
280	    框架一致性。
281	
282	    '
283	  expected_results:
284	    n: 200
285	    math_C1: 28.5%
286	    math_C2: 76.0%
287	    math_C2_CI: '[66.1%, 85.2%]'
288	    math_C3_error_types: 3
289	    math_asymmetry: 1.8:1 (Code-favored)
290	    math_asymmetry_direction: 反转——Python 数值计算在 MATH 上优于 SymPy 符号推理
291	    math_C4_GT_correct_delta: +3.2pp
292	    math_C4_GT_wrong_delta: +7.8pp
293	    math_C5_committed: 88.5%
294	    math_C5_coverage: 55.0%
295	    sympy_crash_rate: 12.5%
296	    python_crash_rate: 4.0%
297	  result_rationale: '在 best 档位下，MATH C1=28.5% 满足 ≥15% gate。C1 低于 FOLIO（42%）合理—— 数学问题有唯一正确答案，两条计算路径比逻辑推理的
298	    formalization 更容易达成一致。 C2=76% 刚好在 [70%, 85%] 范围内——数学分歧中更多是计算错误而非 formalization
299	    错误， 部分分歧来自数值精度问题（如浮点近似 vs 精确符号解），诊断性略低但仍超 70% gate。 关键发现：不对称方向反转（Code-favored
300	    1.8:1），与 FOLIO 的 FOL-favored 5.6:1 相反。 这是 best 档的 killer result——证明不对称性不是 FOL
301	    固有优势，而是表征-任务匹配： 在逻辑推理上 FOL+Z3 有形式验证优势，在数学计算上 Python 的灵活数值方法更鲁棒。 SymPy crash rate
302	    12.5% > Python 4% 因为 SymPy 对输入格式敏感（符号化简失败、 方程无解析解等），而 Python 数值方法更容错。这个反转直接回应
303	    R5（"不只是 FOL-as-verifier"）。
304	
305	    '
306	  tables:
307	  - name: 'Table 6: MATH Level 5 Results (n=200, Qwen3-32B)'
308	    columns:
309	    - Metric
310	    - MATH
311	    - FOLIO (ref)
312	    - LogiQA (ref)
313	    rows:
314	    - - C1 (Disagree Rate)
315	      - 28.5%
316	      - 42.2%
317	      - 34.0%
318	    - - C2 (Diagnostic Rate)
319	      - 76.0%
320	      - 87.2%
321	      - 81.5%
322	    - - C3 (Error Types)
323	      - '3'
324	      - '4'
325	      - '4'
326	    - - Asymmetry
327	      - 1.8:1 Code-fav
328	      - 5.6:1 FOL-fav
329	      - 3.2:1 FOL-fav
330	    - - C5 Committed
331	      - 88.5%
332	      - 94.6%
333	      - 91.2%
334	  - name: 'Table 7: Asymmetry Direction Across Domains'
335	    columns:
336	    - Domain
337	    - Representation A
338	    - Representation B
339	    - Favored
340	    - Ratio
341	    rows:
342	    - - Logic (FOLIO)
343	      - FOL+Z3
344	      - Python exec
345	      - FOL
346	      - 5.6:1
347	    - - Logic (LogiQA)
348	      - FOL+Z3
349	      - Python exec
350	      - FOL
351	      - 3.2:1
352	    - - Math (MATH)
353	      - SymPy symbolic
354	      - Python numerical
355	      - Python
356	      - 1.8:1
357	  figures_description:
358	  - 'Fig 8: 三基准 asymmetry direction 可视化——逻辑 vs 数学域的反转'
359	  - 'Fig 9: MATH 错误类型分布（computation_error, symbolic_failure, exec_crash）'
360	  analysis: 'MATH 的不对称反转是 best 档位的标志性结果。它将 paper 的 story 从 "FOL is better" 升级为 "cross-representation
361	    disagreement reveals domain-specific representation strengths"——更深层的洞察，更广的适用性。C2=76%
362	    虽然低于 FOLIO，但 CI 下界 66.1% 接近 70% gate，在 best 档位下 point estimate 通过。C3=3 types（少了
363	    quantifier_error， 因为数学域没有量词问题），但新增 computation_error（截断/精度）类型。
364	
365	    '
366	- name: Repair 机制改进（多轮修复）
367	  plan_id: exp-005
368	  description: '最多 3 轮 repair，加入错误类型特定修复策略，按 GT label 和 error_type 分层报告。 目标：Unknown
369	    子组 delta 从 +14.7pp 拉到 +20pp+。
370	
371	    '
372	  expected_results:
373	    repair_rounds_avg: 1.8
374	    GT_Unknown_delta_round1: +14.7pp
375	    GT_Unknown_delta_round3: +22.1pp
376	    GT_False_delta_round1: +6.7pp
377	    GT_False_delta_round3: +10.4pp
378	    GT_True_delta_round1: -13.6pp
379	    GT_True_delta_round3: -11.2pp
380	    C4_unknown_false_combined_delta: +15.8pp
381	    error_type_repair_success:
382	      logic_error: 68.3%
383	      negation_error: 72.0%
384	      exec_crash: 81.8%
385	      quantifier_error: 50.0%
386	    round2_additional_fixes: 8 samples
387	    round3_additional_fixes: 3 samples
388	  result_rationale: '在 best 档位下，多轮 repair 将 GT=Unknown delta 从 +14.7pp 拉到 +22.1pp（超过
389	    +20pp gate）。 机制：第一轮修复了大部分 Code overclaiming（Code 输出 True/False 但应为 Unknown）， 第二轮处理残余的
390	    logic_error（FOL 形式化中的量词/否定遗漏导致第一轮修复方向偏移）， 第三轮边际收益递减（仅 3 个 additional fix）。GT=True
391	    overcorrection 从 -13.6pp 改善到 -11.2pp——多轮 repair 的错误类型感知策略对 GT=True 的伤害略有缓解 （negation_error
392	    特定策略避免了盲目翻转），但仍然为负，证明 overcorrection boundary 是结构性的而非策略不足。exec_crash 81.8% 修复率最高因为这类错误最容易诊断和修复
393	    （语法/运行时错误，重新生成即可）。quantifier_error 50% 最低因为量词错误需要 深层理解全称/存在量词的语义。combined delta
394	    +15.8pp 落在 [8, 18] range 的偏高区域。
395	
396	    '
397	  tables:
398	  - name: 'Table 8: Multi-Round Repair Results (FOLIO, n=204)'
399	    columns:
400	    - GT Label
401	    - n
402	    - Round 1 Delta
403	    - Round 3 Delta
404	    - Improvement
405	    rows:
406	    - - Unknown
407	      - 69
408	      - +14.7pp
409	      - +22.1pp
410	      - +7.4pp
411	    - - 'False'
412	      - 63
413	      - +6.7pp
414	      - +10.4pp
415	      - +3.7pp
416	    - - 'True'
417	      - 72
418	      - -13.6pp
419	      - -11.2pp
420	      - +2.4pp (still negative)
421	  - name: 'Table 9: Repair Success Rate by Error Type (Round 3)'
422	    columns:
423	    - Error Type
424	    - Attempted
425	    - Fixed
426	    - Success Rate
427	    rows:
428	    - - logic_error
429	      - 41
430	      - 28
431	      - 68.3%
432	    - - negation_error
433	      - 18
434	      - 13
435	      - 72.0%
436	    - - exec_crash
437	      - 11
438	      - 9
439	      - 81.8%
440	    - - quantifier_error
441	      - 4
442	      - 2
443	      - 50.0%
444	  figures_description:
445	  - 'Fig 10: 多轮 repair 收益曲线（Round 1/2/3 delta 按 GT label）'
446	  - 'Fig 11: 错误类型特定修复成功率 bar chart'
447	  analysis: '多轮 repair 的递减收益模式（Round 1: +14.7→+22.1, Round 2: +5.2, Round 3: +2.2）
448	    是 best 档位的理想结果——证明错误类型特定策略有增量价值，但不是无限的。 GT=True 仍为负是论文的 honesty signal——不掩饰 boundary。错误类型分层报告
449	    为 exp-008（taxonomy ablation）提供了直接支撑。
450	
451	    '
452	- name: Unknown 样本深度分析 + correlated failure 定量
453	  plan_id: exp-006
454	  description: '分析 GT=Unknown 驱动 C4 delta 的机制，FOL/Code 相关系数按 GT 分层， false agreement
455	    rate，specification vs formalization 错误分类。
456	
457	    '
458	  expected_results:
459	    code_overclaiming_rate_unknown: 78.3% (54/69)
460	    code_overclaiming_mechanism: Code 路径倾向输出 True/False 而非 Unknown，因为 Python 缺乏三值逻辑原生支持
461	    fol_overclaiming_rate_unknown: 21.7% (15/69)
462	    phi_by_GT:
463	      'True': 0.245
464	      'False': 0.162
465	      Unknown: 0.098
466	    false_agreement_rate: 12.3% (25/204)
467	    false_agreement_breakdown: GT=True 14/72 (19.4%), GT=False 7/63 (11.1%), GT=Unknown
468	      4/69 (5.8%)
469	    specification_error_rate: 8.3% (17/204)
470	    formalization_specific_error_rate: 91.7% (187/204 non-spec-error)
471	  result_rationale: '在 best 档位下，Code overclaiming 78.3% 的高比率清晰解释了 GT=Unknown 子集的 repair
472	    delta 来源：Python 执行路径缺乏三值逻辑（True/False/Unknown）的原生表达能力， 倾向将 insufficient-information
473	    情况强制映射为 True 或 False。当 CRD 诊断出分歧后， repair prompt 包含"FOL 路径返回 Unknown"的信息，帮助模型认识到证据不足，修正
474	    Code 的 overclaiming。phi 按 GT 分层显示 Unknown 相关性最低（0.098），意味着 FOL/Code 在 Unknown
475	    上最不相关——互补信号最强，这直接解释了为什么 repair delta 最大。 False agreement rate 12.3% 相对低（Denisov-Blanch
476	    2026 担忧的 correlated failure 不严重），且 GT=Unknown 子集仅 5.8% false agreement——再次证明 Unknown
477	    是 CRD 的 最佳应用场景。specification error 仅 8.3% 说明绝大多数错误是 formalization-specific 而非原始问题歧义导致，支撑
478	    CRD 的诊断靶点合理性。
479	
480	    '
481	  tables:
482	  - name: 'Table 10: Correlated Failure Analysis'
483	    columns:
484	    - GT Label
485	    - n
486	    - phi
487	    - False Agreement Rate
488	    - Code Overclaiming
489	    rows:
490	    - - 'True'
491	      - 72
492	      - 0.245
493	      - 19.4%
494	      - N/A
495	    - - 'False'
496	      - 63
497	      - 0.162
498	      - 11.1%
499	      - N/A
500	    - - Unknown
501	      - 69
502	      - 0.098
503	      - 5.8%
504	      - 78.3%
505	    - - Overall
506	      - 204
507	      - 0.189
508	      - 12.3%
509	      - —
510	  figures_description:
511	  - 'Fig 12: Code overclaiming 机制图——Unknown→True/False 的映射路径'
512	  - 'Fig 13: phi coefficient 按 GT label 分层 + false agreement rate 联合可视化'
513	  analysis: '此分析为 Claim 3 提供了因果机制：不是 repair 策略差异导致 GT-dependent 效应， 而是 Code 表征的结构性局限（缺乏三值逻辑）×
514	    GT label 的交互作用。这使得 GT=True overcorrection 也有了合理解释——当 GT=True 但 Code 错误输出 False/Unknown
515	    时， 诊断信号误导 repair 认为应该远离 True，导致 overcorrection。
516	
517	    '
518	- name: Selection vs Repair 消融
519	  plan_id: exp-007
520	  description: '分歧检测+定位错误侧后，直接选正确侧 vs 诊断引导修复，按 error_type 分层报告。
521	
522	    '
523	  expected_results:
524	    blind_baseline_acc_GT_not_true: 61.4%
525	    selection_acc_GT_not_true: 72.7%
526	    repair_acc_GT_not_true: 76.2%
527	    selection_vs_blind_delta: +11.3pp
528	    repair_vs_selection_delta: +3.5pp
529	    selection_by_error_type:
530	      logic_error: 70.7%
531	      negation_error: 77.8%
532	      exec_crash: 90.9%
533	      quantifier_error: 50.0%
534	    repair_by_error_type:
535	      logic_error: 75.6%
536	      negation_error: 77.8%
537	      exec_crash: 90.9%
538	      quantifier_error: 75.0%
539	    repair_advantage_concentrated_on: logic_error (+4.9pp) 和 quantifier_error (+25pp)
540	  result_rationale: '在 best 档位下，selection 已经大幅优于 blind baseline（+11.3pp，远超 +5pp gate），
541	    证明 CRD 诊断+定位的基本价值。repair 在 selection 之上再加 +3.5pp（刚超 +3pp gate）， 增量价值集中在 logic_error
542	    和 quantifier_error——这两类错误需要修正 formalization 而非简单选边，selection 无法解决因为两侧都可能部分正确（如
543	    FOL 量词正确但谓词错误， Code 谓词正确但逻辑流错误）。negation_error 和 exec_crash 上 repair ≈ selection，
544	    因为这两类错误通常有明确的"一侧对一侧错"模式，选正确侧就足够了。 这个分层结果支撑了论文的 nuanced claim：repair 不是全面优于 selection，
545	    而是在特定错误类型上有不可替代的价值——正是 taxonomy 驱动修复的意义。 限制在 GT≠True 子集报告（n=132），因为 GT=True overcorrection
546	    对 selection 和 repair 都适用，不影响二者的相对对比。
547	
548	    '
549	  tables:
550	  - name: 'Table 11: Selection vs Repair on GT≠True Subset (n=132)'
551	    columns:
552	    - Method
553	    - Overall Acc
554	    - logic_error
555	    - negation_error
556	    - exec_crash
557	    - quantifier_error
558	    rows:
559	    - - Blind Baseline
560	      - 61.4%
561	      - 56.1%
562	      - 66.7%
563	      - 72.7%
564	      - 25.0%
565	    - - Selection
566	      - 72.7%
567	      - 70.7%
568	      - 77.8%
569	      - 90.9%
570	      - 50.0%
571	    - - Repair (Round 3)
572	      - 76.2%
573	      - 75.6%
574	      - 77.8%
575	      - 90.9%
576	      - 75.0%
577	  figures_description:
578	  - 'Fig 14: 三方法对比 grouped bar chart，按 error_type 分层'
579	  - 'Fig 15: Repair 增量价值热图（repair - selection delta 按 error type）'
580	  analysis: 'Selection vs repair 的分层结果是 exp-007 的核心贡献：证明 taxonomy 不仅是分析工具， 还有规定性价值（prescriptive
581	    value）——知道错误类型决定了应该 select 还是 repair。 这直接回应 R3 并为 exp-008 铺路。selection_vs_blind
582	    +11.3pp 是强结果， 证明即使不 repair，CRD 诊断+定位已经有实用价值。
583	
584	    '
585	- name: Error Taxonomy 消融
586	  plan_id: exp-008
587	  description: '按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。
588	
589	    '
590	  expected_results:
591	    taxonomy_guided_acc: 76.2%
592	    fixed_strategy_acc: 71.2%
593	    taxonomy_delta: +5.0pp
594	    taxonomy_advantage_by_type:
595	      logic_error: +6.2pp
596	      negation_error: +2.3pp
597	      exec_crash: +0.0pp
598	      quantifier_error: +18.0pp
599	    mcnemar_p: 0.042
600	  result_rationale: '在 best 档位下，taxonomy-guided 策略整体优于 fixed strategy +5.0pp（McNemar
601	    p=0.042， 显著）。增量主要来自 logic_error（最大类，+6.2pp——targeted prompt 包含"检查谓词定义 和推理链"vs
602	    盲目重生成）和 quantifier_error（最小类但增幅最大 +18.0pp——targeted prompt 显式提示"检查全称/存在量词的作用域"，盲目重生成几乎无法修复这类细微错误）。
603	    exec_crash 无差异因为重生成本身就是最优策略（崩溃了就重新生成）。negation_error 增量小因为否定翻转相对简单，固定策略也能偶然修复。McNemar
604	    p=0.042 刚好显著， 反映样本量有限但效应真实。
605	
606	    '
607	  tables:
608	  - name: 'Table 12: Taxonomy-Guided vs Fixed Strategy Repair'
609	    columns:
610	    - Error Type
611	    - n
612	    - Taxonomy-Guided
613	    - Fixed (regen)
614	    - Delta
615	    rows:
616	    - - logic_error
617	      - 41
618	      - 75.6%
619	      - 69.4%
620	      - +6.2pp
621	    - - negation_error
622	      - 18
623	      - 77.8%
624	      - 75.5%
625	      - +2.3pp
626	    - - exec_crash
627	      - 11
628	      - 90.9%
629	      - 90.9%
630	      - +0.0pp
631	    - - quantifier_error
632	      - 4
633	      - 75.0%
634	      - 57.0%
635	      - +18.0pp
636	    - - Overall
637	      - 74
638	      - 76.2%
639	      - 71.2%
640	      - +5.0pp (p=0.042)
641	  figures_description:
642	  - 'Fig 16: Taxonomy-guided vs fixed strategy 按 error type 对比'
643	  analysis: 'Taxonomy ablation 证明 error classification 不只是 analysis contribution——
644	    它有 prescriptive value。这将 Claim 2 从纯分析升级为方法贡献， 增加论文的实用性维度。quantifier_error 的 +18pp
645	    虽然 n 太小（4 samples）不能 单独做统计检验，但方向明确。
646	
647	    '
648	- name: 统计显著性全面检验
649	  plan_id: exp-009
650	  description: '对所有 benchmark 的 C1-C5 指标做 Bootstrap 95% CI + Fisher exact / McNemar
651	    test。
652	
653	    '
654	  expected_results:
655	    FOLIO_C2_CI: '[81.3%, 94.7%]'
656	    LogiQA_C2_CI: '[73.8%, 88.2%]'
657	    MATH_C2_CI: '[66.1%, 85.2%]'
658	    cross_benchmark_C2_min_lower: 66.1%
659	    FOLIO_C4_unknown_fisher_p: 0.038
660	    FOLIO_C4_true_fisher_p: 0.021
661	    LogiQA_C4_positive_subset_fisher_p: 0.045
662	    CRD_vs_SC5_mcnemar_p: 0.031
663	    all_primary_claims_significant: true
664	    aggregate_C4_significant: false
665	  result_rationale: '在 best 档位下，所有主要 claim 的分层指标都达到统计显著：FOLIO GT=Unknown C4 delta
666	    Fisher p=0.038（n=69，+14.7pp→+22.1pp 多轮后更强），GT=True overcorrection p=0.021（负方向也显著，strengthens
667	    boundary characterization）。LogiQA 的正子集 p=0.045 复现效应。CRD vs SC5 McNemar p=0.031
668	    证明诊断精度差异显著。 关键：aggregate C4 仍然不显著——这在 best 档位下是 feature not bug， 因为分层报告是我们的 methodological
669	    contribution。CI 紧致度随样本量提高 （FOLIO n=204 > LogiQA n=200 > MATH n=200），MATH C2 下界
670	    66.1% 最低 但 point estimate 76% 仍超 70% gate。
671	
672	    '
673	  tables:
674	  - name: 'Table 13: Statistical Significance Summary Across Benchmarks'
675	    columns:
676	    - Test
677	    - Benchmark
678	    - Metric
679	    - Statistic
680	    - p-value
681	    - Significant?
682	    rows:
683	    - - Fisher
684	      - FOLIO
685	      - C4 GT=Unknown
686	      - +22.1pp
687	      - '0.038'
688	      - 'Yes'
689	    - - Fisher
690	      - FOLIO
691	      - C4 GT=True
692	      - -11.2pp
693	      - '0.021'
694	      - 'Yes'
695	    - - Fisher
696	      - LogiQA
697	      - C4 positive subset
698	      - +11.3pp
699	      - '0.045'
700	      - 'Yes'
701	    - - McNemar
702	      - FOLIO
703	      - CRD vs SC5 precision
704	      - +7.2pp
705	      - '0.031'
706	      - 'Yes'
707	    - - Fisher
708	      - FOLIO
709	      - C4 aggregate
710	      - +4.65pp
711	      - '0.626'
712	      - 'No'
713	    - - Bootstrap
714	      - All
715	      - C2 range
716	      - '[66.1%, 94.7%]'
717	      - —
718	      - —
719	  figures_description:
720	  - 'Fig 17: 跨基准 C2 Bootstrap CI 的 forest plot'
721	  analysis: '统计检验结果在 best 档位下完美支撑叙事：分层指标显著而 aggregate 不显著， 证明分层分析的必要性。Forest plot
722	    显示三基准 C2 CI 重叠但中心递减 （FOLIO > LogiQA > MATH），反映任务复杂度梯度。
723	
724	    '
725	- name: Self-Consistency Baseline 对比
726	  plan_id: exp-012
727	  description: 'FOLIO + LogiQA + MATH 上对比 k=5 FOL-only majority vote, k=5 Code-only
728	    majority vote, vs single-pass CRD。隔离 cross-representation 信号 vs 单表征 sampling diversity。
729	
730	    '
731	  expected_results:
732	    FOLIO:
733	      SC5_FOL_precision: 79.3%
734	      SC5_Code_precision: 72.1%
735	      CRD_precision: 87.2%
736	      CRD_vs_SC5_FOL_delta: +7.9pp
737	      SC5_FOL_cost_tokens: 5x baseline
738	      SC5_Code_cost_tokens: 5x baseline
739	      CRD_cost_tokens: 2x baseline
740	      CRD_vs_SC5_cost_ratio: '0.40'
741	    LogiQA:
742	      SC5_FOL_precision: 75.8%
743	      SC5_Code_precision: 69.4%
744	      CRD_precision: 81.5%
745	      CRD_vs_SC5_FOL_delta: +5.7pp
746	    MATH:
747	      SC5_SymPy_precision: 71.2%
748	      SC5_Python_precision: 74.8%
749	      CRD_precision: 76.0%
750	      CRD_vs_SC5_best_delta: +1.2pp
751	    overall_CRD_vs_SC5_precision_delta: +4.9pp (avg across benchmarks)
752	    overall_CRD_vs_SC5_cost_ratio: 0.4
753	  result_rationale: '在 best 档位下，CRD 在所有三个基准上诊断精度均优于 k=5 单表征 majority vote， 且 token
754	    成本仅为 40%（2 次生成 vs 5 次生成）。机制：k=5 同表征 sampling 捕获的是 generation variance（同一 prompt
755	    的随机性），而 CRD 捕获的是 paradigm-level difference （形式逻辑 vs 命令式代码的系统性差异）。前者在高温度下有效但容易被
756	    mode collapse 削弱 （LLM 倾向于收敛到同一错误模式），后者因为表征范式根本不同而产生更互补的错误信号。 FOLIO delta 最大（+7.9pp）因为
757	    FOL 和 Python 的范式差异最大；MATH delta 最小（+1.2pp） 因为 SymPy 和 Python numerical 都是 Python
758	    生态，范式差异较小。MATH 上 SC5_Python 甚至略优于 SC5_SymPy（74.8% vs 71.2%），与 exp-004 的不对称反转一致。
759	    CRD cost ratio 0.40 落在 [0.30, 0.45] range——2 次生成 vs 5 次生成 = 0.40， 考虑 CRD 额外的 diagnosis
760	    prompt 开销后正好 40%。
761	
762	    '
763	  tables:
764	  - name: 'Table 14: CRD vs Self-Consistency (k=5) Across Benchmarks'
765	    columns:
766	    - Benchmark
767	    - SC5-FOL Prec
768	    - SC5-Code Prec
769	    - CRD Prec
770	    - CRD-SC5 Δ
771	    - Cost Ratio
772	    rows:
773	    - - FOLIO
774	      - 79.3%
775	      - 72.1%
776	      - 87.2%
777	      - +7.9pp
778	      - '0.40'
779	    - - LogiQA
780	      - 75.8%
781	      - 69.4%
782	      - 81.5%
783	      - +5.7pp
784	      - '0.40'
785	    - - MATH
786	      - 71.2%
787	      - 74.8%
788	      - 76.0%
789	      - +1.2pp
790	      - '0.40'
791	    - - Average
792	      - 75.4%
793	      - 72.1%
794	      - 81.6%
795	      - +4.9pp
796	      - '0.40'
797	  figures_description:
798	  - 'Fig 18: CRD vs SC5 precision-cost Pareto 图——CRD 在 Pareto front 上'
799	  - 'Fig 19: 按基准的 CRD vs SC5 对比 grouped bar chart'
800	  analysis: 'exp-012 是回应 R8 的核心实验。best 档位下 CRD Pareto-dominates SC5（更高精度+更低成本）， headline
801	    变为"用 40% 的 token 成本获得平均 +4.9pp 的诊断精度提升"。 MATH 上 delta 仅 +1.2pp 是可接受的——因为 SymPy/Python
802	    范式差异较小， 但仍为正且 cost advantage 不变。论文可以讨论 "paradigm distance" 作为 CRD 效果的调节变量——范式差异越大，CRD
803	    相对于 SC5 的优势越大。
804	
805	    '
806	- name: Error Taxonomy 交叉验证
807	  plan_id: exp-013
808	  description: 'DeepSeek V4 Pro 对 FOLIO 分歧样本做错误分类，与 Qwen3-32B 分类对比， 计算 Cohen''s κ。验证
809	    taxonomy 跨模型稳定性。
810	
811	    '
812	  expected_results:
813	    n_classified: 75
814	    cohens_kappa: 0.67
815	    kappa_CI: '[0.54, 0.80]'
816	    agreement_by_type:
817	      logic_error: 78.8%
818	      negation_error: 72.7%
819	      exec_crash: 90.9%
820	      quantifier_error: 50.0%
821	    deepseek_type_distribution:
822	      logic_error: 28.0%
823	      negation_error: 12.0%
824	      exec_crash: 6.7%
825	      quantifier_error: 1.3%
826	      unclassified: 4.0%
827	    distribution_stability: rank order preserved (logic > negation > crash > quantifier)
828	  result_rationale: '在 best 档位下，Cohen''s κ=0.67 落在 [0.60, 0.80] range，达到 "substantial
829	    agreement" 标准。κ 不更高的原因合理：两个模型对 logic_error vs negation_error 的边界划分有 模糊区域（一些否定相关的逻辑错误可以归入任一类别），这是分类本身的固有模糊性而非
830	    taxonomy 设计缺陷。exec_crash 一致性最高（90.9%）因为执行崩溃是客观可验证的。 quantifier_error 一致性最低（50%）因为
831	    n 太小（仅 4 样本）且量词错误判断需要 深层语义理解。关键发现：两个模型的错误类型分布 rank order 完全一致 （logic > negation
832	    > crash > quantifier），说明 taxonomy 反映的是错误结构而非 模型偏好。DeepSeek 的 logic_error 比例略高（28%
833	    vs 25.5%）、unclassified 略低 （4% vs 0%），因为 DeepSeek 更倾向给出明确分类而非其他 catch-all。
834	
835	    '
836	  tables:
837	  - name: 'Table 15: Cross-Model Taxonomy Validation (n=75 diagnostic samples)'
838	    columns:
839	    - Error Type
840	    - Qwen3-32B %
841	    - DeepSeek %
842	    - Pairwise Agreement
843	    - κ contribution
844	    rows:
845	    - - logic_error
846	      - 25.5%
847	      - 28.0%
848	      - 78.8%
849	      - '0.71'
850	    - - negation_error
851	      - 10.8%
852	      - 12.0%
853	      - 72.7%
854	      - '0.62'
855	    - - exec_crash
856	      - 5.4%
857	      - 6.7%
858	      - 90.9%
859	      - '0.88'
860	    - - quantifier_error
861	      - 2.0%
862	      - 1.3%
863	      - 50.0%
864	      - '0.45'
865	    - - Overall κ
866	      - —
867	      - —
868	      - —
869	      - '0.67'
870	  figures_description:
871	  - 'Fig 20: 4×4 confusion matrix heatmap (Qwen classification vs DeepSeek classification)'
872	  - 'Fig 21: 两个模型的错误类型分布 side-by-side bar chart'
873	  analysis: 'κ=0.67 回应 R9 的 taxonomy validation 要求。substantial agreement 证明 taxonomy
874	    不是单模型的 artifact——不同 LLM 从同一组分歧样本中识别出一致的错误模式。 rank order 稳定性是更强的信号：即使个别样本分类不同，宏观分布结构跨模型复现，
875	    说明四类错误反映了 formalization 的真实失败模式。
876	
877	    '
878	- name: Qwen3-8B 消融
879	  plan_id: exp-010
880	  description: '低能力模型上的诊断率和分歧率变化。P2 优先级。
881	
882	    '
883	  expected_results:
884	    n: 204
885	    C1_disagree_rate: 55.4%
886	    C2_diagnostic_rate: 74.5%
887	    asymmetry: 2.8:1 (FOL-favored, compressed)
888	    fol_accuracy: 58.3%
889	    code_accuracy: 47.1%
890	    C4_aggregate: +2.1pp
891	  result_rationale: '在 best 档位下，8B 模型 C1 上升到 55.4%（更弱模型→更多 formalization 错误→更多分歧），
892	    但 C2 降至 74.5%（更多分歧来自"两侧都错"的 correlated failure，诊断性下降）。 这个 C1↑C2↓ 的 tradeoff 是
893	    model-capability 对 CRD 有效性的重要 characterization： 存在一个能力下限，低于此 CRD 的诊断价值被 correlated
894	    failure 侵蚀。 不对称比压缩到 2.8:1 因为 8B 的 FOL 能力下降更快（形式逻辑对模型能力更敏感）。 作为 P2 实验，这提供了有价值的
895	    scaling 分析但不影响核心 claim。
896	
897	    '
898	  tables:
899	  - name: 'Table 16: Model Scale Ablation on FOLIO'
900	    columns:
901	    - Model
902	    - C1
903	    - C2
904	    - Asymmetry
905	    - FOL Acc
906	    - Code Acc
907	    rows:
908	    - - Qwen3-32B
909	      - 42.2%
910	      - 87.2%
911	      - 5.6:1
912	      - 78.4%
913	      - 59.8%
914	    - - Qwen3-8B
915	      - 55.4%
916	      - 74.5%
917	      - 2.8:1
918	      - 58.3%
919	      - 47.1%
920	    - - DeepSeek V4 Pro
921	      - 38.7%
922	      - 83.5%
923	      - 4.2:1
924	      - 81.2%
925	      - 64.7%
926	  figures_description:
927	  - 'Fig 22: Model capability vs C1/C2 scatter plot (三模型)'
928	  analysis: '三个模型形成 capability 梯度（8B < 32B < DeepSeek Pro），C2 单调递增， C1 单调递减——完美的 scaling
929	    story。论文 1 段 discussion 即可，不需要更多。
930	
931	    '
932	- name: GPQA Diamond 扩展
933	  plan_id: exp-011
934	  description: '科学知识推理，SymPy/Python 双可执行表征。P2 优先级。
935	
936	    '
937	  expected_results:
938	    n: 150
939	    C1_disagree_rate: 22.0%
940	    C2_diagnostic_rate: 72.7%
941	    asymmetry: 1.4:1 (slight Python-favored)
942	    note: C2 略低于 70% gate——科学推理中 domain knowledge 错误占比高，CRD 对 knowledge gap 诊断力有限
943	  result_rationale: '在 best 档位下，GPQA C1=22% 较低（科学推理需要 domain knowledge 而非纯 formalization，
944	    两条路径的差异更多来自知识错误而非表征差异），C2=72.7% 在 70% gate 边缘。 这是 CRD 适用边界的有价值 characterization：cross-representation
945	    disagreement 对 formalization errors 诊断力强，对 domain knowledge errors 诊断力弱。 作为 P2
946	    可选实验，如果时间不够可以省略，核心三基准已足够。
947	
948	    '
949	  tables:
950	  - name: 'Table 17: Cross-Domain CRD Effectiveness'
951	    columns:
952	    - Domain
953	    - Benchmark
954	    - C1
955	    - C2
956	    - Primary Error Source
957	    rows:
958	    - - Logic
959	      - FOLIO
960	      - 42.2%
961	      - 87.2%
962	      - Formalization
963	    - - Logic
964	      - LogiQA
965	      - 34.0%
966	      - 81.5%
967	      - Formalization
968	    - - Math
969	      - MATH L5
970	      - 28.5%
971	      - 76.0%
972	      - Computation
973	    - - Science
974	      - GPQA
975	      - 22.0%
976	      - 72.7%
977	      - Knowledge gap
978	  figures_description:
979	  - 'Fig 23: Domain × C2 effectiveness 趋势图——formalization-heavy 域 CRD 最有效'
980	  analysis: 四基准形成清晰的域梯度：纯逻辑 > 数学 > 科学，C2 随 formalization 占比下降。 这是 best 档位的 bonus result——不是每个域都好用恰恰证明我们理解了
981	    CRD 的机制和边界。 但 GPQA 作为 P2 实验，若时间不足可省略，不影响核心结论。
982	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa6f2bd6-4655-4a2f-b209-234220680dab",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "4b0f3a9b-3316-48a7-be02-a165e118de55",
  "sourceToolAssistantUUID": "fa6f2bd6-4655-4a2f-b209-234220680dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T07:50:10.062Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GG7iFYQbXiwgwL2ro4gm9z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b0f3a9b-3316-48a7-be02-a165e118de55",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zJ7GPirWfJM8BA5Jot",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b03e04d8-041f-44e0-bb3e-99abe297cf08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F1sFNHSxvMjP4GitV5mKz7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 366,
      "cache_read_input_tokens": 39900,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 366
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 39900,
          "cache_creation_input_tokens": 366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 366,
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

_source line 36 · 2026-05-15T07:50:10.071Z_

<details><summary>↩ Tool result · `toolu_01GG7iFYQbXiwgwL2ro4gm9z`</summary>

```text
1	experiments:
2	  # === P0: Must-have for EMNLP submission ===
3	
4	  - id: exp-001
5	    claim: [1, 2, 3]
6	    description: >
7	      FOLIO 完整分析（MVP 数据深度挖掘）: 基于 204 样本 MVP 数据，完成：
8	      (a) 统计显著性检验（Bootstrap 95% CI + Fisher exact test）
9	      (b) 错误类型详细分类和分布
10	      (c) GT=Unknown vs non-Unknown 子集 C1-C5 分层分析
11	      (d) 分歧不对称性 5.6:1 breakdown
12	      (e) FOL/Code 失败相关性定量分析（phi coefficient / tetrachoric correlation）— Claim 3 核心支撑
13	      (f) cost-effectiveness 分析（每单位 token 成本的 accuracy gain）
14	      不需要新实验运行，纯分析。
15	    priority: P0
16	    gpu_budget_hours: 0
17	    deps: []
18	    registry_id: mvp_pipeline_004
19	    status: data_ready
20	
21	  - id: exp-002
22	    claim: [1, 2]
23	    description: >
24	      跨模型消融（FOLIO）: 三组条件对比——
25	      (a) Qwen3-32B FOL + Qwen3-32B Code（MVP baseline，within-model）
26	      (b) DeepSeek V4 Pro FOL + DeepSeek V4 Pro Code（within-model DeepSeek 对照）
27	      (c) DeepSeek V4 Pro FOL + Qwen3-32B Code（cross-model）
28	      目的：区分分歧来源是表征差异还是模型能力差异。FOLIO 204 样本。
29	    priority: P0
30	    gpu_budget_hours: 4
31	    deps: [exp-001]
32	    api_cost_estimate: "$30-50 (DeepSeek V4 Pro 2 组 + Qwen Cloud 1 组)"
33	
34	  - id: exp-003
35	    claim: [1, 2, 3]
36	    description: >
37	      ProofWriter 扩展: 先跑 20-30 样本 pilot 验证 disagree_rate。
38	      ProofWriter 是合成数据（无 NL 歧义），baseline accuracy 可能 >90%，
39	      C1 有低于 10% 的风险。Pilot 通过（disagree_rate ≥ 10%）则全量跑；
40	      Pilot 失败则切换到 LogiQA（自然语言逻辑推理，歧义性更高）。
41	    priority: P0
42	    gpu_budget_hours: 10
43	    deps: []
44	    pilot_required: true
45	    fallback_dataset: LogiQA
46	    sample_count: 200
47	
48	  - id: exp-004
49	    claim: [1, 2, 3]
50	    description: >
51	      MATH Level 5 扩展: 使用两种可执行表征保持 framing 一致——
52	      (a) SymPy 符号推理（代数化简、方程求解）
53	      (b) Python 数值验证（直接计算、枚举、数值近似）
54	      两条路径均可执行，保持与 FOLIO（FOL/Z3 vs Python）一致的
55	      "cross-executable-representation" 框架。不使用 CoT（不可执行）。
56	    priority: P0
57	    gpu_budget_hours: 10
58	    deps: []
59	    sample_count: 200
60	
61	  - id: exp-005
62	    claim: 3
63	    description: >
64	      Repair 机制改进: 多轮 repair（max 3 rounds）、加入错误类型特定修复策略、
65	      对比 repair 前后 C4 delta。按 GT label 和 error_type 分层报告，不报 aggregate。
66	      **必须区分两个版本**：
67	      (a) v2-deployable（仅用 stability prediction，不用 GT）— 论文主表报这个
68	      (b) v2-oracle（用 GT 做 error_side 判断）— 仅作上界分析，放 appendix
69	      目标：在 Unknown 子组进一步拉大 delta，在 non-Unknown 子组探索改善空间。
70	    priority: P0
71	    gpu_budget_hours: 4
72	    deps: [exp-001]
73	
74	  # === P1: Important for paper strength ===
75	
76	  - id: exp-006
77	    claim: 3
78	    description: >
79	      Unknown 样本深度分析 + correlated failure 定量:
80	      (a) 为什么 GT=Unknown 样本驱动 C4 delta？Code overclaiming 机制分析
81	      (b) FOL/Code 失败的相关系数（phi coefficient）按 GT label 分层
82	      (c) false agreement rate 量化（两条路径都错但答案一致的比例）
83	      (d) specification-level vs formalization-specific 错误分类
84	    priority: P1
85	    gpu_budget_hours: 0
86	    deps: [exp-001]
87	
88	  - id: exp-007
89	    claim: 3
90	    description: >
91	      Selection vs Repair 消融（Dream 审稿三档均要求）: 检测分歧+定位错误侧后，
92	      直接选正确侧答案 vs 诊断引导修复。按 error_type 分层报告。
93	      Dream 三档 Median 指出 selection nearly matches repair — 需量化。
94	      回应 Reviewer Concern R3。
95	    priority: P0
96	    gpu_budget_hours: 2
97	    deps: [exp-001]
98	
99	  - id: exp-008
100	    claim: 2
101	    description: >
102	      Error Taxonomy 消融: 按错误类型分派修复策略 vs 固定策略（统一重生成），
103	      验证 taxonomy 的规定性价值。
104	    priority: P1
105	    gpu_budget_hours: 2
106	    deps: [exp-005]
107	
108	  - id: exp-009
109	    claim: [1, 2, 3]
110	    description: >
111	      统计显著性全面检验: 对所有 benchmark 的 C1-C5 指标做
112	      bootstrap 95% CI + Fisher exact test / McNemar test，
113	      确保所有 claim 有统计支撑。
114	    priority: P1
115	    gpu_budget_hours: 0
116	    deps: [exp-001, exp-003, exp-004]
117	
118	  # === Dream-driven additions (dream_20260515T060408) ===
119	
120	  - id: exp-012
121	    claim: [1]
122	    description: >
123	      Self-consistency baseline 对比（三档一致 CRITICAL 缺失）:
124	      在 FOLIO + ProofWriter + MATH 上对比:
125	      (a) k=5 FOL-only majority vote
126	      (b) k=5 Code-only majority vote
127	      (c) Single-pass CRD（我们的方法，1 FOL + 1 Code）
128	      目的：隔离 cross-representation 信号 vs 单表征 sampling diversity。
129	      如果 k=5 单表征已达到相近诊断精度，需要 reframe 贡献。
130	      如果 CRD 在更少 token 成本下匹配或超过 k=5，则 cost-effectiveness 是卖点。
131	    priority: P0
132	    gpu_budget_hours: 6
133	    deps: [exp-001]
134	    api_cost_estimate: "$20-30"
135	
136	  - id: exp-013
137	    claim: [2]
138	    description: >
139	      Error Taxonomy 交叉验证（三档一致弱点）:
140	      (a) 用 DeepSeek V4 Pro 对同一批 FOLIO 分歧样本做错误分类，与 Qwen3-32B 分类对比，计算 Cohen's κ
141	      (b) 如果时间允许，50 个样本人工标注（用户或 LLM-as-human-proxy）
142	      (c) 报告分类一致性 + 错误类型分布是否跨模型稳定
143	      目的：回应 Dream 审稿三档一致要求的 taxonomy validation
144	    priority: P1
145	    gpu_budget_hours: 0
146	    deps: [exp-001]
147	    api_cost_estimate: "$10-20"
148	
149	  # === P2: Nice-to-have ===
150	
151	  - id: exp-010
152	    claim: [1, 2]
153	    description: "Qwen3-8B 消融: 低能力模型上的诊断率和分歧率变化。"
154	    priority: P2
155	    gpu_budget_hours: 4
156	    deps: []
157	
158	  - id: exp-011
159	    claim: [1, 2]
160	    description: "GPQA Diamond 扩展: 科学知识推理，SymPy/Python 双可执行表征。"
161	    priority: P2
162	    gpu_budget_hours: 6
163	    deps: [exp-004]
164	
165	timeline:
166	  day_1_2: "exp-001（FOLIO 分析）完成 + exp-003 pilot（30 样本）+ exp-004 数据/prompt 准备 + exp-012 self-consistency baseline 设计"
167	  day_3_4: "exp-003/004 全量 + exp-002（跨模型 3 组）+ exp-005（repair 改进）+ exp-012（self-consistency baseline）+ exp-007（selection vs repair）"
168	  day_5_6: "exp-006/008/009/013 完成；启动论文写作（related work 扩展至 ≥25 refs）"
169	  day_7_8: "Paper Agent 全 5 步流水线（含 reference-audit）"
170	  day_9_10: "Review + iterate + submit ARR"
171	
172	gpu_budget_total:
173	  local_vllm_hours: 42
174	  api_cost_estimate: "$130-200"
175	  note: >
176	    GPU 预算修正（Reviewer 审查）：exp-003 10h, exp-004 10h, exp-005 4h,
177	    exp-007 2h, exp-010 4h, exp-012 6h = 36h GPU + pilot 已用 ~2h。
178	    exp-002/exp-012/exp-013 主要走 API。
179	    单卡串行 ~36h ≈ 1.5 天连续运行。如需加速将申请第二张 GPU。
180	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b03e04d8-041f-44e0-bb3e-99abe297cf08",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "4a08a46d-ee38-4fe4-b752-94c1a06b0845",
  "sourceToolAssistantUUID": "b03e04d8-041f-44e0-bb3e-99abe297cf08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T07:50:13.332Z_

Now I have a thorough understanding of the paper, its experimental setup, the data, and the project context. Let me also check if there's a dream review report for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a08a46d-ee38-4fe4-b752-94c1a06b0845",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zJLwfVnCmykNUAoTp9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18cbadbd-8471-46f0-9039-d521de2f77dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPzqys5W1SkSzmYYFHJGpH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20608,
      "cache_read_input_tokens": 40266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20608,
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

_source line 38 · 2026-05-15T07:50:16.686Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PKU9ph63NciBzLTcgyz4qM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper.tex",
  "offset": 0,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18cbadbd-8471-46f0-9039-d521de2f77dc",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zJLwfVnCmykNUAoTp9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8a08161-6ff0-4fd2-818e-a98018ad2f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPzqys5W1SkSzmYYFHJGpH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20608,
      "cache_read_input_tokens": 40266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20608,
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

_source line 39 · 2026-05-15T07:50:16.692Z_

<details><summary>↩ Tool result · `toolu_01PKU9ph63NciBzLTcgyz4qM`</summary>

```text
0	\documentclass[11pt,a4paper]{article}
1	\usepackage[margin=1in]{geometry}
2	\usepackage{times}
3	\usepackage{latexsym}
4	\usepackage{amsmath}
5	\usepackage{amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage[T1]{fontenc}
11	\usepackage[utf8]{inputenc}
12	\usepackage{hyperref}
13	
14	\newcommand{\method}{CRD}
15	\newcommand{\pp}{\,pp}
16	
17	\title{Cross-Representation Disagreement for Diagnosis and Characterization\\of LLM Formalization Errors}
18	
19	\author{Anonymous}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8a08161-6ff0-4fd2-818e-a98018ad2f48",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "65c45388-ec63-49df-8d31-012cad312728",
  "sourceToolAssistantUUID": "b8a08161-6ff0-4fd2-818e-a98018ad2f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T07:50:17.443Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01URKWbYea2UbVmBAoUmMpvx`</summary>

```json
{
  "pattern": "**/dream_*T071730/**/review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65c45388-ec63-49df-8d31-012cad312728",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zJLwfVnCmykNUAoTp9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30fdc70f-240e-4608-80f7-98973a1a878c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPzqys5W1SkSzmYYFHJGpH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20608,
      "cache_read_input_tokens": 40266,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20608
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 40266,
          "cache_creation_input_tokens": 20608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20608,
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

_source line 41 · 2026-05-15T07:50:17.488Z_

<details><summary>↩ Tool result · `toolu_01URKWbYea2UbVmBAoUmMpvx`</summary>

```text
artifacts/dream_reports/dream_20260515T071730/best/review_context.yaml
artifacts/dream_reports/dream_20260515T071730/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30fdc70f-240e-4608-80f7-98973a1a878c",
  "isSidechain": true,
  "promptId": "c0b3bd87-55fc-424c-9c68-4f2a890faa64",
  "agentId": "a3261b1309aeb449c",
  "type": "user",
  "uuid": "2079893f-83fb-4fba-abb5-5f2b19e59c09",
  "sourceToolAssistantUUID": "30fdc70f-240e-4608-80f7-98973a1a878c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-15T07:51:19.327Z_

I now have a comprehensive understanding of the paper, its experimental design, the underlying data, and the development history. Here is my review.

---

### R1 Review: Methods & Experiments

**Score:** 3/6

**Summary:** The paper introduces CRD, a framework that detects LLM formalization errors by comparing FOL/Z3 and Python outputs, classifies errors into a taxonomy, and localizes the faulty representation. The diagnostic signal (C1, C2, C5) is genuinely interesting and well-characterized. However, the downstream utility remains weak: aggregate repair improvement (C4) is non-significant across all four benchmarks, the error taxonomy achieves only moderate cross-model agreement, and several reported numbers in the paper are "imagined" (generated from a review_context.yaml planning document rather than from actual experimental runs), raising serious reproducibility concerns.

**Strengths:**
- S1: **Well-characterized diagnostic signal with honest statistical reporting.** The paper clearly reports bootstrap CIs and significance tests, and is upfront that C4 (repair delta) is non-significant on every benchmark. The GT-label-stratified analysis revealing the three-way split (Unknown +14.7pp, False +6.7pp, True -13.6pp) is a genuine finding that transforms what could be a negative result into an informative boundary characterization. Reporting both C5-committed (94.6%) and C5-coverage (53.0%) is transparent.

- S2: **Multi-benchmark generalization with meaningful gradient.** Testing across FOLIO, LogiQA, MATH Level 5, and GPQA Diamond traces a clear effectiveness boundary: C2 decreases from 87.2% to 58.0% as the bottleneck shifts from formalization to domain knowledge. The ProofWriter pilot failure (6.7% disagreement, below threshold) and its honest reporting strengthens the characterization. The asymmetry reversal on MATH (Code-favored 1.8:1 vs. FOL-favored 5.6:1) is a substantive cross-domain finding.

- S3: **Cost-efficiency framing is compelling.** CRD requires 2 LLM calls vs. 5 for self-consistency, achieving comparable or superior diagnostic precision on FOLIO at 40% cost. The qualitative advantage (error type classification, localization, paradigm asymmetry characterization) over self-consistency's binary signal is well-argued.

**Weaknesses:**
- W1: **Discrepancy between "imagined" and reported numbers raises serious concerns.** The review_context.yaml contains "imagined_experiments" with pre-specified expected results. Several numbers in the paper exactly match these imagined values (e.g., FOLIO C1/C2/C5, GT-stratified repair deltas), which is expected for exp-001 (analysis of existing MVP data). But for experiments that require new runs (exp-002 cross-model, exp-003 LogiQA, exp-004 MATH, exp-010 Qwen3-8B, exp-011 GPQA, exp-012 SC5 comparison), the paper reports numbers that differ from the imagined values in suspicious ways -- some match closely but are rounded differently (e.g., imagined DeepSeek C2=83.5% vs. paper's 74.0%; imagined LogiQA C2=81.5% vs. paper's 72.0%). The project report.md shows only mvp_pipeline_004 (FOLIO, 204 samples) has actually been run, with the pipeline still running at 127/204 samples. There is no evidence in project files that exp-002 through exp-013 have been executed. If these experiments have not actually been run, the paper is reporting fabricated results.

- W2: **No human annotation baseline for taxonomy validation.** The error taxonomy is validated solely by cross-model LLM agreement (kappa=0.54 on 3-type scheme, 0.43 on 4-type). This is circular -- using LLMs to validate an LLM-generated taxonomy. The paper mentions "LLM-as-proxy evaluation on 50 samples" (kappa=0.61) but this compounds the circularity. Without any human expert annotation, there is no ground truth for whether the taxonomy categories are meaningful or whether LLMs are just agreeing on superficial patterns. A kappa of 0.54 is only "moderate" agreement, and the most theoretically interesting category (quantifier_error) has kappa=0.22 with n=4, making it essentially unvalidated.

- W3: **Aggregate C4 is non-significant on every benchmark, and the stratified analysis relies on GT labels unavailable at inference time.** The paper's honest acknowledgment that C4 is non-significant is appreciated, but the consequence is severe: the method provides no statistically significant accuracy improvement anywhere. The GT-label-stratified analysis (the core of Claim 3) requires knowing the ground-truth label to decide whether to apply repair, which is unavailable at inference time. The paper suggests "practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)" but does not demonstrate that such prediction-based selection works, nor does it evaluate accuracy of predicting the GT label category from CRD signals.

- W4: **The self-consistency comparison is unfair and inconsistent across benchmarks.** On FOLIO, CRD outperforms SC5 (+2.2pp). On LogiQA, CRD underperforms (-4.0pp). On MATH, CRD substantially underperforms (-9.0pp). The paper frames FOLIO as the headline result and dismisses the MATH deficit as "attenuated signal," but an equally valid reading is that CRD only works well on a single benchmark specifically designed for FOL translation. The cost argument (2 calls vs. 5) is also incomplete: CRD requires a Z3 solver, Python execution sandbox, and the diagnosis/classification pipeline, none of which are free.

- W5: **Sample sizes are small for the claims being made.** FOLIO n=204, LogiQA n=200, MATH n=200 -- these are reasonable for a primary analysis but marginal for the many stratified analyses performed. The taxonomy has n=4 for quantifier_error. The cross-model ablation has only 3 conditions. The Qwen3-8B ablation and GPQA experiment appear to have been run on a single model without repetition. Multiple comparisons across many stratified tests inflate false discovery risk despite the Bonferroni correction claimed.

**Questions for Authors:**
- Q1: Can you provide evidence that experiments exp-002 through exp-013 were actually executed (e.g., W&B run logs, raw output files, execution timestamps)? The project report.md shows only mvp_pipeline_004 as having been run. Several numbers in the paper (DeepSeek cross-model, LogiQA, MATH, GPQA, SC5 comparison, 8B ablation) do not appear in any artifact files I can locate. Were these experiments run, or are the results projected/simulated?

- Q2: The GT-label-dependent repair effect is framed as the central finding of Claim 3, but practitioners cannot condition on GT labels at inference time. Have you evaluated a realistic deployment scenario where the decision to repair vs. select is based on CRD's own signals (e.g., stability test output, error type, asymmetry direction) rather than GT labels? What accuracy does such GT-free selection achieve?

**Minor Issues:**
- Several references are incomplete placeholders (HybridMind, VeriCoT, Roundtrip Verification listed as "Anonymous. Preprint."). These need real citations or should be removed.
- The paper switches between "3 stable types" and "4-type taxonomy" without consistent justification. The merge of quantifier_error and exec_crash into formalization_other feels ad hoc -- exec_crash (kappa=0.82) is the most reliable category, while quantifier_error (kappa=0.22) is the least. Merging them loses a validated distinction to save an unvalidated one.
- Table 6 in the paper (cross-model) reports DeepSeek C2=74.0%, but the review_context.yaml "imagines" 83.5%. This 9.5pp gap needs explanation.
- The phi coefficient analysis claims failure decorrelation between cross-model (0.14) and within-model (0.189), but the reduction is only 0.049 -- practically negligible.
- The MATH extension using SymPy vs. Python is a fundamentally different instantiation than FOL+Z3 vs. Python. The paper acknowledges this but still groups them under "CRD" without adequately discussing whether the same framework genuinely applies when neither representation has a formal verification guarantee.

**Confidence:** 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2079893f-83fb-4fba-abb5-5f2b19e59c09",
  "isSidechain": true,
  "agentId": "a3261b1309aeb449c",
  "requestId": "req_011Cb3zJtWxJXPGbyU2HeGPV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "978dd4a8-a2b2-453b-a74e-124520bb0ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno",
  "sessionId": "9c43fc49-c139-4fe6-b53f-6dc66ee43cb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017qoi85pBkXr3gVH1GCgN31",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 60874,
      "output_tokens": 2060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2060,
          "cache_read_input_tokens": 60874,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 716,
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
