# Research conversation: You are Reviewer 1 (R1) for an ACL ARR submission. Your focus is **Methods and Experiments**. ## Paper Summary Title: "C

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac3a661244be2fc26.jsonl`
- **Structured JSON:** [`a663d4c33e89e34c93dd.json`](../../sessions/a6/a663d4c33e89e34c93dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-22T03:12:06.260Z_

You are Reviewer 1 (R1) for an ACL ARR submission. Your focus is **Methods and Experiments**. 

## Paper Summary
Title: "Cross-Lingual Conflict Detection in Multilingual LLMs: Mechanistic Evidence for English-Anchored Representations"

This paper investigates how cross-lingual knowledge conflict signals are encoded in the residual stream of multilingual transformers. It uses three analysis tracks:
- Track 1: Linear and MLP probing on residual stream activations across 3 models (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) and 2 language pairs (EN↔ZH, EN↔JA)
- Track 2: SAE (Sparse Autoencoder) feature analysis using Qwen-Scope on Qwen3-8B-Base
- Track 3: Causal intervention via probe-based and SAE-based representation steering

Key findings:
1. Linear probes detect conflict signals at 70-77% balanced accuracy (within-language), 64-73% (cross-lingual), all permutation test p<0.001
2. Directional asymmetry: X→EN outperforms EN→X by 6.3-7.9pp across all 4 model×lang-pair combos (3/4 statistically significant at 95% CI, 4/4 directionally consistent)
3. SAE finds 18 cross-lingually shared conflict features (mid-layer Jaccard=0.28, late-layer=0.12, p=0.008)
4. Steering flip rates: monolingual EN 31.2%, cross-lingual ZH→EN 24.3%, EN→ZH 17.8%, all 3.4-6.5x above random baseline (~5%)
5. Feature-set ablation: shared features alone achieve 28% flip rate vs language-specific 9-11%

Additional robustness:
- COMET tercile ablation rules out translation quality confound
- Label noise ablation: graceful degradation ~2.6pp per 5% noise
- Larger dataset (N=2200) narrows Qwen CI from [-1.2, 13.4] to [1.8, 12.3], achieving significance
- CKA/SVCCA shows mid-layer similarity ~0.82 dropping to ~0.54 in late layers
- PCA visualization: mid-layer cross-lingual overlap (cosine=0.78), late-layer divergence (cosine=0.51)

## Experiment Design Reference (from review_context.yaml)
The full imagined experiment list includes:
1. COMET translation quality verification (mvp_003) — included in paper ✓
2. Third model architecture (Gemma-2-9B-IT, plan_102) — included ✓
3. Multilingual extension EN↔JA (plan_103) — included ✓
4. Layer-wise CKA/SVCCA (plan_104) — included ✓
5. Probe weight PCA visualization (plan_109) — included ✓
6. Label noise ablation (plan_106) — included ✓
7. Representation steering (plan_107) — included ✓
8. Larger dataset validation (plan_108) — included ✓
9. Qwen-Scope SAE conflict feature identification (plan_201) — included ✓
10. LangFIR language feature deconfounding (plan_202) — included ✓
11. Cross-lingual feature Jaccard analysis (plan_203) — included ✓
12. Monolingual→cross-lingual steering transfer (plan_301) — included ✓
13. Cross-lingual-specific steering (plan_302) — included ✓
14. Typological steering correlation (plan_303) — included ✓ (but only 2 language pairs)

All 14 experiments appear to be covered in the paper.

## Your Task
Evaluate the paper's **methodology and experimental design** rigorously. Address:

1. **Methodological Soundness**
   - Is the probing methodology (logistic regression, 5-fold CV, balanced accuracy) appropriate?
   - Is the bootstrap CI approach (n=100) for asymmetry gap sound? Is n=100 sufficient?
   - Are permutation tests (n=1000) appropriate for significance testing?
   - Is the MLP probe design (single hidden layer, 256 units) well-justified?
   - Are the SAE methods (mutual information screening, Jaccard analysis, LangFIR) sound?
   - Is the steering methodology (adding α·v to residual stream) well-controlled?

2. **Experimental Coverage and Controls**
   - Are all necessary controls present (random baselines, confound checks)?
   - Is the COMET tercile ablation sufficient to rule out translation quality?
   - Is the label noise ablation informative?
   - Does the larger dataset validation adequately address the Qwen power issue?

3. **Statistical Rigor**
   - Qwen EN↔ZH asymmetry: CI includes zero at N=1000 but excludes zero at N=2200. Is this pattern concerning or expected?
   - 3/4 significant, 4/4 directionally consistent — is this framing appropriate?
   - Bootstrap n=100 — is this enough for reliable 95% CIs?
   - The Jaccard permutation test p=0.008 — how robust is this given the small feature counts?

4. **Potential Weaknesses**
   - SAE analysis only on Qwen3-8B-Base (not on Llama or Gemma) — is this a significant limitation?
   - SAE on base model vs probing on instruct-tuned models — how problematic is this mismatch?
   - Probe accuracy 70-77% — what does this mean for the strength of claims?
   - Steering flip rates 17-35% — what fraction of the mechanism is captured?
   - Only dense transformers tested (no MoE) — how limiting?
   - Only 2 Asian language pairs — no European languages tested

5. **Missing Experiments or Analyses**
   - Anything that should have been included but wasn't?
   - Any ablations that would strengthen the claims?

## Scoring (ACL ARR 1-5 scale)
Provide preliminary scores:
- **Soundness** (1-5): 5=most thorough given type, 4=sufficient support for all claims, 3=sufficient for main claims, 2=important issues, 1=fundamental flaws
- **Overall Assessment** (1-5): 5=strong accept, 4=accept, 3.5=borderline accept, 3=borderline, 2.5=borderline reject, 2=reject

Format your review as a structured reviewer report with sections: Summary, Strengths, Weaknesses, Questions for Authors, Minor Issues, Preliminary Scores.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "add3ddb0-b9f5-4a88-b227-398f223b7037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T03:12:06.266Z_

```json
{
  "parentUuid": "add3ddb0-b9f5-4a88-b227-398f223b7037",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
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
  "uuid": "9e21199e-49bf-4cc1-bee9-5368b4877e5a",
  "timestamp": "2026-05-22T03:12:06.266Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-22T03:12:09.484Z_



I'll start by reading the paper and relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e21199e-49bf-4cc1-bee9-5368b4877e5a",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGskv2hnAYL5LPUfmyKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f4e0eb4-63df-4279-a1a9-2e97ab829081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wk9niGBQhoc4yUF2rHvea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15831,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15831,
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

_source line 4 · 2026-05-22T03:12:09.962Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Aqhk3Q3p95XeEs6B9rdCo2`</summary>

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
  "parentUuid": "0f4e0eb4-63df-4279-a1a9-2e97ab829081",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGskv2hnAYL5LPUfmyKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c27875c4-1922-4f08-9af1-bd92e46fa52c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wk9niGBQhoc4yUF2rHvea",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15831,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15831
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15831,
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

_source line 5 · 2026-05-22T03:12:09.967Z_

<details><summary>↩ Tool result · `toolu_01Aqhk3Q3p95XeEs6B9rdCo2`</summary>

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
  "parentUuid": "c27875c4-1922-4f08-9af1-bd92e46fa52c",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "f076ba46-1740-4de4-85fc-21ae1d0e2008",
  "sourceToolAssistantUUID": "c27875c4-1922-4f08-9af1-bd92e46fa52c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-22T03:12:12.932Z_



Let me read the paper and key project files to conduct a thorough methods/experiments review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f076ba46-1740-4de4-85fc-21ae1d0e2008",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmC6qVxPpqgL2FQjLg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a63a21e-1969-4e1b-b8fa-0a9769d8fecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QMoaqjgibHc4QSYhX4vTnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15831,
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

_source line 7 · 2026-05-22T03:12:13.948Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Nzb3YSLshV8hgwiGizdJAW`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a63a21e-1969-4e1b-b8fa-0a9769d8fecf",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmC6qVxPpqgL2FQjLg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ae50ccd-03be-46f6-93be-6e17174ca052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QMoaqjgibHc4QSYhX4vTnZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15831,
      "output_tokens": 188,
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
          "output_tokens": 188,
          "cache_read_input_tokens": 15831,
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

### Tool call

_source line 8 · 2026-05-22T03:12:13.956Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01GEbPwf5Tju69EGwpbtKmog`</summary>

```json
{
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ae50ccd-03be-46f6-93be-6e17174ca052",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmC6qVxPpqgL2FQjLg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bd4ceff-707d-4b38-a86d-bc1ac794bfb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QMoaqjgibHc4QSYhX4vTnZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15831,
      "output_tokens": 188,
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
          "output_tokens": 188,
          "cache_read_input_tokens": 15831,
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

_source line 9 · 2026-05-22T03:12:13.979Z_

<details><summary>↩ Tool result · `toolu_01Nzb3YSLshV8hgwiGizdJAW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| comet_llama_v5 | — | — | — | — |\\n| comet_qwen_v5 | — | — | — | — |\\n| comet_llama_v6 | COMET back-translation 质量验证 Llama ZH 翻译（v6: 跟踪 nohup 进程，v5 被 tmux 监控误标 failed） | — | — | — |\\n\\n## 待处理\\n- comet_llama_v4（准备中）\\n- comet_llama_v3（准备中）\\n- comet_llama_v2（准备中）\\n- comet_llama（准备中）\\n- comet_qwen_v4（准备中）\\n- comet_qwen_v3（准备中）\\n- comet_qwen_v2（准备中）\\n- comet_qwen（准备中）\\n- qwen_zh_act_v2: 用 v2 re-verified 数据（966条，enable_thinking=False）重采 Qwen3-8B ZH 激活，替换 v1 污染数据（1116条）（准备中）\\n- probe_qwen_full（准备中）\\n- …另有 13 项\\n\\n## 近期结论\\n- **mvp_probe_v1** (success): 跨语言知识冲突信号可在 Qwen3-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现有意义的跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）\\n  [bootstrap_asymmetry_corrected_qwen](/api/workspace-files/projects/clkc_mech_interp/artifacts/mvp_probe_v1/data/bootstrap_qwen.json)\\n- **mvp_probe_llama_v1** (success): 跨语言知识冲突信号可在 Llama-3.1-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）——与 Qwen3-8B 形成跨模型验证 ← 基于 mvp_probe_v1\\n  [bootstrap_asymmetry_corrected_llama](/api/workspace-files/projects/clkc_mech_interp/artifacts/mvp_probe_llama_v1/data/bootstrap_llama.json)\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-41302: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1352, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ae50ccd-03be-46f6-93be-6e17174ca052",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "f460d1e1-5cde-4d57-9edf-c45ad04aff97",
  "sourceToolAssistantUUID": "1ae50ccd-03be-46f6-93be-6e17174ca052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T03:12:14.062Z_

<details><summary>↩ Tool result · `toolu_01GEbPwf5Tju69EGwpbtKmog`</summary>

```text
{"result":"# 项目 clkc_mech_interp 概况\n\n## 实验状态 (29 个)\n\n- **qwen_zh_act_v2**: PREPARING — \n- **probe_qwen_full**: PREPARING — \n- **translate_zh_qwen_v2**: PREPARING — \n- **qwen_zh_act**: PREPARING — \n- **llama_zh_act**: PREPARING — \n- **qwen_en_act_v3**: PREPARING — \n- **verify_qwen3_v2**: PREPARING — \n- **collect_en_act_qwen_v2**: PREPARING — \n- **collect_en_act_llama_v3**: PREPARING — \n- **translate_zh_qwen**: PREPARING — \n- **translate_zh_llama_v2**: PREPARING — \n- **collect_en_activations_llama_v2**: PREPARING — \n- **collect_en_activations_qwen3_8b**: PREPARING — \n- **qwen3_translate_zh**: PREPARING — \n- **llama31_en_activations**: PREPARING — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| comet_llama_v5 | — | — | — | — |\n| comet_qwen_v5 | — | — | — | — |\n| comet_llama_v6 | COMET back-translation 质量验证 Llama ZH 翻译（v6: 跟踪 nohup 进程，v5 被 tmux 监控误标 failed） | — | — | — |\n\n## 待处理\n- comet_llama_v4（准备中）\n- comet_llama_v3（准备中）\n- comet_llama_v2（准备中）\n- comet_llama（准备中）\n- comet_qwen_v4（准备中）\n- comet_qwen_v3（准备中）\n- comet_qwen_v2（准备中）\n- comet_qwen（准备中）\n- qwen_zh_act_v2: 用 v2 re-verified 数据（966条，enable_thinking=False）重采 Qwen3-8B ZH 激活，替换 v1 污染数据（1116条）（准备中）\n- probe_qwen_full（准备中）\n- …另有 13 项\n\n## 近期结论\n- **mvp_probe_v1** (success): 跨语言知识冲突信号可在 Qwen3-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现有意义的跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）\n  [bootstrap_asymmetry_corrected_qwen](/api/workspace-files/projects/clkc_mech_interp/artifacts/mvp_probe_v1/data/bootstrap_qwen.json)\n- **mvp_probe_llama_v1** (success): 跨语言知识冲突信号可在 Llama-3.1-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）——与 Qwen3-8B 形成跨模型验证 ← 基于 mvp_probe_v1\n  [bootstrap_asymmetry_corrected_llama](/api/workspace-files/projects/clkc_mech_interp/artifacts/mvp_probe_llama_v1/data/bootstrap_llama.json)\n\n## 趋势\n成功 2 / 负向 0 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-41302: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bd4ceff-707d-4b38-a86d-bc1ac794bfb2",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "a2bba803-4501-4a3a-90f4-49a32acb19af",
  "sourceToolAssistantUUID": "2bd4ceff-707d-4b38-a86d-bc1ac794bfb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T03:12:17.169Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01E54Dpt8BYKxiJNgaHtDSZq`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2bba803-4501-4a3a-90f4-49a32acb19af",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmVLRZh6buJRwDuNQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1823b3f1-bcd8-4087-9ed0-541b744fd860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR1MaW69FFvLWdMVRh3oqV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 17278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2442,
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

_source line 12 · 2026-05-22T03:12:17.181Z_

<details><summary>↩ Tool result · `toolu_01E54Dpt8BYKxiJNgaHtDSZq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-21 12:00 UTC\\n  summary: MVP 方案：EN+ZH 双语探针迁移实验验证跨语言冲突信号可检测性\\n  rationale: Track 1（探针迁移）是整个 3-track 研究的基础前提。如果残差流中无法检测冲突信号或跨语言完全不迁移，后续 SAE 分析和 steering\\n    均无意义。选 Qwen3-8B-Instruct 因 Qwen-Scope 提供 base SAE 便于后续 Track 2。选 EN+ZH 因语系距离大，若迁移成功则信号强。ConflictQA\\n    公开可用，无需等 CLEAR 数据。Pass/fail 标准参考 Brink et al. 单语 0.96 F1 和 Zhao et al. ~90% 探针精度。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-21 12:06 UTC\\n  summary: 采纳 Reviewer 5 条 warning，细化 MVP gate：增加 70-79% conditional pass 定义、layer-wise\\n    量化标准、统计显著性要求（binomial p<0.01）、翻译 COMET gate（≥0.80）、FAIL→retry Llama 行动路径\\n  rationale: Reviewer 指出原 gate criteria 存在 ambiguous zone（70-79% 无定义）、layer-wise pattern\\n    逃逸条款过于模糊、ZH 60% 阈值缺统计锚定、翻译质量是迁移失败的混淆因素、FAIL 后行动未定义。全部采纳以确保 MVP 结论可靠。FAIL→retry\\n    on Llama 给予一次排除模型特异性的机会，两模型均 FAIL 才 kill。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-21 14:26 UTC\\n  summary: 补采样至 2000 条 + 取消强制交集，每个模型用各自 verified 数据集\\n  rationale: Llama verify 保留率仅 33%（266/800 train），低于 300 阈值。ConflictQA 有 ~10K 条，扩至\\n    2000 可保证两模型各自 ≥300 有效样本。取消交集策略因为强制交集会进一步损失样本量，且跨模型对比不要求相同样本——各自 verified 集上报告相同指标即可，交集作为补充分析。20%\\n    标签翻转率确认了 M001 verify 步骤的必要性。\\n  related_experiments:\\n  - exp_id: mvp_probe_llama_v1\\n    role: triggered_decision\\n    result: verify 保留率 33%, 266 train / 70 test, 20% flip\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-21 19:17 UTC\\n  summary: Llama MVP CONDITIONAL PASS → EXTEND：EN→EN 77.6%, 跨语言迁移不对称（ZH→EN 71.3% vs\\n    EN→ZH 59.6%），等 Qwen 结果做最终 verdict\\n  rationale: Llama 4 方向探针结果显示冲突信号可线性检测（所有方向 p < 0.01），但 EN→EN 未达 80% PASS 阈值（77.6%）。跨语言迁移存在但高度不对称：ZH→EN\\n    强迁移（71.3%），EN→ZH 弱迁移（59.6%，刚好低于 60% point 阈值但 p=9.7e-4 仍显著）。CONDITIONAL PASS 按\\n    D002 规则进入 EXTEND 评估。等 Qwen 跨模型验证后做最终 MVP verdict。不对称迁移本身是有价值的科学发现。\\n  related_experiments:\\n  - exp_id: mvp_probe_llama_v1\\n    role: primary\\n    result: EN→EN 77.6% L28, ZH→ZH 72.1% L13, EN→ZH 59.6% L5, ZH→EN 71.3% L15\\n  depends_on:\\n  - D002\\n- id: D005\\n  date: 2026-05-21 20:33 UTC\\n  summary: 双模型 MVP CONDITIONAL PASS：Llama EN→EN 77.6% + Qwen EN→EN 75.0%，跨语言迁移不对称且跨架构一致（ZH→EN\\n    >> EN→ZH），等 COMET 验证后进入 research 阶段\\n  rationale: 两个模型全 4 方向探针结果统计高度显著（permutation p < 0.001）。核心发现：(1) 冲突信号在两模型两语言中均可线性检测；(2)\\n    跨语言迁移存在方向性不对称（ZH→EN 71-73% vs EN→ZH 60-67%），两模型一致；(3) 不对称程度与架构相关——Qwen（多语言训练比例更高）EN→ZH\\n    67.3% 远强于 Llama 59.6%。EN→EN 均在 70-79% CONDITIONAL 区间，未达 80% PASS，但跨语言迁移的质量和不对称发现的科学价值足以支撑继续研究。COMET\\n    翻译质量验证是最后一个前置条件。\\n  related_experiments:\\n  - exp_id: mvp_probe_llama_v1\\n    role: primary\\n    result: EN→EN 77.6%, ZH→ZH 72.1%, EN→ZH 59.6%, ZH→EN 71.3%\\n  - exp_id: mvp_probe_v1\\n    role: primary\\n    result: EN→EN 75.0%, ZH→ZH 72.6%, EN→ZH 67.3%, ZH→EN 73.2% (v2 clean labels)\\n  depends_on:\\n  - D002\\n  - D004\\n- id: D006\\n  date: 2026-05-22 02:13 UTC\\n  summary: COMET 0.80 阈值不直接适用 back-translation：提升 plan_105 至 P0，用 ablation 实证判断翻译质量是否影响探针结果\\n  rationale: Qwen test COMET mean=0.70, pass rate 18.45% (31/168 at ≥0.80)。但 0.80\\n    阈值是为正向翻译设定的，back-translation 引入二次噪声（EN→ZH→EN），COMET 天然偏低。降低阈值是 ad hoc 的；正确做法是用\\n    plan_105 COMET 分段 ablation 实证检验：按 COMET tertile 分组比较 probe acc，如果组间无显著差异 → 翻译质量非\\n    confounder → 放宽阈值有据可依；如果组间差异显著 → 需过滤低 COMET 样本重跑探针。\\n  related_experiments:\\n  - exp_id: comet_qwen_v5\\n    role: evidence\\n    result: Qwen test COMET mean=0.70, pass 18.45%\\n  - exp_id: mvp_probe_v1\\n    role: dependent\\n    result: 探针结果可能受翻译质量影响\\n  depends_on:\\n  - D005\\n\", \"total_chars\": 3400, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1823b3f1-bcd8-4087-9ed0-541b744fd860",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "ec2fbeb1-0e44-4735-9600-1b3fe0bc8c7f",
  "sourceToolAssistantUUID": "1823b3f1-bcd8-4087-9ed0-541b744fd860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T03:12:18.065Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SvK1DPKkJYBZg4CNmszWn1`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec2fbeb1-0e44-4735-9600-1b3fe0bc8c7f",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmVLRZh6buJRwDuNQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdbf307e-686e-4e62-9067-4ae4d4b5827c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR1MaW69FFvLWdMVRh3oqV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 17278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2442,
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

_source line 14 · 2026-05-22T03:12:18.077Z_

<details><summary>↩ Tool result · `toolu_01SvK1DPKkJYBZg4CNmszWn1`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'clkc_mech_interp'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdbf307e-686e-4e62-9067-4ae4d4b5827c",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "82fa6985-6a31-4a74-9eaa-b7834b3bed57",
  "sourceToolAssistantUUID": "bdbf307e-686e-4e62-9067-4ae4d4b5827c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T03:12:19.095Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0183xBNqAtJmJEbgNxZZtWXR`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82fa6985-6a31-4a74-9eaa-b7834b3bed57",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmVLRZh6buJRwDuNQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90016d8a-dbb2-4f77-9574-f315b2f5ae3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR1MaW69FFvLWdMVRh3oqV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 17278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2442,
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

_source line 16 · 2026-05-22T03:12:19.107Z_

<details><summary>↩ Tool result · `toolu_0183xBNqAtJmJEbgNxZZtWXR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md\", \"content\": \"# clkc_mech_interp — Research Dashboard\\n\\n> 最后更新: 2026-05-22 02:38 UTC | 更新原因: MVP 通过，进入 Research 阶段，Dream 已提交\\n\\n## 核心方向\\n多语言 LLM 中跨语言知识冲突的机制可解释性研究。核心发现：冲突信号可线性检测，跨语言迁移存在方向性不对称（~7.2pp），跨架构一致。目标 ICLR 2027（DDL 2026-09-24）。详见 paper_framing.md。\\n\\n## 当前阶段：Research（MVP 已通过 ✅）\\n\\nMVP 通过条件：双模型探针验证 + 两个 confounder 排除（token overlap + COMET ablation）。\\n\\n### 双模型 Bootstrap n=100 结果（可引用）\\n\\n| 方向 | Llama-3.1-8B (mean±std) | Qwen3-8B (mean±std) |\\n|------|------------------------|---------------------|\\n| EN→EN | **77.1±1.2%** | **75.3±1.7%** |\\n| ZH→ZH | **71.2±1.3%** | **71.6±1.8%** |\\n| EN→ZH | **64.1±2.5%** | **65.0±2.7%** |\\n| ZH→EN | **71.3±2.7%** | **72.2±2.6%** |\\n\\n不对称性 (corrected): Llama +7.22pp CI [1.1%, 13.6%] sig | Qwen +7.18pp CI [-1.2%, 13.4%] trending\\n\\n### Confounder 排除\\n- **RC1 翻译质量**: plan_105 COMET tercile ablation → delta=-5.64pp (反向), p=0.695, 非 confounder ✅\\n- **RC2 Token overlap**: plan_101 → per-sample Jaccard 3-4%, Llama 负相关 r=-0.15, 非 confounder ✅\\n\\n### 近期任务\\n- [x] ~~complete_mvp()~~ ✅\\n- [ ] dream_simulate(review_mode=\\\"full\\\") — dream_20260522T023801 pending (10-25 min)\\n- [ ] Llama test COMET 完成后跑 Llama 版 tercile ablation（确认一致性）\\n- [ ] COMET train 继续跑（Qwen ~3.8h, Llama ~7h）\\n- [ ] Dream 完成后审阅 → 批准 P0 实验启动\\n\\n### Post-MVP P0 实验（等 Dream 审阅后启动）\\n1. ~~Token overlap (plan_101)~~ ✅\\n2. ~~Bootstrap CI 修正 (plan_099)~~ ✅\\n3. ~~COMET tercile ablation (plan_105)~~ ✅ (Qwen done, Llama pending)\\n4. 第三模型 Gemma-2-9B-IT (plan_102) — 模型已下载, 等 GPU\\n5. 多语言扩展 EN↔JA (plan_103) — planned, ~20 GPU·h\\n6. Layer-wise CKA/SVCCA (plan_104) — planned, ~4 GPU·h\\n7. Representation steering (plan_107) — planned, ~8 GPU·h\\n\\n## GPU 预算\\nwestd-41302: 4× RTX PRO 6000 Blackwell 96GB（cuda:0-3）\\n当前: cuda:0,2 COMET train; cuda:3 COMET Llama test; cuda:1 空闲\\n\\n## 风险\\n1. Llama CI 下界 borderline (1.1pp) — 第三模型 Gemma 结果决定 C2 强度\\n2. 只有 Track 1 时论文贡献可能偏 analysis paper — Dream 审稿将评估\\n3. COMET train 仍需 4-8h 完成\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-22 | COMET 0.80 阈值不直接适用 back-translation：提升 plan_105 至  | comet_qwen_v5, mvp_probe_v1 |\\n| D005 | 2026-05-21 | 双模型 MVP CONDITIONAL PASS：Llama EN→EN 77.6% + Qwen  | mvp_probe_llama_v1, mvp_probe_v1 |\\n| D004 | 2026-05-21 | Llama MVP CONDITIONAL PASS → EXTEND：EN→EN 77.6%, 跨 | mvp_probe_llama_v1 |\\n| D003 | 2026-05-21 | 补采样至 2000 条 + 取消强制交集，每个模型用各自 verified 数据集 | mvp_probe_llama_v1 |\\n| D002 | 2026-05-21 | 采纳 Reviewer 5 条 warning，细化 MVP gate：增加 70-79% cond | — |\\n| D001 | 2026-05-21 | MVP 方案：EN+ZH 双语探针迁移实验验证跨语言冲突信号可检测性 | — |\\n\\n\\n\", \"total_chars\": 2474, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90016d8a-dbb2-4f77-9574-f315b2f5ae3e",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "df5cfc10-581e-4748-9024-b313802f6a54",
  "sourceToolAssistantUUID": "90016d8a-dbb2-4f77-9574-f315b2f5ae3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T03:12:19.389Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018SjNLwqcgeD2XGiM2StwHp`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df5cfc10-581e-4748-9024-b313802f6a54",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmVLRZh6buJRwDuNQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f639eb4-722c-4000-8e83-193fe2f18b5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WR1MaW69FFvLWdMVRh3oqV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 17278,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 394,
          "cache_read_input_tokens": 17278,
          "cache_creation_input_tokens": 2442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2442,
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

_source line 18 · 2026-05-22T03:12:19.403Z_

<details><summary>↩ Tool result · `toolu_018SjNLwqcgeD2XGiM2StwHp`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/memory.md\", \"content\": \"# Gemma-2-9B-IT 兼容性报告 (plan_102)\\n\\n## 模型结构\\n\\n| 属性 | 值 |\\n|------|-----|\\n| model_type | gemma2 |\\n| architecture | Gemma2ForCausalLM |\\n| num_hidden_layers | 42 |\\n| hidden_size | 3584 |\\n| num_attention_heads | 16 |\\n| num_key_value_heads | 8 (GQA) |\\n| head_dim | 256 |\\n| vocab_size | 256000 |\\n| max_position_embeddings | 8192 |\\n| sliding_window | 4096 (alternating layers) |\\n| torch_dtype | bfloat16 |\\n| attn_logit_softcapping | 50.0 |\\n| final_logit_softcapping | 30.0 |\\n\\n## Tokenizer\\n\\n| 属性 | 值 |\\n|------|-----|\\n| padding_side | left |\\n| pad_token | `&lt;pad>` (id=0) |\\n| bos_token | `&lt;bos>` (id=2) |\\n| eos_token | `&lt;eos>` (id=1) |\\n| chat_template | `&lt;bos>&lt;start_of_turn>user\\\\n{content}&lt;end_of_turn>\\\\n&lt;start_of_turn>model\\\\n` |\\n| thinking mode | 无（enable_thinking 参数被 **kwargs 静默接受但无效果） |\\n| system role | 不支持（template 中 raise_exception） |\\n\\n## 各脚本兼容性\\n\\n### verify_parametric_knowledge.py — ✅ 无需修改\\n\\n- `AutoModelForCausalLM.from_pretrained`：通用加载，兼容 ✓\\n- `apply_chat_template(enable_thinking=False)`：Gemma tokenizer 通过 `**kwargs` 静默接受，不报错 ✓\\n- `strip_think_tags()`：Gemma 输出无 `&lt;think>` 标签，函数是 no-op ✓\\n- 生成参数 `do_sample=False, max_new_tokens=128`：通用，兼容 ✓\\n- 运行命令：`python src/verify_parametric_knowledge.py --model /root/autodl-tmp/models/gemma-2-9b-it --data_dir data/ --raw_dir data/ --output_dir data/gemma2/`\\n\\n### collect_activations.py — ✅ 无需修改\\n\\n- `model.model.layers`：Gemma2 结构为 `Gemma2ForCausalLM.model(Gemma2Model).layers[0..41]`，与 Qwen/Llama 同构 ✓\\n- Hook `output[0]`：Gemma2DecoderLayer 返回 tuple，`[0]` 是 hidden_states ✓\\n- `tokenizer.padding_side = \\\"left\\\"`：脚本显式设置，与 Gemma 默认一致 ✓\\n- `tokenizer.pad_token = tokenizer.eos_token`：Gemma 有专用 pad_token（id=0），此 fallback 不触发 ✓\\n- Last-token 提取 `shape[1]-1`：left-padding 下最后位置即最后真实 token ✓\\n- 运行命令：`python src/collect_activations.py --model /root/autodl-tmp/models/gemma-2-9b-it --data_dir data/gemma2 --output_dir outputs/gemma2 --lang en --batch_size 4`\\n\\n### train_probe.py — ✅ 无需修改\\n\\n- 无硬编码维度或模型名\\n- 从 .pt 文件读取 numpy 数组，自动适配任意 hidden_size (3584)\\n- 运行命令：`python src/train_probe.py --en_path outputs/gemma2/en_activations.pt --output_dir outputs/gemma2`\\n\\n## Layer 结构详情\\n\\n```\\nmodel (Gemma2ForCausalLM)\\n├── model (Gemma2Model)\\n│   ├── embed_tokens (Embedding)\\n│   ├── layers (ModuleList) × 42\\n│   │   └── [i] (Gemma2DecoderLayer)\\n│   │       ├── self_attn (Gemma2Attention)\\n│   │       ├── mlp (Gemma2MLP)\\n│   │       ├── input_layernorm (Gemma2RMSNorm)\\n│   │       ├── post_attention_layernorm (Gemma2RMSNorm)\\n│   │       ├── pre_feedforward_layernorm (Gemma2RMSNorm)\\n│   │       └── post_feedforward_layernorm (Gemma2RMSNorm)\\n│   └── norm (Gemma2RMSNorm)\\n└── lm_head (Linear)\\n```\\n\\n注意：Gemma2 比 Llama/Qwen 多了 `pre_feedforward_layernorm` 和 `post_feedforward_layernorm`（pre/post-norm sandwich 结构）。不影响 hook 收集。\\n\\n## GPU 需求估算\\n\\n- 模型加载（bfloat16）：~18GB VRAM\\n- 每样本激活缓存：42 layers × 3584 dim × 4 bytes (float32) ≈ 600KB\\n- 1000 样本总激活：~600MB\\n- 推荐：单卡 24GB+ (A5000/3090/4090) 即可\\n\\n## 与 Qwen3-8B 对比\\n\\n| | Qwen3-8B | Gemma-2-9B |\\n|---|---|---|\\n| layers | 36 | 42 |\\n| hidden_size | 4096 | 3584 |\\n| attention | MHA | GQA (16h/8kv) |\\n| thinking mode | 有 | 无 |\\n| padding_side | left | left |\\n| 专用 pad_token | 无（用 eos） | 有（id=0） |\\n| sliding window | 无 | 4096 (alternating) |\\n\\n## 结论\\n\\n三个核心脚本均无需代码修改即可用于 Gemma-2-9B-IT。只需更改命令行参数中的模型路径和数据目录。\\n\", \"total_chars\": 3231, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f639eb4-722c-4000-8e83-193fe2f18b5f",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "f649edab-b388-4253-a243-766d98a0307a",
  "sourceToolAssistantUUID": "9f639eb4-722c-4000-8e83-193fe2f18b5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T03:12:23.696Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013ynDpWen2wryadpcUUrXL1`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f649edab-b388-4253-a243-766d98a0307a",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmtRjsw9KvyizxLvc5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21a5b530-c784-46e6-93d6-cbb544c787a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVgyskuYYhymx6rrNCSk64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6468,
      "cache_read_input_tokens": 19720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6468,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 20 · 2026-05-22T03:12:23.717Z_

<details><summary>↩ Tool result · `toolu_013ynDpWen2wryadpcUUrXL1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_framing.md\", \"content\": \"# Paper Framing — clkc_mech_interp\\n\\n> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)\\n\\n## Core Insight\\n\\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 \\\"entity-centric factual conflicts 中 linguistic affinity 决定冲突解决\\\" 提供了首个**机制层面的解释**。\\n\\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\\n\\n## Narrative Structure\\n\\n**现象驱动的机制解释**（非 \\\"applying X to Y\\\"）：\\n\\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释\\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？\\n3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预\\n\\n**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界\\n\\n## Competing Hypotheses (pre-registered)\\n\\n**H1 — English-anchored universal detection**:\\n冲突检测信号本身是 language-independent 的（\\\"是否存在冲突\\\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\\n\\n**H2 — Language-pair-specific encoding**:\\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\\n\\n**MVP 证据倾向**:\\n当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。\\n\\n## Core Claims\\n\\n### Claim 1: Cross-lingual conflict detectability\\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\\n**Evidence needed**:\\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\\n- Permutation test p < 0.001 ✅ (all directions)\\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\\n**Status**: MVP 已验证 ✅\\n\\n### Claim 2: Asymmetric cross-lingual transfer\\n**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。\\n**Evidence needed**:\\n- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):\\n  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅\\n  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️\\n- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)\\n- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)\\n- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)\\n**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)\\n\\n### Claim 3: Direction-dependent non-linear components\\n**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。\\n**Evidence needed**:\\n- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)\\n- MLP 不使用 test set 做 early stopping ✅ (已修复)\\n- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)\\n- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)\\n**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)\\n\\n### Claim 4: Layer-wise conflict signal structure\\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\\n**Evidence needed**:\\n- Layer-wise probe accuracy curves for ≥3 models ❌\\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\\n- 与 \\\"Lost in Multilinguality\\\" 的 language transition 层对比 ❌\\n**Status**: 未验证 ❌\\n\\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\\n**Evidence needed**:\\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\\n- LangFIR random-token filtering 控制 ❌\\n- Cross-lingual feature Jaccard 分析 ❌\\n**Status**: 未开始 ❌\\n\\n### Claim 6: Cross-lingual conflict steering (Track 3)\\n**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。\\n**Evidence needed**:\\n- SpARE 框架跨语言扩展 ❌\\n- Monolingual → cross-lingual steering transfer ❌\\n- Steering effectiveness vs linguistic distance correlation ❌\\n**Status**: 未开始 ❌ (依赖 Track 2)\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Translation quality confound [RESOLVED ✅]\\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\\n\\n### RC2: Token overlap confound [RESOLVED ✅]\\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\\n\\n### RC3: Model coverage insufficient [HIGH]\\n**Concern**: 只有 2 个模型，无法声称 \\\"架构无关\\\"\\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\\n**Experiment**: P0 — additional model verification\\n\\n### RC4: Dataset size and diversity [MEDIUM]\\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\\n\\n### RC5: Linear probe expressiveness [LOW]\\n**Concern**: 线性探针可能遗漏复杂非线性信号\\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\\n**Experiment**: Done — MLP vs Linear comparison\\n\\n### RC6: SAE base/instruct mismatch [MEDIUM]\\n**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配\\n**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证\\n**Experiment**: Track 2 设计已考虑\\n\\n### RC7: Steering failure precedent [MEDIUM]\\n**Concern**: \\\"Interpretability without actionability\\\" 证明 SAE steering 可能完全无效\\n**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式\\n**Experiment**: Track 3 包含 negative result framing\\n\\n### RC8: Causal claims without intervention [HIGH]\\n**Concern**: 探针只证明信号可检测，不证明因果关系\\n**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制\\n**Experiment**: Track 3 steering + representation steering (P1)\\n\\n## Paper Structure (Tentative)\\n\\n1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview\\n2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features\\n3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering\\n4. **Experiments & Results**:\\n   - 4.1 Cross-lingual conflict detectability (C1)\\n   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls\\n   - 4.3 Non-linear components (C3) + layer-wise structure (C4)\\n   - 4.4 SAE feature analysis (C5) [if Track 2 ready]\\n   - 4.5 Steering experiments (C6) [if Track 3 ready]\\n5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR\\n6. **Conclusion**\\n\\n## Scope Control\\n\\n**投稿最低要求 (must-have for submission)**:\\n- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)\\n- Claim 4 partially supported (layer-wise analysis on ≥2 models)\\n- ≥3 model architectures\\n- ≥2 language pairs (EN-ZH + one more)\\n- Token overlap control\\n- COMET translation quality validation\\n\\n**理想状态 (nice-to-have)**:\\n- Track 2 SAE analysis (Claim 5)\\n- Track 3 steering (Claim 6)\\n- 5+ language pairs covering multiple typological families\\n- Full CKA/SVCCA layer analysis\\n\\n**不做 (out of scope)**:\\n- 10-language full CLEAR replication\\n- Custom SAE training\\n- MoE model analysis\\n\", \"total_chars\": 7801, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21a5b530-c784-46e6-93d6-cbb544c787a6",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "00a65ef7-a9b8-4f69-90bd-aa7cf4c74014",
  "sourceToolAssistantUUID": "21a5b530-c784-46e6-93d6-cbb544c787a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T03:12:23.973Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Bt9mHAHXiGZqCXPuVxYttw`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00a65ef7-a9b8-4f69-90bd-aa7cf4c74014",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmtRjsw9KvyizxLvc5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22227e24-d8c6-49ec-afbf-2676f7c087c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVgyskuYYhymx6rrNCSk64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6468,
      "cache_read_input_tokens": 19720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6468,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 22 · 2026-05-22T03:12:23.985Z_

<details><summary>↩ Tool result · `toolu_01Bt9mHAHXiGZqCXPuVxYttw`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'clkc_mech_interp'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22227e24-d8c6-49ec-afbf-2676f7c087c3",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "ce675cdd-4a27-4830-bf1a-20a6b65e2bd0",
  "sourceToolAssistantUUID": "22227e24-d8c6-49ec-afbf-2676f7c087c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T03:12:24.555Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01X8i9WsFyREtqZQamDyJzsD`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce675cdd-4a27-4830-bf1a-20a6b65e2bd0",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsmtRjsw9KvyizxLvc5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62c1f637-2d0d-479a-991c-ef188abeec95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVgyskuYYhymx6rrNCSk64",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6468,
      "cache_read_input_tokens": 19720,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6468
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 301,
          "cache_read_input_tokens": 19720,
          "cache_creation_input_tokens": 6468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6468,
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

_source line 24 · 2026-05-22T03:12:24.568Z_

<details><summary>↩ Tool result · `toolu_01X8i9WsFyREtqZQamDyJzsD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'clkc_mech_interp'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62c1f637-2d0d-479a-991c-ef188abeec95",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "0c9f8ab6-d225-4cbe-8840-d6432678fbea",
  "sourceToolAssistantUUID": "62c1f637-2d0d-479a-991c-ef188abeec95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-22T03:12:27.992Z_

Now let me look at the actual paper-related files and experiment artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c9f8ab6-d225-4cbe-8840-d6432678fbea",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsnGZFpbGabqzc5LK5N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73814fe7-eaae-4f8e-9d40-52180610e875",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EKPZcQEAdTnRomrfh8SmX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4775,
      "cache_read_input_tokens": 26188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4775,
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

_source line 26 · 2026-05-22T03:12:29.100Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HiFR1a9NHDH6jzNxzrUNdT`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73814fe7-eaae-4f8e-9d40-52180610e875",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsnGZFpbGabqzc5LK5N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25ec65d7-1d07-47aa-a268-f7bfd74c112e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EKPZcQEAdTnRomrfh8SmX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4775,
      "cache_read_input_tokens": 26188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4775,
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

_source line 27 · 2026-05-22T03:12:29.212Z_

<details><summary>↩ Tool result · `toolu_01HiFR1a9NHDH6jzNxzrUNdT`</summary>

```text
artifacts/dream_reports/dream_20260522T023801/best/paper.tex
artifacts/dream_reports/dream_20260522T023801/median/paper.tex
artifacts/dream_reports/dream_20260522T023801/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25ec65d7-1d07-47aa-a268-f7bfd74c112e",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "f0ec7b8d-9c02-4ab5-9f5d-233e3f745ee7",
  "sourceToolAssistantUUID": "25ec65d7-1d07-47aa-a268-f7bfd74c112e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T03:12:29.414Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PzMwisSv4jPdcVgsQdmUUU`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0ec7b8d-9c02-4ab5-9f5d-233e3f745ee7",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsnGZFpbGabqzc5LK5N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e4ce7a4-1728-4474-9adf-9702434d7476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EKPZcQEAdTnRomrfh8SmX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4775,
      "cache_read_input_tokens": 26188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4775,
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

_source line 29 · 2026-05-22T03:12:29.501Z_

<details><summary>↩ Tool result · `toolu_01PzMwisSv4jPdcVgsQdmUUU`</summary>

```text
artifacts/clkc_code/.venv/lib/python3.14/site-packages/markdown_it/port.yaml
artifacts/clkc_code/.venv/lib/python3.14/site-packages/datasets/utils/resources/readme_structure.yaml
literature_map.yaml
artifacts/clkc_code/.venv/lib/python3.14/site-packages/torch/_export/serde/schema.yaml
artifacts/clkc_code/.venv/lib/python3.14/site-packages/torchgen/packaged/ATen/native/native_functions.yaml
artifacts/clkc_code/.venv/lib/python3.14/site-packages/torchgen/packaged/ATen/native/tags.yaml
artifacts/clkc_code/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/deprecated.yaml
artifacts/clkc_code/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/derivatives.yaml
mistakes.yaml
decisions.yaml
artifacts/manifest.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260522T023801/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T023801/median/imagined_experiments.yaml
registry.yaml
artifacts/dream_reports/dream_20260522T023801/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260522T023801/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e4ce7a4-1728-4474-9adf-9702434d7476",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "3be6fc43-dfbb-4a40-9252-f44ff150d0bf",
  "sourceToolAssistantUUID": "5e4ce7a4-1728-4474-9adf-9702434d7476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T03:12:29.951Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014atMroyswVmaVSZuWyS3xr`</summary>

```json
{
  "pattern": "artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3be6fc43-dfbb-4a40-9252-f44ff150d0bf",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsnGZFpbGabqzc5LK5N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9962278-e5a5-4b68-a373-45a87d6be5b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EKPZcQEAdTnRomrfh8SmX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4775,
      "cache_read_input_tokens": 26188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4775,
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

_source line 31 · 2026-05-22T03:12:30.301Z_

<details><summary>↩ Tool result · `toolu_014atMroyswVmaVSZuWyS3xr`</summary>

```text
artifacts/clkc_code/.venv/.gitignore
artifacts/clkc_code/.venv/pyvenv.cfg
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/METADATA
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/WHEEL
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/entry_points.txt
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/licenses/AUTHORS.txt
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/licenses/LICENSE.txt
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/top_level.txt
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/__main__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/__pip-runner__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/build_env.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cache.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/autocompletion.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/base_command.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/cmdoptions.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/command_context.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/index_command.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/main.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/main_parser.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/parser.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/progress_bars.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/req_command.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/spinners.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/cli/status_codes.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/cache.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/check.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/completion.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/debug.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/download.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/freeze.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/hash.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/help.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/index.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/inspect.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/install.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/list.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/lock.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/search.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/show.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/uninstall.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/commands/wheel.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/distributions/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/distributions/base.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/distributions/installed.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/distributions/sdist.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/distributions/wheel.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/exceptions.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/index/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/index/collector.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/index/package_finder.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/index/sources.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/locations/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/locations/_distutils.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/locations/_sysconfig.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/locations/base.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/main.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/metadata/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/metadata/_json.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/metadata/base.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_compat.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_dists.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_envs.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/metadata/pkg_resources.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/candidate.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/direct_url.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/format_control.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/index.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/installation_report.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/link.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/pylock.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/scheme.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/search_scope.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/selection_prefs.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/target_python.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/models/wheel.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/network/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/network/auth.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/network/cache.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/network/download.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/network/lazy_wheel.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/network/session.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/network/utils.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/network/xmlrpc.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/operations/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__init__.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/build_tracker.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_editable.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_legacy.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_editable.py
artifacts/clkc_code/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_legacy.py
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9962278-e5a5-4b68-a373-45a87d6be5b2",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "8da3dc37-14eb-4521-bc3f-fcff9f903f31",
  "sourceToolAssistantUUID": "f9962278-e5a5-4b68-a373-45a87d6be5b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T03:12:32.984Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pte7q4gXoUEHVUwNK5ut3i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8da3dc37-14eb-4521-bc3f-fcff9f903f31",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsngm3QXMUaWPWZmwQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19c6fcfd-77aa-4339-ba80-a4455733f007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbhdTVUGq4Ry3Qnq6YrzKK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4087,
      "cache_read_input_tokens": 30963,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4087
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 30963,
          "cache_creation_input_tokens": 4087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4087,
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

_source line 33 · 2026-05-22T03:12:33.269Z_

<details><summary>↩ Tool result · `toolu_01Pte7q4gXoUEHVUwNK5ut3i`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{hyperref}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{xcolor}
11	\usepackage{natbib}
12	\usepackage{caption}
13	\usepackage{subcaption}
14	
15	\title{Cross-Lingual Conflict Detection in Multilingual LLMs:\\
16	Mechanistic Evidence for English-Anchored Representations}
17	
18	\author{
19	Anonymous Authors
20	}
21	
22	\date{}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	% ============================================================
29	% ABSTRACT
30	% ============================================================
31	\begin{abstract}
32	Multilingual large language models resolve entity-centric knowledge conflicts in ways that depend on linguistic affinity rather than resource abundance, yet the internal mechanisms underlying this behavior remain unexplored. We present a mechanistic investigation of cross-lingual conflict detection signals in the residual stream of three transformer architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) across two typologically distinct language pairs (EN$\leftrightarrow$ZH, EN$\leftrightarrow$JA). Linear probes trained on residual stream activations detect conflict signals at 70--77\% balanced accuracy, with cross-lingual transfer exhibiting a consistent directional asymmetry: transfer toward English (X$\to$EN) outperforms transfer away from English (EN$\to$X) by 6.3--7.9 percentage points across all model--language-pair combinations tested. Sparse autoencoder (SAE) analysis reveals 18 cross-lingually shared conflict features concentrated in middle layers (Jaccard = 0.28) that diverge in late layers (Jaccard = 0.12, $p = 0.008$), while language-identity features occupy early layers with minimal overlap (4.3\%). Representation steering using probe directions and SAE features causally shifts model outputs from parametric to contextual answers, with cross-lingual flip rates reproducing the same directional asymmetry. These converging lines of evidence---probing, feature decomposition, and causal intervention---support an English-anchored hypothesis: conflict detection is encoded in a language-universal mid-layer representation anchored to English, while language-specific resolution occurs during late-layer language transition.
33	\end{abstract}
34	
35	% ============================================================
36	% 1. INTRODUCTION
37	% ============================================================
38	\section{Introduction}
39	
40	When multilingual LLMs encounter factual knowledge conflicts---cases where contextual information contradicts parametric knowledge---the language of presentation systematically influences which knowledge source prevails. Recent work by Zhao et al.\ (2026) (CLEAR) demonstrated that for entity-centric factual conflicts, linguistic affinity between the context and query languages determines conflict resolution outcomes, rather than the absolute resource abundance of either language. This finding raises a fundamental mechanistic question: \emph{how are cross-lingual conflict signals encoded in the model's internal representations, and why does linguistic similarity play a decisive role?}
41	
42	We investigate this question through three complementary analysis tracks applied to the residual stream of multilingual transformers. \textbf{Track 1} (probing) trains linear and MLP classifiers on residual stream activations to detect and transfer conflict signals across languages. \textbf{Track 2} (SAE decomposition) uses pre-trained sparse autoencoders to identify monosemantic conflict features and characterize their cross-lingual sharing patterns. \textbf{Track 3} (causal intervention) steers model behavior by manipulating conflict-related directions in activation space.
43	
44	We formulate two competing hypotheses about the encoding of cross-lingual conflict signals:
45	
46	\begin{itemize}
47	    \item \textbf{H1 (English-anchored universal detection)}: Conflict detection signals are language-independent, encoded in a mid-layer shared representation space anchored to English. Late-layer language transition introduces language-specific interference that affects resolution but not detection. This predicts: (a) mid-layer cross-lingual feature sharing significantly exceeds late-layer sharing; (b) transfer toward English is consistently stronger than transfer away.
48	
49	    \item \textbf{H2 (Language-pair-specific encoding)}: Conflict features are language-pair-specific from mid-layers onward, with linguistic distance directly encoded in conflict representations. This predicts: (a) no significant difference between mid-layer and late-layer feature sharing; (b) transfer patterns differ qualitatively across language pairs.
50	\end{itemize}
51	
52	Our experiments on three architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) and two language pairs (EN$\leftrightarrow$ZH, EN$\leftrightarrow$JA) yield four principal findings:
53	
54	\begin{enumerate}
55	    \item Cross-lingual conflict signals are linearly detectable in the residual stream at 64--77\% balanced accuracy across all directions and models, with permutation test $p < 0.001$.
56	    \item Cross-lingual transfer is directionally asymmetric: X$\to$EN exceeds EN$\to$X by 6.3--7.9pp across all 4 model$\times$language-pair combinations (3/4 statistically significant at 95\% CI, 4/4 directionally consistent).
57	    \item SAE conflict features are cross-lingually shared in middle layers (Jaccard = 0.28) but diverge in late layers (Jaccard = 0.12), with language-identity features occupying a distinct early-layer subspace (overlap rate 4.3\%).
58	    \item Representation steering causally shifts conflict resolution behavior, with cross-lingual flip rate asymmetry mirroring the probe transfer asymmetry.
59	\end{enumerate}
60	
61	These results collectively support H1: conflict detection is encoded in an English-anchored language-universal representation, with language-specific processing emerging during late-layer transition.
62	
63	% ============================================================
64	% 2. RELATED WORK
65	% ============================================================
66	\section{Related Work}
67	
68	\paragraph{Knowledge conflicts in LLMs.}
69	Knowledge conflicts arise when contextual information contradicts a model's parametric knowledge. Prior work has characterized monolingual conflict resolution behavior and identified internal signals predictive of which knowledge source prevails. However, the cross-lingual dimension remains largely unexplored. CLEAR (Zhao et al., 2026) established that for entity-centric conflicts, linguistic affinity---not resource abundance---determines resolution outcomes across 10 languages, but provided no mechanistic account.
70	
71	\paragraph{Cross-lingual representations in multilingual models.}
72	Multilingual transformers develop shared cross-lingual representations in middle layers before diverging in late layers for language-specific decoding. Wendler et al.\ (2024) documented this ``language transition'' phenomenon across model families, finding that mid-layers form language-agnostic conceptual representations. Our work builds on this finding by examining how conflict-specific signals interact with this layer-wise structure.
73	
74	\paragraph{Sparse autoencoders for mechanistic interpretability.}
75	Sparse autoencoders (SAEs) decompose neural activations into interpretable monosemantic features. Recent work has applied SAEs to identify knowledge-related features and demonstrated that manipulating these features can steer model behavior (SpARE). We extend this line to the cross-lingual setting, using pre-trained SAEs (Qwen-Scope) to decompose conflict signals into shared and language-specific components.
76	
77	\paragraph{Representation steering.}
78	Activation steering modifies model behavior by adding direction vectors to the residual stream. While effective for monolingual settings, cross-lingual steering introduces additional challenges. We use both probe-derived directions and SAE feature directions for cross-lingual conflict steering, providing complementary causal evidence.
79	
80	% ============================================================
81	% 3. METHOD
82	% ============================================================
83	\section{Method}
84	
85	\subsection{Data Construction}
86	
87	We construct cross-lingual knowledge conflict datasets from ConflictQA, which contains entity-centric factual questions where contextual and parametric answers diverge. For each question, we obtain model responses in English (EN) and generate high-quality translations in Chinese (ZH) and Japanese (JA) using the target models themselves, followed by back-translation quality verification using COMET (wmt22-comet-da).
88	
89	\paragraph{Translation quality validation.}
90	Back-translation COMET scores are computed for all translated samples. We perform tercile ablation analysis to verify that translation quality does not confound conflict detection: samples are split into low, medium, and high COMET terciles, and balanced accuracy is compared across groups. As shown in Table~\ref{tab:comet}, both Llama-3.1-8B and Qwen3-8B show no positive correlation between COMET score and probe accuracy (Fisher $p > 0.69$), with the high-COMET tercile actually producing \emph{lower} accuracy than the low-COMET tercile. This rules out translation quality as a confound.
91	
92	\begin{table}[t]
93	\centering
94	\caption{COMET tercile ablation. Probe accuracy does not increase with translation quality, ruling out translation quality as a confound.}
95	\label{tab:comet}
96	\small
97	\begin{tabular}{llcccc}
98	\toprule
99	Model & Tercile & $N$ & COMET$_{\text{mean}}$ & Bal.\ Acc. & $\Delta$ vs Low \\
100	\midrule
101	\multirow{3}{*}{Llama-3.1-8B} & Low & 91 & 0.582 & 64.8\% & --- \\
102	 & Med & 91 & 0.714 & 66.1\% & +1.3pp \\
103	 & High & 90 & 0.821 & 63.2\% & $-$1.6pp \\
104	\midrule
105	\multirow{3}{*}{Qwen3-8B} & Low & 56 & 0.585 & 66.4\% & --- \\
106	 & Med & 56 & 0.700 & 67.7\% & +1.3pp \\
107	 & High & 56 & 0.816 & 60.7\% & $-$5.6pp \\
108	\bottomrule
109	\end{tabular}
110	\end{table}
111	
112	\subsection{Track 1: Residual Stream Probing}
113	
114	For each model, we extract residual stream activations at every layer for conflict and non-conflict samples in each language. We train logistic regression probes (L2-regularized) to classify conflict vs.\ non-conflict, using 5-fold stratified cross-validation with balanced accuracy as the metric. Cross-lingual transfer is evaluated by training on language A and testing on language B without fine-tuning. We assess significance using permutation tests ($n = 1000$) and bootstrap confidence intervals ($n = 100$) for the asymmetry gap.
115	
116	MLP probes (single hidden layer, 256 units) are trained with identical splits to quantify non-linear components. Statistical significance is determined at $\alpha = 0.05$.
117	
118	\subsection{Track 2: SAE Feature Analysis}
119	
120	We apply pre-trained sparse autoencoders from Qwen-Scope to Qwen3-8B-Base activations. Conflict-relevant features are identified via mutual information between feature activations and conflict labels, yielding a ranked list from which the top 128 candidates are selected and filtered to retain features with robust conflict--non-conflict discrimination.
121	
122	To disentangle conflict features from language-identity features, we apply LangFIR-style random-token filtering: features that activate consistently across random token sequences in a given language are classified as language-identity features, and their overlap with conflict features is quantified.
123	
124	Cross-lingual feature sharing is measured by the Jaccard index of EN and ZH conflict feature sets, computed separately for early (0--33\%), mid (33--67\%), and late (67--100\%) layer groups. The H1 vs.\ H2 prediction is tested by a paired permutation test comparing mid-layer and late-layer Jaccard.
125	
126	\subsection{Track 3: Causal Intervention via Steering}
127	
128	\paragraph{Probe-based steering.}
129	The weight vector of the best-layer linear probe defines a conflict direction in activation space. We add $\alpha \cdot \mathbf{v}$ to the residual stream at the optimal layer (where $\alpha$ is tuned to maximize flip rate while preserving coherence) and measure the rate at which model outputs shift from parametric to contextual answers.
130	
131	\paragraph{SAE feature steering.}
132	We construct steering vectors from SAE conflict features (shared, EN-only, ZH-only, and combined sets) by clamping selected feature activations. Cross-lingual transfer is evaluated by applying EN-derived steering vectors to ZH inputs and vice versa.
133	
134	% ============================================================
135	% 4. EXPERIMENTS AND RESULTS
136	% ============================================================
137	\section{Experiments and Results}
138	
139	\subsection{Cross-Architecture Conflict Detectability}
140	\label{sec:detectability}
141	
142	We train linear probes on residual stream activations from three model architectures: Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B-IT. Table~\ref{tab:cross_arch} reports balanced accuracy for all four transfer directions (within-language and cross-lingual) along with the asymmetry gap and bootstrap confidence intervals.
143	
144	\begin{table}[t]
145	\centering
146	\caption{Cross-architecture probe results. EN$\to$EN and ZH$\to$ZH are within-language; EN$\to$ZH and ZH$\to$EN are cross-lingual transfer. Asym.\ gap = (ZH$\to$EN) $-$ (EN$\to$ZH). All permutation test $p < 0.001$.}
147	\label{tab:cross_arch}
148	\small
149	\begin{tabular}{lccccccl}
150	\toprule
151	Model & EN$\to$EN & ZH$\to$ZH & EN$\to$ZH & ZH$\to$EN & Gap & 95\% CI & Sig. \\
152	\midrule
153	Llama-3.1-8B & 77.1\% & 71.2\% & 64.1\% & 71.3\% & +7.2pp & [1.1, 13.6] & Yes \\
154	Qwen3-8B & 75.3\% & 71.6\% & 65.0\% & 72.2\% & +7.2pp & [$-$1.2, 13.4] & No (trend) \\
155	Gemma-2-9B-IT & 76.4\% & 70.8\% & 64.7\% & 72.6\% & +7.9pp & [2.3, 13.8] & Yes \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	All within-language probes achieve 70--77\% balanced accuracy, substantially above the 50\% chance baseline (permutation $p < 0.001$ for all). Cross-lingual transfer succeeds in all directions (64--73\%), confirming that conflict signals are partially shared across languages.
161	
162	The asymmetry gap is remarkably consistent: +7.2pp (Llama), +7.2pp (Qwen), and +7.9pp (Gemma), with a coefficient of variation below 6\%. Two of three models reach statistical significance at 95\% confidence; Qwen shows the same direction but the CI includes zero at $N \approx 1000$. We address this power issue in Section~\ref{sec:scaling}.
163	
164	\paragraph{MLP non-linearity.}
165	MLP probes reveal direction-dependent non-linear components in the weak transfer direction (EN$\to$ZH), as shown in Table~\ref{tab:mlp}. The gain is largest for Gemma (+6.1pp), moderate for Llama (+4.7pp), and smallest for Qwen (+2.3pp). This gradient anti-correlates with each model's Chinese pre-training data proportion, suggesting that stronger cross-lingual alignment reduces the non-linear component of cross-lingual conflict mapping.
166	
167	\begin{table}[t]
168	\centering
169	\caption{MLP gain in the weak transfer direction (EN$\to$ZH). Models with better Chinese alignment show smaller non-linear gains.}
170	\label{tab:mlp}
171	\small
172	\begin{tabular}{lcccc}
173	\toprule
174	Model & Linear & MLP & Gain & Interpretation \\
175	\midrule
176	Llama-3.1-8B & 64.1\% & 68.8\% & +4.7pp & Strong non-linear component \\
177	Qwen3-8B & 65.0\% & 67.3\% & +2.3pp & Weak (better ZH alignment) \\
178	Gemma-2-9B-IT & 64.7\% & 70.8\% & +6.1pp & Moderate non-linear component \\
179	\bottomrule
180	\end{tabular}
181	\end{table}
182	
183	\subsection{Multilingual Extension: EN$\leftrightarrow$JA}
184	\label{sec:multilingual}
185	
186	To test whether the asymmetry generalizes beyond EN$\leftrightarrow$ZH, we replicate the full probe experiment on the EN$\leftrightarrow$JA language pair using Qwen3-8B and Llama-3.1-8B. Japanese is typologically distinct from Chinese (SOV word order, complex morphology, multiple writing systems) while belonging to the same CJK cultural sphere.
187	
188	\begin{table}[t]
189	\centering
190	\caption{Multi-lingual asymmetry comparison. All four model$\times$language-pair combinations show X$\to$EN $>$ EN$\to$X.}
191	\label{tab:multilingual}
192	\small
193	\begin{tabular}{llccccc}
194	\toprule
195	Model & Pair & X$\to$EN & EN$\to$X & Gap & 95\% CI & Direction \\
196	\midrule
197	Qwen3-8B & EN$\leftrightarrow$ZH & 72.2\% & 65.0\% & +7.2pp & [$-$1.2, 13.4] & ZH$\to$EN wins \\
198	Qwen3-8B & EN$\leftrightarrow$JA & 68.1\% & 61.8\% & +6.3pp & [0.4, 12.5] & JA$\to$EN wins \\
199	Llama-3.1-8B & EN$\leftrightarrow$ZH & 71.3\% & 64.1\% & +7.2pp & [1.1, 13.6] & ZH$\to$EN wins \\
200	Llama-3.1-8B & EN$\leftrightarrow$JA & 66.8\% & 60.1\% & +6.7pp & [0.8, 13.1] & JA$\to$EN wins \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	All four combinations in Table~\ref{tab:multilingual} show the same directional asymmetry: transfer toward English outperforms transfer away from English. This is consistent with H1 (English-anchored detection) and inconsistent with H2, which predicts language-pair-specific patterns. The JA asymmetry gap (6.3--6.7pp) is slightly smaller than the ZH gap (7.2pp), consistent with weaker Japanese representation in these models' training data. Three of four CIs exclude zero; the remaining one (Qwen EN$\leftrightarrow$ZH) is directionally consistent.
206	
207	\subsection{Layer-wise Representation Analysis}
208	\label{sec:layerwise}
209	
210	\paragraph{CKA and SVCCA analysis.}
211	We compute Centered Kernel Alignment (CKA) and Singular Vector Canonical Correlation Analysis (SVCCA) between EN and ZH activations at each layer to quantify cross-lingual representation similarity. Table~\ref{tab:cka} reports mean similarity by layer group.
212	
213	\begin{table}[t]
214	\centering
215	\caption{CKA similarity between EN and ZH activations by layer group. All three models show high mid-layer similarity followed by a sharp late-layer drop.}
216	\label{tab:cka}
217	\small
218	\begin{tabular}{lcccc}
219	\toprule
220	Model & Early (0--33\%) & Mid (33--67\%) & Late (67--100\%) & Mid--Late Drop \\
221	\midrule
222	Llama-3.1-8B & 0.71 & 0.83 & 0.52 & $-$0.31 \\
223	Qwen3-8B & 0.68 & 0.81 & 0.56 & $-$0.25 \\
224	Gemma-2-9B-IT & 0.70 & 0.82 & 0.53 & $-$0.29 \\
225	\midrule
226	Mean & 0.70 & 0.82 & 0.54 & $-$0.28 \\
227	\bottomrule
228	\end{tabular}
229	\end{table}
230	
231	All three models exhibit the same pattern: EN--ZH representations are most similar in middle layers (CKA $\approx 0.82$), with a sharp drop in late layers (CKA $\approx 0.54$). The mean mid-layer SVCCA similarity is 0.78, dropping to 0.48 in late layers. This is consistent with the ``language transition'' phenomenon documented by Wendler et al.\ (2024).
232	
233	The probe accuracy peak correlates negatively with the CKA transition point ($r = -0.71$), indicating that conflict signals are most detectable precisely where cross-lingual representations begin to diverge---the boundary between language-universal and language-specific processing. The language transition layer ratios are 0.75 (Llama), 0.60 (Qwen), and 0.68 (Gemma), suggesting model-specific transition dynamics.
234	
235	\paragraph{PCA visualization of probe weights.}
236	PCA analysis of residual stream activations at the optimal probe layer reveals distinct conflict vs.\ non-conflict clusters. At mid-layers, EN and ZH conflict samples show high centroid overlap (cosine similarity = 0.78), supporting language-universal conflict encoding. At late layers, this overlap decreases substantially (cosine = 0.51), reflecting language-specific divergence. The silhouette score for conflict/non-conflict separation is higher for English (0.42) than Chinese (0.35), consistent with the English probe's higher within-language accuracy. PCA explains 38\% of variance in two dimensions, indicating that conflict encoding is distributed but directionally coherent.
237	
238	\subsection{SAE Feature Analysis}
239	\label{sec:sae}
240	
241	\paragraph{Conflict feature identification.}
242	Using Qwen-Scope pre-trained SAEs on Qwen3-8B-Base, we identify conflict-relevant features via mutual information screening. From 65,536 total features, 128 candidates are selected, of which 47 pass robustness filtering. These features achieve AUROC = 0.81 for conflict vs.\ non-conflict discrimination and exhibit mean sparsity of 0.034.
243	
244	\begin{table}[t]
245	\centering
246	\caption{SAE conflict feature summary. Shared features achieve the highest AUROC; language-identity features (control) are near chance.}
247	\label{tab:sae_features}
248	\small
249	\begin{tabular}{lccc}
250	\toprule
251	Category & Count & Sparsity & AUROC \\
252	\midrule
253	EN-specific conflict & 20 & 0.031 & 0.79 \\
254	ZH-specific conflict & 13 & 0.038 & 0.76 \\
255	Cross-lingual shared & 18 & 0.033 & 0.84 \\
256	Language-identity (control) & 42 & 0.025 & 0.52 \\
257	\bottomrule
258	\end{tabular}
259	\end{table}
260	
261	Table~\ref{tab:sae_features} decomposes the identified features into EN-specific (20), ZH-specific (13), and cross-lingually shared (18) conflict features. The shared features achieve the highest AUROC (0.84), while language-identity features serve as a negative control with near-chance AUROC (0.52), confirming that conflict features carry semantic rather than language-identity information.
262	
263	\paragraph{LangFIR deconfounding.}
264	LangFIR random-token filtering identifies 42 language-identity features, concentrated in early layers (68\% in layers 0--33\%). Conflict features, by contrast, concentrate in mid layers (61\% in layers 33--67\%). The overlap between conflict and language-identity features is minimal: only 2 features (overlap rate = 4.3\%), and the layer distributions are significantly different ($p = 0.003$). Table~\ref{tab:langfir} details the layer distribution.
265	
266	\begin{table}[t]
267	\centering
268	\caption{Feature type layer distribution. Language-identity features concentrate in early layers; conflict features concentrate in mid layers with minimal overlap.}
269	\label{tab:langfir}
270	\small
271	\begin{tabular}{lcccc}
272	\toprule
273	Feature Type & Early (0--33\%) & Mid (33--67\%) & Late (67--100\%) & Total \\
274	\midrule
275	Language-identity & 29 (69\%) & 9 (21\%) & 4 (10\%) & 42 \\
276	Conflict (shared) & 2 (11\%) & 11 (61\%) & 5 (28\%) & 18 \\
277	Conflict (EN-only) & 1 (5\%) & 10 (50\%) & 9 (45\%) & 20 \\
278	Conflict (ZH-only) & 1 (8\%) & 7 (54\%) & 5 (38\%) & 13 \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	\paragraph{Cross-lingual Jaccard analysis.}
284	The Jaccard index of EN and ZH conflict features varies significantly across layer groups (Table~\ref{tab:jaccard}). Mid-layer Jaccard (0.28) substantially exceeds late-layer Jaccard (0.12), with a difference of 0.16 that is statistically significant (paired permutation test $p = 0.008$). This directly supports H1 over H2: conflict features are shared across languages in mid layers but diverge after the language transition in late layers.
285	
286	\begin{table}[t]
287	\centering
288	\caption{Layer-group Jaccard analysis. Mid-layer sharing significantly exceeds late-layer sharing ($p = 0.008$), supporting H1.}
289	\label{tab:jaccard}
290	\small
291	\begin{tabular}{lccccc}
292	\toprule
293	Layer Group & EN feat. & ZH feat. & Shared & Jaccard & 95\% CI \\
294	\midrule
295	Early (0--33\%) & 3 & 3 & 1 & 0.20 & [0.04, 0.41] \\
296	Mid (33--67\%) & 21 & 18 & 8 & 0.28 & [0.16, 0.42] \\
297	Late (67--100\%) & 14 & 10 & 3 & 0.12 & [0.03, 0.24] \\
298	\bottomrule
299	\end{tabular}
300	\end{table}
301	
302	\subsection{Causal Intervention: Representation Steering}
303	\label{sec:steering}
304	
305	\paragraph{Probe-based steering.}
306	Using the linear probe's weight vector as a steering direction, we add a scaled perturbation to the residual stream at the optimal layer and measure the rate at which model outputs flip from parametric to contextual answers (or vice versa). Table~\ref{tab:probe_steering} reports flip rates across models and directions.
307	
308	\begin{table}[t]
309	\centering
310	\caption{Probe-based steering flip rates. Cross-lingual steering reproduces the asymmetry: ZH$\to$EN $>$ EN$\to$ZH. All conditions substantially exceed the random baseline ($\approx$5\%).}
311	\label{tab:probe_steering}
312	\small
313	\begin{tabular}{llccc}
314	\toprule
315	Model & Direction & Flip Rate & Random Baseline & Lift \\
316	\midrule
317	Llama & EN (mono) & 31.2\% & 4.8\% & 6.5$\times$ \\
318	Llama & ZH (mono) & 26.8\% & 5.1\% & 5.3$\times$ \\
319	Llama & ZH$\to$EN (cross) & 24.3\% & 4.9\% & 5.0$\times$ \\
320	Llama & EN$\to$ZH (cross) & 17.8\% & 5.2\% & 3.4$\times$ \\
321	\midrule
322	Qwen & EN (mono) & 28.9\% & 4.6\% & 6.3$\times$ \\
323	Qwen & ZH$\to$EN (cross) & 22.1\% & 4.7\% & 4.7$\times$ \\
324	Qwen & EN$\to$ZH (cross) & 19.2\% & 5.0\% & 3.8$\times$ \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	All steering conditions produce flip rates 3.4--6.5$\times$ above random baselines, establishing a causal link between the detected conflict signal and conflict resolution behavior. Monolingual EN steering achieves the highest flip rate (31.2\%), followed by monolingual ZH (26.8\%), cross-lingual ZH$\to$EN (24.3\%), and cross-lingual EN$\to$ZH (17.8\%). The cross-lingual asymmetry gap (Llama: 24.3\% $-$ 17.8\% = 6.5pp) mirrors the probe transfer asymmetry, providing causal evidence that the asymmetry reflects the structure of conflict encoding, not merely a statistical artifact of probe training. Coherence is preserved at 91\%.
330	
331	\paragraph{SAE feature steering.}
332	SAE-based steering enables more targeted intervention at the feature level. Table~\ref{tab:sae_steering} compares monolingual and cross-lingual steering effectiveness using SAE conflict features.
333	
334	\begin{table}[t]
335	\centering
336	\caption{SAE feature steering: cross-lingual transfer. EN features transferred to ZH retain 69\% of monolingual effectiveness. The ZH$\to$EN direction again outperforms EN$\to$ZH.}
337	\label{tab:sae_steering}
338	\small
339	\begin{tabular}{lcccc}
340	\toprule
341	Condition & EM$_C$ & EM$_M$ & Flip Rate & Coherence \\
342	\midrule
343	EN mono (baseline) & 0.42 & 0.31 & 35.0\% & 0.93 \\
344	EN$\to$ZH (cross) & 0.29 & 0.22 & 24.0\% & 0.87 \\
345	ZH$\to$EN (cross) & 0.34 & 0.26 & 31.0\% & 0.89 \\
346	Random features (control) & 0.05 & 0.04 & 5.2\% & 0.94 \\
347	\bottomrule
348	\end{tabular}
349	\end{table}
350	
351	Cross-lingual SAE steering achieves a transfer efficiency of 69\% (cross-lingual flip rate / monolingual flip rate), indicating that English conflict features encode substantial cross-lingual information. The directional asymmetry persists: ZH$\to$EN steering (31.0\%) outperforms EN$\to$ZH steering (24.0\%) by 7.0pp, consistent with probe-based results. Random feature steering serves as a negative control at 5.2\%.
352	
353	\paragraph{Feature-set ablation.}
354	To further test H1, we compare steering effectiveness when using only shared features, only language-specific features, and the full combined set (Table~\ref{tab:feature_ablation}).
355	
356	\begin{table}[t]
357	\centering
358	\caption{Feature-set steering ablation. Shared features drive the majority of cross-lingual steering; language-specific features contribute marginally.}
359	\label{tab:feature_ablation}
360	\small
361	\begin{tabular}{llcc}
362	\toprule
363	Feature Set & Target Lang & Flip Rate & vs.\ Shared \\
364	\midrule
365	Shared (18 features) & ZH & 28.0\% & 1.0$\times$ \\
366	EN-only (20 features) & ZH & 11.0\% & 0.39$\times$ \\
367	ZH-only (13 features) & EN & 9.0\% & 0.32$\times$ \\
368	Combined (all 51) & ZH & 33.0\% & 1.18$\times$ \\
369	\bottomrule
370	\end{tabular}
371	\end{table}
372	
373	Shared features alone achieve 28.0\% cross-lingual flip rate, while language-specific features yield only 9--11\%. The combined set provides a marginal 18\% lift over shared-only, indicating that cross-lingual conflict steering is primarily driven by the language-universal feature subspace. This is the most fine-grained causal evidence for H1: the shared features identified in Section~\ref{sec:sae} are not merely correlated with conflict signals but causally drive cross-lingual conflict resolution.
374	
375	\subsection{Robustness and Scaling}
376	\label{sec:scaling}
377	
378	\paragraph{Larger dataset validation.}
379	Expanding ConflictQA sampling to $\sim$2,200 samples per model narrows confidence intervals by $\sim$28\% (Table~\ref{tab:scaling}). Critically, Qwen's CI shifts from [$-$1.2, 13.4] to [1.8, 12.3], achieving statistical significance. Point estimates remain stable (7.0pp vs.\ 7.2pp), confirming that the effect size is robust and Qwen's initial non-significance was a power issue.
380	
381	\begin{table}[t]
382	\centering
383	\caption{Sample size scaling. Doubling the dataset narrows CIs by $\sim$28\% and brings Qwen to significance.}
384	\label{tab:scaling}
385	\small
386	\begin{tabular}{lcccc}
387	\toprule
388	Model & $N$ & Asym.\ gap & 95\% CI & Sig.? \\
389	\midrule
390	Llama & $\sim$1,000 & +7.2pp & [1.1, 13.6] & Yes \\
391	Llama & $\sim$2,200 & +7.4pp & [3.1, 11.8] & Yes \\
392	Qwen & $\sim$1,000 & +7.2pp & [$-$1.2, 13.4] & No \\
393	Qwen & $\sim$2,200 & +7.0pp & [1.8, 12.3] & Yes \\
394	\bottomrule
395	\end{tabular}
396	\end{table}
397	
398	\paragraph{Label noise robustness.}
399	We systematically inject 5--20\% label noise into the training set and measure probe accuracy degradation (Table~\ref{tab:noise}). The probe degrades gracefully at $\sim$2.6pp per 5\% noise, maintaining $>$73\% accuracy at 10\% noise. Given that our verification pipeline's estimated label error rate is $<$5\%, this provides ample safety margin. Cross-lingual noise sensitivity is similar across directions (1.3$\times$ for EN$\to$ZH, 1.1$\times$ for ZH$\to$EN), indicating that robustness is an intrinsic property of the probe rather than language-dependent.
400	
401	\begin{table}[t]
402	\centering
403	\caption{Label noise robustness (Llama EN$\to$EN). Graceful degradation at $\sim$2.6pp per 5\% noise.}
404	\label{tab:noise}
405	\small
406	\begin{tabular}{lccc}
407	\toprule
408	Noise Level & Bal.\ Acc. & $\Delta$ vs.\ 0\% & Rel.\ Drop \\
409	\midrule
410	0\% & 77.1\% & --- & --- \\
411	5\% & 75.4\% & $-$1.7pp & 2.2\% \\
412	10\% & 73.1\% & $-$4.0pp & 5.2\% \\
413	15\% & 70.2\% & $-$6.9pp & 8.9\% \\
414	20\% & 66.8\% & $-$10.3pp & 13.4\% \\
415	\bottomrule
416	\end{tabular}
417	\end{table}
418	
419	% ============================================================
420	% 5. DISCUSSION
421	% ============================================================
422	\section{Discussion}
423	
424	\paragraph{H1 vs.\ H2 resolution.}
425	Three independent lines of evidence converge on H1 (English-anchored universal detection):
426	
427	\begin{enumerate}
428	    \item \textbf{Probe transfer asymmetry}: All 4 model$\times$language-pair combinations show X$\to$EN $>$ EN$\to$X (6.3--7.9pp), consistent with English as the representation anchor.
429	    \item \textbf{SAE Jaccard analysis}: Mid-layer conflict features are significantly more shared across languages (Jaccard = 0.28) than late-layer features (Jaccard = 0.12, $p = 0.008$), consistent with language-universal mid-layer encoding diverging during late-layer transition.
430	    \item \textbf{Steering asymmetry}: Causal intervention via both probes and SAE features reproduces the directional asymmetry, ruling out statistical artifacts and establishing that the asymmetry reflects the causal structure of conflict encoding.
431	\end{enumerate}
432	
433	H2 is not supported: the asymmetry direction is identical for EN$\leftrightarrow$ZH and EN$\leftrightarrow$JA (two typologically distinct pairs), and mid-layer feature sharing significantly exceeds late-layer sharing.
434	
435	\paragraph{Connection to CLEAR.}
436	Our findings provide a mechanistic account for CLEAR's observation that linguistic affinity determines entity-centric conflict resolution. The English-anchored representation structure means that languages with higher similarity to English have more overlapping conflict features, enabling more effective cross-lingual conflict transfer. The mid-layer language-universal encoding explains why conflict \emph{detection} is robust across languages, while the late-layer language-specific transition explains why conflict \emph{resolution} depends on linguistic similarity.
437	
438	\paragraph{Preliminary typological correlation.}
439	With only two language pairs (EN$\leftrightarrow$ZH, EN$\leftrightarrow$JA), we observe that steering effectiveness is directionally consistent with linguistic similarity (CLEAR similarity: EN--ZH 0.72, EN--JA 0.58; steering flip rate: 28.0\%, 23.0\%). This is suggestive but insufficient for statistical claims; validation with additional language pairs spanning diverse typological families is needed.
440	
441	\paragraph{Limitations.}
442	(1) Our analysis covers three architectures from the same dense transformer family; MoE architectures may exhibit different patterns. (2) The two language pairs tested are both Asian languages; European languages would strengthen typological diversity. (3) SAE analysis uses pre-trained SAEs on a base model, while probing uses instruct-tuned models; the cross-validation between tracks partially mitigates but does not eliminate this mismatch. (4) Steering flip rates of 17--35\% indicate that the linear/sparse approximation captures only part of the conflict mechanism; non-linear components remain unaddressed by our intervention framework.
443	
444	% ============================================================
445	% 6. CONCLUSION
446	% ============================================================
447	\section{Conclusion}
448	
449	We present the first mechanistic investigation of cross-lingual knowledge conflict signals in multilingual LLMs. Through residual stream probing across three architectures and two language pairs, SAE feature decomposition, and causal representation steering, we establish that: (1) conflict signals are linearly detectable in the residual stream with consistent cross-lingual transfer; (2) transfer is directionally asymmetric, favoring English as the anchor language; (3) conflict features are shared across languages in mid layers but diverge in late layers; and (4) manipulating these features causally shifts conflict resolution behavior. These findings support an English-anchored hypothesis for conflict encoding and provide mechanistic grounding for the role of linguistic affinity in cross-lingual conflict resolution.
450	
451	% ============================================================
452	% REFERENCES
453	% ============================================================
454	\bibliographystyle{plainnat}
455	
456	\begin{thebibliography}{10}
457	
458	\bibitem[Zhao et al.(2026)]{zhao2026clear}
459	Zhao, X., et al.
460	\newblock CLEAR: Cross-lingual entity-aware conflict resolution in multilingual language models.
461	\newblock In \emph{Proceedings of ACL 2026}, 2026.
462	
463	\bibitem[Wendler et al.(2024)]{wendler2024lost}
464	Wendler, C., et al.
465	\newblock Do llamas work in {E}nglish? {O}n the latent language of multilingual transformers.
466	\newblock In \emph{Proceedings of ACL 2024}, 2024.
467	
468	\bibitem[Kornblith et al.(2019)]{kornblith2019cka}
469	Kornblith, S., Norouzi, M., Lee, H., and Hinton, G.
470	\newblock Similarity of neural network representations revisited.
471	\newblock In \emph{Proceedings of ICML 2019}, 2019.
472	
473	\bibitem[Bricken et al.(2023)]{bricken2023monosemanticity}
474	Bricken, T., et al.
475	\newblock Towards monosemanticity: Decomposing language models with dictionary learning.
476	\newblock \emph{Transformer Circuits Thread}, 2023.
477	
478	\bibitem[Templeton et al.(2024)]{templeton2024scaling}
479	Templeton, A., et al.
480	\newblock Scaling monosemanticity: Extracting interpretable features from {C}laude 3 {S}onnet.
481	\newblock \emph{Transformer Circuits Thread}, 2024.
482	
483	\bibitem[Xie et al.(2024)]{xie2024conflictqa}
484	Xie, J., et al.
485	\newblock Adaptive chameleon or stubborn sloth: Revealing the behavior of large language models in knowledge conflicts.
486	\newblock In \emph{Proceedings of ICLR 2024}, 2024.
487	
488	\bibitem[Turner et al.(2024)]{turner2024steering}
489	Turner, A., et al.
490	\newblock Activation addition: Steering language models without optimization.
491	\newblock \emph{arXiv preprint arXiv:2308.10248}, 2024.
492	
493	\bibitem[Gao et al.(2024)]{gao2024spare}
494	Gao, L., et al.
495	\newblock SpARE: Sparse autoencoder representations for multi-hop reasoning and knowledge conflicts.
496	\newblock \emph{arXiv preprint}, 2024.
497	
498	\end{thebibliography}
499	
500	\end{document}
501	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19c6fcfd-77aa-4339-ba80-a4455733f007",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "3e89ee03-4488-405d-9a23-a42498b2e911",
  "sourceToolAssistantUUID": "19c6fcfd-77aa-4339-ba80-a4455733f007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-22T03:12:36.528Z_

Now let me read the review context and imagined experiments files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e89ee03-4488-405d-9a23-a42498b2e911",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsnucxBbjzoTknPj8ex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dcb4788-6a76-421d-8288-54adef9bd6f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhLcsok8GZnm1tgqPjd1gm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11956,
      "cache_read_input_tokens": 35050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11956,
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

_source line 35 · 2026-05-22T03:12:38.419Z_

<details open><summary>🔧 Tool call — Read · `toolu_015YV35Whjsduhpnh9ofgvSR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dcb4788-6a76-421d-8288-54adef9bd6f0",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsnucxBbjzoTknPj8ex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee6c3f61-d5fb-4447-a7b0-72f452f62499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhLcsok8GZnm1tgqPjd1gm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11956,
      "cache_read_input_tokens": 35050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11956,
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

_source line 36 · 2026-05-22T03:12:38.769Z_

<details><summary>↩ Tool result · `toolu_015YV35Whjsduhpnh9ofgvSR`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立：CLEAR entity-centric 冲突解决的首个机制解释。 C2 不对称性从 "consistent
2	  trend" 升级为 "statistically robust cross-architecture phenomenon"， 英语锚点假说（H1 变体）获三模型+多语言对支持。
3	  Track 2 SAE 提供 feature-level 证据补强因果叙事，部分缓解 RC8（无 intervention 的因果 claim）。 论文定位：mechanistic
4	  interpretability + cross-lingual，双社区贡献。
5	
6	  '
7	imagined_experiments:
8	- name: COMET 翻译质量验证（Llama 补全）
9	  plan_id: mvp_003
10	  description: wmt22-comet-da back-translation 验证 Llama ZH 翻译质量，补完 Qwen 已有结果
11	  expected_results:
12	    llama_test_total: 272
13	    llama_test_pass_rate_080: 0.22
14	    llama_test_mean_comet: 0.715
15	    llama_test_passed_mean_comet: 0.855
16	    llama_train_total: 1096
17	    llama_train_pass_rate_080: 0.24
18	    llama_train_mean_comet: 0.72
19	    llama_comet_tercile_low_acc: 0.648
20	    llama_comet_tercile_med_acc: 0.661
21	    llama_comet_tercile_high_acc: 0.632
22	    llama_comet_tercile_delta_high_low_pp: -1.6
23	    llama_comet_tercile_fisher_p: 0.82
24	    llama_comet_tercile_conclusion: not_confounder
25	  result_rationale: 'Llama 的翻译管线与 Qwen 共用同一 prompt template，back-translation COMET
26	    分布应高度相似。 best 档要求 Llama 复现 Qwen 的 not_confounder 结论——这在机制上合理： 冲突检测信号编码在残差流的语义层，而非表层翻译质量。
27	    如果翻译质量是 confounder，高 COMET 样本应有更高探针准确率， 但 Qwen 结果已呈反向（-5.64pp），Llama 预期同样反向或无差异。
28	    pass rate 略高于 Qwen（22% vs 18.5%）因 Llama 的 EN 数据比例更大， back-translation 到 EN 的回译质量天然更好。
29	
30	    '
31	  tables:
32	  - name: 'Table: COMET Tercile Ablation (Both Models)'
33	    columns:
34	    - Model
35	    - Tercile
36	    - N
37	    - COMET_mean
38	    - Bal_Acc
39	    - Delta_vs_Low
40	    rows:
41	    - - Llama-3.1-8B
42	      - Low
43	      - '91'
44	      - '0.582'
45	      - 64.8%
46	      - —
47	    - - Llama-3.1-8B
48	      - Med
49	      - '91'
50	      - '0.714'
51	      - 66.1%
52	      - +1.3pp
53	    - - Llama-3.1-8B
54	      - High
55	      - '90'
56	      - '0.821'
57	      - 63.2%
58	      - -1.6pp
59	    - - Qwen3-8B
60	      - Low
61	      - '56'
62	      - '0.585'
63	      - 66.4%
64	      - —
65	    - - Qwen3-8B
66	      - Med
67	      - '56'
68	      - '0.700'
69	      - 67.7%
70	      - +1.3pp
71	    - - Qwen3-8B
72	      - High
73	      - '56'
74	      - '0.816'
75	      - 60.7%
76	      - -5.6pp
77	  figures_description:
78	  - 散点图：per-sample COMET score (x) vs probe confidence (y)，两模型子图，拟合线斜率接近零或为负
79	  analysis: '两模型一致结论：翻译质量非 confounder。这允许放宽 COMET ≥0.80 门槛， 从而保留更多样本进入后续实验（特别是 plan_103
80	    多语言扩展时 JA 翻译质量可能更低）。 RC1 彻底关闭。
81	
82	    '
83	- name: 第三模型架构验证（Gemma-2-9B-IT）
84	  plan_id: plan_102
85	  description: 在 Gemma-2-9B-IT 上重复完整 4 方向探针实验 + bootstrap n=100 不对称性 CI
86	  expected_results:
87	    model: Gemma-2-9B-IT
88	    en_en_bal_acc: 0.764
89	    zh_zh_bal_acc: 0.708
90	    en_zh_bal_acc: 0.647
91	    zh_en_bal_acc: 0.726
92	    asymmetry_gap_pp: 7.9
93	    bootstrap_ci_95: '[2.3%, 13.8%]'
94	    bootstrap_significant: true
95	    bootstrap_positive_iterations: 99/100
96	    best_layer_en: 30
97	    best_layer_zh: 28
98	    best_layer_depth_ratio: 0.71
99	    mlp_en_zh_acc: 0.708
100	    mlp_gain_en_zh_pp: 6.1
101	    mlp_zh_en_acc: 0.739
102	    mlp_gain_zh_en_pp: 1.3
103	    permutation_test_p_en_en: <0.001
104	    permutation_test_p_zh_zh: <0.001
105	    permutation_test_p_en_zh: <0.001
106	    permutation_test_p_zh_en: <0.001
107	    token_overlap_jaccard_mean: 0.035
108	    token_overlap_correlation_p: 0.51
109	  result_rationale: 'best 档核心要求：第三模型显著不对称 + 3/3 方向一致。 Gemma-2-9B-IT 采用 GQA + sliding
110	    window attention，架构与 Llama（GQA）和 Qwen（GQA）有差异但同为 dense transformer。 within-language
111	    acc ~76%/71% 落在 [0.72, 0.82] 范围内—— Gemma 英语预训练数据占比高（Google 英语资源丰富），EN→EN 高于 Qwen/Llama
112	    合理。 ZH 训练数据比例低于 Qwen 但与 Llama 相当，ZH→ZH 在 Llama 附近。 不对称性 +7.9pp 在 [5, 12] 范围中段，CI
113	    排除零—— 这是 best 档与 mid 档的关键区别：Gemma 作为第三个 significant 模型将 C2 从 "2/3 显著" 提升到 "3/3
114	    显著"。 MLP 在 EN→ZH 方向增益 +6.1pp 位于 [3, 10] 范围—— 幅度介于 Llama（~4.7pp bootstrap-corrected）和
115	    Qwen（+2.3pp）之间， 支持"非线性成分与跨语言对齐程度负相关"的叙事： Gemma ZH 对齐弱于 Qwen 但强于 Llama 的 ZH 特化程度。
116	    peak layer depth ~71% 介于 Llama（88%）和 Qwen（67%）， 三模型 peak 均在 mid-to-upper layers
117	    但绝对位置有差异—— 提示冲突信号集中区域与模型的语言 transition layer 有关，非固定比例。
118	
119	    '
120	  tables:
121	  - name: 'Table: Cross-Architecture Probe Results Summary'
122	    columns:
123	    - Model
124	    - EN→EN
125	    - ZH→ZH
126	    - EN→ZH
127	    - ZH→EN
128	    - Asym_gap
129	    - CI_95
130	    - Sig?
131	    rows:
132	    - - Llama-3.1-8B
133	      - 77.1%
134	      - 71.2%
135	      - 64.1%
136	      - 71.3%
137	      - +7.2pp
138	      - '[1.1, 13.6]'
139	      - 'Yes'
140	    - - Qwen3-8B
141	      - 75.3%
142	      - 71.6%
143	      - 65.0%
144	      - 72.2%
145	      - +7.2pp
146	      - '[-1.2, 13.4]'
147	      - No (trend)
148	    - - Gemma-2-9B-IT
149	      - 76.4%
150	      - 70.8%
151	      - 64.7%
152	      - 72.6%
153	      - +7.9pp
154	      - '[2.3, 13.8]'
155	      - 'Yes'
156	  - name: 'Table: MLP Non-linearity Gain (EN→ZH weak direction)'
157	    columns:
158	    - Model
159	    - Linear
160	    - MLP
161	    - Gain_pp
162	    - Interpretation
163	    rows:
164	    - - Llama-3.1-8B
165	      - 64.1%
166	      - 68.8%
167	      - '+4.7'
168	      - Strong non-linear component
169	    - - Qwen3-8B
170	      - 65.0%
171	      - 67.3%
172	      - '+2.3'
173	      - Weak non-linear (better ZH alignment)
174	    - - Gemma-2-9B-IT
175	      - 64.7%
176	      - 70.8%
177	      - '+6.1'
178	      - Moderate non-linear component
179	  figures_description:
180	  - 三模型不对称性 forest plot：每模型一行，点估计 + 95% bootstrap CI，垂直虚线在 0pp
181	  - 三模型 layer-wise probe accuracy 曲线叠加图：EN→EN 和 ZH→EN 方向，x=layer depth ratio
182	  analysis: '三模型不对称性分别为 +7.2pp / +7.2pp / +7.9pp，效果量惊人一致（CV < 6%）。 2/3 统计显著（Llama
183	    borderline + Gemma clear），Qwen 方向一致但 CI 含零。 meta-analytic 角度：即使保守处理 Qwen 为 non-significant，
184	    三模型一致方向 + 效果量同质性本身就是强证据。 C2 升级为 "statistically robust cross-architecture phenomenon"。
185	    MLP 增益的跨模型梯度（Llama 4.7 > Gemma 6.1 > Qwen 2.3） 与各模型的中文预训练数据占比负相关—— 中文对齐越好，EN→ZH
186	    映射越线性，非线性残差越小。
187	
188	    '
189	- name: 多语言扩展 (EN↔JA)
190	  plan_id: plan_103
191	  description: EN↔JA 语言对完整探针实验，检验不对称性方向是否跨语言对一致
192	  expected_results:
193	    model: Qwen3-8B
194	    en_en_bal_acc_ja_split: 0.748
195	    ja_ja_bal_acc: 0.693
196	    en_ja_bal_acc: 0.618
197	    ja_en_bal_acc: 0.681
198	    asymmetry_gap_ja_pp: 6.3
199	    bootstrap_ci_95_ja: '[0.4%, 12.5%]'
200	    bootstrap_significant_ja: true
201	    model_2: Llama-3.1-8B
202	    llama_en_ja_bal_acc: 0.601
203	    llama_ja_en_bal_acc: 0.668
204	    llama_asymmetry_gap_ja_pp: 6.7
205	    llama_bootstrap_ci_95_ja: '[0.8%, 13.1%]'
206	    llama_bootstrap_significant_ja: true
207	    lang_pairs_validated: 2
208	    h1_h2_verdict: H1_supported
209	  result_rationale: 'best 档要求 ≥1 额外语言对方向一致（lang_pairs_validated ∈ [2,3]）。 EN↔JA 预测方向与
210	    EN↔ZH 相同（JA→EN > EN→JA）的原因： H1 英语锚点假说认为冲突信号以英语表征空间为锚点编码， 从任何非英语语言迁移到英语都更容易（"下坡"），反之更难（"上坡"）。
211	    JA 不对称性略小于 ZH（6.3pp vs 7.2pp）合理： 日语与英语的 typological distance 大于中文与英语（形态学复杂度更高、
212	    SOV 语序、多种书写系统），但 Qwen 的 JA 训练数据占比也较低， 两个因素部分抵消。关键是方向一致而非幅度完全相同。 JA 作为 CJK 系但与
213	    ZH typologically 不同的语言—— 如果 H2（language-pair-specific）成立，JA 应呈现不同 pattern； 方向一致强力支持
214	    H1。 JA within-language acc 略低于 ZH（69.3% vs 71.6%）， 因 Qwen 的 JA 训练数据少于 ZH，表征质量略弱。
215	
216	    '
217	  tables:
218	  - name: 'Table: Multi-Lingual Asymmetry Comparison'
219	    columns:
220	    - Model
221	    - Lang_Pair
222	    - X→EN
223	    - EN→X
224	    - Asym_gap
225	    - CI_95
226	    - Direction
227	    rows:
228	    - - Qwen3-8B
229	      - EN↔ZH
230	      - 72.2%
231	      - 65.0%
232	      - +7.2pp
233	      - '[-1.2, 13.4]'
234	      - ZH→EN wins
235	    - - Qwen3-8B
236	      - EN↔JA
237	      - 68.1%
238	      - 61.8%
239	      - +6.3pp
240	      - '[0.4, 12.5]'
241	      - JA→EN wins
242	    - - Llama-3.1-8B
243	      - EN↔ZH
244	      - 71.3%
245	      - 64.1%
246	      - +7.2pp
247	      - '[1.1, 13.6]'
248	      - ZH→EN wins
249	    - - Llama-3.1-8B
250	      - EN↔JA
251	      - 66.8%
252	      - 60.1%
253	      - +6.7pp
254	      - '[0.8, 13.1]'
255	      - JA→EN wins
256	  figures_description:
257	  - 2x2 子图矩阵（model x lang_pair），每个子图为 4 方向探针 accuracy bar chart + error bars
258	  - 不对称性 forest plot 扩展版：4 条（2 models x 2 lang_pairs），方向全部一致
259	  analysis: '4/4 model×lang_pair 组合不对称性方向一致（X→EN > EN→X）， 效果量在 6.3-7.9pp 范围内。这是 H1（English-anchored）的强证据：
260	    冲突信号以英语表征空间为锚点，X→EN 利用了"向锚点靠拢"的表征优势， EN→X 则需要额外的非线性映射。 H2（language-pair-specific）预测
261	    JA 和 ZH 应有不同 pattern——被数据否定。 审稿人 RC4（dataset diversity）部分缓解： 不再是"只有 EN-ZH 一个语言对"，而是"两个
262	    typologically 不同的亚洲语言"。 理想状态下 EN↔DE（印欧语系）也做，但 best 档 2 对已满足最低要求。
263	
264	    '
265	- name: Layer-wise CKA/SVCCA 分析
266	  plan_id: plan_104
267	  description: 逐层计算 EN vs ZH 激活的 CKA 和 SVCCA，量化跨语言表征相似度的层分布
268	  expected_results:
269	    models_analyzed:
270	    - Llama-3.1-8B
271	    - Qwen3-8B
272	    - Gemma-2-9B-IT
273	    cka_peak_similarity_layer_ratio_llama: 0.55
274	    cka_peak_similarity_layer_ratio_qwen: 0.5
275	    cka_peak_similarity_layer_ratio_gemma: 0.52
276	    cka_mid_layer_mean: 0.82
277	    cka_late_layer_mean: 0.54
278	    cka_mid_late_drop_significant: true
279	    svcca_mid_layer_mean: 0.78
280	    svcca_late_layer_mean: 0.48
281	    probe_peak_vs_cka_transition_correlation: -0.71
282	    language_transition_layer_ratio_llama: 0.75
283	    language_transition_layer_ratio_qwen: 0.6
284	    language_transition_layer_ratio_gemma: 0.68
285	  result_rationale: 'CKA/SVCCA 测量 EN 和 ZH 激活的表征几何相似度。 best 档下预期 pattern：mid-layers
286	    高相似度（~0.82）→ late-layers 急剧下降（~0.54）。 这与 "Lost in Multilinguality"（Wendler et
287	    al. 2024）的发现一致： LLM 在 mid-layers 形成 language-agnostic 概念表征， late-layers 发生 language
288	    transition 准备解码。 关键发现：probe accuracy peak 出现在 CKA 下降的"转折层"附近—— 冲突信号在 language-agnostic
289	    和 language-specific 表征的交界处最可检测。 这解释了为什么 ZH→EN 迁移更强：mid-layer 表征以英语为锚点， ZH→EN 方向"顺着"表征空间的自然结构，EN→ZH
290	    则逆行。 三模型 CKA 转折层位置不同（Llama ~55%, Qwen ~50%, Gemma ~52%）， 但 probe peak 与 CKA transition
291	    的关系一致（相关 r=-0.71）。
292	
293	    '
294	  tables:
295	  - name: 'Table: CKA Similarity by Layer Group'
296	    columns:
297	    - Model
298	    - Early (0-33%)
299	    - Mid (33-67%)
300	    - Late (67-100%)
301	    - Mid-Late Drop
302	    rows:
303	    - - Llama-3.1-8B
304	      - '0.71'
305	      - '0.83'
306	      - '0.52'
307	      - '-0.31'
308	    - - Qwen3-8B
309	      - '0.68'
310	      - '0.81'
311	      - '0.56'
312	      - '-0.25'
313	    - - Gemma-2-9B-IT
314	      - '0.70'
315	      - '0.82'
316	      - '0.53'
317	      - '-0.29'
318	  figures_description:
319	  - 三模型 CKA heatmap（layer x layer 对角线）叠加 probe accuracy 曲线，标注 transition zone
320	  - CKA/SVCCA 逐层曲线图 + probe accuracy 曲线双 y 轴叠加，标注 peak 和 transition 点
321	  analysis: 'CKA 分析为 C4（layer structure）提供量化基础，同时为 C2（asymmetry）提供机制解释： 不对称性源于 mid-layer
322	    表征空间的英语锚点特性。 probe peak 与 CKA transition 的相关性（r=-0.71）提示 冲突信号在表征空间从 language-universal
323	    向 language-specific 转变时最显著—— 这正是冲突"需要被解决"的时刻。 与 H1 一致：如果表征空间以英语为锚点， ZH/JA 样本在
324	    mid-layer 被"翻译"为英语表征后冲突信号变得可检测， 而英语样本到 ZH/JA 则需要额外的非线性映射来"离开"锚点。
325	
326	    '
327	- name: 探针权重可视化 + PCA
328	  plan_id: plan_109
329	  description: 最优层线性探针权重 PCA/t-SNE 可视化，展示冲突 vs 非冲突的跨语言表征结构
330	  expected_results:
331	    pca_variance_explained_2d: 0.38
332	    conflict_nonconflict_silhouette_en: 0.42
333	    conflict_nonconflict_silhouette_zh: 0.35
334	    cross_lingual_overlap_mid_layer: high
335	    cross_lingual_overlap_late_layer: low
336	    en_zh_conflict_centroid_cosine_mid: 0.78
337	    en_zh_conflict_centroid_cosine_late: 0.51
338	  result_rationale: 'PCA 可视化在 best 档下应呈现清晰的定性 pattern： mid-layer 中 EN 和 ZH 的冲突样本在
339	    PCA 空间中高度重叠（centroid cosine ~0.78）， 支持 H1 的 language-universal 冲突检测假说。 late-layer
340	    中两语言聚类开始分离（cosine 降至 ~0.51）， 对应 language transition 引入的 language-specific 成分。
341	    silhouette score EN > ZH（0.42 vs 0.35）反映英语探针分离度更好， 与 EN→EN > ZH→ZH 的准确率差异一致。 PCA
342	    只解释 ~38% 方差——冲突信号不是低维线性结构， 但方向性清晰可见，为论文提供直观的 Figure 1 素材。
343	
344	    '
345	  tables: []
346	  figures_description:
347	  - 2x3 PCA 子图矩阵（mid-layer vs late-layer x 3 models），颜色=conflict/non-conflict，形状=EN/ZH，椭圆标注
348	    95% CI
349	  - t-SNE 补充图：mid-layer 全样本，4 类（EN-conflict, EN-non, ZH-conflict, ZH-non）颜色区分
350	  analysis: '可视化为 mechanistic interpretability claim 提供必要的定性证据—— 审稿人需要"看到"冲突信号，而非仅看
351	    accuracy 数字。 mid-layer 重叠 + late-layer 分离的 pattern 与 CKA 分析（plan_104）互洽， 构成完整的层级叙事。
352	
353	    '
354	- name: Label noise ablation
355	  plan_id: plan_106
356	  description: 系统性注入 5%/10%/15%/20% label noise，测量 probe accuracy 下降曲线
357	  expected_results:
358	    noise_0_acc: 0.771
359	    noise_5_acc: 0.754
360	    noise_10_acc: 0.731
361	    noise_15_acc: 0.702
362	    noise_20_acc: 0.668
363	    degradation_slope_per_5pp: -2.6
364	    robustness_threshold_pp: 12
365	    cross_lingual_noise_sensitivity_en_zh: 1.3
366	    cross_lingual_noise_sensitivity_zh_en: 1.1
367	  result_rationale: '线性探针对 label noise 的鲁棒性直接关系到 verification pipeline 的可靠性。 best
368	    档下探针应表现出合理的渐进退化（非突变）， 因为残差流中的冲突信号是分布式编码的，少量 label noise 不会改变决策边界方向， 只会使其偏移。~2.6pp/5%
369	    noise 的斜率表明探针在 10% noise 下仍保持 >73%， 考虑到 verification pipeline 的 label error rate
370	    预估 <5%， 这提供了充分的安全裕度。 跨语言方向的 noise sensitivity 差异小（1.3x vs 1.1x） 表明 noise robustness
371	    是探针的固有属性而非语言依赖的。
372	
373	    '
374	  tables:
375	  - name: 'Table: Label Noise Robustness (Llama EN→EN)'
376	    columns:
377	    - Noise_Level
378	    - Bal_Acc
379	    - Delta_vs_0%
380	    - Relative_Drop
381	    rows:
382	    - - 0%
383	      - 77.1%
384	      - —
385	      - —
386	    - - 5%
387	      - 75.4%
388	      - -1.7pp
389	      - 2.2%
390	    - - 10%
391	      - 73.1%
392	      - -4.0pp
393	      - 5.2%
394	    - - 15%
395	      - 70.2%
396	      - -6.9pp
397	      - 8.9%
398	    - - 20%
399	      - 66.8%
400	      - -10.3pp
401	      - 13.4%
402	  figures_description:
403	  - Noise level (x) vs balanced accuracy (y) 曲线图，4 方向 x 3 模型叠加，error bars from 5-fold
404	  analysis: '探针在 ≤10% noise 下保持 >73% accuracy， 验证 pipeline label quality 的 error tolerance
405	    充裕。 此实验为 C1 的 robustness 声明提供支持，是补充性结果而非核心发现。 建议放入 Appendix 而非主文。
406	
407	    '
408	- name: Representation steering（干预实验）
409	  plan_id: plan_107
410	  description: 用探针方向作为 steering vector 干预残差流中的冲突信号，测量模型输出变化
411	  expected_results:
412	    llama_monolingual_en_flip_rate: 0.312
413	    llama_monolingual_zh_flip_rate: 0.268
414	    llama_cross_lingual_zh_en_flip_rate: 0.243
415	    llama_cross_lingual_en_zh_flip_rate: 0.178
416	    llama_flip_asymmetry_cross: 0.065
417	    qwen_monolingual_en_flip_rate: 0.289
418	    qwen_cross_lingual_zh_en_flip_rate: 0.221
419	    qwen_cross_lingual_en_zh_flip_rate: 0.192
420	    steering_alpha_optimal: 2.5
421	    steering_coherence_preserved_rate: 0.91
422	    parametric_to_contextual_shift_significant: true
423	  result_rationale: 'best 档下 representation steering 应产生有意义的输出翻转—— 这是 RC8（因果 claims
424	    without intervention）的直接缓解。 探针方向即为冲突信号的线性近似，沿该方向干预残差流 应推动模型从 parametric answer
425	    翻转到 contextual answer（或反之）。 monolingual flip rate ~30% 是合理的—— 不是所有样本都能被线性 steering
426	    翻转（非线性成分存在）， 但 30% 显著高于随机翻转基线（~5%）。 cross-lingual flip rate 低于 monolingual（ZH→EN
427	    24.3% vs EN 31.2%）， 且呈现与探针迁移相同的不对称性（ZH→EN 24.3% > EN→ZH 17.8%）， 从因果方向确认 C2：不对称性不仅是探针检测的统计
428	    pattern， 而是残差流中冲突信号编码的因果结构。 coherence preserved rate 91% 表明 steering 没有破坏模型的一般生成质量。
429	
430	    '
431	  tables:
432	  - name: 'Table: Steering Flip Rates by Direction'
433	    columns:
434	    - Model
435	    - Direction
436	    - Flip_Rate
437	    - Random_Baseline
438	    - Lift
439	    rows:
440	    - - Llama
441	      - EN (mono)
442	      - 31.2%
443	      - 4.8%
444	      - 6.5x
445	    - - Llama
446	      - ZH (mono)
447	      - 26.8%
448	      - 5.1%
449	      - 5.3x
450	    - - Llama
451	      - ZH→EN (cross)
452	      - 24.3%
453	      - 4.9%
454	      - 5.0x
455	    - - Llama
456	      - EN→ZH (cross)
457	      - 17.8%
458	      - 5.2%
459	      - 3.4x
460	    - - Qwen
461	      - EN (mono)
462	      - 28.9%
463	      - 4.6%
464	      - 6.3x
465	    - - Qwen
466	      - ZH→EN (cross)
467	      - 22.1%
468	      - 4.7%
469	      - 4.7x
470	    - - Qwen
471	      - EN→ZH (cross)
472	      - 19.2%
473	      - 5.0%
474	      - 3.8x
475	  figures_description:
476	  - Steering alpha sweep 曲线（alpha x flip_rate），标注 optimal alpha 和 coherence collapse
477	    threshold
478	  - Flip rate asymmetry bar chart：monolingual vs cross-lingual x 方向，error bars from
479	    bootstrap
480	  analysis: 'Steering 实验是 best 档的关键差异化实验—— 即使 Track 3 SAE steering 未完成，probe-based
481	    steering 已提供因果证据。 flip rate 不对称性（ZH→EN > EN→ZH）与探针迁移不对称性方向一致， 从相关性→因果性升级。 审稿人如果质疑
482	    "探针只证明信号可检测"（RC8）， steering 实验的回应是："干预该信号确实改变了冲突解决行为"。 放入主文 Section 4.3 作为 C2
483	    不对称性的因果证据。
484	
485	    '
486	- name: 更大数据集验证
487	  plan_id: plan_108
488	  description: 扩大 ConflictQA 采样至 2000+ samples per model，验证结论稳定性
489	  expected_results:
490	    sample_size_per_model: 2200
491	    llama_en_en_2k: 0.775
492	    llama_asymmetry_gap_2k_pp: 7.4
493	    llama_bootstrap_ci_2k: '[3.1%, 11.8%]'
494	    qwen_en_en_2k: 0.758
495	    qwen_asymmetry_gap_2k_pp: 7.0
496	    qwen_bootstrap_ci_2k: '[1.8%, 12.3%]'
497	    qwen_2k_significant: true
498	    ci_width_reduction_pct: 28
499	  result_rationale: '数据量翻倍后 CI 宽度应缩减约 1/√2 ≈ 28%。 best 档下关键收益：Qwen 的 CI 从 [-1.2%,
500	    13.4%] 收窄至 [1.8%, 12.3%]， 终于排除零——即 Qwen 也达到统计显著。 这是 best 档 "3/3 显著" 的另一条路径（与 Gemma
501	    第三模型互补）： 即使不加第三模型，Qwen 扩大样本后也能独立显著。 点估计基本不变（7.0pp vs 7.18pp），表明效果量是稳定的， 之前 Qwen
502	    不显著纯粹是 power 不足而非效果不存在。
503	
504	    '
505	  tables:
506	  - name: 'Table: Sample Size Scaling Effect on CI'
507	    columns:
508	    - Model
509	    - N
510	    - Asym_gap
511	    - CI_95
512	    - Significant?
513	    rows:
514	    - - Llama
515	      - ~1000
516	      - +7.2pp
517	      - '[1.1, 13.6]'
518	      - 'Yes'
519	    - - Llama
520	      - ~2200
521	      - +7.4pp
522	      - '[3.1, 11.8]'
523	      - 'Yes'
524	    - - Qwen
525	      - ~1000
526	      - +7.2pp
527	      - '[-1.2, 13.4]'
528	      - 'No'
529	    - - Qwen
530	      - ~2200
531	      - +7.0pp
532	      - '[1.8, 12.3]'
533	      - 'Yes'
534	  figures_description:
535	  - Power analysis 曲线：sample size (x) vs CI width (y)，标注 'significance threshold'
536	    水平线
537	  analysis: '数据扩展是 low-risk high-value 实验——不可能改变结论方向， 只会收窄 CI。best 档下 Qwen 达显著是锦上添花（因为
538	    Gemma 已提供第三模型）， 建议放入 Appendix 或 robustness 小节。
539	
540	    '
541	- name: Qwen-Scope SAE 冲突特征识别
542	  plan_id: plan_201
543	  description: 用 Qwen-Scope 预训练 SAE 在 Qwen3-8B-Base 上识别冲突相关的稀疏特征
544	  expected_results:
545	    sae_model: Qwen3-8B-Base
546	    sae_source: Qwen-Scope (pre-trained)
547	    format_adaptation: cloze/completion (base model compatible)
548	    total_features_analyzed: 65536
549	    conflict_candidate_features_mi_top: 128
550	    conflict_features_after_filtering: 47
551	    feature_sparsity_mean: 0.034
552	    feature_activation_conflict_vs_nonconflict_auroc: 0.81
553	    en_conflict_features_count: 38
554	    zh_conflict_features_count: 31
555	    shared_conflict_features_count: 18
556	    raw_jaccard_all_layers: 0.22
557	    mid_layer_jaccard: 0.28
558	    late_layer_jaccard: 0.12
559	    language_identity_feature_overlap: 0.03
560	  result_rationale: 'best 档要求 SAE 在 Qwen-Scope 上识别出跨语言共享 conflict feature（Jaccard
561	    > 0.15）。 Qwen-Scope 的 SAE 在 Qwen3-8B-Base 上预训练，特征空间已学到有意义的 monosemantic 分解。 conflict
562	    vs non-conflict 的 mutual-information feature selection（SpARE 方法） 应能从 65K 特征中筛选出
563	    ~128 个 candidate，进一步过滤到 ~47 个 robust 特征。 38 个 EN conflict features 和 31 个 ZH conflict
564	    features 中有 18 个共享（Jaccard ~0.22）， 在 [0.15, 0.35] 范围中段。 mid-layer Jaccard 0.28
565	    显著高于 late-layer 0.12—— 这是 H1 的 SAE-level 证据：mid-layer 冲突特征跨语言共享度高， late-layer
566	    语言分化后共享度下降。 language-identity feature overlap 仅 3% 表明 conflict features 不是 language
567	    features 的子集。 AUROC 0.81 表明 SAE 特征可以高质量区分冲突/非冲突样本， 与探针 accuracy ~75% 在同一水平（不同指标不直接可比但数量级一致）。
568	
569	    '
570	  tables:
571	  - name: 'Table: SAE Conflict Feature Summary'
572	    columns:
573	    - Category
574	    - Count
575	    - Sparsity
576	    - AUROC
577	    rows:
578	    - - EN-specific conflict
579	      - '20'
580	      - '0.031'
581	      - '0.79'
582	    - - ZH-specific conflict
583	      - '13'
584	      - '0.038'
585	      - '0.76'
586	    - - Cross-lingual shared
587	      - '18'
588	      - '0.033'
589	      - '0.84'
590	    - - Language-identity (control)
591	      - '42'
592	      - '0.025'
593	      - '0.52'
594	  figures_description:
595	  - SAE 特征激活 heatmap：top-47 conflict features x 样本（按 EN-conflict/EN-non/ZH-conflict/ZH-non
596	    排列）
597	  - Venn diagram：EN conflict features vs ZH conflict features，标注 Jaccard
598	  analysis: 'Track 2 初步结果成立——SAE 提供了 feature-level 的冲突编码证据。 shared conflict features
599	    的存在直接支持 H1（language-universal detection）， mid > late layer Jaccard 差异支持"冲突信号在
600	    mid-layer 跨语言共享、late-layer 分化"的叙事。 这部分缓解 RC8：SAE 特征激活模式提供了超越线性探针的 interpretability
601	    证据， 虽然不等同于 causal intervention，但结合 plan_107 的 steering 实验， 形成 "探针检测 → SAE 分解 →
602	    steering 干预" 的三层证据链。
603	
604	    '
605	- name: LangFIR 语言特征解耦
606	  plan_id: plan_202
607	  description: 用 LangFIR random-token filtering 识别 language-identity 特征，从冲突特征中排除
608	  expected_results:
609	    language_identity_features_identified: 42
610	    language_features_early_layer_concentration: 0.68
611	    conflict_features_mid_layer_concentration: 0.61
612	    overlap_conflict_language: 2
613	    overlap_rate: 0.043
614	    conflict_features_after_deconfounding: 45
615	    jaccard_change_after_deconfounding: '+0.02'
616	    layer_distribution_separation_p: 0.003
617	  result_rationale: 'LangFIR 通过 random-token filtering 识别在所有 token 上一致激活的 language-identity
618	    特征。 best 档下预期 42 个 language features 主要集中在 early layers（68%）， 而 conflict features
619	    集中在 mid layers（61%）——两类特征的层分布显著不同（p=0.003）。 仅 2 个 overlap（overlap rate 4.3%）表明
620	    conflict 不是 language 的子集， 从 SAE feature 层面证明冲突检测是语义级别的判断，而非语言识别的副产品。 deconfounding
621	    后 Jaccard 轻微上升（+0.02），因为移除 language-contaminated 特征 纯化了 conflict feature 集合。
622	
623	    '
624	  tables:
625	  - name: 'Table: Feature Type Layer Distribution'
626	    columns:
627	    - Feature_Type
628	    - Early (0-33%)
629	    - Mid (33-67%)
630	    - Late (67-100%)
631	    - Total
632	    rows:
633	    - - Language-identity
634	      - 29 (69%)
635	      - 9 (21%)
636	      - 4 (10%)
637	      - '42'
638	    - - Conflict (shared)
639	      - 2 (11%)
640	      - 11 (61%)
641	      - 5 (28%)
642	      - '18'
643	    - - Conflict (EN-only)
644	      - 1 (5%)
645	      - 10 (50%)
646	      - 9 (45%)
647	      - '20'
648	    - - Conflict (ZH-only)
649	      - 1 (8%)
650	      - 7 (54%)
651	      - 5 (38%)
652	      - '13'
653	  figures_description:
654	  - 层分布对比直方图：language-identity features vs conflict features 的 layer histogram 叠加
655	  analysis: 'LangFIR 控制实验为 C5 提供关键的 confound 排除： 冲突信号不是语言信号的 epiphenomenon。 层分布分离（early
656	    vs mid）与 plan_104 的 CKA 分析互洽—— early layers 做语言识别，mid layers 做语义/冲突判断。
657	
658	    '
659	- name: Cross-lingual feature Jaccard 分析
660	  plan_id: plan_203
661	  description: mid-layer vs late-layer conflict feature 跨语言 Jaccard 对比，检验 H1 vs H2
662	  expected_results:
663	    mid_layer_jaccard: 0.28
664	    late_layer_jaccard: 0.12
665	    jaccard_difference: 0.16
666	    paired_permutation_test_p: 0.008
667	    h1_vs_h2_verdict: H1_supported
668	    per_layer_jaccard_peak_ratio: 0.48
669	    per_layer_jaccard_trough_ratio: 0.88
670	  result_rationale: 'H1 预测 mid-layer Jaccard >> late-layer Jaccard， H2 预测无显著差异或 mid
671	    < late。 best 档下 mid 0.28 vs late 0.12，差异 0.16，permutation test p=0.008 < 0.05。
672	    这是 H1 的定量确认：冲突特征在 mid-layers 跨语言高度共享， 在 late-layers（language transition 后）显著分化。
673	    Jaccard peak 在 ~48% depth（mid-layer），trough 在 ~88% depth（late-layer）， 与 CKA transition
674	    zone（plan_104）和 probe peak（plan_102）时间线吻合。 三条独立证据线（CKA 表征相似度、probe accuracy、SAE
675	    feature Jaccard） 收敛在相同的层级叙事上，大幅增强可信度。
676	
677	    '
678	  tables:
679	  - name: 'Table: Layer-Group Jaccard Summary'
680	    columns:
681	    - Layer_Group
682	    - EN_features
683	    - ZH_features
684	    - Shared
685	    - Jaccard
686	    - 95% CI
687	    rows:
688	    - - Early (0-33%)
689	      - '3'
690	      - '3'
691	      - '1'
692	      - '0.20'
693	      - '[0.04, 0.41]'
694	    - - Mid (33-67%)
695	      - '21'
696	      - '18'
697	      - '8'
698	      - '0.28'
699	      - '[0.16, 0.42]'
700	    - - Late (67-100%)
701	      - '14'
702	      - '10'
703	      - '3'
704	      - '0.12'
705	      - '[0.03, 0.24]'
706	  figures_description:
707	  - 逐层 Jaccard 曲线 + 95% permutation CI 带，标注 H1/H2 预测区间
708	  - Mid vs Late Jaccard 散点图（每层一个点），对角线上方=H1，下方=H2
709	  analysis: 'Jaccard 分析是 H1 vs H2 检验的最直接证据。 p=0.008 在 0.05 显著性水平下 comfortably significant。
710	    结合 plan_104（CKA 层分布）和 plan_109（PCA 可视化）， 三条证据线一致支持 H1：冲突信号以英语为锚点在 mid-layer 跨语言共享编码。
711	    这是论文 Discussion 部分 H1 vs H2 resolution 的核心数据。
712	
713	    '
714	- name: Monolingual→cross-lingual steering transfer
715	  plan_id: plan_301
716	  description: 用 SpARE 英语冲突 SAE 特征做 cross-lingual steering，测量跨语言有效性
717	  expected_results:
718	    en_monolingual_em_c: 0.42
719	    en_monolingual_em_m: 0.31
720	    en_monolingual_flip_rate: 0.35
721	    zh_cross_lingual_em_c: 0.29
722	    zh_cross_lingual_em_m: 0.22
723	    zh_cross_lingual_flip_rate: 0.24
724	    transfer_efficiency: 0.69
725	    steering_asymmetry_en_to_zh: 0.24
726	    steering_asymmetry_zh_to_en: 0.31
727	    steering_asymmetry_gap: 0.07
728	    coherence_preserved_cross: 0.87
729	  result_rationale: 'SpARE 已在英语 monolingual 场景证明 SAE steering 对知识冲突有效。 best 档下 cross-lingual
730	    transfer efficiency ~69%（跨语言 flip rate / monolingual flip rate）， 表明英语冲突特征包含约 70%
731	    的跨语言可迁移信号。 30% 的 transfer loss 对应 late-layer language-specific 成分（与 Jaccard 分析一致）。
732	    steering asymmetry（EN→ZH 0.24 < ZH→EN 0.31）再次复现探针和 probe steering 的不对称方向， 从 SAE
733	    feature 干预层面第三次确认 C2。 coherence 87% 略低于 probe steering 的 91%—— SAE feature steering
734	    更 targeted 但也更 brittle（fewer degrees of freedom）。
735	
736	    '
737	  tables:
738	  - name: 'Table: SAE Steering Cross-Lingual Transfer'
739	    columns:
740	    - Condition
741	    - EM_C
742	    - EM_M
743	    - Flip_Rate
744	    - Coherence
745	    rows:
746	    - - EN mono (baseline)
747	      - '0.42'
748	      - '0.31'
749	      - 35.0%
750	      - '0.93'
751	    - - EN→ZH (cross)
752	      - '0.29'
753	      - '0.22'
754	      - 24.0%
755	      - '0.87'
756	    - - ZH→EN (cross)
757	      - '0.34'
758	      - '0.26'
759	      - 31.0%
760	      - '0.89'
761	    - - Random features (control)
762	      - '0.05'
763	      - '0.04'
764	      - 5.2%
765	      - '0.94'
766	  figures_description:
767	  - Steering 效果对比 bar chart：monolingual vs cross-lingual（两个方向），+ random control
768	  - Transfer efficiency vs layer depth 曲线：不同层 steering 的跨语言迁移效率
769	  analysis: 'SAE steering 提供了最直接的因果证据—— 操控特定 SAE 特征改变了跨语言冲突解决行为。 transfer efficiency
770	    69% 与 Jaccard 28% 的 scale 差异 是因为即使非 shared features 也可能有部分跨语言效应。 这是 Track 3 的核心贡献，结合
771	    Track 1 probing + Track 2 SAE 分析， 构成完整的 "检测→分解→干预" 三轨证据。
772	
773	    '
774	- name: Cross-lingual-specific steering
775	  plan_id: plan_302
776	  description: 用 Track 2 跨语言特有特征构建 steering vectors，对比 monolingual features 效果
777	  expected_results:
778	    shared_feature_steering_flip_rate: 0.28
779	    en_only_feature_steering_flip_rate_on_zh: 0.11
780	    zh_only_feature_steering_flip_rate_on_en: 0.09
781	    shared_vs_specific_lift: 2.7
782	    combined_steering_flip_rate: 0.33
783	    combined_vs_shared_only_lift: 1.18
784	  result_rationale: '如果 H1 成立，shared features 的 cross-lingual steering 效果应显著优于 language-specific
785	    features。 best 档下 shared feature steering 0.28 vs specific features ~0.10，lift
786	    2.7x—— 强力支持冲突信号的跨语言共享编码假说。 combined steering（shared + specific）仅比 shared-only
787	    提升 18%， 表明 language-specific features 的增量贡献有限， 冲突解决的核心信号已被 shared features 捕获。
788	
789	    '
790	  tables:
791	  - name: 'Table: Feature Type Steering Comparison'
792	    columns:
793	    - Feature_Set
794	    - Target_Lang
795	    - Flip_Rate
796	    - vs_Shared
797	    rows:
798	    - - Shared (18 features)
799	      - ZH
800	      - 28.0%
801	      - 1.0x
802	    - - EN-only (20 features)
803	      - ZH
804	      - 11.0%
805	      - 0.39x
806	    - - ZH-only (13 features)
807	      - EN
808	      - 9.0%
809	      - 0.32x
810	    - - Combined (all 51)
811	      - ZH
812	      - 33.0%
813	      - 1.18x
814	  figures_description:
815	  - Feature-set ablation bar chart：4 条件 x flip rate，标注显著性星号
816	  analysis: 'Feature-set ablation 是 H1 最精细的因果检验： shared features 包含绝大部分跨语言 steering
817	    能力， language-specific features 贡献边际，combined 收益递减。 这与"冲突检测是 language-universal
818	    的，resolution 才是 language-specific 的"叙事完全一致。
819	
820	    '
821	- name: Typological steering correlation
822	  plan_id: plan_303
823	  description: 测试 steering 有效性与 CLEAR linguistic similarity metric 的相关性
824	  expected_results:
825	    lang_pairs_tested:
826	    - EN↔ZH
827	    - EN↔JA
828	    steering_effectiveness_en_zh: 0.28
829	    steering_effectiveness_en_ja: 0.23
830	    clear_similarity_en_zh: 0.72
831	    clear_similarity_en_ja: 0.58
832	    correlation_direction: positive
833	    note: 仅 2 个语言对，无法计算有意义的相关系数，仅报告方向一致性
834	  result_rationale: 'best 档下 lang_pairs_validated = 2，只有 EN↔ZH 和 EN↔JA 两对数据点。 两个点不足以计算
835	    Pearson r，但方向一致性有意义： CLEAR similarity 更高的 EN↔ZH（0.72）steering 效果更好（0.28 > 0.23），
836	    与 linguistic similarity → conflict resolution 的因果链方向一致。 这是 suggestive evidence
837	    而非 definitive proof—— 论文中应诚实限定为 "consistent with the hypothesis,  pending validation
838	    with additional language pairs"。 best 档的叙事不依赖此实验的强结论，而是用它作为 future work 的 pilot
839	    data。
840	
841	    '
842	  tables:
843	  - name: 'Table: Steering vs Linguistic Similarity'
844	    columns:
845	    - Lang_Pair
846	    - CLEAR_Similarity
847	    - Steering_Flip_Rate
848	    - Probe_Asymmetry
849	    rows:
850	    - - EN↔ZH
851	      - '0.72'
852	      - 28.0%
853	      - +7.2pp
854	    - - EN↔JA
855	      - '0.58'
856	      - 23.0%
857	      - +6.3pp
858	  figures_description:
859	  - 散点图（仅 2 点 + 趋势线虚线）：CLEAR similarity (x) vs steering flip rate (y)，标注 'n=2, directional
860	    only'
861	  analysis: 此实验在 best 档下只能提供方向性暗示。 论文定位为 Discussion 段落而非独立 claim， 明确标注 "preliminary,
862	    n=2" 并指向 future work（5+ 语言对验证）。 审稿人不会因 n=2 的相关分析扣分——前提是作者不 overclaim。
863	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee6c3f61-d5fb-4447-a7b0-72f452f62499",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "ed67c1cc-39bb-4aab-8337-54c308eabd0e",
  "sourceToolAssistantUUID": "ee6c3f61-d5fb-4447-a7b0-72f452f62499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T03:12:38.888Z_

<details open><summary>🔧 Tool call — Read · `toolu_0124tHpkt1Hk1QMn9C9U3cBo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed67c1cc-39bb-4aab-8337-54c308eabd0e",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsnucxBbjzoTknPj8ex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35ce6c57-ef53-487c-a2c4-bab4fd273e69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhLcsok8GZnm1tgqPjd1gm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11956,
      "cache_read_input_tokens": 35050,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 35050,
          "cache_creation_input_tokens": 11956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11956,
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

_source line 38 · 2026-05-22T03:12:39.203Z_

<details><summary>↩ Tool result · `toolu_0124tHpkt1Hk1QMn9C9U3cBo`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立：CLEAR entity-centric 冲突解决的首个机制解释。 C2 不对称性从 "consistent
3	  trend" 升级为 "statistically robust cross-architecture phenomenon"， 英语锚点假说（H1 变体）获三模型+多语言对支持。
4	  Track 2 SAE 提供 feature-level 证据补强因果叙事，部分缓解 RC8（无 intervention 的因果 claim）。 论文定位：mechanistic
5	  interpretability + cross-lingual，双社区贡献。
6	
7	  '
8	imagined_experiments:
9	- name: COMET 翻译质量验证（Llama 补全）
10	  plan_id: mvp_003
11	  description: wmt22-comet-da back-translation 验证 Llama ZH 翻译质量，补完 Qwen 已有结果
12	  expected_results:
13	    llama_test_total: 272
14	    llama_test_pass_rate_080: 0.22
15	    llama_test_mean_comet: 0.715
16	    llama_test_passed_mean_comet: 0.855
17	    llama_train_total: 1096
18	    llama_train_pass_rate_080: 0.24
19	    llama_train_mean_comet: 0.72
20	    llama_comet_tercile_low_acc: 0.648
21	    llama_comet_tercile_med_acc: 0.661
22	    llama_comet_tercile_high_acc: 0.632
23	    llama_comet_tercile_delta_high_low_pp: -1.6
24	    llama_comet_tercile_fisher_p: 0.82
25	    llama_comet_tercile_conclusion: not_confounder
26	  result_rationale: 'Llama 的翻译管线与 Qwen 共用同一 prompt template，back-translation COMET
27	    分布应高度相似。 best 档要求 Llama 复现 Qwen 的 not_confounder 结论——这在机制上合理： 冲突检测信号编码在残差流的语义层，而非表层翻译质量。
28	    如果翻译质量是 confounder，高 COMET 样本应有更高探针准确率， 但 Qwen 结果已呈反向（-5.64pp），Llama 预期同样反向或无差异。
29	    pass rate 略高于 Qwen（22% vs 18.5%）因 Llama 的 EN 数据比例更大， back-translation 到 EN 的回译质量天然更好。
30	
31	    '
32	  tables:
33	  - name: 'Table: COMET Tercile Ablation (Both Models)'
34	    columns:
35	    - Model
36	    - Tercile
37	    - N
38	    - COMET_mean
39	    - Bal_Acc
40	    - Delta_vs_Low
41	    rows:
42	    - - Llama-3.1-8B
43	      - Low
44	      - '91'
45	      - '0.582'
46	      - 64.8%
47	      - —
48	    - - Llama-3.1-8B
49	      - Med
50	      - '91'
51	      - '0.714'
52	      - 66.1%
53	      - +1.3pp
54	    - - Llama-3.1-8B
55	      - High
56	      - '90'
57	      - '0.821'
58	      - 63.2%
59	      - -1.6pp
60	    - - Qwen3-8B
61	      - Low
62	      - '56'
63	      - '0.585'
64	      - 66.4%
65	      - —
66	    - - Qwen3-8B
67	      - Med
68	      - '56'
69	      - '0.700'
70	      - 67.7%
71	      - +1.3pp
72	    - - Qwen3-8B
73	      - High
74	      - '56'
75	      - '0.816'
76	      - 60.7%
77	      - -5.6pp
78	  figures_description:
79	  - 散点图：per-sample COMET score (x) vs probe confidence (y)，两模型子图，拟合线斜率接近零或为负
80	  analysis: '两模型一致结论：翻译质量非 confounder。这允许放宽 COMET ≥0.80 门槛， 从而保留更多样本进入后续实验（特别是 plan_103
81	    多语言扩展时 JA 翻译质量可能更低）。 RC1 彻底关闭。
82	
83	    '
84	- name: 第三模型架构验证（Gemma-2-9B-IT）
85	  plan_id: plan_102
86	  description: 在 Gemma-2-9B-IT 上重复完整 4 方向探针实验 + bootstrap n=100 不对称性 CI
87	  expected_results:
88	    model: Gemma-2-9B-IT
89	    en_en_bal_acc: 0.764
90	    zh_zh_bal_acc: 0.708
91	    en_zh_bal_acc: 0.647
92	    zh_en_bal_acc: 0.726
93	    asymmetry_gap_pp: 7.9
94	    bootstrap_ci_95: '[2.3%, 13.8%]'
95	    bootstrap_significant: true
96	    bootstrap_positive_iterations: 99/100
97	    best_layer_en: 30
98	    best_layer_zh: 28
99	    best_layer_depth_ratio: 0.71
100	    mlp_en_zh_acc: 0.708
101	    mlp_gain_en_zh_pp: 6.1
102	    mlp_zh_en_acc: 0.739
103	    mlp_gain_zh_en_pp: 1.3
104	    permutation_test_p_en_en: <0.001
105	    permutation_test_p_zh_zh: <0.001
106	    permutation_test_p_en_zh: <0.001
107	    permutation_test_p_zh_en: <0.001
108	    token_overlap_jaccard_mean: 0.035
109	    token_overlap_correlation_p: 0.51
110	  result_rationale: 'best 档核心要求：第三模型显著不对称 + 3/3 方向一致。 Gemma-2-9B-IT 采用 GQA + sliding
111	    window attention，架构与 Llama（GQA）和 Qwen（GQA）有差异但同为 dense transformer。 within-language
112	    acc ~76%/71% 落在 [0.72, 0.82] 范围内—— Gemma 英语预训练数据占比高（Google 英语资源丰富），EN→EN 高于 Qwen/Llama
113	    合理。 ZH 训练数据比例低于 Qwen 但与 Llama 相当，ZH→ZH 在 Llama 附近。 不对称性 +7.9pp 在 [5, 12] 范围中段，CI
114	    排除零—— 这是 best 档与 mid 档的关键区别：Gemma 作为第三个 significant 模型将 C2 从 "2/3 显著" 提升到 "3/3
115	    显著"。 MLP 在 EN→ZH 方向增益 +6.1pp 位于 [3, 10] 范围—— 幅度介于 Llama（~4.7pp bootstrap-corrected）和
116	    Qwen（+2.3pp）之间， 支持"非线性成分与跨语言对齐程度负相关"的叙事： Gemma ZH 对齐弱于 Qwen 但强于 Llama 的 ZH 特化程度。
117	    peak layer depth ~71% 介于 Llama（88%）和 Qwen（67%）， 三模型 peak 均在 mid-to-upper layers
118	    但绝对位置有差异—— 提示冲突信号集中区域与模型的语言 transition layer 有关，非固定比例。
119	
120	    '
121	  tables:
122	  - name: 'Table: Cross-Architecture Probe Results Summary'
123	    columns:
124	    - Model
125	    - EN→EN
126	    - ZH→ZH
127	    - EN→ZH
128	    - ZH→EN
129	    - Asym_gap
130	    - CI_95
131	    - Sig?
132	    rows:
133	    - - Llama-3.1-8B
134	      - 77.1%
135	      - 71.2%
136	      - 64.1%
137	      - 71.3%
138	      - +7.2pp
139	      - '[1.1, 13.6]'
140	      - 'Yes'
141	    - - Qwen3-8B
142	      - 75.3%
143	      - 71.6%
144	      - 65.0%
145	      - 72.2%
146	      - +7.2pp
147	      - '[-1.2, 13.4]'
148	      - No (trend)
149	    - - Gemma-2-9B-IT
150	      - 76.4%
151	      - 70.8%
152	      - 64.7%
153	      - 72.6%
154	      - +7.9pp
155	      - '[2.3, 13.8]'
156	      - 'Yes'
157	  - name: 'Table: MLP Non-linearity Gain (EN→ZH weak direction)'
158	    columns:
159	    - Model
160	    - Linear
161	    - MLP
162	    - Gain_pp
163	    - Interpretation
164	    rows:
165	    - - Llama-3.1-8B
166	      - 64.1%
167	      - 68.8%
168	      - '+4.7'
169	      - Strong non-linear component
170	    - - Qwen3-8B
171	      - 65.0%
172	      - 67.3%
173	      - '+2.3'
174	      - Weak non-linear (better ZH alignment)
175	    - - Gemma-2-9B-IT
176	      - 64.7%
177	      - 70.8%
178	      - '+6.1'
179	      - Moderate non-linear component
180	  figures_description:
181	  - 三模型不对称性 forest plot：每模型一行，点估计 + 95% bootstrap CI，垂直虚线在 0pp
182	  - 三模型 layer-wise probe accuracy 曲线叠加图：EN→EN 和 ZH→EN 方向，x=layer depth ratio
183	  analysis: '三模型不对称性分别为 +7.2pp / +7.2pp / +7.9pp，效果量惊人一致（CV < 6%）。 2/3 统计显著（Llama
184	    borderline + Gemma clear），Qwen 方向一致但 CI 含零。 meta-analytic 角度：即使保守处理 Qwen 为 non-significant，
185	    三模型一致方向 + 效果量同质性本身就是强证据。 C2 升级为 "statistically robust cross-architecture phenomenon"。
186	    MLP 增益的跨模型梯度（Llama 4.7 > Gemma 6.1 > Qwen 2.3） 与各模型的中文预训练数据占比负相关—— 中文对齐越好，EN→ZH
187	    映射越线性，非线性残差越小。
188	
189	    '
190	- name: 多语言扩展 (EN↔JA)
191	  plan_id: plan_103
192	  description: EN↔JA 语言对完整探针实验，检验不对称性方向是否跨语言对一致
193	  expected_results:
194	    model: Qwen3-8B
195	    en_en_bal_acc_ja_split: 0.748
196	    ja_ja_bal_acc: 0.693
197	    en_ja_bal_acc: 0.618
198	    ja_en_bal_acc: 0.681
199	    asymmetry_gap_ja_pp: 6.3
200	    bootstrap_ci_95_ja: '[0.4%, 12.5%]'
201	    bootstrap_significant_ja: true
202	    model_2: Llama-3.1-8B
203	    llama_en_ja_bal_acc: 0.601
204	    llama_ja_en_bal_acc: 0.668
205	    llama_asymmetry_gap_ja_pp: 6.7
206	    llama_bootstrap_ci_95_ja: '[0.8%, 13.1%]'
207	    llama_bootstrap_significant_ja: true
208	    lang_pairs_validated: 2
209	    h1_h2_verdict: H1_supported
210	  result_rationale: 'best 档要求 ≥1 额外语言对方向一致（lang_pairs_validated ∈ [2,3]）。 EN↔JA 预测方向与
211	    EN↔ZH 相同（JA→EN > EN→JA）的原因： H1 英语锚点假说认为冲突信号以英语表征空间为锚点编码， 从任何非英语语言迁移到英语都更容易（"下坡"），反之更难（"上坡"）。
212	    JA 不对称性略小于 ZH（6.3pp vs 7.2pp）合理： 日语与英语的 typological distance 大于中文与英语（形态学复杂度更高、
213	    SOV 语序、多种书写系统），但 Qwen 的 JA 训练数据占比也较低， 两个因素部分抵消。关键是方向一致而非幅度完全相同。 JA 作为 CJK 系但与
214	    ZH typologically 不同的语言—— 如果 H2（language-pair-specific）成立，JA 应呈现不同 pattern； 方向一致强力支持
215	    H1。 JA within-language acc 略低于 ZH（69.3% vs 71.6%）， 因 Qwen 的 JA 训练数据少于 ZH，表征质量略弱。
216	
217	    '
218	  tables:
219	  - name: 'Table: Multi-Lingual Asymmetry Comparison'
220	    columns:
221	    - Model
222	    - Lang_Pair
223	    - X→EN
224	    - EN→X
225	    - Asym_gap
226	    - CI_95
227	    - Direction
228	    rows:
229	    - - Qwen3-8B
230	      - EN↔ZH
231	      - 72.2%
232	      - 65.0%
233	      - +7.2pp
234	      - '[-1.2, 13.4]'
235	      - ZH→EN wins
236	    - - Qwen3-8B
237	      - EN↔JA
238	      - 68.1%
239	      - 61.8%
240	      - +6.3pp
241	      - '[0.4, 12.5]'
242	      - JA→EN wins
243	    - - Llama-3.1-8B
244	      - EN↔ZH
245	      - 71.3%
246	      - 64.1%
247	      - +7.2pp
248	      - '[1.1, 13.6]'
249	      - ZH→EN wins
250	    - - Llama-3.1-8B
251	      - EN↔JA
252	      - 66.8%
253	      - 60.1%
254	      - +6.7pp
255	      - '[0.8, 13.1]'
256	      - JA→EN wins
257	  figures_description:
258	  - 2x2 子图矩阵（model x lang_pair），每个子图为 4 方向探针 accuracy bar chart + error bars
259	  - 不对称性 forest plot 扩展版：4 条（2 models x 2 lang_pairs），方向全部一致
260	  analysis: '4/4 model×lang_pair 组合不对称性方向一致（X→EN > EN→X）， 效果量在 6.3-7.9pp 范围内。这是 H1（English-anchored）的强证据：
261	    冲突信号以英语表征空间为锚点，X→EN 利用了"向锚点靠拢"的表征优势， EN→X 则需要额外的非线性映射。 H2（language-pair-specific）预测
262	    JA 和 ZH 应有不同 pattern——被数据否定。 审稿人 RC4（dataset diversity）部分缓解： 不再是"只有 EN-ZH 一个语言对"，而是"两个
263	    typologically 不同的亚洲语言"。 理想状态下 EN↔DE（印欧语系）也做，但 best 档 2 对已满足最低要求。
264	
265	    '
266	- name: Layer-wise CKA/SVCCA 分析
267	  plan_id: plan_104
268	  description: 逐层计算 EN vs ZH 激活的 CKA 和 SVCCA，量化跨语言表征相似度的层分布
269	  expected_results:
270	    models_analyzed:
271	    - Llama-3.1-8B
272	    - Qwen3-8B
273	    - Gemma-2-9B-IT
274	    cka_peak_similarity_layer_ratio_llama: 0.55
275	    cka_peak_similarity_layer_ratio_qwen: 0.5
276	    cka_peak_similarity_layer_ratio_gemma: 0.52
277	    cka_mid_layer_mean: 0.82
278	    cka_late_layer_mean: 0.54
279	    cka_mid_late_drop_significant: true
280	    svcca_mid_layer_mean: 0.78
281	    svcca_late_layer_mean: 0.48
282	    probe_peak_vs_cka_transition_correlation: -0.71
283	    language_transition_layer_ratio_llama: 0.75
284	    language_transition_layer_ratio_qwen: 0.6
285	    language_transition_layer_ratio_gemma: 0.68
286	  result_rationale: 'CKA/SVCCA 测量 EN 和 ZH 激活的表征几何相似度。 best 档下预期 pattern：mid-layers
287	    高相似度（~0.82）→ late-layers 急剧下降（~0.54）。 这与 "Lost in Multilinguality"（Wendler et
288	    al. 2024）的发现一致： LLM 在 mid-layers 形成 language-agnostic 概念表征， late-layers 发生 language
289	    transition 准备解码。 关键发现：probe accuracy peak 出现在 CKA 下降的"转折层"附近—— 冲突信号在 language-agnostic
290	    和 language-specific 表征的交界处最可检测。 这解释了为什么 ZH→EN 迁移更强：mid-layer 表征以英语为锚点， ZH→EN 方向"顺着"表征空间的自然结构，EN→ZH
291	    则逆行。 三模型 CKA 转折层位置不同（Llama ~55%, Qwen ~50%, Gemma ~52%）， 但 probe peak 与 CKA transition
292	    的关系一致（相关 r=-0.71）。
293	
294	    '
295	  tables:
296	  - name: 'Table: CKA Similarity by Layer Group'
297	    columns:
298	    - Model
299	    - Early (0-33%)
300	    - Mid (33-67%)
301	    - Late (67-100%)
302	    - Mid-Late Drop
303	    rows:
304	    - - Llama-3.1-8B
305	      - '0.71'
306	      - '0.83'
307	      - '0.52'
308	      - '-0.31'
309	    - - Qwen3-8B
310	      - '0.68'
311	      - '0.81'
312	      - '0.56'
313	      - '-0.25'
314	    - - Gemma-2-9B-IT
315	      - '0.70'
316	      - '0.82'
317	      - '0.53'
318	      - '-0.29'
319	  figures_description:
320	  - 三模型 CKA heatmap（layer x layer 对角线）叠加 probe accuracy 曲线，标注 transition zone
321	  - CKA/SVCCA 逐层曲线图 + probe accuracy 曲线双 y 轴叠加，标注 peak 和 transition 点
322	  analysis: 'CKA 分析为 C4（layer structure）提供量化基础，同时为 C2（asymmetry）提供机制解释： 不对称性源于 mid-layer
323	    表征空间的英语锚点特性。 probe peak 与 CKA transition 的相关性（r=-0.71）提示 冲突信号在表征空间从 language-universal
324	    向 language-specific 转变时最显著—— 这正是冲突"需要被解决"的时刻。 与 H1 一致：如果表征空间以英语为锚点， ZH/JA 样本在
325	    mid-layer 被"翻译"为英语表征后冲突信号变得可检测， 而英语样本到 ZH/JA 则需要额外的非线性映射来"离开"锚点。
326	
327	    '
328	- name: 探针权重可视化 + PCA
329	  plan_id: plan_109
330	  description: 最优层线性探针权重 PCA/t-SNE 可视化，展示冲突 vs 非冲突的跨语言表征结构
331	  expected_results:
332	    pca_variance_explained_2d: 0.38
333	    conflict_nonconflict_silhouette_en: 0.42
334	    conflict_nonconflict_silhouette_zh: 0.35
335	    cross_lingual_overlap_mid_layer: high
336	    cross_lingual_overlap_late_layer: low
337	    en_zh_conflict_centroid_cosine_mid: 0.78
338	    en_zh_conflict_centroid_cosine_late: 0.51
339	  result_rationale: 'PCA 可视化在 best 档下应呈现清晰的定性 pattern： mid-layer 中 EN 和 ZH 的冲突样本在
340	    PCA 空间中高度重叠（centroid cosine ~0.78）， 支持 H1 的 language-universal 冲突检测假说。 late-layer
341	    中两语言聚类开始分离（cosine 降至 ~0.51）， 对应 language transition 引入的 language-specific 成分。
342	    silhouette score EN > ZH（0.42 vs 0.35）反映英语探针分离度更好， 与 EN→EN > ZH→ZH 的准确率差异一致。 PCA
343	    只解释 ~38% 方差——冲突信号不是低维线性结构， 但方向性清晰可见，为论文提供直观的 Figure 1 素材。
344	
345	    '
346	  tables: []
347	  figures_description:
348	  - 2x3 PCA 子图矩阵（mid-layer vs late-layer x 3 models），颜色=conflict/non-conflict，形状=EN/ZH，椭圆标注
349	    95% CI
350	  - t-SNE 补充图：mid-layer 全样本，4 类（EN-conflict, EN-non, ZH-conflict, ZH-non）颜色区分
351	  analysis: '可视化为 mechanistic interpretability claim 提供必要的定性证据—— 审稿人需要"看到"冲突信号，而非仅看
352	    accuracy 数字。 mid-layer 重叠 + late-layer 分离的 pattern 与 CKA 分析（plan_104）互洽， 构成完整的层级叙事。
353	
354	    '
355	- name: Label noise ablation
356	  plan_id: plan_106
357	  description: 系统性注入 5%/10%/15%/20% label noise，测量 probe accuracy 下降曲线
358	  expected_results:
359	    noise_0_acc: 0.771
360	    noise_5_acc: 0.754
361	    noise_10_acc: 0.731
362	    noise_15_acc: 0.702
363	    noise_20_acc: 0.668
364	    degradation_slope_per_5pp: -2.6
365	    robustness_threshold_pp: 12
366	    cross_lingual_noise_sensitivity_en_zh: 1.3
367	    cross_lingual_noise_sensitivity_zh_en: 1.1
368	  result_rationale: '线性探针对 label noise 的鲁棒性直接关系到 verification pipeline 的可靠性。 best
369	    档下探针应表现出合理的渐进退化（非突变）， 因为残差流中的冲突信号是分布式编码的，少量 label noise 不会改变决策边界方向， 只会使其偏移。~2.6pp/5%
370	    noise 的斜率表明探针在 10% noise 下仍保持 >73%， 考虑到 verification pipeline 的 label error rate
371	    预估 <5%， 这提供了充分的安全裕度。 跨语言方向的 noise sensitivity 差异小（1.3x vs 1.1x） 表明 noise robustness
372	    是探针的固有属性而非语言依赖的。
373	
374	    '
375	  tables:
376	  - name: 'Table: Label Noise Robustness (Llama EN→EN)'
377	    columns:
378	    - Noise_Level
379	    - Bal_Acc
380	    - Delta_vs_0%
381	    - Relative_Drop
382	    rows:
383	    - - 0%
384	      - 77.1%
385	      - —
386	      - —
387	    - - 5%
388	      - 75.4%
389	      - -1.7pp
390	      - 2.2%
391	    - - 10%
392	      - 73.1%
393	      - -4.0pp
394	      - 5.2%
395	    - - 15%
396	      - 70.2%
397	      - -6.9pp
398	      - 8.9%
399	    - - 20%
400	      - 66.8%
401	      - -10.3pp
402	      - 13.4%
403	  figures_description:
404	  - Noise level (x) vs balanced accuracy (y) 曲线图，4 方向 x 3 模型叠加，error bars from 5-fold
405	  analysis: '探针在 ≤10% noise 下保持 >73% accuracy， 验证 pipeline label quality 的 error tolerance
406	    充裕。 此实验为 C1 的 robustness 声明提供支持，是补充性结果而非核心发现。 建议放入 Appendix 而非主文。
407	
408	    '
409	- name: Representation steering（干预实验）
410	  plan_id: plan_107
411	  description: 用探针方向作为 steering vector 干预残差流中的冲突信号，测量模型输出变化
412	  expected_results:
413	    llama_monolingual_en_flip_rate: 0.312
414	    llama_monolingual_zh_flip_rate: 0.268
415	    llama_cross_lingual_zh_en_flip_rate: 0.243
416	    llama_cross_lingual_en_zh_flip_rate: 0.178
417	    llama_flip_asymmetry_cross: 0.065
418	    qwen_monolingual_en_flip_rate: 0.289
419	    qwen_cross_lingual_zh_en_flip_rate: 0.221
420	    qwen_cross_lingual_en_zh_flip_rate: 0.192
421	    steering_alpha_optimal: 2.5
422	    steering_coherence_preserved_rate: 0.91
423	    parametric_to_contextual_shift_significant: true
424	  result_rationale: 'best 档下 representation steering 应产生有意义的输出翻转—— 这是 RC8（因果 claims
425	    without intervention）的直接缓解。 探针方向即为冲突信号的线性近似，沿该方向干预残差流 应推动模型从 parametric answer
426	    翻转到 contextual answer（或反之）。 monolingual flip rate ~30% 是合理的—— 不是所有样本都能被线性 steering
427	    翻转（非线性成分存在）， 但 30% 显著高于随机翻转基线（~5%）。 cross-lingual flip rate 低于 monolingual（ZH→EN
428	    24.3% vs EN 31.2%）， 且呈现与探针迁移相同的不对称性（ZH→EN 24.3% > EN→ZH 17.8%）， 从因果方向确认 C2：不对称性不仅是探针检测的统计
429	    pattern， 而是残差流中冲突信号编码的因果结构。 coherence preserved rate 91% 表明 steering 没有破坏模型的一般生成质量。
430	
431	    '
432	  tables:
433	  - name: 'Table: Steering Flip Rates by Direction'
434	    columns:
435	    - Model
436	    - Direction
437	    - Flip_Rate
438	    - Random_Baseline
439	    - Lift
440	    rows:
441	    - - Llama
442	      - EN (mono)
443	      - 31.2%
444	      - 4.8%
445	      - 6.5x
446	    - - Llama
447	      - ZH (mono)
448	      - 26.8%
449	      - 5.1%
450	      - 5.3x
451	    - - Llama
452	      - ZH→EN (cross)
453	      - 24.3%
454	      - 4.9%
455	      - 5.0x
456	    - - Llama
457	      - EN→ZH (cross)
458	      - 17.8%
459	      - 5.2%
460	      - 3.4x
461	    - - Qwen
462	      - EN (mono)
463	      - 28.9%
464	      - 4.6%
465	      - 6.3x
466	    - - Qwen
467	      - ZH→EN (cross)
468	      - 22.1%
469	      - 4.7%
470	      - 4.7x
471	    - - Qwen
472	      - EN→ZH (cross)
473	      - 19.2%
474	      - 5.0%
475	      - 3.8x
476	  figures_description:
477	  - Steering alpha sweep 曲线（alpha x flip_rate），标注 optimal alpha 和 coherence collapse
478	    threshold
479	  - Flip rate asymmetry bar chart：monolingual vs cross-lingual x 方向，error bars from
480	    bootstrap
481	  analysis: 'Steering 实验是 best 档的关键差异化实验—— 即使 Track 3 SAE steering 未完成，probe-based
482	    steering 已提供因果证据。 flip rate 不对称性（ZH→EN > EN→ZH）与探针迁移不对称性方向一致， 从相关性→因果性升级。 审稿人如果质疑
483	    "探针只证明信号可检测"（RC8）， steering 实验的回应是："干预该信号确实改变了冲突解决行为"。 放入主文 Section 4.3 作为 C2
484	    不对称性的因果证据。
485	
486	    '
487	- name: 更大数据集验证
488	  plan_id: plan_108
489	  description: 扩大 ConflictQA 采样至 2000+ samples per model，验证结论稳定性
490	  expected_results:
491	    sample_size_per_model: 2200
492	    llama_en_en_2k: 0.775
493	    llama_asymmetry_gap_2k_pp: 7.4
494	    llama_bootstrap_ci_2k: '[3.1%, 11.8%]'
495	    qwen_en_en_2k: 0.758
496	    qwen_asymmetry_gap_2k_pp: 7.0
497	    qwen_bootstrap_ci_2k: '[1.8%, 12.3%]'
498	    qwen_2k_significant: true
499	    ci_width_reduction_pct: 28
500	  result_rationale: '数据量翻倍后 CI 宽度应缩减约 1/√2 ≈ 28%。 best 档下关键收益：Qwen 的 CI 从 [-1.2%,
501	    13.4%] 收窄至 [1.8%, 12.3%]， 终于排除零——即 Qwen 也达到统计显著。 这是 best 档 "3/3 显著" 的另一条路径（与 Gemma
502	    第三模型互补）： 即使不加第三模型，Qwen 扩大样本后也能独立显著。 点估计基本不变（7.0pp vs 7.18pp），表明效果量是稳定的， 之前 Qwen
503	    不显著纯粹是 power 不足而非效果不存在。
504	
505	    '
506	  tables:
507	  - name: 'Table: Sample Size Scaling Effect on CI'
508	    columns:
509	    - Model
510	    - N
511	    - Asym_gap
512	    - CI_95
513	    - Significant?
514	    rows:
515	    - - Llama
516	      - ~1000
517	      - +7.2pp
518	      - '[1.1, 13.6]'
519	      - 'Yes'
520	    - - Llama
521	      - ~2200
522	      - +7.4pp
523	      - '[3.1, 11.8]'
524	      - 'Yes'
525	    - - Qwen
526	      - ~1000
527	      - +7.2pp
528	      - '[-1.2, 13.4]'
529	      - 'No'
530	    - - Qwen
531	      - ~2200
532	      - +7.0pp
533	      - '[1.8, 12.3]'
534	      - 'Yes'
535	  figures_description:
536	  - Power analysis 曲线：sample size (x) vs CI width (y)，标注 'significance threshold'
537	    水平线
538	  analysis: '数据扩展是 low-risk high-value 实验——不可能改变结论方向， 只会收窄 CI。best 档下 Qwen 达显著是锦上添花（因为
539	    Gemma 已提供第三模型）， 建议放入 Appendix 或 robustness 小节。
540	
541	    '
542	- name: Qwen-Scope SAE 冲突特征识别
543	  plan_id: plan_201
544	  description: 用 Qwen-Scope 预训练 SAE 在 Qwen3-8B-Base 上识别冲突相关的稀疏特征
545	  expected_results:
546	    sae_model: Qwen3-8B-Base
547	    sae_source: Qwen-Scope (pre-trained)
548	    format_adaptation: cloze/completion (base model compatible)
549	    total_features_analyzed: 65536
550	    conflict_candidate_features_mi_top: 128
551	    conflict_features_after_filtering: 47
552	    feature_sparsity_mean: 0.034
553	    feature_activation_conflict_vs_nonconflict_auroc: 0.81
554	    en_conflict_features_count: 38
555	    zh_conflict_features_count: 31
556	    shared_conflict_features_count: 18
557	    raw_jaccard_all_layers: 0.22
558	    mid_layer_jaccard: 0.28
559	    late_layer_jaccard: 0.12
560	    language_identity_feature_overlap: 0.03
561	  result_rationale: 'best 档要求 SAE 在 Qwen-Scope 上识别出跨语言共享 conflict feature（Jaccard
562	    > 0.15）。 Qwen-Scope 的 SAE 在 Qwen3-8B-Base 上预训练，特征空间已学到有意义的 monosemantic 分解。 conflict
563	    vs non-conflict 的 mutual-information feature selection（SpARE 方法） 应能从 65K 特征中筛选出
564	    ~128 个 candidate，进一步过滤到 ~47 个 robust 特征。 38 个 EN conflict features 和 31 个 ZH conflict
565	    features 中有 18 个共享（Jaccard ~0.22）， 在 [0.15, 0.35] 范围中段。 mid-layer Jaccard 0.28
566	    显著高于 late-layer 0.12—— 这是 H1 的 SAE-level 证据：mid-layer 冲突特征跨语言共享度高， late-layer
567	    语言分化后共享度下降。 language-identity feature overlap 仅 3% 表明 conflict features 不是 language
568	    features 的子集。 AUROC 0.81 表明 SAE 特征可以高质量区分冲突/非冲突样本， 与探针 accuracy ~75% 在同一水平（不同指标不直接可比但数量级一致）。
569	
570	    '
571	  tables:
572	  - name: 'Table: SAE Conflict Feature Summary'
573	    columns:
574	    - Category
575	    - Count
576	    - Sparsity
577	    - AUROC
578	    rows:
579	    - - EN-specific conflict
580	      - '20'
581	      - '0.031'
582	      - '0.79'
583	    - - ZH-specific conflict
584	      - '13'
585	      - '0.038'
586	      - '0.76'
587	    - - Cross-lingual shared
588	      - '18'
589	      - '0.033'
590	      - '0.84'
591	    - - Language-identity (control)
592	      - '42'
593	      - '0.025'
594	      - '0.52'
595	  figures_description:
596	  - SAE 特征激活 heatmap：top-47 conflict features x 样本（按 EN-conflict/EN-non/ZH-conflict/ZH-non
597	    排列）
598	  - Venn diagram：EN conflict features vs ZH conflict features，标注 Jaccard
599	  analysis: 'Track 2 初步结果成立——SAE 提供了 feature-level 的冲突编码证据。 shared conflict features
600	    的存在直接支持 H1（language-universal detection）， mid > late layer Jaccard 差异支持"冲突信号在
601	    mid-layer 跨语言共享、late-layer 分化"的叙事。 这部分缓解 RC8：SAE 特征激活模式提供了超越线性探针的 interpretability
602	    证据， 虽然不等同于 causal intervention，但结合 plan_107 的 steering 实验， 形成 "探针检测 → SAE 分解 →
603	    steering 干预" 的三层证据链。
604	
605	    '
606	- name: LangFIR 语言特征解耦
607	  plan_id: plan_202
608	  description: 用 LangFIR random-token filtering 识别 language-identity 特征，从冲突特征中排除
609	  expected_results:
610	    language_identity_features_identified: 42
611	    language_features_early_layer_concentration: 0.68
612	    conflict_features_mid_layer_concentration: 0.61
613	    overlap_conflict_language: 2
614	    overlap_rate: 0.043
615	    conflict_features_after_deconfounding: 45
616	    jaccard_change_after_deconfounding: '+0.02'
617	    layer_distribution_separation_p: 0.003
618	  result_rationale: 'LangFIR 通过 random-token filtering 识别在所有 token 上一致激活的 language-identity
619	    特征。 best 档下预期 42 个 language features 主要集中在 early layers（68%）， 而 conflict features
620	    集中在 mid layers（61%）——两类特征的层分布显著不同（p=0.003）。 仅 2 个 overlap（overlap rate 4.3%）表明
621	    conflict 不是 language 的子集， 从 SAE feature 层面证明冲突检测是语义级别的判断，而非语言识别的副产品。 deconfounding
622	    后 Jaccard 轻微上升（+0.02），因为移除 language-contaminated 特征 纯化了 conflict feature 集合。
623	
624	    '
625	  tables:
626	  - name: 'Table: Feature Type Layer Distribution'
627	    columns:
628	    - Feature_Type
629	    - Early (0-33%)
630	    - Mid (33-67%)
631	    - Late (67-100%)
632	    - Total
633	    rows:
634	    - - Language-identity
635	      - 29 (69%)
636	      - 9 (21%)
637	      - 4 (10%)
638	      - '42'
639	    - - Conflict (shared)
640	      - 2 (11%)
641	      - 11 (61%)
642	      - 5 (28%)
643	      - '18'
644	    - - Conflict (EN-only)
645	      - 1 (5%)
646	      - 10 (50%)
647	      - 9 (45%)
648	      - '20'
649	    - - Conflict (ZH-only)
650	      - 1 (8%)
651	      - 7 (54%)
652	      - 5 (38%)
653	      - '13'
654	  figures_description:
655	  - 层分布对比直方图：language-identity features vs conflict features 的 layer histogram 叠加
656	  analysis: 'LangFIR 控制实验为 C5 提供关键的 confound 排除： 冲突信号不是语言信号的 epiphenomenon。 层分布分离（early
657	    vs mid）与 plan_104 的 CKA 分析互洽—— early layers 做语言识别，mid layers 做语义/冲突判断。
658	
659	    '
660	- name: Cross-lingual feature Jaccard 分析
661	  plan_id: plan_203
662	  description: mid-layer vs late-layer conflict feature 跨语言 Jaccard 对比，检验 H1 vs H2
663	  expected_results:
664	    mid_layer_jaccard: 0.28
665	    late_layer_jaccard: 0.12
666	    jaccard_difference: 0.16
667	    paired_permutation_test_p: 0.008
668	    h1_vs_h2_verdict: H1_supported
669	    per_layer_jaccard_peak_ratio: 0.48
670	    per_layer_jaccard_trough_ratio: 0.88
671	  result_rationale: 'H1 预测 mid-layer Jaccard >> late-layer Jaccard， H2 预测无显著差异或 mid
672	    < late。 best 档下 mid 0.28 vs late 0.12，差异 0.16，permutation test p=0.008 < 0.05。
673	    这是 H1 的定量确认：冲突特征在 mid-layers 跨语言高度共享， 在 late-layers（language transition 后）显著分化。
674	    Jaccard peak 在 ~48% depth（mid-layer），trough 在 ~88% depth（late-layer）， 与 CKA transition
675	    zone（plan_104）和 probe peak（plan_102）时间线吻合。 三条独立证据线（CKA 表征相似度、probe accuracy、SAE
676	    feature Jaccard） 收敛在相同的层级叙事上，大幅增强可信度。
677	
678	    '
679	  tables:
680	  - name: 'Table: Layer-Group Jaccard Summary'
681	    columns:
682	    - Layer_Group
683	    - EN_features
684	    - ZH_features
685	    - Shared
686	    - Jaccard
687	    - 95% CI
688	    rows:
689	    - - Early (0-33%)
690	      - '3'
691	      - '3'
692	      - '1'
693	      - '0.20'
694	      - '[0.04, 0.41]'
695	    - - Mid (33-67%)
696	      - '21'
697	      - '18'
698	      - '8'
699	      - '0.28'
700	      - '[0.16, 0.42]'
701	    - - Late (67-100%)
702	      - '14'
703	      - '10'
704	      - '3'
705	      - '0.12'
706	      - '[0.03, 0.24]'
707	  figures_description:
708	  - 逐层 Jaccard 曲线 + 95% permutation CI 带，标注 H1/H2 预测区间
709	  - Mid vs Late Jaccard 散点图（每层一个点），对角线上方=H1，下方=H2
710	  analysis: 'Jaccard 分析是 H1 vs H2 检验的最直接证据。 p=0.008 在 0.05 显著性水平下 comfortably significant。
711	    结合 plan_104（CKA 层分布）和 plan_109（PCA 可视化）， 三条证据线一致支持 H1：冲突信号以英语为锚点在 mid-layer 跨语言共享编码。
712	    这是论文 Discussion 部分 H1 vs H2 resolution 的核心数据。
713	
714	    '
715	- name: Monolingual→cross-lingual steering transfer
716	  plan_id: plan_301
717	  description: 用 SpARE 英语冲突 SAE 特征做 cross-lingual steering，测量跨语言有效性
718	  expected_results:
719	    en_monolingual_em_c: 0.42
720	    en_monolingual_em_m: 0.31
721	    en_monolingual_flip_rate: 0.35
722	    zh_cross_lingual_em_c: 0.29
723	    zh_cross_lingual_em_m: 0.22
724	    zh_cross_lingual_flip_rate: 0.24
725	    transfer_efficiency: 0.69
726	    steering_asymmetry_en_to_zh: 0.24
727	    steering_asymmetry_zh_to_en: 0.31
728	    steering_asymmetry_gap: 0.07
729	    coherence_preserved_cross: 0.87
730	  result_rationale: 'SpARE 已在英语 monolingual 场景证明 SAE steering 对知识冲突有效。 best 档下 cross-lingual
731	    transfer efficiency ~69%（跨语言 flip rate / monolingual flip rate）， 表明英语冲突特征包含约 70%
732	    的跨语言可迁移信号。 30% 的 transfer loss 对应 late-layer language-specific 成分（与 Jaccard 分析一致）。
733	    steering asymmetry（EN→ZH 0.24 < ZH→EN 0.31）再次复现探针和 probe steering 的不对称方向， 从 SAE
734	    feature 干预层面第三次确认 C2。 coherence 87% 略低于 probe steering 的 91%—— SAE feature steering
735	    更 targeted 但也更 brittle（fewer degrees of freedom）。
736	
737	    '
738	  tables:
739	  - name: 'Table: SAE Steering Cross-Lingual Transfer'
740	    columns:
741	    - Condition
742	    - EM_C
743	    - EM_M
744	    - Flip_Rate
745	    - Coherence
746	    rows:
747	    - - EN mono (baseline)
748	      - '0.42'
749	      - '0.31'
750	      - 35.0%
751	      - '0.93'
752	    - - EN→ZH (cross)
753	      - '0.29'
754	      - '0.22'
755	      - 24.0%
756	      - '0.87'
757	    - - ZH→EN (cross)
758	      - '0.34'
759	      - '0.26'
760	      - 31.0%
761	      - '0.89'
762	    - - Random features (control)
763	      - '0.05'
764	      - '0.04'
765	      - 5.2%
766	      - '0.94'
767	  figures_description:
768	  - Steering 效果对比 bar chart：monolingual vs cross-lingual（两个方向），+ random control
769	  - Transfer efficiency vs layer depth 曲线：不同层 steering 的跨语言迁移效率
770	  analysis: 'SAE steering 提供了最直接的因果证据—— 操控特定 SAE 特征改变了跨语言冲突解决行为。 transfer efficiency
771	    69% 与 Jaccard 28% 的 scale 差异 是因为即使非 shared features 也可能有部分跨语言效应。 这是 Track 3 的核心贡献，结合
772	    Track 1 probing + Track 2 SAE 分析， 构成完整的 "检测→分解→干预" 三轨证据。
773	
774	    '
775	- name: Cross-lingual-specific steering
776	  plan_id: plan_302
777	  description: 用 Track 2 跨语言特有特征构建 steering vectors，对比 monolingual features 效果
778	  expected_results:
779	    shared_feature_steering_flip_rate: 0.28
780	    en_only_feature_steering_flip_rate_on_zh: 0.11
781	    zh_only_feature_steering_flip_rate_on_en: 0.09
782	    shared_vs_specific_lift: 2.7
783	    combined_steering_flip_rate: 0.33
784	    combined_vs_shared_only_lift: 1.18
785	  result_rationale: '如果 H1 成立，shared features 的 cross-lingual steering 效果应显著优于 language-specific
786	    features。 best 档下 shared feature steering 0.28 vs specific features ~0.10，lift
787	    2.7x—— 强力支持冲突信号的跨语言共享编码假说。 combined steering（shared + specific）仅比 shared-only
788	    提升 18%， 表明 language-specific features 的增量贡献有限， 冲突解决的核心信号已被 shared features 捕获。
789	
790	    '
791	  tables:
792	  - name: 'Table: Feature Type Steering Comparison'
793	    columns:
794	    - Feature_Set
795	    - Target_Lang
796	    - Flip_Rate
797	    - vs_Shared
798	    rows:
799	    - - Shared (18 features)
800	      - ZH
801	      - 28.0%
802	      - 1.0x
803	    - - EN-only (20 features)
804	      - ZH
805	      - 11.0%
806	      - 0.39x
807	    - - ZH-only (13 features)
808	      - EN
809	      - 9.0%
810	      - 0.32x
811	    - - Combined (all 51)
812	      - ZH
813	      - 33.0%
814	      - 1.18x
815	  figures_description:
816	  - Feature-set ablation bar chart：4 条件 x flip rate，标注显著性星号
817	  analysis: 'Feature-set ablation 是 H1 最精细的因果检验： shared features 包含绝大部分跨语言 steering
818	    能力， language-specific features 贡献边际，combined 收益递减。 这与"冲突检测是 language-universal
819	    的，resolution 才是 language-specific 的"叙事完全一致。
820	
821	    '
822	- name: Typological steering correlation
823	  plan_id: plan_303
824	  description: 测试 steering 有效性与 CLEAR linguistic similarity metric 的相关性
825	  expected_results:
826	    lang_pairs_tested:
827	    - EN↔ZH
828	    - EN↔JA
829	    steering_effectiveness_en_zh: 0.28
830	    steering_effectiveness_en_ja: 0.23
831	    clear_similarity_en_zh: 0.72
832	    clear_similarity_en_ja: 0.58
833	    correlation_direction: positive
834	    note: 仅 2 个语言对，无法计算有意义的相关系数，仅报告方向一致性
835	  result_rationale: 'best 档下 lang_pairs_validated = 2，只有 EN↔ZH 和 EN↔JA 两对数据点。 两个点不足以计算
836	    Pearson r，但方向一致性有意义： CLEAR similarity 更高的 EN↔ZH（0.72）steering 效果更好（0.28 > 0.23），
837	    与 linguistic similarity → conflict resolution 的因果链方向一致。 这是 suggestive evidence
838	    而非 definitive proof—— 论文中应诚实限定为 "consistent with the hypothesis,  pending validation
839	    with additional language pairs"。 best 档的叙事不依赖此实验的强结论，而是用它作为 future work 的 pilot
840	    data。
841	
842	    '
843	  tables:
844	  - name: 'Table: Steering vs Linguistic Similarity'
845	    columns:
846	    - Lang_Pair
847	    - CLEAR_Similarity
848	    - Steering_Flip_Rate
849	    - Probe_Asymmetry
850	    rows:
851	    - - EN↔ZH
852	      - '0.72'
853	      - 28.0%
854	      - +7.2pp
855	    - - EN↔JA
856	      - '0.58'
857	      - 23.0%
858	      - +6.3pp
859	  figures_description:
860	  - 散点图（仅 2 点 + 趋势线虚线）：CLEAR similarity (x) vs steering flip rate (y)，标注 'n=2, directional
861	    only'
862	  analysis: 此实验在 best 档下只能提供方向性暗示。 论文定位为 Discussion 段落而非独立 claim， 明确标注 "preliminary,
863	    n=2" 并指向 future work（5+ 语言对验证）。 审稿人不会因 n=2 的相关分析扣分——前提是作者不 overclaim。
864	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35ce6c57-ef53-487c-a2c4-bab4fd273e69",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "2c7e29fc-a5db-4359-b14f-e01638fc37fb",
  "sourceToolAssistantUUID": "35ce6c57-ef53-487c-a2c4-bab4fd273e69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-22T03:12:42.918Z_

Now let me also check the experiment plan and source code to understand the actual implementation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c7e29fc-a5db-4359-b14f-e01638fc37fb",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsoMd8cUSNckuyPtGk7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b44c8669-2e16-453d-a5ae-663395984a9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eReLJfV15DUovZr7CgmHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32275,
      "cache_read_input_tokens": 47006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32275,
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

_source line 40 · 2026-05-22T03:12:44.368Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TTF5a8kRjKm8WiAdNgARQQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b44c8669-2e16-453d-a5ae-663395984a9a",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsoMd8cUSNckuyPtGk7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5beea99-7018-4904-8af7-b482ce65dd62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eReLJfV15DUovZr7CgmHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32275,
      "cache_read_input_tokens": 47006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32275,
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

_source line 41 · 2026-05-22T03:12:44.373Z_

<details><summary>↩ Tool result · `toolu_01TTF5a8kRjKm8WiAdNgARQQ`</summary>

```text
1	# Experiment Plan — clkc_mech_interp
2	# 最后更新: 2026-05-22
3	# 目标: ICLR 2027 (DDL ~2026-09-24)
4	
5	# ── MVP 实验（已完成/进行中）──
6	
7	- plan_id: mvp_001
8	  name: "双模型残差流探针 MVP"
9	  claim: "C1 (detectability) + C2 (asymmetry)"
10	  description: "Llama-3.1-8B + Qwen3-8B 双模型 EN/ZH 4方向探针迁移实验"
11	  priority: P0
12	  status: done
13	  registry_id:
14	    - mvp_probe_llama_v1
15	    - mvp_probe_v1
16	  gpu_hours: 8
17	  results_summary: |
18	    Llama EN→EN 77.1±1.2%, ZH→ZH 71.2±1.3%, EN→ZH 64.1±2.5%, ZH→EN 71.3±2.7%
19	    Qwen EN→EN 75.3±1.7%, ZH→ZH 71.6±1.8%, EN→ZH 65.0±2.7%, ZH→EN 72.2±2.6%
20	    不对称性: Llama +7.22pp, Qwen +7.19pp
21	
22	- plan_id: mvp_002
23	  name: "MLP vs Linear 探针对比"
24	  claim: "C3 (non-linearity)"
25	  description: "1-hidden-layer MLP 探针与线性探针对比，量化非线性成分"
26	  priority: P0
27	  status: done
28	  registry_id:
29	    - mlp_probe_llama
30	    - mlp_probe_qwen
31	  gpu_hours: 4
32	  results_summary: |
33	    Llama EN→ZH: Linear 59.6% → MLP 68.8% (+9.2pp) [single-seed 基线]
34	    Qwen EN→ZH: Linear 67.3% → MLP 69.6% (+2.3pp) [single-seed 基线]
35	    注意: bootstrap mean 线性基线更高 (Llama 64.1%), MLP 优势在 bootstrap 下约 +4.7pp
36	
37	- plan_id: mvp_003
38	  name: "COMET 翻译质量验证"
39	  claim: "RC1 (translation confound)"
40	  description: "wmt22-comet-da back-translation 验证 ZH 翻译质量，threshold ≥ 0.80"
41	  priority: P0
42	  status: running
43	  gpu_hours: 6
44	  depends_on: []
45	
46	# ── 统计修正（P0，Reviewer 发现的 CI 混用问题）──
47	
48	- plan_id: plan_099
49	  name: "训练集 bootstrap 不对称性 CI"
50	  claim: "C2 (asymmetry) — 统计修正"
51	  description: |
52	    用 n=100 训练集 bootstrap 逐迭代计算不对称性，提取 paired CI。
53	    Llama: +7.22pp CI [1.1%, 13.6%] 排除零(borderline); Qwen: +7.18pp CI [-1.2%, 13.4%] 含零。
54	  priority: P0
55	  status: done
56	  gpu_hours: 0
57	  depends_on: [mvp_001]
58	  results_summary: |
59	    Llama: +7.22pp, 95% CI [1.1%, 13.6%], 98/100 iterations positive — significant
60	    Qwen: +7.18pp, 95% CI [-1.2%, 13.4%], 96/100 iterations positive — trending
61	    效果量跨架构高度一致 (7.22 vs 7.18), 第三模型(Gemma)将决定C2强度
62	
63	# ── Track 1: Cross-Lingual Probing (P0) ──
64	
65	- plan_id: plan_101
66	  name: "Token overlap 分析"
67	  claim: "C2 (asymmetry) — RC2 排除"
68	  description: |
69	    计算 EN-ZH 输入的 token overlap ratio，分析共享 token 对探针迁移的贡献。
70	    Per-sample Jaccard + correlation with probe correctness + tercile 分析。
71	  priority: P0
72	  status: done
73	  gpu_hours: 0
74	  depends_on: [mvp_001]
75	  results_summary: |
76	    RC2 排除。Per-sample Jaccard 3-4%, Qwen 无相关 (p>0.4),
77	    Llama 负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。
78	    共享 token 不驱动迁移，迁移发生在语义表示层。
79	
80	- plan_id: plan_102
81	  name: "第三模型架构验证"
82	  claim: "C2 (asymmetry) — RC3 排除"
83	  description: |
84	    在第三个模型架构（Mistral-7B-Instruct-v0.3 或 Gemma-2-9B-IT）上重复完整探针实验。
85	    验证 ~7.2pp 不对称性是否跨架构一致。
86	    包含: verify → translate → collect activations → train probe → bootstrap n=100。
87	  priority: P0
88	  status: planned
89	  gpu_hours: 20
90	  depends_on: []
91	
92	- plan_id: plan_103
93	  name: "多语言扩展 (EN↔JA)"
94	  claim: "C2 (asymmetry) — RC4 + H1/H2 检验"
95	  description: |
96	    扩展到 EN↔JA 语言对，测试不对称性是否与 typological distance 相关。
97	    JA 作为 CJK 系但与 ZH typologically 不同的语言，可检验 H2 的语言距离编码假设。
98	    如果 EN↔JA 不对称性方向和幅度与 EN↔ZH 类似 → 支持 H1 (English-anchored)
99	    如果差异显著 → 支持 H2 (language-pair-specific)
100	  priority: P0
101	  status: planned
102	  gpu_hours: 20
103	  depends_on: []
104	
105	- plan_id: plan_104
106	  name: "Layer-wise CKA/SVCCA"
107	  claim: "C4 (layer structure)"
108	  description: |
109	    在每一层计算 EN vs ZH 激活的 CKA (Centered Kernel Alignment) 和 SVCCA，
110	    量化跨语言表征相似度随层变化的 pattern。
111	    验证 "Lost in Multilinguality" 的 language transition 是否影响冲突信号迁移。
112	  priority: P0
113	  status: planned
114	  gpu_hours: 4
115	  depends_on: [mvp_001]
116	
117	- plan_id: plan_105
118	  name: "COMET 分段 ablation"
119	  claim: "C1 (detectability) — RC1 深化 + COMET gate 判定"
120	  description: |
121	    按 COMET 分数将翻译分为 high/med/low 三档（tertile），用已有探针评估各档 balanced acc。
122	    判断标准: High vs Low tertile acc 差异 < 5pp 且 p > 0.05 → 翻译质量非 confounder → 放宽阈值。
123	    背景: Qwen test back-translation COMET mean=0.70, pass rate 18.45% at ≥0.80。
124	    Back-translation 两步翻译天然拉低 COMET，需 ablation 实证判断是否影响探针。
125	  priority: P0
126	  status: done
127	  gpu_hours: 0
128	  depends_on: [mvp_003]
129	  results_summary: |
130	    Qwen test (n=168): Low COMET 66.35%, Med 67.69%, High 60.71%
131	    Delta(High-Low)=-5.64pp (反向), Fisher p=0.695 → 翻译质量非 confounder
132	    Llama 待确认一致性
133	
134	# ── Track 1 扩展 (P1) ──
135	
136	- plan_id: plan_109
137	  name: "探针权重可视化 + PCA"
138	  claim: "C1 (detectability) + C4 (layer structure) — 定性证据"
139	  description: |
140	    对最优层的线性探针权重做 PCA / t-SNE 可视化，展示冲突 vs 非冲突样本的分布。
141	    跨语言对比：EN 和 ZH 的冲突表征在 PCA 空间中是否重叠？
142	    为 "mechanistic interpretability" claim 提供定性证据（不能只有准确率数字）。
143	  priority: P1
144	  status: planned
145	  gpu_hours: 0.5
146	  depends_on: [mvp_001]
147	
148	- plan_id: plan_106
149	  name: "Label noise ablation"
150	  claim: "C1 (detectability) — robustness"
151	  description: |
152	    系统性注入 5%/10%/15%/20% label noise，测量 probe accuracy 下降曲线。
153	    评估 verification pipeline 的 label error tolerance。
154	  priority: P1
155	  status: planned
156	  gpu_hours: 4
157	  depends_on: [mvp_001]
158	
159	- plan_id: plan_107
160	  name: "Representation steering (干预实验)"
161	  claim: "C2 (asymmetry) — RC8 因果证据"
162	  description: |
163	    用探针方向作为 steering vector，在残差流中干预冲突信号。
164	    测量干预后模型输出（parametric vs contextual answer）的变化。
165	    提供 C2 不对称性的因果证据（不仅是相关性）。
166	    如果 Track 3 SAE steering 无法完成，此实验是因果证据的唯一来源。
167	  priority: P0
168	  status: planned
169	  gpu_hours: 8
170	  depends_on: [mvp_001, plan_104]
171	
172	- plan_id: plan_108
173	  name: "更大数据集验证"
174	  claim: "C1 (detectability) — RC4 数据充分性"
175	  description: |
176	    扩大 ConflictQA 采样至 2000+ samples per model (当前 ~1000)。
177	    或引入其他知识冲突数据集（如 SQuAD-conflict, WebQuestions-conflict）。
178	  priority: P1
179	  status: planned
180	  gpu_hours: 12
181	  depends_on: []
182	
183	# ── Track 2: SAE Feature Analysis (P1-P2) ──
184	
185	- plan_id: plan_201
186	  name: "Qwen-Scope SAE 冲突特征识别"
187	  claim: "C5 (SAE features)"
188	  description: |
189	    用 Qwen-Scope 预训练 SAE (Qwen3-8B-Base) 分析冲突激活中的差异化特征。
190	    适配 cloze/completion 格式（base model 兼容）。
191	    SpARE mutual-information feature selection 方法。
192	  priority: P1
193	  status: planned
194	  gpu_hours: 16
195	  depends_on: [mvp_001]
196	
197	- plan_id: plan_202
198	  name: "LangFIR 语言特征解耦"
199	  claim: "C5 (SAE features) — 控制实验"
200	  description: |
201	    用 LangFIR random-token filtering 识别 language-identity 特征。
202	    从 SAE conflict features 中排除 language-identity 特征。
203	    验证 conflict features 和 language features 的层分布是否非重叠。
204	  priority: P1
205	  status: planned
206	  gpu_hours: 8
207	  depends_on: [plan_201]
208	
209	- plan_id: plan_203
210	  name: "Cross-lingual feature Jaccard 分析"
211	  claim: "C5 (SAE features) — H1 vs H2 检验"
212	  description: |
213	    计算 mid-layer vs late-layer conflict feature 的跨语言 Jaccard index。
214	    H1 预测: mid-layer Jaccard >> late-layer Jaccard
215	    H2 预测: 无显著差异或 mid < late
216	    Paired permutation test p < 0.05。
217	  priority: P1
218	  status: planned
219	  gpu_hours: 4
220	  depends_on: [plan_201, plan_202]
221	
222	# ── Track 3: Steering (P2) ──
223	
224	- plan_id: plan_301
225	  name: "Monolingual→cross-lingual steering transfer"
226	  claim: "C6 (steering)"
227	  description: |
228	    用 SpARE 的英语冲突特征做 cross-lingual steering。
229	    测量跨语言 steering 有效性 (EM_C, EM_M, flip rates)。
230	  priority: P2
231	  status: planned
232	  gpu_hours: 16
233	  depends_on: [plan_201, plan_203]
234	
235	- plan_id: plan_302
236	  name: "Cross-lingual-specific steering"
237	  claim: "C6 (steering)"
238	  description: |
239	    用 Track 2 发现的跨语言特有特征构建 steering vectors。
240	    对比与 monolingual features 的 steering 效果差异。
241	  priority: P2
242	  status: planned
243	  gpu_hours: 16
244	  depends_on: [plan_301]
245	
246	- plan_id: plan_303
247	  name: "Typological steering correlation"
248	  claim: "C6 (steering) — CLEAR 因果链接"
249	  description: |
250	    测试 steering 有效性是否与 CLEAR 的 linguistic similarity metric 相关。
251	    提供 linguistic similarity → conflict resolution 的因果（非仅相关）证据。
252	  priority: P2
253	  status: planned
254	  gpu_hours: 12
255	  depends_on: [plan_301, plan_103]
256	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5beea99-7018-4904-8af7-b482ce65dd62",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "e8e50644-68b8-4392-8ff3-4cd2c325bea3",
  "sourceToolAssistantUUID": "e5beea99-7018-4904-8af7-b482ce65dd62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-22T03:12:44.994Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01S3CJ7i3MaBgNCLG6FBafXg`</summary>

```json
{
  "pattern": "artifacts/clkc_code/src/**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8e50644-68b8-4392-8ff3-4cd2c325bea3",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsoMd8cUSNckuyPtGk7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89562f7b-4d4f-4af0-86b5-1ff492140806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eReLJfV15DUovZr7CgmHV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32275,
      "cache_read_input_tokens": 47006,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32275
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 47006,
          "cache_creation_input_tokens": 32275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32275,
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

_source line 43 · 2026-05-22T03:12:45.106Z_

<details><summary>↩ Tool result · `toolu_01S3CJ7i3MaBgNCLG6FBafXg`</summary>

```text
artifacts/clkc_code/src/train_probe.py
artifacts/clkc_code/src/validate_translation.py
artifacts/clkc_code/src/collect_activations.py
artifacts/clkc_code/src/supplement_sampling.py
artifacts/clkc_code/src/verify_parametric_knowledge.py
artifacts/clkc_code/src/supplement_sampling_2.py
artifacts/clkc_code/src/translate_to_zh.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89562f7b-4d4f-4af0-86b5-1ff492140806",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "96ce7cea-4373-4569-8a9f-5c0dfbcf728e",
  "sourceToolAssistantUUID": "89562f7b-4d4f-4af0-86b5-1ff492140806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-22T03:12:48.622Z_

<details open><summary>🔧 Tool call — Read · `toolu_017nGLvoieFTBN5n5jQf9224`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/src/train_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96ce7cea-4373-4569-8a9f-5c0dfbcf728e",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGson6ni44tn6MW3bxSr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a831b117-3af4-4143-8e47-5b074ecab1a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V71eX2YipfjQaXvM7f9jQx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4757,
      "cache_read_input_tokens": 79281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4757,
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

_source line 45 · 2026-05-22T03:12:48.635Z_

<details><summary>↩ Tool result · `toolu_017nGLvoieFTBN5n5jQf9224`</summary>

```text
1	"""Train per-layer linear probes and evaluate cross-lingual transfer.
2	
3	Loads .pt activation files from collect_activations.py, trains a logistic
4	regression probe per layer, and evaluates on four transfer directions:
5	EN->EN, ZH->ZH, EN->ZH, ZH->EN.
6	
7	Statistical tests:
8	  - Binomial test: is each accuracy significantly above chance (50%)?
9	  - Permutation test (1000 iters): is the layer-wise peak accuracy above noise?
10	
11	Output:
12	  - Console table with per-layer accuracy + p-values
13	  - probe_results.json   (structured results)
14	  - probe_accuracy_by_layer.png  (visualization)
15	
16	Dependencies: torch, numpy, sklearn, scipy, matplotlib
17	"""
18	
19	import argparse
20	import json
21	from pathlib import Path
22	
23	import matplotlib.pyplot as plt
24	import numpy as np
25	import torch
26	from scipy import stats
27	from sklearn.linear_model import LogisticRegression
28	from sklearn.preprocessing import StandardScaler
29	
30	
31	DIRECTIONS = ["EN→EN", "ZH→ZH", "EN→ZH", "ZH→EN"]
32	
33	
34	def load_activations(path: str) -> dict:
35	    data = torch.load(path, map_location="cpu", weights_only=True)
36	    n_train = data["split_sizes"]["train"]
37	    return {
38	        "train_X": data["activations"][:n_train],   # (N_train, L, D)
39	        "train_y": data["labels"][:n_train],          # (N_train,)
40	        "test_X": data["activations"][n_train:],
41	        "test_y": data["labels"][n_train:],
42	    }
43	
44	
45	def train_and_eval(
46	    train_X: np.ndarray,
47	    train_y: np.ndarray,
48	    test_X: np.ndarray,
49	    test_y: np.ndarray,
50	) -> float:
51	    """Train logistic regression, return accuracy on test set."""
52	    scaler = StandardScaler()
53	    train_X = scaler.fit_transform(train_X)
54	    test_X = scaler.transform(test_X)
55	    clf = LogisticRegression(max_iter=1000, solver="lbfgs")
56	    clf.fit(train_X, train_y)
57	    return clf.score(test_X, test_y)
58	
59	
60	def binomial_p(accuracy: float, n: int, chance: float = 0.5) -> float:
61	    """One-sided binomial test: P(X >= k) under chance."""
62	    k = int(round(accuracy * n))
63	    return stats.binomtest(k, n, chance, alternative="greater").pvalue
64	
65	
66	def permutation_test(
67	    train_X: np.ndarray,
68	    train_y: np.ndarray,
69	    test_X: np.ndarray,
70	    test_y: np.ndarray,
71	    observed_acc: float,
72	    n_perm: int = 1000,
73	    rng_seed: int = 42,
74	) -> float:
75	    """Permutation test: fraction of shuffled-label runs with acc >= observed."""
76	    rng = np.random.RandomState(rng_seed)
77	    count = 0
78	    for _ in range(n_perm):
79	        perm_y = rng.permutation(train_y)
80	        acc = train_and_eval(train_X, perm_y, test_X, test_y)
81	        if acc >= observed_acc:
82	            count += 1
83	    return count / n_perm
84	
85	
86	def run_direction(
87	    train_data: dict,
88	    test_data: dict,
89	    num_layers: int,
90	    direction_name: str,
91	    run_permutation: bool = True,
92	) -> list[dict]:
93	    """Evaluate probe for every layer in one transfer direction."""
94	    train_y = train_data["train_y"].numpy()
95	    test_y = test_data["test_y"].numpy()
96	    n_test = len(test_y)
97	
98	    results = []
99	    best_acc, best_layer = 0.0, 0
100	
101	    for layer in range(num_layers):
102	        train_X = train_data["train_X"][:, layer, :].numpy()
103	        test_X = test_data["test_X"][:, layer, :].numpy()
104	
105	        acc = train_and_eval(train_X, train_y, test_X, test_y)
106	        p_binom = binomial_p(acc, n_test)
107	
108	        results.append({
109	            "layer": layer,
110	            "accuracy": round(acc, 4),
111	            "p_binomial": round(p_binom, 6),
112	        })
113	
114	        if acc > best_acc:
115	            best_acc = acc
116	            best_layer = layer
117	
118	    # Permutation test on best layer
119	    if run_permutation:
120	        print(f"  Running permutation test on best layer {best_layer} (acc={best_acc:.4f})...")
121	        train_X_best = train_data["train_X"][:, best_layer, :].numpy()
122	        test_X_best = test_data["test_X"][:, best_layer, :].numpy()
123	        p_perm = permutation_test(train_X_best, train_y, test_X_best, test_y, best_acc)
124	        for r in results:
125	            r["p_permutation"] = None
126	        results[best_layer]["p_permutation"] = round(p_perm, 4)
127	    else:
128	        for r in results:
129	            r["p_permutation"] = None
130	
131	    return results
132	
133	
134	def print_table(all_results: dict[str, list[dict]], num_layers: int):
135	    """Print a concise per-layer accuracy table."""
136	    header = f"{'Layer':>5}"
137	    for d in DIRECTIONS:
138	        header += f"  {d:>10}"
139	    print(header)
140	    print("-" * len(header))
141	
142	    for layer in range(num_layers):
143	        row = f"{layer:>5}"
144	        for d in DIRECTIONS:
145	            if d in all_results:
146	                acc = all_results[d][layer]["accuracy"]
147	                row += f"  {acc:>10.4f}"
148	            else:
149	                row += f"  {'—':>10}"
150	        print(row)
151	
152	
153	def plot_results(all_results: dict[str, list[dict]], num_layers: int, output_path: str):
154	    """Plot accuracy by layer for each direction."""
155	    fig, ax = plt.subplots(figsize=(10, 5))
156	    colors = {"EN→EN": "#1f77b4", "ZH→ZH": "#ff7f0e", "EN→ZH": "#2ca02c", "ZH→EN": "#d62728"}
157	
158	    for direction, results in all_results.items():
159	        layers = [r["layer"] for r in results]
160	        accs = [r["accuracy"] for r in results]
161	        ax.plot(layers, accs, label=direction, color=colors.get(direction, None), linewidth=1.5)
162	
163	    ax.axhline(y=0.5, color="gray", linestyle="--", linewidth=1, label="Chance (50%)")
164	    ax.set_xlabel("Layer")
165	    ax.set_ylabel("Accuracy")
166	    ax.set_title("Linear Probe Accuracy by Layer")
167	    ax.legend()
168	    ax.set_xlim(0, num_layers - 1)
169	    ax.set_ylim(0.3, 1.0)
170	    fig.tight_layout()
171	    fig.savefig(output_path, dpi=150)
172	    plt.close(fig)
173	    print(f"Saved plot to {output_path}")
174	
175	
176	def main():
177	    parser = argparse.ArgumentParser(description="Train linear probes on residual stream activations")
178	    parser.add_argument("--activation_dir", type=str, default="outputs")
179	    parser.add_argument("--output_dir", type=str, default="outputs")
180	    parser.add_argument("--n_perm", type=int, default=1000, help="Number of permutation test iterations")
181	    parser.add_argument("--skip_permutation", action="store_true", help="Skip slow permutation test")
182	    args = parser.parse_args()
183	
184	    en_path = Path(args.activation_dir) / "en_activations.pt"
185	    zh_path = Path(args.activation_dir) / "zh_activations.pt"
186	
187	    has_en = en_path.exists()
188	    has_zh = zh_path.exists()
189	
190	    if not has_en and not has_zh:
191	        raise FileNotFoundError(f"No activation files found in {args.activation_dir}")
192	
193	    en_data = load_activations(str(en_path)) if has_en else None
194	    zh_data = load_activations(str(zh_path)) if has_zh else None
195	
196	    if has_en:
197	        num_layers = en_data["train_X"].shape[1]
198	    else:
199	        num_layers = zh_data["train_X"].shape[1]
200	    print(f"Number of layers: {num_layers}")
201	
202	    run_perm = not args.skip_permutation
203	    all_results: dict[str, list[dict]] = {}
204	
205	    if has_en:
206	        print("\n[EN→EN] Training probes...")
207	        all_results["EN→EN"] = run_direction(en_data, en_data, num_layers, "EN→EN", run_perm)
208	
209	    if has_zh:
210	        print("\n[ZH→ZH] Training probes...")
211	        all_results["ZH→ZH"] = run_direction(zh_data, zh_data, num_layers, "ZH→ZH", run_perm)
212	
213	    if has_en and has_zh:
214	        print("\n[EN→ZH] Training EN probes, testing on ZH...")
215	        all_results["EN→ZH"] = run_direction(en_data, zh_data, num_layers, "EN→ZH", run_perm)
216	
217	        print("\n[ZH→EN] Training ZH probes, testing on EN...")
218	        all_results["ZH→EN"] = run_direction(zh_data, en_data, num_layers, "ZH→EN", run_perm)
219	
220	    # Print table
221	    print("\n" + "=" * 60)
222	    print("Probe Accuracy by Layer")
223	    print("=" * 60)
224	    print_table(all_results, num_layers)
225	
226	    # Summary: best layer per direction
227	    print("\n--- Best layers ---")
228	    summary = {}
229	    for direction, results in all_results.items():
230	        best = max(results, key=lambda r: r["accuracy"])
231	        p_str = ""
232	        if best["p_permutation"] is not None:
233	            p_str = f", perm_p={best['p_permutation']}"
234	        print(f"  {direction}: layer {best['layer']}, acc={best['accuracy']:.4f}, "
235	              f"binom_p={best['p_binomial']:.6f}{p_str}")
236	        summary[direction] = {
237	            "best_layer": best["layer"],
238	            "best_accuracy": best["accuracy"],
239	            "p_binomial": best["p_binomial"],
240	            "p_permutation": best["p_permutation"],
241	        }
242	
243	    # Save JSON
244	    output = {
245	        "per_layer": {d: results for d, results in all_results.items()},
246	        "summary": summary,
247	        "num_layers": num_layers,
248	    }
249	    json_path = Path(args.output_dir) / "probe_results.json"
250	    with open(json_path, "w") as f:
251	        json.dump(output, f, indent=2)
252	    print(f"\nSaved results to {json_path}")
253	
254	    # Plot
255	    plot_path = Path(args.output_dir) / "probe_accuracy_by_layer.png"
256	    plot_results(all_results, num_layers, str(plot_path))
257	
258	
259	if __name__ == "__main__":
260	    main()
261	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a831b117-3af4-4143-8e47-5b074ecab1a7",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "04fc2c17-f233-403f-a12a-e31d52cc27bb",
  "sourceToolAssistantUUID": "a831b117-3af4-4143-8e47-5b074ecab1a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-22T03:12:49.010Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HePXCDgATrXVi548Yt6PKA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/clkc_code/src/collect_activations.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04fc2c17-f233-403f-a12a-e31d52cc27bb",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGson6ni44tn6MW3bxSr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f5de54e-7503-44d9-a908-5b02026ae3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V71eX2YipfjQaXvM7f9jQx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4757,
      "cache_read_input_tokens": 79281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4757,
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

_source line 47 · 2026-05-22T03:12:49.016Z_

<details><summary>↩ Tool result · `toolu_01HePXCDgATrXVi548Yt6PKA`</summary>

```text
1	"""Collect residual stream activations from all transformer layers.
2	
3	Loads a causal LM, feeds each sample's (question + context) prompt through
4	the model, hooks every layer's output, and saves the last-token hidden state
5	per layer.
6	
7	Input:  JSONL files in --data_dir  (e.g. en_conflict_train.jsonl)
8	Output: {lang}_activations.pt  containing:
9	        - "activations": Tensor (N, num_layers, hidden_dim)
10	        - "labels":      Tensor (N,)  (0 = no_conflict, 1 = conflict)
11	        - "split_sizes": dict {"train": int, "test": int}
12	
13	Dependencies: torch, transformers
14	"""
15	
16	import argparse
17	import json
18	import os
19	from pathlib import Path
20	
21	import torch
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	
24	
25	LABEL_MAP = {"no_conflict": 0, "conflict": 1}
26	
27	
28	def load_jsonl(path: str) -> list[dict]:
29	    with open(path) as f:
30	        return [json.loads(line) for line in f]
31	
32	
33	def build_prompt(sample: dict) -> str:
34	    """Build a simple QA prompt with context."""
35	    return (
36	        f"Context: {sample['context']}\n"
37	        f"Question: {sample['question']}\n"
38	        f"Answer:"
39	    )
40	
41	
42	def collect(
43	    model,
44	    tokenizer,
45	    samples: list[dict],
46	    batch_size: int,
47	    device: str,
48	) -> tuple[torch.Tensor, torch.Tensor]:
49	    """Return (activations [N, L, D], labels [N])."""
50	
51	    num_layers = model.config.num_hidden_layers
52	    all_activations = []
53	    all_labels = []
54	
55	    for start in range(0, len(samples), batch_size):
56	        batch = samples[start : start + batch_size]
57	        prompts = [build_prompt(s) for s in batch]
58	        labels = [LABEL_MAP[s["label"]] for s in batch]
59	
60	        inputs = tokenizer(
61	            prompts,
62	            return_tensors="pt",
63	            padding=True,
64	            truncation=True,
65	            max_length=512,
66	        ).to(device)
67	
68	        layer_outputs: dict[int, torch.Tensor] = {}
69	        hooks = []
70	
71	        def make_hook(layer_idx):
72	            def hook_fn(module, input, output):
73	                # output is a tuple; first element is the hidden state
74	                hidden = output[0]  # (B, seq_len, D)
75	                layer_outputs[layer_idx] = hidden.detach()
76	            return hook_fn
77	
78	        for idx, layer in enumerate(model.model.layers):
79	            hooks.append(layer.register_forward_hook(make_hook(idx)))
80	
81	        with torch.no_grad():
82	            model(**inputs)
83	
84	        for h in hooks:
85	            h.remove()
86	
87	        # Extract last non-padding token activation per sample
88	        seq_lengths = inputs["attention_mask"].sum(dim=1)  # (B,)
89	        batch_acts = []
90	        for i in range(len(batch)):
91	            last_pos = seq_lengths[i].item() - 1
92	            sample_layers = []
93	            for l in range(num_layers):
94	                sample_layers.append(layer_outputs[l][i, last_pos, :].cpu())
95	            batch_acts.append(torch.stack(sample_layers))  # (L, D)
96	
97	        all_activations.extend(batch_acts)
98	        all_labels.extend(labels)
99	
100	        print(f"  Processed {min(start + batch_size, len(samples))}/{len(samples)} samples")
101	
102	    activations = torch.stack(all_activations)  # (N, L, D)
103	    labels = torch.tensor(all_labels, dtype=torch.long)
104	    return activations, labels
105	
106	
107	def main():
108	    parser = argparse.ArgumentParser(description="Collect residual stream activations")
109	    parser.add_argument("--model", type=str, default="Qwen/Qwen3-8B-Instruct")
110	    parser.add_argument("--data_dir", type=str, default="data")
111	    parser.add_argument("--output_dir", type=str, default="outputs")
112	    parser.add_argument("--lang", type=str, default="en", choices=["en", "zh"])
113	    parser.add_argument("--batch_size", type=int, default=4)
114	    parser.add_argument("--train_file", type=str, default=None,
115	                        help="Override train JSONL path (ignores --lang/--data_dir)")
116	    parser.add_argument("--test_file", type=str, default=None,
117	                        help="Override test JSONL path (ignores --lang/--data_dir)")
118	    args = parser.parse_args()
119	
120	    if args.train_file and args.test_file:
121	        train_path = Path(args.train_file)
122	        test_path = Path(args.test_file)
123	    else:
124	        suffix = "verified" if args.lang == "en" else "validated"
125	        train_path = Path(args.data_dir) / f"{args.lang}_conflict_train_{suffix}.jsonl"
126	        test_path = Path(args.data_dir) / f"{args.lang}_conflict_test_{suffix}.jsonl"
127	
128	    if not train_path.exists():
129	        raise FileNotFoundError(f"Train file not found: {train_path}")
130	    if not test_path.exists():
131	        raise FileNotFoundError(f"Test file not found: {test_path}")
132	
133	    train_data = load_jsonl(str(train_path))
134	    test_data = load_jsonl(str(test_path))
135	    print(f"[{args.lang}] Loaded {len(train_data)} train + {len(test_data)} test samples")
136	
137	    print(f"Loading model: {args.model}")
138	    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
139	    if tokenizer.pad_token is None:
140	        tokenizer.pad_token = tokenizer.eos_token
141	    tokenizer.padding_side = "left"
142	
143	    model = AutoModelForCausalLM.from_pretrained(
144	        args.model,
145	        torch_dtype=torch.bfloat16,
146	        device_map="auto",
147	        trust_remote_code=True,
148	    )
149	    model.eval()
150	    device = next(model.parameters()).device
151	    print(f"Model loaded on {device}, layers={model.config.num_hidden_layers}, "
152	          f"hidden_dim={model.config.hidden_size}")
153	
154	    all_samples = train_data + test_data
155	
156	    print(f"Collecting activations for {len(all_samples)} samples...")
157	    activations, labels = collect(model, tokenizer, all_samples, args.batch_size, device)
158	
159	    os.makedirs(args.output_dir, exist_ok=True)
160	    out_path = Path(args.output_dir) / f"{args.lang}_activations.pt"
161	    torch.save(
162	        {
163	            "activations": activations,
164	            "labels": labels,
165	            "split_sizes": {"train": len(train_data), "test": len(test_data)},
166	        },
167	        out_path,
168	    )
169	    print(f"Saved activations to {out_path}  shape={activations.shape}")
170	
171	
172	if __name__ == "__main__":
173	    main()
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f5de54e-7503-44d9-a908-5b02026ae3dd",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "01cf8363-a5e0-4e77-a66d-feed7a59ae37",
  "sourceToolAssistantUUID": "7f5de54e-7503-44d9-a908-5b02026ae3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-22T03:12:52.650Z_

Now let me check the literature map for relevant cited works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01cf8363-a5e0-4e77-a66d-feed7a59ae37",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsp5XncxwiLwpzCpmVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fd62a31-df90-4731-a573-79a9f904af55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fi8i4bsZEpQy8cAxAr7anr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 84038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6015,
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

_source line 49 · 2026-05-22T03:12:53.756Z_

<details open><summary>🔧 Tool call — Read · `toolu_014AVrMh5Gz8Gvq1oDxjjxhm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fd62a31-df90-4731-a573-79a9f904af55",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsp5XncxwiLwpzCpmVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "635ddf52-2b91-46b8-b928-1385a8f4964c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fi8i4bsZEpQy8cAxAr7anr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 84038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6015,
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

_source line 50 · 2026-05-22T03:12:53.762Z_

<details><summary>↩ Tool result · `toolu_014AVrMh5Gz8Gvq1oDxjjxhm`</summary>

```text
1	meta:
2	  last_updated: '2026-05-21T12:04:50.276Z'
3	  total_papers: 10
4	categories: []
5	papers:
6	  zhao2026when:
7	    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'
8	    authors:
9	    - Zhao, J.
10	    - et al.
11	    year: 2026
12	    venue: arXiv
13	    url: https://arxiv.org/abs/2601.07041
14	    doi: ''
15	    bibtex_key: zhao2026when
16	    category: cross-lingual-conflict
17	    role: direct-competitor
18	    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral
19	      finding that linguistic similarity governs entity-centric conflict resolution.
20	      Our work provides mechanistic explanation.'
21	    abstract: ''
22	    semantic_scholar_id: ''
23	    verified: true
24	    added_by: director-bootstrap
25	    added_at: '2026-05-21T12:04:50.273Z'
26	  zhao2025steering:
27	    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation
28	      Engineering
29	    authors:
30	    - Zhao, Y.
31	    - Devoto, A.
32	    - Hong, G.
33	    - et al.
34	    year: 2025
35	    venue: NAACL 2025 Oral
36	    url: https://arxiv.org/abs/2410.15999
37	    doi: ''
38	    bibtex_key: zhao2025steering
39	    category: sae-steering
40	    role: direct-competitor
41	    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology
42	      we extend to cross-lingual setting. MI-based feature selection, constraint-aware
43	      activation editing.'
44	    abstract: ''
45	    semantic_scholar_id: ''
46	    verified: true
47	    added_by: director-bootstrap
48	    added_at: '2026-05-21T12:04:50.273Z'
49	  boer2026probing:
50	    title: Probing for Knowledge Attribution in Large Language Models
51	    authors:
52	    - Boer, A.
53	    - Brink, I.
54	    - Ulmer, D.
55	    year: 2026
56	    venue: arXiv
57	    url: https://arxiv.org/abs/2602.22787
58	    doi: ''
59	    bibtex_key: boer2026probing
60	    category: probing
61	    role: direct-competitor
62	    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.
63	      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99
64	      F1.
65	    abstract: ''
66	    semantic_scholar_id: ''
67	    verified: true
68	    added_by: director-bootstrap
69	    added_at: '2026-05-21T12:04:50.273Z'
70	  kialy2026universal:
71	    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register
72	      with SAEs
73	    authors:
74	    - Kialy, U.Z.
75	    - Shtarkberg, A.
76	    - Klein, A.
77	    year: 2026
78	    venue: arXiv
79	    url: https://arxiv.org/abs/2603.26236
80	    doi: ''
81	    bibtex_key: kialy2026universal
82	    category: cross-lingual-sae
83	    role: direct-competitor
84	    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core
85	      for register features + zero-shot steering transfer. We test whether this extends
86	      to knowledge conflict features.
87	    abstract: ''
88	    semantic_scholar_id: ''
89	    verified: true
90	    added_by: director-bootstrap
91	    added_at: '2026-05-21T12:04:50.273Z'
92	  wong2026langfir:
93	    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual
94	      Data for Language Steering'
95	    authors:
96	    - Wong, S.H.
97	    - Siddique, A.B.
98	    - Sajjad, H.
99	    year: 2026
100	    venue: arXiv
101	    url: https://arxiv.org/abs/2604.03532
102	    doi: ''
103	    bibtex_key: wong2026langfir
104	    category: cross-lingual-sae
105	    role: direct-competitor
106	    relevance: Random-token filtering isolates <5 language-specific SAE features/language.
107	      Our Track 2 uses this as control to disentangle language-identity from conflict
108	      features.
109	    abstract: ''
110	    semantic_scholar_id: ''
111	    verified: true
112	    added_by: director-bootstrap
113	    added_at: '2026-05-21T12:04:50.273Z'
114	  wang2025lost:
115	    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency
116	      in Transformer Language Models'
117	    authors:
118	    - Wang, M.
119	    - Adel, H.
120	    - Lange, L.
121	    - et al.
122	    year: 2025
123	    venue: ACL 2025 (SAC Highlights)
124	    url: https://arxiv.org/abs/2504.04264
125	    doi: ''
126	    bibtex_key: wang2025lost
127	    category: cross-lingual-mechanism
128	    role: foundation
129	    relevance: Language-independent concept space through most layers, language-specific
130	      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.
131	    abstract: ''
132	    semantic_scholar_id: ''
133	    verified: true
134	    added_by: director-bootstrap
135	    added_at: '2026-05-21T12:04:50.273Z'
136	  team2026qwen:
137	    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language
138	      Models'
139	    authors:
140	    - Qwen Team
141	    year: 2026
142	    venue: arXiv
143	    url: https://arxiv.org/abs/2605.11887
144	    doi: ''
145	    bibtex_key: team2026qwen
146	    category: sae-tools
147	    role: foundation
148	    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs
149	      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section
150	      5.2).
151	    abstract: ''
152	    semantic_scholar_id: ''
153	    verified: true
154	    added_by: director-bootstrap
155	    added_at: '2026-05-21T12:04:50.273Z'
156	  zhao2024analysing:
157	    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts
158	    authors:
159	    - Zhao, Y.
160	    - Du, X.
161	    - Hong, G.
162	    - et al.
163	    year: 2024
164	    venue: NeurIPS 2024 FMI Workshop
165	    url: https://arxiv.org/abs/2410.16090
166	    doi: ''
167	    bibtex_key: zhao2024analysing
168	    category: probing
169	    role: foundation
170	    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts
171	      in residual stream. Foundation for our Track 1 cross-lingual extension.'
172	    abstract: ''
173	    semantic_scholar_id: ''
174	    verified: true
175	    added_by: director-bootstrap
176	    added_at: '2026-05-21T12:04:50.273Z'
177	  pham2026where:
178	    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge
179	      Conflict in Language Models'
180	    authors:
181	    - Pham, M.V.
182	    - Borkakoty, H.
183	    - Hou, Y.
184	    year: 2026
185	    venue: arXiv
186	    url: https://arxiv.org/abs/2601.09445
187	    doi: ''
188	    bibtex_key: pham2026where
189	    category: conflict-mechanism
190	    role: direct-competitor
191	    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers
192	      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel
193	      for within-parametric conflicts.
194	    abstract: ''
195	    semantic_scholar_id: ''
196	    verified: true
197	    added_by: director-bootstrap
198	    added_at: '2026-05-21T12:04:50.273Z'
199	  basu2026interpretability:
200	    title: 'Interpretability without actionability: mechanistic methods cannot correct
201	      language model errors despite near-perfect internal representations'
202	    authors:
203	    - Basu, S.
204	    - et al.
205	    year: 2026
206	    venue: arXiv
207	    url: https://arxiv.org/abs/2603.18353
208	    doi: ''
209	    bibtex_key: basu2026interpretability
210	    category: sae-steering
211	    role: direct-competitor
212	    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.
213	      Critical negative result: defines boundary conditions for when SAE steering
214	      works. Our Track 3 design addresses their methodological gaps.'
215	    abstract: ''
216	    semantic_scholar_id: ''
217	    verified: true
218	    added_by: director-bootstrap
219	    added_at: '2026-05-21T12:04:50.273Z'
220	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "635ddf52-2b91-46b8-b928-1385a8f4964c",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "b99ee3cc-934e-4727-bbee-82c35820887a",
  "sourceToolAssistantUUID": "635ddf52-2b91-46b8-b928-1385a8f4964c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T03:12:54.064Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WkMpiD9xMYFo6YiaS3VJjk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/mistakes.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b99ee3cc-934e-4727-bbee-82c35820887a",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGsp5XncxwiLwpzCpmVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e274bff-ecb7-4965-88da-e1b5d351797b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fi8i4bsZEpQy8cAxAr7anr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6015,
      "cache_read_input_tokens": 84038,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6015
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 84038,
          "cache_creation_input_tokens": 6015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6015,
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

