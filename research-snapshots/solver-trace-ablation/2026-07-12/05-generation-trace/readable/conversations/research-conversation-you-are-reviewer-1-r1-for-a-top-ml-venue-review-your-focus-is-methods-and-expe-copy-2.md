# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. Review the following paper

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a22073527386a7c5b.jsonl`
- **Structured JSON:** [`447dbcaa129b0b0c2607.json`](../../sessions/44/447dbcaa129b0b0c2607.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

60 recorded events

### User

_source line 1 · 2026-05-13T22:42:18.543Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. Review the following paper and produce a structured review.

## Paper Summary

**Title:** "Solver Trace Ablation Reveals Reward Hacking in GRPO-Trained Formalizers: A Principled Negative Result"

**Core idea:** The paper introduces Solver Trace Ablation (STA), a framework grounded in the RIP (Reachability-Infection-Propagation) model from mutation testing, for deriving structural rewards (ISR = Intensional Structural Reward) from solver execution traces. STA systematically ablates proof components and re-runs the solver to measure structural necessity. The paper reports a principled negative result: STA works as a diagnostic (detecting ~70% of degenerate outputs) but fails as a training reward (reduces prove rate from 0.24 to 0.11 without improving structural quality).

**Key results:**
- Exec-only GRPO: prove rate 0.28 at step 500, but ISR/PR ratio drops from 0.82→0.29 (reward hacking)
- Exec+STA GRPO (α=β=0.5): prove rate only 0.13, ISR/PR ratio 0.27 (worse on both dimensions)
- Held-out: base model ISR/PR=0.53 > exec+STA 0.30 > exec-only 0.26 — GRPO itself induces degeneracy
- O(1) vs O(N) ablation: O(1) tautology-only check has near-zero discriminability (0.02 vs 0.31)
- 6 weight ablation configs (α/β ratios × fixed/sigmoid): no stable operating point found
- Prolog STA instantiation failed (65% solver timeout, prove rate 0.03, training terminated at step ~300)
- Cross-logic transfer: no positive transfer (mean Δ = -0.015)
- SFT on 500 gold translations: PR=0.30, ISR/PR=0.50, hack%=50% — dominates GRPO on all metrics
- 200-sample hacking taxonomy: 4 modes identified (tautology injection 28%, vacuous quantification 19%, premise redundancy 14%, trivial conclusion 8%), ISR overall sensitivity ~70%, κ=0.72

**Model:** Qwen2.5-1.5B, FOL+Prover9, GRPO K=8, 500 steps, 3 seeds for primary comparison, 1 seed for ablations

**Experimental design reference (planned experiments vs. what appears in paper):**
- plan_001: FOL exec-only baseline (500 steps, 3 seeds) → COVERED in Table 1
- plan_002: FOL exec+STA (500 steps, 3 seeds) → COVERED in Table 2
- plan_003: Held-out evaluation → COVERED in Table 3
- plan_004: O(1) vs O(N) ablation → COVERED in Table 4
- plan_005: Weight ablation (6 configs, 200 steps, 1 seed) → COVERED in Table 5
- plan_006: Prolog instantiation → COVERED in Table 6
- plan_007: Multi-logic GRPO → NOT RUN (blocked by plan_006 failure)
- plan_008: Cross-logic transfer → COVERED in Table 7
- plan_009: SFT baseline → COVERED in Table 8
- plan_010: SMT-LIB → NOT RUN (deprioritized)
- plan_011: Qwen3-8B scaling → NOT RUN (deprioritized)
- plan_012: Hacking characterization → COVERED in Tables 9-10

## Your Review Focus

Evaluate:
1. **Methodological soundness**: Is the STA/ISR formulation well-defined? Is the RIP adaptation coherent? Any flaws in the derivation?
2. **Experimental rigor**: Are experiments sufficient to support claims? Statistical validity (3 seeds enough? 1 seed for ablations adequate?)? Controls? Missing baselines?
3. **Experimental coverage**: How well does the paper cover its planned experiments? Are the not-run experiments (plan_007, 010, 011) properly justified?
4. **Reproducibility**: Enough detail to reproduce? Hyperparameters, training details?
5. **Claim-evidence alignment**: Do the results actually support the three stated contributions?
6. **Weaknesses in experimental design**: Single model size, single logic type, sample sizes, etc.

## Output Format

```
## R1 Review: Methods & Experiments

### Summary
[2-3 sentences]

### Strengths
[Bulleted list, 4-6 items]

### Weaknesses
[Bulleted list, 4-6 items, each with severity: minor/moderate/major]

### Questions for Authors
[3-5 specific questions]

### Detailed Comments
[Paragraph-level analysis of key issues]

### Scores
- Soundness: [1-4]
- Empirical Rigor: [1-4]
- Reproducibility: [1-4]
- Overall recommendation: [1-6, where 1=Strong Reject, 6=Strong Accept]
- Confidence: [1-5]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "d24f55da-abbf-440f-910b-9e5bb7f1db18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T22:42:18.549Z_

```json
{
  "parentUuid": "d24f55da-abbf-440f-910b-9e5bb7f1db18",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
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
  "uuid": "72cef4e7-1bae-4f8a-ad1e-179b4acb8bec",
  "timestamp": "2026-05-13T22:42:18.549Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T22:42:21.165Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72cef4e7-1bae-4f8a-ad1e-179b4acb8bec",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NiKnBQ44bms95aZHEz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42604348-955a-471b-a720-b6e2c7787711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqHc9nW9BYugfu2ezzUq3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15358,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15358,
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

_source line 4 · 2026-05-13T22:42:22.611Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XtrVwojG12uax7SG87T2oT`</summary>

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
  "parentUuid": "42604348-955a-471b-a720-b6e2c7787711",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NiKnBQ44bms95aZHEz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91d3915d-96a6-4a75-a9bc-a28a58005950",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqHc9nW9BYugfu2ezzUq3V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15358,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15358
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15358,
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

_source line 5 · 2026-05-13T22:42:22.616Z_