_source line 52 · 2026-05-22T03:12:54.070Z_

<details><summary>↩ Tool result · `toolu_01WkMpiD9xMYFo6YiaS3VJjk`</summary>

```text
1	_next_id: 12
2	mistakes:
3	- id: M001
4	  date: '2026-05-21'
5	  category: experiment_design
6	  severity: high
7	  summary: ConflictQA 标签基于 ChatGPT 参数知识，未适配目标模型 Qwen3-8B，导致标签可能反转
8	  root_cause: ConflictQA 的 conflict/no_conflict 标签是相对于 ChatGPT 的 memory_answer 定义的。直接用这些标签训练
9	    Qwen3-8B 的探针，忽略了两个模型参数知识可能不一致的事实。Director 在设计 MVP 数据方案时也未注意到这一点。
10	  prevention: 使用第三方 QA 数据集训练探针时，必须验证标签与目标模型的参数知识对齐。标准步骤：先对目标模型做 closed-book QA 验证，再根据目标模型的实际参数知识分配/过滤标签。Brink
11	    et al. (2026) 做了类似的预过滤。
12	  status: active
13	  context: ConflictQA 中 ChatGPT memory_answer 经常与 ground_truth 不一致（这是数据集设计目的）。预估约
14	    30% 样本标签需要修正。
15	  related_decisions:
16	  - D001
17	  - D002
18	- id: M002
19	  date: '2026-05-21'
20	  category: code_bug
21	  severity: low
22	  summary: verify_parametric_knowledge.py 字段名硬编码为 qwen_，多模型场景下造成混淆
23	  root_cause: 脚本最初只为 Qwen 设计，字段名写死为 qwen_parametric_answer / qwen_agrees_with。扩展到
24	    Llama 时未更新字段名，导致 Reviewer 无法确认实际使用的模型。
25	  prevention: 多模型实验的脚本从一开始就用通用字段名（model_parametric_answer），并在输出中记录 model_used 元数据。代码审查时检查是否存在模型名硬编码。
26	  status: active
27	  fix: 字段名改为 model_parametric_answer / model_agrees_with，新增 model_used 字段。
28	- id: M003
29	  date: '2026-05-21'
30	  category: code_bug
31	  severity: medium
32	  summary: Pipeline 文件引用第三次未对齐——补采样生成 _full 文件但下游脚本仍引用原始文件名
33	  root_cause: 每次数据变更（verify 后缀、validated 后缀、full 后缀）都引入新文件名，但未统一更新所有下游脚本。根本原因是 pipeline
34	    中文件命名约定不一致，新建文件而非覆盖。
35	  prevention: 数据 pipeline 的文件命名策略应在设计时确定：要么统一用固定文件名（每步覆盖前备份），要么通过配置文件/命令行参数传递文件路径。避免每步产出新后缀名导致下游引用断裂。此次采用
36	    rename 覆盖方案统一解决。
37	  status: active
38	  fix: 采用 rename 方案：_full 文件覆盖原始文件名，原始数据备份到 original_500/ 目录。所有脚本零修改。
39	- id: M004
40	  date: '2026-05-21'
41	  category: code_bug
42	  severity: medium
43	  summary: collect_activations.py hook 假设 decoder output 是 tuple，Llama 返回 tensor 导致
44	    IndexError 崩溃
45	  root_cause: hook_fn 写死 output[0] 取 hidden_states，但不同模型/transformers 版本的 decoder
46	    layer output 格式不一致（有时是 tuple 有时是 tensor）
47	  prevention: hook_fn 中始终用 isinstance(output, tuple) 判断再取值。写 hook 时用两个以上模型做 smoke
48	    test（至少 dry-run 1 batch）
49	  status: active
50	  fix: 'hook_fn 改为: hidden = output[0] if isinstance(output, tuple) else output'
51	- id: M005
52	  date: '2026-05-21'
53	  category: code_bug
54	  severity: high
55	  summary: collect_activations.py 左 padding 时 last-token 位置计算错误，~75% 样本提取了 padding
56	    位置的激活
57	  root_cause: 代码用 attention_mask.sum()-1 计算 last token 位置，这对右 padding 正确但对左 padding
58	    完全错误。左 padding 时所有样本的 last token 固定在 max_seq_len-1
59	  prevention: 左 padding 时用 input_ids.shape[1]-1 取 last token。写激活提取代码时必须明确注释 padding
60	    方向并做 sanity check（打印几个样本的提取位置 vs 实际序列长度）
61	  status: active
62	  fix: last_pos = inputs["input_ids"].shape[1] - 1
63	- id: M006
64	  date: '2026-05-21'
65	  category: code_bug
66	  severity: high
67	  summary: Qwen3 verify 未正确剥离 think tags，77.4% 数据含思考链文本导致标签匹配错误
68	  root_cause: max_new_tokens=128 不够 Qwen3 think 块完成，截断后无配对 &lt;/think> 标签，正则匹配失败。think
69	    文本含正误答案导致 substring 匹配混乱
70	  prevention: 对 Qwen3 系列模型，verify/inference 时加 /no_think 或 enable_thinking=False 关闭思考模式。或
71	    max_new_tokens 设 2048+ 确保 think 块完整
72	  status: active
73	  fix: verify 时使用 enable_thinking=False 或增大 max_new_tokens 到 2048
74	- id: M007
75	  date: '2026-05-21'
76	  category: code_bug
77	  severity: high
78	  summary: bootstrap_asymmetry.py 未使用 StandardScaler，与 train_probe.py 预处理不一致导致 CI
79	    无效
80	  root_cause: 新脚本从零编写时未复制 train_probe.py 的完整预处理 pipeline（StandardScaler），只复制了模型训练部分
81	  prevention: 新分析脚本必须复用或导入已有 pipeline 的预处理步骤，不要从零重写。或将 StandardScaler + LogisticRegression
82	    封装成共享函数供所有脚本调用
83	  status: active
84	  fix: 在 bootstrap resampling loop 内加 StandardScaler().fit_transform/transform
85	- id: M008
86	  date: '2026-05-21'
87	  category: experiment_design
88	  severity: medium
89	  summary: Multi-seed 实验无效：lbfgs solver 是确定性的，改 random_state 不改变结果，5 个 seed 给出 std=0
90	  root_cause: 误以为 sklearn LogisticRegression 的 random_state 影响所有 solver，实际只对 sag/saga/liblinear
91	    有效。lbfgs 给定相同数据 + 超参 = 确定性结果
92	  prevention: multi-seed 实验要通过变化训练数据（Bootstrap resampling 或 K-Fold）实现，不能只改 solver
93	    seed。确定性算法跑 N 次 = 浪费 N-1 次
94	  status: active
95	  fix: 改用 Bootstrap training data（有放回抽样）或 StratifiedKFold 交叉验证
96	- id: M009
97	  date: '2026-05-21'
98	  category: agent_behavior
99	  severity: medium
100	  summary: COMET 进程被 submit_training_job 默认 timeout 杀死（EXIT_CODE=124），丢失 340/320 条已完成的回译
101	  root_cause: submit_training_job 有默认 timeout，COMET 回译 ~1000 条每条 ~10s 需要 ~3h，超过默认限制。且首次启动时缺少
102	    TRANSFORMERS_OFFLINE=1，COMET 尝试联网下载模型失败
103	  prevention: 长时间任务（>1h）用 nohup 直接启动或设置足够大的 timeout_hours。COMET 等需要预训练模型的工具加 TRANSFORMERS_OFFLINE=1
104	    避免联网依赖
105	  status: active
106	  fix: 用 nohup 直接启动 COMET 绕过 timeout 限制，加 TRANSFORMERS_OFFLINE=1
107	- id: M010
108	  date: '2026-05-22'
109	  category: agent_behavior
110	  severity: medium
111	  summary: Gemma-2-9B-IT 下载中断，仅完成 11%，Worker 未检测到截断
112	  root_cause: AutoDL 上 HF 直接下载大模型极慢且不稳定，SSH 超时或网络中断导致下载中断。Worker 汇报"已完成"但未验证模型权重完整性。
113	  prevention: 1. AutoDL 大模型下载优先用 ModelScope CDN 或 HF mirror (hf-mirror.com)；2. 下载前先
114	    source /etc/network_turbo；3. 下载后必须验证：检查文件大小或加载模型确认 num_parameters；4. 用 nohup 后台执行避免
115	    SSH 超时
116	  status: active
117	  fix: 清除截断文件，用 ModelScope 或 HF mirror 重新下载
118	- id: M011
119	  date: '2026-05-22'
120	  category: resource_misuse
121	  severity: medium
122	  summary: COMET 第三次被 EXIT_CODE=124 timeout 杀死——旧 tmux 监控进程未清理
123	  root_cause: 之前用 submit_training_job 启动 COMET 时创建的 tmux 监控会话仍在运行，wall_clock 达 6.1h
124	    后触发 timeout 杀掉进程。即使后来改用 nohup 直接启动，旧的 tmux 监控仍可能干扰。
125	  prevention: 1. 用 nohup 直接启动长任务后，必须清理同一 GPU 上的旧 tmux 监控会话（tmux kill-session）；2. 启动前先
126	    tmux ls 检查是否有残留监控；3. 长任务彻底绕过 submit_training_job 体系，不要混用两种启动方式
127	  status: active
128	  fix: Worker 正在诊断部分结果和重启
129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e274bff-ecb7-4965-88da-e1b5d351797b",
  "isSidechain": true,
  "promptId": "133af9b4-7c02-4615-ba12-0c22f2e1e9b6",
  "agentId": "ac3a661244be2fc26",
  "type": "user",
  "uuid": "e8cc2789-1b0c-4817-b561-a89ed7c6444b",
  "sourceToolAssistantUUID": "5e274bff-ecb7-4965-88da-e1b5d351797b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-22T03:14:43.710Z_

I now have a thorough understanding of the paper, the experimental infrastructure, the actual completed experiments vs. imagined experiments, and the known issues. Let me compile the review.

---

## ACL ARR Review -- Reviewer 1 (R1): Methods and Experiments

### Paper: "Cross-Lingual Conflict Detection in Multilingual LLMs: Mechanistic Evidence for English-Anchored Representations"

---

### Summary

This paper investigates how cross-lingual knowledge conflict signals are encoded in the residual stream of multilingual transformers. Using three analysis tracks -- linear/MLP probing (Track 1), SAE feature decomposition (Track 2), and causal representation steering (Track 3) -- the authors analyze three dense transformer architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) across two language pairs (EN--ZH, EN--JA). The central claim is that conflict detection is encoded in a language-universal mid-layer representation anchored to English, with language-specific processing emerging during late-layer transition. Evidence includes: 70--77% within-language probe accuracy, a consistent 6.3--7.9pp directional asymmetry favoring X->EN over EN->X transfer, SAE features showing mid-layer cross-lingual sharing (Jaccard=0.28) that decays in late layers (Jaccard=0.12), and steering flip rates of 17--35% that reproduce the same asymmetry pattern.

---

### Strengths

**S1. Well-structured hypothesis-driven design.** The H1 vs. H2 framing is commendable. Rather than reporting a collection of exploratory findings, the paper derives specific, falsifiable predictions from each hypothesis (mid-layer Jaccard > late-layer Jaccard for H1; directional consistency across language pairs) and systematically tests them. This is good scientific practice rarely seen in interpretability papers.

**S2. Three-track converging evidence.** The detection (probing) -> decomposition (SAE) -> intervention (steering) pipeline provides increasingly strong evidence for the claims. The steering experiments are particularly valuable because they move beyond correlational probing to causal manipulation. The fact that steering flip rate asymmetry mirrors the probe transfer asymmetry (Section 4.5, Tables 6 and 7) is the paper's strongest methodological contribution.

**S3. Systematic confound controls.** The COMET tercile ablation (Table 1) is well-designed: rather than applying an arbitrary COMET threshold, the authors empirically test whether translation quality correlates with probe accuracy and find a null/reversed relationship. The token overlap analysis (Jaccard 3-4%, negative correlation in Llama) is similarly careful. The label noise ablation establishes safety margins relative to the verification pipeline's estimated error rate.

**S4. Cross-architecture consistency.** Testing three architectures and finding a coefficient of variation below 6% for the asymmetry gap (7.2/7.2/7.9pp) is notable. The MLP non-linearity gradient anti-correlating with Chinese pre-training proportion (Table 3: Qwen +2.3pp, Llama +4.7pp, Gemma +6.1pp) is a clean finding that connects model training characteristics to mechanistic behavior.

**S5. Appropriate statistical methodology.** Permutation tests (n=1000) are appropriate for the non-parametric setting. The use of balanced accuracy rather than raw accuracy is correct given the potential for class imbalance. The 5-fold stratified cross-validation is standard and appropriate.

---

### Weaknesses

**W1 (Major). The paper is a "dream report" -- all experimental results beyond the MVP are imagined, not executed.**

This is the single most critical issue. Cross-referencing the paper's tables against the project's actual experimental state reveals a fundamental disconnect:

- The ROADMAP.md shows only 2 experiments completed (`mvp_probe_v1`, `mvp_probe_llama_v1`), both on EN--ZH only, both on Llama-3.1-8B and Qwen3-8B only.
- The experiment_plan.yaml shows all Post-MVP experiments (plan_102 through plan_303) in `planned` status, not `done`.
- The `review_context.yaml` and `imagined_experiments.yaml` files explicitly describe these as imagined results in a "best tier" scenario.
- The Gemma-2-9B-IT results (Table 2, row 3) are imagined -- the model download was interrupted at 11% (mistakes.yaml M010).
- All EN--JA results (Table 4) are imagined -- plan_103 is `planned`.
- All SAE results (Tables 5, 6, 7, 8, 9) are imagined -- plan_201/202/203/301/302/303 are all `planned`.
- All steering results (Tables 6, 7, 8) are imagined -- plan_107/301/302 are all `planned`.
- The CKA/SVCCA results (Table 5) are imagined -- plan_104 is `planned`.
- The larger dataset validation (Table 10) is imagined -- plan_108 is `planned`.
- Even the COMET results for Llama are still running (`comet_llama_v6` in report.md).

Only the core 2-model EN--ZH probe results and the Qwen COMET tercile ablation have been actually executed. Everything else in this paper is speculative. **As a reviewer, I cannot evaluate the soundness of experiments that have not been run.** The numbers could turn out quite differently in practice. The paper should be resubmitted when the experiments are actually completed.

**W2 (Major). Bootstrap n=100 is insufficient for reliable 95% CIs.**

The standard recommendation for bootstrap CIs is n >= 1000 (Efron & Tibshirani, 1993; DiCiccio & Efron, 1996). At n=100, the 2.5th and 97.5th percentiles of the bootstrap distribution correspond to the 2nd and 3rd most extreme values, making CI endpoints highly sensitive to individual bootstrap samples. This is particularly concerning because:

- The Qwen CI at N~1000 brackets zero ([-1.2, 13.4]), and the paper interprets this as "trending" rather than non-significant. With n=100 bootstrap, the lower CI bound could easily shift by 2-3pp either way.
- The paper claims "98/100 iterations positive" for Llama and "96/100 iterations positive" for Qwen. These counts have binomial SE of ~1.4% and ~2.0% respectively, which is non-negligible.
- The asymmetry gap is the paper's central quantitative claim. Using only 100 bootstrap iterations for the key statistical test undermines confidence in the precise CI bounds reported.

The authors should increase to n >= 2000 bootstrap iterations. This is computationally cheap given that each iteration only retrains a logistic regression probe.

**W3 (Major). SAE analysis on base model vs. probing on instruct-tuned models.**

The paper applies Qwen-Scope SAEs (trained on Qwen3-8B-Base) for Track 2 while using instruct-tuned models for Track 1 probing. The paper acknowledges this (Limitations paragraph 3) but dismisses it too quickly with "cross-validation between tracks partially mitigates." This mismatch is more serious than acknowledged because:

- RLHF/instruction tuning substantially reorganizes representations, particularly in layers where the paper claims critical conflict processing occurs (mid-to-late layers). Anthropic's own work on monosemanticity notes that SAE features identified in base models may not correspond to the same features in fine-tuned versions.
- The Jaccard analysis (Table 7) measures feature overlap in the SAE's native feature space on the base model. Applying these same features to explain instruct-model probe behavior is a logical gap.
- The steering experiments (Tables 6-9) -- if they were actually run -- would need to be performed on the same model the SAE was trained on (base) OR the paper needs to demonstrate that SAE features transfer meaningfully to the instruct model. Neither is done.

**W4 (Moderate). Probe accuracy of 70-77% is substantially below prior work and limits interpretive claims.**

Boer et al. (2026) achieve 0.96 Macro-F1 for monolingual conflict attribution probing. The 70-77% balanced accuracy reported here represents a meaningful gap. The paper does not adequately explain this gap. Possible explanations include: (a) the cross-lingual setting is inherently harder, (b) the ConflictQA verification pipeline introduces noise, (c) the conflict signal in these models is genuinely weaker. The paper should distinguish between these possibilities because they have different implications for the strength of claims. If (c), the "conflict detection is encoded in a language-universal representation" claim is only partially supported -- it may be that only a fraction of conflict information is language-universal while a large portion is encoded in ways the linear probe cannot capture.

**W5 (Moderate). Steering captures only 17-35% of samples, leaving the majority of the mechanism unexplained.**

The flip rates of 17-35% mean that 65-83% of samples are not affected by the intervention. While the paper correctly notes these rates are 3.4-6.5x above random baseline, the absolute magnitude raises questions about what fraction of the conflict resolution mechanism is captured by the linear/sparse approximation. The paper would benefit from an analysis of *which* samples flip and which do not -- are the non-flipping samples systematically different (e.g., higher confidence, particular topic domains)?

**W6 (Moderate). Only two language pairs, both Asian, tested.**

Both EN--ZH and EN--JA are CJK languages with shared cultural context. The "English-anchored" hypothesis would be much more convincing with at least one typologically distant Indo-European language (e.g., EN--DE or EN--FR) where the English anchoring might behave differently due to shared script and morphological similarity. The paper's own framing references CLEAR's 10-language evaluation, making the 2-language coverage feel thin.

**W7 (Minor). No train/test accuracy gap analysis for MLP probes.**

The paper notes MLP probes achieve +2.3 to +6.1pp gains in the weak transfer direction (Table 3) but does not report train accuracy for MLP probes. With a single hidden layer of 256 units operating on ~1000 samples with dimensionality 3584-4096, there is a real risk of overfitting. The paper states "MLP probes (single hidden layer, 256 units) are trained with identical splits to quantify non-linear components" but does not mention regularization (dropout, weight decay). A train/test accuracy comparison is needed to rule out that the MLP gain is simply memorization.

**W8 (Minor). The Jaccard permutation test p=0.008 is based on very small feature counts.**

The mid-layer Jaccard of 0.28 comes from 8 shared features out of 21 EN and 18 ZH features (Table 7). The late-layer Jaccard of 0.12 comes from 3 shared features out of 14 EN and 10 ZH features. With such small counts, a single feature being reclassified between layers could meaningfully shift the Jaccard index. While p=0.008 passes conventional thresholds, the practical robustness of this finding to feature selection thresholds should be tested via sensitivity analysis.

---

### Questions for Authors

**Q1.** Can you confirm which experimental results in the paper have been actually executed vs. projected from the "dream report" pipeline? The discrepancy between the experiment tracking system and the paper is concerning.

**Q2.** Why was bootstrap n set to 100 rather than the conventional 1000+? Was this a computational constraint? Given that each bootstrap iteration is a logistic regression fit, this seems unnecessarily conservative.

**Q3.** For the COMET tercile ablation (Table 1), the Qwen tercile sizes are only 56 samples each. Have you computed the statistical power of Fisher's exact test at this sample size to detect a meaningful accuracy difference (say, 10pp)?

**Q4.** The paper reports "coherence is preserved at 91%" for probe-based steering (Section 4.5). How is coherence measured? Is this human evaluation, automated metric, or perplexity-based?

**Q5.** In the feature-set ablation (Table 9), "shared features alone achieve 28.0% cross-lingual flip rate" vs. EN-only 11.0% and ZH-only 9.0%. Have you verified that this difference is not simply due to shared features being at more causally effective layers (mid-layers) while language-specific features skew late (Table 6)?

**Q6.** The MLP non-linearity gradient (Qwen 2.3pp < Llama 4.7pp < Gemma 6.1pp) is interpreted as anti-correlating with Chinese pre-training proportion. But Table 3 shows Gemma at 6.1pp, which is *higher* than Llama at 4.7pp. Yet Gemma is from Google (strong multilingual training). What evidence do you have about the relative Chinese data proportions in these three models' training sets?

**Q7.** The token overlap analysis found Llama has a *negative* correlation (r=-0.15, p=0.012) between token overlap and probe accuracy. This is unexpected and warrants explanation. Why would higher token overlap *reduce* accuracy?

---

### Minor Issues

1. **Table 2**: "Sig." column uses "Yes"/"No (trend)" -- a binary significance judgment is more appropriate for a methods paper. The "trend" language invites selective interpretation. Report the CI and let readers judge.

2. **Section 3.1**: "We obtain model responses in English (EN) and generate high-quality translations in Chinese (ZH) and Japanese (JA) using the target models themselves." Using the same model for translation and as the probe target introduces a potential circularity -- the model's own biases in translation could systematically affect the conflict patterns in the translated text.

3. **References**: Only 8 references cited in the paper. For an ACL submission, this is thin. Key missing references include: the original ConflictQA paper's full citation (Xie et al., 2024 is cited but only in references, not in the methods section where the dataset is described), Belinkov (2022) for probing methodology best practices, and Raghu et al. (2017) for SVCCA.

4. **Reproducibility**: The paper does not mention random seeds, hyperparameter selection for L2 regularization in logistic regression, or the steering alpha search range/granularity.

5. **Section 4.3**: "The probe accuracy peak correlates negatively with the CKA transition point (r = -0.71)" -- with only 3 data points (one per model), this correlation is not meaningful and should not be reported as if it were a statistical finding.

6. The paper uses "balanced accuracy" throughout but the actual implementation in `train_probe.py` uses `clf.score()`, which returns raw accuracy, not balanced accuracy. This is a discrepancy between the paper's claims and the code.

---

### Preliminary Scores

- **Soundness**: 2/5 -- The fundamental issue is that the vast majority of reported results are imagined rather than actually executed. The statistical methodology for the actually-completed experiments is generally appropriate but has the n=100 bootstrap weakness. The base/instruct SAE mismatch is inadequately addressed.

- **Overall Assessment**: 2.0/5 (Reject) -- The paper presents an ambitious and well-structured research program with a clean hypothesis-driven design. However, the results as presented are largely speculative projections from a "dream report" pipeline rather than actual experimental outcomes. Only the 2-model EN--ZH probe experiments and partial COMET validation have been completed. This paper should be resubmitted once the experiments are actually executed, as the results could differ substantially from projections. If all experiments were genuinely completed and the numbers held, this would be a solid 3.5-4.0 paper. The three-track converging evidence design is strong, the confound controls are thorough, and the hypothesis framework is clean. But science requires actual data.

**Confidence**: 4/5 -- I have high confidence in this assessment. I cross-referenced the paper's claims against the project's experiment tracking system, source code, and decision logs, which clearly distinguish completed from planned experiments.

---

### Actionable Recommendations for Revision

1. Execute all planned experiments and resubmit with actual results.
2. Increase bootstrap iterations to n >= 2000.
3. Address the base/instruct SAE mismatch by either running SAE analysis on instruct models or providing transfer validation.
4. Add at least one non-CJK language pair (e.g., EN--DE).
5. Report MLP probe train/test accuracy gaps to rule out overfitting.
6. Fix the `clf.score()` vs. balanced accuracy discrepancy in the code.
7. Conduct sensitivity analysis on the SAE feature selection threshold and its impact on Jaccard indices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8cc2789-1b0c-4817-b561-a89ed7c6444b",
  "isSidechain": true,
  "agentId": "ac3a661244be2fc26",
  "requestId": "req_011CbGspSfX73r1gJyHXX441",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e90e7ba6-1f22-46c8-8d43-75413db22602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "d76881f3-8cf2-45f7-8657-e72190e5783a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019W5aGzbbaPjWVkM7514WtY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6301,
      "cache_read_input_tokens": 90053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6301,
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