<details><summary>↩ Tool result · `toolu_01XtrVwojG12uax7SG87T2oT`</summary>

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
  "parentUuid": "91d3915d-96a6-4a75-a9bc-a28a58005950",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "7d56f384-5308-44c0-be1c-abbbf3407815",
  "sourceToolAssistantUUID": "91d3915d-96a6-4a75-a9bc-a28a58005950",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-13T22:42:25.419Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01BPgxrtppvWucM6xHsMadJ6`</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d56f384-5308-44c0-be1c-abbbf3407815",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NidH9A5kfY2Ef1sPN6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d8d7799-f94e-4ecf-9845-f1175bea1727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018W83MwGGGfzFqLnD8ZueKH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 7 · 2026-05-13T22:42:25.482Z_

<details><summary>↩ Tool result · `toolu_01BPgxrtppvWucM6xHsMadJ6`</summary>

```text
{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (16 个)\n\n- **plan003-eval-exec-only-r5**: PREPARING — \n- **plan005-sta-low-s42**: PREPARING — \n- **plan001-exec-only-s42**: PREPARING — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-gt-isr-baseline**: DONE (success) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **sta-phase1-exec-sta-r5** (success): —\n- **sta-phase1-exec-only-r5** (success): —\n- **sta-phase1-exec-sta-r4** (negative): —\n\n## 趋势\n成功 4 / 负向 2 / 失败 6 / 共 12\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-39279: 无 GPU 信息\n\n## 告警\n- sta-phase1-exec-only: 训练失败 — unknown\n- sta-phase1-exec-sta: 训练失败 — unknown\n- sta-phase1-exec-only-r2: 训练失败 — unknown\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\n- sta-phase1-exec-only-r3: 训练失败 — unknown\n- sta-phase1-exec-sta-r3: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d8d7799-f94e-4ecf-9845-f1175bea1727",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "c6e629d9-43c8-45e2-8413-5a14ad30d35d",
  "sourceToolAssistantUUID": "5d8d7799-f94e-4ecf-9845-f1175bea1727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T22:42:26.025Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GJD2Ppo6Z9skTFdCkY3gVo`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6e629d9-43c8-45e2-8413-5a14ad30d35d",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NidH9A5kfY2Ef1sPN6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81ae1cea-271b-48a4-839c-9ad0c29a6f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018W83MwGGGfzFqLnD8ZueKH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15358,
      "output_tokens": 162,
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
          "output_tokens": 162,
          "cache_read_input_tokens": 15358,
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-13T22:42:26.035Z_

<details><summary>↩ Tool result · `toolu_01GJD2Ppo6Z9skTFdCkY3gVo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **sta-phase1-exec-sta-r5** (success): —\\n- **sta-phase1-exec-only-r5** (success): —\\n- **sta-phase1-exec-sta-r4** (negative): —\\n\\n## 趋势\\n成功 4 / 负向 2 / 失败 6 / 共 12\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\n\", \"total_chars\": 570, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81ae1cea-271b-48a4-839c-9ad0c29a6f40",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "329dd5d0-ab98-4abf-8026-cbc7d0e28f78",
  "sourceToolAssistantUUID": "81ae1cea-271b-48a4-839c-9ad0c29a6f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T22:42:29.640Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01S3ArAtwNVNCep6his8asn9`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "329dd5d0-ab98-4abf-8026-cbc7d0e28f78",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NiswT8k7RntMLeKfMa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86a521d1-4479-4067-ab5d-9f200fab4202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuZuDFgbiRc6eW3yiwEtUn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 16804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1438,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 11 · 2026-05-13T22:42:29.660Z_

<details><summary>↩ Tool result · `toolu_01S3ArAtwNVNCep6his8asn9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md\", \"content\": \"# solver-trace-ablation — Research Dashboard\\n\\n> 最后更新: 2026-05-13 22:16 UTC | 更新原因: Kill Criteria #4 量化阈值（Reviewer 建议）：3-seed mean < 25% AND last100 slope ≤ 0\\n\\n## 核心方向\\nSTA（Solver Trace Ablation）：首次将 mutation testing RIP 框架系统性引入 RL reward design，为 neurosymbolic formalizer 的 GRPO 训练提供 intensional verification reward。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 部分通过——STA 机制有效但训练集成权重需调整）\\n- **基础设施**: westd-39279 × 2 RTX PRO 6000 96GB ✅\\n- **MVP 结论**: full STA 连续 ISR 有区分力（GT=0.56 vs model=0.064）；但 50/50 权重导致 prove_rate 退化至 baseline 以下（0.10 < 0.12）；O(1) fast_isr 无效\\n- **MVP Pass**: #1✅ #2✅ #3✅ #4❌(ISR指标不可比) #5❌(accuracy差5pp+退化) | Kill criteria 未触发\\n- **⚠️ 因果归因未定**: ISR/PR 下降可能是检测 hacking 也可能是 STA 权重惩罚效应，plan_003 是消歧实验（D005）\\n- **Dream**: dream_20260513T215750 pending\\n- **Agent 状态**: 正在处理，队列有 P0 训练指令待执行\\n\\n## 实验计划摘要（详见 experiment_plan.yaml）\\n- **P0**（~13h）: FOL 500步×3seed + eval + O(1)vsO(N) + weight ablation\\n- **P1**（~8h）: Prolog + multi-logic + SFT baseline + hacking annotation\\n- **P2**（~9h）: SMT-LIB + 8B scaling\\n- **Pivotal**: plan_003（因果消歧）+ plan_005（weight ablation）共同决定 \\\"STA as reward\\\" vs \\\"STA as monitor\\\" 叙事\\n\\n## Research Phase Kill Criteria\\n1. plan_005 所有权重配比（0.1/0.2/0.3 + bonus mode + curriculum）均无法让 exec+STA ≥ exec-only → 论文退化为 \\\"STA as monitoring metric\\\"，claim 力度大幅减弱，与用户讨论是否继续\\n2. plan_001/002（500步3seed）STA 条件一致性差于 exec-only → 同上\\n3. plan_003 held-out eval 确认 ISR/PR 下降但非 hacking（人工标注 plan_012 无 shortcut 证据）→ \\\"检测 hacking\\\" claim 不成立，需重写 story\\n4. plan_001 exec-only 500步 prove_rate 未达阈值 → GRPO+exec reward 本身未产生提升，问题在基座训练而非 STA，需重新评估整个 GRPO pipeline\\n   - **硬阈值**: 3-seed 均值 prove_rate < 25%（baseline 12% 的 ~2倍）**且** last-100-step prove_rate 趋势斜率 ≤ 0（不再上升）\\n   - 两个条件同时满足才触发 kill；若均值 < 25% 但斜率仍正（仍在学习），延长到 800 步再判\\n\\n## 近期任务（GPU 排列）\\n- [ ] cuda:0 → plan_001: exec-only 500步 seed=42（baseline + Kill Criteria #4）\\n- [ ] cuda:1 → plan_003: exec-only checkpoint full STA eval（消歧，eval-only 快速）→ 完成后 plan_005: sta_weight=0.1 训练\\n- [ ] 并行准备: Prolog STA instantiation + SFT baseline 数据\\n- [ ] Dream 回调后评估 framing/plan 是否调整\\n- [ ] registry 修正: exec-sta-r5 conclusion → \\\"negative\\\"\\n\\n## GPU 预算\\n- 本地: westd-39279 × 2 RTX PRO 6000 96GB（cuda:0, cuda:1）\\n- 云: 暂不需要\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-13 | paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_ | sta-phase1-exec-sta-r5, plan_003 |\\n| D005 | 2026-05-13 | ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验 | sta-phase1-exec-sta-r5, sta-phase1-exec-only-r5 |\\n| D004 | 2026-05-13 | Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化） | sta-phase1-exec-sta-r5, sta-phase1-exec-only-r5 |\\n| D003 | 2026-05-13 | Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重 | sta-phase1-exec-only-r4, sta-phase1-exec-sta-r4 |\\n| D002 | 2026-05-13 | MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline +  | — |\\n| D001 | 2026-05-13 | MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA r | — |\\n\\n\\n\", \"total_chars\": 2869, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86a521d1-4479-4067-ab5d-9f200fab4202",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "e202b370-504a-4742-b812-71b55d9659c0",
  "sourceToolAssistantUUID": "86a521d1-4479-4067-ab5d-9f200fab4202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T22:42:30.514Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01J2Hk5Ks6yyYyQBGuaaWdLv`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e202b370-504a-4742-b812-71b55d9659c0",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NiswT8k7RntMLeKfMa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d16b0a1-daf2-448d-adfc-5e3266afa2ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuZuDFgbiRc6eW3yiwEtUn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 16804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1438,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 13 · 2026-05-13T22:42:30.525Z_

<details><summary>↩ Tool result · `toolu_01J2Hk5Ks6yyYyQBGuaaWdLv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# solver-trace-ablation — Memory\\n\\n## 环境信息 (2026-05-13)\\n\\n### westd-39279 服务器\\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2, Z3 4.16.0.0\\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\\n- **代码路径**: `/root/solver-trace-ablation/`\\n\\n### 决策记录\\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\\n- Prover9 从 LADR 源码编译（apt 无包）\\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\\n\\n## 数据 (2026-05-13)\\n\\n### 数据源变更：ProofWriter → FOLIO\\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\\n- Phase 0 子集 100 条，训练子集 500 条\\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\\n\\n## Phase 0 关键发现 (2026-05-13)\\n\\n### Base Model ISR Baseline (sta-phase0-baseline)\\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\\n\\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\\n- **MVP Pass #2 验证**: GT ISR 0.559 > 0.5 ✅，好的 formalization ISR 高\\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\\n\\n### Prover9 局限性\\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\\n- Phase 1 训练中 reward 信号主要来自 `true` 类样本\\n\\n### ISR 已知盲区\\n- premise-conclusion 重复的 trivial formalization 可能获高 ISR\\n- 需在论文 Discussion 中讨论此局限\\n\\n## Phase 1 关键经验 (2026-05-13)\\n\\n### fast_isr_fol 失败教训 (r4)\\n- `fast_isr_fol()` 是二值 tautology gate (0/1)，Qwen3-4B 不产生 tautology → ISR ≡ prove_rate → 两条件零差异\\n- **教训：binary ISR 无法提供有意义的 reward shaping 信号，必须用连续 ISR**\\n\\n### full STA reward 成功验证 (r5) — MVP PASS ✅\\n**配置变更**: r4→r5: `fast_sta_reward` → `sta_reward` (continuous ISR) + K=4→8\\n\\n| 指标 | exec-only (r5) | exec-sta (r5) | Δ |\\n|------|----------------|---------------|---|\\n| overall prove_rate | 0.151 | 0.100 | +0.051 |\\n| overall isr_mean | 0.148 | 0.043 | +0.104 |\\n| last-20 prove_rate MA | 0.200 | 0.150 | +0.050 |\\n| last-20 isr_mean MA | 0.200 | 0.050 | **+0.150** |\\n| ISR/PR ratio (last-20) | 1.000 | 0.330 | — |\\n\\n**核心发现**:\\n1. exec-only: isr_mean ≡ prove_rate（100步无例外）— binary ISR 是冗余信号\\n2. exec-sta: isr_mean << prove_rate（overall 43%, last-20 仅 33%）— continuous ISR 真正度量质量\\n3. **Reward hacking 早期信号**: exec-sta prove_rate +85% 但 ISR 平坦 (-4%)，ISR/PR 比从 64%→33%。模型学会更多 proof 但 formalization 质量下降\\n4. K=8 比 K=4 有效减少全零 batch（但 prove_rate 整体仍偏低 10-20%）\\n5. step 速度: exec-only ~9.4s, exec-sta ~10.1s（STA overhead 约 7%，可接受）\\n\\n### GPU 隔离教训 (r3)\\n- `CUDA_VISIBLE_DEVICES` 必须在 `bash -c` 内部设置，不能依赖外部 shell 继承\\n- 两进程未隔离 → 都加载到 GPU 0 → OOM (SIGKILL 137)\\n\\n### Config merge 教训 (r2)\\n- argparse `store_true` 默认 False（非 None），`is None` 检查跳过 YAML 值\\n- 修复：`parser.set_defaults(**yaml_cfg)` 后重新 parse CLI args\\n\\n### reward_log.jsonl 隔离问题\\n- 多轮 run 数据追加到同一文件，分析时必须按 timestamp 过滤\\n- 后续应每次 run 使用独立 output_dir\\n\\n## MVP 总结 (2026-05-13)\\n\\n| Pass 标准 | r4 | r5 | 说明 |\\n|-----------|-----|-----|------|\\n| #1 STA ISR 可靠运行 | ⚠️ | ✅ | solver 100%, ~10s/step |\\n| #2 ISR 有区分度 | ❌ | ✅ | GT 0.559 vs base 0.064; continuous ISR 解耦 |\\n| #3 ISR 趋势分离 | ❌ | ✅ | last-20 ISR: 0.200 vs 0.050 (Δ=0.150) |\\n| #4 accuracy 无崩溃 | ✅ | ✅ | prove_rate 两组均提升 |\\n\\n**MVP PASS。项目进入全实验矩阵阶段。**\\n\", \"total_chars\": 3433, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d16b0a1-daf2-448d-adfc-5e3266afa2ef",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "5de1bf7f-505f-43c3-896f-71a006201cd6",
  "sourceToolAssistantUUID": "2d16b0a1-daf2-448d-adfc-5e3266afa2ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T22:42:30.695Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WsBA5WptssCwiRAPmVtcnA`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5de1bf7f-505f-43c3-896f-71a006201cd6",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NiswT8k7RntMLeKfMa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4002879f-2c3f-4c41-95e1-29d9da9404ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuZuDFgbiRc6eW3yiwEtUn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 16804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1438,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 15 · 2026-05-13T22:42:30.705Z_

<details><summary>↩ Tool result · `toolu_01WsBA5WptssCwiRAPmVtcnA`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4002879f-2c3f-4c41-95e1-29d9da9404ca",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "b806c7e8-043f-4f74-bb1e-47a9aa50da24",
  "sourceToolAssistantUUID": "4002879f-2c3f-4c41-95e1-29d9da9404ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T22:42:31.211Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013iCnrhT7Q4jR7N5mBMf4tV`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b806c7e8-043f-4f74-bb1e-47a9aa50da24",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NiswT8k7RntMLeKfMa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62c2611d-1c3c-4de3-8e68-0d3b9a397eae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuZuDFgbiRc6eW3yiwEtUn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 16804,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1438
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 16804,
          "cache_creation_input_tokens": 1438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1438,
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

_source line 17 · 2026-05-13T22:42:31.225Z_

<details><summary>↩ Tool result · `toolu_013iCnrhT7Q4jR7N5mBMf4tV`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62c2611d-1c3c-4de3-8e68-0d3b9a397eae",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "3e8f5eac-9d57-47fb-b17a-a62eeabc6740",
  "sourceToolAssistantUUID": "62c2611d-1c3c-4de3-8e68-0d3b9a397eae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T22:42:37.493Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MdZnUyEtbztfJd2UsfNNke`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e8f5eac-9d57-47fb-b17a-a62eeabc6740",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NjGDtt4eGork4LfDgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbdb52eb-6e9e-4b60-8d03-cecffaed1cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3pWa2acQfBk1ujZ5nByXr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4598,
      "cache_read_input_tokens": 18242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4598,
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

_source line 19 · 2026-05-13T22:42:37.503Z_

<details><summary>↩ Tool result · `toolu_01MdZnUyEtbztfJd2UsfNNke`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (2 条，精简自原始 5 条)\\n\\n### Claim 1: STA as Reward Design Methodology\\nSolver Trace Ablation (STA), grounded in the Reachability-Infection-Propagation (RIP) framework from mutation testing theory, provides a **general, solver-agnostic procedure** for deriving intensional verification rewards from solver execution semantics. For any solver+language pair, a 5-step derivation protocol (pilot → collect shortcuts → classify → map RIP → design check) produces domain-specific structural rewards. This is the first application of the RIP framework to RL reward design.\\n\\n**MVP 证据**: Full STA 在 FOL+Prover9 上提供连续 ISR（0.125-0.889），训练过程中观察到 ISR/PR 比从 64%→33% 的下降趋势。O(1) 近似（tautology-only check）信号过粗无效——重要阴性结果，证明了 full component ablation 的必要性。\\n**⚠️ 因果归因待验证**: ISR/PR 下降可能是 (A) STA 检测到 hacking，也可能是 (B) 50/50 STA 权重抑制 prove 行为的惩罚效应（ISR 绝对值始终 ~0.05 ≈ pretrained 水平）。plan_003（exec-only checkpoint 用 full STA 评估）是消歧实验——完成前不可用 \\\"检测 hacking\\\" 因果表述。\\n\\n### Claim 2: Multi-Logic GRPO Empirical Findings\\nMulti-logic GRPO training across structurally different formal languages (FOL→Prover9, Prolog→SWI-Prolog, SMT-LIB→Z3) exhibits measurable cross-logic transfer patterns and logic-type-specific reward hacking modes. STA-derived rewards detect and quantify these phenomena.\\n\\n**MVP 证据**: 待验证（FOL 单逻辑已验证，multi-logic 需 research 阶段实验）。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with solver-verified rewards trains formalizers that achieve high execution accuracy but produce structurally degenerate outputs (reward hacking). Existing structural reward designs are ad-hoc heuristics with no principled derivation.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) demonstrates cross-solver GRPO transfer but uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work provides a general derivation procedure for structural rewards from solver semantics.\\n- **Our framing**: We adapt the RIP framework from mutation testing — a component is \\\"necessary\\\" iff its ablation changes the solver's output — to derive intensional verification rewards. STA fills the **dense + automatic** cell in the ORM-PRM reward taxonomy (ORM=sparse+automatic, PRM=dense+manual, STA=dense+automatic via solver semantics). This positions STA not as \\\"a new algorithm\\\" but as \\\"the first systematic transfer of mutation testing methodology to RL reward design.\\\"\\n- **Headline result template**: \\\"On FOLIO/ProofWriter/LogiQA, STA-rewarded GRPO achieves &lt;X>% formalization accuracy with &lt;Y>% ISR, compared to &lt;Z>% accuracy / &lt;W>% ISR for execution-only GRPO — maintaining accuracy while detecting and reducing structural degeneracy.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Core contribution is neurosymbolic (NLP + formal logic), directly in the NLP and Symbolic Reasoning track. Formal verification + RL reward design is highly relevant.\\n- **\\\"Old wine\\\" risk**: STA's component ablation resembles mutation testing. Mitigation: explicitly acknowledge the RIP origin, claim novelty at the methodology transfer level + empirical findings, not at the algorithm level.\\n- **Scope breadth risk**: Original proposal had 5 contributions — trimmed to 2 core (STA methodology + empirical findings). MLSR framework, hacking taxonomy, STA-IPT duality are secondary analysis within these 2 contributions.\\n- **Single-logic risk**: If only FOL results are available, paper may feel narrow. Mitigation: at minimum include Prolog as second logic type; SMT-LIB as stretch goal.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"STA is just mutation testing applied to FOL\\\"** — Response: yes, that's the point. The contribution is the systematic transfer + empirical validation that it works as RL reward, not algorithmic novelty. The 5-step derivation protocol is the transferable methodology.\\n2. **\\\"O(1) approximation doesn't work\\\"** — Response: this is a feature, not a bug. We report it as a principled negative result showing that domain-specific hacking modes require corresponding ablation granularity.\\n3. **\\\"Low prove rate limits GRPO signal\\\"** — Response: addressed by K=8+ and difficulty-based data selection. Prove rate increases during training (12%→15-20%).\\n4. **\\\"ISR/PR ratio declining even with STA reward\\\"** — Response: 100-step pilot is too short; full runs with curriculum will show whether STA prevents or just detects degradation. Even detection alone is a contribution (monitoring tool).\\n5. **\\\"Only tested on one/two logic types\\\"** — Response: STA derivation protocol is solver-agnostic by design; instantiations for additional logic types follow the same 5-step procedure.\\n\", \"total_chars\": 4814, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbdb52eb-6e9e-4b60-8d03-cecffaed1cdc",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "4b08d446-47f4-4159-b87c-c3778b131cb0",
  "sourceToolAssistantUUID": "fbdb52eb-6e9e-4b60-8d03-cecffaed1cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-13T22:42:38.438Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015HMXKkdSm3Hy1WuohBt3kE`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b08d446-47f4-4159-b87c-c3778b131cb0",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NjGDtt4eGork4LfDgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea3ebae0-33fc-4010-b804-7063445447ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3pWa2acQfBk1ujZ5nByXr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4598,
      "cache_read_input_tokens": 18242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4598,
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

_source line 21 · 2026-05-13T22:42:38.449Z_

<details><summary>↩ Tool result · `toolu_015HMXKkdSm3Hy1WuohBt3kE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差\\n    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)\\n    避免惩罚。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: prove_rate=0.10 < baseline, STA reward 过于惩罚性\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: control\\n    result: prove_rate=0.15, 复现 r4\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 22:13 UTC\\n  summary: ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 有两种解释：(A) STA 检测到 hacking (B) 50/50 权重抑制 prove\\n    行为的惩罚效应。ISR 绝对值 ~0.05 ≈ pretrained 水平支持解释 B。plan_003（用 full STA 评估 exec-only checkpoint）是唯一消歧实验——exec-only\\n    ISR 高→STA reward 导致退化；exec-only ISR 低→GRPO 通病。paper_framing.md 已将 claim 降级为观察性表述，因果表述需等\\n    plan_003 结果。cuda:1 排列改为 plan_003 eval 先行，再 plan_005 training。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: ISR/PR 下降但因果不清\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: baseline\\n    result: prove_rate=0.12, ISR 未用 full STA 评估\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 22:14 UTC\\n  summary: paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_003 为消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 下降存在混淆效应：可能是 STA 检测到 hacking，也可能是 50/50 权重抑制\\n    prove 行为。ISR 绝对值始终 ~0.05 ≈ pretrained 水平，更像惩罚效应。plan_003（exec-only checkpoint\\n    用 full STA 评估）是消歧实验——完成前 paper 不可用因果表述。已修改 paper_framing.md Claim 1 MVP 证据段。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence_source\\n    result: ISR/PR 下降观察到但因果不清\\n  - exp_id: plan_003\\n    role: disambiguation\\n    result: planned\\n  depends_on:\\n  - D004\\n\", \"total_chars\": 3352, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea3ebae0-33fc-4010-b804-7063445447ff",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "fbc0b286-89dc-44e0-aeb4-04a4a9d69b81",
  "sourceToolAssistantUUID": "ea3ebae0-33fc-4010-b804-7063445447ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-13T22:42:38.731Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MPfyYFi49uBuEjdVXgLxDb`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbc0b286-89dc-44e0-aeb4-04a4a9d69b81",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NjGDtt4eGork4LfDgU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "766e2387-4039-45c1-a379-27753406c5fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3pWa2acQfBk1ujZ5nByXr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4598,
      "cache_read_input_tokens": 18242,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4598
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 18242,
          "cache_creation_input_tokens": 4598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4598,
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

_source line 23 · 2026-05-13T22:42:38.747Z_

<details><summary>↩ Tool result · `toolu_01MPfyYFi49uBuEjdVXgLxDb`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "766e2387-4039-45c1-a379-27753406c5fc",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "a4402933-d18d-47cd-b26c-3335b1bf357c",
  "sourceToolAssistantUUID": "766e2387-4039-45c1-a379-27753406c5fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-13T22:42:42.123Z_

Now let me look at the actual paper artifacts and experiment code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4402933-d18d-47cd-b26c-3335b1bf357c",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NjpEjc7Hq9Q9c5j79z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2f178ff-5477-40af-b7d9-7b09c5bfb5c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzsdYGVdmfhYrMZD2kEexs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 22840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4109,
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

_source line 25 · 2026-05-13T22:42:43.552Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0144JTiNJYgN7sqaRUu6CYgC`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2f178ff-5477-40af-b7d9-7b09c5bfb5c7",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NjpEjc7Hq9Q9c5j79z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3bf0f60-db66-45f6-8e65-a9986a592e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzsdYGVdmfhYrMZD2kEexs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 22840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4109,
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

_source line 26 · 2026-05-13T22:42:43.577Z_

<details><summary>↩ Tool result · `toolu_0144JTiNJYgN7sqaRUu6CYgC`</summary>

```text
artifacts/dream_reports/dream_20260513T215750/best/paper.tex
artifacts/dream_reports/dream_20260513T215750/median/paper.tex
artifacts/dream_reports/dream_20260513T215750/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3bf0f60-db66-45f6-8e65-a9986a592e7f",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "aacf5ed6-bd83-499a-b540-192e28b76ceb",
  "sourceToolAssistantUUID": "a3bf0f60-db66-45f6-8e65-a9986a592e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T22:42:44.499Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016vzKa1wTGoxGuY2xz1XadW`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aacf5ed6-bd83-499a-b540-192e28b76ceb",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NjpEjc7Hq9Q9c5j79z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b24d2a17-10b7-4890-a96d-f170294926a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzsdYGVdmfhYrMZD2kEexs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 22840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4109,
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

_source line 28 · 2026-05-13T22:42:44.529Z_

<details><summary>↩ Tool result · `toolu_016vzKa1wTGoxGuY2xz1XadW`</summary>

```text
artifacts/train_grpo.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b24d2a17-10b7-4890-a96d-f170294926a3",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "cd9fba89-b4c2-43b2-956f-25ecc635b7bd",
  "sourceToolAssistantUUID": "b24d2a17-10b7-4890-a96d-f170294926a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T22:42:44.659Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SjrSyuS3AqnEwUq2XrYkaJ`</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd9fba89-b4c2-43b2-956f-25ecc635b7bd",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NjpEjc7Hq9Q9c5j79z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "752abc71-eff1-403f-a79c-fbb6f5786cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzsdYGVdmfhYrMZD2kEexs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 22840,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4109
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 22840,
          "cache_creation_input_tokens": 4109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4109,
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

_source line 30 · 2026-05-13T22:42:44.682Z_

<details><summary>↩ Tool result · `toolu_01SjrSyuS3AqnEwUq2XrYkaJ`</summary>

```text
artifacts/sta-phase0-baseline/data/phase0_baseline_summary.txt
artifacts/manifest.yaml
artifacts/launch_phase1.sh
artifacts/grpo_exec_only.yaml
artifacts/grpo_exec_sta.yaml
artifacts/phase1_r2_diagnosis.md
artifacts/train_grpo.py
artifacts/diagnose_phase1_r3.md
artifacts/dream_reports/dream_20260513T215750/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T215750/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T215750/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T215750/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T215750/best/experiment_data.json
artifacts/dream_reports/dream_20260513T215750/best/paper_framing.md
artifacts/dream_reports/dream_20260513T215750/best/paper.tex
artifacts/dream_reports/dream_20260513T215750/best/paper.aux
artifacts/dream_reports/dream_20260513T215750/best/paper.out
artifacts/dream_reports/dream_20260513T215750/best/paper.pdf
artifacts/dream_reports/dream_20260513T215750/best/paper.log
artifacts/dream_reports/dream_20260513T215750/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T215750/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T215750/median/experiment_data.json
artifacts/dream_reports/dream_20260513T215750/median/paper_framing.md
artifacts/dream_reports/dream_20260513T215750/median/paper.tex
artifacts/dream_reports/dream_20260513T215750/median/paper.aux
artifacts/dream_reports/dream_20260513T215750/median/paper.out
artifacts/dream_reports/dream_20260513T215750/median/paper.pdf
artifacts/dream_reports/dream_20260513T215750/median/paper.log
artifacts/dream_reports/dream_20260513T215750/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T215750/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T215750/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T215750/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T215750/worst/paper.tex
artifacts/dream_reports/dream_20260513T215750/worst/paper.aux
artifacts/dream_reports/dream_20260513T215750/worst/paper.out
artifacts/dream_reports/dream_20260513T215750/worst/paper.pdf
artifacts/dream_reports/dream_20260513T215750/worst/paper.log
artifacts/dream_reports/dream_20260513T215750/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260513T215750/logs/orchestrator.log
artifacts/dream_reports/dream_20260513T215750/best/review_context.yaml
artifacts/dream_reports/dream_20260513T215750/best/review_report.md
artifacts/dream_reports/dream_20260513T215750/logs/review_best.log
artifacts/dream_reports/dream_20260513T215750/median/review_context.yaml
artifacts/dream_reports/dream_20260513T215750/median/review_report.md
artifacts/dream_reports/dream_20260513T215750/logs/review_median.log
artifacts/dream_reports/dream_20260513T215750/worst/review_context.yaml
artifacts/dream_reports/dream_20260513T215750/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "752abc71-eff1-403f-a79c-fbb6f5786cfb",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "5342db19-d662-4ecd-ae62-0bd21ddf9a05",
  "sourceToolAssistantUUID": "752abc71-eff1-403f-a79c-fbb6f5786cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T22:42:48.407Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YAUoPayqDyMxok7phRG3xJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5342db19-d662-4ecd-ae62-0bd21ddf9a05",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NkFaUpfRfsmpnUu6hz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "693cf585-e617-4207-abf0-3a3391ebd16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tksg6gcmix626K7ofwS4S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1433,
      "cache_read_input_tokens": 26949,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1433
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 101,
          "cache_read_input_tokens": 26949,
          "cache_creation_input_tokens": 1433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1433,
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

_source line 32 · 2026-05-13T22:42:48.665Z_

<details><summary>↩ Tool result · `toolu_01YAUoPayqDyMxok7phRG3xJ`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}
12	\usepackage{natbib}
13	\renewcommand{\bibsection}{\section*{References}}
14	
15	\title{Solver Trace Ablation: Dense Structural Rewards for\\Formal Reasoning via Mutation Testing}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	% ============================================================
23	\begin{abstract}
24	Training language models to produce formal logical representations via reinforcement learning (e.g., GRPO with solver-verified rewards) achieves high execution accuracy but introduces \emph{structural degeneracy}: models discover extensional shortcuts---tautological premises, vacuous quantifiers, over-constrained formulas---that satisfy solvers without encoding the intended logical content. We propose \textbf{Solver Trace Ablation (STA)}, a reward design methodology grounded in the Reachability-Infection-Propagation (RIP) framework from mutation testing theory. STA derives dense, automatic structural rewards by systematically ablating components of solver inputs and measuring their contribution to solver outcomes. We introduce a 5-step derivation protocol that instantiates STA for any solver--language pair. Experiments with GRPO training of Qwen3-4B and Qwen3-8B across three formal languages---first-order logic (Prover9), Prolog (SWI-Prolog), and SMT-LIB (Z3)---demonstrate that STA-rewarded training maintains prove rates comparable to execution-only training (0.30 vs.\ 0.28 for FOL) while preserving structural integrity (ISR/PR ratio 0.65 vs.\ 0.35). On held-out evaluation, STA-trained models reduce reward hacking prevalence from 45\% to 18\%. We further show that the O(1) tautology-only approximation fails as a reward signal, validating the necessity of full component ablation. Multi-logic training exhibits positive cross-logic transfer, and STA's benefits are scale-invariant from 4B to 8B parameters.
25	\end{abstract}
26	
27	% ============================================================
28	\section{Introduction}
29	\label{sec:intro}
30	
31	Reinforcement learning with execution-based rewards has emerged as a powerful paradigm for training language models to produce formal logical representations \cite{mellgren2025prolog,evom2026}. Group Relative Policy Optimization (GRPO) with solver-verified correctness rewards enables models to discover proving strategies beyond supervised demonstrations, achieving substantial accuracy gains over supervised finetuning.
32	
33	However, execution-only reward signals create a fundamental misalignment: any output that makes the solver return ``proved'' receives equal reward, regardless of whether the formalization faithfully encodes the intended logical content. This misalignment manifests as \emph{structural degeneracy}---the model learns extensional shortcuts that satisfy the solver without encoding meaningful logical structure. We document five categories of such shortcuts: tautological premises ($\forall x.\, P(x) \lor \neg P(x)$), vacuous quantifiers, redundant clauses, over-constrained formulas, and trivial unification chains.
34	
35	Standard evaluation metrics (prove rate, accuracy) are blind to this phenomenon. A model exhibiting 45\% hacking prevalence appears indistinguishable from a structurally sound model when measured by execution accuracy alone. This is the classic reward hacking signature: the proxy metric (solver verification) improves while the latent quality dimension (structural fidelity) degrades.
36	
37	We propose \textbf{Solver Trace Ablation (STA)}, a methodology for deriving dense, automatic structural rewards from solver execution semantics. STA adapts the Reachability-Infection-Propagation (RIP) framework from mutation testing theory: a component of a formal expression is \emph{structurally necessary} if and only if its ablation (removal) changes the solver's output. This yields the \textbf{Intensional Structure Ratio (ISR)}, a continuous metric that quantifies the fraction of structurally necessary components.
38	
39	STA occupies the \textbf{dense + automatic} cell in the ORM-PRM reward taxonomy: unlike outcome reward models (ORM, sparse + automatic) or process reward models (PRM, dense + manual), STA provides fine-grained, per-component feedback without requiring human annotation. The key insight is that solver semantics already encode structural information---STA extracts it through systematic ablation.
40	
41	Our contributions are:
42	\begin{enumerate}
43	\item A \textbf{general derivation protocol} for structural rewards: a 5-step procedure (pilot $\to$ collect shortcuts $\to$ classify $\to$ map RIP $\to$ design checks) that instantiates STA for any solver--language pair. We demonstrate instantiations for FOL/Prover9, Prolog/SWI-Prolog, and SMT-LIB/Z3.
44	\item \textbf{Empirical evidence} that STA-rewarded GRPO is Pareto-improving over execution-only GRPO: matching prove rate while maintaining structural integrity (ISR/PR ratio 0.65 vs.\ 0.35), with benefits persisting on held-out evaluation and across model scales (4B--8B).
45	\item A \textbf{principled negative result}: O(1) approximations to STA (single-check shortcuts) fail because domain-specific hacking modes require correspondingly granular ablation.
46	\end{enumerate}
47	
48	% ============================================================
49	\section{Related Work}
50	\label{sec:related}
51	
52	\paragraph{RL for Formal Reasoning.}
53	GRPO and related policy gradient methods have been applied to formal theorem proving \cite{polu2020gpt}, code generation \cite{le2022coderl}, and natural-language-to-logic translation \cite{mellgren2025prolog}. EVOM \cite{evom2026} demonstrates cross-solver GRPO transfer using scalar execution rewards. These approaches share a common limitation: execution-only rewards provide no signal about structural quality.
54	
55	\paragraph{Structural Rewards in RL.}
56	Process reward models (PRMs) provide step-level supervision for mathematical reasoning \cite{lightman2023verify} but require human annotation. ExecVerify and EGCA derive trace-level rewards for code from execution traces, but do not address formal logic. Mellgren et al.\ hand-craft Prolog-specific structure penalties. Our work provides the first \emph{general derivation procedure} for structural rewards from solver semantics.
57	
58	\paragraph{Mutation Testing.}
59	Mutation testing evaluates test suite adequacy by introducing small syntactic changes (mutants) and checking whether tests detect them \cite{jia2011analysis}. The RIP framework formalizes mutation adequacy: a mutant must be \emph{reachable}, must \emph{infect} the program state, and the infection must \emph{propagate} to the output. We adapt this framework from test evaluation to reward design---instead of measuring test quality, we measure formalization quality.
60	
61	% ============================================================
62	\section{Method}
63	\label{sec:method}
64	
65	\subsection{Problem Setting}
66	
67	Given a natural language premise--hypothesis pair $(p, h)$, a formalization model $\pi_\theta$ generates a formal expression $f = \pi_\theta(p, h)$ in logic $\mathcal{L}$ (e.g., FOL, Prolog, SMT-LIB). A solver $S$ determines whether $f$ entails the hypothesis: $S(f) \in \{\texttt{proved}, \texttt{failed}\}$. Standard GRPO uses the binary execution reward $r_{\text{exec}}(f) = \mathbb{1}[S(f) = \texttt{proved}]$.
68	
69	\subsection{Solver Trace Ablation}
70	
71	\paragraph{Component Decomposition.}
72	We decompose $f$ into $n$ components $\{c_1, \ldots, c_n\}$ according to $\mathcal{L}$'s syntax. For FOL, components are individual premises (axioms); for Prolog, clauses (rules/facts); for SMT-LIB, assertions and declarations.
73	
74	\paragraph{Ablation and ISR.}
75	For each component $c_i$, we construct the ablated expression $f_{-i} = f \setminus \{c_i\}$ and evaluate $S(f_{-i})$. Component $c_i$ is \emph{structurally necessary} if $S(f_{-i}) \neq S(f)$---removing it changes the solver outcome. The \textbf{Intensional Structure Ratio} is:
76	\begin{equation}
77	\text{ISR}(f) = \frac{1}{n} \sum_{i=1}^{n} \mathbb{1}[S(f_{-i}) \neq S(f)]
78	\label{eq:isr}
79	\end{equation}
80	ISR ranges from 0 (no component is necessary---fully degenerate) to 1 (every component is necessary---maximally structured). ISR is computed only for proved outputs ($S(f) = \texttt{proved}$); for unproved outputs, ISR is undefined.
81	
82	\paragraph{RIP Mapping.}
83	STA's theoretical grounding comes from the RIP framework. For a component $c_i$ in formal expression $f$:
84	\begin{itemize}
85	\item \textbf{Reachability}: $c_i$ is syntactically reachable from the query/goal.
86	\item \textbf{Infection}: $c_i$'s content binds variables or introduces constraints used downstream.
87	\item \textbf{Propagation}: Removing $c_i$ changes the solver's final output.
88	\end{itemize}
89	STA's ablation test directly measures propagation---the strongest condition in the RIP hierarchy. Components that fail propagation are structurally unnecessary regardless of reachability or infection status.
90	
91	\subsection{Combined Reward}
92	
93	The STA-augmented reward combines execution and structural signals:
94	\begin{equation}
95	r(f) = \alpha \cdot r_{\text{exec}}(f) + \beta \cdot r_{\text{exec}}(f) \cdot \text{ISR}(f)
96	\label{eq:reward}
97	\end{equation}
98	where $\alpha + \beta = 1$. The multiplicative coupling $r_{\text{exec}} \cdot \text{ISR}$ ensures that ISR contributes only for proved outputs, avoiding penalizing the model for structural properties of failed attempts.
99	
100	\paragraph{Sigmoid Curriculum.}
101	Fixed $\beta$ weighting suppresses early prove-rate learning when the model cannot yet produce provable outputs. We use a sigmoid curriculum that ramps $\beta$ from a small initial value to its target over the first $T_{\text{ramp}}$ steps:
102	\begin{equation}
103	\beta(t) = \beta_{\text{target}} \cdot \sigma\left(\frac{t - T_{\text{ramp}}/2}{T_{\text{ramp}}/10}\right)
104	\end{equation}
105	This allows execution-dominated early learning before structural reward activates.
106	
107	\subsection{5-Step Derivation Protocol}
108	\label{sec:protocol}
109	
110	To instantiate STA for a new solver--language pair:
111	\begin{enumerate}
112	\item \textbf{Pilot}: Run exec-only GRPO for 100 steps; collect proved outputs.
113	\item \textbf{Collect Shortcuts}: Manually inspect proved outputs for structural anomalies.
114	\item \textbf{Classify}: Categorize shortcuts by type (e.g., tautological, vacuous, redundant).
115	\item \textbf{Map RIP}: For each category, identify which RIP condition it violates (typically propagation).
116	\item \textbf{Design Checks}: Define the component decomposition and ablation procedure for $\mathcal{L}$.
117	\end{enumerate}
118	Steps 1--3 are empirical; steps 4--5 are systematic given the RIP framework. The protocol ensures that STA instantiations target the actual hacking modes of each logic type.
119	
120	\subsection{Computational Cost}
121	
122	STA requires $O(n)$ solver invocations per output, where $n$ is the number of components. For our experiments, $n$ ranges from 3--15, adding 7\% wall-clock overhead compared to execution-only training. We show in Section~\ref{sec:o1_ablation} that $O(1)$ approximations fail, justifying this cost.
123	
124	% ============================================================
125	\section{Experiments}
126	\label{sec:experiments}
127	
128	\subsection{Experimental Setup}
129	
130	\paragraph{Model.} Qwen3-4B as the primary model; Qwen3-8B for scaling analysis.
131	
132	\paragraph{Training.} GRPO with $K=8$ samples per prompt, 500 training steps. Three seeds for primary comparisons; single seed for ablations and secondary experiments.
133	
134	\paragraph{Data.} FOLIO dataset for FOL experiments; equivalent Prolog and SMT-LIB formalization tasks derived from the same natural language premises.
135	
136	\paragraph{Metrics.} \textbf{Prove rate}: fraction of outputs verified by the solver. \textbf{Mean ISR}: average intensional structure ratio across proved outputs. \textbf{ISR/PR ratio}: $\text{mean\_ISR} / \text{prove\_rate}$, a normalized measure of structural quality relative to accuracy. Values near 1.0 indicate structure tracks accuracy; declining values indicate structural degeneracy. \textbf{Hacking prevalence}: fraction of proved outputs containing manually identified structural shortcuts.
137	
138	% -----------------------------------------------------------
139	\subsection{Structural Degeneracy Under Exec-Only Training}
140	\label{sec:exec_only}
141	
142	Table~\ref{tab:exec_only_dynamics} shows the training dynamics of exec-only GRPO on FOL over 500 steps (3-seed mean $\pm$ std).
143	
144	\begin{table}[t]
145	\centering
146	\small
147	\begin{tabular}{lcccc}
148	\toprule
149	\textbf{Steps} & \textbf{Prove Rate} & \textbf{Mean ISR} & \textbf{ISR/PR} & \textbf{Reward} \\
150	\midrule
151	1--100 & 0.18 $\pm$ 0.02 & 0.16 $\pm$ 0.02 & 0.92 $\pm$ 0.05 & 0.18 $\pm$ 0.02 \\
152	101--200 & 0.22 $\pm$ 0.02 & 0.16 $\pm$ 0.03 & 0.73 $\pm$ 0.08 & 0.22 $\pm$ 0.02 \\
153	201--300 & 0.25 $\pm$ 0.03 & 0.13 $\pm$ 0.03 & 0.52 $\pm$ 0.07 & 0.25 $\pm$ 0.03 \\
154	301--400 & 0.27 $\pm$ 0.03 & 0.11 $\pm$ 0.02 & 0.41 $\pm$ 0.06 & 0.27 $\pm$ 0.03 \\
155	401--500 & 0.33 $\pm$ 0.04 & 0.09 $\pm$ 0.02 & 0.35 $\pm$ 0.05 & 0.33 $\pm$ 0.04 \\
156	\bottomrule
157	\end{tabular}
158	\caption{Exec-only GRPO training dynamics on FOL (3-seed mean $\pm$ std). Prove rate improves steadily (+83\% over 500 steps) while ISR/PR ratio degrades from 0.92 to 0.35, indicating progressive structural degeneracy.}
159	\label{tab:exec_only_dynamics}
160	\end{table}
161	
162	Prove rate improves from 0.18 to 0.33 over training---a substantial gain. However, the ISR/PR ratio drops monotonically from 0.92 to 0.35, indicating that the model increasingly relies on structural shortcuts to achieve higher prove rates. Standard evaluation would rate this as a successful training run; only STA-derived ISR reveals the hidden structural degradation.
163	
164	% -----------------------------------------------------------
165	\subsection{STA-Rewarded Training}
166	\label{sec:exec_sta}
167	
168	Table~\ref{tab:exec_sta_dynamics} shows training dynamics with exec+STA reward (curriculum $\alpha=0.5$, $\beta=0.5$).
169	
170	\begin{table}[t]
171	\centering
172	\small
173	\begin{tabular}{lcccc}
174	\toprule
175	\textbf{Steps} & \textbf{Prove Rate} & \textbf{Mean ISR} & \textbf{ISR/PR} & \textbf{Reward} \\
176	\midrule
177	1--100 & 0.16 $\pm$ 0.02 & 0.08 $\pm$ 0.02 & 0.48 $\pm$ 0.08 & 0.13 $\pm$ 0.02 \\
178	101--200 & 0.22 $\pm$ 0.03 & 0.13 $\pm$ 0.03 & 0.58 $\pm$ 0.07 & 0.17 $\pm$ 0.03 \\
179	201--300 & 0.26 $\pm$ 0.03 & 0.17 $\pm$ 0.03 & 0.64 $\pm$ 0.06 & 0.21 $\pm$ 0.03 \\
180	301--400 & 0.28 $\pm$ 0.03 & 0.19 $\pm$ 0.03 & 0.67 $\pm$ 0.06 & 0.23 $\pm$ 0.03 \\
181	401--500 & 0.34 $\pm$ 0.04 & 0.22 $\pm$ 0.03 & 0.65 $\pm$ 0.05 & 0.28 $\pm$ 0.03 \\
182	\bottomrule
183	\end{tabular}
184	\caption{Exec+STA GRPO training dynamics on FOL (3-seed mean $\pm$ std). Prove rate matches exec-only (0.34 vs.\ 0.33 final window) while ISR/PR ratio stabilizes at 0.65 instead of degrading to 0.35.}
185	\label{tab:exec_sta_dynamics}
186	\end{table}
187	
188	The comparison between Tables~\ref{tab:exec_only_dynamics} and \ref{tab:exec_sta_dynamics} delivers the core result. Exec+STA training achieves prove rate comparable to exec-only (overall mean 0.30 vs.\ 0.28, not statistically different) while maintaining ISR/PR ratio $\geq 0.48$ throughout training, stabilizing at 0.65. The sigmoid curriculum is load-bearing: the initial dip in ISR/PR (0.48 at steps 1--100) reflects the low-STA-weight phase where behavior approximates exec-only; ISR/PR then recovers as STA weight ramps up. Wall-clock overhead is 7\% (10.2s vs.\ 9.5s per step).
189	
190	% -----------------------------------------------------------
191	\subsection{Held-Out Generalization}
192	\label{sec:held_out}
193	
194	\begin{table}[t]
195	\centering
196	\small
197	\begin{tabular}{lcccc}
198	\toprule
199	\textbf{Condition} & \textbf{PR} & \textbf{ISR} & \textbf{ISR/PR} & \textbf{Hack \%} \\
200	\midrule
201	Base model & 0.12 & 0.064 & 0.53 & 25 \\
202	Exec-only & 0.24 & 0.08 & 0.33 & 45 \\
203	Exec+STA & 0.26 & 0.22 & 0.85 & 18 \\
204	Ground truth & 0.18 & 0.559 & --- & 0 \\
205	\bottomrule
206	\end{tabular}
207	\caption{Held-out generalization. Exec+STA achieves ISR/PR = 0.85 vs.\ 0.33 for exec-only, with hacking prevalence reduced from 45\% to 18\%. The base model's ISR/PR (0.53) exceeds trained exec-only (0.33)---exec-only training actively \emph{worsens} structural quality.}
208	\label{tab:held_out}
209	\end{table}
210	
211	Table~\ref{tab:held_out} presents the paper's strongest quantitative evidence. While prove rate differences are modest (0.24 vs.\ 0.26), the ISR gap is dramatic: 0.08 vs.\ 0.22 ($2.75\times$). The ISR/PR ratio inversion---exec-only 0.33 vs.\ exec+STA 0.85---is the headline result.
212	
213	A striking finding is that the base model (no training) has \emph{higher} ISR/PR ratio (0.53) than exec-only trained (0.33). Exec-only GRPO does not merely fail to improve structural quality---it actively degrades it below the untrained baseline. This underscores that structural degeneracy is not an inherent model limitation but an artifact of the reward signal.
214	
215	Hacking prevalence drops from 45\% (exec-only) to 18\% (exec+STA), below the base model's 25\%. STA is both diagnostic and corrective: it detects structural shortcuts \emph{and} prevents them through reward shaping.
216	
217	% -----------------------------------------------------------
218	\subsection{O(1) vs.\ O(N) Ablation}
219	\label{sec:o1_ablation}
220	
221	\begin{table}[t]
222	\centering
223	\small
224	\begin{tabular}{lccc}
225	\toprule
226	\textbf{Metric} & \textbf{O(N) STA} & \textbf{O(1)} & \textbf{Exec-only} \\
227	\midrule
228	Prove rate & 0.30 & 0.27 & 0.28 \\
229	Mean ISR & 0.19 & 0.04 & 0.11 \\
230	ISR/PR (last 100) & 0.65 & 0.15 & 0.35 \\
231	Discriminability & 0.72 & 0.08 & --- \\
232	Overhead & +7\% & +1\% & baseline \\
233	\bottomrule
234	\end{tabular}
235	\caption{O(1) tautology-only check vs.\ full O(N) STA. The O(1) approximation has near-zero discriminability (0.08) and produces training dynamics indistinguishable from exec-only.}
236	\label{tab:o1_ablation}
237	\end{table}
238	
239	Table~\ref{tab:o1_ablation} documents a principled negative result. The O(1) approximation (\texttt{fast\_isr\_fol}: tautology-only check) captures only one of many hacking modes. The model quickly learns to avoid tautologies while discovering alternative shortcuts (vacuous quantifiers, over-constrained premises) that O(1) cannot detect.
240	
241	ISR discriminability---the fraction of proved outputs receiving nonzero ISR signal---drops from 0.72 (full STA) to 0.08 (O(1)), meaning $<$8\% of outputs receive any structural feedback. The combined reward degenerates to effectively exec-only (correlation with full O(N) ISR: 0.12). The ISR/PR ratio (0.15) is actually \emph{worse} than exec-only (0.35), suggesting that the tautology-only penalty forces the model into a narrower set of non-tautological shortcuts, reducing structural diversity.
242	
243	This result motivates the O(N) cost: domain-specific hacking modes require correspondingly granular ablation components.
244	
245	% -----------------------------------------------------------
246	\subsection{Reward Weight Ablation}
247	\label{sec:weight_ablation}
248	
249	\begin{table}[t]
250	\centering
251	\small
252	\begin{tabular}{lcccc}
253	\toprule
254	$\alpha/\beta$ & \textbf{Schedule} & \textbf{PR} & \textbf{ISR/PR} & \textbf{PR$\times$Ratio} \\
255	\midrule
256	0.3/0.7 & fixed & 0.20 & 0.72 & 0.144 \\
257	0.5/0.5 & fixed & 0.25 & 0.68 & 0.170 \\
258	0.7/0.3 & fixed & 0.30 & 0.52 & 0.156 \\
259	\midrule
260	0.3/0.7 & curriculum & 0.26 & 0.70 & 0.182 \\
261	0.5/0.5 & curriculum & 0.30 & 0.65 & \textbf{0.195} \\
262	0.7/0.3 & curriculum & 0.32 & 0.55 & 0.176 \\
263	\midrule
264	1.0/0.0 & --- & 0.28 & 0.35 & 0.098 \\
265	\bottomrule
266	\end{tabular}
267	\caption{Weight ablation (500 steps, 1 seed). Sigmoid curriculum consistently Pareto-dominates fixed weighting. Curriculum $\alpha{=}0.5$/$\beta{=}0.5$ achieves the best PR$\times$ISR/PR product.}
268	\label{tab:weight_ablation}
269	\end{table}
270	
271	Table~\ref{tab:weight_ablation} reveals three insights. First, STA weight has a predictable dose--response relationship with structural quality, confirming it is a genuine training signal. Second, sigmoid curriculum Pareto-dominates fixed weighting at matched terminal weights: curriculum 0.5/0.5 matches fixed 0.7/0.3's prove rate (0.30) while achieving higher ISR/PR ratio (0.65 vs.\ 0.52). Third, the optimal configuration is curriculum $\alpha{=}0.5$/$\beta{=}0.5$, achieving the highest PR$\times$ISR/PR product (0.195).
272	
273	% -----------------------------------------------------------
274	\subsection{Multi-Logic Validation}
275	\label{sec:multi_logic}
276	
277	\paragraph{Prolog.}
278	Table~\ref{tab:prolog} shows STA instantiated for Prolog via clause ablation (remove each clause, check if query still succeeds). Prolog-specific hacking modes---redundant clauses, catch-all rules, trivial unification---are structurally distinct from FOL's, confirming that hacking is logic-type-specific and STA detects it across logic types.
279	
280	\begin{table}[t]
281	\centering
282	\small
283	\begin{tabular}{lcccc}
284	\toprule
285	\textbf{Condition} & \textbf{PR} & \textbf{ISR} & \textbf{ISR/PR} & \textbf{Discrim.} \\
286	\midrule
287	Exec-only & 0.22 & 0.08 & 0.32 & --- \\
288	Exec+STA & 0.24 & 0.14 & 0.58 & 0.45 \\
289	\bottomrule
290	\end{tabular}
291	\caption{Prolog single-logic GRPO (500 steps, 1 seed). The exec+STA pattern replicates: ISR/PR ratio stabilizes at 0.58 vs.\ 0.32.}
292	\label{tab:prolog}
293	\end{table}
294	
295	\paragraph{SMT-LIB.}
296	Table~\ref{tab:three_logic} completes the three-logic validation. SMT-LIB STA uses constraint ablation (remove each \texttt{assert}/\texttt{declare}, check if \texttt{(check-sat)} result changes). SMT-LIB-specific hacking modes include trivial assertions, over-constrained declarations, and unused variables.
297	
298	\begin{table}[t]
299	\centering
300	\small
301	\begin{tabular}{lccccc}
302	\toprule
303	\textbf{Logic} & \textbf{EO PR} & \textbf{ES PR} & \textbf{EO Ratio} & \textbf{ES Ratio} & \textbf{Discrim.} \\
304	\midrule
305	FOL & 0.28 & 0.30 & 0.35 & 0.65 & 0.72 \\
306	Prolog & 0.22 & 0.24 & 0.32 & 0.58 & 0.45 \\
307	SMT-LIB & 0.18 & 0.19 & 0.38 & 0.52 & 0.35 \\
308	\bottomrule
309	\end{tabular}
310	\caption{Three-logic STA summary. EO = exec-only, ES = exec+STA. The qualitative pattern (STA stabilizes structural quality) holds across all three logic types despite different absolute metrics and discriminability levels.}
311	\label{tab:three_logic}
312	\end{table}
313	
314	The diminishing effect magnitude (FOL $>$ Prolog $>$ SMT-LIB) correlates with ISR discriminability, which itself correlates with component independence---SMT-LIB assertions are often interdependent, producing a coarser ISR signal.
315	
316	\paragraph{Multi-Logic Training.}
317	Table~\ref{tab:multi_logic} compares single-logic and multi-logic training.
318	
319	\begin{table}[t]
320	\centering
321	\small
322	\begin{tabular}{llccc}
323	\toprule
324	\textbf{Logic} & \textbf{Training} & \textbf{PR} & \textbf{ISR/PR} & $\Delta$ \textbf{vs single} \\
325	\midrule
326	FOL & single exec+STA & 0.30 & 0.65 & --- \\
327	FOL & multi exec+STA & 0.29 & 0.62 & $-$0.01 / $-$0.03 \\
328	Prolog & single exec+STA & 0.24 & 0.58 & --- \\
329	Prolog & multi exec+STA & 0.25 & 0.55 & +0.01 / $-$0.03 \\
330	\bottomrule
331	\end{tabular}
332	\caption{Multi-logic vs.\ single-logic training. Prolog benefits from multi-logic training (+0.01 PR); FOL shows marginal decrease. ISR/PR ratio is slightly lower under multi-logic due to mixed reward signal noise.}
333	\label{tab:multi_logic}
334	\end{table}
335	
336	Cross-logic transfer is positive but modest: Prolog benefits more from FOL co-training (+0.01 PR, +0.03 over single-logic baseline) because FOL training data is larger and formal reasoning skills partially transfer. The slight ISR/PR decrease under multi-logic training reflects gradient variance from mixed logic-specific STA signals.
337	
338	\paragraph{Zero-Shot Cross-Logic Transfer.}
339	Table~\ref{tab:cross_transfer} evaluates models on the logic type they were \emph{not} trained on.
340	
341	\begin{table}[t]
342	\centering
343	\small
344	\begin{tabular}{llccc}
345	\toprule
346	\textbf{Source} & \textbf{Target} & \textbf{PR} & $\Delta$ \textbf{vs base} & \textbf{ISR} \\
347	\midrule
348	Base & FOL & 0.12 & --- & 0.064 \\
349	Base & Prolog & 0.12 & --- & 0.05 \\
350	FOL exec+STA & Prolog & 0.16 & +0.04 & 0.09 \\
351	Prolog exec+STA & FOL & 0.17 & +0.05 & 0.10 \\
352	FOL exec-only & Prolog & 0.15 & +0.03 & 0.06 \\
353	Prolog exec-only & FOL & 0.16 & +0.04 & 0.07 \\
354	\bottomrule
355	\end{tabular}
356	\caption{Zero-shot cross-logic transfer. STA-trained models show marginally higher transfer ($+0.01$ additional $\Delta$) than exec-only trained models, suggesting structurally sound formalizations encode more transferable logical patterns.}
357	\label{tab:cross_transfer}
358	\end{table}
359	
360	Both directions show positive transfer (mean $\Delta = 0.045$ over base). STA-trained models exhibit marginally higher transfer than exec-only models (+0.01 additional $\Delta$), consistent with the hypothesis that structurally sound formalizations encode more generalizable logical structure.
361	
362	% -----------------------------------------------------------
363	\subsection{SFT Baseline}
364	\label{sec:sft}
365	
366	\begin{table}[t]
367	\centering
368	\small
369	\begin{tabular}{lcccc}
370	\toprule
371	\textbf{Method} & \textbf{PR} & \textbf{ISR} & \textbf{ISR/PR} & \textbf{Held-out PR} \\
372	\midrule
373	Base model & 0.12 & 0.064 & 0.53 & 0.12 \\
374	SFT & 0.20 & 0.13 & 0.65 & 0.18 \\
375	GRPO exec-only & 0.28 & 0.11 & 0.39 & 0.24 \\
376	GRPO exec+STA & 0.30 & 0.19 & 0.63 & 0.26 \\
377	\bottomrule
378	\end{tabular}
379	\caption{SFT vs.\ GRPO comparison. SFT maintains structural quality (ISR/PR = 0.65) but achieves lower accuracy than GRPO. Exec+STA combines GRPO's accuracy advantage with SFT-level structural quality.}
380	\label{tab:sft}
381	\end{table}
382	
383	Table~\ref{tab:sft} positions STA within the accuracy--structure tradeoff. SFT on ground-truth formalizations achieves good structure (ISR/PR = 0.65) by imitating human-written outputs, but lacks GRPO's exploration and achieves lower prove rate (0.20 vs.\ 0.30). Exec-only GRPO achieves high accuracy but degraded structure. Exec+STA GRPO achieves both: GRPO-level accuracy with SFT-level structural quality. This demonstrates that GRPO is necessary for accuracy and STA is necessary for maintaining the structural quality that SFT inherits from human demonstrations.
384	
385	% -----------------------------------------------------------
386	\subsection{Scaling Analysis}
387	\label{sec:scaling}
388	
389	\begin{table}[t]
390	\centering
391	\small
392	\begin{tabular}{llccc}
393	\toprule
394	\textbf{Model} & \textbf{Condition} & \textbf{PR} & \textbf{ISR/PR} & \textbf{Held-out PR} \\
395	\midrule
396	Qwen3-4B & exec-only & 0.28 & 0.35 & 0.24 \\
397	Qwen3-4B & exec+STA & 0.30 & 0.65 & 0.26 \\
398	Qwen3-8B & exec-only & 0.38 & 0.40 & 0.32 \\
399	Qwen3-8B & exec+STA & 0.40 & 0.68 & 0.34 \\
400	\bottomrule
401	\end{tabular}
402	\caption{Scale comparison (4B vs.\ 8B). The STA benefit is approximately scale-invariant: ISR/PR improvement of ${\sim}0.28$ at both scales. Structural degeneracy persists at 8B, confirming it is a property of the optimization, not a small-model artifact.}
403	\label{tab:scaling}
404	\end{table}
405	
406	Table~\ref{tab:scaling} demonstrates that STA's benefits are scale-invariant. Scaling from 4B to 8B increases prove rate by ${\sim}0.10$ for both conditions, but the ISR/PR ratio gap persists: exec-only degrades to 0.40 (slightly better than 4B's 0.35---larger models hack less aggressively due to greater capacity for genuine solutions), while exec+STA maintains 0.68. The relative ISR/PR improvement (${\sim}0.28$) is consistent across scales, confirming that structural degeneracy under exec-only reward is a fundamental property of GRPO optimization, not a small-model artifact.
407	
408	% -----------------------------------------------------------
409	\subsection{Hacking Characterization}
410	\label{sec:hacking}
411	
412	\begin{table}[t]
413	\centering
414	\small
415	\begin{tabular}{lcccc}
416	\toprule
417	\textbf{Shortcut Type} & \textbf{Base} & \textbf{EO} & \textbf{E+S} & \textbf{SFT} \\
418	\midrule
419	Tautological premise & 8 & 18 & 3 & 2 \\
420	Vacuous quantifier & 7 & 12 & 4 & 3 \\
421	Redundant clause & 5 & 8 & 6 & 4 \\
422	Over-constrained & 3 & 5 & 3 & 2 \\
423	Other/subtle & 2 & 2 & 2 & 1 \\
424	\midrule
425	\textbf{Total hack rate (\%)} & 25 & 45 & 18 & 12 \\
426	\bottomrule
427	\end{tabular}
428	\caption{Hacking taxonomy distribution (\%, 200 outputs per condition, $\kappa = 0.78$). EO = exec-only, E+S = exec+STA. Exec-only training amplifies hacking from 25\% to 45\%; STA reduces it to 18\%, below the untrained baseline.}
429	\label{tab:hacking}
430	\end{table}
431	
432	Table~\ref{tab:hacking} provides qualitative evidence complementing the quantitative ISR metrics. Manual annotation of 200 outputs per condition (inter-annotator $\kappa = 0.78$) reveals the composition of structural degeneracy.
433	
434	Exec-only training amplifies every hacking category relative to the base model: tautological premises increase from 8\% to 18\%, vacuous quantifiers from 7\% to 12\%. This is expected---GRPO's policy gradient selects for outputs that prove easily, and structural shortcuts prove more easily than genuine formalizations.
435	
436	STA-rewarded training suppresses the most egregious categories: tautological premises drop from 18\% to 3\% (STA assigns ISR = 0 to tautology components), vacuous quantifiers from 12\% to 4\%. Residual hacking (18\% total) consists primarily of subtler shortcuts---redundant clauses with small but nonzero ISR contributions (6\%)---that partial ISR does not fully penalize. This identifies a clear direction for future work: finer-grained ablation or curriculum emphasis on high-residual hacking modes.
437	
438	% ============================================================
439	\section{Discussion}
440	\label{sec:discussion}
441	
442	\paragraph{STA in the ORM-PRM Taxonomy.}
443	STA fills a previously empty cell: dense + automatic rewards derived from solver semantics rather than human annotation. ORMs provide sparse (outcome-level) automatic feedback; PRMs provide dense (step-level) feedback but require manual labels. STA achieves PRM-level granularity (per-component structural scores) with ORM-level automation (derived from solver execution). This positions STA as complementary to, not competitive with, existing reward paradigms.
444	
445	\paragraph{When Does STA Help Most?}
446	Our results suggest STA's benefit scales with ISR discriminability---the degree to which components are independently ablatable. FOL (discriminability 0.72) shows the strongest effect; SMT-LIB (0.35) the weakest. This provides a practical guideline: STA is most valuable for languages with modular, independently testable components.
447	
448	\paragraph{Limitations.}
449	Our experiments use a single base model family (Qwen3) and a limited set of formal languages. The 5-step derivation protocol requires manual inspection (steps 2--3), introducing human effort. ISR treats all components equally---a premise that constrains the entire proof is scored the same as one that constrains a single variable. Future work should explore weighted ISR based on component influence depth.
450	
451	% ============================================================
452	\section{Conclusion}
453	\label{sec:conclusion}
454	
455	We introduced Solver Trace Ablation (STA), a methodology for deriving dense structural rewards from solver execution semantics via the RIP framework from mutation testing. Our 5-step derivation protocol generalizes across three logic types (FOL, Prolog, SMT-LIB), and STA-rewarded GRPO consistently maintains structural integrity without sacrificing prove rate. The O(1) negative result validates the necessity of comprehensive component ablation. Scaling analysis confirms that structural degeneracy is a fundamental property of execution-only GRPO, not a small-model artifact, and STA addresses it at all tested scales. STA provides a principled, automatic approach to the structural reward design problem that has limited prior work to ad-hoc, domain-specific heuristics.
456	
457	\begin{thebibliography}{9}
458	
459	\bibitem[Mellgren et~al.(2025)]{mellgren2025prolog}
460	E.~Mellgren, A.~Bj{\"o}rklund, and J.~Nivre.
461	\newblock Structure-aware reinforcement learning for Prolog synthesis.
462	\newblock In \emph{Proc.\ ACL}, 2025.
463	
464	\bibitem[EVOM(2026)]{evom2026}
465	Cross-solver GRPO transfer with execution-verified outcome models.
466	\newblock In \emph{Proc.\ ICLR}, 2026.
467	
468	\bibitem[Polu and Sutskever(2020)]{polu2020gpt}
469	S.~Polu and I.~Sutskever.
470	\newblock Generative language modeling for automated theorem proving.
471	\newblock \emph{arXiv:2009.03393}, 2020.
472	
473	\bibitem[Le et~al.(2022)]{le2022coderl}
474	H.~Le, Y.~Wang, A.~D.~Gotmare, S.~Savarese, and S.~Hoi.
475	\newblock CodeRL: Mastering code generation through pretrained models and deep reinforcement learning.
476	\newblock In \emph{Proc.\ NeurIPS}, 2022.
477	
478	\bibitem[Lightman et~al.(2023)]{lightman2023verify}
479	H.~Lightman, V.~Kosaraju, Y.~Burda, H.~Edwards, B.~Baker, T.~Lee, J.~Leike, J.~Schulman, I.~Sutskever, and K.~Cobbe.
480	\newblock Let's verify step by step.
481	\newblock In \emph{Proc.\ ICLR}, 2024.
482	
483	\bibitem[Jia and Harman(2011)]{jia2011analysis}
484	Y.~Jia and M.~Harman.
485	\newblock An analysis and survey of the development of mutation testing.
486	\newblock \emph{IEEE TSE}, 37(5):649--678, 2011.
487	
488	\end{thebibliography}
489	
490	\end{document}
491	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "693cf585-e617-4207-abf0-3a3391ebd16a",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "e0c96272-8832-4928-9bed-4e215414fe2b",
  "sourceToolAssistantUUID": "693cf585-e617-4207-abf0-3a3391ebd16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T22:42:53.342Z_

Now let me read the "median" and "worst" papers, the experiment data, and the training script to understand what was actually run vs. what's reported.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0c96272-8832-4928-9bed-4e215414fe2b",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NkYWhzmqWFBxwYEyP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9fdf7f1-373a-401e-9ae3-20c38ee5b68d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7crCdsJY67pNNX36kE16r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12139,
      "cache_read_input_tokens": 28382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12139,
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

_source line 34 · 2026-05-13T22:42:55.705Z_

<details open><summary>🔧 Tool call — Read · `toolu_0124LvMbezQVYdFp7T14z15c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9fdf7f1-373a-401e-9ae3-20c38ee5b68d",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NkYWhzmqWFBxwYEyP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1151ef1-a2c2-4a4f-a373-31b5278c7abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7crCdsJY67pNNX36kE16r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12139,
      "cache_read_input_tokens": 28382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12139,
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

_source line 35 · 2026-05-13T22:42:56.050Z_

<details><summary>↩ Tool result · `toolu_0124LvMbezQVYdFp7T14z15c`</summary>

```text
1	[
2	  {
3	    "name": "FOL Exec-Only 500-Step Baseline",
4	    "description": "FOL single-logic GRPO, execution-only reward, 500 steps, K=8, 3 seeds. Establishes the structural degradation trajectory that STA is designed to prevent.\n",
5	    "results": {
6	      "prove_rate_mean": 0.28,
7	      "prove_rate_std": 0.03,
8	      "prove_rate_first100": 0.18,
9	      "prove_rate_last100": 0.33,
10	      "mean_isr_overall": 0.11,
11	      "mean_isr_last100": 0.09,
12	      "isr_pr_ratio_overall": 0.39,
13	      "isr_pr_ratio_last100": 0.35,
14	      "isr_pr_ratio_first100": 0.92,
15	      "parse_rate": 1.0,
16	      "training_minutes": 79,
17	      "step_time_s": 9.5
18	    },
19	    "tables": [
20	      {
21	        "name": "Table 2a: Exec-Only Training Dynamics (3-seed mean ± std)",
22	        "columns": [
23	          "step_window",
24	          "prove_rate",
25	          "mean_isr",
26	          "isr_pr_ratio",
27	          "reward_mean"
28	        ],
29	        "rows": [
30	          [
31	            "1-100",
32	            "0.18 ± 0.02",
33	            "0.16 ± 0.02",
34	            "0.92 ± 0.05",
35	            "0.18 ± 0.02"
36	          ],
37	          [
38	            "101-200",
39	            "0.22 ± 0.02",
40	            "0.16 ± 0.03",
41	            "0.73 ± 0.08",
42	            "0.22 ± 0.02"
43	          ],
44	          [
45	            "201-300",
46	            "0.25 ± 0.03",
47	            "0.13 ± 0.03",
48	            "0.52 ± 0.07",
49	            "0.25 ± 0.03"
50	          ],
51	          [
52	            "301-400",
53	            "0.27 ± 0.03",
54	            "0.11 ± 0.02",
55	            "0.41 ± 0.06",
56	            "0.27 ± 0.03"
57	          ],
58	          [
59	            "401-500",
60	            "0.33 ± 0.04",
61	            "0.09 ± 0.02",
62	            "0.35 ± 0.05",
63	            "0.33 ± 0.04"
64	          ]
65	        ]
66	      }
67	    ],
68	    "figures": [],
69	    "analysis": "The exec-only trajectory confirms the core problem statement: execution-only GRPO optimizes prove_rate effectively (+133% from baseline) but introduces structural degeneracy that accelerates after step ~150. The declining isr_pr_ratio is the paper's primary diagnostic signal. Notably, prove_rate continues improving even as ISR declines, meaning standard evaluation (accuracy-only) would rate this as a successful training run. Only STA-derived ISR reveals the hidden failure mode. This motivates the need for STA as a reward component, not just a diagnostic.\n\n\nPhase 1 pilot (r5) showed prove_rate=0.15 at 100 steps with isr_pr_ratio=1.0 (ISR tracks prove_rate perfectly because the model hasn't yet learned structural shortcuts). At 500 steps, GRPO's policy gradient drives prove_rate up to ~0.28 — substantial improvement from the 0.12 baseline — but the model discovers extensional shortcuts: tautological premises, vacuous quantifiers, over-constrained formulas that prove trivially. These shortcuts yield solver-verified \"correct\" outputs with degraded internal structure, causing ISR to lag behind prove_rate. The isr_pr_ratio drops from ~0.92 (step 1-100, structure intact) to ~0.35 (step 400-500, structural degeneracy). This is the classic reward hacking signature: the model maximizes the proxy (execution reward) while degrading the latent quality dimension (structural fidelity). Three seeds provide sufficient signal to distinguish this trend from noise; std ~0.03 reflects Qwen3-4B's moderate sensitivity to initialization on FOLIO-scale data.\n"
70	  },
71	  {
72	    "name": "FOL Exec+STA 500-Step Primary",
73	    "description": "FOL single-logic GRPO, execution+STA reward (full continuous STA), 500 steps, K=8, 3 seeds. Primary validation that STA reward prevents structural degradation while maintaining prove_rate.\n",
74	    "results": {
75	      "prove_rate_mean": 0.3,
76	      "prove_rate_std": 0.03,
77	      "prove_rate_first100": 0.16,
78	      "prove_rate_last100": 0.34,
79	      "mean_isr_overall": 0.19,
80	      "mean_isr_last100": 0.22,
81	      "isr_pr_ratio_overall": 0.63,
82	      "isr_pr_ratio_last100": 0.65,
83	      "isr_pr_ratio_first100": 0.48,
84	      "parse_rate": 1.0,
85	      "combined_reward_mean": 0.24,
86	      "training_minutes": 85,
87	      "step_time_s": 10.2
88	    },
89	    "tables": [
90	      {
91	        "name": "Table 2b: Exec+STA Training Dynamics (3-seed mean ± std)",
92	        "columns": [
93	          "step_window",
94	          "prove_rate",
95	          "mean_isr",
96	          "isr_pr_ratio",
97	          "combined_reward"
98	        ],
99	        "rows": [
100	          [
101	            "1-100",
102	            "0.16 ± 0.02",
103	            "0.08 ± 0.02",
104	            "0.48 ± 0.08",
105	            "0.13 ± 0.02"
106	          ],
107	          [
108	            "101-200",
109	            "0.22 ± 0.03",
110	            "0.13 ± 0.03",
111	            "0.58 ± 0.07",
112	            "0.17 ± 0.03"
113	          ],
114	          [
115	            "201-300",
116	            "0.26 ± 0.03",
117	            "0.17 ± 0.03",
118	            "0.64 ± 0.06",
119	            "0.21 ± 0.03"
120	          ],
121	          [
122	            "301-400",
123	            "0.28 ± 0.03",
124	            "0.19 ± 0.03",
125	            "0.67 ± 0.06",
126	            "0.23 ± 0.03"
127	          ],
128	          [
129	            "401-500",
130	            "0.34 ± 0.04",
131	            "0.22 ± 0.03",
132	            "0.65 ± 0.05",
133	            "0.28 ± 0.03"
134	          ]
135	        ]
136	      }
137	    ],
138	    "figures": [],
139	    "analysis": "Exec+STA achieves the best-tier prediction: prove_rate matches exec-only (0.30 vs 0.28, not statistically different) while maintaining isr_pr_ratio ≥0.5 throughout training (vs exec-only's degradation to 0.35). The slight prove_rate advantage (+0.02) emerges because STA penalizes degenerate shortcuts, forcing the model to discover structurally sound proving strategies that also happen to generalize better. The 7% wall-clock overhead (10.2s vs 9.5s per step) is negligible. This validates the core claim: STA reward is Pareto-improving (same accuracy, better structure) or at worst Pareto-neutral (same accuracy, maintained structure). The curriculum is load-bearing — without it (as in Phase 1 pilot), the 0.5 STA weight suppresses early prove_rate learning.\n\n\nPhase 1 pilot (r5) showed exec+STA with 0.5/0.5 weighting depressed prove_rate (0.10 vs 0.15 for exec-only) because the STA penalty was too punitive at initialization, when the model produces mostly unprovable outputs. At 500 steps with curriculum weighting (sigmoid ramp from sta_weight=0.1→0.5 over first 200 steps), the model first learns to prove (prove_rate rises rapidly steps 1-200 under near-exec-only reward), then learns to prove structurally (ISR catches up steps 200-500 as STA weight activates). The key prediction: prove_rate matches or slightly exceeds exec-only (0.30 vs 0.28) because STA reward actively penalizes the degenerate shortcuts that exec-only relies on for its final prove_rate gains. The model is forced to find structurally sound proofs, which are more robust and transfer better. The isr_pr_ratio stabilizes at ~0.65 instead of degrading to 0.35 — this is the headline comparison. The initial dip in isr_pr_ratio (0.48 at step 1-100) reflects the low-STA-weight curriculum phase where behavior approximates exec-only; it then recovers as STA weight ramps up.\n"
140	  },
141	  {
142	    "name": "FOL Held-Out Evaluation",
143	    "description": "Held-out test set evaluation comparing plan_001 (exec-only) vs plan_002 (exec+STA) checkpoints. Full STA metrics on unseen problems to measure generalization.\n",
144	    "results": {
145	      "exec_only_held_out_prove_rate": 0.24,
146	      "exec_sta_held_out_prove_rate": 0.26,
147	      "exec_only_held_out_isr_mean": 0.08,
148	      "exec_sta_held_out_isr_mean": 0.22,
149	      "exec_only_held_out_isr_pr_ratio": 0.33,
150	      "exec_sta_held_out_isr_pr_ratio": 0.85,
151	      "exec_only_hacking_prevalence": 0.45,
152	      "exec_sta_hacking_prevalence": 0.18
153	    },
154	    "tables": [
155	      {
156	        "name": "Table 3: Held-Out Generalization (best checkpoint per condition)",
157	        "columns": [
158	          "condition",
159	          "prove_rate",
160	          "mean_isr",
161	          "isr_pr_ratio",
162	          "hacking_prevalence"
163	        ],
164	        "rows": [
165	          [
166	            "Base model (no training)",
167	            "0.12",
168	            "0.064",
169	            "0.53",
170	            "0.25"
171	          ],
172	          [
173	            "Exec-only (plan_001)",
174	            "0.24",
175	            "0.08",
176	            "0.33",
177	            "0.45"
178	          ],
179	          [
180	            "Exec+STA (plan_002)",
181	            "0.26",
182	            "0.22",
183	            "0.85",
184	            "0.18"
185	          ],
186	          [
187	            "Ground-truth reference",
188	            "0.18",
189	            "0.559",
190	            "—",
191	            "0.0"
192	          ]
193	        ]
194	      }
195	    ],
196	    "figures": [],
197	    "analysis": "The held-out results deliver the paper's strongest evidence. While prove_rate difference is modest and possibly not significant (0.24 vs 0.26, needs paired test), the ISR gap is dramatic (0.08 vs 0.22, ~2.75x). This means exec-only training produces models that \"prove\" held-out problems but via degenerate means (45% hacking rate), while exec+STA training produces models whose proofs are structurally meaningful. The isr_pr_ratio inversion (exec-only 0.33 < exec+STA 0.85) is the quantitative headline. Note the base model's isr_pr_ratio of 0.53 is higher than trained exec-only's 0.33 — training actively worsens structural quality under exec-only reward, a finding that underscores the need for STA.\n\n\nHeld-out evaluation amplifies the structural gap because degenerate shortcuts overfit to training distribution. Exec-only model's prove_rate drops more on held-out (0.24 vs 0.28 in-distribution) because tautological/vacuous shortcuts are less likely to accidentally match held-out problem structures. Its held-out ISR drops further (0.08) because the learned shortcuts are even less structurally valid on new problems. Exec+STA model retains prove_rate better (0.26 vs 0.30, smaller drop) because structurally sound proofs generalize. Its ISR actually improves relative to isr_pr_ratio (0.85 vs 0.65 in-distribution) because the remaining proved outputs are genuinely well-structured — the degenerate easy wins that inflated training prove_rate without proportional ISR are gone. The hacking prevalence (fraction of proved outputs that are structurally degenerate by manual taxonomy) drops from 45% to 18%, directly supporting the \"STA corrects, not just detects\" narrative.\n"
198	  },
199	  {
200	    "name": "STA O(1) vs O(N) Ablation at Scale",
201	    "description": "Rerun exec+STA with fast_isr_fol (O(1) tautology-only check) for 500 steps, 1 seed. Documents the negative result that coarse-grained ablation provides insufficient signal.\n",
202	    "results": {
203	      "prove_rate": 0.27,
204	      "mean_isr_o1": 0.04,
205	      "isr_pr_ratio": 0.15,
206	      "isr_discriminability": 0.08,
207	      "combined_reward_correlation_with_on": 0.12,
208	      "training_trajectory": "indistinguishable from exec-only"
209	    },
210	    "tables": [
211	      {
212	        "name": "Table 4: O(1) vs O(N) Ablation Comparison",
213	        "columns": [
214	          "metric",
215	          "O(N) full STA",
216	          "O(1) fast_isr",
217	          "exec-only"
218	        ],
219	        "rows": [
220	          [
221	            "prove_rate (500 step)",
222	            "0.30",
223	            "0.27",
224	            "0.28"
225	          ],
226	          [
227	            "mean_isr",
228	            "0.19",
229	            "0.04",
230	            "0.11"
231	          ],
232	          [
233	            "isr_pr_ratio_last100",
234	            "0.65",
235	            "0.15",
236	            "0.35"
237	          ],
238	          [
239	            "isr_discriminability",
240	            "0.72",
241	            "0.08",
242	            "—"
243	          ],
244	          [
245	            "wall-clock overhead",
246	            "+7%",
247	            "+1%",
248	            "baseline"
249	          ]
250	        ]
251	      }
252	    ],
253	    "figures": [],
254	    "analysis": "The O(1) negative result is essential for the paper's methodology argument. It demonstrates that STA's value comes from comprehensive component ablation (O(N) cost per output), not from any single structural check. This motivates the 5-step RIP derivation protocol: each logic type has its own hacking modes, and the ablation set must cover them all. The O(1) result also preempts reviewer concern about STA's computational cost — yes, it's O(N) per component, but O(1) approximations demonstrably fail, so the cost is necessary. The slightly worse isr_pr_ratio for O(1) vs exec-only (0.15 vs 0.35) suggests the tautology penalty actively worsens structural diversity by forcing the model into a narrower set of non-tautological shortcuts.\n\n\nPhase 1 r4 already showed O(1) failure at 100 steps. At 500 steps, the result is cleaner: fast_isr_fol checks only tautology (is the formula trivially true?), which catches only one of many hacking modes. The model quickly learns to avoid tautologies while discovering other shortcuts (vacuous quantifiers, over-constrained premises, redundant clauses) that O(1) cannot detect. Prove_rate (~0.27) and training dynamics are indistinguishable from exec-only because the O(1) ISR signal is near-zero for all non-tautological outputs (discriminability 0.08, meaning <8% of proved outputs receive any ISR signal). The combined reward reduces to effectively exec-only (correlation with full O(N) ISR is only 0.12). This is the principled negative result: domain-specific hacking modes require correspondingly granular ablation components. A single-check approximation captures one failure mode while the model routes around it to exploit others.\n"
255	  },
256	  {
257	    "name": "STA Reward Weight Ablation",
258	    "description": "Test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3) × {fixed, sigmoid curriculum}. 6 runs × 500 steps × 1 seed = 6 runs total.\n",
259	    "results": {
260	      "fixed_03_07_prove_rate": 0.2,
261	      "fixed_03_07_isr_pr_ratio": 0.72,
262	      "fixed_05_05_prove_rate": 0.25,
263	      "fixed_05_05_isr_pr_ratio": 0.68,
264	      "fixed_07_03_prove_rate": 0.3,
265	      "fixed_07_03_isr_pr_ratio": 0.52,
266	      "curriculum_03_07_prove_rate": 0.26,
267	      "curriculum_03_07_isr_pr_ratio": 0.7,
268	      "curriculum_05_05_prove_rate": 0.3,
269	      "curriculum_05_05_isr_pr_ratio": 0.65,
270	      "curriculum_07_03_prove_rate": 0.32,
271	      "curriculum_07_03_isr_pr_ratio": 0.55,
272	      "best_config": "curriculum α=0.5 β=0.5"
273	    },
274	    "tables": [
275	      {
276	        "name": "Table 5: Weight Ablation Results (500 steps, 1 seed)",
277	        "columns": [
278	          "α/β",
279	          "schedule",
280	          "prove_rate",
281	          "isr_pr_ratio",
282	          "pr × ratio"
283	        ],
284	        "rows": [
285	          [
286	            "0.3/0.7",
287	            "fixed",
288	            "0.20",
289	            "0.72",
290	            "0.144"
291	          ],
292	          [
293	            "0.5/0.5",
294	            "fixed",
295	            "0.25",
296	            "0.68",
297	            "0.170"
298	          ],
299	          [
300	            "0.7/0.3",
301	            "fixed",
302	            "0.30",
303	            "0.52",
304	            "0.156"
305	          ],
306	          [
307	            "0.3/0.7",
308	            "curriculum",
309	            "0.26",
310	            "0.70",
311	            "0.182"
312	          ],
313	          [
314	            "0.5/0.5",
315	            "curriculum",
316	            "0.30",
317	            "0.65",
318	            "0.195"
319	          ],
320	          [
321	            "0.7/0.3",
322	            "curriculum",
323	            "0.32",
324	            "0.55",
325	            "0.176"
326	          ],
327	          [
328	            "1.0/0.0",
329	            "—",
330	            "0.28",
331	            "0.35",
332	            "0.098"
333	          ]
334	        ]
335	      }
336	    ],
337	    "figures": [],
338	    "analysis": "The weight ablation provides three key insights: (1) STA weight has a predictable dose-response relationship with structural quality, confirming it's a genuine training signal, not noise. (2) Sigmoid curriculum is a principled solution to the Phase 1 pilot's prove_rate depression problem — it recovers ~0.05 prove_rate compared to fixed weighting at matched terminal weights. (3) The Pareto analysis gives practitioners a concrete recommendation: use curriculum 0.5/0.5 for balanced accuracy-structure, or curriculum 0.7/0.3 if accuracy is the priority. This section also serves as an implicit response to \"how sensitive is STA to hyperparameters?\" — the answer is \"moderately, but curriculum scheduling makes it robust.\"\n\n\nThe weight ablation reveals a clear Pareto frontier trading prove_rate against structural quality. Fixed weighting shows the expected tradeoff: higher STA weight (β=0.7) produces highest isr_pr_ratio (0.72) but lowest prove_rate (0.20) because the STA penalty is too punitive during early training when the model cannot yet produce provable outputs. Lower STA weight (β=0.3) produces near-exec-only prove_rate (0.30) but only moderate structural benefit (isr_pr_ratio 0.52 vs exec-only's 0.35). The sigmoid curriculum consistently Pareto-dominates fixed weighting at the same terminal α/β: curriculum 0.5/0.5 matches fixed 0.7/0.3's prove_rate (0.30) while achieving higher isr_pr_ratio (0.65 vs 0.52). This is because the curriculum allows exec-reward-dominated early learning (the model first learns to prove) before STA activates (forcing structural quality). The optimal configuration is curriculum α=0.5/β=0.5 — it achieves the best prove_rate × isr_pr_ratio product (0.30 × 0.65 = 0.195) and lies at the Pareto knee. Curriculum α=0.7/β=0.3 achieves marginally higher prove_rate (0.32) but substantially lower structural quality — diminishing returns on the accuracy axis.\n"
339	  },
340	  {
341	    "name": "Prolog Single-Logic GRPO",
342	    "description": "Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 1 seed). Second logic type to validate STA derivation protocol generality.\n",
343	    "results": {
344	      "prolog_exec_only_prove_rate": 0.22,
345	      "prolog_exec_sta_prove_rate": 0.24,
346	      "prolog_exec_only_isr_mean": 0.08,
347	      "prolog_exec_sta_isr_mean": 0.14,
348	      "prolog_exec_only_isr_pr_ratio_last100": 0.32,
349	      "prolog_exec_sta_isr_pr_ratio_last100": 0.58,
350	      "prolog_isr_discriminability": 0.45,
351	      "prolog_hacking_modes": [
352	        "redundant_clauses",
353	        "catch_all_rules",
354	        "trivial_unification"
355	      ]
356	    },
357	    "tables": [
358	      {
359	        "name": "Table 6: Prolog Single-Logic Results (500 steps, 1 seed)",
360	        "columns": [
361	          "condition",
362	          "prove_rate",
363	          "mean_isr",
364	          "isr_pr_ratio",
365	          "discriminability"
366	        ],
367	        "rows": [
368	          [
369	            "Exec-only",
370	            "0.22",
371	            "0.08",
372	            "0.32",
373	            "—"
374	          ],
375	          [
376	            "Exec+STA",
377	            "0.24",
378	            "0.14",
379	            "0.58",
380	            "0.45"
381	          ]
382	        ]
383	      }
384	    ],
385	    "figures": [],
386	    "analysis": "Prolog results validate the STA derivation protocol's generality — the same 5-step procedure (pilot → shortcuts → classify → RIP map → design checks) produces a functional ISR signal for a structurally different logic type. The Prolog-specific hacking modes (redundant clauses, catch-all rules) are distinct from FOL's (tautological premises, vacuous quantifiers), confirming that hacking is logic-type-specific and STA catches it in both cases. Lower absolute metrics reflect the harder generation task, not methodology failure.\n\n\nProlog STA instantiation uses rule ablation (remove each clause, check if query still succeeds) — the RIP mapping is: Reachability=clause is syntactically reachable from query, Infection=clause body binds variables used downstream, Propagation=removing clause changes query result. Prolog's hacking modes differ from FOL: instead of tautological premises, the model produces redundant clauses (rules that never fire), catch-all rules (match anything via anonymous variables), and trivial unification chains. These are detectable by STA because ablating redundant/catch-all clauses doesn't change the query result (ISR contribution = 0). Prove_rate is slightly lower than FOL (0.22 vs 0.28 for exec-only) because SWI-Prolog is more sensitive to syntactic errors and Qwen3-4B has less Prolog in its pretraining data. The exec+STA pattern replicates: ISR/PR ratio stabilizes (0.58 vs 0.32), confirming the methodology transfers. Discriminability (0.45) is lower than FOL (~0.72) because Prolog programs have fewer components per output (fewer clauses to ablate), creating a coarser ISR signal, but still sufficient for reward shaping.\n"
387	  },
388	  {
389	    "name": "Multi-Logic GRPO (FOL+Prolog)",
390	    "description": "Multi-logic GRPO training on mixed FOL+Prolog data, exec-only vs exec+STA (500 steps, K=8, 1 seed). Tests whether joint training enables cross-logic transfer.\n",
391	    "results": {
392	      "multi_fol_prove_rate": 0.29,
393	      "multi_prolog_prove_rate": 0.25,
394	      "multi_fol_isr_pr_ratio": 0.62,
395	      "multi_prolog_isr_pr_ratio": 0.55,
396	      "fol_improvement_over_single": 0.01,
397	      "prolog_improvement_over_single": 0.03,
398	      "cross_logic_transfer_signal": "positive"
399	    },
400	    "tables": [
401	      {
402	        "name": "Table 7: Multi-Logic vs Single-Logic Comparison",
403	        "columns": [
404	          "logic",
405	          "training",
406	          "prove_rate",
407	          "isr_pr_ratio",
408	          "Δ vs single"
409	        ],
410	        "rows": [
411	          [
412	            "FOL",
413	            "single exec+STA",
414	            "0.30",
415	            "0.65",
416	            "—"
417	          ],
418	          [
419	            "FOL",
420	            "multi exec+STA",
421	            "0.29",
422	            "0.62",
423	            "-0.01 / -0.03"
424	          ],
425	          [
426	            "Prolog",
427	            "single exec+STA",
428	            "0.24",
429	            "0.58",
430	            "—"
431	          ],
432	          [
433	            "Prolog",
434	            "multi exec+STA",
435	            "0.25",
436	            "0.55",
437	            "+0.01 / -0.03"
438	          ]
439	        ]
440	      }
441	    ],
442	    "figures": [],
443	    "analysis": "Multi-logic results are positive but not dramatic — the transfer signal is real but modest at 4B scale with 500 steps. This is expected: cross-logic transfer requires the model to abstract beyond surface syntax to shared logical reasoning patterns, which 4B models have limited capacity for. The paper frames this as \"measurably positive transfer\" rather than \"large effect,\" setting up future work on larger models. The slight isr_pr_ratio decrease under multi-logic training is an important nuance — mixed reward signals add noise, suggesting that logic-specific STA calibration (e.g., per-logic α/β) could improve multi-logic training.\n\n\nMulti-logic training with mixed FOL+Prolog batches forces the model to maintain distinct formalization strategies per logic type, acting as implicit regularization against logic-specific hacking modes. FOL prove_rate is marginally better than single-logic (0.29 vs 0.28 exec-only baseline) because Prolog's different structural constraints provide auxiliary gradient signal. Prolog benefits more (+0.03 over single-logic's 0.24) because FOL training data is larger and the formal reasoning skills partially transfer (both involve quantifier scoping, logical connectives, variable binding). The isr_pr_ratio is slightly lower than single-logic exec+STA for both (0.62 vs 0.65 for FOL, 0.55 vs 0.58 for Prolog) because the mixed reward signal is noisier — each logic type's STA has different component counts and score distributions, creating gradient variance. The positive transfer signal is modest but measurable, supporting the Claim 2 narrative that GRPO over multiple formal languages exhibits useful cross-logic dynamics.\n"
444	  },
445	  {
446	    "name": "Cross-Logic Transfer Evaluation",
447	    "description": "Zero-shot cross-logic evaluation: FOL-trained model on Prolog tasks, Prolog-trained model on FOL tasks. Measures transfer without explicit multi-logic training.\n",
448	    "results": {
449	      "fol_model_on_prolog_prove_rate": 0.16,
450	      "prolog_model_on_fol_prove_rate": 0.17,
451	      "fol_model_on_prolog_delta_vs_base": 0.04,
452	      "prolog_model_on_fol_delta_vs_base": 0.05,
453	      "cross_logic_transfer_delta_mean": 0.045
454	    },
455	    "tables": [
456	      {
457	        "name": "Table 8: Cross-Logic Zero-Shot Transfer",
458	        "columns": [
459	          "source_model",
460	          "target_logic",
461	          "prove_rate",
462	          "Δ vs base",
463	          "mean_isr"
464	        ],
465	        "rows": [
466	          [
467	            "Base (no training)",
468	            "FOL",
469	            "0.12",
470	            "—",
471	            "0.064"
472	          ],
473	          [
474	            "Base (no training)",
475	            "Prolog",
476	            "0.12",
477	            "—",
478	            "0.05"
479	          ],
480	          [
481	            "FOL exec+STA",
482	            "Prolog",
483	            "0.16",
484	            "+0.04",
485	            "0.09"
486	          ],
487	          [
488	            "Prolog exec+STA",
489	            "FOL",
490	            "0.17",
491	            "+0.05",
492	            "0.10"
493	          ],
494	          [
495	            "FOL exec-only",
496	            "Prolog",
497	            "0.15",
498	            "+0.03",
499	            "0.06"
500	          ],
501	          [
502	            "Prolog exec-only",
503	            "FOL",
504	            "0.16",
505	            "+0.04",
506	            "0.07"
507	          ]
508	        ]
509	      }
510	    ],
511	    "figures": [],
512	    "analysis": "Cross-logic transfer is positive but small, consistent with the \"best\" tier narrative that the methodology generalizes. The exec+STA advantage in transfer (+0.01 additional delta) is a subtle but important finding: structurally sound formalizations transfer better because they encode genuine logical structure rather than solver-specific shortcuts. This supports the paper's claim that STA doesn't just improve in-distribution metrics — it produces qualitatively different model capabilities.\n\n\nCross-logic transfer delta [0.02, 0.08] predicted range. FOL→Prolog transfer (+0.04 prove_rate over base model's ~0.12 Prolog prove_rate) is modest because FOL training teaches quantifier handling and logical structure that partially maps to Prolog's clause semantics — both require correct variable scoping and logical decomposition. Prolog→FOL transfer (+0.05) is slightly larger because Prolog's rule-based reasoning develops a \"compositional formalization\" skill that transfers to FOL premise construction. Neither direction produces dramatic gains because the surface syntax is too different for shallow transfer, and 4B models at 500 steps don't develop deep enough logical abstractions for strong transfer. The positive delta (mean 0.045) is nonetheless noteworthy — it suggests shared latent formal reasoning capabilities that multi-logic training could amplify. Exec+STA-trained models show marginally higher transfer than exec-only trained models (+0.01 additional delta) because structurally sound formalizations encode more transferable logical patterns.\n"
513	  },
514	  {
515	    "name": "SFT Baseline",
516	    "description": "Supervised finetuning on same FOLIO 500 data. Provides a non-RL baseline for GRPO comparison.\n",
517	    "results": {
518	      "sft_prove_rate": 0.2,
519	      "sft_mean_isr": 0.13,
520	      "sft_isr_pr_ratio": 0.65,
521	      "sft_held_out_prove_rate": 0.18,
522	      "sft_held_out_isr_mean": 0.12
523	    },
524	    "tables": [
525	      {
526	        "name": "Table 9: SFT vs GRPO Comparison",
527	        "columns": [
528	          "method",
529	          "prove_rate",
530	          "mean_isr",
531	          "isr_pr_ratio",
532	          "held_out_pr"
533	        ],
534	        "rows": [
535	          [
536	            "SFT",
537	            "0.20",
538	            "0.13",
539	            "0.65",
540	            "0.18"
541	          ],
542	          [
543	            "GRPO exec-only",
544	            "0.28",
545	            "0.11",
546	            "0.39",
547	            "0.24"
548	          ],
549	          [
550	            "GRPO exec+STA",
551	            "0.30",
552	            "0.19",
553	            "0.63",
554	            "0.26"
555	          ],
556	          [
557	            "Base model",
558	            "0.12",
559	            "0.064",
560	            "0.53",
561	            "0.12"
562	          ]
563	        ]
564	      }
565	    ],
566	    "figures": [],
567	    "analysis": "SFT baseline serves a narrative function: it shows that structural quality is a property of the training signal, not an inherent limitation of the model. SFT achieves good structure by imitating structured outputs; exec+STA achieves good structure by rewarding structural properties. The key advantage of exec+STA over SFT is accuracy (+0.10 prove_rate) — GRPO's exploration discovers proving strategies beyond the SFT training set.\n\n\nSFT on ground-truth FOL translations achieves moderate prove_rate (0.20) — higher than base model (0.12) but lower than GRPO variants (0.28-0.30) — because SFT copies the distribution of training outputs without the exploration-exploitation dynamics that GRPO provides. Crucially, SFT maintains a healthy isr_pr_ratio (0.65) because it imitates human-written formalizations that are structurally sound by construction. This creates an interesting comparison: SFT has good structure but low accuracy; exec-only GRPO has high accuracy but degraded structure; exec+STA GRPO has both. The SFT baseline thus demonstrates that GRPO is necessary for accuracy and STA is necessary for maintaining the structural quality that SFT gets for free from human demonstrations. Held-out performance drops proportionally (0.18, 0.12) because SFT overfits to training problem templates more than GRPO does.\n"
568	  },
569	  {
570	    "name": "SMT-LIB Single-Logic GRPO",
571	    "description": "SMT-LIB third logic type: exec-only vs exec+STA (500 steps, K=8, 1 seed). Stretch goal.\n",
572	    "results": {
573	      "smt_exec_only_prove_rate": 0.18,
574	      "smt_exec_sta_prove_rate": 0.19,
575	      "smt_isr_pr_ratio_exec_only": 0.38,
576	      "smt_isr_pr_ratio_exec_sta": 0.52,
577	      "smt_isr_discriminability": 0.35,
578	      "smt_hacking_modes": [
579	        "trivial_assertions",
580	        "over_constrained_declares",
581	        "unused_variables"
582	      ]
583	    },
584	    "tables": [
585	      {
586	        "name": "Table 10: Three-Logic STA Summary",
587	        "columns": [
588	          "logic",
589	          "exec_only_pr",
590	          "exec_sta_pr",
591	          "exec_only_ratio",
592	          "exec_sta_ratio",
593	          "discriminability"
594	        ],
595	        "rows": [
596	          [
597	            "FOL (Prover9)",
598	            "0.28",
599	            "0.30",
600	            "0.35",
601	            "0.65",
602	            "0.72"
603	          ],
604	          [
605	            "Prolog (SWI)",
606	            "0.22",
607	            "0.24",
608	            "0.32",
609	            "0.58",
610	            "0.45"
611	          ],
612	          [
613	            "SMT-LIB (Z3)",
614	            "0.18",
615	            "0.19",
616	            "0.38",
617	            "0.52",
618	            "0.35"
619	          ]
620	        ]
621	      }
622	    ],
623	    "figures": [],
624	    "analysis": "SMT-LIB completes the three-logic validation, demonstrating the RIP derivation protocol produces functional STA instantiations across theorem proving (FOL), logic programming (Prolog), and constraint satisfaction (SMT-LIB). The diminishing effect magnitude correlates with ISR discriminability, which itself correlates with component independence — a finding that informs future STA instantiation design. Three logic types is sufficient for an EMNLP paper; the consistent qualitative pattern (exec+STA stabilizes structure) across structurally different formal languages is the core evidence for methodology generality.\n\n\nSMT-LIB is the hardest logic type for Qwen3-4B: the syntax is S-expression-based (less represented in pretraining), Z3's error messages are less informative for learning, and the constraint satisfaction paradigm is structurally different from theorem proving. Prove_rate is lower (0.18 exec-only) but still above baseline. SMT-LIB STA uses constraint ablation: remove each assert/declare, check if (check-sat) result changes. Hacking modes are SMT-specific: trivial assertions (assert true), over-constrained declarations (declaring variables with unit domains), unused variables. ISR discriminability (0.35) is lower than FOL (0.72) because SMT-LIB programs have fewer independently ablatable components (many assertions are interdependent). The exec+STA benefit is present but smaller (isr_pr_ratio 0.52 vs 0.38) — still validates the methodology but with less dramatic effect, consistent with the coarser ISR signal.\n"
625	  },
626	  {
627	    "name": "Qwen3-8B Scaling",
628	    "description": "Full MLSR pipeline on Qwen3-8B (1 seed, curriculum α=0.5/β=0.5, 500 steps). Model scale effect.\n",
629	    "results": {
630	      "8b_exec_only_prove_rate": 0.38,
631	      "8b_exec_sta_prove_rate": 0.4,
632	      "8b_exec_only_isr_pr_ratio": 0.4,
633	      "8b_exec_sta_isr_pr_ratio": 0.68,
634	      "8b_held_out_prove_rate": 0.34,
635	      "8b_held_out_isr_mean": 0.28,
636	      "scaling_delta_prove_rate": 0.1,
637	      "scaling_delta_isr_ratio": 0.03
638	    },
639	    "tables": [
640	      {
641	        "name": "Table 11: Scale Comparison (4B vs 8B, curriculum 0.5/0.5)",
642	        "columns": [
643	          "model",
644	          "condition",
645	          "prove_rate",
646	          "isr_pr_ratio",
647	          "held_out_pr"
648	        ],
649	        "rows": [
650	          [
651	            "Qwen3-4B",
652	            "exec-only",
653	            "0.28",
654	            "0.35",
655	            "0.24"
656	          ],
657	          [
658	            "Qwen3-4B",
659	            "exec+STA",
660	            "0.30",
661	            "0.65",
662	            "0.26"
663	          ],
664	          [
665	            "Qwen3-8B",
666	            "exec-only",
667	            "0.38",
668	            "0.40",
669	            "0.32"
670	          ],
671	          [
672	            "Qwen3-8B",
673	            "exec+STA",
674	            "0.40",
675	            "0.68",
676	            "0.34"
677	          ]
678	        ]
679	      }
680	    ],
681	    "figures": [],
682	    "analysis": "8B results serve two functions: (1) demonstrate STA's scale-invariance — the methodology works at larger scales, not just small models where hacking is easier; (2) provide a more competitive absolute prove_rate (0.40) that looks better in a paper. The preserved isr_pr_ratio gap at 8B scale is the key finding — if the gap had closed, it would suggest structural degeneracy is a small-model artifact that STA addresses unnecessarily. Instead, the gap persists, confirming STA is needed regardless of model scale.\n\n\nScaling from 4B to 8B increases prove_rate substantially (+0.10 for both conditions) because the larger model has better baseline FOL syntax knowledge and can explore a wider policy space during GRPO. The isr_pr_ratio pattern is preserved: exec-only degrades to 0.40 (slightly better than 4B's 0.35 — larger models hack slightly less aggressively because they have more capacity for genuine solutions alongside hacking shortcuts), while exec+STA maintains 0.68 (slightly above 4B's 0.65 — same structural reward prevents the same degradation mode). The STA benefit is approximately scale-invariant in relative terms (isr_pr_ratio improvement of ~0.28 at both scales), suggesting that structural degeneracy under exec-only reward is a fundamental property of GRPO optimization, not a small-model artifact. Held-out generalization improves proportionally.\n"
683	  },
684	  {
685	    "name": "Hacking Characterization",
686	    "description": "Manual annotation of 200 outputs per condition (exec-only, exec+STA, base model, SFT) using extensional-shortcut taxonomy. No GPU required.\n",
687	    "results": {
688	      "exec_only_hack_rate": 0.45,
689	      "exec_sta_hack_rate": 0.18,
690	      "base_model_hack_rate": 0.25,
691	      "sft_hack_rate": 0.12,
692	      "exec_only_taxonomy": {
693	        "tautological_premise": 0.18,
694	        "vacuous_quantifier": 0.12,
695	        "redundant_clause": 0.08,
696	        "over_constrained": 0.05,
697	        "other": 0.02
698	      },
699	      "exec_sta_taxonomy": {
700	        "tautological_premise": 0.03,
701	        "vacuous_quantifier": 0.04,
702	        "redundant_clause": 0.06,
703	        "over_constrained": 0.03,
704	        "other": 0.02
705	      },
706	      "inter_annotator_agreement_kappa": 0.78
707	    },
708	    "tables": [
709	      {
710	        "name": "Table 12: Hacking Taxonomy Distribution (%)",
711	        "columns": [
712	          "shortcut_type",
713	          "base_model",
714	          "exec_only",
715	          "exec+STA",
716	          "SFT"
717	        ],
718	        "rows": [
719	          [
720	            "Tautological premise",
721	            "8",
722	            "18",
723	            "3",
724	            "2"
725	          ],
726	          [
727	            "Vacuous quantifier",
728	            "7",
729	            "12",
730	            "4",
731	            "3"
732	          ],
733	          [
734	            "Redundant clause",
735	            "5",
736	            "8",
737	            "6",
738	            "4"
739	          ],
740	          [
741	            "Over-constrained",
742	            "3",
743	            "5",
744	            "3",
745	            "2"
746	          ],
747	          [
748	            "Other/subtle",
749	            "2",
750	            "2",
751	            "2",
752	            "1"
753	          ],
754	          [
755	            "Total hack rate",
756	            "25",
757	            "45",
758	            "18",
759	            "12"
760	          ]
761	        ]
762	      }
763	    ],
764	    "figures": [],
765	    "analysis": "The hacking characterization provides the qualitative evidence that complements the quantitative ISR/PR ratio. Reviewers can see exactly what \"structural degeneracy\" means: 18% of exec-only proved outputs contain tautological premises like \"∀x(P(x) ∨ ¬P(x))\" that trivially satisfy the solver but contribute nothing to the formalization. STA's suppression of these modes (18%→3%) is directly attributable to ISR=0 scores for tautological components. The residual 18% hacking under exec+STA identifies limitations and future work: subtler shortcuts (redundant clauses with small ISR) require finer-grained ablation or curriculum-based emphasis on high-residual hacking modes.\n\nThe hacking taxonomy distinguishes five shortcut types, derived from the Phase 0 pilot analysis and RIP framework. Exec-only training amplifies hacking from 25% (base model) to 45% because GRPO's reward gradient selects for outputs that prove easily, and structural shortcuts prove more easily than genuine formalizations. The distribution is dominated by tautological premises (18%) and vacuous quantifiers (12%) — the two cheapest hacking modes (highest reward-per-character). Exec+STA training suppresses hacking to 18% (below base model's 25%) because STA penalizes these modes: tautological premises drop from 18%→3% (STA assigns ISR=0 to tautology components), vacuous quantifiers from 12%→4%. Residual hacking (18%) consists of subtler shortcuts that partial ISR doesn't fully penalize — primarily redundant clauses (6%) that have small but nonzero ISR contributions. SFT's low hack rate (12%) sets the floor — human-written outputs have few structural shortcuts. Inter-annotator agreement κ=0.78 (substantial) is achievable because the taxonomy categories have operational definitions tied to STA component ablation patterns.\n"
766	  }
767	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1151ef1-a2c2-4a4f-a373-31b5278c7abe",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "30d12a76-9095-493c-86cd-79f1d59a4f5b",
  "sourceToolAssistantUUID": "b1151ef1-a2c2-4a4f-a373-31b5278c7abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T22:42:56.655Z_

<details open><summary>🔧 Tool call — Read · `toolu_013Xeh9ea7C8dQmN1BQXuNf3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30d12a76-9095-493c-86cd-79f1d59a4f5b",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NkYWhzmqWFBxwYEyP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46066ebd-ad45-40b2-8c72-6f21b3bfb190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7crCdsJY67pNNX36kE16r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12139,
      "cache_read_input_tokens": 28382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12139,
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

_source line 37 · 2026-05-13T22:42:56.937Z_

<details><summary>↩ Tool result · `toolu_013Xeh9ea7C8dQmN1BQXuNf3`</summary>

```text
1	tier: best
2	narrative_guidance: 'STA is both diagnostic and corrective: prevents structural degeneracy
3	  while maintaining or improving prove rate. "RIP-derived rewards are the dense+automatic
4	  cell in the ORM-PRM taxonomy, and they work — execution-only training degrades structurally,
5	  STA-rewarded training does not." Multi-logic results demonstrate the 5-step derivation
6	  protocol generalizes across solver types. O(1) negative result strengthens the story
7	  (ablation granularity matters). Target EMNLP main with full confidence.
8	
9	  '
10	imagined_experiments:
11	- name: FOL Exec-Only 500-Step Baseline
12	  plan_id: plan_001
13	  description: 'FOL single-logic GRPO, execution-only reward, 500 steps, K=8, 3 seeds.
14	    Establishes the structural degradation trajectory that STA is designed to prevent.
15	
16	    '
17	  expected_results:
18	    prove_rate_mean: 0.28
19	    prove_rate_std: 0.03
20	    prove_rate_first100: 0.18
21	    prove_rate_last100: 0.33
22	    mean_isr_overall: 0.11
23	    mean_isr_last100: 0.09
24	    isr_pr_ratio_overall: 0.39
25	    isr_pr_ratio_last100: 0.35
26	    isr_pr_ratio_first100: 0.92
27	    parse_rate: 1.0
28	    training_minutes: 79
29	    step_time_s: 9.5
30	  result_rationale: 'Phase 1 pilot (r5) showed prove_rate=0.15 at 100 steps with isr_pr_ratio=1.0
31	    (ISR tracks prove_rate perfectly because the model hasn''t yet learned structural
32	    shortcuts). At 500 steps, GRPO''s policy gradient drives prove_rate up to ~0.28
33	    — substantial improvement from the 0.12 baseline — but the model discovers extensional
34	    shortcuts: tautological premises, vacuous quantifiers, over-constrained formulas
35	    that prove trivially. These shortcuts yield solver-verified "correct" outputs
36	    with degraded internal structure, causing ISR to lag behind prove_rate. The isr_pr_ratio
37	    drops from ~0.92 (step 1-100, structure intact) to ~0.35 (step 400-500, structural
38	    degeneracy). This is the classic reward hacking signature: the model maximizes
39	    the proxy (execution reward) while degrading the latent quality dimension (structural
40	    fidelity). Three seeds provide sufficient signal to distinguish this trend from
41	    noise; std ~0.03 reflects Qwen3-4B''s moderate sensitivity to initialization on
42	    FOLIO-scale data.
43	
44	    '
45	  tables:
46	  - name: 'Table 2a: Exec-Only Training Dynamics (3-seed mean ± std)'
47	    columns:
48	    - step_window
49	    - prove_rate
50	    - mean_isr
51	    - isr_pr_ratio
52	    - reward_mean
53	    rows:
54	    - - 1-100
55	      - 0.18 ± 0.02
56	      - 0.16 ± 0.02
57	      - 0.92 ± 0.05
58	      - 0.18 ± 0.02
59	    - - 101-200
60	      - 0.22 ± 0.02
61	      - 0.16 ± 0.03
62	      - 0.73 ± 0.08
63	      - 0.22 ± 0.02
64	    - - 201-300
65	      - 0.25 ± 0.03
66	      - 0.13 ± 0.03
67	      - 0.52 ± 0.07
68	      - 0.25 ± 0.03
69	    - - 301-400
70	      - 0.27 ± 0.03
71	      - 0.11 ± 0.02
72	      - 0.41 ± 0.06
73	      - 0.27 ± 0.03
74	    - - 401-500
75	      - 0.33 ± 0.04
76	      - 0.09 ± 0.02
77	      - 0.35 ± 0.05
78	      - 0.33 ± 0.04
79	  figures_description:
80	  - 'Figure 2 (left panel): prove_rate and mean_isr vs training step, 3-seed ribbon
81	    plot. prove_rate monotonically increases; ISR rises briefly then plateaus and
82	    declines. The divergence point (~step 150) marks the onset of reward hacking.'
83	  - 'Figure 2 (right panel): isr_pr_ratio vs training step. Smooth decline from ~0.92
84	    to ~0.35, visually encoding the structural degradation rate.'
85	  analysis: 'The exec-only trajectory confirms the core problem statement: execution-only
86	    GRPO optimizes prove_rate effectively (+133% from baseline) but introduces structural
87	    degeneracy that accelerates after step ~150. The declining isr_pr_ratio is the
88	    paper''s primary diagnostic signal. Notably, prove_rate continues improving even
89	    as ISR declines, meaning standard evaluation (accuracy-only) would rate this as
90	    a successful training run. Only STA-derived ISR reveals the hidden failure mode.
91	    This motivates the need for STA as a reward component, not just a diagnostic.
92	
93	    '
94	- name: FOL Exec+STA 500-Step Primary
95	  plan_id: plan_002
96	  description: 'FOL single-logic GRPO, execution+STA reward (full continuous STA),
97	    500 steps, K=8, 3 seeds. Primary validation that STA reward prevents structural
98	    degradation while maintaining prove_rate.
99	
100	    '
101	  expected_results:
102	    prove_rate_mean: 0.3
103	    prove_rate_std: 0.03
104	    prove_rate_first100: 0.16
105	    prove_rate_last100: 0.34
106	    mean_isr_overall: 0.19
107	    mean_isr_last100: 0.22
108	    isr_pr_ratio_overall: 0.63
109	    isr_pr_ratio_last100: 0.65
110	    isr_pr_ratio_first100: 0.48
111	    parse_rate: 1.0
112	    combined_reward_mean: 0.24
113	    training_minutes: 85
114	    step_time_s: 10.2
115	  result_rationale: 'Phase 1 pilot (r5) showed exec+STA with 0.5/0.5 weighting depressed
116	    prove_rate (0.10 vs 0.15 for exec-only) because the STA penalty was too punitive
117	    at initialization, when the model produces mostly unprovable outputs. At 500 steps
118	    with curriculum weighting (sigmoid ramp from sta_weight=0.1→0.5 over first 200
119	    steps), the model first learns to prove (prove_rate rises rapidly steps 1-200
120	    under near-exec-only reward), then learns to prove structurally (ISR catches up
121	    steps 200-500 as STA weight activates). The key prediction: prove_rate matches
122	    or slightly exceeds exec-only (0.30 vs 0.28) because STA reward actively penalizes
123	    the degenerate shortcuts that exec-only relies on for its final prove_rate gains.
124	    The model is forced to find structurally sound proofs, which are more robust and
125	    transfer better. The isr_pr_ratio stabilizes at ~0.65 instead of degrading to
126	    0.35 — this is the headline comparison. The initial dip in isr_pr_ratio (0.48
127	    at step 1-100) reflects the low-STA-weight curriculum phase where behavior approximates
128	    exec-only; it then recovers as STA weight ramps up.
129	
130	    '
131	  tables:
132	  - name: 'Table 2b: Exec+STA Training Dynamics (3-seed mean ± std)'
133	    columns:
134	    - step_window
135	    - prove_rate
136	    - mean_isr
137	    - isr_pr_ratio
138	    - combined_reward
139	    rows:
140	    - - 1-100
141	      - 0.16 ± 0.02
142	      - 0.08 ± 0.02
143	      - 0.48 ± 0.08
144	      - 0.13 ± 0.02
145	    - - 101-200
146	      - 0.22 ± 0.03
147	      - 0.13 ± 0.03
148	      - 0.58 ± 0.07
149	      - 0.17 ± 0.03
150	    - - 201-300
151	      - 0.26 ± 0.03
152	      - 0.17 ± 0.03
153	      - 0.64 ± 0.06
154	      - 0.21 ± 0.03
155	    - - 301-400
156	      - 0.28 ± 0.03
157	      - 0.19 ± 0.03
158	      - 0.67 ± 0.06
159	      - 0.23 ± 0.03
160	    - - 401-500
161	      - 0.34 ± 0.04
162	      - 0.22 ± 0.03
163	      - 0.65 ± 0.05
164	      - 0.28 ± 0.03
165	  figures_description:
166	  - 'Figure 2 (center panel): prove_rate and mean_isr vs training step for exec+STA.
167	    Both curves rise together; ISR tracks prove_rate with a bounded gap (ratio ~0.65),
168	    in stark contrast to exec-only where the gap widens continuously.'
169	  - 'Figure 3: Overlay of isr_pr_ratio for exec-only (declining) and exec+STA (stable/recovering).
170	    This is the paper''s signature figure — the visual proof that STA prevents structural
171	    degradation.'
172	  analysis: 'Exec+STA achieves the best-tier prediction: prove_rate matches exec-only
173	    (0.30 vs 0.28, not statistically different) while maintaining isr_pr_ratio ≥0.5
174	    throughout training (vs exec-only''s degradation to 0.35). The slight prove_rate
175	    advantage (+0.02) emerges because STA penalizes degenerate shortcuts, forcing
176	    the model to discover structurally sound proving strategies that also happen to
177	    generalize better. The 7% wall-clock overhead (10.2s vs 9.5s per step) is negligible.
178	    This validates the core claim: STA reward is Pareto-improving (same accuracy,
179	    better structure) or at worst Pareto-neutral (same accuracy, maintained structure).
180	    The curriculum is load-bearing — without it (as in Phase 1 pilot), the 0.5 STA
181	    weight suppresses early prove_rate learning.
182	
183	    '
184	- name: FOL Held-Out Evaluation
185	  plan_id: plan_003
186	  description: 'Held-out test set evaluation comparing plan_001 (exec-only) vs plan_002
187	    (exec+STA) checkpoints. Full STA metrics on unseen problems to measure generalization.
188	
189	    '
190	  expected_results:
191	    exec_only_held_out_prove_rate: 0.24
192	    exec_sta_held_out_prove_rate: 0.26
193	    exec_only_held_out_isr_mean: 0.08
194	    exec_sta_held_out_isr_mean: 0.22
195	    exec_only_held_out_isr_pr_ratio: 0.33
196	    exec_sta_held_out_isr_pr_ratio: 0.85
197	    exec_only_hacking_prevalence: 0.45
198	    exec_sta_hacking_prevalence: 0.18
199	  result_rationale: 'Held-out evaluation amplifies the structural gap because degenerate
200	    shortcuts overfit to training distribution. Exec-only model''s prove_rate drops
201	    more on held-out (0.24 vs 0.28 in-distribution) because tautological/vacuous shortcuts
202	    are less likely to accidentally match held-out problem structures. Its held-out
203	    ISR drops further (0.08) because the learned shortcuts are even less structurally
204	    valid on new problems. Exec+STA model retains prove_rate better (0.26 vs 0.30,
205	    smaller drop) because structurally sound proofs generalize. Its ISR actually improves
206	    relative to isr_pr_ratio (0.85 vs 0.65 in-distribution) because the remaining
207	    proved outputs are genuinely well-structured — the degenerate easy wins that inflated
208	    training prove_rate without proportional ISR are gone. The hacking prevalence
209	    (fraction of proved outputs that are structurally degenerate by manual taxonomy)
210	    drops from 45% to 18%, directly supporting the "STA corrects, not just detects"
211	    narrative.
212	
213	    '
214	  tables:
215	  - name: 'Table 3: Held-Out Generalization (best checkpoint per condition)'
216	    columns:
217	    - condition
218	    - prove_rate
219	    - mean_isr
220	    - isr_pr_ratio
221	    - hacking_prevalence
222	    rows:
223	    - - Base model (no training)
224	      - '0.12'
225	      - '0.064'
226	      - '0.53'
227	      - '0.25'
228	    - - Exec-only (plan_001)
229	      - '0.24'
230	      - '0.08'
231	      - '0.33'
232	      - '0.45'
233	    - - Exec+STA (plan_002)
234	      - '0.26'
235	      - '0.22'
236	      - '0.85'
237	      - '0.18'
238	    - - Ground-truth reference
239	      - '0.18'
240	      - '0.559'
241	      - —
242	      - '0.0'
243	  figures_description:
244	  - 'Figure 4: Bar chart comparing held-out metrics across conditions. prove_rate
245	    bars are similar height; ISR bars show dramatic gap (0.08 vs 0.22). Includes ground-truth
246	    ISR reference line at 0.559.'
247	  - 'Figure 5: ISR distribution histograms for proved outputs. Exec-only is heavily
248	    left-skewed (mode near 0); exec+STA has a more uniform/right-shifted distribution
249	    approaching ground-truth shape.'
250	  analysis: 'The held-out results deliver the paper''s strongest evidence. While prove_rate
251	    difference is modest and possibly not significant (0.24 vs 0.26, needs paired
252	    test), the ISR gap is dramatic (0.08 vs 0.22, ~2.75x). This means exec-only training
253	    produces models that "prove" held-out problems but via degenerate means (45% hacking
254	    rate), while exec+STA training produces models whose proofs are structurally meaningful.
255	    The isr_pr_ratio inversion (exec-only 0.33 < exec+STA 0.85) is the quantitative
256	    headline. Note the base model''s isr_pr_ratio of 0.53 is higher than trained exec-only''s
257	    0.33 — training actively worsens structural quality under exec-only reward, a
258	    finding that underscores the need for STA.
259	
260	    '
261	- name: STA O(1) vs O(N) Ablation at Scale
262	  plan_id: plan_004
263	  description: 'Rerun exec+STA with fast_isr_fol (O(1) tautology-only check) for 500
264	    steps, 1 seed. Documents the negative result that coarse-grained ablation provides
265	    insufficient signal.
266	
267	    '
268	  expected_results:
269	    prove_rate: 0.27
270	    mean_isr_o1: 0.04
271	    isr_pr_ratio: 0.15
272	    isr_discriminability: 0.08
273	    combined_reward_correlation_with_on: 0.12
274	    training_trajectory: indistinguishable from exec-only
275	  result_rationale: 'Phase 1 r4 already showed O(1) failure at 100 steps. At 500 steps,
276	    the result is cleaner: fast_isr_fol checks only tautology (is the formula trivially
277	    true?), which catches only one of many hacking modes. The model quickly learns
278	    to avoid tautologies while discovering other shortcuts (vacuous quantifiers, over-constrained
279	    premises, redundant clauses) that O(1) cannot detect. Prove_rate (~0.27) and training
280	    dynamics are indistinguishable from exec-only because the O(1) ISR signal is near-zero
281	    for all non-tautological outputs (discriminability 0.08, meaning <8% of proved
282	    outputs receive any ISR signal). The combined reward reduces to effectively exec-only
283	    (correlation with full O(N) ISR is only 0.12). This is the principled negative
284	    result: domain-specific hacking modes require correspondingly granular ablation
285	    components. A single-check approximation captures one failure mode while the model
286	    routes around it to exploit others.
287	
288	    '
289	  tables:
290	  - name: 'Table 4: O(1) vs O(N) Ablation Comparison'
291	    columns:
292	    - metric
293	    - O(N) full STA
294	    - O(1) fast_isr
295	    - exec-only
296	    rows:
297	    - - prove_rate (500 step)
298	      - '0.30'
299	      - '0.27'
300	      - '0.28'
301	    - - mean_isr
302	      - '0.19'
303	      - '0.04'
304	      - '0.11'
305	    - - isr_pr_ratio_last100
306	      - '0.65'
307	      - '0.15'
308	      - '0.35'
309	    - - isr_discriminability
310	      - '0.72'
311	      - '0.08'
312	      - —
313	    - - wall-clock overhead
314	      - +7%
315	      - +1%
316	      - baseline
317	  figures_description:
318	  - 'Figure 6: Three-way isr_pr_ratio trajectory plot (O(N), O(1), exec-only). O(N)
319	    is stable at ~0.65; O(1) and exec-only both decline, with O(1) declining faster
320	    (to 0.15) because the tautology penalty pushes the model toward even more exotic
321	    shortcuts.'
322	  analysis: 'The O(1) negative result is essential for the paper''s methodology argument.
323	    It demonstrates that STA''s value comes from comprehensive component ablation
324	    (O(N) cost per output), not from any single structural check. This motivates the
325	    5-step RIP derivation protocol: each logic type has its own hacking modes, and
326	    the ablation set must cover them all. The O(1) result also preempts reviewer concern
327	    about STA''s computational cost — yes, it''s O(N) per component, but O(1) approximations
328	    demonstrably fail, so the cost is necessary. The slightly worse isr_pr_ratio for
329	    O(1) vs exec-only (0.15 vs 0.35) suggests the tautology penalty actively worsens
330	    structural diversity by forcing the model into a narrower set of non-tautological
331	    shortcuts.
332	
333	    '
334	- name: STA Reward Weight Ablation
335	  plan_id: plan_005
336	  description: 'Test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3) × {fixed, sigmoid curriculum}.
337	    6 runs × 500 steps × 1 seed = 6 runs total.
338	
339	    '
340	  expected_results:
341	    fixed_03_07_prove_rate: 0.2
342	    fixed_03_07_isr_pr_ratio: 0.72
343	    fixed_05_05_prove_rate: 0.25
344	    fixed_05_05_isr_pr_ratio: 0.68
345	    fixed_07_03_prove_rate: 0.3
346	    fixed_07_03_isr_pr_ratio: 0.52
347	    curriculum_03_07_prove_rate: 0.26
348	    curriculum_03_07_isr_pr_ratio: 0.7
349	    curriculum_05_05_prove_rate: 0.3
350	    curriculum_05_05_isr_pr_ratio: 0.65
351	    curriculum_07_03_prove_rate: 0.32
352	    curriculum_07_03_isr_pr_ratio: 0.55
353	    best_config: curriculum α=0.5 β=0.5
354	  result_rationale: 'The weight ablation reveals a clear Pareto frontier trading prove_rate
355	    against structural quality. Fixed weighting shows the expected tradeoff: higher
356	    STA weight (β=0.7) produces highest isr_pr_ratio (0.72) but lowest prove_rate
357	    (0.20) because the STA penalty is too punitive during early training when the
358	    model cannot yet produce provable outputs. Lower STA weight (β=0.3) produces near-exec-only
359	    prove_rate (0.30) but only moderate structural benefit (isr_pr_ratio 0.52 vs exec-only''s
360	    0.35). The sigmoid curriculum consistently Pareto-dominates fixed weighting at
361	    the same terminal α/β: curriculum 0.5/0.5 matches fixed 0.7/0.3''s prove_rate
362	    (0.30) while achieving higher isr_pr_ratio (0.65 vs 0.52). This is because the
363	    curriculum allows exec-reward-dominated early learning (the model first learns
364	    to prove) before STA activates (forcing structural quality). The optimal configuration
365	    is curriculum α=0.5/β=0.5 — it achieves the best prove_rate × isr_pr_ratio product
366	    (0.30 × 0.65 = 0.195) and lies at the Pareto knee. Curriculum α=0.7/β=0.3 achieves
367	    marginally higher prove_rate (0.32) but substantially lower structural quality
368	    — diminishing returns on the accuracy axis.
369	
370	    '
371	  tables:
372	  - name: 'Table 5: Weight Ablation Results (500 steps, 1 seed)'
373	    columns:
374	    - α/β
375	    - schedule
376	    - prove_rate
377	    - isr_pr_ratio
378	    - pr × ratio
379	    rows:
380	    - - 0.3/0.7
381	      - fixed
382	      - '0.20'
383	      - '0.72'
384	      - '0.144'
385	    - - 0.5/0.5
386	      - fixed
387	      - '0.25'
388	      - '0.68'
389	      - '0.170'
390	    - - 0.7/0.3
391	      - fixed
392	      - '0.30'
393	      - '0.52'
394	      - '0.156'
395	    - - 0.3/0.7
396	      - curriculum
397	      - '0.26'
398	      - '0.70'
399	      - '0.182'
400	    - - 0.5/0.5
401	      - curriculum
402	      - '0.30'
403	      - '0.65'
404	      - '0.195'
405	    - - 0.7/0.3
406	      - curriculum
407	      - '0.32'
408	      - '0.55'
409	      - '0.176'
410	    - - 1.0/0.0
411	      - —
412	      - '0.28'
413	      - '0.35'
414	      - '0.098'
415	  figures_description:
416	  - 'Figure 7: Pareto frontier plot (prove_rate vs isr_pr_ratio). Fixed-weight points
417	    form a lower curve; curriculum points form a higher curve. Curriculum 0.5/0.5
418	    is marked as the Pareto-optimal knee.'
419	  - 'Figure 8: Sigmoid curriculum activation curves overlaid with isr_pr_ratio trajectories.
420	    Shows how STA weight ramp-up corresponds to isr_pr_ratio recovery.'
421	  analysis: 'The weight ablation provides three key insights: (1) STA weight has a
422	    predictable dose-response relationship with structural quality, confirming it''s
423	    a genuine training signal, not noise. (2) Sigmoid curriculum is a principled solution
424	    to the Phase 1 pilot''s prove_rate depression problem — it recovers ~0.05 prove_rate
425	    compared to fixed weighting at matched terminal weights. (3) The Pareto analysis
426	    gives practitioners a concrete recommendation: use curriculum 0.5/0.5 for balanced
427	    accuracy-structure, or curriculum 0.7/0.3 if accuracy is the priority. This section
428	    also serves as an implicit response to "how sensitive is STA to hyperparameters?"
429	    — the answer is "moderately, but curriculum scheduling makes it robust."
430	
431	    '
432	- name: Prolog Single-Logic GRPO
433	  plan_id: plan_006
434	  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 1
435	    seed). Second logic type to validate STA derivation protocol generality.
436	
437	    '
438	  expected_results:
439	    prolog_exec_only_prove_rate: 0.22
440	    prolog_exec_sta_prove_rate: 0.24
441	    prolog_exec_only_isr_mean: 0.08
442	    prolog_exec_sta_isr_mean: 0.14
443	    prolog_exec_only_isr_pr_ratio_last100: 0.32
444	    prolog_exec_sta_isr_pr_ratio_last100: 0.58
445	    prolog_isr_discriminability: 0.45
446	    prolog_hacking_modes:
447	    - redundant_clauses
448	    - catch_all_rules
449	    - trivial_unification
450	  result_rationale: 'Prolog STA instantiation uses rule ablation (remove each clause,
451	    check if query still succeeds) — the RIP mapping is: Reachability=clause is syntactically
452	    reachable from query, Infection=clause body binds variables used downstream, Propagation=removing
453	    clause changes query result. Prolog''s hacking modes differ from FOL: instead
454	    of tautological premises, the model produces redundant clauses (rules that never
455	    fire), catch-all rules (match anything via anonymous variables), and trivial unification
456	    chains. These are detectable by STA because ablating redundant/catch-all clauses
457	    doesn''t change the query result (ISR contribution = 0). Prove_rate is slightly
458	    lower than FOL (0.22 vs 0.28 for exec-only) because SWI-Prolog is more sensitive
459	    to syntactic errors and Qwen3-4B has less Prolog in its pretraining data. The
460	    exec+STA pattern replicates: ISR/PR ratio stabilizes (0.58 vs 0.32), confirming
461	    the methodology transfers. Discriminability (0.45) is lower than FOL (~0.72) because
462	    Prolog programs have fewer components per output (fewer clauses to ablate), creating
463	    a coarser ISR signal, but still sufficient for reward shaping.
464	
465	    '
466	  tables:
467	  - name: 'Table 6: Prolog Single-Logic Results (500 steps, 1 seed)'
468	    columns:
469	    - condition
470	    - prove_rate
471	    - mean_isr
472	    - isr_pr_ratio
473	    - discriminability
474	    rows:
475	    - - Exec-only
476	      - '0.22'
477	      - '0.08'
478	      - '0.32'
479	      - —
480	    - - Exec+STA
481	      - '0.24'
482	      - '0.14'
483	      - '0.58'
484	      - '0.45'
485	  figures_description:
486	  - 'Figure 9: Side-by-side isr_pr_ratio trajectories for Prolog (left) and FOL (right).
487	    Same pattern: exec-only declines, exec+STA stabilizes. Different absolute levels
488	    reflect logic-type-specific baseline difficulty.'
489	  analysis: 'Prolog results validate the STA derivation protocol''s generality — the
490	    same 5-step procedure (pilot → shortcuts → classify → RIP map → design checks)
491	    produces a functional ISR signal for a structurally different logic type. The
492	    Prolog-specific hacking modes (redundant clauses, catch-all rules) are distinct
493	    from FOL''s (tautological premises, vacuous quantifiers), confirming that hacking
494	    is logic-type-specific and STA catches it in both cases. Lower absolute metrics
495	    reflect the harder generation task, not methodology failure.
496	
497	    '
498	- name: Multi-Logic GRPO (FOL+Prolog)
499	  plan_id: plan_007
500	  description: 'Multi-logic GRPO training on mixed FOL+Prolog data, exec-only vs exec+STA
501	    (500 steps, K=8, 1 seed). Tests whether joint training enables cross-logic transfer.
502	
503	    '
504	  expected_results:
505	    multi_fol_prove_rate: 0.29
506	    multi_prolog_prove_rate: 0.25
507	    multi_fol_isr_pr_ratio: 0.62
508	    multi_prolog_isr_pr_ratio: 0.55
509	    fol_improvement_over_single: 0.01
510	    prolog_improvement_over_single: 0.03
511	    cross_logic_transfer_signal: positive
512	  result_rationale: 'Multi-logic training with mixed FOL+Prolog batches forces the
513	    model to maintain distinct formalization strategies per logic type, acting as
514	    implicit regularization against logic-specific hacking modes. FOL prove_rate is
515	    marginally better than single-logic (0.29 vs 0.28 exec-only baseline) because
516	    Prolog''s different structural constraints provide auxiliary gradient signal.
517	    Prolog benefits more (+0.03 over single-logic''s 0.24) because FOL training data
518	    is larger and the formal reasoning skills partially transfer (both involve quantifier
519	    scoping, logical connectives, variable binding). The isr_pr_ratio is slightly
520	    lower than single-logic exec+STA for both (0.62 vs 0.65 for FOL, 0.55 vs 0.58
521	    for Prolog) because the mixed reward signal is noisier — each logic type''s STA
522	    has different component counts and score distributions, creating gradient variance.
523	    The positive transfer signal is modest but measurable, supporting the Claim 2
524	    narrative that GRPO over multiple formal languages exhibits useful cross-logic
525	    dynamics.
526	
527	    '
528	  tables:
529	  - name: 'Table 7: Multi-Logic vs Single-Logic Comparison'
530	    columns:
531	    - logic
532	    - training
533	    - prove_rate
534	    - isr_pr_ratio
535	    - Δ vs single
536	    rows:
537	    - - FOL
538	      - single exec+STA
539	      - '0.30'
540	      - '0.65'
541	      - —
542	    - - FOL
543	      - multi exec+STA
544	      - '0.29'
545	      - '0.62'
546	      - -0.01 / -0.03
547	    - - Prolog
548	      - single exec+STA
549	      - '0.24'
550	      - '0.58'
551	      - —
552	    - - Prolog
553	      - multi exec+STA
554	      - '0.25'
555	      - '0.55'
556	      - +0.01 / -0.03
557	  figures_description:
558	  - 'Figure 10: Grouped bar chart showing single-logic vs multi-logic prove_rate and
559	    isr_pr_ratio per logic type. Modest gains in prove_rate for Prolog; slight isr_pr_ratio
560	    decrease across both.'
561	  analysis: 'Multi-logic results are positive but not dramatic — the transfer signal
562	    is real but modest at 4B scale with 500 steps. This is expected: cross-logic transfer
563	    requires the model to abstract beyond surface syntax to shared logical reasoning
564	    patterns, which 4B models have limited capacity for. The paper frames this as
565	    "measurably positive transfer" rather than "large effect," setting up future work
566	    on larger models. The slight isr_pr_ratio decrease under multi-logic training
567	    is an important nuance — mixed reward signals add noise, suggesting that logic-specific
568	    STA calibration (e.g., per-logic α/β) could improve multi-logic training.
569	
570	    '
571	- name: Cross-Logic Transfer Evaluation
572	  plan_id: plan_008
573	  description: 'Zero-shot cross-logic evaluation: FOL-trained model on Prolog tasks,
574	    Prolog-trained model on FOL tasks. Measures transfer without explicit multi-logic
575	    training.
576	
577	    '
578	  expected_results:
579	    fol_model_on_prolog_prove_rate: 0.16
580	    prolog_model_on_fol_prove_rate: 0.17
581	    fol_model_on_prolog_delta_vs_base: 0.04
582	    prolog_model_on_fol_delta_vs_base: 0.05
583	    cross_logic_transfer_delta_mean: 0.045
584	  result_rationale: 'Cross-logic transfer delta [0.02, 0.08] predicted range. FOL→Prolog
585	    transfer (+0.04 prove_rate over base model''s ~0.12 Prolog prove_rate) is modest
586	    because FOL training teaches quantifier handling and logical structure that partially
587	    maps to Prolog''s clause semantics — both require correct variable scoping and
588	    logical decomposition. Prolog→FOL transfer (+0.05) is slightly larger because
589	    Prolog''s rule-based reasoning develops a "compositional formalization" skill
590	    that transfers to FOL premise construction. Neither direction produces dramatic
591	    gains because the surface syntax is too different for shallow transfer, and 4B
592	    models at 500 steps don''t develop deep enough logical abstractions for strong
593	    transfer. The positive delta (mean 0.045) is nonetheless noteworthy — it suggests
594	    shared latent formal reasoning capabilities that multi-logic training could amplify.
595	    Exec+STA-trained models show marginally higher transfer than exec-only trained
596	    models (+0.01 additional delta) because structurally sound formalizations encode
597	    more transferable logical patterns.
598	
599	    '
600	  tables:
601	  - name: 'Table 8: Cross-Logic Zero-Shot Transfer'
602	    columns:
603	    - source_model
604	    - target_logic
605	    - prove_rate
606	    - Δ vs base
607	    - mean_isr
608	    rows:
609	    - - Base (no training)
610	      - FOL
611	      - '0.12'
612	      - —
613	      - '0.064'
614	    - - Base (no training)
615	      - Prolog
616	      - '0.12'
617	      - —
618	      - '0.05'
619	    - - FOL exec+STA
620	      - Prolog
621	      - '0.16'
622	      - '+0.04'
623	      - '0.09'
624	    - - Prolog exec+STA
625	      - FOL
626	      - '0.17'
627	      - '+0.05'
628	      - '0.10'
629	    - - FOL exec-only
630	      - Prolog
631	      - '0.15'
632	      - '+0.03'
633	      - '0.06'
634	    - - Prolog exec-only
635	      - FOL
636	      - '0.16'
637	      - '+0.04'
638	      - '0.07'
639	  figures_description:
640	  - 'Figure 11: Transfer delta heatmap (source logic × target logic × training condition).
641	    Exec+STA models show consistently higher transfer deltas than exec-only counterparts.'
642	  analysis: 'Cross-logic transfer is positive but small, consistent with the "best"
643	    tier narrative that the methodology generalizes. The exec+STA advantage in transfer
644	    (+0.01 additional delta) is a subtle but important finding: structurally sound
645	    formalizations transfer better because they encode genuine logical structure rather
646	    than solver-specific shortcuts. This supports the paper''s claim that STA doesn''t
647	    just improve in-distribution metrics — it produces qualitatively different model
648	    capabilities.
649	
650	    '
651	- name: SFT Baseline
652	  plan_id: plan_009
653	  description: 'Supervised finetuning on same FOLIO 500 data. Provides a non-RL baseline
654	    for GRPO comparison.
655	
656	    '
657	  expected_results:
658	    sft_prove_rate: 0.2
659	    sft_mean_isr: 0.13
660	    sft_isr_pr_ratio: 0.65
661	    sft_held_out_prove_rate: 0.18
662	    sft_held_out_isr_mean: 0.12
663	  result_rationale: 'SFT on ground-truth FOL translations achieves moderate prove_rate
664	    (0.20) — higher than base model (0.12) but lower than GRPO variants (0.28-0.30)
665	    — because SFT copies the distribution of training outputs without the exploration-exploitation
666	    dynamics that GRPO provides. Crucially, SFT maintains a healthy isr_pr_ratio (0.65)
667	    because it imitates human-written formalizations that are structurally sound by
668	    construction. This creates an interesting comparison: SFT has good structure but
669	    low accuracy; exec-only GRPO has high accuracy but degraded structure; exec+STA
670	    GRPO has both. The SFT baseline thus demonstrates that GRPO is necessary for accuracy
671	    and STA is necessary for maintaining the structural quality that SFT gets for
672	    free from human demonstrations. Held-out performance drops proportionally (0.18,
673	    0.12) because SFT overfits to training problem templates more than GRPO does.
674	
675	    '
676	  tables:
677	  - name: 'Table 9: SFT vs GRPO Comparison'
678	    columns:
679	    - method
680	    - prove_rate
681	    - mean_isr
682	    - isr_pr_ratio
683	    - held_out_pr
684	    rows:
685	    - - SFT
686	      - '0.20'
687	      - '0.13'
688	      - '0.65'
689	      - '0.18'
690	    - - GRPO exec-only
691	      - '0.28'
692	      - '0.11'
693	      - '0.39'
694	      - '0.24'
695	    - - GRPO exec+STA
696	      - '0.30'
697	      - '0.19'
698	      - '0.63'
699	      - '0.26'
700	    - - Base model
701	      - '0.12'
702	      - '0.064'
703	      - '0.53'
704	      - '0.12'
705	  figures_description:
706	  - 'Figure 12: Radar chart showing prove_rate, ISR, isr_pr_ratio, held-out prove_rate,
707	    held-out ISR for each method. exec+STA dominates all axes except held-out ISR
708	    where SFT is competitive.'
709	  analysis: 'SFT baseline serves a narrative function: it shows that structural quality
710	    is a property of the training signal, not an inherent limitation of the model.
711	    SFT achieves good structure by imitating structured outputs; exec+STA achieves
712	    good structure by rewarding structural properties. The key advantage of exec+STA
713	    over SFT is accuracy (+0.10 prove_rate) — GRPO''s exploration discovers proving
714	    strategies beyond the SFT training set.
715	
716	    '
717	- name: SMT-LIB Single-Logic GRPO
718	  plan_id: plan_010
719	  description: 'SMT-LIB third logic type: exec-only vs exec+STA (500 steps, K=8, 1
720	    seed). Stretch goal.
721	
722	    '
723	  expected_results:
724	    smt_exec_only_prove_rate: 0.18
725	    smt_exec_sta_prove_rate: 0.19
726	    smt_isr_pr_ratio_exec_only: 0.38
727	    smt_isr_pr_ratio_exec_sta: 0.52
728	    smt_isr_discriminability: 0.35
729	    smt_hacking_modes:
730	    - trivial_assertions
731	    - over_constrained_declares
732	    - unused_variables
733	  result_rationale: 'SMT-LIB is the hardest logic type for Qwen3-4B: the syntax is
734	    S-expression-based (less represented in pretraining), Z3''s error messages are
735	    less informative for learning, and the constraint satisfaction paradigm is structurally
736	    different from theorem proving. Prove_rate is lower (0.18 exec-only) but still
737	    above baseline. SMT-LIB STA uses constraint ablation: remove each assert/declare,
738	    check if (check-sat) result changes. Hacking modes are SMT-specific: trivial assertions
739	    (assert true), over-constrained declarations (declaring variables with unit domains),
740	    unused variables. ISR discriminability (0.35) is lower than FOL (0.72) because
741	    SMT-LIB programs have fewer independently ablatable components (many assertions
742	    are interdependent). The exec+STA benefit is present but smaller (isr_pr_ratio
743	    0.52 vs 0.38) — still validates the methodology but with less dramatic effect,
744	    consistent with the coarser ISR signal.
745	
746	    '
747	  tables:
748	  - name: 'Table 10: Three-Logic STA Summary'
749	    columns:
750	    - logic
751	    - exec_only_pr
752	    - exec_sta_pr
753	    - exec_only_ratio
754	    - exec_sta_ratio
755	    - discriminability
756	    rows:
757	    - - FOL (Prover9)
758	      - '0.28'
759	      - '0.30'
760	      - '0.35'
761	      - '0.65'
762	      - '0.72'
763	    - - Prolog (SWI)
764	      - '0.22'
765	      - '0.24'
766	      - '0.32'
767	      - '0.58'
768	      - '0.45'
769	    - - SMT-LIB (Z3)
770	      - '0.18'
771	      - '0.19'
772	      - '0.38'
773	      - '0.52'
774	      - '0.35'
775	  figures_description:
776	  - 'Figure 13: Three-panel isr_pr_ratio trajectory comparison across logic types.
777	    Same qualitative pattern (exec-only degrades, exec+STA stabilizes) with varying
778	    magnitudes.'
779	  analysis: 'SMT-LIB completes the three-logic validation, demonstrating the RIP derivation
780	    protocol produces functional STA instantiations across theorem proving (FOL),
781	    logic programming (Prolog), and constraint satisfaction (SMT-LIB). The diminishing
782	    effect magnitude correlates with ISR discriminability, which itself correlates
783	    with component independence — a finding that informs future STA instantiation
784	    design. Three logic types is sufficient for an EMNLP paper; the consistent qualitative
785	    pattern (exec+STA stabilizes structure) across structurally different formal languages
786	    is the core evidence for methodology generality.
787	
788	    '
789	- name: Qwen3-8B Scaling
790	  plan_id: plan_011
791	  description: 'Full MLSR pipeline on Qwen3-8B (1 seed, curriculum α=0.5/β=0.5, 500
792	    steps). Model scale effect.
793	
794	    '
795	  expected_results:
796	    8b_exec_only_prove_rate: 0.38
797	    8b_exec_sta_prove_rate: 0.4
798	    8b_exec_only_isr_pr_ratio: 0.4
799	    8b_exec_sta_isr_pr_ratio: 0.68
800	    8b_held_out_prove_rate: 0.34
801	    8b_held_out_isr_mean: 0.28
802	    scaling_delta_prove_rate: 0.1
803	    scaling_delta_isr_ratio: 0.03
804	  result_rationale: 'Scaling from 4B to 8B increases prove_rate substantially (+0.10
805	    for both conditions) because the larger model has better baseline FOL syntax knowledge
806	    and can explore a wider policy space during GRPO. The isr_pr_ratio pattern is
807	    preserved: exec-only degrades to 0.40 (slightly better than 4B''s 0.35 — larger
808	    models hack slightly less aggressively because they have more capacity for genuine
809	    solutions alongside hacking shortcuts), while exec+STA maintains 0.68 (slightly
810	    above 4B''s 0.65 — same structural reward prevents the same degradation mode).
811	    The STA benefit is approximately scale-invariant in relative terms (isr_pr_ratio
812	    improvement of ~0.28 at both scales), suggesting that structural degeneracy under
813	    exec-only reward is a fundamental property of GRPO optimization, not a small-model
814	    artifact. Held-out generalization improves proportionally.
815	
816	    '
817	  tables:
818	  - name: 'Table 11: Scale Comparison (4B vs 8B, curriculum 0.5/0.5)'
819	    columns:
820	    - model
821	    - condition
822	    - prove_rate
823	    - isr_pr_ratio
824	    - held_out_pr
825	    rows:
826	    - - Qwen3-4B
827	      - exec-only
828	      - '0.28'
829	      - '0.35'
830	      - '0.24'
831	    - - Qwen3-4B
832	      - exec+STA
833	      - '0.30'
834	      - '0.65'
835	      - '0.26'
836	    - - Qwen3-8B
837	      - exec-only
838	      - '0.38'
839	      - '0.40'
840	      - '0.32'
841	    - - Qwen3-8B
842	      - exec+STA
843	      - '0.40'
844	      - '0.68'
845	      - '0.34'
846	  figures_description:
847	  - 'Figure 14: Scale comparison — prove_rate and isr_pr_ratio for 4B vs 8B. Both
848	    conditions scale similarly in prove_rate; the isr_pr_ratio gap (exec-only vs exec+STA)
849	    is preserved at both scales.'
850	  analysis: '8B results serve two functions: (1) demonstrate STA''s scale-invariance
851	    — the methodology works at larger scales, not just small models where hacking
852	    is easier; (2) provide a more competitive absolute prove_rate (0.40) that looks
853	    better in a paper. The preserved isr_pr_ratio gap at 8B scale is the key finding
854	    — if the gap had closed, it would suggest structural degeneracy is a small-model
855	    artifact that STA addresses unnecessarily. Instead, the gap persists, confirming
856	    STA is needed regardless of model scale.
857	
858	    '
859	- name: Hacking Characterization
860	  plan_id: plan_012
861	  description: 'Manual annotation of 200 outputs per condition (exec-only, exec+STA,
862	    base model, SFT) using extensional-shortcut taxonomy. No GPU required.
863	
864	    '
865	  expected_results:
866	    exec_only_hack_rate: 0.45
867	    exec_sta_hack_rate: 0.18
868	    base_model_hack_rate: 0.25
869	    sft_hack_rate: 0.12
870	    exec_only_taxonomy:
871	      tautological_premise: 0.18
872	      vacuous_quantifier: 0.12
873	      redundant_clause: 0.08
874	      over_constrained: 0.05
875	      other: 0.02
876	    exec_sta_taxonomy:
877	      tautological_premise: 0.03
878	      vacuous_quantifier: 0.04
879	      redundant_clause: 0.06
880	      over_constrained: 0.03
881	      other: 0.02
882	    inter_annotator_agreement_kappa: 0.78
883	  result_rationale: 'The hacking taxonomy distinguishes five shortcut types, derived
884	    from the Phase 0 pilot analysis and RIP framework. Exec-only training amplifies
885	    hacking from 25% (base model) to 45% because GRPO''s reward gradient selects for
886	    outputs that prove easily, and structural shortcuts prove more easily than genuine
887	    formalizations. The distribution is dominated by tautological premises (18%) and
888	    vacuous quantifiers (12%) — the two cheapest hacking modes (highest reward-per-character).
889	    Exec+STA training suppresses hacking to 18% (below base model''s 25%) because
890	    STA penalizes these modes: tautological premises drop from 18%→3% (STA assigns
891	    ISR=0 to tautology components), vacuous quantifiers from 12%→4%. Residual hacking
892	    (18%) consists of subtler shortcuts that partial ISR doesn''t fully penalize —
893	    primarily redundant clauses (6%) that have small but nonzero ISR contributions.
894	    SFT''s low hack rate (12%) sets the floor — human-written outputs have few structural
895	    shortcuts. Inter-annotator agreement κ=0.78 (substantial) is achievable because
896	    the taxonomy categories have operational definitions tied to STA component ablation
897	    patterns.
898	
899	    '
900	  tables:
901	  - name: 'Table 12: Hacking Taxonomy Distribution (%)'
902	    columns:
903	    - shortcut_type
904	    - base_model
905	    - exec_only
906	    - exec+STA
907	    - SFT
908	    rows:
909	    - - Tautological premise
910	      - '8'
911	      - '18'
912	      - '3'
913	      - '2'
914	    - - Vacuous quantifier
915	      - '7'
916	      - '12'
917	      - '4'
918	      - '3'
919	    - - Redundant clause
920	      - '5'
921	      - '8'
922	      - '6'
923	      - '4'
924	    - - Over-constrained
925	      - '3'
926	      - '5'
927	      - '3'
928	      - '2'
929	    - - Other/subtle
930	      - '2'
931	      - '2'
932	      - '2'
933	      - '1'
934	    - - Total hack rate
935	      - '25'
936	      - '45'
937	      - '18'
938	      - '12'
939	  figures_description:
940	  - 'Figure 15: Stacked bar chart of hacking taxonomy by condition. Exec-only bar
941	    is tallest and dominated by tautological/vacuous shortcuts; exec+STA bar is shortest
942	    among trained models with more uniform distribution.'
943	  - 'Figure 16: Sankey diagram showing how hacking modes flow between conditions —
944	    which shortcuts GRPO amplifies and which STA suppresses.'
945	  analysis: 'The hacking characterization provides the qualitative evidence that complements
946	    the quantitative ISR/PR ratio. Reviewers can see exactly what "structural degeneracy"
947	    means: 18% of exec-only proved outputs contain tautological premises like "∀x(P(x)
948	    ∨ ¬P(x))" that trivially satisfy the solver but contribute nothing to the formalization.
949	    STA''s suppression of these modes (18%→3%) is directly attributable to ISR=0 scores
950	    for tautological components. The residual 18% hacking under exec+STA identifies
951	    limitations and future work: subtler shortcuts (redundant clauses with small ISR)
952	    require finer-grained ablation or curriculum-based emphasis on high-residual hacking
953	    modes.'
954	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46066ebd-ad45-40b2-8c72-6f21b3bfb190",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "11f47488-4a56-4599-ba7e-888c8f54a750",
  "sourceToolAssistantUUID": "46066ebd-ad45-40b2-8c72-6f21b3bfb190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T22:42:57.310Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SSaF3xFJhN29UEq6T5hZ2n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11f47488-4a56-4599-ba7e-888c8f54a750",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NkYWhzmqWFBxwYEyP5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc469bde-4b66-4525-8202-d65ceef7fe38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7crCdsJY67pNNX36kE16r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12139,
      "cache_read_input_tokens": 28382,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12139
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 28382,
          "cache_creation_input_tokens": 12139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12139,
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

_source line 39 · 2026-05-13T22:42:57.317Z_

<details><summary>↩ Tool result · `toolu_01SSaF3xFJhN29UEq6T5hZ2n`</summary>

```text
1	---
2	dream_id: dream_20260513T215750
3	tier: best
4	overall_score: 4/6 Borderline Reject
5	timestamp: 2026-05-13T22:32:49.918165+00:00
6	---
7	
8	# Dream Review Report: Solver Trace Ablation
9	
10	**Paper**: "Solver Trace Ablation: Dense Structural Rewards for Formal Reasoning via Mutation Testing"
11	**Review Mode**: Full (2 Reviewers + Roundtable)
12	**Date**: 2026-05-13
13	
14	---
15	
16	## Reviewer Assignments
17	- **R1** (Methods + Experiments): Methodology soundness, experimental rigor, reproducibility
18	- **R2** (Novelty + Related Work): Novelty assessment, related work completeness, positioning
19	
20	---
21	
22	## Step 1: Independent Reviews
23	
24	### R1: Methods + Experiments
25	
26	**Score: 4/6 (Borderline Reject)**
27	
28	#### Strengths
29	
30	**S1. Principled grounding in mutation testing.** The RIP framework provides a well-established theoretical foundation. The mapping—component ablation = mutant generation, solver outcome change = mutant killing—is natural. The insight that mutation adequacy criteria translate to reward signal quality is genuinely novel in the RL-for-formal-reasoning context.
31	
32	**S2. Actionable 5-step derivation protocol.** The procedure (pilot → collect shortcuts → classify → map RIP → design checks) is concrete enough for replication and demonstrated for three distinct solver-language pairs.
33	
34	**S3. Clean combined reward formulation.** r(f) = α·r_exec + β·r_exec·ISR multiplicatively couples execution and structure, ensuring ISR affects only proved outputs. The sigmoid curriculum addresses the initialization sensitivity observed in the pilot.
35	
36	**S4. O(1) vs O(N) negative result.** Discriminability 0.08 vs 0.72 provides principled justification for computational overhead and deepens understanding of why component-level ablation is necessary.
37	
38	**S5. Comprehensive experimental matrix.** All 12 planned experiments are covered: single-logic (3 types), multi-logic, cross-logic transfer, weight ablation, scaling, SFT baseline, hacking characterization.
39	
40	**S6. Manual hacking taxonomy with κ=0.78.** Grounds the quantitative ISR metric in qualitative assessment with concrete examples.
41	
42	#### Weaknesses
43	
44	**W1. ISR conflates necessity with quality.** A component being "necessary for the solver outcome" does not guarantee semantic correctness. A formula with N non-redundant but logically arbitrary premises that convolve to entail the conclusion would score high ISR but be a poor formalization. The gap between structural necessity and semantic adequacy is not discussed.
45	
46	**W2. RIP mapping is informal.** The three-stage decomposition (Reachability, Infection, Propagation) collapses into the single ablation test. Only Propagation is operationally measured. This makes RIP more of an analogy than a formal derivation—"component necessity testing" would be equally accurate.
47	
48	**W3. ISR sensitivity to decomposition granularity.** Discriminability varies (FOL 0.72, Prolog 0.45, SMT-LIB 0.35) but the 5-step protocol provides no guidance on choosing the ablation unit. Splitting premises into sub-clauses or merging premises changes ISR.
49	
50	**W4. Curriculum sigmoid is load-bearing but under-analyzed.** Table 5 shows curriculum Pareto-dominates fixed weighting, but the sigmoid shape (center, slope) is not ablated. Is sigmoid better than linear ramp? What is sensitivity to the ramp midpoint (reported as step 200 of 500)?
51	
52	**W5. Single-seed ablations insufficient.** Plans 004-011 all use 1 seed. Table 5's Pareto dominance claim, Table 6/7's cross-logic validation, and Table 11's scaling analysis could be driven by initialization variance. At minimum, top-2 configurations should have 3 seeds.
53	
54	**W6. Prove rate differences not statistically significant.** Table 1: 0.33±0.04 vs Table 2: 0.34±0.04 (overlapping CIs). Held-out: 0.24 vs 0.26. The paper should state "no significant difference" rather than "matches or slightly exceeds."
55	
56	**W7. ISR optimization is partially circular.** Optimizing ISR as a reward naturally increases ISR. The hacking taxonomy (200 samples, κ=0.78) partially breaks this circularity but is not dispositive. A downstream logical inference task evaluation would be stronger validation.
57	
58	**W8. Simpson's paradox risk in base model ISR/PR.** Base model ISR/PR (0.53) > trained exec-only (0.33), cited as evidence that "training actively worsens structural quality." But the base model computes ISR/PR over only 12% of outputs (those that prove), a self-selected population of "easy" problems that are structurally well-posed. The populations are different.
59	
60	**W9. Multi-logic effects too small.** Table 8: +0.01 PR for Prolog from multi-logic training; Table 9: mean transfer Δ=0.045, STA adds only +0.01. At 1 seed, these are indistinguishable from noise.
61	
62	**W10. Training horizon limited.** 500 steps (4000 rollouts over FOLIO) is short. Does exec-only continue to degrade at 2000+ steps, or stabilize? Does STA's benefit persist or diminish? The limited horizon leaves the durability of STA's structural protection unclear.
63	
64	**W11. SFT baseline comparison conflates training paradigm with data efficiency.** SFT's lower prove rate (0.20 vs 0.30) could reflect imitation learning's limited exploration with 500 examples, not inherent inferiority.
65	
66	#### Questions for Authors
67	1. Can you provide examples where ISR is high but the formalization is semantically wrong? What is the false-positive rate?
68	2. What happens with linear ramp instead of sigmoid? Sensitivity to ramp midpoint?
69	3. Do you have data beyond 500 steps? Does ISR/PR gap persist?
70	4. How do you handle ISR for the ~70% of outputs that fail to prove?
71	5. Have you verified the ISR/PR trend is not an artifact of changing population composition (Simpson's paradox)?
72	6. Who are the hacking taxonomy annotators? If authors, κ=0.78 may be inflated by shared mental models.
73	
74	---
75	
76	### R2: Novelty + Related Work
77	
78	**Score: 3/6 (Borderline Reject)**
79	
80	#### Novelty Assessment
81	
82	**Moderate novelty.** The core idea—leave-one-out ablation of solver input components as a reward signal—is sound but conceptually straightforward. ISR is equivalent to well-known feature importance/sensitivity tests (Shapley-style leave-one-out) applied to a new domain. The genuine contribution is recognizing that this specific application (RL rewards for formal reasoning) is valuable, not the technique itself.
83	
84	The RIP framework invocation is largely window-dressing. Only Propagation is operationally measured. The paper does not use Reachability or Infection as independent diagnostic or reward signals. Renaming "component necessity testing" as "RIP-grounded STA" inflates the theoretical contribution.
85	
86	The 5-step derivation protocol is a practical contribution but methodologically amounts to "run a pilot, find failure modes, design targeted checks"—standard engineering methodology, not a theoretical framework.
87	
88	#### Related Work: Critically Deficient
89	
90	**6 references is unacceptable for a venue paper.** Missing critical citations include:
91	
92	- **Reward shaping theory**: Ng et al. (1999) "Policy invariance under reward transformations" — the foundational result on potential-based reward shaping. STA's combined reward should be discussed in this context.
93	- **Reward hacking/overoptimization**: Gao et al. (2023) "Scaling Laws for Reward Model Overoptimization"; Skalse et al. (2022) "Defining and Characterizing Reward Hacking." The paper's core problem statement (reward hacking under exec-only rewards) must cite this literature.
94	- **GRPO itself**: Shao et al. (2024) "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models" where GRPO was introduced. The paper uses GRPO as its RL algorithm but does not cite its origin.
95	- **Modern formal verification + LLM**: LeanDojo (Yang et al. 2024), Baldur (First et al. 2023), AlphaProof (DeepMind 2024). These are the current state-of-the-art in formal reasoning with LLMs.
96	- **FOLIO dataset**: Han et al. (2022) "FOLIO: Natural Language Reasoning with First-Order Logic." The paper uses FOLIO as its primary dataset without citing it.
97	- **Mutation testing for ML**: DeepMutation (Ma et al. 2018), MuNN. Recent work applying mutation testing to ML systems should be discussed.
98	- **Feature attribution connections**: SHAP (Lundberg & Lee 2017), Leave-One-Out (LOO) feature importance. ISR is structurally equivalent to binary LOO feature importance.
99	- **Dense rewards in RL**: Potential-based reward shaping, intrinsic motivation, curiosity-driven exploration. STA's "dense+automatic" claim needs context within this broader literature.
100	
101	The "EVOM (2026)" reference has no author list — it appears to be a self-citation or placeholder.
102	
103	#### Conceptual Clarity
104	
105	The ORM-PRM taxonomy positioning ("dense + automatic cell") is reasonable but under-argued. The paper should explicitly compare:
106	- Why not train a PRM on solver execution traces? Math-Shepherd and similar approaches learn dense process rewards automatically from execution feedback.
107	- Why is component ablation better than attention-based structural analysis?
108	- How does STA relate to reward shaping theory (Ng 1999)?
109	
110	The "dense reward" claim is weakened by ISR being undefined for 67-88% of training examples (those that fail to prove). The reward r(f) = α·r_exec + β·r_exec·ISR reduces to α·r_exec = 0 for unproved outputs (since r_exec = 0). So for the majority of training examples, STA provides no signal at all. This should be acknowledged.
111	
112	#### Writing Quality
113	
114	The paper is well-organized and clearly written. Claims are generally appropriate, with exceptions noted above (prove rate "matching or slightly exceeding" should be "not significantly different"). The abstract accurately summarizes the content. Tables are clear and consistently formatted.
115	
116	However, the 10-page length feels thin for the experimental breadth — many experiments are described in 2-3 sentences where a full paragraph of analysis would be appropriate. The multi-logic and cross-logic sections are particularly rushed.
117	
118	#### Limitations
119	
120	The Limitations paragraph is honest about model family (Qwen3 only), limited languages, and manual steps. It correctly identifies the "uniform component weighting" limitation. Missing from limitations:
121	- ISR is undefined for unproved outputs (majority of training)
122	- Sensitivity to decomposition granularity
123	- Potential Simpson's paradox in ISR/PR ratio comparisons
124	- Short training horizon (500 steps)
125	
126	#### Questions for Authors
127	1. Has the actual 500-step, 3-seed training been completed, or are results projected from shorter pilots?
128	2. Why is GRPO not cited? Which GRPO implementation was used?
129	3. Can you provide the FOLIO dataset citation?
130	4. How does ISR relate to Shapley values or SHAP-style feature importance?
131	5. Why not compare against a PRM trained on solver traces?
132	6. What is the "EVOM (2026)" reference? It has no authors listed.
133	
134	---
135	
136	## Step 2: Cross-Sharing
137	
138	### R1 responding to R2's concerns:
139	- **Agree** that 6 references is critically deficient. The missing GRPO, FOLIO, and reward hacking citations are serious oversights.
140	- **Agree** that the RIP framing overstates the theoretical contribution. R2's characterization as "window-dressing" is harsh but not unfair — only Propagation is measured.
141	- **Partially agree** on novelty: the domain application (RL rewards for formal reasoning) has genuine value even if LOO ablation is not novel. The 5-step protocol and three-logic demonstration are meaningful contributions.
142	- **Note** R2's concern about whether experiments were actually run vs projected. This cannot be adjudicated from the paper alone but is a valid concern given the limited training horizon and single-seed secondary experiments.
143	
144	### R2 responding to R1's concerns:
145	- **Agree** that ISR conflating necessity with quality (W1) is a fundamental limitation. This aligns with the novelty concern — ISR is a simple binary LOO test, and its limitations are well-known in the feature importance literature.
146	- **Agree** that Simpson's paradox (W8) is a real risk and should be formally tested.
147	- **Agree** that the curriculum analysis (W4) is under-developed for a "load-bearing" design choice.
148	- **Elevate** W7 (circularity): this is arguably the paper's most fundamental concern. The paper optimizes ISR as a reward and then reports ISR improvement as the primary result. The hacking taxonomy breaks this somewhat, but 200 samples with potentially author-authored annotation is not enough.
149	
150	---
151	
152	## Step 3: Convergence
153	
154	### Points of Agreement (both reviewers):
155	1. **Core idea has merit.** Component ablation as a structural reward for formal reasoning is well-motivated and potentially impactful.
156	2. **RIP framing overstated.** Only Propagation is measured; Reachability and Infection add no operational content. "Component necessity testing" is more accurate.
157	3. **Related work critically deficient.** 6 references is far below venue standards. Missing citations to GRPO, FOLIO, reward hacking, reward shaping, and modern formal verification work.
158	4. **Statistical rigor insufficient for secondary claims.** Single-seed ablations (Tables 4-11) cannot support the conclusions drawn. Multi-logic transfer effects (+0.01) are indistinguishable from noise.
159	5. **Prove rate "Pareto-improving" claim overclaimed.** Differences are not statistically significant; should be "no significant prove rate degradation."
160	6. **ISR circularity partially addressed but not resolved.** Hacking taxonomy (200 samples, κ=0.78) helps but is insufficient. Downstream task evaluation needed.
161	7. **ISR undefined for majority of training examples.** The "dense reward" positioning is weakened by ISR contributing 0 signal for 67-88% of outputs.
162	8. **O(1) negative result is a genuine strength.** Both reviewers value this ablation.
163	9. **Comprehensive experimental breadth.** The 12-experiment matrix is thorough for a methods paper, even if individual experiments lack statistical depth.
164	
165	### Points of Disagreement:
166	- **Novelty level**: R1 rates the mutation-testing-to-reward-design insight as "genuinely novel"; R2 sees it as "straightforward LOO applied to a new domain." Converged position: the application is valuable but the technique itself is not novel.
167	- **Severity of related work gap**: R1 flags it as a concern; R2 considers it grounds for rejection. Converged: it is a major weakness that must be addressed but is fixable.
168	- **Overall score**: R1 gives 4 (Borderline Reject), R2 gives 3 (Reject). After discussion, converged at **4 (Borderline Reject)** — the core contribution has value and the paper is fixable, but substantial revision is needed.
169	
170	---
171	
172	## Step 4: Consolidated Assessment
173	
174	### Overall Score: 4/6 (Borderline Reject)
175	
176	### Summary Assessment
177	
178	The paper addresses a real and important problem — structural degeneracy (reward hacking) in execution-only RL for formal reasoning — with a well-motivated solution: component ablation as a dense structural reward. The idea is sound, the experimental plan is comprehensive, and the O(1) negative result is a genuinely informative contribution.
179	
180	However, the paper falls short of top venue standards in several dimensions:
181	
182	### Major Issues (must fix)
183	
184	**M1. Related work critically deficient.** 6 references is unacceptable. The paper must cite GRPO's origin (Shao et al. 2024), the FOLIO dataset (Han et al. 2022), reward hacking literature (Gao et al. 2023; Skalse et al. 2022), reward shaping theory (Ng et al. 1999), and modern formal verification+LLM work (LeanDojo, Baldur, AlphaProof). The "EVOM (2026)" reference lacks authors. A top venue paper in this space should have 25-40 references.
185	
186	**M2. ISR circularity.** The paper optimizes ISR as a reward and reports ISR improvement as the primary result. The hacking taxonomy (Table 12) partially breaks this circularity but relies on 200 samples with potentially non-independent annotators (κ=0.78). The paper needs either: (a) a downstream evaluation showing high-ISR formalizations are genuinely better on an independent criterion, or (b) a much larger and externally-annotated hacking study.
187	
188	**M3. Statistical rigor for secondary claims.** 8 of 12 experiments use a single seed. The weight ablation (Table 5), multi-logic (Tables 8-9), scaling (Table 11), and cross-logic transfer (Table 9) results cannot support the conclusions drawn. Effect sizes of +0.01-0.03 at 1 seed are not meaningful. Minimum: 3 seeds for the top-2 weight configurations and at least 1 secondary logic type.
189	
190	**M4. "Pareto-improving" overclaimed.** Prove rate differences (exec-only 0.28±0.03 vs exec+STA 0.30±0.03) are not statistically significant. The paper should claim "STA preserves prove rate while substantially improving structural quality" rather than "Pareto-improving."
191	
192	### Minor Issues (should fix)
193	
194	**m1. RIP framing overstated.** Only Propagation is operationally measured. Either formalize the Reachability and Infection conditions as independent diagnostic signals, or reframe as "component necessity testing" without the three-stage RIP hierarchy.
195	
196	**m2. "Dense reward" claim weakened.** ISR is undefined for unproved outputs (67-88% of training examples). The reward reduces to r_exec = 0 for these. The paper should acknowledge this and discuss implications for training signal density.
197	
198	**m3. ISR sensitivity to decomposition granularity.** The 5-step protocol should include guidance on choosing the ablation unit. The varying discriminability across logic types (0.72, 0.45, 0.35) is acknowledged but not addressed.
199	
200	**m4. Curriculum under-analyzed.** The sigmoid is load-bearing (Table 5) but its shape parameters are not ablated. Linear ramp comparison and midpoint sensitivity analysis needed.
201	
202	**m5. Simpson's paradox risk in base model comparison.** The claim that "training actively worsens structural quality" (base ISR/PR 0.53 > exec-only 0.33) may be an artifact of different populations. The base model computes ISR/PR over only its 12% prove-rate outputs.
203	
204	**m6. Short training horizon.** 500 steps leaves open whether STA's benefits persist or diminish at longer training.
205	
206	**m7. SFT comparison conflates paradigm with data efficiency.** Should match total compute or effective training signal.
207	
208	### Experiment Coverage vs Design
209	
210	All 12 imagined experiments from the experimental design are present in the paper. Coverage is complete. The primary gap is statistical depth (seeds) rather than breadth.
211	
212	| Experiment | Seeds | Coverage | Concern |
213	|---|---|---|---|
214	| FOL Exec-Only (plan_001) | 3 | ✓ Full | — |
215	| FOL Exec+STA (plan_002) | 3 | ✓ Full | — |
216	| FOL Held-Out (plan_003) | — | ✓ Full | Simpson's paradox |
217	| O(1) vs O(N) (plan_004) | 1 | ✓ Full | Need 3 seeds |
218	| Weight Ablation (plan_005) | 1 | ✓ Full | Need 3 seeds for top configs |
219	| Prolog (plan_006) | 1 | ✓ Full | Need 3 seeds |
220	| Multi-Logic (plan_007) | 1 | ✓ Full | Effects < noise |
221	| Cross-Logic (plan_008) | — | ✓ Full | Effects < noise |
222	| SFT Baseline (plan_009) | — | ✓ Full | Paradigm confound |
223	| SMT-LIB (plan_010) | 1 | ✓ Full | Need 3 seeds |
224	| Qwen3-8B (plan_011) | 1 | ✓ Full | Need 3 seeds |
225	| Hacking Characterization (plan_012) | — | ✓ Full | Annotator independence |
226	
227	### Recommendation
228	
229	**Reject with encouragement to revise and resubmit.** The core contribution — component ablation as a principled dense reward for formal reasoning — has genuine value and could be publishable with:
230	1. Proper related work (expand from 6 to 25+ references)
231	2. 3-seed runs for top-3 configurations beyond the primary FOL comparison
232	3. Either downstream task validation of ISR or larger external hacking annotation study
233	4. Honest statistical characterization (remove "Pareto-improving" for non-significant prove rate differences)
234	5. Either formalize RIP properly or reframe as component necessity testing
235	
236	The direction is promising and the paper would be competitive after these revisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc469bde-4b66-4525-8202-d65ceef7fe38",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "27481f39-1a12-4586-97bd-57af1c583ffd",
  "sourceToolAssistantUUID": "cc469bde-4b66-4525-8202-d65ceef7fe38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-13T22:43:09.709Z_

Now let me also check the actual experimental results that were truly run vs. the "dream" (imagined) results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27481f39-1a12-4586-97bd-57af1c583ffd",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NmCGpaAV8JShFfdPQ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49a7ab82-9c35-4ae3-810b-8db3b8ba1b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VaQaaDiaAAds2M2q9667cd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34149,
      "cache_read_input_tokens": 40521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34149,
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

_source line 41 · 2026-05-13T22:43:11.616Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KMWG33w7oMdMRw5mbiRSHg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49a7ab82-9c35-4ae3-810b-8db3b8ba1b6d",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NmCGpaAV8JShFfdPQ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18c3d70c-2451-464c-b0ff-e3555a33bb52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VaQaaDiaAAds2M2q9667cd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34149,
      "cache_read_input_tokens": 40521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34149,
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

_source line 42 · 2026-05-13T22:43:11.633Z_

<details><summary>↩ Tool result · `toolu_01KMWG33w7oMdMRw5mbiRSHg`</summary>

```text
1	"""Phase 1 GRPO training: execution-only vs execution+STA reward.
2	
3	Usage:
4	  # execution-only (GPU 0)
5	  CUDA_VISIBLE_DEVICES=0 python scripts/train_grpo.py \
6	    --model_path /root/autodl-tmp/models/Qwen3-4B \
7	    --data_path data/proofwriter_fol_500.jsonl \
8	    --reward_mode execution_only --output_dir outputs/grpo_exec_only \
9	    --num_steps 100 --wandb_project solver-trace-ablation
10	
11	  # execution+STA (GPU 1)
12	  CUDA_VISIBLE_DEVICES=1 python scripts/train_grpo.py \
13	    --model_path /root/autodl-tmp/models/Qwen3-4B \
14	    --data_path data/proofwriter_fol_500.jsonl \
15	    --reward_mode execution_sta --output_dir outputs/grpo_exec_sta \
16	    --num_steps 100 --wandb_project solver-trace-ablation
17	"""
18	
19	from __future__ import annotations
20	
21	import argparse
22	import json
23	import logging
24	import os
25	import re
26	import sys
27	import time
28	from datetime import datetime, timezone
29	from pathlib import Path
30	
31	import torch
32	from datasets import Dataset
33	from transformers import AutoModelForCausalLM, AutoTokenizer, TrainerCallback
34	from trl import GRPOConfig, GRPOTrainer
35	
36	sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
37	
38	from src.solvers.factory import get_solver
39	from src.sta.reward import _parse_formalization, fast_sta_reward
40	
41	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
42	logger = logging.getLogger(__name__)
43	
44	
45	SYSTEM_PROMPT = (
46	    "You are a first-order logic (FOL) expert. "
47	    "Given natural language premises and a conclusion, formalize them into FOL.\n\n"
48	    "Output format:\n"
49	    "Premises:\n"
50	    "1. &lt;FOL formula>\n"
51	    "2. &lt;FOL formula>\n"
52	    "...\n"
53	    "Conclusion: &lt;FOL formula>\n\n"
54	    "Use standard FOL notation with predicate-argument syntax: "
55	    "all x (P(x) -> Q(x)), exists x P(x), P(a) & Q(a), -P(a), P(a) | Q(a), P(a) -> Q(a)."
56	)
57	
58	USER_TEMPLATE = (
59	    "Formalize the following in first-order logic.\n\n"
60	    "Context:\n{context}\n\n"
61	    "Statement to formalize:\n{question}"
62	)
63	
64	
65	def load_jsonl(path: str) -> list[dict]:
66	    data = []
67	    with open(path) as f:
68	        for line in f:
69	            line = line.strip()
70	            if line:
71	                data.append(json.loads(line))
72	    return data
73	
74	
75	def build_dataset(data: list[dict]) -> Dataset:
76	    records = []
77	    for item in data:
78	        prompt = [
79	            {"role": "system", "content": SYSTEM_PROMPT},
80	            {"role": "user", "content": USER_TEMPLATE.format(
81	                context=item["context"], question=item["question"]
82	            )},
83	        ]
84	        records.append({
85	            "prompt": prompt,
86	            "id": item.get("id", ""),
87	            "answer": item.get("answer", ""),
88	            "fol_premises": json.dumps(item.get("fol_premises", [])),
89	            "fol_conclusion": item.get("fol_conclusion", ""),
90	        })
91	    return Dataset.from_list(records)
92	
93	
94	def strip_thinking(text: str) -> str:
95	    return re.sub(r"&lt;think>.*?&lt;/think>\s*", "", text, flags=re.DOTALL).strip()
96	
97	
98	def extract_completion_text(completion) -> str:
99	    """Extract text from a completion (handles both string and conversational formats)."""
100	    if isinstance(completion, list):
101	        return completion[-1]["content"] if completion else ""
102	    return completion
103	
104	
105	def make_reward_fn(reward_mode: str, solver, exec_weight: float = 0.5, sta_weight: float = 0.5):
106	    stats = {"total": 0, "parsed": 0, "proved": 0, "isr_sum": 0.0}
107	    step_buf = {"total": 0, "parsed": 0, "proved": 0, "isr_sum": 0.0, "reward_sum": 0.0}
108	
109	    def reward_fn(prompts, completions, **kwargs):
110	        rewards = []
111	        for completion in completions:
112	            text = extract_completion_text(completion)
113	            cleaned = strip_thinking(text)
114	            stats["total"] += 1
115	            step_buf["total"] += 1
116	
117	            if reward_mode == "execution_only":
118	                result = fast_sta_reward(
119	                    {}, cleaned, solver,
120	                    execution_weight=1.0, sta_weight=0.0, timeout=5,
121	                )
122	                reward_val = result["execution_reward"]
123	            else:
124	                result = fast_sta_reward(
125	                    {}, cleaned, solver,
126	                    execution_weight=exec_weight, sta_weight=sta_weight, timeout=5,
127	                )
128	                reward_val = result["combined_reward"]
129	
130	            parsed = "error" not in result.get("details", {})
131	            proved = result["execution_reward"] > 0
132	            isr = result.get("sta_reward", 0.0)
133	
134	            if parsed:
135	                stats["parsed"] += 1
136	                step_buf["parsed"] += 1
137	            if proved:
138	                stats["proved"] += 1
139	                step_buf["proved"] += 1
140	            stats["isr_sum"] += isr
141	            step_buf["isr_sum"] += isr
142	            step_buf["reward_sum"] += reward_val
143	
144	            rewards.append(reward_val)
145	        return rewards
146	
147	    def get_stats():
148	        n = stats["total"]
149	        if n == 0:
150	            return {}
151	        return {
152	            "parse_rate": stats["parsed"] / n,
153	            "prove_rate": stats["proved"] / n,
154	            "mean_isr": stats["isr_sum"] / n,
155	        }
156	
157	    def get_step_stats():
158	        n = step_buf["total"]
159	        if n == 0:
160	            return {}
161	        result = {
162	            "parse_rate": step_buf["parsed"] / n,
163	            "prove_rate": step_buf["proved"] / n,
164	            "mean_isr": step_buf["isr_sum"] / n,
165	            "reward_mean": step_buf["reward_sum"] / n,
166	            "reward_std": 0.0,
167	        }
168	        step_buf["total"] = 0
169	        step_buf["parsed"] = 0
170	        step_buf["proved"] = 0
171	        step_buf["isr_sum"] = 0.0
172	        step_buf["reward_sum"] = 0.0
173	        return result
174	
175	    def reset_stats():
176	        stats["total"] = 0
177	        stats["parsed"] = 0
178	        stats["proved"] = 0
179	        stats["isr_sum"] = 0.0
180	
181	    reward_fn.get_stats = get_stats
182	    reward_fn.get_step_stats = get_step_stats
183	    reward_fn.reset_stats = reset_stats
184	    return reward_fn
185	
186	
187	class LocalLogCallback(TrainerCallback):
188	    def __init__(self, output_dir, reward_fn):
189	        self.output_dir = Path(output_dir)
190	        self.output_dir.mkdir(parents=True, exist_ok=True)
191	        self.log_path = self.output_dir / "reward_log.jsonl"
192	        self.reward_fn = reward_fn
193	        self.last_step = 0
194	
195	    def on_log(self, args, state, control, logs=None, **kwargs):
196	        if logs is None or state.global_step == 0:
197	            return
198	        if state.global_step == self.last_step:
199	            return
200	        self.last_step = state.global_step
201	        step_stats = self.reward_fn.get_step_stats()
202	        entry = {
203	            "step": state.global_step,
204	            "reward_mean": logs.get("reward", step_stats.get("reward_mean", 0.0)),
205	            "reward_std": logs.get("reward_std", step_stats.get("reward_std", 0.0)),
206	            "prove_rate": step_stats.get("prove_rate", 0.0),
207	            "isr_mean": step_stats.get("mean_isr", 0.0),
208	            "parse_rate": step_stats.get("parse_rate", 0.0),
209	            "loss": logs.get("loss", 0.0),
210	            "lr": logs.get("learning_rate", 0.0),
211	            "timestamp": datetime.now(timezone.utc).isoformat(),
212	        }
213	        with open(self.log_path, "a") as f:
214	            f.write(json.dumps(entry) + "\n")
215	            f.flush()
216	        print(
217	            f"[REWARD_LOG] step={entry['step']} reward={entry['reward_mean']:.4f} "
218	            f"prove_rate={entry['prove_rate']:.3f} isr={entry['isr_mean']:.3f} "
219	            f"parse_rate={entry['parse_rate']:.3f}",
220	            flush=True,
221	        )
222	
223	
224	def parse_args():
225	    parser = argparse.ArgumentParser(description="Phase 1 GRPO Training")
226	    parser.add_argument("--model_path", type=str, default=None)
227	    parser.add_argument("--data_path", type=str, default=None)
228	    parser.add_argument("--reward_mode", type=str, default=None,
229	                        choices=["execution_only", "execution_sta"])
230	    parser.add_argument("--output_dir", type=str, default=None)
231	    parser.add_argument("--num_steps", type=int, default=100)
232	    parser.add_argument("--per_device_batch_size", type=int, default=4)
233	    parser.add_argument("--gradient_accumulation_steps", type=int, default=2)
234	    parser.add_argument("--num_generations", type=int, default=4)
235	    parser.add_argument("--max_completion_length", type=int, default=512)
236	    parser.add_argument("--learning_rate", type=float, default=1e-6)
237	    parser.add_argument("--exec_weight", type=float, default=0.5)
238	    parser.add_argument("--sta_weight", type=float, default=0.5)
239	    parser.add_argument("--seed", type=int, default=42)
240	    parser.add_argument("--solver", type=str, default="prover9")
241	    parser.add_argument("--wandb_project", type=str, default=None)
242	    parser.add_argument("--wandb_run", type=str, default=None)
243	    parser.add_argument("--no_wandb", action="store_true")
244	    parser.add_argument("--config", type=str, default=None,
245	                        help="YAML config file (overrides CLI args)")
246	    args = parser.parse_args()
247	
248	    if args.config:
249	        cfg = load_yaml_config(args.config)
250	        for k, v in cfg.items():
251	            if hasattr(args, k):
252	                current = getattr(args, k)
253	                if current is None or (isinstance(v, bool) and v and not current):
254	                    setattr(args, k, v)
255	            else:
256	                setattr(args, k, v)
257	
258	    missing = [f for f in ("model_path", "data_path", "reward_mode", "output_dir")
259	               if getattr(args, f, None) is None]
260	    if missing:
261	        parser.error(f"the following arguments are required: {', '.join('--' + f for f in missing)}")
262	
263	    return args
264	
265	
266	def load_yaml_config(path: str) -> dict:
267	    import yaml
268	    with open(path) as f:
269	        return yaml.safe_load(f)
270	
271	
272	def main():
273	    args = parse_args()
274	
275	    if args.no_wandb:
276	        os.environ["WANDB_MODE"] = "disabled"
277	
278	    report_to = "none" if args.no_wandb else "wandb"
279	    if args.wandb_project and not args.no_wandb:
280	        import wandb
281	        run_name = args.wandb_run or f"grpo_{args.reward_mode}"
282	        wandb.init(project=args.wandb_project, name=run_name, config=vars(args))
283	
284	    logger.info(f"Loading data from {args.data_path}")
285	    raw_data = load_jsonl(args.data_path)
286	    dataset = build_dataset(raw_data)
287	    logger.info(f"Dataset: {len(dataset)} examples")
288	
289	    logger.info(f"Initializing solver: {args.solver}")
290	    solver = get_solver(args.solver)
291	    logger.info(f"Solver ready: {type(solver).__name__}")
292	
293	    reward_fn = make_reward_fn(
294	        args.reward_mode, solver,
295	        exec_weight=args.exec_weight, sta_weight=args.sta_weight,
296	    )
297	
298	    grpo_config = GRPOConfig(
299	        output_dir=args.output_dir,
300	        max_steps=args.num_steps,
301	        per_device_train_batch_size=args.per_device_batch_size,
302	        gradient_accumulation_steps=args.gradient_accumulation_steps,
303	        learning_rate=args.learning_rate,
304	        num_generations=args.num_generations,
305	        max_completion_length=args.max_completion_length,
306	        logging_steps=1,
307	        save_steps=50,
308	        save_total_limit=2,
309	        save_only_model=True,
310	        report_to=report_to,
311	        bf16=True,
312	        seed=args.seed,
313	        log_completions=True,
314	        num_completions_to_print=2,
315	        chat_template_kwargs={"enable_thinking": False},
316	    )
317	
318	    logger.info(f"Loading model from {args.model_path}")
319	    trainer = GRPOTrainer(
320	        model=args.model_path,
321	        reward_funcs=reward_fn,
322	        args=grpo_config,
323	        train_dataset=dataset,
324	        callbacks=[LocalLogCallback(args.output_dir, reward_fn)],
325	    )
326	
327	    logger.info(f"Starting GRPO training: mode={args.reward_mode}, steps={args.num_steps}")
328	    trainer.train()
329	
330	    logger.info("Saving final model")
331	    trainer.save_model(args.output_dir)
332	
333	    final_stats = reward_fn.get_stats()
334	    logger.info(f"Final reward stats: {final_stats}")
335	
336	    if not args.no_wandb and args.wandb_project:
337	        import wandb
338	        wandb.log({"final/" + k: v for k, v in final_stats.items()})
339	        wandb.finish()
340	
341	    logger.info("Done.")
342	
343	
344	if __name__ == "__main__":
345	    main()
346	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18c3d70c-2451-464c-b0ff-e3555a33bb52",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "80605559-35dd-4e80-a71e-1c19170dd76c",
  "sourceToolAssistantUUID": "18c3d70c-2451-464c-b0ff-e3555a33bb52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T22:43:12.097Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Rue7qS4HZGH9moE36AmM2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/grpo_exec_only.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80605559-35dd-4e80-a71e-1c19170dd76c",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NmCGpaAV8JShFfdPQ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b59bdba-b079-4fea-a51a-5677ca6b92da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VaQaaDiaAAds2M2q9667cd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34149,
      "cache_read_input_tokens": 40521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34149,
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

_source line 44 · 2026-05-13T22:43:12.103Z_

<details><summary>↩ Tool result · `toolu_016Rue7qS4HZGH9moE36AmM2`</summary>

```text
1	model_path: /root/autodl-tmp/models/Qwen3-4B
2	data_path: data/proofwriter_fol_500.jsonl
3	reward_mode: execution_only
4	output_dir: /root/autodl-tmp/outputs/grpo_exec_only
5	num_steps: 100
6	per_device_batch_size: 4
7	gradient_accumulation_steps: 2
8	num_generations: 4
9	max_completion_length: 512
10	learning_rate: 1.0e-6
11	exec_weight: 1.0
12	sta_weight: 0.0
13	seed: 42
14	solver: prover9
15	wandb_project: solver-trace-ablation
16	wandb_run: exec_only
17	no_wandb: true
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b59bdba-b079-4fea-a51a-5677ca6b92da",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "86b1c2a8-0e42-4a8c-9041-a043cef93649",
  "sourceToolAssistantUUID": "3b59bdba-b079-4fea-a51a-5677ca6b92da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-13T22:43:12.559Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PGSJ1ZwnsTcyujSwqN96ke`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/grpo_exec_sta.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86b1c2a8-0e42-4a8c-9041-a043cef93649",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NmCGpaAV8JShFfdPQ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2db6e93e-b882-4199-9682-755ff9ab3d2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VaQaaDiaAAds2M2q9667cd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34149,
      "cache_read_input_tokens": 40521,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34149
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 40521,
          "cache_creation_input_tokens": 34149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34149,
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

_source line 46 · 2026-05-13T22:43:12.565Z_

<details><summary>↩ Tool result · `toolu_01PGSJ1ZwnsTcyujSwqN96ke`</summary>

```text
1	model_path: /root/autodl-tmp/models/Qwen3-4B
2	data_path: data/proofwriter_fol_500.jsonl
3	reward_mode: execution_sta
4	output_dir: /root/autodl-tmp/outputs/grpo_exec_sta
5	num_steps: 100
6	per_device_batch_size: 4
7	gradient_accumulation_steps: 2
8	num_generations: 4
9	max_completion_length: 512
10	learning_rate: 1.0e-6
11	exec_weight: 0.5
12	sta_weight: 0.5
13	seed: 42
14	solver: prover9
15	wandb_project: solver-trace-ablation
16	wandb_run: exec_sta
17	no_wandb: true
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2db6e93e-b882-4199-9682-755ff9ab3d2c",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "f84574ef-93e1-4396-99bd-c502b6da4554",
  "sourceToolAssistantUUID": "2db6e93e-b882-4199-9682-755ff9ab3d2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-13T22:43:31.921Z_

Now let me look at the actual Phase 0 and Phase 1 results to compare with the paper's claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f84574ef-93e1-4396-99bd-c502b6da4554",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NnKLWK45DVzupYLW4Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc945e5e-fd73-43bf-a0ef-458ee051bc71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gNpR7mqWCcUGJ1YpjLsag",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 74670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5373,
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

_source line 48 · 2026-05-13T22:43:33.799Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YNk6erQTW36bPaAX47HoJ9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/sta-phase0-baseline/data/phase0_baseline_summary.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc945e5e-fd73-43bf-a0ef-458ee051bc71",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NnKLWK45DVzupYLW4Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0044de71-f281-402d-944d-9970f7c44c3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gNpR7mqWCcUGJ1YpjLsag",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 74670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5373,
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

_source line 49 · 2026-05-13T22:43:33.812Z_

<details><summary>↩ Tool result · `toolu_01YNk6erQTW36bPaAX47HoJ9`</summary>

```text
1	Phase 0 ISR Baseline Results
2	=============================
3	Model: Qwen3-4B (base, no fine-tuning)
4	Data: 100 FOLIO FOL problems
5	Solver: Prover9
6	
7	Summary:
8	- n_problems: 100
9	- n_proved: 12 (12.0%)
10	- mean_isr: 0.0641 +/- 0.1983
11	- median_isr: 0.0
12	- range: [0.0, 0.889]
13	
14	By answer type:
15	- true:    n=34, proved=9 (26.5%), ISR=0.1345
16	- false:   n=25, proved=1 (4.0%),  ISR=0.0240
17	- unknown: n=41, proved=2 (4.9%),  ISR=0.0302
18	
19	Top ISR (proved):
20	- folio_1255: ISR=0.889 (9 components, 8 necessary)
21	- folio_833:  ISR=0.833 (6 components, 5 necessary)
22	
23	Bottom ISR (proved):
24	- folio_960:  ISR=0.125 (8 components, 1 necessary)
25	- folio_167:  ISR=0.143 (7 components, 1 necessary)
26	
27	Runtime: 336s (3.4s/sample)
28	Full results: server:/root/solver-trace-ablation/outputs/phase0_baseline.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0044de71-f281-402d-944d-9970f7c44c3e",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "dd943ee2-bdef-4f1d-b869-2519a67f3ffe",
  "sourceToolAssistantUUID": "0044de71-f281-402d-944d-9970f7c44c3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-13T22:43:34.390Z_

<details open><summary>🔧 Tool call — Read · `toolu_016sgPodioAv6B4qqdiPNbij`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd943ee2-bdef-4f1d-b869-2519a67f3ffe",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NnKLWK45DVzupYLW4Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b7ccff5-cfc2-42ea-abc8-2204f4873440",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gNpR7mqWCcUGJ1YpjLsag",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5373,
      "cache_read_input_tokens": 74670,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5373
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 74670,
          "cache_creation_input_tokens": 5373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5373,
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

_source line 51 · 2026-05-13T22:43:34.397Z_

<details><summary>↩ Tool result · `toolu_016sgPodioAv6B4qqdiPNbij`</summary>

```text
1	- id: art_20260513_c10626
2	  name: phase0-baseline-results
3	  type: data
4	  description: 'Phase 0 ISR baseline: Qwen3-4B base model on 100 FOLIO FOL problems.
5	    Mean ISR=0.0641, prove rate=12%. Full results at server:/root/solver-trace-ablation/outputs/phase0_baseline.json'
6	  path: projects/solver-trace-ablation/artifacts/sta-phase0-baseline/data/phase0_baseline_summary.txt
7	  url: null
8	  project: solver-trace-ablation
9	  exp_id: sta-phase0-baseline
10	  skill: ''
11	  created_at: '2026-05-13T18:05:35.222614+00:00'
12	  tags:
13	  - phase0
14	  - baseline
15	  - isr
16	  - qwen3-4b
17	- id: art_20260513_4ecf62
18	  name: gt_isr_baseline
19	  type: data
20	  description: 'Ground-truth FOL ISR baseline: 100 FOLIO problems, GT mean ISR=0.5588
21	    (>0.5 confirmed), prove rate=18%, solver execution rate=100%'
22	  path: null
23	  url: file:///root/solver-trace-ablation/outputs/gt_isr_baseline.json
24	  project: solver-trace-ablation
25	  exp_id: sta-gt-isr-baseline
26	  skill: ''
27	  created_at: '2026-05-13T18:13:21.547878+00:00'
28	  tags:
29	  - isr
30	  - baseline
31	  - ground-truth
32	  - folio
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b7ccff5-cfc2-42ea-abc8-2204f4873440",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "1026edc2-37f8-4cb4-9821-bc9a95a9937e",
  "sourceToolAssistantUUID": "5b7ccff5-cfc2-42ea-abc8-2204f4873440",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-13T22:43:39.694Z_

Now let me look at the paper summary more carefully. The user provided a description that mentions **different results** from what the "best" dream paper reports. The summary says the paper reports a **negative result** (STA fails as training reward), while the dream "best" paper shows STA **succeeding**. Let me check the other paper versions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1026edc2-37f8-4cb4-9821-bc9a95a9937e",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NovBH2h4AGaTBPEFae",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e218ff55-a6ae-459f-94b9-e36293846806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpfkUsuCvcjtrnsoJ7VKat",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1150,
      "cache_read_input_tokens": 80043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1150,
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

_source line 53 · 2026-05-13T22:43:40.544Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xq6Wq8nXBy1qoigT76EmEU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e218ff55-a6ae-459f-94b9-e36293846806",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NovBH2h4AGaTBPEFae",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6de9077-761b-484f-ac00-08b333519ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpfkUsuCvcjtrnsoJ7VKat",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1150,
      "cache_read_input_tokens": 80043,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1150
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 80043,
          "cache_creation_input_tokens": 1150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1150,
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

_source line 54 · 2026-05-13T22:43:40.954Z_

<details><summary>↩ Tool result · `toolu_01Xq6Wq8nXBy1qoigT76EmEU`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{amsmath}
5	\usepackage{amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{enumitem}
11	\usepackage{natbib}
12	\usepackage{hyperref}
13	
14	\title{Solver Trace Ablation: A Mutation-Testing-Derived Methodology\\for Detecting Structural Degeneracy in RL-Trained Formalizers}
15	
16	\author{Anonymous}
17	
18	\begin{document}
19	\maketitle
20	
21	% ============================================================
22	\begin{abstract}
23	Reinforcement learning with solver-verified rewards (e.g., GRPO) trains language models that achieve high execution accuracy on formal reasoning tasks but produce structurally degenerate outputs---a form of reward hacking where proved formulas contain tautological padding, vacuous quantifiers, or redundant clauses.
24	We introduce \textbf{Solver Trace Ablation (STA)}, a methodology grounded in the Reachability-Infection-Propagation (RIP) framework from mutation testing, that derives intensional structural rewards from solver execution semantics.
25	For any solver--language pair, STA follows a 5-step derivation protocol to produce domain-specific structural integrity scores via systematic component ablation.
26	Across three logic types (FOL/Prover9, Prolog/SWI-Prolog, SMT-LIB/Z3), STA-derived rewards consistently detect and partially reduce structural degeneracy during GRPO training: on held-out FOL data, STA-trained models produce outputs with 1.9$\times$ higher structural integrity (ISR 0.132 vs.\ 0.068) and reduce the hacking rate from 69\% to 35\%, at a modest accuracy cost of 5 percentage points.
27	Manual annotation of 400 proved outputs reveals that STA effectively suppresses surface-level hacking modes (tautology padding $-$15pp, redundant clauses $-$13pp) but models adaptively shift toward semantic-level shortcuts that evade syntactic ablation.
28	We position STA as a principled monitoring and diagnostic tool: it reliably detects and slows structural degeneracy, while full prevention likely requires complementary curriculum design or semantic-level reward shaping.
29	\end{abstract}
30	
31	% ============================================================
32	\section{Introduction}
33	
34	Recent work demonstrates that reinforcement learning with solver-verified rewards can train language models to generate provably correct formal logic~\cite{xie2025logic,wu2025agentic}.
35	GRPO~\cite{shao2024deepseekmath} with execution-based reward---where the model receives positive signal whenever a solver accepts its output---has emerged as a practical paradigm for improving formalization accuracy without human annotation.
36	
37	However, execution correctness does not entail structural soundness.
38	A first-order logic (FOL) formula can be provable yet structurally degenerate: padded with tautological conjuncts, wrapped in vacuous quantifiers, or inflated with redundant clause duplications.
39	Such outputs exploit the solver's acceptance criterion while circumventing the intended reasoning structure.
40	This \emph{extensional correctness with intensional degeneracy} constitutes a form of reward hacking that existing scalar execution rewards cannot detect.
41	
42	Existing approaches to structural quality enforcement are ad-hoc.
43	\citet{mellgren2025prolog} hand-craft Prolog-specific structure penalties.
44	EVOM~\cite{wang2026evom} demonstrates cross-solver GRPO but relies on scalar execution rewards only.
45	No prior work provides a \emph{general derivation procedure} for structural rewards from solver semantics.
46	
47	We address this gap by adapting the \textbf{Reachability-Infection-Propagation (RIP)} framework from mutation testing to RL reward design.
48	In mutation testing, a test is adequate if mutating (ablating) a program component changes the test outcome~\cite{jia2011mutation}.
49	Analogously, a formula component is \emph{structurally necessary} if its ablation changes the solver's verdict.
50	This yields \textbf{Solver Trace Ablation (STA)}: a 5-step protocol that, for any solver--language pair, derives an Intensional Structural Reward (ISR) measuring component-level necessity.
51	
52	Our contributions:
53	\begin{enumerate}[nosep]
54	  \item A general, solver-agnostic \textbf{STA derivation protocol} grounded in the RIP framework, instantiated for FOL/Prover9, Prolog/SWI-Prolog, and SMT-LIB/Z3.
55	  \item Empirical characterization of \textbf{logic-type-specific reward hacking modes} across three formal languages, including a manually-annotated hacking taxonomy.
56	  \item Evidence that STA functions as a \textbf{principled monitoring and diagnostic tool}: it reliably detects and partially reduces structural degeneracy, with clear characterization of its detection boundaries.
57	\end{enumerate}
58	
59	% ============================================================
60	\section{Related Work}
61	
62	\paragraph{RL for formal reasoning.}
63	DeepSeek-Prover~\cite{xie2025logic} and Logic-RL~\cite{wu2025agentic} apply GRPO with solver-verified rewards to formal theorem proving and logic programming.
64	These approaches use binary execution rewards (proved/not proved) and do not address structural quality of outputs.
65	
66	\paragraph{Structural rewards.}
67	Process Reward Models (PRMs)~\cite{lightman2024lets} provide dense step-level supervision but require human annotation.
68	Outcome Reward Models (ORMs) are sparse but automatic.
69	STA fills the \emph{dense + automatic} cell: it derives step-level (component-level) structural scores automatically from solver semantics, without human labeling.
70	
71	\paragraph{Mutation testing.}
72	The RIP framework~\cite{jia2011mutation} formalizes mutation adequacy: a mutant is killed if (R) the test reaches the mutated statement, (I) the mutation infects the program state, and (P) the infection propagates to the output.
73	We adapt this framework by treating formula components as ``statements'' and solver verdicts as ``test outputs,'' yielding a principled basis for structural necessity scoring.
74	
75	\paragraph{Reward hacking in RL.}
76	Reward hacking---where agents exploit reward signals without achieving intended objectives---is well-documented in RL~\cite{skalse2022defining}.
77	In formal reasoning, this manifests as models producing syntactically valid but structurally degenerate outputs that satisfy execution checks.
78	Our hacking taxonomy provides the first systematic characterization of this phenomenon in formal logic generation.
79	
80	% ============================================================
81	\section{Method}
82	
83	\subsection{Problem Setting}
84	
85	We consider GRPO training of a language model $\pi_\theta$ for formal logic generation.
86	Given a natural language premise $x$, the model generates $K$ candidate formalizations $\{y_1, \ldots, y_K\}$.
87	An external solver $S$ provides execution feedback: $S(y_i) \in \{0, 1\}$ (proved or not).
88	Standard execution-only reward assigns $r_{\text{exec}}(y_i) = S(y_i)$.
89	
90	The \emph{reward hacking problem}: as training progresses, prove rate increases but structural quality degrades.
91	The model learns to produce outputs that satisfy $S$ through degenerate shortcuts rather than sound formalization.
92	
93	\subsection{Solver Trace Ablation (STA)}
94	
95	STA derives an Intensional Structural Reward (ISR) that quantifies the structural necessity of each component in a proved output.
96	
97	\paragraph{5-step derivation protocol.}
98	For a given solver--language pair:
99	\begin{enumerate}[nosep]
100	  \item \textbf{Pilot}: Run execution-only GRPO to collect proved outputs.
101	  \item \textbf{Collect shortcuts}: Identify outputs where execution succeeds despite structural degeneracy.
102	  \item \textbf{Classify}: Categorize shortcut types (e.g., tautological padding, vacuous quantification).
103	  \item \textbf{Map RIP}: For each shortcut category, identify which RIP condition it violates---the component is \emph{reachable} by the solver but its ablation does not \emph{infect} the solver state (the component is removable without changing the verdict).
104	  \item \textbf{Design check}: Implement component ablation: systematically remove each component and re-run the solver to determine structural necessity.
105	\end{enumerate}
106	
107	\paragraph{ISR computation.}
108	For a proved output $y$ with $N$ parseable components $\{c_1, \ldots, c_N\}$:
109	\begin{equation}
110	  \text{ISR}(y) = \frac{1}{N} \sum_{i=1}^{N} \mathbf{1}[S(y \setminus c_i) \neq S(y)]
111	\end{equation}
112	where $y \setminus c_i$ denotes $y$ with component $c_i$ ablated.
113	$\text{ISR}(y) = 1$ means every component is necessary; $\text{ISR}(y) \approx 0$ means most components are structurally redundant.
114	
115	\paragraph{Combined reward.}
116	The training reward combines execution and structural signals:
117	\begin{equation}
118	  r(y) = \alpha \cdot r_{\text{exec}}(y) + \beta \cdot \text{ISR}(y)
119	\end{equation}
120	where $\alpha + \beta = 1$.
121	For outputs where $S(y) = 0$ (not proved), $\text{ISR}(y) = 0$ by convention.
122	
123	\subsection{Logic-Specific Instantiations}
124	
125	\paragraph{FOL/Prover9.}
126	Components are clauses in the CNF representation.
127	Ablation removes one clause at a time and re-runs Prover9.
128	Complexity: $O(N)$ solver calls per output.
129	
130	\paragraph{Prolog/SWI-Prolog.}
131	Components are rules (head :- body).
132	Ablation removes one rule and re-queries SWI-Prolog.
133	Rule dependencies create cascading effects, increasing ISR variance.
134	
135	\paragraph{SMT-LIB/Z3.}
136	Components are \texttt{assert} statements.
137	Ablation removes one assertion and re-checks satisfiability via Z3.
138	Sort annotations and quantifier bindings impose stricter syntactic constraints.
139	
140	% ============================================================
141	\section{Experimental Setup}
142	
143	\paragraph{Model.}
144	We use Qwen3-4B as the primary model and Qwen3-8B for scaling analysis.
145	All GRPO training uses $K=8$ candidate generations per prompt.
146	
147	\paragraph{Data.}
148	FOL experiments use FOLIO~\cite{han2022folio} with Prover9 as the solver.
149	Prolog experiments use a curated set of logic programming tasks with SWI-Prolog.
150	SMT-LIB experiments use constraint satisfaction problems with Z3.
151	
152	\paragraph{Training.}
153	All runs are 500 GRPO steps.
154	FOL experiments use 3 random seeds; Prolog, SMT-LIB, and scaling experiments use 1 seed.
155	Default reward weights: $\alpha = 0.5$, $\beta = 0.5$ (unless otherwise specified in ablations).
156	
157	\paragraph{Metrics.}
158	\begin{itemize}[nosep]
159	  \item \textbf{Prove rate}: fraction of outputs accepted by the solver.
160	  \item \textbf{Mean ISR}: average intensional structural reward across proved outputs.
161	  \item \textbf{ISR/PR ratio}: $\frac{\text{count of proved outputs with ISR} > \tau}{\text{count of proved outputs}}$, measuring structural integrity among proved outputs.
162	  \item \textbf{Hacking rate}: fraction of proved outputs exhibiting structural degeneracy ($1 - \text{ISR/PR ratio}$, approximately).
163	  \item \textbf{Discriminability}: ISR's ability to distinguish structurally sound from degenerate outputs.
164	\end{itemize}
165	
166	% ============================================================
167	\section{Experiments and Results}
168	
169	\subsection{FOL Baseline: Structural Degeneracy Under Execution-Only Reward}
170	
171	We first establish that execution-only GRPO training produces measurable structural degeneracy.
172	Table~\ref{tab:fol_trajectory} shows the training trajectory over 500 steps (3-seed mean).
173	
174	\begin{table}[t]
175	\centering
176	\small
177	\caption{FOL exec-only training trajectory (3-seed mean). Prove rate rises while ISR/PR ratio declines, indicating progressive structural degeneracy.}
178	\label{tab:fol_trajectory}
179	\begin{tabular}{lcccc}
180	\toprule
181	Steps & Prove Rate & Mean ISR & ISR/PR & Reward \\
182	\midrule
183	1--100   & 0.16 & 0.115 & 0.72 & 0.14 \\
184	101--200 & 0.21 & 0.105 & 0.50 & 0.18 \\
185	201--300 & 0.24 & 0.096 & 0.40 & 0.22 \\
186	301--400 & 0.25 & 0.091 & 0.36 & 0.24 \\
187	401--500 & 0.26 & 0.089 & 0.34 & 0.26 \\
188	\bottomrule
189	\end{tabular}
190	\end{table}
191	
192	Prove rate increases steadily from 0.16 to 0.26, while the ISR/PR ratio drops from 0.72 to 0.34.
193	By step 500, roughly two-thirds of proved outputs exhibit structural degeneracy.
194	The divergence between execution accuracy and structural integrity begins within the first 100 steps and accelerates, confirming that reward hacking is not an artifact of overtraining but an inherent dynamic of execution-only GRPO.
195	
196	\subsection{STA as Training Signal: Detection and Partial Prevention}
197	
198	Table~\ref{tab:sta_trajectory} shows the trajectory under combined exec+STA reward ($\alpha=0.5$, $\beta=0.5$).
199	
200	\begin{table}[t]
201	\centering
202	\small
203	\caption{FOL exec+STA training trajectory (3-seed mean). STA slows ISR/PR decline but does not prevent it.}
204	\label{tab:sta_trajectory}
205	\begin{tabular}{lcccc}
206	\toprule
207	Steps & Prove Rate & Mean ISR & ISR/PR & Reward \\
208	\midrule
209	1--100   & 0.11 & 0.053 & 0.68 & 0.082 \\
210	101--200 & 0.15 & 0.082 & 0.55 & 0.116 \\
211	201--300 & 0.18 & 0.094 & 0.52 & 0.128 \\
212	301--400 & 0.19 & 0.089 & 0.47 & 0.136 \\
213	401--500 & 0.20 & 0.084 & 0.42 & 0.142 \\
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	STA reward slows the ISR/PR decline (0.42 vs.\ 0.34 at step 500, $\Delta = +0.08$) but both curves trend downward.
219	The accuracy cost is 6 percentage points (prove rate 0.20 vs.\ 0.26).
220	This confirms STA's role as a \emph{monitoring and decelerating} mechanism rather than a complete preventive one: it detects and penalizes structural degeneracy, slowing its onset, but the model gradually learns to exploit STA's detection boundaries.
221	
222	\subsection{Held-Out Evaluation}
223	\label{sec:heldout}
224	
225	Table~\ref{tab:heldout} compares the two conditions and an SFT baseline on a held-out test set using full STA evaluation.
226	
227	\begin{table}[t]
228	\centering
229	\small
230	\caption{Held-out evaluation with full STA metrics. SFT serves as the structural quality ceiling.}
231	\label{tab:heldout}
232	\begin{tabular}{lcccc}
233	\toprule
234	Method & Prove Rate & Mean ISR & ISR/PR & Hack.\% \\
235	\midrule
236	GRPO exec-only   & 0.22 & 0.068 & 0.31 & 69 \\
237	GRPO exec+STA    & 0.17 & 0.132 & 0.78 & 35 \\
238	SFT              & 0.19 & 0.182 & 0.96 &  8 \\
239	GT reference     & 0.18 & 0.559 & 1.00 &  0 \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	On held-out data, exec+STA achieves 1.9$\times$ higher mean ISR (0.132 vs.\ 0.068) and reduces the hacking rate from 69\% to 35\%.
245	The ISR/PR ratio of 0.78 on held-out data is substantially higher than the training-time value of 0.42, because held-out evaluation applies full component ablation rather than batch-level approximation.
246	
247	SFT---which directly imitates ground-truth FOL---achieves ISR/PR of 0.96 with only 8\% hacking rate, establishing the structural quality ceiling achievable without solver feedback.
248	GRPO exec+STA's prove rate (0.17) is comparable to SFT (0.19), but its structural quality (ISR/PR 0.78) remains well below SFT (0.96), indicating that STA partially but not fully bridges the structural gap between RL and supervised learning.
249	
250	\subsection{Ablation: O(1) vs.\ O(N) STA Granularity}
251	
252	A natural question is whether a lightweight approximation suffices.
253	We compare O(1) STA (tautology-only check) against full O(N) component ablation (Table~\ref{tab:o1_on}).
254	
255	\begin{table}[t]
256	\centering
257	\small
258	\caption{O(1) tautology-only check provides negligible structural benefit over exec-only, validating the necessity of full component ablation.}
259	\label{tab:o1_on}
260	\begin{tabular}{lcccc}
261	\toprule
262	Condition & Prove Rate & ISR/PR & Mean ISR & Overhead \\
263	\midrule
264	Exec-only           & 0.26 & 0.34 & 0.089 & 1.0$\times$ \\
265	Exec + O(1) STA     & 0.24 & 0.33 & 0.079 & 1.02$\times$ \\
266	Exec + O(N) full STA & 0.20 & 0.42 & 0.084 & 1.30$\times$ \\
267	\bottomrule
268	\end{tabular}
269	\end{table}
270	
271	O(1) STA yields ISR/PR of 0.33---virtually identical to exec-only (0.34, $\Delta = -0.01$)---despite 2\% computational overhead.
272	This is an important negative result: the dominant hacking modes in FOL are not pure tautologies but subtler structural degeneracies (redundant clauses, vacuous quantification) that only full component ablation can detect.
273	The 30\% overhead of O(N) STA is justified by the 8 percentage point ISR/PR improvement.
274	
275	\subsection{Reward Weight Ablation and Curriculum}
276	
277	Table~\ref{tab:weight_ablation} explores the accuracy--structure tradeoff across different $\alpha/\beta$ configurations.
278	
279	\begin{table}[t]
280	\centering
281	\small
282	\caption{STA reward weight ablation. Higher $\beta$ (STA weight) improves structural quality at the cost of accuracy. Curriculum scheduling achieves a favorable tradeoff.}
283	\label{tab:weight_ablation}
284	\begin{tabular}{lccccc}
285	\toprule
286	Condition & $\alpha$ & $\beta$ & Prove Rate & ISR/PR & Mean ISR \\
287	\midrule
288	Exec-only      & 1.0 & 0.0 & 0.26 & 0.34 & 0.089 \\
289	STA-light      & 0.7 & 0.3 & 0.22 & 0.38 & 0.084 \\
290	STA-balanced   & 0.5 & 0.5 & 0.19 & 0.42 & 0.080 \\
291	STA-heavy      & 0.3 & 0.7 & 0.16 & 0.46 & 0.074 \\
292	Curriculum     & \multicolumn{2}{c}{$0.7{\to}0.3$} & 0.21 & 0.44 & 0.092 \\
293	\bottomrule
294	\end{tabular}
295	\end{table}
296	
297	The accuracy--structure tradeoff is continuous and unavoidable: no configuration achieves both high prove rate and high ISR/PR.
298	Sigmoid curriculum scheduling ($\alpha$: 0.7$\to$0.3 over 500 steps) achieves a favorable position on the Pareto frontier---prove rate 0.21 with ISR/PR 0.44 and the highest mean ISR (0.092)---by allowing the model to first develop proving capability under high execution weight before gradually increasing structural pressure.
299	The improvement over fixed $\alpha=0.5$ is modest ($+$2pp ISR/PR, $+$1pp prove rate), consistent with curriculum providing incremental rather than transformative benefit.
300	
301	\subsection{Cross-Logic Generalization}
302	\label{sec:crosslogic}
303	
304	To evaluate whether STA generalizes beyond FOL, we instantiate it for Prolog (rule ablation) and SMT-LIB (constraint ablation).
305	
306	\begin{table}[t]
307	\centering
308	\small
309	\caption{Three-logic comparison. STA consistently improves ISR/PR across all logic types, with varying discriminability reflecting instantiation-specific signal strength.}
310	\label{tab:three_logic}
311	\begin{tabular}{llccccc}
312	\toprule
313	Logic & Solver & PR\textsubscript{exec} & PR\textsubscript{STA} & ISR/PR\textsubscript{exec} & ISR/PR\textsubscript{STA} & Disc. \\
314	\midrule
315	FOL     & Prover9    & 0.26 & 0.20 & 0.34 & 0.42 & 0.38 \\
316	Prolog  & SWI-Prolog & 0.11 & 0.08 & 0.40 & 0.52 & 0.21 \\
317	SMT-LIB & Z3         & 0.14 & 0.10 & 0.38 & 0.48 & 0.17 \\
318	\bottomrule
319	\end{tabular}
320	\end{table}
321	
322	Across all three logic types, STA-augmented training improves ISR/PR ratio over exec-only (Table~\ref{tab:three_logic}).
323	The direction of effect is consistent, supporting the generality of the STA derivation protocol.
324	However, discriminability varies substantially (0.38 for FOL vs.\ 0.17 for SMT-LIB), reflecting differences in ablation granularity and component interdependency.
325	Prolog's denser rule dependencies produce noisier ISR signals; SMT-LIB's re-solving overhead is highest (1.55$\times$).
326	
327	Prolog's lower prove rate (0.11 exec-only) limits statistical confidence---with approximately 40 proved samples per seed, ISR statistics are indicative but not conclusive.
328	
329	\subsection{Cross-Logic Transfer}
330	
331	Table~\ref{tab:transfer} evaluates zero-shot cross-logic transfer.
332	
333	\begin{table}[t]
334	\centering
335	\small
336	\caption{Cross-logic transfer matrix. Training induces strong logic-type specialization with near-zero cross-logic transfer.}
337	\label{tab:transfer}
338	\begin{tabular}{llccc}
339	\toprule
340	Trained On & Evaluated On & Prove Rate & Parse Rate & $\Delta$ vs.\ Same \\
341	\midrule
342	FOL    & FOL    & 0.26 & 1.00 & ref \\
343	FOL    & Prolog & 0.02 & 0.35 & $-$0.09 \\
344	Prolog & Prolog & 0.11 & 0.92 & ref \\
345	Prolog & FOL    & 0.04 & 0.55 & $-$0.22 \\
346	Base   & FOL    & 0.03 & 0.48 & --- \\
347	Base   & Prolog & 0.01 & 0.28 & --- \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	Cross-logic transfer is near-zero.
353	FOL-trained models achieve only 0.02 prove rate on Prolog (vs.\ 0.11 for Prolog-trained), and Prolog-trained models achieve 0.04 on FOL (vs.\ 0.26 for FOL-trained).
354	After controlling for base model zero-shot capability, the adjusted transfer delta falls within $[-0.02, +0.03]$---GRPO training induces strong logic-type specialization rather than general formalization ability.
355	
356	This motivates STA's per-logic-type instantiation design: since training dynamics and hacking modes are logic-specific, structural rewards must be derived separately for each solver--language pair.
357	
358	\subsection{Multi-Logic Joint Training}
359	
360	Table~\ref{tab:multi_logic} compares single-logic and multi-logic (FOL+Prolog) GRPO.
361	
362	\begin{table}[t]
363	\centering
364	\small
365	\caption{Multi-logic vs.\ single-logic training. Joint training shows no positive transfer; FOL accuracy drops 5pp from training budget dilution.}
366	\label{tab:multi_logic}
367	\begin{tabular}{llccc}
368	\toprule
369	Setup & Logic & Prove Rate & ISR/PR & $\Delta$ vs.\ Single \\
370	\midrule
371	Single exec-only & FOL    & 0.26 & 0.34 & --- \\
372	Single exec-only & Prolog & 0.11 & 0.40 & --- \\
373	Multi exec-only  & FOL    & 0.21 & 0.36 & $-$0.05 \\
374	Multi exec-only  & Prolog & 0.09 & 0.43 & $-$0.02 \\
375	Multi exec+STA   & FOL    & 0.17 & 0.41 & --- \\
376	Multi exec+STA   & Prolog & 0.07 & 0.49 & --- \\
377	\bottomrule
378	\end{tabular}
379	\end{table}
380	
381	Multi-logic training produces no significant positive transfer.
382	FOL prove rate drops 5 percentage points in the multi-logic setting, attributable to training budget dilution rather than negative transfer.
383	Importantly, STA's structural signal remains effective in the mixed setting: multi-logic exec+STA improves ISR/PR over multi-logic exec-only for both FOL ($+$5pp) and Prolog ($+$6pp).
384	
385	\subsection{Model Scale Analysis}
386	
387	\begin{table}[t]
388	\centering
389	\small
390	\caption{Model scale comparison (FOL, 500 steps). Larger models hack more aggressively, but STA detection scales correspondingly.}
391	\label{tab:scale}
392	\begin{tabular}{llcccc}
393	\toprule
394	Model & Condition & Prove Rate & ISR/PR & Mean ISR & Acc.\ Cost \\
395	\midrule
396	Qwen3-4B & exec-only & 0.26 & 0.34 & 0.089 & --- \\
397	Qwen3-4B & exec+STA  & 0.20 & 0.42 & 0.084 & $-$0.06 \\
398	Qwen3-8B & exec-only & 0.38 & 0.30 & 0.114 & --- \\
399	Qwen3-8B & exec+STA  & 0.31 & 0.40 & 0.124 & $-$0.07 \\
400	\bottomrule
401	\end{tabular}
402	\end{table}
403	
404	Table~\ref{tab:scale} reveals that reward hacking severity scales with model capacity.
405	Qwen3-8B achieves higher prove rate (0.38 vs.\ 0.26) but lower ISR/PR (0.30 vs.\ 0.34) than Qwen3-4B under exec-only training---the larger model finds more sophisticated structural shortcuts.
406	STA's detection remains effective at 8B scale (ISR/PR improvement of 10pp vs.\ 8pp at 4B), suggesting that structural monitoring becomes \emph{more} important, not less, as models scale.
407	
408	% ============================================================
409	\section{Analysis: Reward Hacking Taxonomy}
410	\label{sec:taxonomy}
411	
412	To characterize the hacking modes that STA detects and those it misses, we manually annotated 400 proved outputs (200 per condition) from the held-out evaluation (\S\ref{sec:heldout}).
413	Inter-annotator agreement was $\kappa = 0.72$ (substantial).
414	
415	\begin{table}[t]
416	\centering
417	\small
418	\caption{Hacking taxonomy distribution. STA suppresses surface-level modes it can directly detect (tautology padding, redundant clauses) but models shift toward semantic-level shortcuts (trivial implication, minimal axiom gaming).}
419	\label{tab:taxonomy}
420	\begin{tabular}{lcccc}
421	\toprule
422	Hacking Mode & Exec\% & STA\% & $\Delta$ & Detectable \\
423	\midrule
424	Tautology padding        & 23 &  8 & $-$15 & Yes \\
425	Vacuous quantification   & 19 & 12 & $-$7  & Partial \\
426	Trivial implication      & 15 & 18 & $+$3  & No \\
427	Redundant clause dup.    & 22 &  9 & $-$13 & Yes \\
428	Minimal axiom gaming     &  8 & 14 & $+$6  & No \\
429	Genuine structural       & 13 & 39 & $+$26 & N/A \\
430	\bottomrule
431	\end{tabular}
432	\end{table}
433	
434	Three findings emerge from Table~\ref{tab:taxonomy}:
435	
436	\paragraph{STA effectively suppresses detectable hacking.}
437	Modes that STA directly detects via component ablation---tautology padding and redundant clause duplication---decrease by 28 percentage points combined (45\% $\to$ 17\%).
438	These are ``surface-level'' degeneracies where removing a component does not change the solver verdict.
439	
440	\paragraph{Models exhibit adversarial adaptation.}
441	Modes that STA cannot detect through syntactic ablation---trivial implication chains and minimal axiom gaming---\emph{increase} by 9 percentage points combined (23\% $\to$ 32\%).
442	These involve semantic-level degeneracy: components that are individually necessary for the proof but collectively encode trivial reasoning.
443	This adversarial shift explains why STA's ISR/PR improvement plateaus: as STA penalizes detectable shortcuts, the model migrates to its blind spots.
444	
445	\paragraph{Genuine structural outputs triple.}
446	Despite incomplete prevention, the proportion of genuinely well-structured outputs increases from 13\% to 39\%---a 3$\times$ improvement.
447	This confirms that STA provides substantial practical benefit even as a partial solution.
448	
449	These findings delineate STA's \emph{detection boundary}: it operates at the syntactic component level and is effective against structural redundancy, but semantic-level degeneracy requires either deeper semantic analysis or complementary reward signals.
450	
451	% ============================================================
452	\section{Discussion}
453	
454	\paragraph{STA as monitoring vs.\ prevention.}
455	Our results consistently show that STA detects and slows structural degeneracy but does not prevent it.
456	The ISR/PR ratio declines under all STA configurations (Table~\ref{tab:sta_trajectory}), the hacking rate remains at 35\% on held-out data (Table~\ref{tab:heldout}), and models adaptively shift to semantic-level shortcuts (Table~\ref{tab:taxonomy}).
457	We therefore position STA primarily as a \emph{diagnostic tool}: it provides a principled, quantitative measure of structural integrity that can inform training decisions (early stopping, curriculum adjustment) without claiming to solve reward hacking.
458	
459	\paragraph{The accuracy--structure tradeoff.}
460	Across all experiments, improving structural quality costs accuracy (5--7pp prove rate reduction).
461	This tradeoff appears fundamental: execution rewards and structural rewards impose partially conflicting optimization pressures.
462	Curriculum scheduling partially mitigates the tension (Table~\ref{tab:weight_ablation}) but does not eliminate it.
463	Full resolution likely requires richer reward signals---possibly combining STA with semantic verification or human feedback.
464	
465	\paragraph{Logic-type specificity.}
466	Cross-logic transfer is near-zero (\S\ref{sec:crosslogic}), and hacking modes differ qualitatively across logic types.
467	This validates STA's design as a \emph{derivation protocol} rather than a fixed algorithm: each solver--language pair requires its own instantiation of component ablation, consistent with the RIP framework's emphasis on domain-specific mutation operators.
468	
469	\paragraph{Scaling implications.}
470	The finding that larger models hack more aggressively (Table~\ref{tab:scale}) suggests that structural monitoring is increasingly important as language models scale.
471	STA's detection capability scales with model size, making it a viable monitoring component for larger systems.
472	
473	% ============================================================
474	\section{Conclusion}
475	
476	We introduced Solver Trace Ablation (STA), a methodology grounded in mutation testing's RIP framework for deriving structural integrity rewards from solver execution semantics.
477	Across three logic types and two model scales, STA consistently detects structural degeneracy in GRPO-trained formalizers, achieving 1.9$\times$ higher structural integrity on held-out FOL data while reducing the hacking rate from 69\% to 35\%.
478	Manual annotation of 400 outputs reveals that STA suppresses surface-level hacking modes but models adaptively shift toward semantic-level shortcuts, delineating STA's detection boundary.
479	
480	We position STA as a principled monitoring and diagnostic tool---the first systematic application of mutation testing methodology to RL reward design---rather than a complete solution to reward hacking.
481	Full prevention of structural degeneracy likely requires complementary approaches: semantic-level reward shaping, curriculum design informed by STA's diagnostic output, or hybrid verification combining syntactic ablation with semantic analysis.
482	The 5-step derivation protocol is solver-agnostic and directly applicable to new formal languages and solvers.
483	
484	\paragraph{Limitations.}
485	Our experiments are limited to 500 training steps and a single primary model (Qwen3-4B).
486	Prolog and SMT-LIB experiments use single seeds, limiting statistical confidence.
487	The hacking taxonomy is based on FOL outputs only; Prolog and SMT-LIB may exhibit different hacking mode distributions.
488	STA's $O(N)$ computational overhead (1.3--1.55$\times$) may be prohibitive for very long outputs.
489	
490	\bibliographystyle{plainnat}
491	\begin{thebibliography}{10}
492	
493	\bibitem[Han et al.(2022)]{han2022folio}
494	Han, S., Schoelkopf, H., Zhao, Y., Qi, Z., Riddell, M., Benson, L., Sun, L., Zubova, E., Qiao, Y., Burtell, M., Peng, D., Fan, J., Liu, Z., Barber, S., Zheng, Y., Torber, S., Rao, Z., Qiu, Y., Starber, N., Mosber, B., \& Radev, D.
495	\newblock FOLIO: Natural language reasoning with first-order logic.
496	\newblock \emph{arXiv preprint arXiv:2209.00840}, 2022.
497	
498	\bibitem[Jia and Harman(2011)]{jia2011mutation}
499	Jia, Y. and Harman, M.
500	\newblock An analysis and survey of the development of mutation testing.
501	\newblock \emph{IEEE Transactions on Software Engineering}, 37(5):649--678, 2011.
502	
503	\bibitem[Lightman et al.(2024)]{lightman2024lets}
504	Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and Cobbe, K.
505	\newblock Let's verify step by step.
506	\newblock \emph{ICLR}, 2024.
507	
508	\bibitem[Mellgren et al.(2025)]{mellgren2025prolog}
509	Mellgren, J., Holmstr{\"o}m, E., and Bjurling, M.
510	\newblock Structural penalties for Prolog program synthesis via reinforcement learning.
511	\newblock \emph{arXiv preprint}, 2025.
512	
513	\bibitem[Shao et al.(2024)]{shao2024deepseekmath}
514	Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Zhang, M., Li, Y., Wu, Y., and Guo, D.
515	\newblock DeepSeekMath: Pushing the limits of mathematical reasoning in open language models.
516	\newblock \emph{arXiv preprint arXiv:2402.03300}, 2024.
517	
518	\bibitem[Skalse et al.(2022)]{skalse2022defining}
519	Skalse, J., Howe, N., Krasheninnikov, D., and Krueger, D.
520	\newblock Defining and characterizing reward hacking.
521	\newblock \emph{NeurIPS}, 2022.
522	
523	\bibitem[Wang et al.(2026)]{wang2026evom}
524	Wang, X., Chen, L., and Liu, Y.
525	\newblock EVOM: Cross-solver GRPO for formal verification.
526	\newblock \emph{arXiv preprint}, 2026.
527	
528	\bibitem[Wu et al.(2025)]{wu2025agentic}
529	Wu, Z., Bi, S., and Chen, Z.
530	\newblock Agentic reasoning with logic programming.
531	\newblock \emph{arXiv preprint}, 2025.
532	
533	\bibitem[Xie et al.(2025)]{xie2025logic}
534	Xie, Y., Li, Z., and Wang, H.
535	\newblock Logic-RL: Reinforcement learning for formal logic reasoning.
536	\newblock \emph{arXiv preprint}, 2025.
537	
538	\end{thebibliography}
539	
540	\end{document}
541	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6de9077-761b-484f-ac00-08b333519ca1",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "6ed692f6-5dba-4c71-9ed1-6b39b320d49f",
  "sourceToolAssistantUUID": "b6de9077-761b-484f-ac00-08b333519ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-13T22:43:45.944Z_

Now I have a comprehensive picture. Let me also check the median paper's review and the paper provenance/framing to understand the gap between actual experiments and the "dream" papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ed692f6-5dba-4c71-9ed1-6b39b320d49f",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NpQ2b8qBN9WwW85t3B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a2a6cc7-1fb8-4f76-8260-3ceb720996a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WM3ogmRD3S5RQPwoM59vxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11091,
      "cache_read_input_tokens": 81193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11091,
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

_source line 56 · 2026-05-13T22:43:48.838Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Auk8GmEYXAF3sNs8WLQvu1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a2a6cc7-1fb8-4f76-8260-3ceb720996a6",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NpQ2b8qBN9WwW85t3B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ebd968a-056c-43d2-907c-00531898c36a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WM3ogmRD3S5RQPwoM59vxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11091,
      "cache_read_input_tokens": 81193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11091,
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

_source line 57 · 2026-05-13T22:43:48.850Z_

<details><summary>↩ Tool result · `toolu_01Auk8GmEYXAF3sNs8WLQvu1`</summary>

```text
1	---
2	dream_id: dream_20260513T215750
3	tier: median
4	overall_score: weak reject (3/6)
5	timestamp: 2026-05-13T22:41:07.174689+00:00
6	---
7	
8	# Dream Review Report: Solver Trace Ablation (STA)
9	
10	**Paper**: "Solver Trace Ablation: A Mutation-Testing-Derived Methodology for Detecting Structural Degeneracy in RL-Trained Formalizers"
11	**Dream ID**: 20260513T215750
12	**Review Mode**: Full (2 Reviewers, 4-step roundtable)
13	**Date**: 2026-05-13
14	
15	---
16	
17	## 1. Paper Summary
18	
19	The paper introduces Solver Trace Ablation (STA), a methodology adapted from mutation testing's RIP (Reachability-Infection-Propagation) framework, for detecting structural degeneracy (reward hacking) in GRPO-trained formal logic generators. STA defines an Intensional Structural Reward (ISR) via systematic component ablation: for each proved output, each component is removed and the solver is re-run; the fraction of components whose ablation changes the solver verdict constitutes the ISR score. The combined reward r = α·r_exec + β·ISR is used for GRPO training across three logic types (FOL/Prover9, Prolog/SWI-Prolog, SMT-LIB/Z3). The paper reports 1.9× ISR improvement on held-out FOL data (0.132 vs 0.068), hacking rate reduction from 69% to 35%, at 5pp accuracy cost. A manual annotation of 400 outputs reveals STA suppresses surface-level hacking but models shift toward semantic-level shortcuts.
20	
21	---
22	
23	## 2. Reviewer Summaries
24	
25	### R1 (Methods + Experiments): Score 4/6 (Weak Accept)
26	R1 finds the paper addresses a real problem with a well-motivated approach. The 5-step derivation protocol is portable and the hacking taxonomy provides genuine insight. The honest "partial prevention" framing is commendable. However, R1 identifies four major weaknesses: (1) insufficient statistical rigor for secondary claims (8/12 experiments single-seed), (2) ISR circularity (optimizing and evaluating on the same metric without downstream validation), (3) inadequate explanation of the ISR/PR discrepancy between training (0.42) and held-out (0.78), and (4) ISR sparsity for unproved outputs undermining the "dense + automatic" positioning.
27	
28	### R2 (Novelty + Related Work): Score 3/6 (Weak Reject)
29	R2 finds the problem identification valuable but the novelty insufficient for a top venue. ISR is structurally identical to leave-one-out (LOO) feature importance — a well-known technique applied to a new domain. The RIP framework invocation is cosmetic: only Propagation is operationally measured; Reachability and Infection contribute no independent signal. Related work is critically deficient (8 references vs 25-40 expected), missing entire literatures on reward shaping theory, feature attribution methods, modern formal reasoning with LLMs, and reward hacking mitigation.
30	
31	---
32	
33	## 3. Roundtable Convergence
34	
35	### 3.1 Points of Agreement
36	
37	**Both reviewers agree on:**
38	
39	1. **Problem identification is valuable and timely.** Structural degeneracy under execution-only GRPO training is a real, underappreciated problem. The observation that prove rate rises while structural quality degrades is important.
40	
41	2. **RIP framework invocation is overstated.** Only the Propagation condition is operationally measured. The 5-step protocol maps to RIP in step 4 but this step adds no actionable content beyond step 3 (classification). The methodology is effectively component necessity testing via LOO ablation, with RIP serving as motivating analogy rather than formal grounding.
42	
43	3. **ISR is LOO ablation importance applied to a new domain.** ISR(y) = (1/N) Σ 1[S(y\c_i) ≠ S(y)] is structurally identical to binary leave-one-out feature importance. The novelty is in the application domain (RL reward design for formal reasoning), not in the metric itself. The paper does not cite or discuss this connection to the feature attribution literature.
44	
45	4. **ISR is sparse for the majority of training examples.** With prove rates of 10-26%, ISR provides zero signal for 74-90% of outputs. The "dense + automatic" positioning in the ORM-PRM taxonomy is misleading. ISR is conditionally dense — dense only within the minority of proved outputs.
46	
47	5. **Statistical rigor is insufficient for secondary claims.** Only the core FOL experiments (plans 001-002) use 3 seeds. Eight of twelve experiments use single seeds. Effect sizes in cross-logic, multi-logic, and scaling experiments (8-12pp ISR/PR differences) could easily fall within seed variance. No confidence intervals or significance tests are reported.
48	
49	6. **The hacking taxonomy is the strongest novelty element.** The manually-annotated taxonomy with the adversarial adaptation finding (models shift from surface-level to semantic-level hacking) is a genuine empirical contribution. The O(1) negative result (tautology-only check ≈ exec-only) is informative and well-executed.
50	
51	7. **Related work is thin.** 8 references is below venue standards. Missing citations to reward shaping theory (Ng et al. 1999), feature attribution (SHAP, LOO analysis), modern formal reasoning with LLMs (LeanDojo, AlphaProof), reward hacking mitigation (Gao et al. 2023), and the FOLIO dataset paper.
52	
53	8. **Honest framing is commendable.** The "monitoring/diagnostic tool" positioning is well-calibrated to the evidence. The paper does not overclaim.
54	
55	### 3.2 Points of Divergence
56	
57	**R1 emphasizes experimental concerns:**
58	- The ISR/PR discrepancy between training (0.42) and held-out (0.78) is inadequately explained. The paper attributes it to "batch-level approximation vs full ablation" but does not specify the approximation or analyze its implications. The exec-only condition shows stability (0.34→0.31), making the asymmetry suspicious.
59	- ISR circularity: optimizing ISR as reward and evaluating ISR as metric. No downstream task evaluation validates that high ISR correlates with genuine formalization quality.
60	- Missing random reward baseline: without controlling for multi-objective regularization, it is unclear whether ISR's specific formulation matters or any penalty on proved outputs achieves similar effects.
61	
62	**R2 emphasizes novelty concerns:**
63	- The conceptual advance is modest: recognizing that component ablation reveals structural necessity and using this as an RL reward. This is sound engineering but not a deep conceptual contribution.
64	- The 5-step derivation protocol is standard engineering methodology, not a methodological contribution.
65	- Missing connection to mutation testing theory (equivalent mutant problem, weak vs strong mutation, mutant subsuming).
66	
67	### 3.3 Converged Assessment
68	
69	After cross-sharing, both reviewers agree the paper is **borderline** for a top ML venue main track. The core tension: the paper identifies a real problem, proposes a reasonable solution, and characterizes its limitations honestly — but the technical novelty (LOO ablation as RL reward) and the experimental evidence (single-seed secondary experiments, unexplained ISR/PR discrepancy, no downstream validation) do not clear the bar individually. The strongest contributions (hacking taxonomy, O(1) negative result, honest framing) are genuine but modest.
70	
71	**Consensus score: 3.5/6 (borderline Weak Reject / Weak Accept)**, rounded to **Weak Reject** for main track, with clear path to **Findings** after revision.
72	
73	---
74	
75	## 4. Detailed Strengths
76	
77	**S1. Genuine problem identification (High impact).** The paper provides the first systematic quantification of structural degeneracy in execution-only GRPO for formal reasoning. The prove_rate ↑ / ISR/PR ↓ divergence pattern (Table 1) is a clear, reproducible finding.
78	
79	**S2. Hacking taxonomy with adversarial adaptation (Medium-high impact).** The finding that STA suppresses surface-level hacking (tautology padding −15pp, redundant clauses −13pp) while models shift to semantic-level shortcuts (trivial implication +3pp, minimal axiom gaming +6pp) is a genuine empirical insight with implications for reward design more broadly. κ=0.72 is substantial.
80	
81	**S3. O(1) negative result (Medium impact).** Demonstrating that tautology-only check provides negligible benefit (ISR/PR 0.33 ≈ exec-only 0.34) validates the need for full component ablation and refutes the "simple heuristic" alternative.
82	
83	**S4. Three-logic instantiation (Medium impact).** Demonstrating the ablation approach across FOL, Prolog, and SMT-LIB supports generality in principle, even if single-seed evidence is thin.
84	
85	**S5. Honest framing (Presentation strength).** The paper consistently positions STA as "monitoring/diagnostic tool" rather than "solution," acknowledges the accuracy-structure tradeoff as fundamental, and does not overclaim.
86	
87	**S6. Well-organized paper.** Tables are clear, section structure is logical, and claims generally match evidence.
88	
89	---
90	
91	## 5. Detailed Weaknesses
92	
93	### Major
94	
95	**W1. ISR novelty is overstated (Novelty, Major).**
96	ISR is structurally equivalent to binary LOO feature importance — a technique with decades of history in statistics and ML interpretability (Shapley values, SHAP, permutation importance). The paper does not acknowledge this connection. The RIP framework invocation dresses up a known technique with borrowed terminology: only Propagation is measured; Reachability and Infection contribute nothing operational. The paper should honestly position ISR as "LOO ablation importance applied to RL rewards for formal reasoning" — application novelty, not metric novelty.
97	
98	**W2. Statistical rigor insufficient for secondary claims (Experimental, Major).**
99	Eight of twelve experiments use single random seeds. The cross-logic generalization claim — a central contribution — rests entirely on single-seed evidence with effect sizes (8-12pp ISR/PR) that could be noise. No confidence intervals, significance tests, or effect size estimates are reported for any comparison. This is the most damaging experimental weakness because the paper's breadth-over-depth strategy requires secondary results to be reliable.
100	
101	**W3. ISR/PR discrepancy between training and held-out (Experimental, Major).**
102	The ISR/PR ratio jumps from 0.42 (training, Table 2) to 0.78 (held-out, Table 3) for the STA condition, while exec-only is stable (0.34→0.31). The paper attributes this to "batch-level approximation vs full component ablation" but does not specify the approximation or analyze its implications. This asymmetry suggests training-time and evaluation-time ISR are computed differently, which means the model is optimized against a different objective than the one being evaluated. The headline "1.9× higher structural integrity" rests on held-out numbers whose relationship to training dynamics is unclear.
103	
104	**W4. ISR circularity without downstream validation (Experimental, Major).**
105	The paper optimizes ISR as a reward and evaluates ISR improvement as the primary result. No downstream task evaluation (e.g., logical inference accuracy using generated formalizations, proof quality assessment by external verifiers) validates that high ISR correlates with genuine formalization quality. The hacking taxonomy partially breaks this circularity, but 200 samples with undisclosed annotator identity is insufficient.
106	
107	**W5. ISR sparsity undermines "dense + automatic" positioning (Framing, Major).**
108	With prove rates of 10-26%, ISR provides zero signal for 74-90% of training outputs. The paper's claim to fill the "dense + automatic" cell in the ORM-PRM taxonomy is misleading. ISR is conditionally dense — dense only within the small proved subset. This should be explicitly acknowledged.
109	
110	### Moderate
111	
112	**W6. Related work critically deficient (Presentation, Moderate).**
113	8 references is far below venue standards (25-40 expected). Missing entire literatures: reward shaping theory (Ng et al. 1999), feature attribution (SHAP, LOO analysis), modern formal reasoning with LLMs (LeanDojo, AlphaProof, Baldur), reward hacking mitigation (Gao et al. 2023, RLHF), program synthesis quality metrics (CodeBLEU, functional correctness), intrinsic motivation literature.
114	
115	**W7. No random reward baseline (Experimental, Moderate).**
116	Without a control for the general regularization effect of multi-objective optimization, it is unclear whether ISR's specific component-ablation formulation matters, or whether any penalty on proved outputs would achieve similar structural improvement. A random structural penalty baseline is needed.
117	
118	**W8. Hacking taxonomy is FOL-only (Experimental, Moderate).**
119	The paper claims cross-logic generalization but provides hacking characterization for only FOL. Prolog and SMT-LIB may exhibit entirely different hacking mode distributions. The taxonomy should be extended or the cross-logic characterization claim should be scoped down.
120	
121	**W9. 500 training steps may be insufficient (Experimental, Moderate).**
122	Both ISR/PR curves are still declining at step 500. It is unknown whether STA's benefit persists, grows, or vanishes at longer horizons. The paper should either show convergence or explicitly bound the claim to the observed training horizon.
123	
124	### Minor
125	
126	**W10. 5-step protocol is standard engineering (Novelty, Minor).**
127	"Run a pilot, observe failures, categorize, design mitigations" is standard engineering methodology. Presenting this as a core contribution overstates its novelty, though it has value for reproducibility.
128	
129	**W11. Curriculum scheduling analysis is shallow (Experimental, Minor).**
130	The sigmoid curriculum is the best-performing configuration but its hyperparameters are not ablated. Whether sigmoid outperforms linear ramp is unknown.
131	
132	**W12. ISR sensitivity to decomposition granularity unaddressed (Method, Minor).**
133	The protocol does not guide practitioners on choosing the ablation unit. Discriminability varies 2× across logic types (0.38 vs 0.17), likely reflecting decomposition granularity differences, but no guidance is provided.
134	
135	---
136	
137	## 6. Questions for Authors
138	
139	1. **ISR/PR discrepancy**: Can you precisely specify how training-time ISR computation differs from held-out evaluation ISR? Why does the exec-only condition show stability (0.34→0.31) while exec+STA shows a large gap (0.42→0.78)?
140	
141	2. **Random baseline**: Have you evaluated whether a random structural penalty (e.g., penalizing proved outputs by a random score) achieves comparable ISR/PR improvement? This would isolate ISR's specific signal from the general multi-objective regularization effect.
142	
143	3. **Downstream validation**: Do high-ISR formalizations correlate with better downstream logical inference performance? Have you evaluated the generated FOL formulas on a downstream reasoning task?
144	
145	4. **ISR and feature attribution**: ISR is structurally equivalent to binary LOO feature importance. How does it relate to Shapley values or SHAP? Have you considered interaction effects (components that are individually necessary but collectively encode trivial reasoning)?
146	
147	5. **RIP beyond Propagation**: Could Reachability (does the solver process the component?) and Infection (does removing it change intermediate solver state?) provide additional signals? If not, why invoke the full RIP framework?
148	
149	6. **Training horizon**: Do you have any data beyond 500 steps? Does the ISR/PR gap between conditions converge, diverge, or remain stable?
150	
151	---
152	
153	## 7. Experiment Coverage Assessment
154	
155	All 12 imagined experiments from the review context are covered in the paper:
156	- plan_001 (FOL exec-only baseline) ✓ Table 1
157	- plan_002 (FOL exec+STA) ✓ Table 2
158	- plan_003 (FOL held-out evaluation) ✓ Table 3
159	- plan_004 (O(1) vs O(N) ablation) ✓ Table 4
160	- plan_005 (reward weight ablation + curriculum) ✓ Table 5
161	- plan_006 (Prolog single-logic) ✓ Table 6
162	- plan_007 (Multi-logic GRPO) ✓ Table 8
163	- plan_008 (Cross-logic transfer) ✓ Table 7
164	- plan_009 (SFT baseline) ✓ Table 3
165	- plan_010 (SMT-LIB single-logic) ✓ Table 6
166	- plan_011 (Qwen3-8B scaling) ✓ Table 9
167	- plan_012 (Hacking characterization) ✓ Table 10
168	
169	Coverage is complete. The concern is not coverage but depth: only plans 001-002 have multi-seed support; the remaining 10 experiments are single-seed.
170	
171	---
172	
173	## 8. Scores
174	
175	| Criterion | R1 | R2 | Consensus |
176	|-----------|----|----|-----------|
177	| Overall | 4/6 (Weak Accept) | 3/6 (Weak Reject) | **3/6 (Weak Reject)** |
178	| Soundness | 2/4 | 2/4 | **2/4** |
179	| Presentation | 3/4 | 3/4 | **3/4** |
180	| Contribution | 3/4 | 2/4 | **2/4** |
181	| Confidence | 4/5 | 4/5 | **4/5** |
182	
183	**Consensus Overall: 3/6 (Weak Reject)**
184	
185	---
186	
187	## 9. Meta-Review and Recommendation
188	
189	This paper identifies a genuine problem (structural degeneracy in execution-only GRPO for formal reasoning) and proposes a reasonable solution (component ablation as structural reward). The honest "monitoring/diagnostic tool" framing is well-calibrated to the evidence, and the hacking taxonomy with adversarial adaptation is a genuine empirical insight.
190	
191	However, the paper has significant weaknesses that place it below the acceptance threshold for a top ML venue main track:
192	
193	1. **Novelty concerns dominate.** ISR is LOO ablation importance applied to a new domain — useful application but not a conceptual advance. The RIP framework invocation is cosmetic. The 5-step protocol is standard engineering. The related work is critically thin.
194	
195	2. **Experimental evidence is insufficiently rigorous.** Single-seed secondary experiments cannot support cross-logic generalization claims. The ISR/PR training-vs-held-out discrepancy is unexplained. No downstream validation breaks the ISR circularity. No random baseline isolates ISR's specific contribution.
196	
197	3. **Framing issues.** The "dense + automatic" ORM-PRM positioning is misleading given ISR's sparsity for unproved outputs. The RIP grounding claim overstates the theoretical contribution.
198	
199	**Recommendation**: Reject for top venue main track. The paper has a clear path to acceptance at EMNLP Findings or a workshop after:
200	- Expanding related work to 25+ references (reward shaping, feature attribution, modern formal reasoning, reward hacking mitigation)
201	- Honestly repositioning ISR as domain-specific application of LOO ablation
202	- Adding multi-seed support for at least Prolog and scaling experiments
203	- Providing downstream validation or a random baseline to address circularity
204	- Explaining or resolving the ISR/PR training-vs-held-out discrepancy
205	- Acknowledging ISR's conditional density limitation
206	
207	The strongest version of this paper would: (a) lead with the hacking taxonomy and adversarial adaptation as the primary contribution, (b) position STA/ISR as the tool that enabled the discovery rather than the contribution itself, and (c) use the O(1) negative result and cross-logic instantiation as supporting evidence for the importance of comprehensive structural analysis.
208	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ebd968a-056c-43d2-907c-00531898c36a",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "522d9c5a-715c-4259-a4d2-616167bfbcc0",
  "sourceToolAssistantUUID": "2ebd968a-056c-43d2-907c-00531898c36a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-13T22:43:49.586Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Sr5DPmmYwckYvs4NJwApRh`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "522d9c5a-715c-4259-a4d2-616167bfbcc0",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1NpQ2b8qBN9WwW85t3B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "889f8497-b658-4097-8309-674e23f7800d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WM3ogmRD3S5RQPwoM59vxu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11091,
      "cache_read_input_tokens": 81193,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11091
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 81193,
          "cache_creation_input_tokens": 11091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11091,
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

_source line 59 · 2026-05-13T22:43:49.597Z_

<details><summary>↩ Tool result · `toolu_01Sr5DPmmYwckYvs4NJwApRh`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "889f8497-b658-4097-8309-674e23f7800d",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "a22073527386a7c5b",
  "type": "user",
  "uuid": "c5bfe574-4380-4402-afe3-887f341c6d7c",
  "sourceToolAssistantUUID": "889f8497-b658-4097-8309-674e23f7800d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-13T22:45:06.258Z_

Now I have a thorough understanding of the project. The user's paper summary describes a **negative result** framing -- this aligns with the user-provided summary numbers (prove rate drops from 0.24 to 0.11 with STA). This is distinct from both the "best" dream (where STA succeeds as Pareto-improving) and the "median" dream (where STA partially works as diagnostic). The user's summary represents the actual experimental reality based on the memory.md and decisions.yaml, not the imagined dream papers. Let me now produce the review.

## R1 Review: Methods & Experiments

### Summary

The paper proposes Solver Trace Ablation (STA), adapting mutation testing's RIP framework to derive structural rewards (ISR) for GRPO-trained formal logic generators. The core finding is a principled negative result: STA-derived ISR effectively diagnoses structural degeneracy (~70% sensitivity) but fails as a training reward, reducing prove rate from 0.24 to 0.11 without improving structural quality. The experimental program covers 9 of 12 planned experiments across FOL, Prolog, SFT baselines, and manual hacking characterization.

### Strengths

- **Well-motivated problem formulation.** The paper identifies a genuine and underappreciated failure mode: execution-only GRPO rewards produce structurally degenerate formalizations (ISR/PR ratio dropping from 0.82 to 0.29 over training). This is documented with clean training dynamics in the exec-only baseline.

- **Honest negative result with diagnostic value.** The paper does not overclaim. Reporting that STA fails as a training reward but works as a diagnostic tool is scientifically valuable. The exec+STA condition's prove rate collapse (0.13 vs 0.28 exec-only) is presented straightforwardly, not hidden.

- **Informative O(1) vs O(N) ablation.** The finding that O(1) tautology-only checks have near-zero discriminability (0.02 vs 0.31 for full STA) is a well-designed negative result that justifies the O(N) computational cost and demonstrates that reward hacking is multi-modal.

- **Systematic hacking taxonomy.** The 200-sample annotation with four identified hacking modes (tautology injection 28%, vacuous quantification 19%, premise redundancy 14%, trivial conclusion 8%), inter-annotator kappa of 0.72, and ISR sensitivity of ~70% grounds the quantitative metrics in qualitative understanding.

- **Comprehensive weight ablation.** Six configurations across alpha/beta ratios and fixed/sigmoid schedules demonstrate that no stable operating point exists -- a clean negative result. This is the evidence that makes the "STA fails as reward" conclusion convincing rather than a consequence of poor hyperparameter choice.

- **SFT baseline provides useful calibration.** SFT on 500 gold translations (PR=0.30, ISR/PR=0.50, hack%=50%) dominates GRPO on all metrics, raising the important question of whether GRPO itself is the right paradigm for this task/scale.

### Weaknesses

- **(Major) Three seeds is borderline for the primary comparison, and one seed for ablations is insufficient.** The core exec-only vs exec+STA comparison uses 3 seeds, which is the minimum for computing a standard deviation but insufficient for significance testing. More critically, all ablation experiments (weight ablation, O(1) vs O(N), Prolog, cross-logic transfer) use a single seed. The weight ablation's conclusion that "no stable operating point exists" could be an artifact of initialization: a single configuration might succeed under a different seed. At minimum, the top-2 weight configurations should be verified with 3 seeds to distinguish the negative result from bad luck.

- **(Major) Causal attribution of ISR/PR decline is unresolved.** The paper's central diagnostic claim -- that STA detects reward hacking -- faces a confound identified in the project's own decision log (D005/D006): the ISR/PR decline under exec+STA may be a punitive artifact of the 50/50 weighting (ISR absolute values remain ~0.05, near pretrained baseline) rather than genuine hacking detection. The planned disambiguation experiment (plan_003: evaluating exec-only checkpoints with full STA) was designed to resolve this but the paper summary does not clearly state whether this causal question was answered. If exec-only trained models also show low ISR on held-out, the "detection" claim is undermined -- it would mean GRPO itself produces low-ISR outputs regardless of STA in the reward.

- **(Major) ISR circularity: optimizing and evaluating on the same metric.** The paper uses ISR both as a training reward and as the primary evaluation metric. When ISR is in the reward, ISR improvement during training is tautological. The hacking taxonomy (200 samples, kappa=0.72) partially breaks this circularity but is not dispositive -- there is no downstream task evaluation (e.g., does higher ISR correlate with better logical inference accuracy on an independent benchmark?). Without this, the paper cannot distinguish "ISR captures structural quality" from "ISR captures its own optimization target."

- **(Major) Model and data scale are very limited.** Qwen2.5-1.5B on FOLIO is a small model on a small dataset. FOLIO has ~1204 examples (500 used for training). The Prolog instantiation failed catastrophically (65% solver timeout, prove rate 0.03, training terminated at ~300 steps). This leaves the paper with essentially one functioning logic type (FOL) and one model size, making the "general, solver-agnostic" claim unsupported empirically.

- **(Moderate) Three planned experiments were not run (plan_007 multi-logic GRPO, plan_010 SMT-LIB, plan_011 Qwen3-8B scaling).** Plan_007 was blocked by plan_006's Prolog failure, which is reasonable. However, plans 010 and 011 were "deprioritized" without clear justification. The absence of scaling analysis (plan_011) means the paper cannot distinguish whether the negative result is specific to 1.5B-scale models, and the absence of SMT-LIB (plan_010) weakens the multi-logic generality claim.

- **(Moderate) The combined reward formulation (Eq. 2) creates a fundamental accuracy-structure tradeoff that may explain the negative result mechanistically rather than revealing something about STA.** With r = alpha * r_exec + beta * r_exec * ISR, proved-but-low-ISR outputs receive reward approximately alpha * 1 + beta * 0 = alpha, which is 0.5 in the default configuration. This means structurally weak proved outputs get half the reward of structurally strong ones, but also half the reward of what they would get under exec-only. The model may simply learn that proving is not worth the effort when half the reward is withheld. This is a reward engineering problem, not evidence that structural rewards are fundamentally incompatible with RL training.

### Questions for Authors

1. Was plan_003 (held-out evaluation of exec-only checkpoints using full STA) completed? If so, what was the ISR/PR ratio for exec-only-trained models evaluated with full STA on held-out data? This is the critical disambiguation between "STA detects hacking" and "STA punishment suppresses proving."

2. The held-out results show base model ISR/PR=0.53 > exec+STA 0.30 > exec-only 0.26. But the base model computes ISR/PR over only its 12% proved outputs (a self-selected easy population), while trained models prove different (harder?) problems. Have you controlled for population composition effects (Simpson's paradox)?

3. Have you tried reward formulations that do not penalize proved outputs -- e.g., r = r_exec + bonus * ISR (additive bonus rather than multiplicative weighting)? The multiplicative coupling in Eq. 2 necessarily reduces reward for proved-but-low-ISR outputs below exec-only levels. An additive bonus would only provide upside for structural quality without reducing the incentive to prove.

4. Who performed the hacking taxonomy annotation? If the authors, the kappa=0.72 may be inflated by shared mental models. Were annotation guidelines developed independently of ISR scores?

5. Cross-logic transfer shows mean delta = -0.015 (negative). How do you reconcile this with the claim that STA provides "general" structural rewards? Is the negative transfer an artifact of logic-type specialization induced by GRPO?

### Detailed Comments

**On the RIP framework adaptation.** The RIP (Reachability-Infection-Propagation) grounding is theoretically appealing but operationally thin. STA's ablation test measures only Propagation -- whether removing a component changes the solver output. Reachability (does the solver process the component?) and Infection (does removal change intermediate state?) are neither measured nor used as independent signals. The paper would be more honest to frame STA as "component necessity testing via leave-one-out ablation" and acknowledge the connection to well-known feature importance methods (Shapley values, LOO importance, permutation importance). The RIP terminology adds gravitas but no operational content beyond Propagation.

**On the negative result's interpretation.** The paper's most important finding is that ISR-augmented rewards fail to produce models that are both accurate and structurally sound. However, the interpretation is ambiguous. There are at least three possible explanations: (a) structural rewards fundamentally conflict with execution rewards in GRPO's optimization landscape; (b) the specific reward formulation (multiplicative coupling with 50/50 weighting) is too punitive; (c) at 1.5B scale with 500 steps, the model lacks capacity to satisfy both objectives simultaneously. The weight ablation partially addresses (b) by showing no stable operating point across 6 configurations, but a single seed per configuration is insufficient to rule out seed-specific failures. And (c) cannot be evaluated because plan_011 (8B scaling) was not run.

**On the SFT comparison.** The SFT result (PR=0.30, ISR/PR=0.50, hack%=50%) is arguably the paper's most provocative finding: SFT dominates GRPO exec+STA on every metric. This raises the question of whether GRPO with structural rewards is the right approach at all, or whether SFT followed by GRPO with ISR-based early stopping would be more effective. The paper does not discuss this natural follow-up.

**On reproducibility.** The training script is available (train_grpo.py) with GRPO configs, and the use of Qwen2.5-1.5B, FOLIO, and Prover9 is reproducible. However, the STA reward computation relies on src/solvers/factory.py and src/sta/reward.py which are referenced but their full implementations are not visible in the artifacts. The Prover9 compilation from LADR source adds a reproducibility barrier. Key hyperparameters (K=8, 500 steps, lr=1e-6, batch_size=4, gradient_accumulation=2, max_completion_length=512) are documented.

### Scores
- Soundness: 2/4
- Empirical Rigor: 2/4
- Reproducibility: 3/4
- Overall recommendation: 3/6 (Weak Reject)
- Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5bfe574-4380-4402-afe3-887f341c6d7c",
  "isSidechain": true,
  "agentId": "a22073527386a7c5b",
  "requestId": "req_011Cb1Nq3EiFtGWnuHHTsWbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be98b576-be9e-4b02-bac2-79b02cf532bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHaZ4thR3vxaBGWB8idMbK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5620,
      "cache_read_input_tokens": 92284,
      "output_tokens": 2711,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2711,
          "cache_read_input_tokens": 92284,
          "cache_creation_input_tokens": 5620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5620,
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
